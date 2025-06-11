# coding: utf-8
from mcp.server.fastmcp import FastMCP
import logging
import sys
sys.path.append("C:\\kylecheng\\mcp-server")
from assets.utils import sdk_utils
from mcp_server_das import das_tools


logger = logging.getLogger(__name__)


def main(transport: str):
    sdk_utils.setup_logging()

    # Create an MCP server
    mcp = FastMCP("huawei-cloud-mcp-server")

    for tool in das_tools.tools:
        mcp.add_tool(tool)

    # Initialize and run the server
    logger.debug(f"mcp server is running on {transport} mode.")
    mcp.run(transport=transport)


if __name__ == "__main__":
    main(sdk_utils.get_transport())
