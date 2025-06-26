# DDS MCP Server 


## Version
v0.1.0

## Overview

DDS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DDS. Full-chain management of DDS resources can be carried out based on natural language.

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
                    <td rowspan="13">Backup and Restore</td>
                    <td>BatchDeleteBackup</td>
                    <td>This API is used to delete manual backups of database instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackups</td>
                    <td>Obtain the backup list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateManualBackup</td>
                    <td>Create a manual backup.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupDownloadLink</td>
                    <td>Obtain the backup download link.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreDatabases</td>
                    <td>Obtain the list of databases that can be recovered.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreCollections</td>
                    <td>Obtain the list of recoverable database sets.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreInstanceFromCollection</td>
                    <td>Database and table-level data is restored to a point in time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopBackup</td>
                    <td>Stopping creating a backup</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreNewInstance</td>
                    <td>This API is used to restore a new DB instance from the backup.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBackupPolicy</td>
                    <td>Set the automatic backup policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreTimes</td>
                    <td>Query the recoverable time segment.</td>
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
                    <td rowspan="1">Backup management</td>
                    <td>RestoreInstance</td>
                    <td>Restoring to the current DB instance from a backup</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Connection management</td>
                    <td>ShowConnectionStatistics</td>
                    <td>Query the statistics on the number of connections between the client IP address and the DDS database instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSession</td>
                    <td>Terminates the instance node session.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSessions</td>
                    <td>Query the session of an instance node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Database O&amp;M</td>
                    <td>SwitchInstancePrimary</td>
                    <td>Replica sets, shards, and config standby nodes can be forcibly promoted to primary.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKillOpRuleList</td>
                    <td>Delete the killOp rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKillOpRuleRuleList</td>
                    <td>Obtain the killOp rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKillOpRule</td>
                    <td>Enable or disable the killOp rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKillOpRule</td>
                    <td>Create a killOp rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Database permission management</td>
                    <td>CreateDatabaseUser</td>
                    <td>Create a database user or role.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseUsers</td>
                    <td>Query all database users and roles.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabaseUser</td>
                    <td>Delete a database user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Database security</td>
                    <td>SwitchSsl</td>
                    <td>Set SSL data encryption.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Engine version and specification</td>
                    <td>ListFlavorInfos</td>
                    <td>Query the instance specifications that match the specified criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatastoreVersions</td>
                    <td>Query the database version information of a specified DB instance type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStorageType</td>
                    <td>Query the database disk type in the current region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
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
                    <td>DeleteInstance</td>
                    <td>Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ITaskController</td>
                    <td>ListTasks</td>
                    <td>Obtain the task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="33">Instance Management</td>
                    <td>CheckWeakPassword</td>
                    <td>Checking weak passwords</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandReplicasetNode</td>
                    <td>Expand the number of nodes in a specified replica set instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchoverReplicaSet</td>
                    <td>Switch the active/standby node in the replica set instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLtsConfig</td>
                    <td>Associate instance logs with LTS log streams. The background automatically uploads instance logs to the associated LTS log streams.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLtsConfigs</td>
                    <td>Query the LTS log configuration information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelEip</td>
                    <td>Unbinds an EIP from a node in the instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeDuration</td>
                    <td>Query the estimated database patch upgrade duration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeInstanceVolume</td>
                    <td>Storage capacity related to the instance to be scaled up.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachInternalIp</td>
                    <td>Change the private IP address of the instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteReadonlyNode</td>
                    <td>When a read-only node is added to a replica set, you need to call this API to delete the read-only node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMongosNode</td>
                    <td>Call this API when the mongos nodes need to be reduced in a cluster instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClientNetwork</td>
                    <td>Query the cross-network segment access configuration of a replica set</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSslCertDownloadAddress</td>
                    <td>Obtain the SSL certificate download address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClientNetwork</td>
                    <td>Configure the cross-network segment access of replica sets.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceRemark</td>
                    <td>Modifies the instance remarks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShrinkInstanceNodes</td>
                    <td>Delete the instance node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstancePort</td>
                    <td>Change the port number of the database instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPassword</td>
                    <td>Reset the password (only for instances with SSL enabled).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchSecondLevelMonitoring</td>
                    <td>Enables or disables second-level monitoring for a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAz2Migrate</td>
                    <td>Query the AZ to which the DB instance can be migrated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetAutoEnlargePolicies</td>
                    <td>Set the automatic disk capacity expansion policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLtsConfig</td>
                    <td>Disassociate instance logs from the LTS log stream. The background cancels the upload of instance logs to the LTS log stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeDatabaseVersion</td>
                    <td>Upgrade the database patch version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReplSetName</td>
                    <td>Query the name of a database replica set</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddReadonlyNode</td>
                    <td>This API is used to add a read node to a DDS replica set instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIp</td>
                    <td>Shard/Config IP address for creating a cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateAz</td>
                    <td>Migrate an instance to an AZ.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpgradeDatabaseVersion</td>
                    <td>Upgrade database patch versions in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddShardingNode</td>
                    <td>This API is used to expand the number of nodes in a specified cluster instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecondLevelMonitoringStatus</td>
                    <td>Query the second-level monitoring configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDiskUsage</td>
                    <td>Query the instance disk information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateReplSetName</td>
                    <td>Changing the name of a database replica set</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartInstance</td>
                    <td>Restarts a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Instance management</td>
                    <td>UpdateInstanceName</td>
                    <td>Change the instance name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeOpsWindow</td>
                    <td>Set the maintenance time segment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoEnlargePolicy</td>
                    <td>Query the automatic storage capacity expansion policy of a DB instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachEip</td>
                    <td>Associate and unbind an EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Lifecycle Management</td>
                    <td>ListInstances</td>
                    <td>Query the instance list of a tenant. Query by condition is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Manage databases and users</td>
                    <td>ListDatabaseRoles</td>
                    <td>Query the database role list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckPassword</td>
                    <td>Check the database password.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabaseRole</td>
                    <td>Create a database role.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBalancerSwitch</td>
                    <td>Set the cluster balancing switch.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabaseRole</td>
                    <td>Delete a database role.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBalancerWindow</td>
                    <td>Set the active time window for cluster balancing.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowShardingBalancer</td>
                    <td>Query cluster balancing settings.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Managing Databases and Users (MySQL)</td>
                    <td>ListDatabases</td>
                    <td>Query the database list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">Obtain log information</td>
                    <td>ListLtsErrorLogs</td>
                    <td>Query database error logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadErrorlog</td>
                    <td>Obtain the link for downloading error logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchSlowlogDesensitization</td>
                    <td>Sets the plaintext switch for slow logs of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadSlowlog</td>
                    <td>Obtain the link for downloading slow logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLtsSlowLogs</td>
                    <td>Query slow database logs.</td>
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
                    <td>ListAuditlogs</td>
                    <td>Obtain the audit log list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetAuditlogPolicy</td>
                    <td>Set the audit log policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditlogLinks</td>
                    <td>Obtain the link for downloading audit logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAuditLog</td>
                    <td>Delete audit logs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSlowlogDesensitizationSwitch</td>
                    <td>Querying the plaintext of slow logs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowLogs</td>
                    <td>Query slow database logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">OpenStack - API version information</td>
                    <td>ListApiVersion</td>
                    <td>All available API versions (only for native OpenStack APIs) are returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">Parameter Configuration</td>
                    <td>ShowInstanceConfigurationModifyHistory</td>
                    <td>Query the modification history of instance parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppliedInstances</td>
                    <td>Query the instances where the specified parameter template can be applied.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateConfigurationName</td>
                    <td>Verifies whether the parameter template name exists.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetConfiguration</td>
                    <td>Reset the parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurations</td>
                    <td>Obtain the parameter template list, including the default parameter templates of all databases and the parameter templates created by users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationAppliedHistory</td>
                    <td>Querying the application history of a parameter template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEntityConfiguration</td>
                    <td>Modifies the parameters of a specified instance, which can be the parameter template of an instance, group, or node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEntityConfiguration</td>
                    <td>Obtains the parameters of a specified DB instance, which can be the parameter template of an DB instance, a group, or a node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CompareConfiguration</td>
                    <td>Compare the differences between two parameter templates.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchConfiguration</td>
                    <td>Specify a parameter template for changing an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfigurationParameter</td>
                    <td>Modifies the parameter information of a specified parameter template, including the name, description, and value of a specified parameter.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyConfiguration</td>
                    <td>Copying a parameter template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConfiguration</td>
                    <td>Create a parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationModifyHistory</td>
                    <td>Query the modification history of a parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConfiguration</td>
                    <td>Delete a parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationParameter</td>
                    <td>Obtain the details about a parameter template.</td>
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
                    <td>SetRecyclePolicy</td>
                    <td>Set the recycle bin policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecycleInstances</td>
                    <td>Query the instance information in the recycle bin</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Scheduled Task</td>
                    <td>ListScheduledTasks</td>
                    <td>Query the list of scheduled tasks based on the specified conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelScheduledTask</td>
                    <td>Cancel a scheduled task based on the task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Security group</td>
                    <td>UpdateSecurityGroup</td>
                    <td>Update a security group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Specification Change Management</td>
                    <td>ResizeInstance</td>
                    <td>The instance specification is changed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Tag Management</td>
                    <td>ListInstanceTags</td>
                    <td>Query the instance tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesByTags</td>
                    <td>Query a specified database instance by tag.</td>
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
                    <td rowspan="1">Task Management</td>
                    <td>ShowJobDetail</td>
                    <td>Query the execution status of a job. This API is used to query the execution status of an SFS Turbo asynchronous API. For example, you can use the jobId returned by calling the interface for creating and binding LDAP configuration to query the execution status of a job.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
