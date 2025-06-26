# DWS MCP Server 


## Version
v0.1.0

## Overview

DWS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DWS. Full-chain management of DWS resources can be carried out based on natural language.

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
                    <td rowspan="7">Alarm management</td>
                    <td>UpdateAlarmSub</td>
                    <td>Update subscribed alarms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmStatistic</td>
                    <td>Query alarm statistics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmConfigs</td>
                    <td>Query alarm configurations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlarmSub</td>
                    <td>Delete subscribed alarms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmSubs</td>
                    <td>Query subscribed alarms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlarmSub</td>
                    <td>Create an alarm subscription.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmDetail</td>
                    <td>Query the alarm details list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Audit Log</td>
                    <td>ListAuditLog</td>
                    <td>Query audit logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="24">Cluster management</td>
                    <td>ShowClusters</td>
                    <td>This API is used to query and display the cluster list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveClusterDescriptionInfo</td>
                    <td>Modifies the cluster description.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDwsCluster</td>
                    <td>This API is used to delete a cluster. After a cluster is deleted, all resources in the cluster, including customer data, are released. To be safe, create a snapshot for the cluster before deleting it.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClusterV2</td>
                    <td>This API is used to create a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckCluster</td>
                    <td>Precheck before creating a cluster to identify issues such as insufficient subnets and quotas in advance to prevent cluster creation failures after a cluster creation request is initiated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterEncryptInfo</td>
                    <td>Obtain the cluster encryption information. Non-encrypted clusters do not support this function. The returned information is empty.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagsForResource</td>
                    <td>Query the enterprise project information of a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchOverCluster</td>
                    <td>When the cluster status is Unbalanced, the number of primary instances on some nodes increases, causing heavy load. In this case, the cluster status is normal, but the overall performance is lower than that in the balanced state. You can restore the cluster active/standby to switch the cluster status to Available.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterVolume</td>
                    <td>Query the disk usage of nodes on the tenant side.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterFlavor</td>
                    <td>Query the specifications used by a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceStatistics</td>
                    <td>This interface is used to query resource statistics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyClusterTimezone</td>
                    <td>Modify the cluster time zone. This operation will change the time zones of both the operating system and database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopCluster</td>
                    <td>Stop the cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterDetails</td>
                    <td>This API is used to query cluster details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDssPools</td>
                    <td>Obtain the dedicated distributed storage pool list, including only the SSD dedicated resource pool information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopoRings</td>
                    <td>Query the ring node information in the cluster topology.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartCluster</td>
                    <td>This API is used to restart a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelReadonlyCluster</td>
                    <td>When the cluster enters the read-only state, you cannot perform database-related operations. You can cancel the read-only state of the cluster on the management console. The read-only status may be triggered by high disk usage. Therefore, you need to clear or expand the cluster data. - Removed read-only support for 1.7.2 and above.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EncryptCluster</td>
                    <td>Convert to an encrypted cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterActions</td>
                    <td>Query cluster task details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodeTypes</td>
                    <td>This API is used to query the flavors supported by all GaussDB (DWS) services.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartCluster</td>
                    <td>Start the cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyClusterName</td>
                    <td>Change the cluster name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RotateKey</td>
                    <td>Roll the encryption cluster key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Cluster management interface</td>
                    <td>CreateCluster</td>
                    <td>Create an MRS cluster and submit a job in the cluster. This interface is not compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCluster</td>
                    <td>You can delete the cluster service after data processing and analysis are complete or the cluster is running abnormally and cannot provide services. This interface is compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusters</td>
                    <td>View the cluster list created by the user. This interface is not compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ClusterManagement</td>
                    <td>ShrinkCluster</td>
                    <td>The MRS cluster is scaled in.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Connection management</td>
                    <td>AssociateElb</td>
                    <td>The ELB interface is bound to the cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListElbs</td>
                    <td>Query the list of ELBs that can be associated with a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClusterDns</td>
                    <td>Deletes a specified cluster domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateEip</td>
                    <td>The cluster is bound to an EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeSecurityGroup</td>
                    <td>Modify the security group bound to the SFS Turbo file system. If the security group modification task is an asynchronous task, you can determine whether to modify the security group status based on the sub_status field returned by Querying a Single File System. If the sub_status field is 232, the security group is successfully modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClusterDns</td>
                    <td>Change the domain name for a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateElb</td>
                    <td>This API is used to unbind the cluster from the ELB.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClusterDns</td>
                    <td>This command is used to apply for a domain name for a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateEip</td>
                    <td>Unbind an EIP from a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterEndpoints</td>
                    <td>Query connection information. including public and private domain names.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">DR Instance</td>
                    <td>DeleteDisasterRecovery</td>
                    <td>Interface for deleting the DR relationship between an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">DR management</td>
                    <td>ListAvailableDisasterClusters</td>
                    <td>This interface is used to query the list of available DR clusters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDisasterInfo</td>
                    <td>This interface is used to update the DR configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartDisasterRecovery</td>
                    <td>This interface is used to start DR operations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDisasterDetail</td>
                    <td>This interface is used to query the details of a single DR.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDisasterProgress</td>
                    <td>This interface is used to query DR progress details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDisasterRecovery</td>
                    <td>This interface is used to create an inter-cluster DR.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PauseDisasterRecovery</td>
                    <td>This interface is used to stop DR operations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDisasterRecover</td>
                    <td>This interface is used to query the DR list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchoverDisasterRecovery</td>
                    <td>This interface is used to perform DR switchover.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckDisasterName</td>
                    <td>This interface is used to check whether the DR name is available.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreDisaster</td>
                    <td>This interface is used to perform DR recovery operations after the standby cluster becomes available after the active/standby cluster is switched over unexpectedly.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchFailoverDisaster</td>
                    <td>This interface is used to perform the active/standby cluster switchover in the case of a DR exception.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Data Source</td>
                    <td>ListDataSource</td>
                    <td>This interface is used to query data sources.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Data Source Management</td>
                    <td>DeleteDataSource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataSource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataSource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Database permission management</td>
                    <td>UpdateDatabaseAuthority</td>
                    <td>Modify the database object permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseUsers</td>
                    <td>Query all database users and roles.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseUserAuthorities</td>
                    <td>Query the permissions of a user or role.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatabaseAuthority</td>
                    <td>Query the database object permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteDatabaseOmUserAction</td>
                    <td>Perform operations on the database O&amp;M account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatabaseUser</td>
                    <td>Query the information about a specified user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncIamUsers</td>
                    <td>Synchronize the IAM user to the database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportUserAuthority</td>
                    <td>Exports the permission list of database users and roles. The output stream returned by the interface is an XLSX file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabaseUser</td>
                    <td>Create a database user or role.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDatabaseUserInfo</td>
                    <td>Modifies the information about a specified user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatabaseOmUserStatus</td>
                    <td>Obtain the database O&amp;M account status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabaseUser</td>
                    <td>Delete a database user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSyncRecords</td>
                    <td>Query the synchronization records of an identity source.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportDatabaseUsers</td>
                    <td>Export database users and roles. The interface returns an output stream in an XLSX file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">EVS Snapshot</td>
                    <td>ListSnapshots</td>
                    <td>Query the details about EVS snapshots.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSnapshot</td>
                    <td>Create an EVS snapshot.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSnapshot</td>
                    <td>Delete an EVS snapshot.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Event Management</td>
                    <td>DeleteEventSub</td>
                    <td>Delete subscribed events.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEventSub</td>
                    <td>Add subscribed events.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventSubs</td>
                    <td>Query subscribed events.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventSpecs</td>
                    <td>Query the event configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEventSub</td>
                    <td>Update the subscription event.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Exclusive Instance Management</td>
                    <td>ShowInstance</td>
                    <td>Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Function Log</td>
                    <td>EnableLtsLogs</td>
                    <td>Enable the lts log reporting function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Function test event</td>
                    <td>ListEvents</td>
                    <td>Obtain the test event list of a specified function</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Host monitoring</td>
                    <td>ListMonitorIndicators</td>
                    <td>Query performance monitoring indicators.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetrics</td>
                    <td>Query the cluster usage indicator list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueries</td>
                    <td>This interface is used to query the list of real-time SQL statements.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetricsData</td>
                    <td>Obtain the collected data of a specified indicator.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostDisk</td>
                    <td>This API is used to query disk information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostOverview</td>
                    <td>This API is used to query the host overview.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMonitorIndicatorData</td>
                    <td>This API is used to query historical monitoring data.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowQueryDetail</td>
                    <td>Query SQL execution information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostNet</td>
                    <td>Openapi obtains the NIC status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTablesStatistic</td>
                    <td>This interface is used to query the skew or dirty page rate of a table.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Image Tag</td>
                    <td>ListTags</td>
                    <td>Query the image tag list based on different conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Instance Management</td>
                    <td>ResetPassword</td>
                    <td>Reset the password (only for instances with SSL enabled).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Log management</td>
                    <td>DisableLtsLogs</td>
                    <td>This API is used to disable LTS in a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLtsLogs</td>
                    <td>Obtains the LTS log list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">Logical cluster management</td>
                    <td>ListLogicalClusterRings</td>
                    <td>Query information about available ring nodes in a logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableLogicalCluster</td>
                    <td>This interface is used to switch the logical cluster switch. It is used only to determine whether to display functional modules related to the logical cluster on the page. If the cluster is a logical cluster, modifying this API has no impact.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogicalClusterPlans</td>
                    <td>This API is used to query the scheduled addition and deletion plans of a logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogicalClusterPlan</td>
                    <td>This interface is used to add a scheduled adding or deleting plan for a logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartLogicalCluster</td>
                    <td>This API is used to restart a logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShrinkLogicalCluster</td>
                    <td>You can scale in a logical cluster from the elastic pool or logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConvertToLogicalCluster</td>
                    <td>Conversion from a physical cluster to a logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogicalClusterVolumes</td>
                    <td>Query the disk information of a logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableLogicalClusterPlan</td>
                    <td>This API is used to enable the scheduled adding and deleting plan of the logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogicalClusters</td>
                    <td>Query the logical cluster list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableLogicalClusterPlan</td>
                    <td>Disable the schedule for adding and deleting logical clusters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogicalClusterPlan</td>
                    <td>This API is used to delete a scheduled adding or deleting plan for a logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogicalCluster</td>
                    <td>Create a logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogicalCluster</td>
                    <td>This API is used to edit and modify a logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogicalCluster</td>
                    <td>This API is used to delete a logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogicalClusterTasks</td>
                    <td>Query the task information about a logical cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogicalClusterPlan</td>
                    <td>This API is used to edit, modify, and edit plans for adding and deleting logical clusters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="21">Node change</td>
                    <td>ShowClusterRedistribution</td>
                    <td>This API is used to view monitoring information such as the redistribution mode, redistribution progress, and data table redistribution details of the current cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeClusterWithExistedNodes</td>
                    <td>This interface is used to expand the capacity of idle nodes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeCluster</td>
                    <td>This API is used to expand cluster capacity and add idle nodes. By default, capacity expansion is performed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterCn</td>
                    <td>Query the CN node list of a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTargetFlavors</td>
                    <td>Query the list of target flavors that can be changed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClusterNodes</td>
                    <td>This interface is used to delete idle nodes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteFlavorChange</td>
                    <td>Change the specification.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandInstanceStorage</td>
                    <td>With the development of customer services, disk space is the first to encounter resource bottlenecks. When other resources are sufficient, disk capacity expansion can quickly relieve the bottlenecks. During the operation, services do not need to be suspended, and CPU and memory resources are not wasted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteClusterCn</td>
                    <td>After a cluster is created, the number of required CNs varies with service requirements. Therefore, the CN management function enables users to dynamically adjust the number of CNs in the cluster based on actual requirements.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterStorageExpandRange</td>
                    <td>This API is used to view the capacity expansion scope supported by the disk capacity expansion operation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopRedistribution</td>
                    <td>This interface is used to suspend the redistribution operation in the running state. In the paused redistribution state, you can set the redistribution priority and modify the number of concurrent redistribution operations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckGrowCluster</td>
                    <td>This interface is used to check the cluster before capacity expansion and identify capacity expansion failures caused by insufficient subnets and insufficient permissions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRedistributionSchema</td>
                    <td>Obtain the schema information of the table to be redistributed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteRedistributionCluster</td>
                    <td>This API is used to redistribute data on old nodes to new nodes after cluster capacity expansion. After data redistribution, the service response speed is greatly improved.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRedistributionConfigurations</td>
                    <td>Update the redistribution configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetRedistributionPriority</td>
                    <td>Update the redistribution table priority.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreRedistribution</td>
                    <td>This API is used to resume the redistribution operation in the suspended state. Only the data warehouse 2.0 cluster is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterNodes</td>
                    <td>Query the node list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateClusterCn</td>
                    <td>After a cluster is created, the number of required CNs varies with service requirements. Therefore, the CN management function enables users to dynamically adjust the number of CNs in the cluster based on actual requirements.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterScaleInNumbers</td>
                    <td>Query the proper number of scales to be reduced.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckClusterShrink</td>
                    <td>Check before and after the scale-in meets the normal operation requirements.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Parameter Configuration</td>
                    <td>ListClusterConfigurationsParameter</td>
                    <td>Query the parameter groups associated with the cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfiguration</td>
                    <td>Modifies a parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurationsAuditRecords</td>
                    <td>Query parameter modification audit records.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterConfigurations</td>
                    <td>Query the parameter groups associated with the cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query</td>
                    <td>ListSchemas</td>
                    <td>List Schemas</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota Management</td>
                    <td>ListQuotas</td>
                    <td>Obtain quota information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="25">Resource management</td>
                    <td>ListWorkloadQueue</td>
                    <td>Query the workload queue.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkloadPlanStage</td>
                    <td>Query details about the workload planning phase.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkloadPlan</td>
                    <td>Query details about a workload plan.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddWorkloadPlanStage</td>
                    <td>Add a workload planning phase.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkloadRules</td>
                    <td>Query the list of abnormal rules of the current cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateQueueResources</td>
                    <td>Updates the configuration information about the workload queue resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkloadPlanStage</td>
                    <td>Delete a workload plan.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClusterWorkload</td>
                    <td>Enable or disable the resource management function. By default, the resource management function is enabled for new clusters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkloadQueue</td>
                    <td>Obtain the details about the workload queue.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkloadPlan</td>
                    <td>Add a workload plan.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopWorkloadPlan</td>
                    <td>Stop the workload plan.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkloadPlanStage</td>
                    <td>Modify the resource management plan phase.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkloadQueue</td>
                    <td>This API is used to delete a resource pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterWorkload</td>
                    <td>Query the resource management function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddWorkloadRule</td>
                    <td>Add an exception rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkloadQueueUsers</td>
                    <td>Obtain the list of users bound to a workload queue.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddWorkloadQueue</td>
                    <td>Add a workload queue.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkloadPlan</td>
                    <td>Delete a workload plan.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteQueueUserList</td>
                    <td>Delete the user bound to the workload queue.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartWorkloadPlan</td>
                    <td>Start the workload plan.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchPlanStage</td>
                    <td>Switch the workload planning phase.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlanExecLogs</td>
                    <td>View plan execution logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSchemas</td>
                    <td>Updates the schema space quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkloadPlans</td>
                    <td>Query all resource management plans in a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddQueueUserList</td>
                    <td>Add the user bound to the workload queue.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Security Overview</td>
                    <td>ListStatistics</td>
                    <td>Query the number of security overview requests and attacks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Snapshot Management</td>
                    <td>ListSnapshotDetails</td>
                    <td>This API is used to query snapshot details by snapshot ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreCluster</td>
                    <td>This API is used to restore a cluster using a snapshot.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddSnapshotCrossRegionPolicy</td>
                    <td>This interface is used to set cross-region backup configurations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshotCrossRegion</td>
                    <td>This interface is used to obtain the available sites for cross-region snapshots.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSnapshotPolicy</td>
                    <td>This API is used to delete a snapshot policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckTableRestore</td>
                    <td>This interface is used to restore the table name detection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterSnapshots</td>
                    <td>This API is used to query the cluster snapshot list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshotStatistics</td>
                    <td>Snapshot statistics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopySnapshot</td>
                    <td>This API is used to copy an automatic snapshot.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSnapshotPolicy</td>
                    <td>This API is used to set a snapshot policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSnapshotCrossRegionPolicy</td>
                    <td>This interface is used to delete cross-region backup configurations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshotCrossRegionPolicy</td>
                    <td>This API is used to query all cross-region snapshot configurations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreTable</td>
                    <td>This interface is used to restore tables.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshotPolicy</td>
                    <td>Query the snapshot policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tag Management</td>
                    <td>BatchCreateResourceTag</td>
                    <td>Add tags to a specified cluster in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteResourceTag</td>
                    <td>This API is used to delete tags from a specified cluster in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tag management interface</td>
                    <td>ListClusterTags</td>
                    <td>Query the label information of a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Task Management</td>
                    <td>ListJobDetails</td>
                    <td>Query the task progress information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Upgrade Management</td>
                    <td>UpdateMaintenanceWindow</td>
                    <td>You can set the maintenance time segment based on service requirements. You are advised to set the maintainable period during off-peak hours to avoid abnormal service interruption during maintenance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpdatableVersion</td>
                    <td>Obtain the target version of the cluster to be upgraded.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteClusterUpgradeAction</td>
                    <td>Deliver cluster upgrade operations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpdateRecord</td>
                    <td>This API is used to obtain the upgrade records of the current cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">VpnGateway</td>
                    <td>ListAvailabilityZones</td>
                    <td>Querying the AZ of the VPN gateway</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
