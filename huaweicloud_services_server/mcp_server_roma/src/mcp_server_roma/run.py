import asyncio
from pathlib import Path

from assets.utils import run_server


def main():
    config_folder = Path(__file__).parent / "config"
    config_file = "config.yaml"
    asyncio.run(run_server(config_folder / config_file))


if __name__ == "__main__":
    main()
