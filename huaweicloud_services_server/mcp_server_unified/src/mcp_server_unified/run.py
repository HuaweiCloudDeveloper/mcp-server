import argparse
import asyncio
from pathlib import Path

from assets.utils.unified_server import UnifiedMCPServer


def main():
    parser = argparse.ArgumentParser(description="Unified MCP Server (multi-service)")
    parser.add_argument("-p", "--port", type=int, help="Port number")
    parser.add_argument(
        "-t", "--transport", type=str, choices=["http", "sse", "stdio"],
        help="Transport of MCP Server",
    )
    args = parser.parse_args()

    config_path = Path(__file__).parent / "config" / "config.yaml"
    server = UnifiedMCPServer(config_path)

    if args.transport:
        server.config.transport = args.transport
    if args.port:
        server.config.port = args.port

    asyncio.run(server.run_server())


if __name__ == "__main__":
    main()
