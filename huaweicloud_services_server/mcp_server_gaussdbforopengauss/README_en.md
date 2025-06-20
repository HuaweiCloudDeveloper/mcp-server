# GaussDBforopenGauss MCP Server 


## Version
v0.1.0

## Overview

GaussDBforopenGauss MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GaussDBforopenGauss. Full-chain management of GaussDBforopenGauss resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Add-on management | ListKernelPlugins | Query the list of installed plug-ins in an instance | To be tested |
|  | ListPluginExtensions | Query the extension information about the instance plug-in | To be tested |
|  | ResumePluginExtensions | Configure the plug-in expansion capability. | To be tested |
|  | InstallKernelPlugin | Install the plug-in | To be tested |
|  | ListSupportKernelPlugins | Query the list of supported plug-ins | To be tested |
|  | SetKernelPluginLicense | Configure the plug-in license | To be tested |
| Backup and Restore | CreateManualBackup | Create a manual backup. | To be tested |
|  | ShowBackupPolicy | Query the automatic backup policy. | To be tested |
|  | CreateRestoreInstance | Restore to a new DB instance. | To be tested |
|  | DeleteManualBackup | Delete a manual backup. | To be tested |
|  | SetBackupPolicy | Set the automatic backup policy. | To be tested |
|  | ListBackups | Obtain the backup list. | To be tested |
|  | ListRestoreTimes | Query the recoverable time segment. | To be tested |
|  | StopBackup | Stopping creating a backup | To be tested |
| Backup management | ShowInstanceSnapshot | Query the original DB instance information based on the time point or backup file. | To be tested |
|  | ListRestorableInstancesDetails | Query the list of DB instances that can be used for backup and restoration. The DB instance information must meet the backup conditions. | To be tested |
|  | RestoreInstance | Restoring to the current DB instance from a backup | To be tested |
|  | SetNewBackupPolicy | Setting the automatic backup policy | To be tested |
|  | DownloadBackup | Obtain the backup download link. | To be tested |
|  | ListRestorableInstances | Query the list of instances that can be used for backup and restoration. The instance information must meet the backup conditions. | To be tested |
|  | ListBackupsDetails | Obtain the backup list. | To be tested |
|  | ConfirmRestoredData | Ensure that the data backed up and restored to the target DB instance is normal. | To be tested |
|  | ListDbBackups | Obtain the backup list. | To be tested |
|  | ShowSourceInstanceDetail | Query the original DB instance information based on the time point or backup file. | To be tested |
| DR management | ShowCrossCloudDisasterInstanceMonitor | Query the real-time DR monitoring status of an instance. | To be tested |
|  | ExecuteCrossCloudDisasterRecoveryFailover | Switchover from DR to primary (delivered by the DR instance) | To be tested |
|  | ShowCrossCloudDisasterRelations | Query the DR relationship list. | To be tested |
|  | ExecuteCrossCloudReleaseDisaster | Disable DR (delivered from the master DR cluster). | To be tested |
|  | ExecuteCrossCloudDisasterDataCacheEnd | End the log retention function for Streaming DR. Currently, only Streaming DR supports this function. | To be tested |
|  | ExecuteCrossCloudDisasterDataCacheStart | The primary instance starts to retain DR logs. Currently, only Stream DR supports this function. | To be tested |
|  | ListDisasterRecoveryRecord | Query DR operation records. | To be tested |
|  | ExecuteCrossCloudDisasterSwitchover | DR switchover, which can be delivered on either end of the active/standby. | To be tested |
|  | ExecuteCrossCloudDisasterRestore | The DR switchback is supported when the flow DR switchover is selected to rebuild the DR relationship. | To be tested |
|  | ExecuteCrossCloudDisasterStartSimulation | Start the DR drill. Currently, only Stream DR is supported. | To be tested |
|  | ResetDrConfig | Reset the DR network configuration. 1. The system automatically creates an agency to authorize DBS to access VPC resources and query IaaS APIs. 2. Reset the DR network configuration of the instance. | To be tested |
|  | ExecuteCrossCloudDisasterEndSimulation | The DR drill for the DR instance is complete. Currently, only Stream DR is supported. | To be tested |
|  | CreateCrossCloudConstructDisaster | Set up the DR relationship (delivered from the master instance). | To be tested |
| Database management | StartInstance | Starts the database and supports node-level startup operations. | To be tested |
| Disk management | ShowInstanceDisk | Query the used storage space and maximum storage space of a specified DB instance. | To be tested |
| Engine version and specification | ListFlavors | Query database specifications. | To be tested |
|  | ListDatastores | Query the database engine version. | To be tested |
|  | ListAvailableFlavors | Query the list of flavor that can be modified for a DB instance. | To be tested |
|  | ListFlavorsDetails | Query the specifications of the database. | To be tested |
|  | ListInstanceEngineDetail | View the DB instance engine version distribution | To be tested |
|  | ListDatastoresDetails | Query the engine list. | To be tested |
|  | ListStorageTypes | Query the database disk type. | To be tested |
|  | ListDbFlavors | Query the specifications of the database. | To be tested |
|  | ListGaussDbDatastores | Query the engine list. | To be tested |
| Exclusive Instance Management | DeleteInstance | Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
|  | CreateInstance | Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore | To be tested |
| ITaskController | ListTasks | Obtain the task list | To be tested |
| Instance Management | CreateGaussDbInstance | Create a database instance. Only the new plane authentication mode (AK/SK authentication) of IAM5 is supported. | To be tested |
|  | SearchAutoEnlargePolicy | Query the automatic disk capacity expansion policy | To be tested |
|  | ShowDeploymentForm | Query the number of copies, shards, and nodes based on the solution template name or instance ID. | To be tested |
|  | ListDatabaseInstances | Querying the database instance list/Querying instance details | To be tested |
|  | ValidateWeakPassword | Verify the password security of the database user root. | To be tested |
|  | ListCnInfosBeforeReduce | Query the coordinator node list | To be tested |
|  | UpdateMysqlCompatibility | Updates the M-compatible port service configuration of a specified instance. | To be tested |
|  | ListInstancesDetails | Querying the database instance list/Querying instance details | To be tested |
|  | ResizeInstanceFlavor | GaussDB instance specification change | To be tested |
|  | RunInstanceAction | CN scale-out/DN shard scale-out/disk scale-out | To be tested |
|  | ShowProjectQuotas |  | To be tested |
|  | ShowSslCertDownloadLink | Query the SSL certificate download address of a DB instance. | To be tested |
|  | CreateDbInstance | Create a database instance | To be tested |
|  | ShowBalanceStatus | Check whether the active/standby switchover has occurred on the instance, resulting in load imbalance on the host. | To be tested |
|  | SwitchShard | You can perform active/standby switchover on one or multiple DN shards. Only one new standby node can be specified in a group to be switched to the active node. | To be tested |
|  | RestartInstance | Restarts a specified instance. | To be tested |
|  | ListBindedEips | Query the list of EIPs bound to an instance. | To be tested |
|  | StartMysqlCompatibility | Enables the M-compatible port of a specified instance. | To be tested |
|  | ListFeatures | Query the advanced feature list of the current instance. | To be tested |
|  | CreateDatabaseInstance | Create a database instance | To be tested |
|  | ListComponentInfos | Query the component list of an instance | To be tested |
|  | UpdateFeatures | Enable the advanced feature switch. | To be tested |
|  | ListInstanceDetails | Query the database instance list/Query the instance details | To be tested |
| Instance management | AttachEip | Associate and unbind an EIP. | To be tested |
|  | StopInstance | When an instance is stopped, you can temporarily stop the pay-per-use instance to save costs. By default, the instance will be stopped for seven days. | To be tested |
|  | UpdateInstanceName | Change the instance name. | To be tested |
| Lifecycle Management | ListInstances | Query the instance list of a tenant. Query by condition is supported. | To be tested |
| Log management | ShowErrorLogSwitchStatus | Query the status of the database error log collection function. | To be tested |
|  | ListInstanceErrorLogs | Query the link for downloading database error logs. | To be tested |
|  | CreateSlowLogDownload | Create slow log download information | To be tested |
|  | ShowSlowLogDownload | Query slow log download information | To be tested |
| Manage databases and users | CreateDatabaseSchemas | Create a database schema in the database of a specified DB instance. | To be tested |
|  | AllowDbRolePrivileges | Set the role permission in the database. | To be tested |
|  | ListDatabaseRoles | Query the database role list. | To be tested |
|  | CreateDbRole | Create a database role. | To be tested |
|  | AllowDbPrivileges | This API is used to set account permissions in the database of a specified instance. | To be tested |
|  | ListDatabaseSchemas | Query the database schema list of a specified DB instance. | To be tested |
|  | DeleteDatabaseSchema | Delete a database schema. | To be tested |
| Managing Databases and Users (MySQL) | CreateDatabase | Create a database. | To be tested |
|  | CreateDbUser | Create a database account in a specified instance. | To be tested |
|  | DeleteDatabase | Delete the database. | To be tested |
|  | ResetPwd | Resetting the database password. | To be tested |
|  | SetDbUserPwd | Setting the database account password | To be tested |
|  | ListDatabases | Query the database list. | To be tested |
|  | ListDbUsers | Query the database user list. | To be tested |
| Parameter Configuration | CreateConfigurationTemplate | Create a parameter template. | To be tested |
|  | UpdateInstanceConfiguration | Modifies the parameters of a specified instance. | To be tested |
|  | ShowInstanceConfiguration | Obtains the parameter template of a specified DB instance. | To be tested |
|  | ListParamGroupTemplates | Obtain the parameter template list, including the default parameter templates of all databases and the parameter templates created by users. | To be tested |
|  | CopyConfiguration | Copying a parameter template | To be tested |
|  | ListConfigurationsDiff | Obtain the difference list between two parameter configuration templates. | To be tested |
|  | ListHistoryOperations | Query the modification history of a parameter template. | To be tested |
|  | ShowConfigurationDetail | This API is used to obtain details about a parameter template based on the parameter template ID. | To be tested |
|  | ListParameterGroupTemplates | Obtain the parameter template list, including the default parameter templates of all databases and the parameter templates created by users. | To be tested |
|  | ListAppliedHistories | Query the application records of a parameter template by instance level. | To be tested |
|  | SwitchConfiguration | Specify a parameter template for changing an instance. | To be tested |
|  | ListApplicableInstances | Query the list of instances where the current parameter group template can be applied. | To be tested |
|  | ShowInstanceParamGroup | Obtains the parameter template of a specified DB instance. | To be tested |
|  | ValidateParaGroupName | Check whether the parameter group name exists. | To be tested |
|  | ShowInstanceParamGroupDetail | Obtains the parameter template of a specified DB instance. | To be tested |
|  | ShowParameterGroupDetail | This API is used to obtain details about a parameter template based on the parameter template ID. | To be tested |
|  | ListConfigurations | Obtain the parameter template list, including the default parameter templates of all databases and the parameter templates created by users. | To be tested |
|  | ResetConfiguration | Reset the parameter template. | To be tested |
|  | DeleteConfiguration | Delete a parameter template. | To be tested |
| Quota Management | ListEpsQuotas | Query the quota group information of an enterprise project. | To be tested |
|  | ModifyEpsQuota | Modify the enterprise project quota. | To be tested |
| Recycle bin | ShowRecyclePolicy | Query the recycling policy in the recycle bin. | To be tested |
|  | ListRecycleInstancesDetails | Query the list of all engine instances in the recycle bin. | To be tested |
|  | ListRecycleInstances | Query the instance information in the recycle bin | To be tested |
|  | SetRecyclePolicy | Set the recycle bin policy. | To be tested |
| SQL Traffic Limit | ListLimitTask | Query the list of rate limiting tasks based on the specified conditions. | To be tested |
|  | DeleteLimitTask | Delete a traffic limiting task based on the task_id. | To be tested |
|  | CreateLimitTask | Create a traffic limiting task based on the specific scope and type. | To be tested |
|  | ShowLimitTask | Query details about a rate limiting task | To be tested |
|  | SyncLimitData | Synchronize SQL rate limiting data on the kernel side to the management and control side | To be tested |
|  | ListNodeLimitSqlModel | Query the SQL template list of a node | To be tested |
|  | UpdateLimitTask | Update the traffic limiting task based on the new conditions. | To be tested |
| Tag Management | DeleteInstanceTag | Delete an instance label | To be tested |
|  | ListPredefinedTags | Query predefined tags. | To be tested |
|  | ListInstanceTags | Query the instance tag. | To be tested |
|  | AddInstanceTags | This API is used to add user tags to a specified instance. | To be tested |
| Tags | ListProjectTags | Query all tags of a specified resource type in a specified project | To be tested |
| Task Management | ListScheduleTask | View the scheduled task list | To be tested |
|  | CancelScheduleTask | Cancel the scheduled task | To be tested |
|  | DeleteScheduleTask | Delete the information about a scheduled task | To be tested |
|  | ShowJobDetail | Query the execution status of a job. This API is used to query the execution status of an SFS Turbo asynchronous API. For example, you can use the jobId returned by calling the interface for creating and binding LDAP configuration to query the execution status of a job. | To be tested |
|  | DeleteJob |  | To be tested |
| Version upgrade | UpgradeInstanceVersion | GaussDB(for openGauss) instance version. There are three upgrade modes: gray upgrade, local upgrade, and hot patch upgrade. | To be tested |
|  | ShowBatchUpgradeCandidateVersions | Query the versions and upgrade types that can be upgraded in batches. | To be tested |
|  | ShowUpgradeCandidateVersions | Query the version that can be upgraded. | To be tested |
|  | BatchShowUpgradeCandidateVersions | Query the versions and upgrade types that can be upgraded in batches. | To be tested |
|  | ShowUpgradeCandidateVersionsDetails | Query the version that can be upgraded. | To be tested |
|  | UpgradeInstancesVersion | Upgrade GaussDB instances in batches. There are three upgrade modes: gray upgrade, local upgrade, and hot patch upgrade. | To be tested |
|  | CreateScheduleTask | Upgrade the kernel versions of batch instances at a scheduled time | To be tested |

