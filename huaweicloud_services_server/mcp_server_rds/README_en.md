# RDS MCP Server 


## Version
v0.1.0

## Overview

RDS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RDS. Full-chain management of RDS resources can be carried out based on natural language.

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
                    <td rowspan="29">Backup and Restore</td>
                    <td>BatchRestorePostgreSqlTables</td>
                    <td>Recovery to a Table Point in Time (PostgreSQL)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHistoryDatabase</td>
                    <td>Query the databases that can be restored at a specified time point</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreExistInstance</td>
                    <td>Restore to an existing DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupDownloadLink</td>
                    <td>Obtain the backup download link.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpdateBackupEnhancePolicy</td>
                    <td>Query advanced backup policies, including user-defined sparse backup policies</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOffSiteBackups</td>
                    <td>Query the cross-region backup list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIncreBackupPolicy1</td>
                    <td>Modifying the incremental backup policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteManualBackup</td>
                    <td>Delete a manual backup.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupPolicy</td>
                    <td>Query the automatic backup policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteManualBackup</td>
                    <td>Delete manual backups in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOffSiteBackupPolicy</td>
                    <td>Query the cross-region backup policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesSupportFastRestore</td>
                    <td>This command is used to obtain instances in batches and check whether fast recovery can be used during database and table restoration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListShareBackups</td>
                    <td>Querying the list of shared backups</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIncreBackupPolicy1</td>
                    <td>Obtain incremental backup policies</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOffSiteRestoreTimes</td>
                    <td>Query the restoreable period of a cross-region backup.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreToExistingInstance</td>
                    <td>Restore to an existing DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRestoreDatabase</td>
                    <td>Database-level point-in-time restoration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreTablesNew</td>
                    <td>Table-level point-in-time restoration (MySQL)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBackupPolicy</td>
                    <td>Set the automatic backup policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatabaseLevelDatabase</td>
                    <td>Query the databases contained in the database-level backup</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreTimes</td>
                    <td>Query the recoverable time segment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateManualBackup</td>
                    <td>Create a manual backup.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackups</td>
                    <td>Obtain the backup list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPostgresqlListHistoryTables</td>
                    <td>Querying tables that can be recovered at a specified point in time (PostgreSQL)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOffSiteInstances</td>
                    <td>Query the cross-region backup instance list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreTables</td>
                    <td>Table-level point-in-time restoration (MySQL)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRestoreInstance</td>
                    <td>Restore to a new DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetOffSiteBackupPolicy</td>
                    <td>Set a cross-region backup policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopBackup</td>
                    <td>Stopping creating a backup</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Configure the read-only latency database (PostgreSQL)</td>
                    <td>SwitchLogReplay</td>
                    <td>Stops and resumes wal log playback</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecoveryTimeWindow</td>
                    <td>Query the time window for restoring wal logs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReplayDelayStatus</td>
                    <td>Obtain the delayed playback status of wal logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">DR Instance</td>
                    <td>ListDrInfos</td>
                    <td>Query the DR management list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDrRelations</td>
                    <td>Query DR instance information in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceMasterDrAction</td>
                    <td>Configure the DR capability of the master instance when establishing the cross-cloud DR relationship.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDisasterRecovery</td>
                    <td>Interface for deleting the DR relationship between an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceDrToMasterAction</td>
                    <td>If the cross-cloud DR relationship between instances is abnormal, the DR instance is upgraded to the primary instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceSlaveDrAction</td>
                    <td>Configure the DR capability of the DR instance when the cross-cloud DR relationship is established.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDrReplicaStatus</td>
                    <td>Query the replication status and latency between the primary and DR instances after the cross-cloud DR relationship is established.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Database proxy</td>
                    <td>ListRdSforMysqlProxyFlavors</td>
                    <td>Query the specification information about the database proxy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRdSforMySqlProxy</td>
                    <td>Disable the database proxy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetInstancesProxyRestart</td>
                    <td>Restart the database proxy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRdSforMySqlProxy</td>
                    <td>Query the database proxy information list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRdSforMySqlProxy</td>
                    <td>Enable the database proxy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyRdSforMySqlProxyRouteMode</td>
                    <td>Set the read/write separation mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Database proxy (PostgreSQL)</td>
                    <td>ChangeProxyScale</td>
                    <td>The specification of the database proxy instance is being changed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInformationAboutDatabaseProxy</td>
                    <td>Query the details about the database proxy of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchQueryScaleFlavors</td>
                    <td>Query the specifications that can be changed by the database proxy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchQueryScaleComputeFlavors</td>
                    <td>Query the specifications that can be modified by the database proxy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartDatabaseProxy</td>
                    <td>This command is used to enable the database proxy for a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateReadWeight</td>
                    <td>Modifies the read/write separation weight of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeTheDelayThreshold</td>
                    <td>Modifies the read/write separation latency threshold of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopDatabaseProxy</td>
                    <td>Disable the database proxy for a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Database security</td>
                    <td>SetSecurityGroup</td>
                    <td>Modifying a security group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchSsl</td>
                    <td>Set SSL data encryption.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataIp</td>
                    <td>Change the internal IP address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Engine version and specification</td>
                    <td>ListStorageTypes</td>
                    <td>Query the database disk type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlavors</td>
                    <td>Query database specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatastores</td>
                    <td>Query the database engine version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Exclusive Instance Management</td>
                    <td>CreateInstance</td>
                    <td>Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="61">Instance management</td>
                    <td>UpgradeDbVersionNew</td>
                    <td>A small version upgrade is performed on the instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartFailover</td>
                    <td>Manually switch the active/standby.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoUpgradePolicy</td>
                    <td>Query the automatic upgrade policy of the small kernel version of an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpgradeHistories</td>
                    <td>Query the upgrade history of a major version of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlLimit</td>
                    <td>Query the SQL rate limit list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeDbVersion</td>
                    <td>A small version upgrade is performed on the instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceName</td>
                    <td>Change the instance name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlavorsResize</td>
                    <td>Interface for querying the specifications that can be modified in the database</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateFollower</td>
                    <td>Migrating the standby active/standby instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDnsName</td>
                    <td>Query the IPv6 domain name of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopInstance</td>
                    <td>Stopping instances in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnlockNodeReadonlyStatus</td>
                    <td>Interface for canceling the read-only status of a node</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetAutoUpgradePolicy</td>
                    <td>Setting the automatic upgrade policy for the small version of the instance kernel</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateToPeriod</td>
                    <td>Change pay-per-use RDS DB instances to yearly/monthly</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeDbMajorVersion</td>
                    <td>Upgrade the PostgreSQL database to a major version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReadOnlyReplayDatabase</td>
                    <td>Query the database to which the read replica can be restored to the primary DB instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSqlLimit</td>
                    <td>Modifying SQL Traffic Limiting</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartResizeFlavorAction</td>
                    <td>Change the specifications of a database instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePostgresqlHbaConf</td>
                    <td>Delete one or more configurations in the pg_hba.conf file. The configuration is uniquely identified by priority.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeFailoverMode</td>
                    <td>Change the data synchronization mode of the active/standby instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceSingleToHaAction</td>
                    <td>Convert a single-node system to a active/standby instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStorageUsedSpace</td>
                    <td>Query the disk space usage of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceReduceVolumeAction</td>
                    <td>The disk space of the database instance is reduced.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceEnlargeVolumeAction</td>
                    <td>Expand the disk space of the database instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopInstance</td>
                    <td>When an instance is stopped, you can temporarily stop the pay-per-use instance to save costs. By default, the instance will be stopped for seven days.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePostgresqlInstanceAlias</td>
                    <td>Modifies the remarks of a specified database instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetSecondLevelMonitor</td>
                    <td>The second-level monitoring policy takes effect in about 5 minutes. For 1-second monitoring and 5-second monitoring, the billing mode is pay-per-use (fees are deducted every hour).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAvailableVersion</td>
                    <td>Query the target version of the instance to be upgraded</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInspectionHistories</td>
                    <td>Query the major version upgrade check history of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPostgresqlHbaInfo</td>
                    <td>Query the pg_hba.conf file configuration of an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReplicationStatus</td>
                    <td>Obtain the replication status of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeFailoverStrategy</td>
                    <td>Switch the switchover policy of the active/standby instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeOpsWindow</td>
                    <td>Set the maintenance time segment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVolumeInfo</td>
                    <td>Query the disk information of an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoEnlargePolicy</td>
                    <td>Query the automatic storage capacity expansion policy of a DB instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartupInstance</td>
                    <td>You can manually restart the DB instance after stopping the DB instance to reduce costs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddPostgresqlHbaConf</td>
                    <td>Overwrite the current pg_hba.conf file content with the input configuration. If the input parameter is empty, overwrite the current file content with the default configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecondLevelMonitoring</td>
                    <td>Query the second-level monitoring policy of an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEngineFlavors</td>
                    <td>Querying the flavor that can be changed</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceRestartAction</td>
                    <td>Restart the database instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlLimit</td>
                    <td>Delete SQL rate limiting</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesInfoDiagnosis</td>
                    <td>Obtain the diagnosis result of a specified diagnosis item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlLimit</td>
                    <td>Add SQL rate limiting</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainName</td>
                    <td>Query the IPv4 domain name of an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceIam5</td>
                    <td>The V5 API for creating a database instance supports only the new plane authentication mode (AK/SK authentication) of IAM5.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyPostgresqlHbaConf</td>
                    <td>Modify or add one or more configurations in the pg_hba.conf file. The configuration is uniquely identified by priority. If the priority does not exist, add the configuration. If the priority exists, modify the configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceDiagnosis</td>
                    <td>Obtain the number of diagnosed instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDnsName</td>
                    <td>Application domain name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTdeStatus</td>
                    <td>sqlserverTDE switch.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTdeStatus</td>
                    <td>Query the SQL Server TDE status based on the instance ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDnsName</td>
                    <td>Modifying a domain name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeDbMajorVersionPreCheck</td>
                    <td>Check the upgrade before the upgrade of the major version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeDbMajorVersionStatus</td>
                    <td>Query the major version check or upgrade status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetAutoEnlargePolicy</td>
                    <td>This API is used to set an automatic instance storage capacity expansion policy and deduct storage fees based on the expanded capacity.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachEip</td>
                    <td>Associate and unbind an EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPostgresqlHbaInfoHistory</td>
                    <td>Query the modification history of the pg_hba.conf file of an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCollations</td>
                    <td>Query the available character sets of the SQL Server</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchSqlLimit</td>
                    <td>Enable/Disable all SQL rate limiting</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSslCertDownloadLink</td>
                    <td>Obtain the SSL certificate download address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSimplifiedInstances</td>
                    <td>Obtains details about a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreLogReplayDatabase</td>
                    <td>Deferred database read-only, restore the database to the primary DB instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Lifecycle Management</td>
                    <td>ListInstances</td>
                    <td>Query the instance list of a tenant. Query by condition is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Log</td>
                    <td>ListErrorlogForLts</td>
                    <td>Query the error log data of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetLogLtsConfigs</td>
                    <td>Associate LTS configuration information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogLtsConfigs</td>
                    <td>Obtain LTS configuration information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowLogStatisticsForLts</td>
                    <td>Query the statistics of slow DB instance logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogLtsConfigs</td>
                    <td>Deleting the LTS Configuration Information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowlogForLts</td>
                    <td>Query the slow log data of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">Manage Databases and Users (SQL Server)</td>
                    <td>ListAuthorizedSqlserverDbUsers</td>
                    <td>Query the authorized users of a specified database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlserverDatabase</td>
                    <td>Create a database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlserverDbUser</td>
                    <td>Delete a database user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMsdtcLocalHost</td>
                    <td>Delete the host address related to the MSDTC.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetInstancesDbShrink</td>
                    <td>Shrunk database logs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlserverDatabase</td>
                    <td>Delete the database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMsdtcHosts</td>
                    <td>Query the MSDTC hosts information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlserverDbUsers</td>
                    <td>Query the database user list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyCollation</td>
                    <td>Modify the character set of the instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddMsdtcs</td>
                    <td>Adding the host address of the MSDTC</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlserverDatabaseEx</td>
                    <td>Delete the database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlserverDatabases</td>
                    <td>Query the database list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlserverDbUser</td>
                    <td>Create a database user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeSqlserverDbUserPrivilege</td>
                    <td>Disable the permission of the database account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowSqlserverDbUserPrivilege</td>
                    <td>Authorize the database account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyDatabase</td>
                    <td>Replicating a Database</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetInstancesNewDbShrink</td>
                    <td>Shrunk database logs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="25">Manage databases and users (PostgreSQL)</td>
                    <td>ListPostgresqlExtension</td>
                    <td>Obtain the plug-in information of a specified database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteRevokeDatabaseUserRole</td>
                    <td>Revoke a user role</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDatabaseOwner</td>
                    <td>Modifying the database owner</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokePostgresqlDbPrivilege</td>
                    <td>Disable the permission of the database account</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDbUserPrivilege</td>
                    <td>Authentication of the database account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostgresqlDbUser</td>
                    <td>Create a database user in a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPostgresqlDbUserPaginated</td>
                    <td>Query the database user list in a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostgresqlDatabaseSchema</td>
                    <td>Create a database schema in the database of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPostgresqlDatabases</td>
                    <td>Query the database list in a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPostgresqlDatabaseSchemas</td>
                    <td>Query the database schema list of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetPostgresqlDbUserPwd</td>
                    <td>Reset the password of a specified database account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostgresqlExtension</td>
                    <td>Creates a plug-in on the specified database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePostgresqlDbUserComment</td>
                    <td>Modifying the remarks of the database user name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePostgresqlDatabase</td>
                    <td>Delete the database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePostgresqlExtension</td>
                    <td>Delete a plug-in from the specified database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetDatabaseUserPrivilege</td>
                    <td>Set the database user permission to read-only or read-write.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePostgresqlDbUser</td>
                    <td>Delete a database user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowDbPrivilege</td>
                    <td>This API is used to set account permissions in the database of a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPostgresqlParamValue</td>
                    <td>Obtains the value of a specified parameter of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePostgresqlParameterValue</td>
                    <td>Modify the value of a specified parameter of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostgresqlDatabase</td>
                    <td>Creates a database in a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseUserRole</td>
                    <td>Query database role information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePostgresqlExtension</td>
                    <td>Updates the plug-in on the specified database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecutePrivilegeDatabaseUserRole</td>
                    <td>Grant a role to a user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePostgresqlDatabase</td>
                    <td>Modifies the database remarks in a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">Managing Databases and Users (MySQL)</td>
                    <td>ResetPwd</td>
                    <td>Resetting the database password.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuthorizedDatabases</td>
                    <td>Query the authorized database of a specified user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDbUser</td>
                    <td>Delete a database user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDatabase</td>
                    <td>Modifies the database remarks in a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabase</td>
                    <td>Delete the database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDbUser</td>
                    <td>Create a database account in a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbUsers</td>
                    <td>Query the database user list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetDbUserPwd</td>
                    <td>Setting the database account password</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHostPrivilege</td>
                    <td>Modifies the host information of a user in an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDbUserComment</td>
                    <td>Modifying the remarks of the database user name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuthorizedDbUsers</td>
                    <td>Query the authorized users of a specified database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Revoke</td>
                    <td>Disable the permission of the database account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabase</td>
                    <td>Create a database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetReadOnlySwitch</td>
                    <td>Set the database user to read-only based on service requirements.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowDbUserPrivilege</td>
                    <td>Authorize the database account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabases</td>
                    <td>Query the database list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Obtain extended log download information</td>
                    <td>CreateXelLogDownload</td>
                    <td>Obtain extended log download information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Obtain extended log file list</td>
                    <td>ListXellogFiles</td>
                    <td>Query the extended log file list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">Obtain log information</td>
                    <td>DownloadSlowlog</td>
                    <td>Obtain the link for downloading slow logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowLogs</td>
                    <td>Query slow database logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowLogsNew</td>
                    <td>Query slow database logs. (The offset is modified compared with the original v3 API, which complies with HUAWEI CLOUD Open API Compliance Specification 3.0.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetSensitiveSlowLog</td>
                    <td>V3 slow log sensitive information switch</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetAuditlogPolicy</td>
                    <td>Set the audit log policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListErrorLogsNew</td>
                    <td>Query database error logs. (The offset is modified compared with the original v3 API, which complies with the HUAWEI CLOUD Open API Compliance Specification 3.0.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditlogs</td>
                    <td>Obtain the audit log list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBinlogClearPolicy</td>
                    <td>Query the local retention duration of binlogs of a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBinlogClearPolicy</td>
                    <td>Modifies the local retention duration of binlogs of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowlogStatistics</td>
                    <td>Obtains slow log statistics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAuditlogPolicy</td>
                    <td>Query the audit log policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListErrorLogs</td>
                    <td>Query database error logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadErrorlog</td>
                    <td>Obtain the link for downloading error logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowLogFile</td>
                    <td>Query the list of slow log files.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAuditlogDownloadLink</td>
                    <td>Generate the link for downloading audit logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">OpenStack - API version information</td>
                    <td>ListApiVersion</td>
                    <td>All available API versions (only for native OpenStack APIs) are returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Parameter Configuration</td>
                    <td>ShowInstanceConfiguration</td>
                    <td>Obtains the parameter template of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceParamHistories</td>
                    <td>Modification history of instance parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableConfiguration</td>
                    <td>Apply a parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurations</td>
                    <td>Obtain the parameter template list, including the default parameter templates of all databases and the parameter templates created by users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConfiguration</td>
                    <td>Create a parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfiguration</td>
                    <td>Obtains the parameters of a specified parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyConfiguration</td>
                    <td>Copying a parameter template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConfigurationAsync</td>
                    <td>Modifies the parameters of a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfiguration</td>
                    <td>Modifies a parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConfiguration</td>
                    <td>Delete a parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConfiguration</td>
                    <td>Modifies the parameters of a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplyConfigurationAsync</td>
                    <td>Apply a parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Port</td>
                    <td>UpdatePort</td>
                    <td>Update the port number.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query API version</td>
                    <td>ListApiVersionNew</td>
                    <td>Query the API version list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query version operation</td>
                    <td>ShowApiVersion</td>
                    <td>Query the details about a specified TMS API version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowQuotas</td>
                    <td>Query the resource quota of the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Recycle bin</td>
                    <td>ShowRecyclePolicy</td>
                    <td>Query the recycling policy in the recycle bin.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecycleInstances</td>
                    <td>Query the instance information in the recycle bin</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartRecyclePolicy</td>
                    <td>Set the recycle bin policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Tag Management</td>
                    <td>BatchTagDelAction</td>
                    <td>Delete tags in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchTagAddAction</td>
                    <td>Add tags in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceTags</td>
                    <td>Query the instance tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPredefinedTag</td>
                    <td>Query predefined tags</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>Query all tags of a specified resource type in a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Task Management</td>
                    <td>DeleteJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobInfo</td>
                    <td>Obtain the task information with a specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobInfoDetail</td>
                    <td>Obtains the task information of a specified DB instance and time range (SQL Server).</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
