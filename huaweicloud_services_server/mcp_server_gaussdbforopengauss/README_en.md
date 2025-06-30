# GaussDBforopenGauss MCP Server 


## Version
v0.1.0

## Overview

GaussDBforopenGauss MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GaussDBforopenGauss. Full-chain management of GaussDBforopenGauss resources can be carried out based on natural language.

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
                    <td rowspan="6">Add-on management</td>
                    <td>ListKernelPlugins</td>
                    <td>Query the list of installed plug-ins in an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPluginExtensions</td>
                    <td>Query the extension information about the instance plug-in</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResumePluginExtensions</td>
                    <td>Configure the plug-in expansion capability.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InstallKernelPlugin</td>
                    <td>Install the plug-in</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSupportKernelPlugins</td>
                    <td>Query the list of supported plug-ins</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetKernelPluginLicense</td>
                    <td>Configure the plug-in license</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Backup and Restore</td>
                    <td>CreateManualBackup</td>
                    <td>Create a manual backup.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupPolicy</td>
                    <td>Query the automatic backup policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRestoreInstance</td>
                    <td>Restore to a new DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteManualBackup</td>
                    <td>Delete a manual backup.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBackupPolicy</td>
                    <td>Set the automatic backup policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackups</td>
                    <td>Obtain the backup list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreTimes</td>
                    <td>Query the recoverable time segment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopBackup</td>
                    <td>Stopping creating a backup</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Backup management</td>
                    <td>ShowInstanceSnapshot</td>
                    <td>Query the original DB instance information based on the time point or backup file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestorableInstancesDetails</td>
                    <td>Query the list of DB instances that can be used for backup and restoration. The DB instance information must meet the backup conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreInstance</td>
                    <td>Restoring to the current DB instance from a backup</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetNewBackupPolicy</td>
                    <td>Setting the automatic backup policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadBackup</td>
                    <td>Obtain the backup download link.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestorableInstances</td>
                    <td>Query the list of instances that can be used for backup and restoration. The instance information must meet the backup conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackupsDetails</td>
                    <td>Obtain the backup list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConfirmRestoredData</td>
                    <td>Ensure that the data backed up and restored to the target DB instance is normal.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbBackups</td>
                    <td>Obtain the backup list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSourceInstanceDetail</td>
                    <td>Query the original DB instance information based on the time point or backup file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">DR management</td>
                    <td>ShowCrossCloudDisasterInstanceMonitor</td>
                    <td>Query the real-time DR monitoring status of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterRecoveryFailover</td>
                    <td>Switchover from DR to primary (delivered by the DR instance)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCrossCloudDisasterRelations</td>
                    <td>Query the DR relationship list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudReleaseDisaster</td>
                    <td>Disable DR (delivered from the master DR cluster).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterDataCacheEnd</td>
                    <td>End the log retention function for Streaming DR. Currently, only Streaming DR supports this function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterDataCacheStart</td>
                    <td>The primary instance starts to retain DR logs. Currently, only Stream DR supports this function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDisasterRecoveryRecord</td>
                    <td>Query DR operation records.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterSwitchover</td>
                    <td>DR switchover, which can be delivered on either end of the active/standby.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterRestore</td>
                    <td>The DR switchback is supported when the flow DR switchover is selected to rebuild the DR relationship.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterStartSimulation</td>
                    <td>Start the DR drill. Currently, only Stream DR is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetDrConfig</td>
                    <td>Reset the DR network configuration. 1. The system automatically creates an agency to authorize DBS to access VPC resources and query IaaS APIs. 2. Reset the DR network configuration of the instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterEndSimulation</td>
                    <td>The DR drill for the DR instance is complete. Currently, only Stream DR is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCrossCloudConstructDisaster</td>
                    <td>Set up the DR relationship (delivered from the master instance).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Database management</td>
                    <td>StartInstance</td>
                    <td>Starts the database and supports node-level startup operations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Disk management</td>
                    <td>ShowInstanceDisk</td>
                    <td>Query the used storage space and maximum storage space of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Engine version and specification</td>
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
                    <td>ListAvailableFlavors</td>
                    <td>Query the list of flavor that can be modified for a DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlavorsDetails</td>
                    <td>Query the specifications of the database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceEngineDetail</td>
                    <td>View the DB instance engine version distribution</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatastoresDetails</td>
                    <td>Query the engine list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStorageTypes</td>
                    <td>Query the database disk type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbFlavors</td>
                    <td>Query the specifications of the database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGaussDbDatastores</td>
                    <td>Query the engine list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Exclusive Instance Management</td>
                    <td>DeleteInstance</td>
                    <td>Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstance</td>
                    <td>Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ITaskController</td>
                    <td>ListTasks</td>
                    <td>Obtain the task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="23">Instance Management</td>
                    <td>CreateGaussDbInstance</td>
                    <td>Create a database instance. Only the new plane authentication mode (AK/SK authentication) of IAM5 is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchAutoEnlargePolicy</td>
                    <td>Query the automatic disk capacity expansion policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeploymentForm</td>
                    <td>Query the number of copies, shards, and nodes based on the solution template name or instance ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseInstances</td>
                    <td>Querying the database instance list/Querying instance details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateWeakPassword</td>
                    <td>Verify the password security of the database user root.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCnInfosBeforeReduce</td>
                    <td>Query the coordinator node list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMysqlCompatibility</td>
                    <td>Updates the M-compatible port service configuration of a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesDetails</td>
                    <td>Querying the database instance list/Querying instance details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeInstanceFlavor</td>
                    <td>GaussDB instance specification change</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunInstanceAction</td>
                    <td>CN scale-out/DN shard scale-out/disk scale-out</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectQuotas</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSslCertDownloadLink</td>
                    <td>Query the SSL certificate download address of a DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDbInstance</td>
                    <td>Create a database instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBalanceStatus</td>
                    <td>Check whether the active/standby switchover has occurred on the instance, resulting in load imbalance on the host.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchShard</td>
                    <td>You can perform active/standby switchover on one or multiple DN shards. Only one new standby node can be specified in a group to be switched to the active node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartInstance</td>
                    <td>Restarts a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBindedEips</td>
                    <td>Query the list of EIPs bound to an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartMysqlCompatibility</td>
                    <td>Enables the M-compatible port of a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFeatures</td>
                    <td>Query the advanced feature list of the current instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabaseInstance</td>
                    <td>Create a database instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComponentInfos</td>
                    <td>Query the component list of an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFeatures</td>
                    <td>Enable the advanced feature switch.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceDetails</td>
                    <td>Query the database instance list/Query the instance details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Instance management</td>
                    <td>AttachEip</td>
                    <td>Associate and unbind an EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopInstance</td>
                    <td>When an instance is stopped, you can temporarily stop the pay-per-use instance to save costs. By default, the instance will be stopped for seven days.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceName</td>
                    <td>Change the instance name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Lifecycle Management</td>
                    <td>ListInstances</td>
                    <td>Query the instance list of a tenant. Query by condition is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Log management</td>
                    <td>ShowErrorLogSwitchStatus</td>
                    <td>Query the status of the database error log collection function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceErrorLogs</td>
                    <td>Query the link for downloading database error logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSlowLogDownload</td>
                    <td>Create slow log download information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSlowLogDownload</td>
                    <td>Query slow log download information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Manage databases and users</td>
                    <td>CreateDatabaseSchemas</td>
                    <td>Create a database schema in the database of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowDbRolePrivileges</td>
                    <td>Set the role permission in the database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseRoles</td>
                    <td>Query the database role list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDbRole</td>
                    <td>Create a database role.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowDbPrivileges</td>
                    <td>This API is used to set account permissions in the database of a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseSchemas</td>
                    <td>Query the database schema list of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabaseSchema</td>
                    <td>Delete a database schema.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Managing Databases and Users (MySQL)</td>
                    <td>CreateDatabase</td>
                    <td>Create a database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDbUser</td>
                    <td>Create a database account in a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabase</td>
                    <td>Delete the database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPwd</td>
                    <td>Resetting the database password.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetDbUserPwd</td>
                    <td>Setting the database account password</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabases</td>
                    <td>Query the database list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbUsers</td>
                    <td>Query the database user list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="19">Parameter Configuration</td>
                    <td>CreateConfigurationTemplate</td>
                    <td>Create a parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConfiguration</td>
                    <td>Modifies the parameters of a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceConfiguration</td>
                    <td>Obtains the parameter template of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListParamGroupTemplates</td>
                    <td>Obtain the parameter template list, including the default parameter templates of all databases and the parameter templates created by users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyConfiguration</td>
                    <td>Copying a parameter template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurationsDiff</td>
                    <td>Obtain the difference list between two parameter configuration templates.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHistoryOperations</td>
                    <td>Query the modification history of a parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationDetail</td>
                    <td>This API is used to obtain details about a parameter template based on the parameter template ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListParameterGroupTemplates</td>
                    <td>Obtain the parameter template list, including the default parameter templates of all databases and the parameter templates created by users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppliedHistories</td>
                    <td>Query the application records of a parameter template by instance level.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchConfiguration</td>
                    <td>Specify a parameter template for changing an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplicableInstances</td>
                    <td>Query the list of instances where the current parameter group template can be applied.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceParamGroup</td>
                    <td>Obtains the parameter template of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateParaGroupName</td>
                    <td>Check whether the parameter group name exists.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceParamGroupDetail</td>
                    <td>Obtains the parameter template of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowParameterGroupDetail</td>
                    <td>This API is used to obtain details about a parameter template based on the parameter template ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurations</td>
                    <td>Obtain the parameter template list, including the default parameter templates of all databases and the parameter templates created by users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetConfiguration</td>
                    <td>Reset the parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConfiguration</td>
                    <td>Delete a parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Quota Management</td>
                    <td>ListEpsQuotas</td>
                    <td>Query the quota group information of an enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyEpsQuota</td>
                    <td>Modify the enterprise project quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Recycle bin</td>
                    <td>ShowRecyclePolicy</td>
                    <td>Query the recycling policy in the recycle bin.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecycleInstancesDetails</td>
                    <td>Query the list of all engine instances in the recycle bin.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecycleInstances</td>
                    <td>Query the instance information in the recycle bin</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetRecyclePolicy</td>
                    <td>Set the recycle bin policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">SQL Traffic Limit</td>
                    <td>ListLimitTask</td>
                    <td>Query the list of rate limiting tasks based on the specified conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLimitTask</td>
                    <td>Delete a traffic limiting task based on the task_id.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLimitTask</td>
                    <td>Create a traffic limiting task based on the specific scope and type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLimitTask</td>
                    <td>Query details about a rate limiting task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncLimitData</td>
                    <td>Synchronize SQL rate limiting data on the kernel side to the management and control side</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodeLimitSqlModel</td>
                    <td>Query the SQL template list of a node</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLimitTask</td>
                    <td>Update the traffic limiting task based on the new conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Tag Management</td>
                    <td>DeleteInstanceTag</td>
                    <td>Delete an instance label</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPredefinedTags</td>
                    <td>Query predefined tags.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceTags</td>
                    <td>Query the instance tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddInstanceTags</td>
                    <td>This API is used to add user tags to a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>Query all tags of a specified resource type in a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Task Management</td>
                    <td>ListScheduleTask</td>
                    <td>View the scheduled task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelScheduleTask</td>
                    <td>Cancel the scheduled task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScheduleTask</td>
                    <td>Delete the information about a scheduled task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobDetail</td>
                    <td>Query the execution status of a job. This API is used to query the execution status of an SFS Turbo asynchronous API. For example, you can use the jobId returned by calling the interface for creating and binding LDAP configuration to query the execution status of a job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Version upgrade</td>
                    <td>UpgradeInstanceVersion</td>
                    <td>GaussDB(for openGauss) instance version. There are three upgrade modes: gray upgrade, local upgrade, and hot patch upgrade.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBatchUpgradeCandidateVersions</td>
                    <td>Query the versions and upgrade types that can be upgraded in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeCandidateVersions</td>
                    <td>Query the version that can be upgraded.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowUpgradeCandidateVersions</td>
                    <td>Query the versions and upgrade types that can be upgraded in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeCandidateVersionsDetails</td>
                    <td>Query the version that can be upgraded.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeInstancesVersion</td>
                    <td>Upgrade GaussDB instances in batches. There are three upgrade modes: gray upgrade, local upgrade, and hot patch upgrade.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScheduleTask</td>
                    <td>Upgrade the kernel versions of batch instances at a scheduled time</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
