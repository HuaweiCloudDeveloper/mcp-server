import asyncio
from pathlib import Path

from assets.utils.server import MCPServer


async def main():
    config_folder = Path(__file__).parent / "config"
    config_file = "config.yaml"
    mcp_server = MCPServer(config_folder / config_file)
    await mcp_server.run_server()


if __name__ == "__main__":
    asyncio.run(main())
