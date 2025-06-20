# DRS MCP Server 


## Version
v0.1.0

## Overview

DRS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DRS. Full-chain management of DRS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Asset Management | ListUsers | Query the server list of the account | To be tested |
| Asynchronous Instance Management in Batches | ImportBatchCreateJobs | Batch import task | To be tested |
|  | CommitAsyncJob | Submit the batch creation of asynchronous tasks. After the batch creation of asynchronous tasks or the parameters are updated, the system automatically verifies the parameters. After the parameters of all tasks are successfully verified and no error is reported, you can call this API to create a DRS task instance. | To be tested |
|  | UpdateBatchAsyncJobs | This API is used to update details about a batch asynchronous task with a specified ID of a tenant. | To be tested |
|  | BatchCreateJobsAsync | You can create asynchronous tasks in batches. You can create real-time migration, real-time synchronization, and real-time DR tasks in batches based on the request parameters. | To be tested |
|  | ListAsyncJobs | Query the list of asynchronous batch tasks created by a tenant. | To be tested |
|  | DownloadBatchCreateTemplate | Download the batch import task template | To be tested |
|  | ListAsyncJobDetail | Query details about asynchronous batch tasks with a specified ID of a tenant. The results are sorted by create_time in descending order by default. The query can be performed on multiple pages. | To be tested |
| Backup Migration | CreateReplicationJob | This interface is used to configure backup and migration tasks in three common scenarios. | To be tested |
|  | UpdateReplicationJob | Modifies the information, name, and description of a specified backup migration task. | To be tested |
|  | ListReplicationJobs | Obtain the current backup migration task list, excluding deleted tasks. | To be tested |
|  | ShowReplicationJob | Obtains details about a specified backup migration task. | To be tested |
|  | DeleteReplicationJob | You can delete a completed backup migration task. | To be tested |
| Comparison Management | ShowComparePolicy | Query the comparison policy. | To be tested |
|  | ShowHealthCompareJobDetail | Query details about a health comparison task. | To be tested |
|  | UpdateComparePolicy | Modify the periodic comparison policy. Currently, only the MySQL->MySQL, MySQL->GaussDB(for MySQL), MySQL->GaussDB(DWS), and GaussDB(for MySQL)-> MySQL synchronization task, MySQL-to-MySQL, and MySQL-to-GaussDB (for MySQL) migration task Comparison policies can be set for MySQL->MySQL, MySQL->GaussDB (for MySQL), GaussDB(for MySQL)->GaussDB(for MySQL), DDM->DDM, and DDS-DDS DR tasks. | To be tested |
|  | ShowProgressData | Query the migration progress of different types of migration objects. | To be tested |
|  | ShowHealthObjectCompareJobOverview | Obtains the health comparison object-level comparison overview. | To be tested |
|  | ShowHealthCompareJobList | Query the health comparison list. | To be tested |
| Configuration Management | ListJobDdls | Query the list of incremental DDLs by status. | To be tested |
|  | CleanAlarms | Clear DDL alarms | To be tested |
| Connection management | ModifyConnection | Modify the information about the created connection. | To be tested |
| Data Processing | ShowDataFilteringResult | Obtain the data filtering verification result | To be tested |
|  | CollectColumns | Collection of column information in a specified database table | To be tested |
|  | ShowDataProcessingRulesResult | Obtain the data processing rule update result of a specified task | To be tested |
|  | ShowColumnInfoResult | Obtain the column information of a specified database table | To be tested |
|  | CheckDataFilter | Data filtering rule validation | To be tested |
|  | UpdateDataProgress | Update the data processing rule of a specified task | To be tested |
|  | ShowDataProgress | Query the data processing rule, including the mapping, column, data filtering, additional column, DDL, and DML information of the database table. | To be tested |
| Destination Connection Management | ListConnections | Query the list of target connections. | To be tested |
|  | CreateConnection | Create the target connection. | To be tested |
|  | DeleteConnection | Delete the target connection. | To be tested |
| Enterprise Project Management Operation | ShowEnterpriseProject | Query enterprise project details. | To be tested |
| Image Tag | ListTags | Query the image tag list based on different conditions. | To be tested |
| Instance Database Object Configuration | CollectDbObjectsInfo | Submit the query for database object information, for example: | To be tested |
|  | ListDbObjects | Query database object information. | To be tested |
|  | ShowDbObjectTemplateProgress | Object selection (file import-progress query) | To be tested |
|  | CollectDbObjectsAsync | Submit to query the database object information, for example,  | To be tested |
|  | ShowObjectMapping | Querying real-time synchronization mapping relationships includes database mapping, schema mapping, table mapping, and column mapping during object selection and data processing. | To be tested |
|  | ShowDbObjectTemplateResult | Object selection (file import-get import result) | To be tested |
|  | ShowDbObjectCollectionStatus | Obtain the query result of the database object information submission. | To be tested |
|  | ShowUpdateObjectSavingStatus | Obtains the object saving progress. | To be tested |
|  | ShowDbObjectsList | Query database object information. | To be tested |
|  | UploadDbObjectTemplate | Object selection (file import-template upload) | To be tested |
|  | ShowSupportObjectType | Query the object selection type, column mapping, and object types supported by the task. | To be tested |
|  | DownloadDbObjectTemplate | Object selection (file import-template download) | To be tested |
| Instance Management | CreateJob | You can create a single task, such as live migration, real-time synchronization, and real-time DR based on the request parameters. | To be tested |
|  | ChangeToPeriod | Change the billing mode from pay-per-use to yearly/monthly for DRS synchronization and DR tasks. | To be tested |
|  | UpdateJob | This API is used to update details about a task with a specified ID of a tenant. | To be tested |
|  | CopyJob | DRS supports the cloning function to quickly copy the configuration of an existing synchronization task. | To be tested |
|  | ListFeatures | Query the advanced feature list of the current instance. | To be tested |
|  | BatchDeleteJobsById | Delete tasks with specified IDs in batches. | To be tested |
| Instance details | ShowIncrementComponentsDetail | Query the details about the incremental component of a task synchronization task. This interface is used only when the task mode is incremental or full+increment.  | To be tested |
|  | ShowMonitorData | Obtain the task monitoring data. | To be tested |
|  | ShowDirtyData | Query the list of abnormal data records. | To be tested |
|  | ShowMetering | Obtain the parameters of the RFQ interface. | To be tested |
|  | ShowTimeline | You can specify a task ID to display the timeline information about the current task creation time, start time, retry time, and reset time. | To be tested |
|  | ExportOperationInfo | Exports the operation statistics of a specified task. | To be tested |
| Instance operation | BatchStopJobsAction | This API is used to stop the tasks of specifying tenant IDs in batches. | To be tested |
|  | DeleteUserJdbcDriver | Delete the driver file. | To be tested |
|  | ShowPositionResult | Obtain the result of querying the database location | To be tested |
|  | ValidateJobName | The system verifies the task name when creating a task. | To be tested |
|  | ExecuteJobAction | Operate the task with the specified ID of the tenant. | To be tested |
|  | BatchExecuteJobActions | Perform batch operations on tasks with specified IDs for tenants. | To be tested |
|  | UploadJdbcDriver | Upload the driver file. | To be tested |
|  | StopJobAction | End the task of specifying the tenant ID. | To be tested |
|  | ListJdbcDrivers | Query the driver file list. | To be tested |
|  | DeleteJdbcDriver | Delete the driver file. | To be tested |
|  | CollectPositionAsync | Collection of database loci information. | To be tested |
|  | ShowActions | Obtain the allowed, forbidden, and current operation information of a specified task. | To be tested |
|  | UploadUserJdbcDriver | Upload the driver file. | To be tested |
|  | UpdateStartPosition | Update the start location of the incremental task. | To be tested |
|  | ListUserJdbcDrivers | Query the driver file list. | To be tested |
|  | SyncJdbcDriver | Synchronize the driver file. | To be tested |
|  | SyncUserJdbcDriver | Synchronize the driver file. | To be tested |
| Job management interface | BatchDeleteJobs | Delete jobs in batches from the MRS cluster. | To be tested |
| Parameter management | ListJobParameters | Query the parameter configuration list of a task | To be tested |
|  | UpdateJobConfigurations | Update the parameter information of the task. | To be tested |
|  | ListJobHistoryParameters | Query the parameter setting modification history of a task | To be tested |
| Public Interface Management | ListDataCompareDetail | Query row number comparison details. | To be tested |
|  | BatchShowParams | During database migration, DRS provides the parameter comparison function to help you compare parameter consistency between the source and destination databases to ensure that service applications are not affected after the migration is successful. | To be tested |
|  | ListContentCompareDifference | Query content comparison differences. | To be tested |
|  | BatchUpdateJob | Modify task names or descriptions in batches and set exception notification information. | To be tested |
|  | BatchSetSpeed | Set the speed limit for a batch task. After the task is created, the speed limit is not set by default. | To be tested |
|  | BatchSetObjects | Before the migration, select the database or table to be migrated. | To be tested |
|  | BatchListJobDetails | Query task details in batches by task ID. | To be tested |
|  | BatchStopJobs | Stopping tasks in batches. | To be tested |
|  | StartPromptlyDataLevelTableCompareJob | Start the data-level table comparison task immediately. | To be tested |
|  | CreateDataLevelTableCompareJob | Create a data-level table comparison task. | To be tested |
|  | BatchSetDefiner | Whether to migrate Definers to the user in batches. | To be tested |
|  | ListObejectLevelCompareDetail | Query details about an object comparison task. | To be tested |
|  | CreateCompareResultFile | Export the result file of the comparison task. | To be tested |
|  | ListAvailableZone | Query AZs whose flavors are not sold out | To be tested |
|  | DownloadCompareResultFile | Download the result file of the comparison task. | To be tested |
|  | BatchCheckJobs | Batch pre-check, which is used to check whether the migration can be performed. | To be tested |
|  | ListDataLevelTableCompareJobs | Query the list of data-level table comparison tasks. | To be tested |
|  | ListDataCompareOverview | Query the row number comparison overview. | To be tested |
|  | ListCompareResult | Query the comparison result. | To be tested |
|  | ListAvailableNodeTypes | Query available node specifications. | To be tested |
|  | BatchValidateClustersConnections | - Test connections in batches (cluster mode). | To be tested |
|  | ShowJobList | Query the task list of a tenant by engine type, network type, task status, task name, or task ID. | To be tested |
|  | BatchListProgresses | Query the full progress and incremental delay information in batches based on the task ID. | To be tested |
|  | BatchValidateConnections | Test connections in batches. | To be tested |
|  | BatchCreateJobs | You can create real-time migration, synchronization, and DR tasks in batches based on the request parameters. | To be tested |
|  | UpdateParams | Modify database parameters. | To be tested |
|  | ListObejectLevelCompareOverview | Query the overview of object comparison tasks. | To be tested |
|  | ListContentCompareOverview | Query the content comparison overview. | To be tested |
|  | BatchListJobStatus | Query the task status in batches by task ID. | To be tested |
|  | BatchSetSmn | An exception notification cannot be set for an ended task in batches. | To be tested |
|  | CreateObjectLevelCompareJob | Create an object-level comparison task. | To be tested |
|  | BatchStartJobs | Starts live migration, synchronization, and DR tasks in batches. | To be tested |
|  | DeleteCompareJob | Cancel the comparison task. | To be tested |
|  | CreateCompareTask | Create a comparison task. | To be tested |
|  | BatchRestoreTask | If the migration task fails due to uncertain factors, you can resubmit the migration task by using the retry function. | To be tested |
|  | BatchCheckResults | Query the precheck results of tasks in batches. | To be tested |
|  | ListContentCompareDetail | Query content comparison details | To be tested |
|  | BatchResetPassword | This interface is invoked when the source and destination database passwords need to be changed after a task is started. | To be tested |
| Quota | ShowQuotas | Query the resource quota of the current project. | To be tested |
| Real Migration Management | BatchUpdateUser | During the database migration, users need to be migrated separately. This API can be invoked to set users and roles to be migrated in batches. | To be tested |
| Real-time DR management | BatchListStructProcess | This API is used to query the DR initialization progress in batches based on the task ID. The VM ID cannot be queried. | To be tested |
|  | BatchListRposAndRtos | Query RPOs and RTOs in batches. | To be tested |
|  | ShowMonitoringData | Query DR monitoring data based on the task ID. | To be tested |
|  | BatchListStructDetail | This API is used to query details about DR initialization objects in batches based on the task ID. | To be tested |
|  | BatchSwitchover | Switch active/standby in batches. | To be tested |
| Real-time synchronization management | BatchSetPolicy | -Set synchronization policies in batches, including the conflict policy, filtering DROP data, and object synchronization scope. | To be tested |
|  | UpdateTuningParams | Change the value of the optimization parameter. | To be tested |
|  | BatchChangeData | DRS supports the processing of synchronized objects, that is, you can add rules for selected objects. | To be tested |
| Recording and playback | ShowReplayResults | Obtains recording playback result data, including playback statistics by time, abnormal SQL statements and statistical results, and slow SQL statements and statistical results. | To be tested |
| Resource management | ListLinks | You can query available link information, such as live migration, real-time synchronization, and real-time DR, based on different parameters. | To be tested |
| Right management | UpdateAgencyPolicy | Update the agency permission policy | To be tested |
|  | ShowAgencyInfo | Query agency permission details | To be tested |
|  | ListsAgencyPermissions | Obtain the permissions required by the agency based on the source database type, destination database type, and whether to create an agency. | To be tested |
| Tag Management | BatchCreateTags | Create tags in batches | To be tested |
|  | CountInstanceByTags | Query the number of resource instances. | To be tested |
|  | ShowInstanceTags | Query the label information of a specified DB instance. | To be tested |
|  | BatchDeleteTags | This API is used to delete tags for a specified protected instance in batches. A maximum of 10 labels can be placed on a resource. | To be tested |
|  | ListInstanceTags | Query the instance tag. | To be tested |
|  | ListInstanceByTags | Query the resource instance list. | To be tested |
|  | BatchTagAction | Add or delete resource tags in batches. | To be tested |
| Tags | ListProjectTags | Query all tags of a specified resource type in a specified project | To be tested |
| Task Center API | ListJobs | Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph. | To be tested |
| Task Management | ShowJobDetail | Query the execution status of a job. This API is used to query the execution status of an SFS Turbo asynchronous API. For example, you can use the jobId returned by calling the interface for creating and binding LDAP configuration to query the execution status of a job. | To be tested |
|  | DeleteJob |  | To be tested |

