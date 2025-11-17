import psycopg2
import dws_mcp_server.config as config

def connect_db():
    try:
        db_config = config.get_config()
        conn = psycopg2.connect(**db_config)
        conn.autocommit = True
        return conn
    except psycopg2.Error as e:
        raise ConnectionError(f"Database connection error: {e}")


def handle_resource_call(args):
    try:
        if args["name"] == "list_db":
            return execute_query("SELECT datname FROM pg_database;")
        elif args["name"] == "list_schema":
            return execute_query("""
                SELECT schema_name 
                FROM information_schema.schemata 
                WHERE schema_name NOT LIKE 'pg_%' 
                AND schema_name != 'information_schema'
                """)
        elif args["name"] == "list_table":
            return execute_query(f"""
                SELECT tablename
                FROM pg_tables
                WHERE schemaname = '{args["schema"]}'
                """)
        elif args["name"] == "list_view":
            return execute_query(f"""
                SELECT viewname
                FROM pg_views
                WHERE schemaname = '{args["schema"]}'
                """)
        elif args["name"] == "list_table_column":
            return get_view_or_table_def(args["schema"], args["table"])
        elif args["name"] == "version":
            return execute_query("SELECT version()")

        return "Resource handler not implemented."
    except Exception as e:
        return f"Error handling resource. {e}"


def handle_tool_call(tool_name, args):
    try:
        if tool_name == "list_databases":
            return execute_query("SELECT datname FROM pg_database;")
        elif tool_name == "get_activity":
            return execute_query("SELECT * FROM pgxc_stat_activity")
        elif tool_name == "execute_query":
            return execute_query(args)
        elif tool_name == "list_schemas":
            return execute_query("""
                SELECT schema_name 
                FROM information_schema.schemata 
                WHERE schema_name NOT LIKE 'pg_%' 
                AND schema_name != 'information_schema'
                """)
        elif tool_name == "list_tables":
            return execute_query(f"""
                SELECT tablename
                FROM pg_tables
                WHERE schemaname = '{args}'
                """)
        elif tool_name == "list_views":
            return execute_query(f"""
                SELECT viewname
                FROM pg_views
                WHERE schemaname = '{args}'
                """)

        elif tool_name == "get_table_info":
            return get_view_or_table_def(args["schema"], args["table"])
        elif tool_name == "get_comment":
            return get_comment(args["schema"], args["table"])

        return "Tool handler not implemented."
    except Exception as e:
        return f"Error handling tool {tool_name}: {str(e)}"


def _ensure_connection(conn):
    if conn is None or conn.closed:
        raise ValueError("The database connection is invalid.")
    return True


def execute_query(query):
    with connect_db() as conn:
        if not _ensure_connection(conn):
            return "Database connection failed."

        with conn.cursor() as cur:
            cur.execute(query)
            if cur.description:
                columns = [desc[0] for desc in cur.description]
                return "\n".join([",".join(columns)] + preprocess_result(cur.fetchall()))
            else:
                return f"Query executed successfully. Rows affected: {cur.rowcount}"


def get_view_or_table_def(schema, table):
    return execute_query(f"""
                SELECT 
                    n.nspname AS schemaname,
                    c.relname AS tablename,
                    CASE WHEN c.relkind = 'r' THEN pg_get_tabledef(c.oid) ELSE pg_get_viewdef(c.oid, 1, 1) END AS obj_def
                FROM pg_class c
                INNER JOIN pg_namespace n ON n.oid = c.relnamespace
                WHERE c.relkind IN ('r', 'm', 'v') AND n.nspname NOT IN ('pg_catalog', 'cstore', 'pg_toast', 'information_schema')
                AND n.nspname = '{schema}' AND c.relname = '{table}';
                """)


def get_comment(schema, table):
    return execute_query(f"""
            SELECT * FROM 
                (SELECT
                    current_database() AS database,
                    CASE WHEN a.attname IS NOT NULL THEN 'column'
                         WHEN ob.relkind = 'r' THEN 'table'
                         WHEN ob.relkind IN ('m', 'v') THEN 'view'
                    END AS object_type
                    ,n.nspname AS schemaname
                    ,ob.relname AS tablename
                    ,attname
                    ,description
                FROM pg_description d
                INNER JOIN pg_class c ON c.oid = d.classoid
                LEFT JOIN pg_class ob ON ob.oid = d.objoid
                LEFT JOIN pg_namespace n ON n.oid = ob.relnamespace
                LEFT JOIN pg_attribute a ON a.attrelid = ob.oid AND a.attnum = d.objsubid
                WHERE d.classoid IN (SELECT oid FROM pg_class WHERE relnamespace = 11 AND relname IN ('pg_database','pg_class','pg_attribute'))

                UNION ALL

                SELECT
                    current_database() AS database
                    ,'schema' AS object_type
                    ,n.nspname AS schemaname
                    ,NULL AS tablename
                    ,NULL
                    ,description
                FROM pg_description d
                INNER JOIN pg_namespace n ON n.oid = d.objoid
                WHERE d.classoid IN (SELECT oid FROM pg_class WHERE relnamespace = 11 AND relname IN ('pg_namespace'))
                AND n.nspname NOT IN('gs_logical_cluster','dbms_job','cstore','pg_toast', 'pg_catalog'))
            WHERE schemaname='{schema}' AND (tablename is NULL OR tablename = '{table}');
            """)


def preprocess_result(rows):
    return [",".join(map(str, row)) for row in rows]
