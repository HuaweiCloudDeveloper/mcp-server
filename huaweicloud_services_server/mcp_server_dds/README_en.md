# DDS MCP Server 


## Version
v0.1.0

## Overview

DDS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DDS. Full-chain management of DDS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Backup and Restore | BatchDeleteBackup | This API is used to delete manual backups of database instances in batches. | To be tested |
|  | ListBackups | Obtain the backup list. | To be tested |
|  | CreateManualBackup | Create a manual backup. | To be tested |
|  | ShowBackupDownloadLink | Obtain the backup download link. | To be tested |
|  | ListRestoreDatabases | Obtain the list of databases that can be recovered. | To be tested |
|  | ListRestoreCollections | Obtain the list of recoverable database sets. | To be tested |
|  | RestoreInstanceFromCollection | Database and table-level data is restored to a point in time. | To be tested |
|  | StopBackup | Stopping creating a backup | To be tested |
|  | RestoreNewInstance | This API is used to restore a new DB instance from the backup. | To be tested |
|  | SetBackupPolicy | Set the automatic backup policy. | To be tested |
|  | ListRestoreTimes | Query the recoverable time segment. | To be tested |
|  | DeleteManualBackup | Delete a manual backup. | To be tested |
|  | ShowBackupPolicy | Query the automatic backup policy. | To be tested |
| Backup management | RestoreInstance | Restoring to the current DB instance from a backup | To be tested |
| Connection management | ShowConnectionStatistics | Query the statistics on the number of connections between the client IP address and the DDS database instance. | To be tested |
|  | DeleteSession | Terminates the instance node session. | To be tested |
|  | ListSessions | Query the session of an instance node. | To be tested |
| Database O&M | SwitchInstancePrimary | Replica sets, shards, and config standby nodes can be forcibly promoted to primary. | To be tested |
|  | DeleteKillOpRuleList | Delete the killOp rule. | To be tested |
|  | ShowKillOpRuleRuleList | Obtain the killOp rule list. | To be tested |
|  | UpdateKillOpRule | Enable or disable the killOp rule. | To be tested |
|  | CreateKillOpRule | Create a killOp rule. | To be tested |
| Database permission management | CreateDatabaseUser | Create a database user or role. | To be tested |
|  | ListDatabaseUsers | Query all database users and roles. | To be tested |
|  | DeleteDatabaseUser | Delete a database user. | To be tested |
| Database security | SwitchSsl | Set SSL data encryption. | To be tested |
| Engine version and specification | ListFlavorInfos | Query the instance specifications that match the specified criteria. | To be tested |
|  | ListDatastoreVersions | Query the database version information of a specified DB instance type. | To be tested |
|  | ListStorageType | Query the database disk type in the current region. | To be tested |
|  | ListFlavors | Query database specifications. | To be tested |
| Exclusive Instance Management | CreateInstance | Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore | To be tested |
|  | DeleteInstance | Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
| ITaskController | ListTasks | Obtain the task list | To be tested |
| Instance Management | CheckWeakPassword | Checking weak passwords | To be tested |
|  | ExpandReplicasetNode | Expand the number of nodes in a specified replica set instance | To be tested |
|  | SwitchoverReplicaSet | Switch the active/standby node in the replica set instance | To be tested |
|  | UpdateLtsConfig | Associate instance logs with LTS log streams. The background automatically uploads instance logs to the associated LTS log streams. | To be tested |
|  | ListLtsConfigs | Query the LTS log configuration information. | To be tested |
|  | CancelEip | Unbinds an EIP from a node in the instance. | To be tested |
|  | ShowUpgradeDuration | Query the estimated database patch upgrade duration | To be tested |
|  | ResizeInstanceVolume | Storage capacity related to the instance to be scaled up. | To be tested |
|  | AttachInternalIp | Change the private IP address of the instance | To be tested |
|  | DeleteReadonlyNode | When a read-only node is added to a replica set, you need to call this API to delete the read-only node. | To be tested |
|  | DeleteMongosNode | Call this API when the mongos nodes need to be reduced in a cluster instance. | To be tested |
|  | ShowClientNetwork | Query the cross-network segment access configuration of a replica set | To be tested |
|  | ListSslCertDownloadAddress | Obtain the SSL certificate download address. | To be tested |
|  | UpdateClientNetwork | Configure the cross-network segment access of replica sets. | To be tested |
|  | UpdateInstanceRemark | Modifies the instance remarks. | To be tested |
|  | ShrinkInstanceNodes | Delete the instance node. | To be tested |
|  | UpdateInstancePort | Change the port number of the database instance. | To be tested |
|  | ResetPassword | Reset the password (only for instances with SSL enabled). | To be tested |
|  | SwitchSecondLevelMonitoring | Enables or disables second-level monitoring for a specified instance. | To be tested |
|  | ListAz2Migrate | Query the AZ to which the DB instance can be migrated. | To be tested |
|  | SetAutoEnlargePolicies | Set the automatic disk capacity expansion policy. | To be tested |
|  | DeleteLtsConfig | Disassociate instance logs from the LTS log stream. The background cancels the upload of instance logs to the LTS log stream. | To be tested |
|  | UpgradeDatabaseVersion | Upgrade the database patch version. | To be tested |
|  | ShowReplSetName | Query the name of a database replica set | To be tested |
|  | AddReadonlyNode | This API is used to add a read node to a DDS replica set instance. | To be tested |
|  | CreateIp | Shard/Config IP address for creating a cluster | To be tested |
|  | MigrateAz | Migrate an instance to an AZ. | To be tested |
|  | BatchUpgradeDatabaseVersion | Upgrade database patch versions in batches. | To be tested |
|  | AddShardingNode | This API is used to expand the number of nodes in a specified cluster instance. | To be tested |
|  | ShowSecondLevelMonitoringStatus | Query the second-level monitoring configuration. | To be tested |
|  | ShowDiskUsage | Query the instance disk information | To be tested |
|  | UpdateReplSetName | Changing the name of a database replica set | To be tested |
|  | RestartInstance | Restarts a specified instance. | To be tested |
| Instance management | UpdateInstanceName | Change the instance name. | To be tested |
|  | ChangeOpsWindow | Set the maintenance time segment | To be tested |
|  | ShowAutoEnlargePolicy | Query the automatic storage capacity expansion policy of a DB instance | To be tested |
|  | AttachEip | Associate and unbind an EIP. | To be tested |
| Lifecycle Management | ListInstances | Query the instance list of a tenant. Query by condition is supported. | To be tested |
| Manage databases and users | ListDatabaseRoles | Query the database role list. | To be tested |
|  | CheckPassword | Check the database password. | To be tested |
|  | CreateDatabaseRole | Create a database role. | To be tested |
|  | SetBalancerSwitch | Set the cluster balancing switch. | To be tested |
|  | DeleteDatabaseRole | Delete a database role. | To be tested |
|  | SetBalancerWindow | Set the active time window for cluster balancing. | To be tested |
|  | ShowShardingBalancer | Query cluster balancing settings. | To be tested |
| Managing Databases and Users (MySQL) | ListDatabases | Query the database list. | To be tested |
| Obtain log information | ListLtsErrorLogs | Query database error logs. | To be tested |
|  | DownloadErrorlog | Obtain the link for downloading error logs. | To be tested |
|  | SwitchSlowlogDesensitization | Sets the plaintext switch for slow logs of an instance. | To be tested |
|  | DownloadSlowlog | Obtain the link for downloading slow logs. | To be tested |
|  | ListLtsSlowLogs | Query slow database logs. | To be tested |
|  | ShowAuditlogPolicy | Query the audit log policy. | To be tested |
|  | ListErrorLogs | Query database error logs. | To be tested |
|  | ListAuditlogs | Obtain the audit log list. | To be tested |
|  | SetAuditlogPolicy | Set the audit log policy. | To be tested |
|  | ListAuditlogLinks | Obtain the link for downloading audit logs. | To be tested |
|  | DeleteAuditLog | Delete audit logs | To be tested |
|  | ShowSlowlogDesensitizationSwitch | Querying the plaintext of slow logs | To be tested |
|  | ListSlowLogs | Query slow database logs. | To be tested |
| OpenStack - API version information | ListApiVersion | All available API versions (only for native OpenStack APIs) are returned. | To be tested |
| Parameter Configuration | ShowInstanceConfigurationModifyHistory | Query the modification history of instance parameters. | To be tested |
|  | ListAppliedInstances | Query the instances where the specified parameter template can be applied. | To be tested |
|  | ValidateConfigurationName | Verifies whether the parameter template name exists. | To be tested |
|  | ResetConfiguration | Reset the parameter template. | To be tested |
|  | ListConfigurations | Obtain the parameter template list, including the default parameter templates of all databases and the parameter templates created by users. | To be tested |
|  | ShowConfigurationAppliedHistory | Querying the application history of a parameter template | To be tested |
|  | UpdateEntityConfiguration | Modifies the parameters of a specified instance, which can be the parameter template of an instance, group, or node. | To be tested |
|  | ShowEntityConfiguration | Obtains the parameters of a specified DB instance, which can be the parameter template of an DB instance, a group, or a node. | To be tested |
|  | CompareConfiguration | Compare the differences between two parameter templates. | To be tested |
|  | SwitchConfiguration | Specify a parameter template for changing an instance. | To be tested |
|  | UpdateConfigurationParameter | Modifies the parameter information of a specified parameter template, including the name, description, and value of a specified parameter. | To be tested |
|  | CopyConfiguration | Copying a parameter template | To be tested |
|  | CreateConfiguration | Create a parameter template. | To be tested |
|  | ShowConfigurationModifyHistory | Query the modification history of a parameter template. | To be tested |
|  | DeleteConfiguration | Delete a parameter template. | To be tested |
|  | ShowConfigurationParameter | Obtain the details about a parameter template. | To be tested |
| Query version operation | ShowApiVersion | Query the details about a specified TMS API version. | To be tested |
| Quota | ShowQuotas | Query the resource quota of the current project. | To be tested |
| Recycle bin | ShowRecyclePolicy | Query the recycling policy in the recycle bin. | To be tested |
|  | SetRecyclePolicy | Set the recycle bin policy. | To be tested |
|  | ListRecycleInstances | Query the instance information in the recycle bin | To be tested |
| Scheduled Task | ListScheduledTasks | Query the list of scheduled tasks based on the specified conditions. | To be tested |
|  | CancelScheduledTask | Cancel a scheduled task based on the task ID. | To be tested |
| Security group | UpdateSecurityGroup | Update a security group | To be tested |
| Specification Change Management | ResizeInstance | The instance specification is changed. | To be tested |
| Tag Management | ListInstanceTags | Query the instance tag. | To be tested |
|  | ListInstancesByTags | Query a specified database instance by tag. | To be tested |
|  | BatchTagAction | Add or delete resource tags in batches. | To be tested |
| Tags | ListProjectTags | Query all tags of a specified resource type in a specified project | To be tested |
| Task Management | ShowJobDetail | Query the execution status of a job. This API is used to query the execution status of an SFS Turbo asynchronous API. For example, you can use the jobId returned by calling the interface for creating and binding LDAP configuration to query the execution status of a job. | To be tested |

