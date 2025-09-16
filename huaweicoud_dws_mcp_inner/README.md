# DWS MCP Server
The DWS MCP Server is a Model Context Protocol (MCP) server that provides tools and resources for managing data warehouse systems. It acts as an intermediary layer between clients and database systems, offering standardized APIs for query execution, schema management, and real-time monitoring through MCP-compliant interfaces.

## Key Features
- **MCP Tool Integration**: Exposes database operations as standardized MCP tools (e.g., `execute_query`, `list_databases`).
- **Resource Management**: Provides access to database resources via MCP resource templates (e.g., `gaussdb:///{schema}/{table}/attributes`).
- **Centralized Configuration**: Manages database connections and server settings through `config.py`.
- **API-First Design**: Enables programmatic access to database functionality via HTTP endpoints.
- **Cross-Platform Compatibility**: Works with any database system supported by the underlying DWS infrastructure.

## Configuration
1. **Install Dependencies**: Use `uv sync` to install packages from `pyproject.toml`.
2. **Configure MCP Server**: Edit `config.py` to set:
   - Server port and host
   - Logging verbosity
   - Database connection strings
3. **Run Server**: Start the MCP server with `uv --directory src/dws_mcp_server run server.py`.
4. **Access Tools**: Use `use_mcp_tool` with server name `dws` to execute commands like `list_databases` or `execute_query`.

## Available Tools
The DWS MCP Server provides the following tools for database management:

1. **list_databases**  
   - Lists all databases  
   - Input Schema: `{}`

2. **get_activity**  
   - Retrieves recent query activities from `pgxc_stat_activity`  
   - Input Schema: `{}`

3. **execute_query**  
   - Executes SQL queries  
   - Input Schema: `{"query": "string"}`

4. **list_schemas**  
   - Lists all schemas in the current database  
   - Input Schema: `{}`

5. **list_tables**  
   - Lists tables in a specified schema  
   - Input Schema: `{"schema": "string"}`

6. **list_views**  
   - Lists views in a specified schema  
   - Input Schema: `{"schema": "string"}`

7. **get_table_info**  
   - Retrieves table/view definitions  
   - Input Schema: `{"schema": "string", "table": "string"}`

8. **get_comment**  
   - Gets comments for schemas/tables  
   - Input Schema: `{"schema": "string", "table": "string"}`

## Available Resources
The server exposes these resources via MCP:

- **gaussdb:////{schema}/tables**  
  List tables in a schema

- **gaussdb:///{schema}/views**  
  List views in a schema

- **gaussdb:///{schema}/{table}/attributes**  
  List columns for a table/view

- **system:///{system_path}**  
  System information (e.g., `/version`)

## Getting Started
0. Make sure you have uv installed. If not, use `pip install uv` to install.
1. Clone the repository
2. Install dependencies: `uv sync`
3. Install vscode. You can download at `https://code.visualstudio.com/`
4. Install the Cline extension
