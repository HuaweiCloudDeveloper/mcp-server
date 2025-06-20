# DCS MCP Server 


## Version
v0.1.0

## Overview

DCS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DCS. Full-chain management of DCS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Account management | CreateAclAccount | "Create an access account with read, write, and read permissions for Redis 4.0/5.0 DB instances (excluding cluster DB instances). | To be tested |
|  | UpdateAclAccountRemark | ACL account modification remarks | To be tested |
|  | UpdateAclAccount | Modify the user type. | To be tested |
|  | ListAclAccounts | Query the ACL account list. | To be tested |
|  | UpdateAclAccountPassWord | Change the password of the ACL account. | To be tested |
|  | DeleteAclAccount | Delete the created common ACL account. | To be tested |
|  | ResetAclAccountPassWord | Reset the ACL account password. | To be tested |
| Analyze full offline keys | CreateOfflineKeyAnalysis | Create an offline full key analysis task. Offline full key analysis is used to analyze the top 100 keys in the backup files of a specified node, the top 50 keys with the number of prefixes of each data type, and the memory usage and quantity distribution of keys of each data type. This command is supported only by Redis 4.0, 5.0, 6.0, and Redis Enterprise Edition instances. | To be tested |
|  | ShowOfflineKeyAnalysisTask | Query offline full key analysis details. | To be tested |
|  | ListOfflineKeyAnalysisTask | This command is used to query the list of offline full key analysis tasks. Redis 4.0, 5.0, 6.0, and Enterprise Redis are supported. | To be tested |
|  | DeleteOfflineKeyAnalysisTask | Delete an offline full key analysis record. | To be tested |
| Background Task Management | ExportExcelJob | Query the details of an instance list export task | To be tested |
|  | DeleteBackgroundTask | Delete a specified record in background task management. | To be tested |
|  | ListBackgroundTask | Query the background task list | To be tested |
|  | StartInstanceResizeCheckJob | Submit the precheck task | To be tested |
|  | ListCenterTask | Querying the Task Center Task List | To be tested |
|  | ShowBackgroundTaskProgress | Query background task details | To be tested |
|  | ShowJobInfo | Query the job execution result of a tenant. | To be tested |
|  | DeleteCenterTask | Delete Task Center Task | To be tested |
| Backup and Restore | ListBackupRecords | Query the backup information list of a specified DCS instance. | To be tested |
|  | CopyInstance | Backs up the specified DCS instance. | To be tested |
|  | DeleteBackupFile | Delete the backup files of the DCS instance. | To be tested |
|  | ListRestoreRecords | Query the restoration records of a specified DCS instance. | To be tested |
|  | ListBackupFileLinks | Obtain the backup file download link of a specified DB instance and download the backup file. | To be tested |
| Backup management | RestoreInstance | Restoring to the current DB instance from a backup | To be tested |
| Bandwidth | UpdateBandwidth | Update the bandwidth. | To be tested |
| Cache Analysis | UpdateExpireAutoScanConfig | Modifying the automatic scanning configuration | To be tested |
|  | DownloadHotKey | Download the hot key. | To be tested |
|  | ShowBigkeyAutoscanConfig | Query the automatic analysis configuration of a big key. | To be tested |
|  | ShowHotkeyAutoscanConfig | Query the hot key automatic analysis configuration. | To be tested |
|  | ShowHotkeyTaskDetails | Query hot key analysis details. | To be tested |
|  | CreateBigkeyScanTask | Create a big key analysis task for the Redis instance. | To be tested |
|  | CreateHotkeyScanTask | Create a hot key analysis task. Redis 3.0 does not support hot key analysis. | To be tested |
|  | UpdateHotkeyAutoScanConfig | Set the hot key automatic analysis configuration. | To be tested |
|  | ShowExpireKeyScanInfo | Query expired key scanning records | To be tested |
|  | ListHotKeyScanTasks | Query historical hot key analysis records. | To be tested |
|  | ListBigkeyScanTasks | Query the list of big key analysis tasks. | To be tested |
|  | ShowExpireAutoScanConfig | Query the automatic scanning configuration | To be tested |
|  | UpdateBigkeyAutoscanConfig | Set the automatic analysis configuration of the big key. | To be tested |
|  | DeleteBigkeyScanTask | Delete a big key analysis record. | To be tested |
|  | ShowBigkeyScanTaskDetails | Query big key analysis details. | To be tested |
|  | ScanExpireKey | Scan expired keys immediately | To be tested |
|  | DeleteHotkeyScanTask | Delete a hot key analysis task. | To be tested |
|  | CreateAutoExpireScanTask | Create an expired key scanning task. Redis 3.0 does not support expired key scanning. | To be tested |
| Certificate Label Management | BatchCreateOrDeleteTags | Create or delete tags in batches. | To be tested |
| Data Migration | StopMigrationTask | Stop the data migration task. | To be tested |
|  | CreateMigrationTask | Create a data migration task. | To be tested |
|  | StopMigrationTaskSync | Stop the data migration task synchronously. | To be tested |
|  | DeleteMigrationTask | Delete a data migration task. | To be tested |
|  | ShowMigrationTask | Query the details of a migration task. | To be tested |
|  | BatchRestartOnlineMigrationTasks | Restart online migration tasks in batches. The interface sends a success response and the delivery result of restarting the online migration tasks is returned. | To be tested |
|  | SetOnlineMigrationTask | Configure an online data migration task. | To be tested |
|  | ShowMigrationTaskStats | Query online migration progress details. | To be tested |
|  | RollbackExchangeInstanceIp | IP address swap rollback. | To be tested |
|  | UpdateMigrationTask | Set the automatic reconnection for the migration task | To be tested |
|  | ExchangeInstanceIp | IP exchange | To be tested |
|  | BatchStopMigrationTasks | If the interface sends a response indicating that data migration tasks are stopped in batches, the task is delivered successfully. If the status of the migration task is Terminused, the migration task is stopped successfully. | To be tested |
|  | ListMigrationTaskLogs | Query the migration log list | To be tested |
|  | ListMigrationTask | Query the migration task list. | To be tested |
|  | CreateOnlineMigrationTask | Create an online data migration task. | To be tested |
| EIP | UpdatePublicIp | Updates EIP information, which is used to unbind EIPs and bind relationships between EIPs and VIPs. | To be tested |
|  | DeletePublicIp | Delete an EIP based on the EIP ID. | To be tested |
| Engine version and specification | ListFlavors | Query database specifications. | To be tested |
| Exclusive Instance Management | CreateInstance | Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore | To be tested |
|  | ShowInstance | Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
| IP trustlist management | ShowIpWhitelist | Query the IP address trustlist of a specified instance. | To be tested |
|  | UpdateIpWhitelist | Sets IP address trustlist groups for a specified instance, including creating, disabling, editing, and deleting the trustlist. | To be tested |
| Instance Management | UpdatePassword | Change the password of the DCS instance. | To be tested |
|  | MigrateAz | Migrate an instance to an AZ. | To be tested |
|  | UpdateClientIpTransparentTransmission | Enable or disable transparent transmission of client IP addresses. | To be tested |
|  | ShowBandwidths | Obtain the bandwidth of each slice of an instance. | To be tested |
|  | ShowInstanceTopology | Query the cluster instance topology. | To be tested |
|  | RestartOrFlushInstances | Restart the running DCS instance. | To be tested |
|  | UpdateInstanceBandwidth | Changing the bandwidth of a specified DB instance | To be tested |
|  | ListNumberOfInstancesInDifferentStatus | Query the number of instances in different states in the current region of the tenant. | To be tested |
|  | UpgradeInstanceMinorVersion | Upgrade the instance minor version. | To be tested |
|  | ShowInstanceVersion | Obtain the kernel version number of the corresponding instance. | To be tested |
|  | ChangeNodesStartStopStatus | Start and stop an instance node. Within 24 hours before the node is stopped, back up data of the instance (except single-node instances). | To be tested |
|  | DeleteInstanceBandwidthAutoScalingPolicy | Delete the instance bandwidth scaling policy. | To be tested |
|  | ExportInstancesTask | Export instance resources asynchronously | To be tested |
|  | ListStatisticsOfRunningInstances | Query the statistics of DCS instances in the Running state of the current tenant. | To be tested |
|  | ResetPassword | Reset the password (only for instances with SSL enabled). | To be tested |
|  | UpdateInstanceBandwidthAutoScalingPolicy | This API is used to update the instance bandwidth scaling policy. Currently, the DB instance bandwidth cannot be automatically scaled back. | To be tested |
|  | ChangeMasterStandby | Switch the active/standby node. Only the primary and standby DB instances support this operation. | To be tested |
|  | ChangeMasterStandbyAsync | Asynchronous exchange instance active/standby node | To be tested |
|  | ShowConfigHistoryDetail | Query the parameter modification details of an instance. | To be tested |
|  | ExecuteClusterSwitchover | Cluster shard switchover, applicable to proxy and cluster instances | To be tested |
|  | ListInstanceOperations | Querying whether an instance can be scaled out | To be tested |
|  | ShowInstanceBandwidthAutoScalingPolicy | Query the bandwidth scaling policy of a DB instance. | To be tested |
| Instance diagnosis | CreateDiagnosisTask | Diagnose the specified DCS instance. | To be tested |
|  | DeleteDiagnosisTask | Delete a diagnosis record. | To be tested |
|  | ShowDiagnosisTaskDetails | Query details about a diagnosis report by report ID. | To be tested |
|  | ListDiagnosisTasks | Query the diagnosis task list of a specified DCS instance. | To be tested |
| Lifecycle Management | UpdateInstance | Modifies the name and description of an instance. | To be tested |
|  | CreateResizeOrder | Change the specification of a yearly/monthly DB instance | To be tested |
|  | BatchDeleteInstances | Delete instances in batches. After the instance is deleted, the original data in the instance will be deleted and no backup will be performed. Exercise caution when performing this operation. | To be tested |
|  | ValidateDeletableReplica | Check whether cluster copies can be deleted | To be tested |
|  | ListInstances | Query the instance list of a tenant. Query by condition is supported. | To be tested |
|  | DeleteSingleInstance | This API is used to delete a specified DCS instance and release all resources of the instance. | To be tested |
| Log management | CreateRedislogDownloadLink | Obtains the link for downloading logs. | To be tested |
|  | ListSlowlog | Query slow logs. | To be tested |
|  | CreateRedislog | Collect Redis run logs. | To be tested |
|  | ListRedislog | Query the Redis run log list. | To be tested |
| Network security | UpdateSslSwitch | Enables or disables SSL. Currently, this API applies only to Redis 6.0 basic edition instances. | To be tested |
|  | UpdateIpWhitelistAsync | This API is used to set IP address trustlist groups for a specified DB instance, including creating, disabling, editing, and deleting IP address trustlist groups. Return the jobId of the asynchronous task. The trustlist group information will overwrite the existing trustlist information. Therefore, when adding an IP address trustlist group, retain the existing trustlist information and edit the new trustlist group information. | To be tested |
|  | DownloadSslCert | Download the SSL certificate of an instance. Currently, this API applies only to Redis 6.0 basic edition instances. | To be tested |
|  | ShowInstanceSslDetail | Query the SSL information about an instance. Currently, this API applies only to Redis 6.0 basic edition instances. | To be tested |
| Other interfaces | ListMonitoredObjects | Query the main dimension object list. Currently, the main dimension ID can be dcs_instance_id,dcs_memcached_instance_id. | To be tested |
|  | ShowQuotaOfTenant | Query the default number of instances that can be created by a tenant, the quota limit of the total memory, and the maximum and minimum quotas that can be applied for by the tenant. Tenants may have different quotas in different regions. | To be tested |
|  | ExecuteCommandMobilization | Log in to the web-cli and run the Redis command. | To be tested |
|  | ListMaintenanceWindows | Query the start time and end time of the maintenance time window. | To be tested |
|  | LoginWebCli | Login to the webCli | To be tested |
|  | ListMonitoredObjectsOfInstance | Query the list of monitored objects in subdimensions of a primary dimension. Currently, the IDs of subdimensions can be dcs_instance_id. | To be tested |
|  | ListAvailableZones | When creating an instance, you need to configure the ID of the AZ where the instance is located. You can use this API to query the ID of the AZ. | To be tested |
|  | LogoffWebCli | Log out of the webCli | To be tested |
| Parameter Configuration | ListConfigurations | Obtain the parameter template list, including the default parameter templates of all databases and the parameter templates created by users. | To be tested |
| Parameter management | UpdateConfigurations | To ensure the optimal performance of DCS, you can adjust the running parameters of DCS instances based on your service requirements. | To be tested |
|  | UpdateInstanceConfig | To ensure the optimal performance of DCS, you can adjust the running parameters of DCS instances as required. | To be tested |
|  | ListConfigHistories | Query the parameter modification records of an instance. The query can be based on keywords. | To be tested |
| Session management | HangUpKillAllClients | Deliver the task of killing all sessions on a specified node or instance | To be tested |
|  | ListClients | Obtain the session list | To be tested |
|  | HangUpClients | kill the specified session | To be tested |
|  | ScanClients | Deliver the task of querying the session list | To be tested |
| Shard and Replica | DeleteIpFromDomainName | Remove the IP address of the read replica from the domain name. After the IP address is successfully removed, the domain name will not be resolved to the IP address of the read replica. | To be tested |
|  | BatchShowNodesInformation | Query the node information, number of valid instances, and number of nodes of all instances of a specified project in batches. | To be tested |
|  | ListGroupReplicationInfo | Query shards and replicas of read/write isolation instances and cluster instances. Read/write isolation instances are supported only by active/standby instances of Redis 4.0 and Redis 5.0. | To be tested |
|  | ShowNodesInformation | Query the node information of a specified DB instance. | To be tested |
|  | UpdateSlavePriority | Set the priority of the copy. When the primary node is faulty, the standby node with a smaller weight has a higher priority for switching to the primary node. | To be tested |
|  | ShowReplicationStates | Obtain the copy status. | To be tested |
| Specification Change Management | ResizeInstance | The instance specification is changed. | To be tested |
| Tag Management | ListTagsOfTenant | Query the collection of all resource tags of a tenant instance type in a specified project. | To be tested |
|  | ShowTags | Query tags by instance ID. | To be tested |
| Template Management | CreateCustomTemplate | Create a custom template | To be tested |
|  | ShowConfigTemplate | Query parameter template details | To be tested |
|  | DeleteConfigTemplate | Delete a user-defined template | To be tested |
|  | ListConfigTemplates | Query the parameter template list of a tenant. Query by condition is supported. | To be tested |
|  | UpdateConfigTemplate | Modifying a user-defined template | To be tested |

