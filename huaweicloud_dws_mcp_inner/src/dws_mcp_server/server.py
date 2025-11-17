import asyncio
import os
import logging
from logging import Logger
from mcp.server import Server
from mcp.types import Resource, Tool, TextContent, ResourceTemplate, GetPromptResult, Prompt
import dws_mcp_server.utils as utils
from pydantic import AnyUrl

# initialize server
server = Server("dws_mcp_server")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename="../../server-log.out"
)
logger = logging.getLogger("mcp-server")

DWS_SYS_DESC = '''
System level information for the DWS database, following are some common paths:

'/version'	Shows the version of the current gaussdb system.

'''

@server.list_resources()
async def list_resources() -> list[Resource]:
    """ dynamic resource uri templates """
    return [
        Resource(
            uri="gaussdb:///databases",
            name="All Databases",
            description="Show all databases",
            mimeType="text/plain"
        ),
        Resource(
            uri="gaussdb:///schemas",
            name="List Schemas",
            description="List all schemas in current database",
            mimeType="text/plain"
        )
    ]


@server.list_resource_templates()
async def list_resource_templates() -> list[ResourceTemplate]:
    return [
        ResourceTemplate(
            uriTemplate="gaussdb:////{schema}/tables",
            name="List Tables",
            description="List all tables in current schema",
            mimeType="text/plain"
        ),
        ResourceTemplate(
            uriTemplate="gaussdb:///{schema}/views",
            name="List Views",
            description="List all views in current schema",
            mimeType="text/plain"
        ),
        ResourceTemplate(
            uriTemplate="gaussdb:///{schema}/{table}/attributes",
            name="List Table/View Cols",
            description="List the columns for the specified table or view",
            mimeType="text/plain"
        ),
        ResourceTemplate(
            uriTemplate="system:///{system_path}",
            name="System Info",
            description=DWS_SYS_DESC,
            mimeType="text/plain"
        )
    ]


@server.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    uri_str = str(uri)
    protocol = uri_str.split(":///")[0]
    if protocol == "gaussdb":
        logger.info("resource template under gaussdb called")
        path = uri_str.split(":///")[1].split("/")
        if len(path) == 1:
            if path[0] == "databases":
                result = utils.handle_resource_call(
                    {"name": "list_db"}
                )
                return f"Databases:\n{result}"
            elif path[0] == "schemas":
                result = utils.handle_resource_call(
                    {
                        "name": "list_schema",
                        "db": path[0]
                    })
                return f"Schemas:\n{result}"
        elif len(path) == 2:
            if path[1] == "tables":
                result = utils.handle_resource_call(
                    {
                        "name": "list_table",
                        "schema": path[0]
                    })
                return f"Tables:\n{result}"
            elif path[1] == "views":
                result = utils.handle_resource_call(
                    {
                        "name": "list_view",
                        "schema": path[0]
                    })
                return f"Views:\n{result}"

        elif len(path) == 3:
            if path[2] == "attributes":
                result = utils.handle_resource_call(
                    {
                        "name": "list_table_column",
                        "schema": path[0],
                        "table": path[1],
                    })
                return f"Table/View columns:\n{result}"

    elif protocol == "system":
        path = uri_str.split(":///")[1]
        if path == "version":
            result = utils.handle_resource_call({"name": "version"})
            return f"Version: {result}"

    raise ValueError(f"Read resource failed: resource at '{uri_str}' not defined.")


@server.list_tools()
async def list_tools() -> list[Tool]:
    logger.info("Listing available tools")
    return [
        # list all db
        Tool(
            name="list_databases",
            description="List all databases.",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        # Get database activity log
        Tool(
            name="get_activity",
            description="get recent query activities in the system(from system catalog pgxc_stat_activity)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        # Execute SQL query
        Tool(
            name="execute_query",
            description="execute a sql query",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The sql query that needs to be executed."
                    }
                },
                "required": ["query"]
            }
        ),
        # List all schemas in the current database
        Tool(
            name="list_schemas",
            description="List all schemas in the current database",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        # List all tables under current schema
        Tool(
            name="list_tables",
            description="List all tables in the specified schema",
            inputSchema={
                "type": "object",
                "properties": {
                    "schema": {
                        "type": "string",
                        "description": "Schema name"
                    }
                },
                "required": ["schema"]
            }
        ),
        # List all views under current schema
        Tool(
            name="list_views",
            description="List all views in the specified schema",
            inputSchema={
                "type": "object",
                "properties": {
                    "schema": {
                        "type": "string",
                        "description": "Schema name"
                    }
                },
                "required": ["schema"]
            }
        ),
        # Show definition info for specified table/view
        Tool(
            name="get_table_info",
            description="Get table/view definition for the specified table/view",
            inputSchema={
                "type": "object",
                "properties": {
                    "schema": {
                        "type": "string",
                        "description": "Schema name"
                    },
                    "table": {
                        "type": "string",
                        "description": "Table/View name"
                    }
                },
                "required": ["schema", "table"]
            }
        ),
        # Show comment for schema, table
        Tool(
            name="get_comment",
            description="Get comment for specified schema or table",
            inputSchema={
                "type": "object",
                "properties": {
                    "schema": {
                        "type": "string",
                        "description": "The name of the schema"
                    },
                    "table": {
                        "type": "string",
                        "description": "The name of the table, '' if only querying for a schema"
                    }
                },
                "required": ["schema"]
            }
        )
    ]


@server.call_tool()
async def call_tool(
        name: str, arguments: dict | None
) -> list[TextContent]:
    if name == "get_activity" or name == "list_schemas" or name == "list_databases":
        arg = None
    elif name == "execute_query":
        if arguments is None or "query" not in arguments:
            raise ValueError(f"Tool {name} requires argument: 'query'.")
        arg = arguments["query"]
    elif name == "list_tables" or name == "list_views":
        if arguments is None or "schema" not in arguments:
            raise ValueError(f"Tool {name} requires argument 'schema'.")
        arg = arguments["schema"]
    elif name == "get_table_info":
        if arguments is None or "table" not in arguments:
            raise ValueError(f"Tool {name} requires argument: 'table'.")
        arg = arguments
    elif name == "get_comment":
        if arguments is None or "table" not in arguments or "schema" not in arguments:
            raise ValueError(f"Tool {name} requires argument: 'table'.")
        arg = arguments
    else:
        raise ValueError(f"Call tool failed, unnamed tool: {name}.")
    result = utils.handle_tool_call(name, arg)
    return [TextContent(type="text", text=f"{name}:\n{result}")]


async def main():
    logger.info("Starting server...")
    from mcp.server.stdio import stdio_server
    async with stdio_server() as (read_stream, write_stream):
        try:
            await server.run(read_stream, write_stream,
                             server.create_initialization_options())
        except Exception as e:
            logger.error(f"Server error: {e}.")
            raise e


if __name__ == "__main__":
    asyncio.run(main())
