import asyncio
import json
import os
import time
import uuid
from pathlib import Path
from typing import Any, Optional

import uvicorn
from huaweicloudsdkcore.exceptions.exceptions import ClientRequestException
from mcp.server import Server
from mcp.server.fastmcp.exceptions import ToolError
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
from .model import MCPConfig
from .openapi import OpenAPIToToolsConverter
from .variable import TRANSPORT_SSE, TRANSPORT_HTTP

logger = get_logger(__name__)
configure_logging("INFO")

HUAWEI_SERVICES = "HUAWEI_SERVICES"

# Readonly prefixes: verbs that only read data (no mutations)
_READONLY_PREFIXES = (
    "List", "Show", "Get", "Count", "Check", "Search", "Query", "Describe",
)


def _is_readonly_tool(name: str) -> bool:
    """Check if a tool name (without service prefix) is a read-only operation."""
    for prefix in _READONLY_PREFIXES:
        if prefix in name:
            return True
    return False


def _find_openapi_json(service_code: str) -> Optional[Path]:
    """Locate the OpenAPI JSON for a service code."""
    base = Path(__file__).parent.parent.parent / "huaweicloud_services_server"
    candidate = base / f"mcp_server_{service_code}" / "src" / f"mcp_server_{service_code}" / "config" / f"{service_code}.json"
    return candidate if candidate.exists() else None


