# coding: utf-8

from mcp.server.fastmcp import FastMCP
import logging
from tools import utils
from tools import ecs_tools
from tools import obs_tools
from tools import ocr_tools


logger = logging.getLogger(__name__)


def main(transport: str):
    utils.setup_logging()

    # Create an MCP server
    mcp = FastMCP("huawei-cloud-mcp-server")
    for tool in ecs_tools.tools:
        mcp.add_tool(tool)

    for tool in obs_tools.tools:
        mcp.add_tool(tool)

    for tool in ocr_tools.tools:
        mcp.add_tool(tool)

    # Initialize and run the server
    logger.debug(f'mcp server is running on {transport} mode.')
    mcp.run(transport=transport)


if __name__ == "__main__":
    main(utils.get_transport())