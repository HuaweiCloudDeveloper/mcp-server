import argparse
import asyncio
from pathlib import Path

from assets.utils.server import MCPServer


def main():
    config_folder = Path(__file__).parent / "config"
    config_file = "config.yaml"
    asyncio.run(run_server(config_folder / config_file))


async def run_server(config_path):
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument("-p", "--port", type=int, help="Port number")
    parser.add_argument(
        "-t",
        "--transport",
        type=str,
        choices=["http", "sse", "stdio"],
        help="Transport of MCP Server",
    )
    args = parser.parse_args()

    mcp_server = MCPServer(config_path)

    if args.transport:
        mcp_server.config.transport = args.transport
    if args.port:
        mcp_server.config.port = args.port

    await mcp_server.run_server()


if __name__ == "__main__":
    main()