class UnifiedMCPServer:
    """Single-process MCP server that loads multiple Huawei Cloud services."""

    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.config: Optional[MCPConfig] = None
        self.server: Optional[Server] = None
        self.tools: list[Tool] = []
        self.initialized: bool = False

        # service_code -> {openapi_dict, tools}
        self.services: dict[str, dict[str, Any]] = {}

        self.initialize()

    def initialize(self) -> None:
        if self.initialized:
            return

        logger.info("Initializing unified MCP server...")

        self.config = load_config(self.config_path)
        if not self.config:
            raise ValueError("Failed to load config")

        self.server = Server("hwc-mcp-server-unified")

        # Determine which services to load
        services_env = os.environ.get(HUAWEI_SERVICES, "")
        if not services_env:
            raise ValueError(
                f"{HUAWEI_SERVICES} env var required. "
                "Comma-separated service codes, e.g.: ecs,vpc,cce,elb"
            )

        service_codes = [s.strip().lower() for s in services_env.split(",") if s.strip()]
        logger.info(f"Loading {len(service_codes)} services: {service_codes}")

        tools_mode = os.environ.get("HUAWEI_TOOLS_MODE", "readonly").lower()
        if tools_mode not in ("readonly", "full"):
            tools_mode = "readonly"
        logger.info(f"Tools mode: {tools_mode}")

        for code in service_codes:
            json_path = _find_openapi_json(code)
            if not json_path:
                logger.warning(f"OpenAPI JSON not found for service '{code}', skipping")
                continue

            try:
                openapi_dict = load_openapi(json_path)
            except Exception as e:
                logger.warning(f"Failed to load OpenAPI for '{code}': {e}, skipping")
                continue

            raw_tools = OpenAPIToToolsConverter(openapi_dict).convert()

            # Filter tools based on mode
            if tools_mode == "readonly":
                raw_tools = [t for t in raw_tools if _is_readonly_tool(t.name)]

            # Prefix tool names with service code
            prefixed_tools = []
            for tool in raw_tools:
                prefixed = Tool(
                    name=f"{code}_{tool.name}",
                    description=f"[{code.upper()}] {tool.description or tool.name}",
                    inputSchema=tool.inputSchema,
                )
                prefixed_tools.append(prefixed)

            self.services[code] = {
                "openapi_dict": openapi_dict,
                "tools": prefixed_tools,
                "raw_tools": raw_tools,
            }
            self.tools.extend(prefixed_tools)
            logger.info(f"  {code}: {len(raw_tools)} tools loaded")

        # Inject tenant parameter if multi-tenant active
        if self.config.tenants:
            tenant_names = list(self.config.tenants.keys())
            for tool in self.tools:
                tool.inputSchema.setdefault("properties", {})["tenant"] = {
                    "type": "string",
                    "description": f"Tenant name. Available: {tenant_names}",
                }

        logger.info(f"Total: {len(self.tools)} tools from {len(self.services)} services")

        self._register_tool_handlers()
        self.initialized = True

    def _resolve_service(self, prefixed_name: str):
        """Given 'ecs_ListServers', return ('ecs', 'ListServers', service_dict)."""
        for code, svc in self.services.items():
            prefix = f"{code}_"
            if prefixed_name.startswith(prefix):
                original_name = prefixed_name[len(prefix):]
                return code, original_name, svc
        raise ToolError(f"Unknown tool: {prefixed_name}")

    def _register_tool_handlers(self) -> None:
        if not self.server:
            raise RuntimeError("Server not initialized")

        @self.server.list_tools()
        async def list_tools() -> list[Tool]:
            return self.tools

        @self.server.call_tool()
        async def call_tool(
            name: str, arguments: dict
        ) -> list[TextContent | ImageContent | EmbeddedResource]:
            code, original_name, svc = self._resolve_service(name)
            openapi_dict = svc["openapi_dict"]
            raw_tools = svc["raw_tools"]

            region = arguments.pop("region", None) or "cn-north-4"
            tenant_name = arguments.pop("tenant", None)
            x_host = openapi_dict["info"]["x-host"]

            # Resolve credentials
            ak, sk = self.config.ak, self.config.sk
            endpoint_domain = self.config.endpoint_domain
            endpoint_prefix = self.config.endpoint_prefix
            project_id = self.config.project_id
            iam_endpoint = self.config.iam_endpoint

            if self.config.tenants:
                t_name = tenant_name or self.config.default_tenant
                if t_name and t_name in self.config.tenants:
                    t = self.config.tenants[t_name]
                    ak, sk = t.ak, t.sk
                    endpoint_domain = t.endpoint_domain or endpoint_domain
                    endpoint_prefix = t.endpoint_prefix or endpoint_prefix
                    project_id = t.project_id or project_id
                    iam_endpoint = t.iam_endpoint or iam_endpoint
                    region = t.region or region
                elif t_name:
                    raise ToolError(
                        f"Unknown tenant '{t_name}'. Available: {list(self.config.tenants.keys())}"
                    )

            if not ak or not sk:
                raise ToolError("HUAWEI_ACCESS_KEY or HUAWEI_SECRET_KEY not configured")

            client = create_api_client(
                ak, sk, x_host, region,
                endpoint_domain, endpoint_prefix, project_id, iam_endpoint,
            )
            try:
                arguments = filter_parameters(arguments)
                http_info = build_http_info(original_name, arguments, openapi_dict, raw_tools)
                response = client.do_http_request(**http_info)
                response_data = response.json() if response and response.content else {}
                return [
                    TextContent(
                        type="text",
                        text=json.dumps(response_data, indent=2, ensure_ascii=False),
                    )
                ]
            except ClientRequestException as ex:
                logger.error(f"[{code}] API request failed: {ex.error_msg}")
                raise ValueError(ex.error_msg)
            except Exception as ex:
                logger.error(f"[{code}] Unexpected error: {str(ex)}")
                raise

    async def run_server(self):
        if not self.initialized:
            raise RuntimeError("Server not initialized")
        if self.config.transport == TRANSPORT_SSE:
            await self._run_sse()
        elif self.config.transport == TRANSPORT_HTTP:
            await self._run_http()
        else:
            await self._run_stdio()

    async def _run_stdio(self):
        logger.info("Starting unified server (stdio)")
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream, write_stream, self.server.create_initialization_options()
            )

    async def _run_sse(self):
        logger.info(f"Starting unified server (SSE) on port {self.config.port}")
        sse = SseServerTransport("/messages/")

        async def handle_sse(request):
            async with sse.connect_sse(
                request.scope, request.receive, request._send
            ) as streams:
                await self.server.run(
                    streams[0], streams[1], self.server.create_initialization_options()
                )

        starlette_app = Starlette(
            routes=[
                Route("/sse", endpoint=handle_sse),
                Mount("/messages/", app=sse.handle_post_message),
            ]
        )
        starlette_app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

        config = uvicorn.Config(starlette_app, host="0.0.0.0", port=self.config.port)
        server = uvicorn.Server(config)
        await server.serve()

    async def _run_http(self):
        logger.info(f"Starting unified server (HTTP) on port {self.config.port}")
        session_manager = StreamableHTTPSessionManager(
            app=self.server,
            json_response=True,
            stateless=True,
        )
        await session_manager.run(
            host="0.0.0.0",
            port=self.config.port,
        )
