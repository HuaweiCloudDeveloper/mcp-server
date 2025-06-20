# DAS MCP Server 


## Version
v0.1.0

## Overview

DAS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DAS. Full-chain management of DAS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Cloud DBA | ChangeChargeMode | Setting a paid instance | To be tested |
|  | ListFullSqlTasks | Query the SQL insight task list after the full SQL statement function is enabled. This feature only supports paid instances. | To be tested |
|  | ShowSqlSwitchStatus | Query the status of the switch for collecting full and slow SQL statements by the DAS. This feature only supports paid instances. | To be tested |
|  | DeleteSqlLimitRules | Delete an SQL rate limit rule. Currently, only MySQL and PostgreSQL databases are supported. | To be tested |
|  | ShowTuning | Obtain the diagnosis result | To be tested |
|  | CreateSqlLimitRules | Add an SQL rate limiting rule. Currently, only MySQL and PostgreSQL databases are supported. | To be tested |
|  | ShowSqlExecutionPlan | Query the SQL execution plan. | To be tested |
|  | ListSqlLimitRules | Query SQL rate limiting rules. Currently, only MySQL and PostgreSQL databases are supported. | To be tested |
|  | SetThresholdForMetric | Setting Indicator Thresholds | To be tested |
|  | SynchronizeInstances | Synchronize the instance list. | To be tested |
|  | ListCloudDbaInstances | Obtain the DAS DB instance list. | To be tested |
|  | ListProcesses | Query the instance session list by database or user. | To be tested |
|  | ExportFullSqlDetails | After the full SQL statement function is enabled, you can create an SQL insight task and export full SQL details by node, user name, database, and operation type. This feature only supports paid instances. | To be tested |
|  | ListRiskItems | Query resource risk instance risk items | To be tested |
|  | ChangeSqlSwitch | This command is used to enable or disable DAS to collect full SQL statements. After the function is enabled, the DB instance performance loss is within 5%. After the full SQL statement function is enabled, the service stores the text content of the SQL statement for analysis. Users can set the storage duration of full SQL statements. After the storage duration expires, the SQL statements will be automatically deleted. If this parameter is not set, data is retained for 7 days by default. | To be tested |
|  | ListInstanceTopSlowLog | Query the list of top slow SQL statements of a DB instance | To be tested |
|  | ExportTopSqlTrendDetails | After the TopSQL switch is turned on, the SQL execution time range data is exported. This function supports only paid instances. The maximum query interval is six hours. | To be tested |
|  | ChangeTransactionSwitchStatus | To enable or disable the historical transaction function, only the MySQL engine is supported, and the full SQL or slow SQL function must be enabled. | To be tested |
|  | ShowSqlExplain | Query the SQL execution plan. | To be tested |
|  | CreateTuning | Executing SQL Diagnosis, | To be tested |
|  | CreateSpaceAnalysisTask | Create a spatial analysis task, for example, triggering reanalysis. The MySQL and GaussDB (for MySQL) engines are supported. | To be tested |
|  | ExportSlowSqlStatistics | Export slow SQL statistics after the slow SQL switch is enabled. | To be tested |
|  | ListInnodbLocks | Query the InnoDB lock waiting list. | To be tested |
|  | ExportSqlStatements | After the full SQL statement function is enabled, all SQL statements in a specified time range are exported at a time. The data can be obtained by page. This feature only supports paid instances. | To be tested |
|  | ShowTransactionSwitchStatus | Query historical transactions. | To be tested |
|  | ListTopSlowLog | Query the list of top slow SQL statements | To be tested |
|  | DeleteProcess | Session scanning and killing. Sessions can be scanned and killed by user, database, or session list. At least one of the three conditions must be specified. | To be tested |
|  | RegisterDbUser | This interface is used to register the database user and password with the DAS and return a database user ID. This database user ID will be used when other interfaces (such as the interface for querying the instance session list) are invoked. Passwords are encrypted and used only for DAS API-related functions. This interface does not create database user objects on the database instance. Please make sure that the user name and password you entered already exist and are correct. | To be tested |
|  | ExportSlowQueryLogs | After the slow SQL collection switch is enabled, slow SQL data within a specified time range is exported at a time. The slow SQL data can be obtained by page. You can only view data of the last hour for free instances. | To be tested |
|  | ShowDbUser | Query the database user information registered with the DAS. This interface cannot query the database user object on the database instance. | To be tested |
|  | ListSpaceAnalysis | Obtain the spatial analysis data list. Instance-level data comes from the file system, and database- and table-level data comes from the information_schema.tables table. Space & Metadata Analysis can analyze a maximum of 10000 tables. If database tablespace data is missing, the possible cause is that there are too many database instance tables or the account password is not saved. If you want to save the password, enter the database account through the user management interface or page. Supports MySQL, GaussDB (for MySQL), and SQL Server engines. | To be tested |
|  | ExportSlowSqlTrendDetails | After the slow SQL statement switch is turned on, the trend of the number of slow SQL statements is exported. You can only view data of the last hour for free instances. The maximum query interval is one day. | To be tested |
|  | ParseSqlLimitRules | Generate SQL rate limiting keywords based on original SQL statements. Currently, MySQL, MariaDB, and GaussDB (for MySQL) engines are supported. | To be tested |
|  | ListInstanceMultiNodesSingleMetric | Obtain the data of a single metric on multiple nodes | To be tested |
|  | ListMetadataLocks | Query the metadata lock list. | To be tested |
|  | ListRiskTrend | Query the resource risk instance risk trend | To be tested |
|  | UpdateDbUser | Change the database user name and password registered with the DAS. This interface does not change the user name and password of the database user object on the database instance. Please make sure that the user name and password you entered already exist and are correct. | To be tested |
|  | ListHealthReportTask | Query the instance health diagnosis report list. | To be tested |
|  | ShowSqlLimitJobInfo | Query information about SQL rate limiting tasks with a specified ID | To be tested |
|  | ExportTopRiskInstances | Export the list of top risky instances. You can view data in the last 24 hours. | To be tested |
|  | AddFullSqlTask | Create a full SQL detail parsing task | To be tested |
|  | ListInstanceDistribution | Query the instance distribution | To be tested |
|  | ShowInstanceHealthReport | Obtains the instance health diagnosis report. | To be tested |
|  | ShowSqlLimitSwitchStatus | Query the status of the SQL rate limiting switch. Currently, only MySQL DB instances are supported. | To be tested |
|  | ListTransactions | Query the historical transaction list. | To be tested |
|  | ChangeSqlLimitSwitchStatus | Sets the SQL rate limiting switch status. Currently, only MySQL databases are supported. | To be tested |
|  | UpdateSqlLimitRules | Modifies an SQL rate limiting rule. Currently, only the PostgreSQL database is supported. | To be tested |
|  | ListInstanceNodesInfo | Obtain the node information of a single instance | To be tested |
|  | CreateHealthReportTask | Create an instance health diagnosis task. | To be tested |
|  | ShowMetricNamesSupport | Supports indicator information for a single metric on multiple nodes | To be tested |
|  | ExportTopSqlTemplatesDetails | After the TopSQL switch is turned on, the topSQL template list is exported. This function supports only paid instances. The maximum query interval is one hour. | To be tested |
|  | ExportSlowSqlTemplatesDetails | Export the slow SQL template list after the slow SQL function is enabled. You can only view data of the last hour for free instances. The maximum query interval is one day. | To be tested |
| Destination Connection Management | ListConnections | Query the list of target connections. | To be tested |
| Development tool | CancelShareConnections | Deleting a shared link, | To be tested |
|  | CreateInstanceConnection | Create an instance connection | To be tested |
|  | CreateShareConnections | Set the sharing link, | To be tested |
| Managing Databases and Users (MySQL) | DeleteDbUser | Delete a database user. | To be tested |
|  | ListDbUsers | Query the database user list. | To be tested |
| Query version operation | ShowApiVersion | Query the details about a specified TMS API version. | To be tested |
|  | ListApiVersions | Query the TMS API version list. | To be tested |
| Quota | ShowQuotas | Query the resource quota of the current project. | To be tested |

