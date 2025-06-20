# DLI MCP Server 


## Version
v0.1.0

## Overview

DLI MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DLI. Full-chain management of DLI resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| APIs related to data catalog | ShowCatalog | This API is used to describe the DLI catalog details. | To be tested |
|  | ListCatalogs | This API is used to obtain all catalog information of a specified project. | To be tested |
|  | RunCatalogAction | This API is used to create information about the metadata catalog (CATALOG) for binding or unbinding DLI from services such as lakeformation. | To be tested |
| APIs related to dynamic masking policies | ShowDataMaskStrategy | This API is used to obtain a dynamic masking policy. | To be tested |
|  | DeleteDataMaskStrategy | This API is used to delete a dynamic masking policy. | To be tested |
|  | CreateDataMaskStrategyUserAuth | This API is used for dynamic masking policy authorization. | To be tested |
|  | ListDataMaskStrategies | This API is used to obtain dynamic masking policies in batches. | To be tested |
|  | CreateDataMaskStrategy | This API is used for dynamic masking policies. SQL execution results are masked and displayed. | To be tested |
|  | ShowDataMaskStrategyUserAuth | This API is used to obtain the masking policy permission. | To be tested |
|  | UpdateDataMaskStrategy | This API is used to update the dynamic anonymization policy and anonymize the SQL execution result. | To be tested |
| APIs related to enhanced cross-source connection | ListJobAuthInfos | This API is used to query cross-source authentication information. | To be tested |
|  | CreateJobAuthInfo | This API is used to create cross-source authentication. | To be tested |
|  | ShowEnhancedConnectionPrivilege | This API is used to query information about enhanced cross-source connection authorization. | To be tested |
|  | ShowEnhancedConnection | This API is used to query the created enhanced cross-source connections specified by the user. | To be tested |
|  | CreateRouteToEnhancedConnection | This API is used to create a cross-source route. | To be tested |
|  | DeleteJobAuthInfo | This API is used to delete cross-source authentication information. | To be tested |
|  | DeleteRouteFromEnhancedConnection | This API is used to delete a cross-source route. | To be tested |
|  | UpdateJobAuthInfo | This API is used to update cross-source authentication information. | To be tested |
|  | DeleteEnhancedConnection | This API is used to delete an enhanced cross-source connection. | To be tested |
|  | UpdateEnhancedConnection | This API is used to modify data source host information in cross-source mode. Only full data can be overwritten. | To be tested |
|  | ListEnhancedConnections | This API is used to query the list of enhanced cross-source connections created by the user. | To be tested |
|  | DisassociateQueueFromEnhancedConnection | This API is used to unbind a bound queue in the enhanced cross-source scenario. | To be tested |
|  | CreateEnhancedConnection | This API is used to create enhanced cross-source connections to other services. | To be tested |
|  | AssociateQueueToEnhancedConnection | This API is used to bind a queue to a created enhanced cross-source resource. | To be tested |
| APIs related to global variables | UpdateGlobalVariable | Modify a global variable. | To be tested |
|  | DeleteGlobalVariable | Delete a global variable. | To be tested |
|  | ListGlobalVariables | Query the global variable list. | To be tested |
|  | CreateGlobalVariable | Create a global variable. Global variables are used to replace sensitive data in SQL jobs. | To be tested |
| APIs related to resource tags | ListResourcesTags | Query the tag information of a specified resource type. | To be tested |
| APIs related to the elastic resource pool | CreatePeriodElasticResourcePoolSpecChangeOrder | API for placing an order for changing the specifications of the yearly/monthly elastic resource pool | To be tested |
|  | ListElasticResourcePoolScaleRecords | Query the scaling history of the current elastic resource pool | To be tested |
|  | ListElasticResourcePools | Query all elastic resource pools | To be tested |
|  | AssociateQueueToElasticResourcePool | Associate the queue to the elastic resource pool | To be tested |
|  | DeleteElasticResourcePool | Delete an elastic resource pool | To be tested |
|  | UpdateElasticResourcePoolQueue | This API is used to set the scaling policy for a specified queue in the elastic resource pool. | To be tested |
|  | CreatePeriodElasticResourcePoolOrder | Create a yearly/monthly elastic resource pool | To be tested |
|  | CreateElasticResourcePool | Create an elastic resource pool | To be tested |
|  | UpdateElasticResourcePool | Modifying elastic resource pool information | To be tested |
|  | ListElasticResourcePoolQueues | Query the queue to which the elastic resource pool belongs | To be tested |
| Database permission management | ListDatabaseUsers | Query all database users and roles. | To be tested |
| Deprecated - APIs related to group resources | UploadPythonFileJobResources | This API is used to upload pyfile modules in a project. | To be tested |
|  | UploadFileJobResources | This API is used to upload a module of the file type in a project. | To be tested |
|  | UploadJobResources | This API is used to upload group resources to a project. | To be tested |
|  | UpdateJobResourceOwner | Modifies the owner of the package. | To be tested |
|  | UploadJarJobResources | This API is used to upload JAR group resources in a project. | To be tested |
|  | ShowJobResource | This API is used to view resource information in a group of a project. | To be tested |
|  | ListJobResources | This API is used to view all resources, including groups, in a project. | To be tested |
|  | DeleteJobResource | This API is used to delete a resource package in a group of a project. | To be tested |
| Deprecated - Cross-source connection related API | ShowDatasourceConnection | This API is used to query the typical cross-source connections created by the specified user. | To be tested |
|  | UpdateAuthInfo | This API is used to update cross-source authentication information. | To be tested |
|  | ListAuthInfo | This API is used to query cross-source authentication information. | To be tested |
|  | ListDatasourceConnections | This API is used to query the list of typical cross-source connections created by the user. | To be tested |
|  | CreateEnhancedConnectionRoutes | This API is used to create cross-source routes. | To be tested |
|  | DeleteAuthInfo | This API is used to delete cross-source authentication information. | To be tested |
|  | CreateDatasourceConnection | This API is used to create typical cross-source connections to other services. | To be tested |
|  | DeleteEnhancedConnectionRoutes | This API is used to delete a cross-source route. | To be tested |
|  | CreateAuthInfo | This API is used to create cross-source authentication. | To be tested |
|  | DeleteDatasourceConnection | This API is used to delete a typical cross-source connection. | To be tested |
| Deprecated - Delegate and Permission Related API | ListQueueUsers | This API is used to query the names of all users who can use a specified queue. | To be tested |
|  | RunDataAuthorizationAction | This API is used to assign data permission on a database or data table to a specified user. | To be tested |
|  | ListTablePrivileges | This API is used to query the permissions of a specified user on a table. | To be tested |
|  | ListTableUsers | This API is used to view all users who have access to a specified table or column of a table. | To be tested |
|  | CreateDliAgency | Create a DLI agency | To be tested |
|  | RegisterAuthorizedQueue | This API is used to share a specified queue with other users. You can grant or revoke the permission to use the specified queue to the user. | To be tested |
|  | ShowDliAgency | Obtain the DLI agency information | To be tested |
| Deprecated - Flink Job - Job Related API | RegisterBucket | Users proactively grant operation permissions on OBS buckets to DLI to save checkpoints and run logs of jobs. | To be tested |
|  | ShowFlinkMetric | This API is used to query the monitoring information of multiple Flink jobs at the same time. | To be tested |
|  | CreateIefSystemEvents | This API is used to process IEF system events. | To be tested |
|  | UpdateFlinkJobStatusReport | This API is used to process the reported status information of edge Flink jobs. | To be tested |
|  | RunIefJobActionCallBack | This API is used to process action callback information of IEF Flink jobs. | To be tested |
|  | CreateIefMessageChannel | This API is used to create an IEF message channel. | To be tested |
| Deprecated - Queue related API | BatchDeleteQueuePlans | This API is used to delete scheduled queue scaling plans in batches. | To be tested |
|  | ListQueuePlans | This API is used to view the scheduled scaling plan of a queue. This API is used to list the scheduled specification change plan of a specified queue. | To be tested |
|  | UpdateQueueCidr | This function is used to modify the network segment of a yearly/monthly queue. | To be tested |
|  | DeleteQueuePlan | This API is used to delete a scheduled queue scaling plan with a specified ID. | To be tested |
|  | UpdateQueuePlan | This API is used to modify a scheduled scaling plan for a queue with a specified ID. | To be tested |
|  | CreateQueuePlan | This API is used to create a scheduled scaling plan for a specified queue. | To be tested |
| Deprecated - SQL Job Related API | ListTables | This API is used to query the information about the tables that meet the filter criteria or all tables in a specified database. | To be tested |
|  | ListPartitions |  | To be tested |
|  | ListSqlSampleTemplates | This API is used to query all SQL sample templates. | To be tested |
|  | PreviewTable | This API is used to preview the first 10 rows in a table. | To be tested |
|  | ImportTable | This API is used to import data from files to DLI or OBS tables. Currently, only data on OBS can be imported to DLI or OBS. | To be tested |
|  | ExportTable | This API is used to export query results of SQL statements to OBS OBS. Only query results of Query jobs can be exported. | To be tested |
|  | UpdateTableOwner | Modifies the owner of a table. | To be tested |
|  | ShowTable | This API is used to describe the metadata of a specified table. | To be tested |
| Deprecated-Spark Job-Job Related API | ShowSparkJobLog | This API is used to query the background logs of batch processing jobs. | To be tested |
| Flink Job-Job-related API | ShowFlinkJobExecutionGraph | Query the Flink job execution plan. | To be tested |
|  | ListFlinkJobs | Query the job list of the current user. You can use the job ID as the ID to query the number of jobs whose number is greater than or smaller than the specified number. By default, all jobs are queried. You can also set running or other status conditions. | To be tested |
|  | BatchRunFlinkJobs | Trigger batch running of Flink jobs. | To be tested |
|  | CreateFlinkJarJob | Currently, user-defined jobs support the JAR format and run in an exclusive cluster. | To be tested |
|  | BatchDeleteFlinkJobs | Delete jobs in any state in batches. | To be tested |
|  | BatchStopFlinkJobs | Stops running Flink jobs in batches. | To be tested |
|  | CreateFlinkSqlJobGraph | Generate the static flow graph of the Flink SQL job | To be tested |
|  | UpdateFlinkSqlJob | The Stream SQL syntax extends Apache Flink SQL. | To be tested |
|  | ShowFlinkJob | View details about a Flink job. | To be tested |
|  | ImportFlinkJobs | Import a Flink job in POST mode. The request body is in JSON format. | To be tested |
|  | CreateFlinkSqlJob | To submit an interactive SQL job in POST mode. The request body is in JSON format. | To be tested |
|  | UpdateFlinkJarJob | Updates a user-defined job. Currently, the JAR format is supported and the job runs in an exclusive cluster. | To be tested |
|  | ExportFlinkJobs | Export a Flink job in POST mode. The request body is in JSON format. | To be tested |
|  | DeleteFlinkJob | Delete a job in any state. | To be tested |
| Flink Job-Management API | ImportFlinkJobSavepoint | Import a Flink job savepoint. | To be tested |
|  | ExecuteFlinkJobSavepoint | Trigger the savepoint of a Flink job. | To be tested |
| Flink Job-Template-Related APIs | CreateFlinkSqlJobTemplate | Create a Flink job template in DLI. A maximum of 100 Flink job templates can be created. | To be tested |
|  | ListFlinkSqlJobTemplates | Query the Flink job template list. Currently, only user-defined templates can be queried. | To be tested |
|  | UpdateFlinkSqlJobTemplate | This API is used to update the existing Flink job template in DLI. | To be tested |
|  | DeleteFlinkSqlJobTemplate | Delete a Flink job template even if the template is being used by a job. | To be tested |
| Manage databases and users (PostgreSQL) | UpdateDatabaseOwner | Modifying the database owner | To be tested |
| Managing Databases and Users (MySQL) | DeleteDatabase | Delete the database. | To be tested |
|  | CreateDatabase | Create a database. | To be tested |
|  | ListDatabases | Query the database list. | To be tested |
| Permission-related API | RunAuthorizationAction | This API is used to grant, revoke, and update DLI resource permissions to specified users or projects. | To be tested |
|  | ListAuthorizationPrivileges | Obtains the permission information of the user to whom the permission is granted to an object. | To be tested |
| Queue-related API | CreateQueueProperty | This interface is used to add queue attributes. Multiple attributes can be added at a time. | To be tested |
|  | ShowConnectivityTask | This API is used to query the connectivity result after the connectivity test is submitted. | To be tested |
|  | DeleteQueue | This API is used to delete a specified queue. | To be tested |
|  | ListQueues | This API is used to list all queues in a project. | To be tested |
|  | UpdateQueueProperty | Update queue attributes | To be tested |
|  | CreateQueue | This API is used to create a queue. The queue will be bound to specified computing resources. | To be tested |
|  | ShowQueue | This API is used to list details about a specified queue in a project. | To be tested |
|  | ListQueueProperties | Obtain the attributes of the queue configuration. | To be tested |
|  | RunQueueAction | This function is used to restart, expand, and reduce queues. | To be tested |
|  | CreateConnectivityTask | Create an address connectivity request API, send an address connectivity test request to the specified cluster, and insert the test address into the table. | To be tested |
|  | DeleteQueueProperty | This API is used to delete a queue attribute. Multiple attribute values can be deleted at a time. | To be tested |
| Quota | ShowQuota | Query the network resource quotas of a single tenant in the VPC service, including the VPC quota, subnet quota, security group quota, security group rule quota, EIP quota, and VPN quota. | To be tested |
| SQL Job-Intercept Rule-Related APIs | UpdateSqlJobDefendRule | This API is used to update SQL interception rules and intercept SQL statements that match the rules. | To be tested |
|  | CreateSqlJobDefendRule | This API is used to create an SQL interception rule to intercept SQL statements matching the rule. | To be tested |
|  | ShowSqlJobSystemDefendRule | This API is used to obtain preconfigured SQL interception rules. | To be tested |
|  | DeleteSqlJobDefendRule | This API is used to delete an SQL interception rule. | To be tested |
|  | ListSqlJobSystemDefendRules | This API is used to obtain preconfigured SQL interception rules. | To be tested |
|  | ShowSqlJobDefendRule | This API is used to obtain a single SQL interception rule. | To be tested |
|  | ListSqlJobDefendRules | This API is used to obtain SQL interception rules in batches. | To be tested |
| SQL Job-Job-related API | CancelSqlJob | This API is used to cancel a submitted job. A job that has been executed or fails to be executed cannot be canceled. | To be tested |
|  | ExportSqlJobResult | This API is used to export query results of SQL statements to OBS OBS. Only query results of Query jobs can be exported. | To be tested |
|  | ShowSqlJobProgress | This API is used to obtain the job execution progress. If a job is being executed, the subjob information can be obtained. If a job has just started or ended, the subjob information cannot be obtained. | To be tested |
|  | CheckSql | This API is used to check the SQL syntax. | To be tested |
|  | ShowSqlJobDetail | This API is used to query job details, such as the database name, table name, file size, and export mode of a job. | To be tested |
|  | ShowSqlJobStatus | This API is used to query the job status after a job is submitted. | To be tested |
|  | PreviewSqlJobResult | This API is used to view the execution result of a job that executes an SQL query statement after the job is complete. Currently, you can view the execution results of only the Query jobs. | To be tested |
|  | ListSqlJobs | This API is used to query information about all jobs in the current project. | To be tested |
|  | CreateSqlJob | This API is used to submit jobs to queues by executing SQL statements. | To be tested |
| SQL Job-Template-related API | BatchDeleteSqlJobTemplates | This API is used to delete SQL templates in batches. | To be tested |
|  | UpdateSqlJobTemplate | This API is used to update an SQL template. | To be tested |
|  | CreateSqlJobTemplate | This API is used to store specified SQL statements and can be reused later. | To be tested |
|  | ListSqlJobTemplates | This API is used to view all SQL templates saved by a user. | To be tested |
| Spark Job-Job-related APIs | ShowSparkJob | This API is used to query job details based on the batch processing job ID. | To be tested |
|  | CancelSparkJob | This API is used to cancel batch processing jobs. | To be tested |
|  | ListSparkJobs | This API is used to query the list of batch processing jobs in a queue in a project. | To be tested |
|  | CreateSparkJob | This API is used to create a job in a queue. | To be tested |
|  | ShowSparkJobStatus | This API is used to query the status of a batch processing job. | To be tested |
| Spark Job-Template-Related APIs | ShowSparkJobTemplate | This API is used to obtain job templates. | To be tested |
|  | UpdateSparkJobTemplate | This API is used to modify a job template. | To be tested |
|  | ListSparkJobTemplates | This API is used to query the job template list. | To be tested |
|  | CreateSparkJobTemplate | This API is used to create a job template. | To be tested |
| Table interface | DeleteTable | This API is used to delete a specified table and all KV documents. After the table is marked as deleted, the space is not released immediately. Concurrent read and write operations still need to be completed. | To be tested |
| Tags | BatchCreateResourceTags | Adding tags to specified instances in batches | To be tested |
|  | CountResourcesByTags | Query the number of resource instances by tag | To be tested |
|  | ListResourcesByTags | Query the resource instance list by tag | To be tested |
|  | BatchDeleteResourceTags | Delete tags in batches for specified instances | To be tested |
|  | ShowResourceTags | Query the label information of a specified DB instance | To be tested |
| Warehouse interface | CreateTable | Create a table in the specified repository. The table name is unique in the repository. When creating a table, you need to specify the primary key profile, local secondary index profile, and global secondary index profile. When you create a table, if the warehouse does not exist, the warehouse will be created automatically. | To be tested |

