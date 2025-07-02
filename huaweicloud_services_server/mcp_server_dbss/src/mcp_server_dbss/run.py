from pathlib import Path

from assets.utils import server, load_config


def main():
    """Huawei Cloud MCP Server"""
    import asyncio
    server.config_folder = Path(__file__).parent / 'config'
    server.config_file = 'config.yaml'
    server.server_config = load_config(Path(server.config_folder) / server.config_file)
    asyncio.run(server.serve())


if __name__ == "__main__":
    main()
