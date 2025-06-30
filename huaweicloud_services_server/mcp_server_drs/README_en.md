# DRS MCP Server 


## Version
v0.1.0

## Overview

DRS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DRS. Full-chain management of DRS resources can be carried out based on natural language.

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
                    <td rowspan="1">Asset Management</td>
                    <td>ListUsers</td>
                    <td>Query the server list of the account</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Asynchronous Instance Management in Batches</td>
                    <td>ImportBatchCreateJobs</td>
                    <td>Batch import task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CommitAsyncJob</td>
                    <td>Submit the batch creation of asynchronous tasks. After the batch creation of asynchronous tasks or the parameters are updated, the system automatically verifies the parameters. After the parameters of all tasks are successfully verified and no error is reported, you can call this API to create a DRS task instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBatchAsyncJobs</td>
                    <td>This API is used to update details about a batch asynchronous task with a specified ID of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateJobsAsync</td>
                    <td>You can create asynchronous tasks in batches. You can create real-time migration, real-time synchronization, and real-time DR tasks in batches based on the request parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAsyncJobs</td>
                    <td>Query the list of asynchronous batch tasks created by a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadBatchCreateTemplate</td>
                    <td>Download the batch import task template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAsyncJobDetail</td>
                    <td>Query details about asynchronous batch tasks with a specified ID of a tenant. The results are sorted by create_time in descending order by default. The query can be performed on multiple pages.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Backup Migration</td>
                    <td>CreateReplicationJob</td>
                    <td>This interface is used to configure backup and migration tasks in three common scenarios.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateReplicationJob</td>
                    <td>Modifies the information, name, and description of a specified backup migration task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReplicationJobs</td>
                    <td>Obtain the current backup migration task list, excluding deleted tasks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReplicationJob</td>
                    <td>Obtains details about a specified backup migration task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteReplicationJob</td>
                    <td>You can delete a completed backup migration task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Comparison Management</td>
                    <td>ShowComparePolicy</td>
                    <td>Query the comparison policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHealthCompareJobDetail</td>
                    <td>Query details about a health comparison task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateComparePolicy</td>
                    <td>Modify the periodic comparison policy. Currently, only the MySQL-&gt;MySQL, MySQL-&gt;GaussDB(for MySQL), MySQL-&gt;GaussDB(DWS), and GaussDB(for MySQL)-&gt; MySQL synchronization task, MySQL-to-MySQL, and MySQL-to-GaussDB (for MySQL) migration task Comparison policies can be set for MySQL-&gt;MySQL, MySQL-&gt;GaussDB (for MySQL), GaussDB(for MySQL)-&gt;GaussDB(for MySQL), DDM-&gt;DDM, and DDS-DDS DR tasks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProgressData</td>
                    <td>Query the migration progress of different types of migration objects.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHealthObjectCompareJobOverview</td>
                    <td>Obtains the health comparison object-level comparison overview.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHealthCompareJobList</td>
                    <td>Query the health comparison list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Configuration Management</td>
                    <td>ListJobDdls</td>
                    <td>Query the list of incremental DDLs by status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CleanAlarms</td>
                    <td>Clear DDL alarms</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Connection management</td>
                    <td>ModifyConnection</td>
                    <td>Modify the information about the created connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Data Processing</td>
                    <td>ShowDataFilteringResult</td>
                    <td>Obtain the data filtering verification result</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectColumns</td>
                    <td>Collection of column information in a specified database table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataProcessingRulesResult</td>
                    <td>Obtain the data processing rule update result of a specified task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowColumnInfoResult</td>
                    <td>Obtain the column information of a specified database table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckDataFilter</td>
                    <td>Data filtering rule validation</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataProgress</td>
                    <td>Update the data processing rule of a specified task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataProgress</td>
                    <td>Query the data processing rule, including the mapping, column, data filtering, additional column, DDL, and DML information of the database table.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Destination Connection Management</td>
                    <td>ListConnections</td>
                    <td>Query the list of target connections.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnection</td>
                    <td>Create the target connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnection</td>
                    <td>Delete the target connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Enterprise Project Management Operation</td>
                    <td>ShowEnterpriseProject</td>
                    <td>Query enterprise project details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Image Tag</td>
                    <td>ListTags</td>
                    <td>Query the image tag list based on different conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Instance Database Object Configuration</td>
                    <td>CollectDbObjectsInfo</td>
                    <td>Submit the query for database object information, for example:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbObjects</td>
                    <td>Query database object information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDbObjectTemplateProgress</td>
                    <td>Object selection (file import-progress query)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectDbObjectsAsync</td>
                    <td>Submit to query the database object information, for example,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowObjectMapping</td>
                    <td>Querying real-time synchronization mapping relationships includes database mapping, schema mapping, table mapping, and column mapping during object selection and data processing.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDbObjectTemplateResult</td>
                    <td>Object selection (file import-get import result)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDbObjectCollectionStatus</td>
                    <td>Obtain the query result of the database object information submission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpdateObjectSavingStatus</td>
                    <td>Obtains the object saving progress.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDbObjectsList</td>
                    <td>Query database object information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadDbObjectTemplate</td>
                    <td>Object selection (file import-template upload)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSupportObjectType</td>
                    <td>Query the object selection type, column mapping, and object types supported by the task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadDbObjectTemplate</td>
                    <td>Object selection (file import-template download)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Instance Management</td>
                    <td>CreateJob</td>
                    <td>You can create a single task, such as live migration, real-time synchronization, and real-time DR based on the request parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeToPeriod</td>
                    <td>Change the billing mode from pay-per-use to yearly/monthly for DRS synchronization and DR tasks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateJob</td>
                    <td>This API is used to update details about a task with a specified ID of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyJob</td>
                    <td>DRS supports the cloning function to quickly copy the configuration of an existing synchronization task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFeatures</td>
                    <td>Query the advanced feature list of the current instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteJobsById</td>
                    <td>Delete tasks with specified IDs in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Instance details</td>
                    <td>ShowIncrementComponentsDetail</td>
                    <td>Query the details about the incremental component of a task synchronization task. This interface is used only when the task mode is incremental or full+increment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonitorData</td>
                    <td>Obtain the task monitoring data.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDirtyData</td>
                    <td>Query the list of abnormal data records.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetering</td>
                    <td>Obtain the parameters of the RFQ interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTimeline</td>
                    <td>You can specify a task ID to display the timeline information about the current task creation time, start time, retry time, and reset time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportOperationInfo</td>
                    <td>Exports the operation statistics of a specified task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">Instance operation</td>
                    <td>BatchStopJobsAction</td>
                    <td>This API is used to stop the tasks of specifying tenant IDs in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUserJdbcDriver</td>
                    <td>Delete the driver file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPositionResult</td>
                    <td>Obtain the result of querying the database location</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateJobName</td>
                    <td>The system verifies the task name when creating a task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteJobAction</td>
                    <td>Operate the task with the specified ID of the tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchExecuteJobActions</td>
                    <td>Perform batch operations on tasks with specified IDs for tenants.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadJdbcDriver</td>
                    <td>Upload the driver file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopJobAction</td>
                    <td>End the task of specifying the tenant ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJdbcDrivers</td>
                    <td>Query the driver file list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteJdbcDriver</td>
                    <td>Delete the driver file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectPositionAsync</td>
                    <td>Collection of database loci information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowActions</td>
                    <td>Obtain the allowed, forbidden, and current operation information of a specified task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadUserJdbcDriver</td>
                    <td>Upload the driver file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStartPosition</td>
                    <td>Update the start location of the incremental task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserJdbcDrivers</td>
                    <td>Query the driver file list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncJdbcDriver</td>
                    <td>Synchronize the driver file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncUserJdbcDriver</td>
                    <td>Synchronize the driver file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job management interface</td>
                    <td>BatchDeleteJobs</td>
                    <td>Delete jobs in batches from the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Parameter management</td>
                    <td>ListJobParameters</td>
                    <td>Query the parameter configuration list of a task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateJobConfigurations</td>
                    <td>Update the parameter information of the task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobHistoryParameters</td>
                    <td>Query the parameter setting modification history of a task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="38">Public Interface Management</td>
                    <td>ListDataCompareDetail</td>
                    <td>Query row number comparison details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowParams</td>
                    <td>During database migration, DRS provides the parameter comparison function to help you compare parameter consistency between the source and destination databases to ensure that service applications are not affected after the migration is successful.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContentCompareDifference</td>
                    <td>Query content comparison differences.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateJob</td>
                    <td>Modify task names or descriptions in batches and set exception notification information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetSpeed</td>
                    <td>Set the speed limit for a batch task. After the task is created, the speed limit is not set by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetObjects</td>
                    <td>Before the migration, select the database or table to be migrated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListJobDetails</td>
                    <td>Query task details in batches by task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopJobs</td>
                    <td>Stopping tasks in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartPromptlyDataLevelTableCompareJob</td>
                    <td>Start the data-level table comparison task immediately.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataLevelTableCompareJob</td>
                    <td>Create a data-level table comparison task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetDefiner</td>
                    <td>Whether to migrate Definers to the user in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListObejectLevelCompareDetail</td>
                    <td>Query details about an object comparison task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCompareResultFile</td>
                    <td>Export the result file of the comparison task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableZone</td>
                    <td>Query AZs whose flavors are not sold out</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadCompareResultFile</td>
                    <td>Download the result file of the comparison task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCheckJobs</td>
                    <td>Batch pre-check, which is used to check whether the migration can be performed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataLevelTableCompareJobs</td>
                    <td>Query the list of data-level table comparison tasks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataCompareOverview</td>
                    <td>Query the row number comparison overview.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCompareResult</td>
                    <td>Query the comparison result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableNodeTypes</td>
                    <td>Query available node specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchValidateClustersConnections</td>
                    <td>- Test connections in batches (cluster mode).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobList</td>
                    <td>Query the task list of a tenant by engine type, network type, task status, task name, or task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListProgresses</td>
                    <td>Query the full progress and incremental delay information in batches based on the task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchValidateConnections</td>
                    <td>Test connections in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateJobs</td>
                    <td>You can create real-time migration, synchronization, and DR tasks in batches based on the request parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateParams</td>
                    <td>Modify database parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListObejectLevelCompareOverview</td>
                    <td>Query the overview of object comparison tasks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContentCompareOverview</td>
                    <td>Query the content comparison overview.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListJobStatus</td>
                    <td>Query the task status in batches by task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetSmn</td>
                    <td>An exception notification cannot be set for an ended task in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateObjectLevelCompareJob</td>
                    <td>Create an object-level comparison task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartJobs</td>
                    <td>Starts live migration, synchronization, and DR tasks in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCompareJob</td>
                    <td>Cancel the comparison task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCompareTask</td>
                    <td>Create a comparison task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRestoreTask</td>
                    <td>If the migration task fails due to uncertain factors, you can resubmit the migration task by using the retry function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCheckResults</td>
                    <td>Query the precheck results of tasks in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContentCompareDetail</td>
                    <td>Query content comparison details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchResetPassword</td>
                    <td>This interface is invoked when the source and destination database passwords need to be changed after a task is started.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowQuotas</td>
                    <td>Query the resource quota of the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Real Migration Management</td>
                    <td>BatchUpdateUser</td>
                    <td>During the database migration, users need to be migrated separately. This API can be invoked to set users and roles to be migrated in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Real-time DR management</td>
                    <td>BatchListStructProcess</td>
                    <td>This API is used to query the DR initialization progress in batches based on the task ID. The VM ID cannot be queried.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListRposAndRtos</td>
                    <td>Query RPOs and RTOs in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonitoringData</td>
                    <td>Query DR monitoring data based on the task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListStructDetail</td>
                    <td>This API is used to query details about DR initialization objects in batches based on the task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSwitchover</td>
                    <td>Switch active/standby in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Real-time synchronization management</td>
                    <td>BatchSetPolicy</td>
                    <td>-Set synchronization policies in batches, including the conflict policy, filtering DROP data, and object synchronization scope.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTuningParams</td>
                    <td>Change the value of the optimization parameter.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchChangeData</td>
                    <td>DRS supports the processing of synchronized objects, that is, you can add rules for selected objects.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Recording and playback</td>
                    <td>ShowReplayResults</td>
                    <td>Obtains recording playback result data, including playback statistics by time, abnormal SQL statements and statistical results, and slow SQL statements and statistical results.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Resource management</td>
                    <td>ListLinks</td>
                    <td>You can query available link information, such as live migration, real-time synchronization, and real-time DR, based on different parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Right management</td>
                    <td>UpdateAgencyPolicy</td>
                    <td>Update the agency permission policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgencyInfo</td>
                    <td>Query agency permission details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListsAgencyPermissions</td>
                    <td>Obtain the permissions required by the agency based on the source database type, destination database type, and whether to create an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Tag Management</td>
                    <td>BatchCreateTags</td>
                    <td>Create tags in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountInstanceByTags</td>
                    <td>Query the number of resource instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceTags</td>
                    <td>Query the label information of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTags</td>
                    <td>This API is used to delete tags for a specified protected instance in batches. A maximum of 10 labels can be placed on a resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceTags</td>
                    <td>Query the instance tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceByTags</td>
                    <td>Query the resource instance list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchTagAction</td>
                    <td>Add or delete resource tags in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>Query all tags of a specified resource type in a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Task Center API</td>
                    <td>ListJobs</td>
                    <td>Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Task Management</td>
                    <td>ShowJobDetail</td>
                    <td>Query the execution status of a job. This API is used to query the execution status of an SFS Turbo asynchronous API. For example, you can use the jobId returned by calling the interface for creating and binding LDAP configuration to query the execution status of a job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
