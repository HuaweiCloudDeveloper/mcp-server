import unittest
from unittest.mock import patch, MagicMock
from mcp.types import TextContent, Resource, ResourceTemplate
from dws_mcp_server.server import list_resources, list_resource_templates, read_resource, list_tools, call_tool
from dws_mcp_server.utils import handle_tool_call
from pydantic import AnyUrl
import os
import sys

test_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append("{}/../src".format(test_path))

class TestServerMethods(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        pass

    async def asyncTearDown(self):
        pass

    @patch('dws_mcp_server.utils.handle_tool_call')
    async def test_call_tool_get_activity(self, mock_handle_tool_call):
        mock_handle_tool_call.return_value = "Activity data"
        result = await call_tool("get_activity", None)
        self.assertEqual(result, [TextContent(type="text", text="get_activity:\nActivity data")])

    @patch('dws_mcp_server.utils.handle_tool_call')
    async def test_call_tool_execute_query_no_query(self, mock_handle_tool_call):
        with self.assertRaisesRegex(ValueError, "Tool execute_query requires argument: 'query'."):
            await call_tool("execute_query", None)

    @patch('dws_mcp_server.utils.handle_tool_call')
    async def test_call_tool_execute_query_with_query(self, mock_handle_tool_call):
        mock_handle_tool_call.return_value = "Query result"
        result = await call_tool("execute_query", {"query": "SELECT * FROM table;"})
        self.assertEqual(result, [TextContent(type="text", text="execute_query:\nQuery result")])

    @patch('dws_mcp_server.utils.handle_tool_call')
    async def test_call_tool_list_tables_no_schema(self, mock_handle_tool_call):
        with self.assertRaisesRegex(ValueError, "Tool list_tables requires argument 'schema'."):
            await call_tool("list_tables", None)

    @patch('dws_mcp_server.utils.handle_tool_call')
    async def test_call_tool_list_tables_with_schema(self, mock_handle_tool_call):
        mock_handle_tool_call.return_value = "Table list"
        result = await call_tool("list_tables", {"schema": "public"})
        self.assertEqual(result, [TextContent(type="text", text="list_tables:\nTable list")])

    @patch('dws_mcp_server.utils.handle_tool_call')
    async def test_call_tool_get_table_info_no_table(self, mock_handle_tool_call):
        with self.assertRaisesRegex(ValueError, "Tool get_table_info requires argument: 'table'."):
            await call_tool("get_table_info", None)

    @patch('dws_mcp_server.utils.handle_tool_call')
    async def test_call_tool_get_table_info_with_table(self, mock_handle_tool_call):
        mock_handle_tool_call.return_value = "Table info"
        result = await call_tool("get_table_info", {"table": "my_table"})
        self.assertEqual(result, [TextContent(type="text", text="get_table_info:\nTable info")])

    @patch('dws_mcp_server.utils.handle_tool_call')
    async def test_call_tool_get_comment_no_table_or_schema(self, mock_handle_tool_call):
        with self.assertRaisesRegex(ValueError, "Tool get_comment requires argument: 'table'."):
            await call_tool("get_comment", None)

    @patch('dws_mcp_server.utils.handle_tool_call')
    async def test_call_tool_get_comment_with_table_and_schema(self, mock_handle_tool_call):
        mock_handle_tool_call.return_value = "Comment data"
        result = await call_tool("get_comment", {"table": "my_table", "schema": "public"})
        self.assertEqual(result, [TextContent(type="text", text="get_comment:\nComment data")])

    @patch('dws_mcp_server.utils.handle_tool_call')
    async def test_call_tool_unnamed_tool(self, mock_handle_tool_call):
        with self.assertRaisesRegex(ValueError, "Call tool failed, unnamed tool: unknown_tool."):
            await call_tool("unknown_tool", None)

    @patch('dws_mcp_server.utils.execute_query')
    async def test_exception_handling(self, mock_execute_query):
        mock_execute_query.side_effect = Exception("Database connection failed")

        result = handle_tool_call("list_databases", None)

        expected_error = "Error handling tool list_databases: Database connection failed"
        self.assertEqual(result, expected_error)

    async def test_list_tools_returns_correct_tools(self):
        tools = await list_tools()

        self.assertEqual(len(tools), 8)

        tool_names = [tool.name for tool in tools]
        expected_tool_names = [
            "list_databases",
            "get_activity",
            "execute_query",
            "list_schemas",
            "list_tables",
            "list_views",
            "get_table_info",
            "get_comment"
        ]

        self.assertEqual(tool_names, expected_tool_names)

        list_databases_tool = next((tool for tool in tools if tool.name == "list_databases"), None)
        self.assertIsNotNone(list_databases_tool)
        self.assertEqual(list_databases_tool.description, "List all databases.")
        self.assertEqual(list_databases_tool.inputSchema, {
            "type": "object",
            "properties": {},
            "required": []
        })

        execute_query_tool = next((tool for tool in tools if tool.name == "execute_query"), None)
        self.assertIsNotNone(execute_query_tool)
        self.assertEqual(execute_query_tool.description, "execute a sql query")
        self.assertEqual(execute_query_tool.inputSchema, {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The sql query that needs to be executed."
                }
            },
            "required": ["query"]
        })

    async def test_list_resources(self):
        resources = await list_resources()

        self.assertEqual(len(resources), 2)

        self.assertIsInstance(resources[0], Resource)
        self.assertEqual(resources[0].uri, AnyUrl("gaussdb:///databases"))
        self.assertEqual(resources[0].name, "All Databases")
        self.assertEqual(resources[0].description, "Show all databases")
        self.assertEqual(resources[0].mimeType, "text/plain")

        self.assertIsInstance(resources[1], Resource)
        self.assertEqual(resources[1].uri, AnyUrl("gaussdb:///schemas"))
        self.assertEqual(resources[1].name, "List Schemas")
        self.assertEqual(resources[1].description, "List all schemas in current database")
        self.assertEqual(resources[1].mimeType, "text/plain")

    async def test_list_resource_templates(self):
        DWS_SYS_DESC = '''
System level information for the DWS database, following are some common paths:

'/version'	Shows the version of the current gaussdb system.

'''
        templates = await list_resource_templates()

        self.assertEqual(len(templates), 4)

        expected_templates = [
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

        for template, expected in zip(templates, expected_templates):
            self.assertEqual(template.uriTemplate, expected.uriTemplate)
            self.assertEqual(template.name, expected.name)
            self.assertEqual(template.description, expected.description)
            self.assertEqual(template.mimeType, expected.mimeType)

    @patch('dws_mcp_server.utils.handle_resource_call')
    async def test_read_resource(self, mock_handle_resource_call):
        test_cases = [
            (
                "gaussdb:///databases",
                "Databases:\nmock_db_result",
                {"name": "list_db"}
            ),
            (
                "gaussdb:///schemas",
                "Schemas:\nmock_schema_result",
                {"name": "list_schema", "db": "schemas"}
            ),
            (
                "gaussdb:///schema1/tables",
                "Tables:\nmock_table_result",
                {"name": "list_table", "schema": "schema1"}
            ),
            (
                "gaussdb:///schema1/views",
                "Views:\nmock_view_result",
                {"name": "list_view", "schema": "schema1"}
            ),
            (
                "gaussdb:///schema1/table1/attributes",
                "Table/View columns:\nmock_column_result",
                {"name": "list_table_column", "schema": "schema1", "table": "table1"}
            )
        ]
        for uri, expected_result, expected_call_args in test_cases:
            with self.subTest(uri=uri, expected_call_args=expected_call_args):
                with patch('dws_mcp_server.utils.handle_resource_call') as mock_handle_resource_call:
                    mock_handle_resource_call.return_value = expected_result.split(':\n')[1]

                    result = await read_resource(AnyUrl(uri))

                    self.assertEqual(result, expected_result)
                    mock_handle_resource_call.assert_called_once_with(expected_call_args)

    async def test_read_resource_invalid_uri(self):
        invalid = AnyUrl("gaussdb:///invalidurl")
        with self.assertRaisesRegex(ValueError, f"Read resource failed: resource at '{invalid}' not defined."):
            await read_resource(invalid)