# DAS MCP Server 


## Version
v0.1.0

## Overview

DAS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DAS. Full-chain management of DAS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

<html>
    <head></head>
    <body>
        <table border="1" cellspacing="0" cellpadding="5">
            <tbody>
                <tr>
                    <th>类别</th>
                    <th>工具名称</th>
                    <th>功能描述</th>
                    <th>状态</th>
                </tr>
                <tr>
                    <td rowspan="52">Cloud DBA</td>
                    <td>ChangeChargeMode</td>
                    <td>Setting a paid instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFullSqlTasks</td>
                    <td>Query the SQL insight task list after the full SQL statement function is enabled. This feature only supports paid instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlSwitchStatus</td>
                    <td>Query the status of the switch for collecting full and slow SQL statements by the DAS. This feature only supports paid instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlLimitRules</td>
                    <td>Delete an SQL rate limit rule. Currently, only MySQL and PostgreSQL databases are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTuning</td>
                    <td>Obtain the diagnosis result</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlLimitRules</td>
                    <td>Add an SQL rate limiting rule. Currently, only MySQL and PostgreSQL databases are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlExecutionPlan</td>
                    <td>Query the SQL execution plan.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlLimitRules</td>
                    <td>Query SQL rate limiting rules. Currently, only MySQL and PostgreSQL databases are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetThresholdForMetric</td>
                    <td>Setting Indicator Thresholds</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SynchronizeInstances</td>
                    <td>Synchronize the instance list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudDbaInstances</td>
                    <td>Obtain the DAS DB instance list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProcesses</td>
                    <td>Query the instance session list by database or user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportFullSqlDetails</td>
                    <td>After the full SQL statement function is enabled, you can create an SQL insight task and export full SQL details by node, user name, database, and operation type. This feature only supports paid instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRiskItems</td>
                    <td>Query resource risk instance risk items</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeSqlSwitch</td>
                    <td>This command is used to enable or disable DAS to collect full SQL statements. After the function is enabled, the DB instance performance loss is within 5%. After the full SQL statement function is enabled, the service stores the text content of the SQL statement for analysis. Users can set the storage duration of full SQL statements. After the storage duration expires, the SQL statements will be automatically deleted. If this parameter is not set, data is retained for 7 days by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceTopSlowLog</td>
                    <td>Query the list of top slow SQL statements of a DB instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportTopSqlTrendDetails</td>
                    <td>After the TopSQL switch is turned on, the SQL execution time range data is exported. This function supports only paid instances. The maximum query interval is six hours.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeTransactionSwitchStatus</td>
                    <td>To enable or disable the historical transaction function, only the MySQL engine is supported, and the full SQL or slow SQL function must be enabled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlExplain</td>
                    <td>Query the SQL execution plan.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTuning</td>
                    <td>Executing SQL Diagnosis,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSpaceAnalysisTask</td>
                    <td>Create a spatial analysis task, for example, triggering reanalysis. The MySQL and GaussDB (for MySQL) engines are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportSlowSqlStatistics</td>
                    <td>Export slow SQL statistics after the slow SQL switch is enabled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInnodbLocks</td>
                    <td>Query the InnoDB lock waiting list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportSqlStatements</td>
                    <td>After the full SQL statement function is enabled, all SQL statements in a specified time range are exported at a time. The data can be obtained by page. This feature only supports paid instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTransactionSwitchStatus</td>
                    <td>Query historical transactions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopSlowLog</td>
                    <td>Query the list of top slow SQL statements</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProcess</td>
                    <td>Session scanning and killing. Sessions can be scanned and killed by user, database, or session list. At least one of the three conditions must be specified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterDbUser</td>
                    <td>This interface is used to register the database user and password with the DAS and return a database user ID. This database user ID will be used when other interfaces (such as the interface for querying the instance session list) are invoked. Passwords are encrypted and used only for DAS API-related functions. This interface does not create database user objects on the database instance. Please make sure that the user name and password you entered already exist and are correct.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportSlowQueryLogs</td>
                    <td>After the slow SQL collection switch is enabled, slow SQL data within a specified time range is exported at a time. The slow SQL data can be obtained by page. You can only view data of the last hour for free instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDbUser</td>
                    <td>Query the database user information registered with the DAS. This interface cannot query the database user object on the database instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSpaceAnalysis</td>
                    <td>Obtain the spatial analysis data list. Instance-level data comes from the file system, and database- and table-level data comes from the information_schema.tables table. Space &amp; Metadata Analysis can analyze a maximum of 10000 tables. If database tablespace data is missing, the possible cause is that there are too many database instance tables or the account password is not saved. If you want to save the password, enter the database account through the user management interface or page. Supports MySQL, GaussDB (for MySQL), and SQL Server engines.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportSlowSqlTrendDetails</td>
                    <td>After the slow SQL statement switch is turned on, the trend of the number of slow SQL statements is exported. You can only view data of the last hour for free instances. The maximum query interval is one day.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ParseSqlLimitRules</td>
                    <td>Generate SQL rate limiting keywords based on original SQL statements. Currently, MySQL, MariaDB, and GaussDB (for MySQL) engines are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceMultiNodesSingleMetric</td>
                    <td>Obtain the data of a single metric on multiple nodes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetadataLocks</td>
                    <td>Query the metadata lock list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRiskTrend</td>
                    <td>Query the resource risk instance risk trend</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDbUser</td>
                    <td>Change the database user name and password registered with the DAS. This interface does not change the user name and password of the database user object on the database instance. Please make sure that the user name and password you entered already exist and are correct.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHealthReportTask</td>
                    <td>Query the instance health diagnosis report list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlLimitJobInfo</td>
                    <td>Query information about SQL rate limiting tasks with a specified ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportTopRiskInstances</td>
                    <td>Export the list of top risky instances. You can view data in the last 24 hours.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddFullSqlTask</td>
                    <td>Create a full SQL detail parsing task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceDistribution</td>
                    <td>Query the instance distribution</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceHealthReport</td>
                    <td>Obtains the instance health diagnosis report.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlLimitSwitchStatus</td>
                    <td>Query the status of the SQL rate limiting switch. Currently, only MySQL DB instances are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTransactions</td>
                    <td>Query the historical transaction list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeSqlLimitSwitchStatus</td>
                    <td>Sets the SQL rate limiting switch status. Currently, only MySQL databases are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSqlLimitRules</td>
                    <td>Modifies an SQL rate limiting rule. Currently, only the PostgreSQL database is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceNodesInfo</td>
                    <td>Obtain the node information of a single instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHealthReportTask</td>
                    <td>Create an instance health diagnosis task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetricNamesSupport</td>
                    <td>Supports indicator information for a single metric on multiple nodes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportTopSqlTemplatesDetails</td>
                    <td>After the TopSQL switch is turned on, the topSQL template list is exported. This function supports only paid instances. The maximum query interval is one hour.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportSlowSqlTemplatesDetails</td>
                    <td>Export the slow SQL template list after the slow SQL function is enabled. You can only view data of the last hour for free instances. The maximum query interval is one day.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Destination Connection Management</td>
                    <td>ListConnections</td>
                    <td>Query the list of target connections.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Development tool</td>
                    <td>CancelShareConnections</td>
                    <td>Deleting a shared link,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceConnection</td>
                    <td>Create an instance connection</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateShareConnections</td>
                    <td>Set the sharing link,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Managing Databases and Users (MySQL)</td>
                    <td>DeleteDbUser</td>
                    <td>Delete a database user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbUsers</td>
                    <td>Query the database user list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Query version operation</td>
                    <td>ShowApiVersion</td>
                    <td>Query the details about a specified TMS API version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersions</td>
                    <td>Query the TMS API version list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowQuotas</td>
                    <td>Query the resource quota of the current project.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
