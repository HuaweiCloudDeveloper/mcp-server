# coding: utf-8
from mcp.server.fastmcp import FastMCP
import logging
from tools import utils
from tools import ecs_tools
from tools import obs_tools
from tools import ocr_tools
from tools import evs_tools
from tools import ims_tools
from tools import vpc_tools
from tools import eip_tools
from tools import das_tools
from tools import elb_tools


logger = logging.getLogger(__name__)


def main(transport: str):
    utils.setup_logging()

    # Create an MCP server
    mcp = FastMCP("huawei-cloud-mcp-server")
    for tool in ecs_tools.tools:
        mcp.add_tool(tool)

    for tool in ims_tools.tools:
        mcp.add_tool(tool)

    for tool in obs_tools.tools:
        mcp.add_tool(tool)

    for tool in ocr_tools.tools:
        mcp.add_tool(tool)

    for tool in evs_tools.tools:
        mcp.add_tool(tool)

    for tool in vpc_tools.tools:
        mcp.add_tool(tool)

    for tool in eip_tools.tools:
        mcp.add_tool(tool)

    for tool in das_tools.tools:
        mcp.add_tool(tool)

    for tool in elb_tools.tools:
        mcp.add_tool(tool)

    # Initialize and run the server
    logger.debug(f"mcp server is running on {transport} mode.")
    mcp.run(transport=transport)


if __name__ == "__main__":
    main(utils.get_transport())
