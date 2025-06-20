# DWS MCP Server 


## Version
v0.1.0

## Overview

DWS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DWS. Full-chain management of DWS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Alarm management | UpdateAlarmSub | Update subscribed alarms. | To be tested |
|  | ListAlarmStatistic | Query alarm statistics. | To be tested |
|  | ListAlarmConfigs | Query alarm configurations. | To be tested |
|  | DeleteAlarmSub | Delete subscribed alarms. | To be tested |
|  | ListAlarmSubs | Query subscribed alarms. | To be tested |
|  | CreateAlarmSub | Create an alarm subscription. | To be tested |
|  | ListAlarmDetail | Query the alarm details list. | To be tested |
| Audit Log | ListAuditLog | Query audit logs. | To be tested |
| Cluster management | ShowClusters | This API is used to query and display the cluster list. | To be tested |
|  | SaveClusterDescriptionInfo | Modifies the cluster description. | To be tested |
|  | DeleteDwsCluster | This API is used to delete a cluster. After a cluster is deleted, all resources in the cluster, including customer data, are released. To be safe, create a snapshot for the cluster before deleting it. | To be tested |
|  | CreateClusterV2 | This API is used to create a cluster. | To be tested |
|  | CheckCluster | Precheck before creating a cluster to identify issues such as insufficient subnets and quotas in advance to prevent cluster creation failures after a cluster creation request is initiated. | To be tested |
|  | ShowClusterEncryptInfo | Obtain the cluster encryption information. Non-encrypted clusters do not support this function. The returned information is empty. | To be tested |
|  | ListTagsForResource | Query the enterprise project information of a specified cluster. | To be tested |
|  | SwitchOverCluster | When the cluster status is Unbalanced, the number of primary instances on some nodes increases, causing heavy load. In this case, the cluster status is normal, but the overall performance is lower than that in the balanced state. You can restore the cluster active/standby to switch the cluster status to Available. | To be tested |
|  | ShowClusterVolume | Query the disk usage of nodes on the tenant side. | To be tested |
|  | ShowClusterFlavor | Query the specifications used by a cluster. | To be tested |
|  | ShowResourceStatistics | This interface is used to query resource statistics. | To be tested |
|  | ModifyClusterTimezone | Modify the cluster time zone. This operation will change the time zones of both the operating system and database. | To be tested |
|  | StopCluster | Stop the cluster. | To be tested |
|  | ListClusterDetails | This API is used to query cluster details. | To be tested |
|  | ListDssPools | Obtain the dedicated distributed storage pool list, including only the SSD dedicated resource pool information. | To be tested |
|  | ListTopoRings | Query the ring node information in the cluster topology. | To be tested |
|  | RestartCluster | This API is used to restart a cluster. | To be tested |
|  | CancelReadonlyCluster | When the cluster enters the read-only state, you cannot perform database-related operations. You can cancel the read-only state of the cluster on the management console. The read-only status may be triggered by high disk usage. Therefore, you need to clear or expand the cluster data. - Removed read-only support for 1.7.2 and above. | To be tested |
|  | EncryptCluster | Convert to an encrypted cluster. | To be tested |
|  | ListClusterActions | Query cluster task details. | To be tested |
|  | ListNodeTypes | This API is used to query the flavors supported by all GaussDB (DWS) services. | To be tested |
|  | StartCluster | Start the cluster. | To be tested |
|  | ModifyClusterName | Change the cluster name. | To be tested |
|  | RotateKey | Roll the encryption cluster key. | To be tested |
| Cluster management interface | CreateCluster | Create an MRS cluster and submit a job in the cluster. This interface is not compatible with Sahara. | To be tested |
|  | DeleteCluster | You can delete the cluster service after data processing and analysis are complete or the cluster is running abnormally and cannot provide services. This interface is compatible with Sahara. | To be tested |
|  | ListClusters | View the cluster list created by the user. This interface is not compatible with Sahara. | To be tested |
| ClusterManagement | ShrinkCluster | The MRS cluster is scaled in. | To be tested |
| Connection management | AssociateElb | The ELB interface is bound to the cluster. | To be tested |
|  | ListElbs | Query the list of ELBs that can be associated with a cluster. | To be tested |
|  | DeleteClusterDns | Deletes a specified cluster domain name. | To be tested |
|  | AssociateEip | The cluster is bound to an EIP. | To be tested |
|  | ChangeSecurityGroup | Modify the security group bound to the SFS Turbo file system. If the security group modification task is an asynchronous task, you can determine whether to modify the security group status based on the sub_status field returned by Querying a Single File System. If the sub_status field is 232, the security group is successfully modified. | To be tested |
|  | UpdateClusterDns | Change the domain name for a specified cluster. | To be tested |
|  | DisassociateElb | This API is used to unbind the cluster from the ELB. | To be tested |
|  | CreateClusterDns | This command is used to apply for a domain name for a specified cluster. | To be tested |
|  | DisassociateEip | Unbind an EIP from a cluster. | To be tested |
|  | ListClusterEndpoints | Query connection information. including public and private domain names. | To be tested |
| DR Instance | DeleteDisasterRecovery | Interface for deleting the DR relationship between an instance | To be tested |
| DR management | ListAvailableDisasterClusters | This interface is used to query the list of available DR clusters. | To be tested |
|  | UpdateDisasterInfo | This interface is used to update the DR configuration. | To be tested |
|  | StartDisasterRecovery | This interface is used to start DR operations. | To be tested |
|  | ShowDisasterDetail | This interface is used to query the details of a single DR. | To be tested |
|  | ShowDisasterProgress | This interface is used to query DR progress details. | To be tested |
|  | CreateDisasterRecovery | This interface is used to create an inter-cluster DR. | To be tested |
|  | PauseDisasterRecovery | This interface is used to stop DR operations. | To be tested |
|  | ListDisasterRecover | This interface is used to query the DR list. | To be tested |
|  | SwitchoverDisasterRecovery | This interface is used to perform DR switchover. | To be tested |
|  | CheckDisasterName | This interface is used to check whether the DR name is available. | To be tested |
|  | RestoreDisaster | This interface is used to perform DR recovery operations after the standby cluster becomes available after the active/standby cluster is switched over unexpectedly. | To be tested |
|  | SwitchFailoverDisaster | This interface is used to perform the active/standby cluster switchover in the case of a DR exception. | To be tested |
| Data Source | ListDataSource | This interface is used to query data sources. | To be tested |
| Data Source Management | DeleteDataSource |  | To be tested |
|  | CreateDataSource |  | To be tested |
|  | UpdateDataSource |  | To be tested |
| Database permission management | UpdateDatabaseAuthority | Modify the database object permission. | To be tested |
|  | ListDatabaseUsers | Query all database users and roles. | To be tested |
|  | ListDatabaseUserAuthorities | Query the permissions of a user or role. | To be tested |
|  | ShowDatabaseAuthority | Query the database object permission. | To be tested |
|  | ExecuteDatabaseOmUserAction | Perform operations on the database O&M account. | To be tested |
|  | ShowDatabaseUser | Query the information about a specified user. | To be tested |
|  | SyncIamUsers | Synchronize the IAM user to the database. | To be tested |
|  | ExportUserAuthority | Exports the permission list of database users and roles. The output stream returned by the interface is an XLSX file. | To be tested |
|  | CreateDatabaseUser | Create a database user or role. | To be tested |
|  | UpdateDatabaseUserInfo | Modifies the information about a specified user. | To be tested |
|  | ShowDatabaseOmUserStatus | Obtain the database O&M account status. | To be tested |
|  | DeleteDatabaseUser | Delete a database user. | To be tested |
|  | ListSyncRecords | Query the synchronization records of an identity source. | To be tested |
|  | ExportDatabaseUsers | Export database users and roles. The interface returns an output stream in an XLSX file. | To be tested |
| EVS Snapshot | ListSnapshots | Query the details about EVS snapshots. | To be tested |
|  | CreateSnapshot | Create an EVS snapshot. | To be tested |
|  | DeleteSnapshot | Delete an EVS snapshot. | To be tested |
| Event Management | DeleteEventSub | Delete subscribed events. | To be tested |
|  | CreateEventSub | Add subscribed events. | To be tested |
|  | ListEventSubs | Query subscribed events. | To be tested |
|  | ListEventSpecs | Query the event configuration. | To be tested |
|  | UpdateEventSub | Update the subscription event. | To be tested |
| Exclusive Instance Management | ShowInstance | Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
| Function Log | EnableLtsLogs | Enable the lts log reporting function. | To be tested |
| Function test event | ListEvents | Obtain the test event list of a specified function | To be tested |
| Host monitoring | ListMonitorIndicators | Query performance monitoring indicators. | To be tested |
|  | ListMetrics | Query the cluster usage indicator list. | To be tested |
|  | ListQueries | This interface is used to query the list of real-time SQL statements. | To be tested |
|  | ListMetricsData | Obtain the collected data of a specified indicator. | To be tested |
|  | ListHostDisk | This API is used to query disk information. | To be tested |
|  | ListHostOverview | This API is used to query the host overview. | To be tested |
|  | ListMonitorIndicatorData | This API is used to query historical monitoring data. | To be tested |
|  | ShowQueryDetail | Query SQL execution information. | To be tested |
|  | ListHostNet | Openapi obtains the NIC status. | To be tested |
|  | ListTablesStatistic | This interface is used to query the skew or dirty page rate of a table. | To be tested |
| Image Tag | ListTags | Query the image tag list based on different conditions. | To be tested |
| Instance Management | ResetPassword | Reset the password (only for instances with SSL enabled). | To be tested |
| Log management | DisableLtsLogs | This API is used to disable LTS in a cluster. | To be tested |
|  | ListLtsLogs | Obtains the LTS log list. | To be tested |
| Logical cluster management | ListLogicalClusterRings | Query information about available ring nodes in a logical cluster. | To be tested |
|  | EnableLogicalCluster | This interface is used to switch the logical cluster switch. It is used only to determine whether to display functional modules related to the logical cluster on the page. If the cluster is a logical cluster, modifying this API has no impact. | To be tested |
|  | ListLogicalClusterPlans | This API is used to query the scheduled addition and deletion plans of a logical cluster. | To be tested |
|  | CreateLogicalClusterPlan | This interface is used to add a scheduled adding or deleting plan for a logical cluster. | To be tested |
|  | RestartLogicalCluster | This API is used to restart a logical cluster. | To be tested |
|  | ShrinkLogicalCluster | You can scale in a logical cluster from the elastic pool or logical cluster. | To be tested |
|  | ConvertToLogicalCluster | Conversion from a physical cluster to a logical cluster. | To be tested |
|  | ListLogicalClusterVolumes | Query the disk information of a logical cluster. | To be tested |
|  | EnableLogicalClusterPlan | This API is used to enable the scheduled adding and deleting plan of the logical cluster. | To be tested |
|  | ListLogicalClusters | Query the logical cluster list. | To be tested |
|  | DisableLogicalClusterPlan | Disable the schedule for adding and deleting logical clusters. | To be tested |
|  | DeleteLogicalClusterPlan | This API is used to delete a scheduled adding or deleting plan for a logical cluster. | To be tested |
|  | CreateLogicalCluster | Create a logical cluster. | To be tested |
|  | UpdateLogicalCluster | This API is used to edit and modify a logical cluster. | To be tested |
|  | DeleteLogicalCluster | This API is used to delete a logical cluster. | To be tested |
|  | ListLogicalClusterTasks | Query the task information about a logical cluster. | To be tested |
|  | UpdateLogicalClusterPlan | This API is used to edit, modify, and edit plans for adding and deleting logical clusters. | To be tested |
| Node change | ShowClusterRedistribution | This API is used to view monitoring information such as the redistribution mode, redistribution progress, and data table redistribution details of the current cluster. | To be tested |
|  | ResizeClusterWithExistedNodes | This interface is used to expand the capacity of idle nodes. | To be tested |
|  | ResizeCluster | This API is used to expand cluster capacity and add idle nodes. By default, capacity expansion is performed. | To be tested |
|  | ListClusterCn | Query the CN node list of a cluster. | To be tested |
|  | ListTargetFlavors | Query the list of target flavors that can be changed. | To be tested |
|  | DeleteClusterNodes | This interface is used to delete idle nodes. | To be tested |
|  | ExecuteFlavorChange | Change the specification. | To be tested |
|  | ExpandInstanceStorage | With the development of customer services, disk space is the first to encounter resource bottlenecks. When other resources are sufficient, disk capacity expansion can quickly relieve the bottlenecks. During the operation, services do not need to be suspended, and CPU and memory resources are not wasted. | To be tested |
|  | BatchDeleteClusterCn | After a cluster is created, the number of required CNs varies with service requirements. Therefore, the CN management function enables users to dynamically adjust the number of CNs in the cluster based on actual requirements. | To be tested |
|  | ShowClusterStorageExpandRange | This API is used to view the capacity expansion scope supported by the disk capacity expansion operation. | To be tested |
|  | StopRedistribution | This interface is used to suspend the redistribution operation in the running state. In the paused redistribution state, you can set the redistribution priority and modify the number of concurrent redistribution operations. | To be tested |
|  | CheckGrowCluster | This interface is used to check the cluster before capacity expansion and identify capacity expansion failures caused by insufficient subnets and insufficient permissions. | To be tested |
|  | ListRedistributionSchema | Obtain the schema information of the table to be redistributed. | To be tested |
|  | ExecuteRedistributionCluster | This API is used to redistribute data on old nodes to new nodes after cluster capacity expansion. After data redistribution, the service response speed is greatly improved. | To be tested |
|  | UpdateRedistributionConfigurations | Update the redistribution configuration. | To be tested |
|  | SetRedistributionPriority | Update the redistribution table priority. | To be tested |
|  | RestoreRedistribution | This API is used to resume the redistribution operation in the suspended state. Only the data warehouse 2.0 cluster is supported. | To be tested |
|  | ListClusterNodes | Query the node list. | To be tested |
|  | BatchCreateClusterCn | After a cluster is created, the number of required CNs varies with service requirements. Therefore, the CN management function enables users to dynamically adjust the number of CNs in the cluster based on actual requirements. | To be tested |
|  | ListClusterScaleInNumbers | Query the proper number of scales to be reduced. | To be tested |
|  | CheckClusterShrink | Check before and after the scale-in meets the normal operation requirements. | To be tested |
| Parameter Configuration | ListClusterConfigurationsParameter | Query the parameter groups associated with the cluster. | To be tested |
|  | UpdateConfiguration | Modifies a parameter template. | To be tested |
|  | ListConfigurationsAuditRecords | Query parameter modification audit records. | To be tested |
|  | ListClusterConfigurations | Query the parameter groups associated with the cluster. | To be tested |
| Query | ListSchemas | List Schemas | To be tested |
| Quota Management | ListQuotas | Obtain quota information | To be tested |
| Resource management | ListWorkloadQueue | Query the workload queue. | To be tested |
|  | ShowWorkloadPlanStage | Query details about the workload planning phase. | To be tested |
|  | ShowWorkloadPlan | Query details about a workload plan. | To be tested |
|  | AddWorkloadPlanStage | Add a workload planning phase. | To be tested |
|  | ListWorkloadRules | Query the list of abnormal rules of the current cluster. | To be tested |
|  | UpdateQueueResources | Updates the configuration information about the workload queue resource. | To be tested |
|  | DeleteWorkloadPlanStage | Delete a workload plan. | To be tested |
|  | CreateClusterWorkload | Enable or disable the resource management function. By default, the resource management function is enabled for new clusters. | To be tested |
|  | ShowWorkloadQueue | Obtain the details about the workload queue. | To be tested |
|  | CreateWorkloadPlan | Add a workload plan. | To be tested |
|  | StopWorkloadPlan | Stop the workload plan. | To be tested |
|  | UpdateWorkloadPlanStage | Modify the resource management plan phase. | To be tested |
|  | DeleteWorkloadQueue | This API is used to delete a resource pool. | To be tested |
|  | ListClusterWorkload | Query the resource management function. | To be tested |
|  | AddWorkloadRule | Add an exception rule. | To be tested |
|  | ListWorkloadQueueUsers | Obtain the list of users bound to a workload queue. | To be tested |
|  | AddWorkloadQueue | Add a workload queue. | To be tested |
|  | DeleteWorkloadPlan | Delete a workload plan. | To be tested |
|  | DeleteQueueUserList | Delete the user bound to the workload queue. | To be tested |
|  | StartWorkloadPlan | Start the workload plan. | To be tested |
|  | SwitchPlanStage | Switch the workload planning phase. | To be tested |
|  | ListPlanExecLogs | View plan execution logs. | To be tested |
|  | UpdateSchemas | Updates the schema space quota. | To be tested |
|  | ListWorkloadPlans | Query all resource management plans in a cluster. | To be tested |
|  | AddQueueUserList | Add the user bound to the workload queue. | To be tested |
| Security Overview | ListStatistics | Query the number of security overview requests and attacks. | To be tested |
| Snapshot Management | ListSnapshotDetails | This API is used to query snapshot details by snapshot ID. | To be tested |
|  | RestoreCluster | This API is used to restore a cluster using a snapshot. | To be tested |
|  | AddSnapshotCrossRegionPolicy | This interface is used to set cross-region backup configurations. | To be tested |
|  | ListSnapshotCrossRegion | This interface is used to obtain the available sites for cross-region snapshots. | To be tested |
|  | DeleteSnapshotPolicy | This API is used to delete a snapshot policy. | To be tested |
|  | CheckTableRestore | This interface is used to restore the table name detection. | To be tested |
|  | ListClusterSnapshots | This API is used to query the cluster snapshot list. | To be tested |
|  | ListSnapshotStatistics | Snapshot statistics. | To be tested |
|  | CopySnapshot | This API is used to copy an automatic snapshot. | To be tested |
|  | CreateSnapshotPolicy | This API is used to set a snapshot policy. | To be tested |
|  | DeleteSnapshotCrossRegionPolicy | This interface is used to delete cross-region backup configurations. | To be tested |
|  | ListSnapshotCrossRegionPolicy | This API is used to query all cross-region snapshot configurations. | To be tested |
|  | RestoreTable | This interface is used to restore tables. | To be tested |
|  | ListSnapshotPolicy | Query the snapshot policy. | To be tested |
| Tag Management | BatchCreateResourceTag | Add tags to a specified cluster in batches. | To be tested |
|  | BatchDeleteResourceTag | This API is used to delete tags from a specified cluster in batches. | To be tested |
| Tag management interface | ListClusterTags | Query the label information of a specified cluster. | To be tested |
| Task Management | ListJobDetails | Query the task progress information. | To be tested |
| Upgrade Management | UpdateMaintenanceWindow | You can set the maintenance time segment based on service requirements. You are advised to set the maintainable period during off-peak hours to avoid abnormal service interruption during maintenance. | To be tested |
|  | ListUpdatableVersion | Obtain the target version of the cluster to be upgraded. | To be tested |
|  | ExecuteClusterUpgradeAction | Deliver cluster upgrade operations. | To be tested |
|  | ListUpdateRecord | This API is used to obtain the upgrade records of the current cluster. | To be tested |
| VpnGateway | ListAvailabilityZones | Querying the AZ of the VPN gateway | To be tested |

