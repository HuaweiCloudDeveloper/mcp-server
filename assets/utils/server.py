import json
from contextvars import ContextVar
from pathlib import Path
from typing import Optional, Any, Sequence

import uvicorn
from fastmcp.utilities.logging import configure_logging, get_logger
from huaweicloudsdkcore.exceptions.exceptions import ClientRequestException
from mcp.server import Server
from mcp.server.sse import SseServerTransport
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount, Route

from .hwc_tools import create_api_client, build_http_info, load_openapi, filter_parameters, load_config
from .model import TopResponseModel, MCPConfig
from .openapi import OpenAPIToToolsConverter
from .variable import TRANSPORT_SSE

auth_context: ContextVar[Optional[dict[str, Any]]] = ContextVar("auth_context", default=None)

logger = get_logger(__name__)
configure_logging("INFO")

server_config: Optional[MCPConfig] = None
config_folder = Path(__file__).parent / 'config'
config_file = 'config.yaml'


async def serve() -> None:
    mcp_tools = []
    # 加载OpenAPI
    openapi_path = Path(config_folder) / f'{server_config.service_code}.json'
    openapi_dict = load_openapi(openapi_path)
    try:
        mcp_tools = OpenAPIToToolsConverter(openapi_dict).convert()
    except Exception as e:
        logger.error(f"加载OpenAPI转换MCP工具失败: {e}")
        raise

    server = Server(f'hwc-mcp-server-{server_config.service_code.lower()}')

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return mcp_tools

    @server.call_tool()
    async def call_tool(
            name: str, arguments: dict
    ) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
        result: TopResponseModel
        region = arguments.get('region') or "cn-north-4"
        product_short = openapi_dict["info"]["title"].lower()

        ak = server_config.ak
        sk = server_config.sk

        if not ak or not sk:
            error_msg = {
                "code": "MISSING_CREDENTIALS",
                "message": "HUAWEI_ACCESS_KEY or HUAWEI_SECRET_KEY not configured"
            }
            return [TextContent(type="text", text=json.dumps(error_msg, indent=2))]

        client = create_api_client(ak, sk, product_short, region)
        try:
            arguments = filter_parameters(arguments)

            http_info = build_http_info(name, arguments, openapi_dict, mcp_tools)

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

    if server_config.transport == TRANSPORT_SSE:
        # 配置SSE服务器
        sse = SseServerTransport("/messages/")

        async def handle_sse_connection(request):
            async with sse.connect_sse(
                    request.scope, request.receive, request._send
            ) as streams:
                await server.run(
                    streams[0], streams[1], server.create_initialization_options()
                )

        app = Starlette(
            routes=[
                Route("/sse", endpoint=handle_sse_connection),
                Mount("/messages/", app=sse.handle_post_message),
            ],
        )

        # 添加CORS中间件
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_headers=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        )

        sse_config = uvicorn.Config(app, host="0.0.0.0", port=server_config.sse_port)
        sse_server = uvicorn.Server(sse_config)
        await sse_server.serve()
    else:
        logger.info("启动STDIO服务器")
        options = server.create_initialization_options()
        async with stdio_server() as (read_stream, write_stream):
            await server.run(read_stream, write_stream, options)


if __name__ == "__main__":
    # 获取全局配置
    config_folder = Path(__file__).parent / 'config'
    config_file = 'config.yaml'
    server_config = load_config(config_folder / config_file)
