# DCS MCP Server 


## Version
v0.1.0

## Overview

DCS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DCS. Full-chain management of DCS resources can be carried out based on natural language.

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
                    <td rowspan="7">Account management</td>
                    <td>CreateAclAccount</td>
                    <td>"Create an access account with read, write, and read permissions for Redis 4.0/5.0 DB instances (excluding cluster DB instances).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAclAccountRemark</td>
                    <td>ACL account modification remarks</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAclAccount</td>
                    <td>Modify the user type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAclAccounts</td>
                    <td>Query the ACL account list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAclAccountPassWord</td>
                    <td>Change the password of the ACL account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAclAccount</td>
                    <td>Delete the created common ACL account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetAclAccountPassWord</td>
                    <td>Reset the ACL account password.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Analyze full offline keys</td>
                    <td>CreateOfflineKeyAnalysis</td>
                    <td>Create an offline full key analysis task. Offline full key analysis is used to analyze the top 100 keys in the backup files of a specified node, the top 50 keys with the number of prefixes of each data type, and the memory usage and quantity distribution of keys of each data type. This command is supported only by Redis 4.0, 5.0, 6.0, and Redis Enterprise Edition instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOfflineKeyAnalysisTask</td>
                    <td>Query offline full key analysis details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOfflineKeyAnalysisTask</td>
                    <td>This command is used to query the list of offline full key analysis tasks. Redis 4.0, 5.0, 6.0, and Enterprise Redis are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOfflineKeyAnalysisTask</td>
                    <td>Delete an offline full key analysis record.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Background Task Management</td>
                    <td>ExportExcelJob</td>
                    <td>Query the details of an instance list export task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackgroundTask</td>
                    <td>Delete a specified record in background task management.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackgroundTask</td>
                    <td>Query the background task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceResizeCheckJob</td>
                    <td>Submit the precheck task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCenterTask</td>
                    <td>Querying the Task Center Task List</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackgroundTaskProgress</td>
                    <td>Query background task details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobInfo</td>
                    <td>Query the job execution result of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCenterTask</td>
                    <td>Delete Task Center Task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Backup and Restore</td>
                    <td>ListBackupRecords</td>
                    <td>Query the backup information list of a specified DCS instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyInstance</td>
                    <td>Backs up the specified DCS instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackupFile</td>
                    <td>Delete the backup files of the DCS instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreRecords</td>
                    <td>Query the restoration records of a specified DCS instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackupFileLinks</td>
                    <td>Obtain the backup file download link of a specified DB instance and download the backup file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Backup management</td>
                    <td>RestoreInstance</td>
                    <td>Restoring to the current DB instance from a backup</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Bandwidth</td>
                    <td>UpdateBandwidth</td>
                    <td>Update the bandwidth.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="18">Cache Analysis</td>
                    <td>UpdateExpireAutoScanConfig</td>
                    <td>Modifying the automatic scanning configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadHotKey</td>
                    <td>Download the hot key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBigkeyAutoscanConfig</td>
                    <td>Query the automatic analysis configuration of a big key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHotkeyAutoscanConfig</td>
                    <td>Query the hot key automatic analysis configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHotkeyTaskDetails</td>
                    <td>Query hot key analysis details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBigkeyScanTask</td>
                    <td>Create a big key analysis task for the Redis instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHotkeyScanTask</td>
                    <td>Create a hot key analysis task. Redis 3.0 does not support hot key analysis.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHotkeyAutoScanConfig</td>
                    <td>Set the hot key automatic analysis configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowExpireKeyScanInfo</td>
                    <td>Query expired key scanning records</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHotKeyScanTasks</td>
                    <td>Query historical hot key analysis records.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBigkeyScanTasks</td>
                    <td>Query the list of big key analysis tasks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowExpireAutoScanConfig</td>
                    <td>Query the automatic scanning configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBigkeyAutoscanConfig</td>
                    <td>Set the automatic analysis configuration of the big key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBigkeyScanTask</td>
                    <td>Delete a big key analysis record.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBigkeyScanTaskDetails</td>
                    <td>Query big key analysis details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ScanExpireKey</td>
                    <td>Scan expired keys immediately</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHotkeyScanTask</td>
                    <td>Delete a hot key analysis task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutoExpireScanTask</td>
                    <td>Create an expired key scanning task. Redis 3.0 does not support expired key scanning.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Certificate Label Management</td>
                    <td>BatchCreateOrDeleteTags</td>
                    <td>Create or delete tags in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">Data Migration</td>
                    <td>StopMigrationTask</td>
                    <td>Stop the data migration task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMigrationTask</td>
                    <td>Create a data migration task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopMigrationTaskSync</td>
                    <td>Stop the data migration task synchronously.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMigrationTask</td>
                    <td>Delete a data migration task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMigrationTask</td>
                    <td>Query the details of a migration task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRestartOnlineMigrationTasks</td>
                    <td>Restart online migration tasks in batches. The interface sends a success response and the delivery result of restarting the online migration tasks is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetOnlineMigrationTask</td>
                    <td>Configure an online data migration task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMigrationTaskStats</td>
                    <td>Query online migration progress details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollbackExchangeInstanceIp</td>
                    <td>IP address swap rollback.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMigrationTask</td>
                    <td>Set the automatic reconnection for the migration task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExchangeInstanceIp</td>
                    <td>IP exchange</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopMigrationTasks</td>
                    <td>If the interface sends a response indicating that data migration tasks are stopped in batches, the task is delivered successfully. If the status of the migration task is Terminused, the migration task is stopped successfully.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMigrationTaskLogs</td>
                    <td>Query the migration log list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMigrationTask</td>
                    <td>Query the migration task list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOnlineMigrationTask</td>
                    <td>Create an online data migration task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">EIP</td>
                    <td>UpdatePublicIp</td>
                    <td>Updates EIP information, which is used to unbind EIPs and bind relationships between EIPs and VIPs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePublicIp</td>
                    <td>Delete an EIP based on the EIP ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Engine version and specification</td>
                    <td>ListFlavors</td>
                    <td>Query database specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Exclusive Instance Management</td>
                    <td>CreateInstance</td>
                    <td>Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">IP trustlist management</td>
                    <td>ShowIpWhitelist</td>
                    <td>Query the IP address trustlist of a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIpWhitelist</td>
                    <td>Sets IP address trustlist groups for a specified instance, including creating, disabling, editing, and deleting the trustlist.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="22">Instance Management</td>
                    <td>UpdatePassword</td>
                    <td>Change the password of the DCS instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateAz</td>
                    <td>Migrate an instance to an AZ.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClientIpTransparentTransmission</td>
                    <td>Enable or disable transparent transmission of client IP addresses.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBandwidths</td>
                    <td>Obtain the bandwidth of each slice of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceTopology</td>
                    <td>Query the cluster instance topology.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartOrFlushInstances</td>
                    <td>Restart the running DCS instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceBandwidth</td>
                    <td>Changing the bandwidth of a specified DB instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNumberOfInstancesInDifferentStatus</td>
                    <td>Query the number of instances in different states in the current region of the tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeInstanceMinorVersion</td>
                    <td>Upgrade the instance minor version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceVersion</td>
                    <td>Obtain the kernel version number of the corresponding instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeNodesStartStopStatus</td>
                    <td>Start and stop an instance node. Within 24 hours before the node is stopped, back up data of the instance (except single-node instances).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstanceBandwidthAutoScalingPolicy</td>
                    <td>Delete the instance bandwidth scaling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportInstancesTask</td>
                    <td>Export instance resources asynchronously</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStatisticsOfRunningInstances</td>
                    <td>Query the statistics of DCS instances in the Running state of the current tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPassword</td>
                    <td>Reset the password (only for instances with SSL enabled).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceBandwidthAutoScalingPolicy</td>
                    <td>This API is used to update the instance bandwidth scaling policy. Currently, the DB instance bandwidth cannot be automatically scaled back.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeMasterStandby</td>
                    <td>Switch the active/standby node. Only the primary and standby DB instances support this operation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeMasterStandbyAsync</td>
                    <td>Asynchronous exchange instance active/standby node</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigHistoryDetail</td>
                    <td>Query the parameter modification details of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteClusterSwitchover</td>
                    <td>Cluster shard switchover, applicable to proxy and cluster instances</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceOperations</td>
                    <td>Querying whether an instance can be scaled out</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceBandwidthAutoScalingPolicy</td>
                    <td>Query the bandwidth scaling policy of a DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Instance diagnosis</td>
                    <td>CreateDiagnosisTask</td>
                    <td>Diagnose the specified DCS instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDiagnosisTask</td>
                    <td>Delete a diagnosis record.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDiagnosisTaskDetails</td>
                    <td>Query details about a diagnosis report by report ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDiagnosisTasks</td>
                    <td>Query the diagnosis task list of a specified DCS instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Lifecycle Management</td>
                    <td>UpdateInstance</td>
                    <td>Modifies the name and description of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResizeOrder</td>
                    <td>Change the specification of a yearly/monthly DB instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteInstances</td>
                    <td>Delete instances in batches. After the instance is deleted, the original data in the instance will be deleted and no backup will be performed. Exercise caution when performing this operation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateDeletableReplica</td>
                    <td>Check whether cluster copies can be deleted</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>Query the instance list of a tenant. Query by condition is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSingleInstance</td>
                    <td>This API is used to delete a specified DCS instance and release all resources of the instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Log management</td>
                    <td>CreateRedislogDownloadLink</td>
                    <td>Obtains the link for downloading logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowlog</td>
                    <td>Query slow logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRedislog</td>
                    <td>Collect Redis run logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRedislog</td>
                    <td>Query the Redis run log list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Network security</td>
                    <td>UpdateSslSwitch</td>
                    <td>Enables or disables SSL. Currently, this API applies only to Redis 6.0 basic edition instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIpWhitelistAsync</td>
                    <td>This API is used to set IP address trustlist groups for a specified DB instance, including creating, disabling, editing, and deleting IP address trustlist groups. Return the jobId of the asynchronous task. The trustlist group information will overwrite the existing trustlist information. Therefore, when adding an IP address trustlist group, retain the existing trustlist information and edit the new trustlist group information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadSslCert</td>
                    <td>Download the SSL certificate of an instance. Currently, this API applies only to Redis 6.0 basic edition instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceSslDetail</td>
                    <td>Query the SSL information about an instance. Currently, this API applies only to Redis 6.0 basic edition instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Other interfaces</td>
                    <td>ListMonitoredObjects</td>
                    <td>Query the main dimension object list. Currently, the main dimension ID can be dcs_instance_id,dcs_memcached_instance_id.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowQuotaOfTenant</td>
                    <td>Query the default number of instances that can be created by a tenant, the quota limit of the total memory, and the maximum and minimum quotas that can be applied for by the tenant. Tenants may have different quotas in different regions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCommandMobilization</td>
                    <td>Log in to the web-cli and run the Redis command.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMaintenanceWindows</td>
                    <td>Query the start time and end time of the maintenance time window.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LoginWebCli</td>
                    <td>Login to the webCli</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMonitoredObjectsOfInstance</td>
                    <td>Query the list of monitored objects in subdimensions of a primary dimension. Currently, the IDs of subdimensions can be dcs_instance_id.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableZones</td>
                    <td>When creating an instance, you need to configure the ID of the AZ where the instance is located. You can use this API to query the ID of the AZ.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LogoffWebCli</td>
                    <td>Log out of the webCli</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Parameter Configuration</td>
                    <td>ListConfigurations</td>
                    <td>Obtain the parameter template list, including the default parameter templates of all databases and the parameter templates created by users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Parameter management</td>
                    <td>UpdateConfigurations</td>
                    <td>To ensure the optimal performance of DCS, you can adjust the running parameters of DCS instances based on your service requirements.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConfig</td>
                    <td>To ensure the optimal performance of DCS, you can adjust the running parameters of DCS instances as required.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigHistories</td>
                    <td>Query the parameter modification records of an instance. The query can be based on keywords.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Session management</td>
                    <td>HangUpKillAllClients</td>
                    <td>Deliver the task of killing all sessions on a specified node or instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClients</td>
                    <td>Obtain the session list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>HangUpClients</td>
                    <td>kill the specified session</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ScanClients</td>
                    <td>Deliver the task of querying the session list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Shard and Replica</td>
                    <td>DeleteIpFromDomainName</td>
                    <td>Remove the IP address of the read replica from the domain name. After the IP address is successfully removed, the domain name will not be resolved to the IP address of the read replica.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowNodesInformation</td>
                    <td>Query the node information, number of valid instances, and number of nodes of all instances of a specified project in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGroupReplicationInfo</td>
                    <td>Query shards and replicas of read/write isolation instances and cluster instances. Read/write isolation instances are supported only by active/standby instances of Redis 4.0 and Redis 5.0.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNodesInformation</td>
                    <td>Query the node information of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSlavePriority</td>
                    <td>Set the priority of the copy. When the primary node is faulty, the standby node with a smaller weight has a higher priority for switching to the primary node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReplicationStates</td>
                    <td>Obtain the copy status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Specification Change Management</td>
                    <td>ResizeInstance</td>
                    <td>The instance specification is changed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tag Management</td>
                    <td>ListTagsOfTenant</td>
                    <td>Query the collection of all resource tags of a tenant instance type in a specified project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTags</td>
                    <td>Query tags by instance ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Template Management</td>
                    <td>CreateCustomTemplate</td>
                    <td>Create a custom template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigTemplate</td>
                    <td>Query parameter template details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConfigTemplate</td>
                    <td>Delete a user-defined template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigTemplates</td>
                    <td>Query the parameter template list of a tenant. Query by condition is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfigTemplate</td>
                    <td>Modifying a user-defined template</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
