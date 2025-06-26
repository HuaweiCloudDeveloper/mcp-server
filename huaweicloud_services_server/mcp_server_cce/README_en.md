# CCE MCP Server 


## Version
v0.1.0

## Overview

CCE MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CCE. Full-chain management of CCE resources can be carried out based on natural language.

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
                    <td rowspan="7">Add-on management</td>
                    <td>UpdateAddonInstance</td>
                    <td>Updates the function of the plug-in instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAddonTemplates</td>
                    <td>A plug-in template query interface, which is used to query plug-in information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAddonInstances</td>
                    <td>Obtain all installed plug-in instances in a cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAddonInstance</td>
                    <td>Deletes the function of a plug-in instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAddonInstance</td>
                    <td>Install the plug-in instance based on the provided plug-in template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollbackAddonInstance</td>
                    <td>Roll back the plug-in instance to the source version. Only the current plug-in instance version can be rolled back to the source version (status.isRollbackable is set to true). If the plug-in instance status is running, available, abnormal, upgradeFailed, or rollbackFailed, the plug-in instance can be rolled back.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAddonInstance</td>
                    <td>Obtains the plug-in instance details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Allied management</td>
                    <td>ListNodes</td>
                    <td>Function description: Users can use this API to query the list of trusted nodes (including aggregation nodes and compute nodes) in an alliance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Autopilot</td>
                    <td>ShowAutopilotAddonInstance</td>
                    <td>Obtain the plug-in instance details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutopilotAddonInstance</td>
                    <td>Updates the function of the plug-in instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollbackAutopilotAddonInstance</td>
                    <td>Roll back the plug-in instance to the source version. Only the current plug-in instance version can be rolled back to the source version (status.isRollbackable is set to true). If the plug-in instance status is running, available, abnormal, upgradeFailed, or rollbackFailed, the plug-in instance can be rolled back.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotAddonTemplates</td>
                    <td>A plug-in template query interface, used to query plug-in information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAutopilotAddonInstance</td>
                    <td>Deletes the function of a plug-in instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotAddonInstance</td>
                    <td>Install the plug-in instance based on the provided plug-in template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotAddonInstances</td>
                    <td>Obtain all installed plug-in instances in a cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Cluster management</td>
                    <td>AwakeCluster</td>
                    <td>Cluster wakeup is used to wake up a hibernation cluster. After the cluster wakeup, the controller node resource fee will continue to be charged.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>HibernateCluster</td>
                    <td>Cluster hibernation is used to hibernate a running cluster. After the hibernation, the system does not charge the controller node resources.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCluster</td>
                    <td>This API is used to update a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeKubernetesClusterCert</td>
                    <td>This API is used to revoke the user certificate of a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterConfig</td>
                    <td>Obtain the LTS configuration information reported by cluster components</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKubernetesClusterCert</td>
                    <td>This API is used to obtain the certificate information of a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePartition</td>
                    <td>Create a partition</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePartition</td>
                    <td>Update a partition</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClusterEip</td>
                    <td>This API is used to bind or unbind the public network API server address of a cluster based on the cluster ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPartition</td>
                    <td>Obtain the details of a partition.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterEndpoints</td>
                    <td>This API is used to obtain the cluster access address based on the cluster ID, including the private IP address (VIP returned by the HA cluster) and public IP address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClusterLogConfig</td>
                    <td>Users can select the components whose logs are reported to LTS on the cluster management node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Cluster management (Autopilot)</td>
                    <td>ListAutopilotClusters</td>
                    <td>This API is used to obtain details about all clusters in a specified project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotCluster</td>
                    <td>This API is used to create an empty cluster. (That is, only the master control node is configured.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotKubernetesClusterCert</td>
                    <td>This API is used to obtain the certificate information of a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotClusterEndpoints</td>
                    <td>This API is used to obtain the cluster access address based on the cluster ID, including the private IP address (VIP returned by the HA cluster) and public IP address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAutopilotCluster</td>
                    <td>This API is used to delete a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutopilotClusterEip</td>
                    <td>This API is used to bind or unbind the public network API server address of a cluster based on the cluster ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotCluster</td>
                    <td>This API is used to obtain details about a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutopilotCluster</td>
                    <td>This API is used to update a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotJob</td>
                    <td>This API is used to obtain task information. This API is used to query the progress of a specified task based on the job ID returned after a task request is delivered.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Cluster management interface</td>
                    <td>ListClusters</td>
                    <td>View the cluster list created by the user. This interface is not compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
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
                    <td rowspan="19">Cluster upgrade</td>
                    <td>ContinueUpgradeClusterTask</td>
                    <td>Continue the suspended cluster upgrade task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeWorkFlowUpdate</td>
                    <td>This API is used to update the status of a specified cluster upgrade boot task. Currently, this API is used only to cancel the upgrade process.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClusterMasterSnapshot</td>
                    <td>Cluster backup</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpgradeClusterTasks</td>
                    <td>Obtain the cluster upgrade task details list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostCheck</td>
                    <td>Confirm the cluster after the upgrade. It is recommended that this interface be used together with the console. This interface is used to provide feedback after the upgrade is complete and the customer confirms the cluster status and services are normal.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterUpgradeInfo</td>
                    <td>Obtain cluster upgrade information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUpgradeWorkFlow</td>
                    <td>This API is used to create a cluster upgrade process guidance task. After the boot task is created by calling this API, perform the cluster pre-upgrade check to start the task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterUpgradeFeatureGates</td>
                    <td>Obtain the cluster upgrade feature switch configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PauseUpgradeClusterTask</td>
                    <td>Suspend the cluster upgrade task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPreCheck</td>
                    <td>Obtain the details about the cluster pre-upgrade check task. The task ID is obtained from the uid field in the response body after the cluster check API is invoked.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeWorkFlow</td>
                    <td>This API is used to obtain the details about an upgrade boot task based on the upgrade boot task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeCluster</td>
                    <td>Upgrade the cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeClusterTask</td>
                    <td>Obtain the cluster upgrade task details. The task ID is obtained from the uid field in the response body after the cluster upgrade API is invoked.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterMasterSnapshotTasks</td>
                    <td>Obtain the cluster backup task details list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePreCheck</td>
                    <td>Cluster pre-upgrade check</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryUpgradeClusterTask</td>
                    <td>Reexecute the failed cluster upgrade task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterUpgradePaths</td>
                    <td>Obtain the cluster upgrade path</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPreCheckTasks</td>
                    <td>Obtain the cluster pre-upgrade check task details list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpgradeWorkFlows</td>
                    <td>Obtain the historical cluster upgrade boot task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="23">Cluster upgrade (Autopilot)</td>
                    <td>UpdateAutopilotMaintenanceWindow</td>
                    <td>This API is used to update the cluster maintenance window.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotPreCheckTasks</td>
                    <td>Obtain the cluster pre-upgrade check task details list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotMaintenanceWindow</td>
                    <td>This API is used to obtain the cluster maintenance window.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotClusterMasterSnapshotTasks</td>
                    <td>Obtain the cluster backup task details list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotPreCheck</td>
                    <td>Cluster pre-upgrade check</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotClusterUpgradePaths</td>
                    <td>Obtain the cluster upgrade path</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotUpgradeClusterTasks</td>
                    <td>Obtain the cluster upgrade task details list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotUpgradeClusterTask</td>
                    <td>Obtain the cluster upgrade task details. The task ID is obtained from the uid field in the response body after the cluster upgrade API is invoked.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryAutopilotUpgradeClusterTask</td>
                    <td>Reexecute the failed cluster upgrade task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotPostCheck</td>
                    <td>Confirm the cluster upgrade. It is recommended that this interface be used with the console to provide feedback after the upgrade is complete and the customer confirms the cluster status and services are normal.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotMaintenanceWindow</td>
                    <td>This API is used to create a cluster maintenance window.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotClusterMasterSnapshot</td>
                    <td>Cluster backup</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotUpgradePlans</td>
                    <td>This API is used to obtain the automatic cluster upgrade plan.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeAutopilotWorkFlowUpdate</td>
                    <td>This API is used to update the status of a specified cluster upgrade boot task. Currently, this API is used only to cancel the upgrade process.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotUpgradeWorkFlow</td>
                    <td>This API is used to create a cluster upgrade process guidance task. After the boot task is created by calling this API, perform the cluster pre-upgrade check to start the task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotClusterUpgradeFeatureGates</td>
                    <td>Obtain the cluster upgrade feature switch configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotUpgradeWorkFlow</td>
                    <td>This API is used to obtain the details about an upgrade boot task based on the upgrade boot task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutopilotUpgradePlan</td>
                    <td>This API is used to extend the automatic cluster upgrade plan.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotClusterUpgradeInfo</td>
                    <td>Obtain the cluster upgrade information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotUpgradeWorkFlows</td>
                    <td>Obtain the historical cluster upgrade boot task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeAutopilotCluster</td>
                    <td>Upgrade the cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAutopilotMaintenanceWindow</td>
                    <td>This API is used to delete the cluster maintenance window.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotPreCheck</td>
                    <td>Obtain the details about the cluster pre-upgrade check task. The task ID is obtained from the uid field in the response body after the cluster check API is invoked.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Configuration Management</td>
                    <td>ShowClusterSupportConfiguration</td>
                    <td>This API is used to query detailed configuration items supported by a cluster based on the cluster version type. The configuration items are specified during cluster creation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNodePoolConfigurationDetails</td>
                    <td>This API is used to query the parameter list supported by a specified node pool of CCE.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNodePoolConfigurations</td>
                    <td>This API is used to query the parameters supported by a specified node pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterConfigurationDetails</td>
                    <td>This API is used to query the parameter list supported by a specified cluster of CCE.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNodePoolConfiguration</td>
                    <td>This API is used to modify the configuration parameters of a specified CCE node pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">DDM Instance Management</td>
                    <td>ShowNode</td>
                    <td>Query the DDM instance node details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Deprecated - SQL Job Related API</td>
                    <td>ListPartitions</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Instance Management</td>
                    <td>ShowCluster</td>
                    <td>Query Kafka cluster metadata.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Log Flow Chart</td>
                    <td>ListCharts</td>
                    <td>This interface is used to query log flow charts.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Mirror Cache Management</td>
                    <td>ListImageCaches</td>
                    <td>Query the image cache list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageCache</td>
                    <td>Query details about the image cache</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateImageCache</td>
                    <td>Creates an image cache. During the creation, temporary pods are started in the specified cluster to build image cache. After the image cache is created, you can use the image cache function to greatly reduce the time required for downloading container images during workload creation, implementing quick container startup. A tenant can create a maximum of 50 images in the cache.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteImageCache</td>
                    <td>Delete the image cache</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Mirror Task</td>
                    <td>ShowJob</td>
                    <td>This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Node Pool Management</td>
                    <td>UpgradeNodePool</td>
                    <td>This API is used to synchronize the configuration of existing nodes in the node pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNodePool</td>
                    <td>This API is used to create a node pool in a specified cluster. This API can be invoked only when the cluster is in the available, scaled-out, or scaled-in state.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNodePool</td>
                    <td>This API is used to obtain details about a specified node pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNodePool</td>
                    <td>This API is used to delete a specified node pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodePools</td>
                    <td>This API is used to obtain all node pools in a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNodePool</td>
                    <td>This API is used to update a specified node pool. This API can be invoked only when the cluster is in the available, scaled-out, or scaled-in state.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ScaleNodePool</td>
                    <td>This API is used to scale in a specified node pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Node change</td>
                    <td>ResizeCluster</td>
                    <td>This API is used to expand cluster capacity and add idle nodes. By default, capacity expansion is performed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Node management</td>
                    <td>UpdateNode</td>
                    <td>This API is used to update a specified node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddNodesToNodePool</td>
                    <td>This API is used to manage nodes in a custom node pool of a specified cluster. Bidding instances cannot be managed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNode</td>
                    <td>This API is used to create nodes in a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveNode</td>
                    <td>This API is used to remove a node from a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LockNodepoolNodeScaleDown</td>
                    <td>This API is used to enable scale-in protection for nodes. A node with scale-in protection enabled cannot be scaled in by changing the number of node pools.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncNode</td>
                    <td>This API is used to synchronize nodes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetNode</td>
                    <td>This API is used to reset nodes in a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNode</td>
                    <td>This API is used to delete a specified node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddNode</td>
                    <td>This API is used to manage nodes in a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSyncNodes</td>
                    <td>This API is used to synchronize nodes in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnlockNodepoolNodeScaleDown</td>
                    <td>This API is used to disable the scale-in protection function for a node. A node for which the scale-in protection function is disabled can be scaled in by modifying the number of node pools. The scale-in protection function can be disabled only for on-demand nodes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateNode</td>
                    <td>This API is used to migrate nodes from a specified cluster to another cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query the API version information about the CMK</td>
                    <td>ShowVersion</td>
                    <td>-Function description: This API is used to query the version information of a specified API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowQuotas</td>
                    <td>Query the resource quota of the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota Management (Autopilot)</td>
                    <td>ShowAutopilotQuotas</td>
                    <td>This API is used to query the resource quota of CCE.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Storage Management</td>
                    <td>CreateCloudPersistentVolumeClaims</td>
                    <td>This API is used to create a PersistentVolumeClaim (PVC) using the cloud storage (EVS, SFS, and OBS) in the cloud storage service in a specified namespace. This API is to be discarded. Use Kubernetes PVC-related APIs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCloudPersistentVolumeClaims</td>
                    <td>This API is used to delete a Persistent VolumeClaim (PVC) object in a specified namespace and retain the backend cloud storage. This API is to be discarded. Use Kubernetes PVC-related APIs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tag Management (Autopilot)</td>
                    <td>BatchDeleteAutopilotClusterTags</td>
                    <td>This API is used to delete resource tags of a specified cluster in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateAutopilotClusterTags</td>
                    <td>This API is used to add resource tags for a specified cluster in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tag management interface</td>
                    <td>BatchCreateClusterTags</td>
                    <td>Add tags to a specified cluster in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteClusterTags</td>
                    <td>This API is used to delete tags from a specified cluster in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">Template Management</td>
                    <td>ShowChartValues</td>
                    <td>Obtain Template Values</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateChart</td>
                    <td>Update Template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowChart</td>
                    <td>Obtain the template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRelease</td>
                    <td>Create a template instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRelease</td>
                    <td>Delete a specified template instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReleaseHistory</td>
                    <td>Query historical records of a specified template instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRelease</td>
                    <td>Obtain a specified template instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteChart</td>
                    <td>Delete a template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadChart</td>
                    <td>Download Template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadChart</td>
                    <td>Upload template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserChartsQuotas</td>
                    <td>Obtain the user template quota</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRelease</td>
                    <td>Updates a specified template instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReleases</td>
                    <td>Obtain the template instance list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Template management (Autopilot)</td>
                    <td>DeleteAutopilotRelease</td>
                    <td>Delete a specified template instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotReleases</td>
                    <td>Obtain the template instance list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadAutopilotChart</td>
                    <td>Upload template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadAutopilotChart</td>
                    <td>Download Template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutopilotChart</td>
                    <td>Update Template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotRelease</td>
                    <td>Create a template instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotRelease</td>
                    <td>Obtains a specified template instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotUserChartsQuotas</td>
                    <td>Obtain the user template quota</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotReleaseHistory</td>
                    <td>Query historical records of a specified template instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAutopilotChart</td>
                    <td>Delete a template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotChartValues</td>
                    <td>Obtain Template Values</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutopilotRelease</td>
                    <td>Updates a specified template instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotCharts</td>
                    <td>Obtain the template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotChart</td>
                    <td>Obtain the template</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
