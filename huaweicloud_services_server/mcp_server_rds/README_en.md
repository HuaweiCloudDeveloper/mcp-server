# RDS MCP Server 


## Version
v0.1.0

## Overview

RDS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RDS. Full-chain management of RDS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Backup and Restore | BatchRestorePostgreSqlTables | Recovery to a Table Point in Time (PostgreSQL) | To be tested |
|  | ListHistoryDatabase | Query the databases that can be restored at a specified time point | To be tested |
|  | RestoreExistInstance | Restore to an existing DB instance. | To be tested |
|  | ShowBackupDownloadLink | Obtain the backup download link. | To be tested |
|  | ListUpdateBackupEnhancePolicy | Query advanced backup policies, including user-defined sparse backup policies | To be tested |
|  | ListOffSiteBackups | Query the cross-region backup list. | To be tested |
|  | UpdateIncreBackupPolicy1 | Modifying the incremental backup policy | To be tested |
|  | DeleteManualBackup | Delete a manual backup. | To be tested |
|  | ShowBackupPolicy | Query the automatic backup policy. | To be tested |
|  | BatchDeleteManualBackup | Delete manual backups in batches. | To be tested |
|  | ShowOffSiteBackupPolicy | Query the cross-region backup policy. | To be tested |
|  | ListInstancesSupportFastRestore | This command is used to obtain instances in batches and check whether fast recovery can be used during database and table restoration. | To be tested |
|  | ListShareBackups | Querying the list of shared backups | To be tested |
|  | ShowIncreBackupPolicy1 | Obtain incremental backup policies | To be tested |
|  | ListOffSiteRestoreTimes | Query the restoreable period of a cross-region backup. | To be tested |
|  | RestoreToExistingInstance | Restore to an existing DB instance. | To be tested |
|  | BatchRestoreDatabase | Database-level point-in-time restoration | To be tested |
|  | RestoreTablesNew | Table-level point-in-time restoration (MySQL) | To be tested |
|  | SetBackupPolicy | Set the automatic backup policy. | To be tested |
|  | ShowDatabaseLevelDatabase | Query the databases contained in the database-level backup | To be tested |
|  | ListRestoreTimes | Query the recoverable time segment. | To be tested |
|  | CreateManualBackup | Create a manual backup. | To be tested |
|  | ListBackups | Obtain the backup list. | To be tested |
|  | ListPostgresqlListHistoryTables | Querying tables that can be recovered at a specified point in time (PostgreSQL) | To be tested |
|  | ListOffSiteInstances | Query the cross-region backup instance list. | To be tested |
|  | RestoreTables | Table-level point-in-time restoration (MySQL) | To be tested |
|  | CreateRestoreInstance | Restore to a new DB instance. | To be tested |
|  | SetOffSiteBackupPolicy | Set a cross-region backup policy. | To be tested |
|  | StopBackup | Stopping creating a backup | To be tested |
| Configure the read-only latency database (PostgreSQL) | SwitchLogReplay | Stops and resumes wal log playback | To be tested |
|  | ShowRecoveryTimeWindow | Query the time window for restoring wal logs | To be tested |
|  | ShowReplayDelayStatus | Obtain the delayed playback status of wal logs. | To be tested |
| DR Instance | ListDrInfos | Query the DR management list. | To be tested |
|  | ListDrRelations | Query DR instance information in batches | To be tested |
|  | StartInstanceMasterDrAction | Configure the DR capability of the master instance when establishing the cross-cloud DR relationship. | To be tested |
|  | DeleteDisasterRecovery | Interface for deleting the DR relationship between an instance | To be tested |
|  | StartInstanceDrToMasterAction | If the cross-cloud DR relationship between instances is abnormal, the DR instance is upgraded to the primary instance. | To be tested |
|  | StartInstanceSlaveDrAction | Configure the DR capability of the DR instance when the cross-cloud DR relationship is established. | To be tested |
|  | ShowDrReplicaStatus | Query the replication status and latency between the primary and DR instances after the cross-cloud DR relationship is established. | To be tested |
| Database proxy | ListRdSforMysqlProxyFlavors | Query the specification information about the database proxy. | To be tested |
|  | DeleteRdSforMySqlProxy | Disable the database proxy. | To be tested |
|  | SetInstancesProxyRestart | Restart the database proxy. | To be tested |
|  | ListRdSforMySqlProxy | Query the database proxy information list. | To be tested |
|  | CreateRdSforMySqlProxy | Enable the database proxy. | To be tested |
|  | ModifyRdSforMySqlProxyRouteMode | Set the read/write separation mode. | To be tested |
| Database proxy (PostgreSQL) | ChangeProxyScale | The specification of the database proxy instance is being changed. | To be tested |
|  | ShowInformationAboutDatabaseProxy | Query the details about the database proxy of a specified DB instance. | To be tested |
|  | SearchQueryScaleFlavors | Query the specifications that can be changed by the database proxy. | To be tested |
|  | SearchQueryScaleComputeFlavors | Query the specifications that can be modified by the database proxy. | To be tested |
|  | StartDatabaseProxy | This command is used to enable the database proxy for a specified DB instance. | To be tested |
|  | UpdateReadWeight | Modifies the read/write separation weight of a specified DB instance. | To be tested |
|  | ChangeTheDelayThreshold | Modifies the read/write separation latency threshold of a specified DB instance. | To be tested |
|  | StopDatabaseProxy | Disable the database proxy for a specified instance. | To be tested |
| Database security | SetSecurityGroup | Modifying a security group | To be tested |
|  | SwitchSsl | Set SSL data encryption. | To be tested |
|  | UpdateDataIp | Change the internal IP address. | To be tested |
| Engine version and specification | ListStorageTypes | Query the database disk type. | To be tested |
|  | ListFlavors | Query database specifications. | To be tested |
|  | ListDatastores | Query the database engine version. | To be tested |
| Exclusive Instance Management | CreateInstance | Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore | To be tested |
|  | DeleteInstance | Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
| Instance management | UpgradeDbVersionNew | A small version upgrade is performed on the instance. | To be tested |
|  | StartFailover | Manually switch the active/standby. | To be tested |
|  | ShowAutoUpgradePolicy | Query the automatic upgrade policy of the small kernel version of an instance | To be tested |
|  | ListUpgradeHistories | Query the upgrade history of a major version of an instance. | To be tested |
|  | ListSqlLimit | Query the SQL rate limit list | To be tested |
|  | UpgradeDbVersion | A small version upgrade is performed on the instance. | To be tested |
|  | UpdateInstanceName | Change the instance name. | To be tested |
|  | ListFlavorsResize | Interface for querying the specifications that can be modified in the database | To be tested |
|  | MigrateFollower | Migrating the standby active/standby instance | To be tested |
|  | ShowDnsName | Query the IPv6 domain name of an instance. | To be tested |
|  | BatchStopInstance | Stopping instances in batches | To be tested |
|  | UnlockNodeReadonlyStatus | Interface for canceling the read-only status of a node | To be tested |
|  | SetAutoUpgradePolicy | Setting the automatic upgrade policy for the small version of the instance kernel | To be tested |
|  | UpdateToPeriod | Change pay-per-use RDS DB instances to yearly/monthly | To be tested |
|  | UpgradeDbMajorVersion | Upgrade the PostgreSQL database to a major version. | To be tested |
|  | ListReadOnlyReplayDatabase | Query the database to which the read replica can be restored to the primary DB instance | To be tested |
|  | UpdateSqlLimit | Modifying SQL Traffic Limiting | To be tested |
|  | StartResizeFlavorAction | Change the specifications of a database instance. | To be tested |
|  | DeletePostgresqlHbaConf | Delete one or more configurations in the pg_hba.conf file. The configuration is uniquely identified by priority. | To be tested |
|  | ChangeFailoverMode | Change the data synchronization mode of the active/standby instance. | To be tested |
|  | StartInstanceSingleToHaAction | Convert a single-node system to a active/standby instance. | To be tested |
|  | ShowStorageUsedSpace | Query the disk space usage of an instance. | To be tested |
|  | StartInstanceReduceVolumeAction | The disk space of the database instance is reduced. | To be tested |
|  | StartInstanceEnlargeVolumeAction | Expand the disk space of the database instance. | To be tested |
|  | StopInstance | When an instance is stopped, you can temporarily stop the pay-per-use instance to save costs. By default, the instance will be stopped for seven days. | To be tested |
|  | UpdatePostgresqlInstanceAlias | Modifies the remarks of a specified database instance. | To be tested |
|  | SetSecondLevelMonitor | The second-level monitoring policy takes effect in about 5 minutes. For 1-second monitoring and 5-second monitoring, the billing mode is pay-per-use (fees are deducted every hour). | To be tested |
|  | ShowAvailableVersion | Query the target version of the instance to be upgraded | To be tested |
|  | ListInspectionHistories | Query the major version upgrade check history of an instance. | To be tested |
|  | ListPostgresqlHbaInfo | Query the pg_hba.conf file configuration of an instance | To be tested |
|  | ShowReplicationStatus | Obtain the replication status of an instance. | To be tested |
|  | ChangeFailoverStrategy | Switch the switchover policy of the active/standby instance. | To be tested |
|  | ChangeOpsWindow | Set the maintenance time segment | To be tested |
|  | ListVolumeInfo | Query the disk information of an instance | To be tested |
|  | ShowAutoEnlargePolicy | Query the automatic storage capacity expansion policy of a DB instance | To be tested |
|  | StartupInstance | You can manually restart the DB instance after stopping the DB instance to reduce costs. | To be tested |
|  | AddPostgresqlHbaConf | Overwrite the current pg_hba.conf file content with the input configuration. If the input parameter is empty, overwrite the current file content with the default configuration. | To be tested |
|  | ShowSecondLevelMonitoring | Query the second-level monitoring policy of an instance | To be tested |
|  | ListEngineFlavors | Querying the flavor that can be changed | To be tested |
|  | StartInstanceRestartAction | Restart the database instance. | To be tested |
|  | DeleteSqlLimit | Delete SQL rate limiting | To be tested |
|  | ListInstancesInfoDiagnosis | Obtain the diagnosis result of a specified diagnosis item | To be tested |
|  | CreateSqlLimit | Add SQL rate limiting | To be tested |
|  | ShowDomainName | Query the IPv4 domain name of an instance | To be tested |
|  | CreateInstanceIam5 | The V5 API for creating a database instance supports only the new plane authentication mode (AK/SK authentication) of IAM5. | To be tested |
|  | ModifyPostgresqlHbaConf | Modify or add one or more configurations in the pg_hba.conf file. The configuration is uniquely identified by priority. If the priority does not exist, add the configuration. If the priority exists, modify the configuration. | To be tested |
|  | ListInstanceDiagnosis | Obtain the number of diagnosed instances. | To be tested |
|  | CreateDnsName | Application domain name | To be tested |
|  | UpdateTdeStatus | sqlserverTDE switch. | To be tested |
|  | ShowTdeStatus | Query the SQL Server TDE status based on the instance ID. | To be tested |
|  | UpdateDnsName | Modifying a domain name | To be tested |
|  | UpgradeDbMajorVersionPreCheck | Check the upgrade before the upgrade of the major version. | To be tested |
|  | ShowUpgradeDbMajorVersionStatus | Query the major version check or upgrade status. | To be tested |
|  | SetAutoEnlargePolicy | This API is used to set an automatic instance storage capacity expansion policy and deduct storage fees based on the expanded capacity. | To be tested |
|  | AttachEip | Associate and unbind an EIP. | To be tested |
|  | ListPostgresqlHbaInfoHistory | Query the modification history of the pg_hba.conf file of an instance | To be tested |
|  | ListCollations | Query the available character sets of the SQL Server | To be tested |
|  | SwitchSqlLimit | Enable/Disable all SQL rate limiting | To be tested |
|  | ListSslCertDownloadLink | Obtain the SSL certificate download address. | To be tested |
|  | ListSimplifiedInstances | Obtains details about a specified DB instance. | To be tested |
|  | RestoreLogReplayDatabase | Deferred database read-only, restore the database to the primary DB instance | To be tested |
| Lifecycle Management | ListInstances | Query the instance list of a tenant. Query by condition is supported. | To be tested |
| Log | ListErrorlogForLts | Query the error log data of an instance. | To be tested |
|  | SetLogLtsConfigs | Associate LTS configuration information | To be tested |
|  | ListLogLtsConfigs | Obtain LTS configuration information | To be tested |
|  | ListSlowLogStatisticsForLts | Query the statistics of slow DB instance logs. | To be tested |
|  | DeleteLogLtsConfigs | Deleting the LTS Configuration Information | To be tested |
|  | ListSlowlogForLts | Query the slow log data of an instance. | To be tested |
| Manage Databases and Users (SQL Server) | ListAuthorizedSqlserverDbUsers | Query the authorized users of a specified database. | To be tested |
|  | CreateSqlserverDatabase | Create a database. | To be tested |
|  | DeleteSqlserverDbUser | Delete a database user. | To be tested |
|  | DeleteMsdtcLocalHost | Delete the host address related to the MSDTC. | To be tested |
|  | SetInstancesDbShrink | Shrunk database logs | To be tested |
|  | DeleteSqlserverDatabase | Delete the database. | To be tested |
|  | ListMsdtcHosts | Query the MSDTC hosts information | To be tested |
|  | ListSqlserverDbUsers | Query the database user list. | To be tested |
|  | ModifyCollation | Modify the character set of the instance. | To be tested |
|  | BatchAddMsdtcs | Adding the host address of the MSDTC | To be tested |
|  | DeleteSqlserverDatabaseEx | Delete the database. | To be tested |
|  | ListSqlserverDatabases | Query the database list. | To be tested |
|  | CreateSqlserverDbUser | Create a database user. | To be tested |
|  | RevokeSqlserverDbUserPrivilege | Disable the permission of the database account. | To be tested |
|  | AllowSqlserverDbUserPrivilege | Authorize the database account. | To be tested |
|  | CopyDatabase | Replicating a Database | To be tested |
|  | SetInstancesNewDbShrink | Shrunk database logs | To be tested |
| Manage databases and users (PostgreSQL) | ListPostgresqlExtension | Obtain the plug-in information of a specified database. | To be tested |
|  | ExecuteRevokeDatabaseUserRole | Revoke a user role | To be tested |
|  | UpdateDatabaseOwner | Modifying the database owner | To be tested |
|  | RevokePostgresqlDbPrivilege | Disable the permission of the database account | To be tested |
|  | UpdateDbUserPrivilege | Authentication of the database account. | To be tested |
|  | CreatePostgresqlDbUser | Create a database user in a specified instance. | To be tested |
|  | ListPostgresqlDbUserPaginated | Query the database user list in a specified instance. | To be tested |
|  | CreatePostgresqlDatabaseSchema | Create a database schema in the database of a specified DB instance. | To be tested |
|  | ListPostgresqlDatabases | Query the database list in a specified DB instance. | To be tested |
|  | ListPostgresqlDatabaseSchemas | Query the database schema list of a specified DB instance. | To be tested |
|  | SetPostgresqlDbUserPwd | Reset the password of a specified database account. | To be tested |
|  | CreatePostgresqlExtension | Creates a plug-in on the specified database. | To be tested |
|  | UpdatePostgresqlDbUserComment | Modifying the remarks of the database user name | To be tested |
|  | DeletePostgresqlDatabase | Delete the database. | To be tested |
|  | DeletePostgresqlExtension | Delete a plug-in from the specified database. | To be tested |
|  | SetDatabaseUserPrivilege | Set the database user permission to read-only or read-write. | To be tested |
|  | DeletePostgresqlDbUser | Delete a database user. | To be tested |
|  | AllowDbPrivilege | This API is used to set account permissions in the database of a specified instance. | To be tested |
|  | ShowPostgresqlParamValue | Obtains the value of a specified parameter of an instance. | To be tested |
|  | UpdatePostgresqlParameterValue | Modify the value of a specified parameter of an instance. | To be tested |
|  | CreatePostgresqlDatabase | Creates a database in a specified instance. | To be tested |
|  | ListDatabaseUserRole | Query database role information | To be tested |
|  | UpdatePostgresqlExtension | Updates the plug-in on the specified database. | To be tested |
|  | ExecutePrivilegeDatabaseUserRole | Grant a role to a user | To be tested |
|  | UpdatePostgresqlDatabase | Modifies the database remarks in a specified instance. | To be tested |
| Managing Databases and Users (MySQL) | ResetPwd | Resetting the database password. | To be tested |
|  | ListAuthorizedDatabases | Query the authorized database of a specified user. | To be tested |
|  | DeleteDbUser | Delete a database user. | To be tested |
|  | UpdateDatabase | Modifies the database remarks in a specified instance. | To be tested |
|  | DeleteDatabase | Delete the database. | To be tested |
|  | CreateDbUser | Create a database account in a specified instance. | To be tested |
|  | ListDbUsers | Query the database user list. | To be tested |
|  | SetDbUserPwd | Setting the database account password | To be tested |
|  | UpdateHostPrivilege | Modifies the host information of a user in an instance. | To be tested |
|  | UpdateDbUserComment | Modifying the remarks of the database user name | To be tested |
|  | ListAuthorizedDbUsers | Query the authorized users of a specified database. | To be tested |
|  | Revoke | Disable the permission of the database account. | To be tested |
|  | CreateDatabase | Create a database. | To be tested |
|  | SetReadOnlySwitch | Set the database user to read-only based on service requirements. | To be tested |
|  | AllowDbUserPrivilege | Authorize the database account. | To be tested |
|  | ListDatabases | Query the database list. | To be tested |
| Obtain extended log download information | CreateXelLogDownload | Obtain extended log download information | To be tested |
| Obtain extended log file list | ListXellogFiles | Query the extended log file list. | To be tested |
| Obtain log information | DownloadSlowlog | Obtain the link for downloading slow logs. | To be tested |
|  | ListSlowLogs | Query slow database logs. | To be tested |
|  | ListSlowLogsNew | Query slow database logs. (The offset is modified compared with the original v3 API, which complies with HUAWEI CLOUD Open API Compliance Specification 3.0.) | To be tested |
|  | SetSensitiveSlowLog | V3 slow log sensitive information switch | To be tested |
|  | SetAuditlogPolicy | Set the audit log policy. | To be tested |
|  | ListErrorLogsNew | Query database error logs. (The offset is modified compared with the original v3 API, which complies with the HUAWEI CLOUD Open API Compliance Specification 3.0.) | To be tested |
|  | ListAuditlogs | Obtain the audit log list. | To be tested |
|  | ShowBinlogClearPolicy | Query the local retention duration of binlogs of a specified instance. | To be tested |
|  | SetBinlogClearPolicy | Modifies the local retention duration of binlogs of a specified DB instance. | To be tested |
|  | ListSlowlogStatistics | Obtains slow log statistics | To be tested |
|  | ShowAuditlogPolicy | Query the audit log policy. | To be tested |
|  | ListErrorLogs | Query database error logs. | To be tested |
|  | DownloadErrorlog | Obtain the link for downloading error logs. | To be tested |
|  | ListSlowLogFile | Query the list of slow log files. | To be tested |
|  | ShowAuditlogDownloadLink | Generate the link for downloading audit logs. | To be tested |
| OpenStack - API version information | ListApiVersion | All available API versions (only for native OpenStack APIs) are returned. | To be tested |
| Parameter Configuration | ShowInstanceConfiguration | Obtains the parameter template of a specified DB instance. | To be tested |
|  | ListInstanceParamHistories | Modification history of instance parameters. | To be tested |
|  | EnableConfiguration | Apply a parameter template. | To be tested |
|  | ListConfigurations | Obtain the parameter template list, including the default parameter templates of all databases and the parameter templates created by users. | To be tested |
|  | CreateConfiguration | Create a parameter template. | To be tested |
|  | ShowConfiguration | Obtains the parameters of a specified parameter template. | To be tested |
|  | CopyConfiguration | Copying a parameter template | To be tested |
|  | UpdateInstanceConfigurationAsync | Modifies the parameters of a specified instance. | To be tested |
|  | UpdateConfiguration | Modifies a parameter template. | To be tested |
|  | DeleteConfiguration | Delete a parameter template. | To be tested |
|  | UpdateInstanceConfiguration | Modifies the parameters of a specified instance. | To be tested |
|  | ApplyConfigurationAsync | Apply a parameter template. | To be tested |
| Port | UpdatePort | Update the port number. | To be tested |
| Query API version | ListApiVersionNew | Query the API version list. | To be tested |
| Query version operation | ShowApiVersion | Query the details about a specified TMS API version. | To be tested |
| Quota | ShowQuotas | Query the resource quota of the current project. | To be tested |
| Recycle bin | ShowRecyclePolicy | Query the recycling policy in the recycle bin. | To be tested |
|  | ListRecycleInstances | Query the instance information in the recycle bin | To be tested |
|  | StartRecyclePolicy | Set the recycle bin policy. | To be tested |
| Tag Management | BatchTagDelAction | Delete tags in batches. | To be tested |
|  | BatchTagAddAction | Add tags in batches. | To be tested |
|  | ListInstanceTags | Query the instance tag. | To be tested |
|  | ListPredefinedTag | Query predefined tags | To be tested |
| Tags | ListProjectTags | Query all tags of a specified resource type in a specified project | To be tested |
| Task Management | DeleteJob |  | To be tested |
|  | ListJobInfo | Obtain the task information with a specified ID. | To be tested |
|  | ListJobInfoDetail | Obtains the task information of a specified DB instance and time range (SQL Server).  | To be tested |

