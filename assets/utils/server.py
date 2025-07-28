import asyncio
import contextlib
import json
import time
import uuid
from pathlib import Path
from typing import Any, Optional, AsyncIterator

import uvicorn
from huaweicloudsdkcore.exceptions.exceptions import ClientRequestException
from mcp.server import Server
from mcp.server.fastmcp.utilities.logging import configure_logging, get_logger
from mcp.server.sse import SseServerTransport
from mcp.server.stdio import stdio_server
from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route
from starlette.types import Receive, Scope, Send

from .hwc_tools import (
    create_api_client,
    build_http_info,
    load_openapi,
    filter_parameters,
    load_config,
)
from .model import TopResponseModel, MCPConfig
from .openapi import OpenAPIToToolsConverter
from .variable import TRANSPORT_SSE, TRANSPORT_HTTP

logger = get_logger(__name__)
configure_logging("INFO")


class MCPServer:
    def __init__(self, config_path: Path):
        self.config_path = config_path

        self.config: Optional[MCPConfig] = None
        self.server: Optional[Server] = None
        self.tools: list[Tool] = []
        self.initialized: bool = False
        self.openapi_dict: dict[str, Any] = {}

        self.active_clients: dict[str, Any] = {}
        self._clients_lock = asyncio.Lock()

        self.initialize()

    def initialize(self) -> None:
        """初始化服务器组件"""
        if self.initialized:
            return

        logger.info("开始初始化MCP服务器...")

        try:
            self.config = load_config(self.config_path)
            if not self.config:
                raise ValueError("无法加载服务器配置")

            self.server = Server(f"hwc-mcp-server-{self.config.service_code.lower()}")
            logger.info(
                f"初始化MCP服务器实例： hwc-mcp-server-{self.config.service_code.lower()}"
            )

            # 加载OpenAPI规范
            openapi_path = (
                Path(self.config_path.parent) / f"{self.config.service_code}.json"
            )
            self.openapi_dict = load_openapi(openapi_path)
            if not self.openapi_dict:
                raise ValueError(
                    f"加载OpenAPI文档失败，请检查{openapi_path}文档内容是否有误"
                )

            # 转换为MCP工具
            self.tools = OpenAPIToToolsConverter(self.openapi_dict).convert()
            logger.info(f"成功加载 {len(self.tools)} 个工具")

            # 注册工具处理函数
            self._register_tool_handlers()

            self.initialized = True
            logger.info("MCP服务器初始化完成")

        except Exception as e:
            logger.error(f"服务器初始化失败: {e}")
            raise

    async def register_client(self, client_id, request):
        async with self._clients_lock:
            self.active_clients[client_id] = {
                "request": request,
                "connected_at": time.time(),
            }
            logger.info(f"客户端注册成功: {client_id}")

    async def unregister_client(self, client_id):
        async with self._clients_lock:
            if client_id in self.active_clients:
                del self.active_clients[client_id]
                logger.info(f"客户端已注销: {client_id}")
            else:
                logger.warning(f"尝试注销不存在的客户端: {client_id}")

    def _register_tool_handlers(self) -> None:
        """注册工具处理函数"""
        if not self.server:
            raise RuntimeError("服务器未初始化")

        @self.server.list_tools()
        async def list_tools() -> list[Tool]:
            self._ensure_initialized()
            return self.tools

        @self.server.call_tool()
        async def call_tool(
            name: str, arguments: dict
        ) -> list[TextContent | ImageContent | EmbeddedResource]:
            result: TopResponseModel
            region = arguments.get("region") or "cn-north-4"
            product_short = self.openapi_dict["info"]["x-host_prefix"].lower()

            ak = self.config.ak
            sk = self.config.sk

            if not ak or not sk:
                error_msg = {
                    "code": "MISSING_CREDENTIALS",
                    "message": "HUAWEI_ACCESS_KEY or HUAWEI_SECRET_KEY not configured",
                }
                return [TextContent(type="text", text=json.dumps(error_msg, indent=2))]

            client = create_api_client(ak, sk, product_short, region)
            try:
                arguments = filter_parameters(arguments)

                http_info = build_http_info(
                    name, arguments, self.openapi_dict, self.tools
                )

                response = client.do_http_request(**http_info)
                response_data = response.json() if response and response.content else {}
                result = TopResponseModel(**response_data)
                return [TextContent(type="text", text=json.dumps(result.model_dump()))]
            except ClientRequestException as ex:
                logger.error(f"API 请求失败: {ex.error_msg}")
                raise ValueError(ex.error_msg)
            except Exception as ex:
                logger.error(f"意外的错误: {str(ex)}")
                raise

    def _ensure_initialized(self) -> None:
        """确保服务器已初始化"""
        if not self.initialized:
            raise RuntimeError("服务器未初始化")

    async def run_server(self):
        self._ensure_initialized()
        if self.config.transport == TRANSPORT_SSE:
            await self.run_sse_server()
        elif self.config.transport == TRANSPORT_HTTP:
            await self.run_http_server()
        else:
            await self.run_stdio_server()

    async def run_sse_server(self):
        logger.info("启动SSE服务器")
        # 配置SSE服务器
        sse = SseServerTransport("/messages/")

        async def handle_sse_connection(request):
            logger.info(f"SSE连接请求来自: {request.client}")

            # 检查服务器状态
            if not self.initialized:
                return JSONResponse({"error": "Server initializing"}, status_code=503)

            client_id = str(uuid.uuid4())
            connection_active = True

            try:
                # 注册客户端连接（添加到活跃连接列表）
                await self.register_client(client_id, request)

                # 使用MCP的SSE连接工具建立连接
                async with sse.connect_sse(
                    request.scope, request.receive, request._send
                ) as streams:
                    input_stream, output_stream = streams

                    try:
                        await self.server.run(
                            input_stream,
                            output_stream,
                            self.server.create_initialization_options(),
                        )

                    except asyncio.CancelledError:
                        # 任务被取消（正常关闭）
                        logger.info(f"SSE任务被取消: {client_id}")
                        connection_active = False

                    except Exception as e:
                        # 处理其他异常
                        logger.error(f"SSE通信异常: {e}", exc_info=True)
                        connection_active = False

                        # 尝试向客户端发送错误信息（如果连接仍可用）
                        if not output_stream.closed:
                            try:
                                error_msg = {
                                    "event": "error",
                                    "data": {"message": str(e), "code": 500},
                                }
                                await output_stream.send(json.dumps(error_msg))
                            except Exception as send_error:
                                logger.warning(f"发送错误信息失败: {send_error}")

                    finally:
                        # 确保资源释放
                        if connection_active:
                            connection_active = False
                            await self.unregister_client(client_id)
                            logger.info(f"SSE连接已关闭: {client_id}")

            except Exception as e:
                logger.error(f"SSE连接建立失败: {e}", exc_info=True)

                return JSONResponse(
                    {"error": "Failed to establish SSE connection", "details": str(e)},
                    status_code=500,
                )

            # 如果没有异常，返回成功响应
            return JSONResponse(
                {"status": "SSE connection closed normally"}, status_code=200
            )

        app = Starlette(
            routes=[
                Route("/sse", endpoint=handle_sse_connection),
                Mount("/messages/", app=sse.handle_post_message),
            ],
            debug=True,
        )

        # 添加CORS中间件
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_headers=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        )
        sse_config = uvicorn.Config(app, host="0.0.0.0", port=self.config.port)
        sse_server = uvicorn.Server(sse_config)
        await sse_server.serve()

    async def run_stdio_server(self):
        logger.info("启动STDIO服务器")
        async with stdio_server() as streams:
            await self.server.run(
                streams[0], streams[1], self.server.create_initialization_options()
            )

    async def run_http_server(self):
        logger.info("启动StreamableHTTP服务器")
        # Create the session manager with true stateless mode
        session_manager = StreamableHTTPSessionManager(
            app=self.server,
            event_store=None,
            stateless=True,
        )

        async def handle_streamable_http(
            scope: Scope, receive: Receive, send: Send
        ) -> None:
            await session_manager.handle_request(scope, receive, send)

        @contextlib.asynccontextmanager
        async def lifespan(app: Starlette) -> AsyncIterator[None]:
            """Context manager for session manager."""
            async with session_manager.run():
                logger.info("Application started with StreamableHTTP session manager!")
                try:
                    yield
                finally:
                    logger.info("Application shutting down...")

        # Create an ASGI application using the transport
        starlette_app = Starlette(
            debug=True,
            routes=[
                Mount("/mcp", app=handle_streamable_http),
            ],
            lifespan=lifespan,
        )

        http_config = uvicorn.Config(
            starlette_app, host="0.0.0.0", port=self.config.port
        )
        http_server = uvicorn.Server(http_config)
        await http_server.serve()
