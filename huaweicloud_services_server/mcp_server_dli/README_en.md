# DLI MCP Server 


## Version
v0.1.0

## Overview

DLI MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DLI. Full-chain management of DLI resources can be carried out based on natural language.

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
                    <td rowspan="3">APIs related to data catalog</td>
                    <td>ShowCatalog</td>
                    <td>This API is used to describe the DLI catalog details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCatalogs</td>
                    <td>This API is used to obtain all catalog information of a specified project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunCatalogAction</td>
                    <td>This API is used to create information about the metadata catalog (CATALOG) for binding or unbinding DLI from services such as lakeformation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">APIs related to dynamic masking policies</td>
                    <td>ShowDataMaskStrategy</td>
                    <td>This API is used to obtain a dynamic masking policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDataMaskStrategy</td>
                    <td>This API is used to delete a dynamic masking policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataMaskStrategyUserAuth</td>
                    <td>This API is used for dynamic masking policy authorization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataMaskStrategies</td>
                    <td>This API is used to obtain dynamic masking policies in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataMaskStrategy</td>
                    <td>This API is used for dynamic masking policies. SQL execution results are masked and displayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataMaskStrategyUserAuth</td>
                    <td>This API is used to obtain the masking policy permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataMaskStrategy</td>
                    <td>This API is used to update the dynamic anonymization policy and anonymize the SQL execution result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">APIs related to enhanced cross-source connection</td>
                    <td>ListJobAuthInfos</td>
                    <td>This API is used to query cross-source authentication information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateJobAuthInfo</td>
                    <td>This API is used to create cross-source authentication.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnhancedConnectionPrivilege</td>
                    <td>This API is used to query information about enhanced cross-source connection authorization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnhancedConnection</td>
                    <td>This API is used to query the created enhanced cross-source connections specified by the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRouteToEnhancedConnection</td>
                    <td>This API is used to create a cross-source route.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteJobAuthInfo</td>
                    <td>This API is used to delete cross-source authentication information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRouteFromEnhancedConnection</td>
                    <td>This API is used to delete a cross-source route.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateJobAuthInfo</td>
                    <td>This API is used to update cross-source authentication information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnhancedConnection</td>
                    <td>This API is used to delete an enhanced cross-source connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnhancedConnection</td>
                    <td>This API is used to modify data source host information in cross-source mode. Only full data can be overwritten.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnhancedConnections</td>
                    <td>This API is used to query the list of enhanced cross-source connections created by the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateQueueFromEnhancedConnection</td>
                    <td>This API is used to unbind a bound queue in the enhanced cross-source scenario.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnhancedConnection</td>
                    <td>This API is used to create enhanced cross-source connections to other services.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateQueueToEnhancedConnection</td>
                    <td>This API is used to bind a queue to a created enhanced cross-source resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">APIs related to global variables</td>
                    <td>UpdateGlobalVariable</td>
                    <td>Modify a global variable.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGlobalVariable</td>
                    <td>Delete a global variable.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalVariables</td>
                    <td>Query the global variable list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGlobalVariable</td>
                    <td>Create a global variable. Global variables are used to replace sensitive data in SQL jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">APIs related to resource tags</td>
                    <td>ListResourcesTags</td>
                    <td>Query the tag information of a specified resource type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">APIs related to the elastic resource pool</td>
                    <td>CreatePeriodElasticResourcePoolSpecChangeOrder</td>
                    <td>API for placing an order for changing the specifications of the yearly/monthly elastic resource pool</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListElasticResourcePoolScaleRecords</td>
                    <td>Query the scaling history of the current elastic resource pool</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListElasticResourcePools</td>
                    <td>Query all elastic resource pools</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateQueueToElasticResourcePool</td>
                    <td>Associate the queue to the elastic resource pool</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteElasticResourcePool</td>
                    <td>Delete an elastic resource pool</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateElasticResourcePoolQueue</td>
                    <td>This API is used to set the scaling policy for a specified queue in the elastic resource pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePeriodElasticResourcePoolOrder</td>
                    <td>Create a yearly/monthly elastic resource pool</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateElasticResourcePool</td>
                    <td>Create an elastic resource pool</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateElasticResourcePool</td>
                    <td>Modifying elastic resource pool information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListElasticResourcePoolQueues</td>
                    <td>Query the queue to which the elastic resource pool belongs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Database permission management</td>
                    <td>ListDatabaseUsers</td>
                    <td>Query all database users and roles.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Deprecated - APIs related to group resources</td>
                    <td>UploadPythonFileJobResources</td>
                    <td>This API is used to upload pyfile modules in a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadFileJobResources</td>
                    <td>This API is used to upload a module of the file type in a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadJobResources</td>
                    <td>This API is used to upload group resources to a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateJobResourceOwner</td>
                    <td>Modifies the owner of the package.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadJarJobResources</td>
                    <td>This API is used to upload JAR group resources in a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobResource</td>
                    <td>This API is used to view resource information in a group of a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobResources</td>
                    <td>This API is used to view all resources, including groups, in a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteJobResource</td>
                    <td>This API is used to delete a resource package in a group of a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Deprecated - Cross-source connection related API</td>
                    <td>ShowDatasourceConnection</td>
                    <td>This API is used to query the typical cross-source connections created by the specified user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAuthInfo</td>
                    <td>This API is used to update cross-source authentication information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuthInfo</td>
                    <td>This API is used to query cross-source authentication information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatasourceConnections</td>
                    <td>This API is used to query the list of typical cross-source connections created by the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnhancedConnectionRoutes</td>
                    <td>This API is used to create cross-source routes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAuthInfo</td>
                    <td>This API is used to delete cross-source authentication information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatasourceConnection</td>
                    <td>This API is used to create typical cross-source connections to other services.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnhancedConnectionRoutes</td>
                    <td>This API is used to delete a cross-source route.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAuthInfo</td>
                    <td>This API is used to create cross-source authentication.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatasourceConnection</td>
                    <td>This API is used to delete a typical cross-source connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Deprecated - Delegate and Permission Related API</td>
                    <td>ListQueueUsers</td>
                    <td>This API is used to query the names of all users who can use a specified queue.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunDataAuthorizationAction</td>
                    <td>This API is used to assign data permission on a database or data table to a specified user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTablePrivileges</td>
                    <td>This API is used to query the permissions of a specified user on a table.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTableUsers</td>
                    <td>This API is used to view all users who have access to a specified table or column of a table.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDliAgency</td>
                    <td>Create a DLI agency</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterAuthorizedQueue</td>
                    <td>This API is used to share a specified queue with other users. You can grant or revoke the permission to use the specified queue to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDliAgency</td>
                    <td>Obtain the DLI agency information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Deprecated - Flink Job - Job Related API</td>
                    <td>RegisterBucket</td>
                    <td>Users proactively grant operation permissions on OBS buckets to DLI to save checkpoints and run logs of jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlinkMetric</td>
                    <td>This API is used to query the monitoring information of multiple Flink jobs at the same time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIefSystemEvents</td>
                    <td>This API is used to process IEF system events.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlinkJobStatusReport</td>
                    <td>This API is used to process the reported status information of edge Flink jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunIefJobActionCallBack</td>
                    <td>This API is used to process action callback information of IEF Flink jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIefMessageChannel</td>
                    <td>This API is used to create an IEF message channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Deprecated - Queue related API</td>
                    <td>BatchDeleteQueuePlans</td>
                    <td>This API is used to delete scheduled queue scaling plans in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueuePlans</td>
                    <td>This API is used to view the scheduled scaling plan of a queue. This API is used to list the scheduled specification change plan of a specified queue.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateQueueCidr</td>
                    <td>This function is used to modify the network segment of a yearly/monthly queue.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteQueuePlan</td>
                    <td>This API is used to delete a scheduled queue scaling plan with a specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateQueuePlan</td>
                    <td>This API is used to modify a scheduled scaling plan for a queue with a specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateQueuePlan</td>
                    <td>This API is used to create a scheduled scaling plan for a specified queue.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Deprecated - SQL Job Related API</td>
                    <td>ListTables</td>
                    <td>This API is used to query the information about the tables that meet the filter criteria or all tables in a specified database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPartitions</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlSampleTemplates</td>
                    <td>This API is used to query all SQL sample templates.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PreviewTable</td>
                    <td>This API is used to preview the first 10 rows in a table.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportTable</td>
                    <td>This API is used to import data from files to DLI or OBS tables. Currently, only data on OBS can be imported to DLI or OBS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportTable</td>
                    <td>This API is used to export query results of SQL statements to OBS OBS. Only query results of Query jobs can be exported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTableOwner</td>
                    <td>Modifies the owner of a table.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTable</td>
                    <td>This API is used to describe the metadata of a specified table.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Deprecated-Spark Job-Job Related API</td>
                    <td>ShowSparkJobLog</td>
                    <td>This API is used to query the background logs of batch processing jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Flink Job-Job-related API</td>
                    <td>ShowFlinkJobExecutionGraph</td>
                    <td>Query the Flink job execution plan.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlinkJobs</td>
                    <td>Query the job list of the current user. You can use the job ID as the ID to query the number of jobs whose number is greater than or smaller than the specified number. By default, all jobs are queried. You can also set running or other status conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRunFlinkJobs</td>
                    <td>Trigger batch running of Flink jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFlinkJarJob</td>
                    <td>Currently, user-defined jobs support the JAR format and run in an exclusive cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteFlinkJobs</td>
                    <td>Delete jobs in any state in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopFlinkJobs</td>
                    <td>Stops running Flink jobs in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFlinkSqlJobGraph</td>
                    <td>Generate the static flow graph of the Flink SQL job</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlinkSqlJob</td>
                    <td>The Stream SQL syntax extends Apache Flink SQL.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlinkJob</td>
                    <td>View details about a Flink job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportFlinkJobs</td>
                    <td>Import a Flink job in POST mode. The request body is in JSON format.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFlinkSqlJob</td>
                    <td>To submit an interactive SQL job in POST mode. The request body is in JSON format.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlinkJarJob</td>
                    <td>Updates a user-defined job. Currently, the JAR format is supported and the job runs in an exclusive cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportFlinkJobs</td>
                    <td>Export a Flink job in POST mode. The request body is in JSON format.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFlinkJob</td>
                    <td>Delete a job in any state.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Flink Job-Management API</td>
                    <td>ImportFlinkJobSavepoint</td>
                    <td>Import a Flink job savepoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteFlinkJobSavepoint</td>
                    <td>Trigger the savepoint of a Flink job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Flink Job-Template-Related APIs</td>
                    <td>CreateFlinkSqlJobTemplate</td>
                    <td>Create a Flink job template in DLI. A maximum of 100 Flink job templates can be created.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlinkSqlJobTemplates</td>
                    <td>Query the Flink job template list. Currently, only user-defined templates can be queried.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlinkSqlJobTemplate</td>
                    <td>This API is used to update the existing Flink job template in DLI.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFlinkSqlJobTemplate</td>
                    <td>Delete a Flink job template even if the template is being used by a job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Manage databases and users (PostgreSQL)</td>
                    <td>UpdateDatabaseOwner</td>
                    <td>Modifying the database owner</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Managing Databases and Users (MySQL)</td>
                    <td>DeleteDatabase</td>
                    <td>Delete the database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabase</td>
                    <td>Create a database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabases</td>
                    <td>Query the database list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Permission-related API</td>
                    <td>RunAuthorizationAction</td>
                    <td>This API is used to grant, revoke, and update DLI resource permissions to specified users or projects.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuthorizationPrivileges</td>
                    <td>Obtains the permission information of the user to whom the permission is granted to an object.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Queue-related API</td>
                    <td>CreateQueueProperty</td>
                    <td>This interface is used to add queue attributes. Multiple attributes can be added at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConnectivityTask</td>
                    <td>This API is used to query the connectivity result after the connectivity test is submitted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteQueue</td>
                    <td>This API is used to delete a specified queue.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueues</td>
                    <td>This API is used to list all queues in a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateQueueProperty</td>
                    <td>Update queue attributes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateQueue</td>
                    <td>This API is used to create a queue. The queue will be bound to specified computing resources.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowQueue</td>
                    <td>This API is used to list details about a specified queue in a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueueProperties</td>
                    <td>Obtain the attributes of the queue configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunQueueAction</td>
                    <td>This function is used to restart, expand, and reduce queues.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnectivityTask</td>
                    <td>Create an address connectivity request API, send an address connectivity test request to the specified cluster, and insert the test address into the table.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteQueueProperty</td>
                    <td>This API is used to delete a queue attribute. Multiple attribute values can be deleted at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowQuota</td>
                    <td>Query the network resource quotas of a single tenant in the VPC service, including the VPC quota, subnet quota, security group quota, security group rule quota, EIP quota, and VPN quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">SQL Job-Intercept Rule-Related APIs</td>
                    <td>UpdateSqlJobDefendRule</td>
                    <td>This API is used to update SQL interception rules and intercept SQL statements that match the rules.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlJobDefendRule</td>
                    <td>This API is used to create an SQL interception rule to intercept SQL statements matching the rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlJobSystemDefendRule</td>
                    <td>This API is used to obtain preconfigured SQL interception rules.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlJobDefendRule</td>
                    <td>This API is used to delete an SQL interception rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlJobSystemDefendRules</td>
                    <td>This API is used to obtain preconfigured SQL interception rules.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlJobDefendRule</td>
                    <td>This API is used to obtain a single SQL interception rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlJobDefendRules</td>
                    <td>This API is used to obtain SQL interception rules in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">SQL Job-Job-related API</td>
                    <td>CancelSqlJob</td>
                    <td>This API is used to cancel a submitted job. A job that has been executed or fails to be executed cannot be canceled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportSqlJobResult</td>
                    <td>This API is used to export query results of SQL statements to OBS OBS. Only query results of Query jobs can be exported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlJobProgress</td>
                    <td>This API is used to obtain the job execution progress. If a job is being executed, the subjob information can be obtained. If a job has just started or ended, the subjob information cannot be obtained.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckSql</td>
                    <td>This API is used to check the SQL syntax.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlJobDetail</td>
                    <td>This API is used to query job details, such as the database name, table name, file size, and export mode of a job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlJobStatus</td>
                    <td>This API is used to query the job status after a job is submitted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PreviewSqlJobResult</td>
                    <td>This API is used to view the execution result of a job that executes an SQL query statement after the job is complete. Currently, you can view the execution results of only the Query jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlJobs</td>
                    <td>This API is used to query information about all jobs in the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlJob</td>
                    <td>This API is used to submit jobs to queues by executing SQL statements.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">SQL Job-Template-related API</td>
                    <td>BatchDeleteSqlJobTemplates</td>
                    <td>This API is used to delete SQL templates in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSqlJobTemplate</td>
                    <td>This API is used to update an SQL template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlJobTemplate</td>
                    <td>This API is used to store specified SQL statements and can be reused later.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlJobTemplates</td>
                    <td>This API is used to view all SQL templates saved by a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Spark Job-Job-related APIs</td>
                    <td>ShowSparkJob</td>
                    <td>This API is used to query job details based on the batch processing job ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelSparkJob</td>
                    <td>This API is used to cancel batch processing jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSparkJobs</td>
                    <td>This API is used to query the list of batch processing jobs in a queue in a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSparkJob</td>
                    <td>This API is used to create a job in a queue.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSparkJobStatus</td>
                    <td>This API is used to query the status of a batch processing job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Spark Job-Template-Related APIs</td>
                    <td>ShowSparkJobTemplate</td>
                    <td>This API is used to obtain job templates.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSparkJobTemplate</td>
                    <td>This API is used to modify a job template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSparkJobTemplates</td>
                    <td>This API is used to query the job template list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSparkJobTemplate</td>
                    <td>This API is used to create a job template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Table interface</td>
                    <td>DeleteTable</td>
                    <td>This API is used to delete a specified table and all KV documents. After the table is marked as deleted, the space is not released immediately. Concurrent read and write operations still need to be completed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Tags</td>
                    <td>BatchCreateResourceTags</td>
                    <td>Adding tags to specified instances in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountResourcesByTags</td>
                    <td>Query the number of resource instances by tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourcesByTags</td>
                    <td>Query the resource instance list by tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteResourceTags</td>
                    <td>Delete tags in batches for specified instances</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceTags</td>
                    <td>Query the label information of a specified DB instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Warehouse interface</td>
                    <td>CreateTable</td>
                    <td>Create a table in the specified repository. The table name is unique in the repository. When creating a table, you need to specify the primary key profile, local secondary index profile, and global secondary index profile. When you create a table, if the warehouse does not exist, the warehouse will be created automatically.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
