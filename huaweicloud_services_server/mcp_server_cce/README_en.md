# CCE MCP Server 


## Version
v0.1.0

## Overview

CCE MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CCE. Full-chain management of CCE resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Add-on management | UpdateAddonInstance | Updates the function of the plug-in instance. | To be tested |
|  | ListAddonTemplates | A plug-in template query interface, which is used to query plug-in information. | To be tested |
|  | ListAddonInstances | Obtain all installed plug-in instances in a cluster | To be tested |
|  | DeleteAddonInstance | Deletes the function of a plug-in instance. | To be tested |
|  | CreateAddonInstance | Install the plug-in instance based on the provided plug-in template. | To be tested |
|  | RollbackAddonInstance | Roll back the plug-in instance to the source version. Only the current plug-in instance version can be rolled back to the source version (status.isRollbackable is set to true). If the plug-in instance status is running, available, abnormal, upgradeFailed, or rollbackFailed, the plug-in instance can be rolled back.  | To be tested |
|  | ShowAddonInstance | Obtains the plug-in instance details. | To be tested |
| Allied management | ListNodes | Function description: Users can use this API to query the list of trusted nodes (including aggregation nodes and compute nodes) in an alliance. | To be tested |
| Autopilot | ShowAutopilotAddonInstance | Obtain the plug-in instance details. | To be tested |
|  | UpdateAutopilotAddonInstance | Updates the function of the plug-in instance. | To be tested |
|  | RollbackAutopilotAddonInstance | Roll back the plug-in instance to the source version. Only the current plug-in instance version can be rolled back to the source version (status.isRollbackable is set to true). If the plug-in instance status is running, available, abnormal, upgradeFailed, or rollbackFailed, the plug-in instance can be rolled back.  | To be tested |
|  | ListAutopilotAddonTemplates | A plug-in template query interface, used to query plug-in information. | To be tested |
|  | DeleteAutopilotAddonInstance | Deletes the function of a plug-in instance. | To be tested |
|  | CreateAutopilotAddonInstance | Install the plug-in instance based on the provided plug-in template. | To be tested |
|  | ListAutopilotAddonInstances | Obtain all installed plug-in instances in a cluster | To be tested |
| Cluster management | AwakeCluster | Cluster wakeup is used to wake up a hibernation cluster. After the cluster wakeup, the controller node resource fee will continue to be charged. | To be tested |
|  | HibernateCluster | Cluster hibernation is used to hibernate a running cluster. After the hibernation, the system does not charge the controller node resources. | To be tested |
|  | UpdateCluster | This API is used to update a specified cluster. | To be tested |
|  | RevokeKubernetesClusterCert | This API is used to revoke the user certificate of a specified cluster. | To be tested |
|  | ShowClusterConfig | Obtain the LTS configuration information reported by cluster components | To be tested |
|  | CreateKubernetesClusterCert | This API is used to obtain the certificate information of a specified cluster. | To be tested |
|  | CreatePartition | Create a partition | To be tested |
|  | UpdatePartition | Update a partition | To be tested |
|  | UpdateClusterEip | This API is used to bind or unbind the public network API server address of a cluster based on the cluster ID. | To be tested |
|  | ShowPartition | Obtain the details of a partition. | To be tested |
|  | ShowClusterEndpoints | This API is used to obtain the cluster access address based on the cluster ID, including the private IP address (VIP returned by the HA cluster) and public IP address. | To be tested |
|  | UpdateClusterLogConfig | Users can select the components whose logs are reported to LTS on the cluster management node. | To be tested |
| Cluster management (Autopilot) | ListAutopilotClusters | This API is used to obtain details about all clusters in a specified project. | To be tested |
|  | CreateAutopilotCluster | This API is used to create an empty cluster. (That is, only the master control node is configured. | To be tested |
|  | CreateAutopilotKubernetesClusterCert | This API is used to obtain the certificate information of a specified cluster. | To be tested |
|  | ShowAutopilotClusterEndpoints | This API is used to obtain the cluster access address based on the cluster ID, including the private IP address (VIP returned by the HA cluster) and public IP address. | To be tested |
|  | DeleteAutopilotCluster | This API is used to delete a specified cluster. | To be tested |
|  | UpdateAutopilotClusterEip | This API is used to bind or unbind the public network API server address of a cluster based on the cluster ID. | To be tested |
|  | ShowAutopilotCluster | This API is used to obtain details about a specified cluster. | To be tested |
|  | UpdateAutopilotCluster | This API is used to update a specified cluster. | To be tested |
|  | ShowAutopilotJob | This API is used to obtain task information. This API is used to query the progress of a specified task based on the job ID returned after a task request is delivered. | To be tested |
| Cluster management interface | ListClusters | View the cluster list created by the user. This interface is not compatible with Sahara. | To be tested |
|  | CreateCluster | Create an MRS cluster and submit a job in the cluster. This interface is not compatible with Sahara. | To be tested |
|  | DeleteCluster | You can delete the cluster service after data processing and analysis are complete or the cluster is running abnormally and cannot provide services. This interface is compatible with Sahara. | To be tested |
| Cluster upgrade | ContinueUpgradeClusterTask | Continue the suspended cluster upgrade task. | To be tested |
|  | UpgradeWorkFlowUpdate | This API is used to update the status of a specified cluster upgrade boot task. Currently, this API is used only to cancel the upgrade process. | To be tested |
|  | CreateClusterMasterSnapshot | Cluster backup | To be tested |
|  | ListUpgradeClusterTasks | Obtain the cluster upgrade task details list | To be tested |
|  | CreatePostCheck | Confirm the cluster after the upgrade. It is recommended that this interface be used together with the console. This interface is used to provide feedback after the upgrade is complete and the customer confirms the cluster status and services are normal. | To be tested |
|  | ShowClusterUpgradeInfo | Obtain cluster upgrade information | To be tested |
|  | CreateUpgradeWorkFlow | This API is used to create a cluster upgrade process guidance task. After the boot task is created by calling this API, perform the cluster pre-upgrade check to start the task. | To be tested |
|  | ListClusterUpgradeFeatureGates | Obtain the cluster upgrade feature switch configuration. | To be tested |
|  | PauseUpgradeClusterTask | Suspend the cluster upgrade task. | To be tested |
|  | ShowPreCheck | Obtain the details about the cluster pre-upgrade check task. The task ID is obtained from the uid field in the response body after the cluster check API is invoked. | To be tested |
|  | ShowUpgradeWorkFlow | This API is used to obtain the details about an upgrade boot task based on the upgrade boot task ID. | To be tested |
|  | UpgradeCluster | Upgrade the cluster. | To be tested |
|  | ShowUpgradeClusterTask | Obtain the cluster upgrade task details. The task ID is obtained from the uid field in the response body after the cluster upgrade API is invoked. | To be tested |
|  | ListClusterMasterSnapshotTasks | Obtain the cluster backup task details list | To be tested |
|  | CreatePreCheck | Cluster pre-upgrade check | To be tested |
|  | RetryUpgradeClusterTask | Reexecute the failed cluster upgrade task. | To be tested |
|  | ListClusterUpgradePaths | Obtain the cluster upgrade path | To be tested |
|  | ListPreCheckTasks | Obtain the cluster pre-upgrade check task details list | To be tested |
|  | ListUpgradeWorkFlows | Obtain the historical cluster upgrade boot task list | To be tested |
| Cluster upgrade (Autopilot) | UpdateAutopilotMaintenanceWindow | This API is used to update the cluster maintenance window. | To be tested |
|  | ListAutopilotPreCheckTasks | Obtain the cluster pre-upgrade check task details list | To be tested |
|  | ShowAutopilotMaintenanceWindow | This API is used to obtain the cluster maintenance window. | To be tested |
|  | ListAutopilotClusterMasterSnapshotTasks | Obtain the cluster backup task details list | To be tested |
|  | CreateAutopilotPreCheck | Cluster pre-upgrade check | To be tested |
|  | ListAutopilotClusterUpgradePaths | Obtain the cluster upgrade path | To be tested |
|  | ListAutopilotUpgradeClusterTasks | Obtain the cluster upgrade task details list | To be tested |
|  | ShowAutopilotUpgradeClusterTask | Obtain the cluster upgrade task details. The task ID is obtained from the uid field in the response body after the cluster upgrade API is invoked. | To be tested |
|  | RetryAutopilotUpgradeClusterTask | Reexecute the failed cluster upgrade task. | To be tested |
|  | CreateAutopilotPostCheck | Confirm the cluster upgrade. It is recommended that this interface be used with the console to provide feedback after the upgrade is complete and the customer confirms the cluster status and services are normal. | To be tested |
|  | CreateAutopilotMaintenanceWindow | This API is used to create a cluster maintenance window. | To be tested |
|  | CreateAutopilotClusterMasterSnapshot | Cluster backup | To be tested |
|  | ListAutopilotUpgradePlans | This API is used to obtain the automatic cluster upgrade plan. | To be tested |
|  | UpgradeAutopilotWorkFlowUpdate | This API is used to update the status of a specified cluster upgrade boot task. Currently, this API is used only to cancel the upgrade process. | To be tested |
|  | CreateAutopilotUpgradeWorkFlow | This API is used to create a cluster upgrade process guidance task. After the boot task is created by calling this API, perform the cluster pre-upgrade check to start the task. | To be tested |
|  | ListAutopilotClusterUpgradeFeatureGates | Obtain the cluster upgrade feature switch configuration. | To be tested |
|  | ShowAutopilotUpgradeWorkFlow | This API is used to obtain the details about an upgrade boot task based on the upgrade boot task ID. | To be tested |
|  | UpdateAutopilotUpgradePlan | This API is used to extend the automatic cluster upgrade plan. | To be tested |
|  | ShowAutopilotClusterUpgradeInfo | Obtain the cluster upgrade information. | To be tested |
|  | ListAutopilotUpgradeWorkFlows | Obtain the historical cluster upgrade boot task list | To be tested |
|  | UpgradeAutopilotCluster | Upgrade the cluster. | To be tested |
|  | DeleteAutopilotMaintenanceWindow | This API is used to delete the cluster maintenance window. | To be tested |
|  | ShowAutopilotPreCheck | Obtain the details about the cluster pre-upgrade check task. The task ID is obtained from the uid field in the response body after the cluster check API is invoked. | To be tested |
| Configuration Management | ShowClusterSupportConfiguration | This API is used to query detailed configuration items supported by a cluster based on the cluster version type. The configuration items are specified during cluster creation. | To be tested |
|  | ShowNodePoolConfigurationDetails | This API is used to query the parameter list supported by a specified node pool of CCE. | To be tested |
|  | ShowNodePoolConfigurations | This API is used to query the parameters supported by a specified node pool. | To be tested |
|  | ShowClusterConfigurationDetails | This API is used to query the parameter list supported by a specified cluster of CCE. | To be tested |
|  | UpdateNodePoolConfiguration | This API is used to modify the configuration parameters of a specified CCE node pool. | To be tested |
| DDM Instance Management | ShowNode | Query the DDM instance node details. | To be tested |
| Deprecated - SQL Job Related API | ListPartitions |  | To be tested |
| Instance Management | ShowCluster | Query Kafka cluster metadata. | To be tested |
| Log Flow Chart | ListCharts | This interface is used to query log flow charts. | To be tested |
| Mirror Cache Management | ListImageCaches | Query the image cache list | To be tested |
|  | ShowImageCache | Query details about the image cache | To be tested |
|  | CreateImageCache | Creates an image cache. During the creation, temporary pods are started in the specified cluster to build image cache. After the image cache is created, you can use the image cache function to greatly reduce the time required for downloading container images during workload creation, implementing quick container startup. A tenant can create a maximum of 50 images in the cache. | To be tested |
|  | DeleteImageCache | Delete the image cache | To be tested |
| Mirror Task | ShowJob | This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task. | To be tested |
| Node Pool Management | UpgradeNodePool | This API is used to synchronize the configuration of existing nodes in the node pool. | To be tested |
|  | CreateNodePool | This API is used to create a node pool in a specified cluster. This API can be invoked only when the cluster is in the available, scaled-out, or scaled-in state. | To be tested |
|  | ShowNodePool | This API is used to obtain details about a specified node pool. | To be tested |
|  | DeleteNodePool | This API is used to delete a specified node pool. | To be tested |
|  | ListNodePools | This API is used to obtain all node pools in a cluster. | To be tested |
|  | UpdateNodePool | This API is used to update a specified node pool. This API can be invoked only when the cluster is in the available, scaled-out, or scaled-in state. | To be tested |
|  | ScaleNodePool | This API is used to scale in a specified node pool. | To be tested |
| Node change | ResizeCluster | This API is used to expand cluster capacity and add idle nodes. By default, capacity expansion is performed. | To be tested |
| Node management | UpdateNode | This API is used to update a specified node. | To be tested |
|  | AddNodesToNodePool | This API is used to manage nodes in a custom node pool of a specified cluster. Bidding instances cannot be managed. | To be tested |
|  | CreateNode | This API is used to create nodes in a specified cluster. | To be tested |
|  | RemoveNode | This API is used to remove a node from a specified cluster. | To be tested |
|  | LockNodepoolNodeScaleDown | This API is used to enable scale-in protection for nodes. A node with scale-in protection enabled cannot be scaled in by changing the number of node pools. | To be tested |
|  | SyncNode | This API is used to synchronize nodes. | To be tested |
|  | ResetNode | This API is used to reset nodes in a specified cluster. | To be tested |
|  | DeleteNode | This API is used to delete a specified node. | To be tested |
|  | AddNode | This API is used to manage nodes in a specified cluster. | To be tested |
|  | BatchSyncNodes | This API is used to synchronize nodes in batches. | To be tested |
|  | UnlockNodepoolNodeScaleDown | This API is used to disable the scale-in protection function for a node. A node for which the scale-in protection function is disabled can be scaled in by modifying the number of node pools. The scale-in protection function can be disabled only for on-demand nodes. | To be tested |
|  | MigrateNode | This API is used to migrate nodes from a specified cluster to another cluster. | To be tested |
| Query the API version information about the CMK | ShowVersion | -Function description: This API is used to query the version information of a specified API. | To be tested |
| Quota | ShowQuotas | Query the resource quota of the current project. | To be tested |
| Quota Management (Autopilot) | ShowAutopilotQuotas | This API is used to query the resource quota of CCE. | To be tested |
| Storage Management | CreateCloudPersistentVolumeClaims | This API is used to create a PersistentVolumeClaim (PVC) using the cloud storage (EVS, SFS, and OBS) in the cloud storage service in a specified namespace. This API is to be discarded. Use Kubernetes PVC-related APIs. | To be tested |
|  | DeleteCloudPersistentVolumeClaims | This API is used to delete a Persistent VolumeClaim (PVC) object in a specified namespace and retain the backend cloud storage. This API is to be discarded. Use Kubernetes PVC-related APIs. | To be tested |
| Tag Management (Autopilot) | BatchDeleteAutopilotClusterTags | This API is used to delete resource tags of a specified cluster in batches. | To be tested |
|  | BatchCreateAutopilotClusterTags | This API is used to add resource tags for a specified cluster in batches. | To be tested |
| Tag management interface | BatchCreateClusterTags | Add tags to a specified cluster in batches. | To be tested |
|  | BatchDeleteClusterTags | This API is used to delete tags from a specified cluster in batches. | To be tested |
| Template Management | ShowChartValues | Obtain Template Values | To be tested |
|  | UpdateChart | Update Template | To be tested |
|  | ShowChart | Obtain the template | To be tested |
|  | CreateRelease | Create a template instance | To be tested |
|  | DeleteRelease | Delete a specified template instance | To be tested |
|  | ShowReleaseHistory | Query historical records of a specified template instance | To be tested |
|  | ShowRelease | Obtain a specified template instance | To be tested |
|  | DeleteChart | Delete a template | To be tested |
|  | DownloadChart | Download Template | To be tested |
|  | UploadChart | Upload template | To be tested |
|  | ShowUserChartsQuotas | Obtain the user template quota | To be tested |
|  | UpdateRelease | Updates a specified template instance | To be tested |
|  | ListReleases | Obtain the template instance list | To be tested |
| Template management (Autopilot) | DeleteAutopilotRelease | Delete a specified template instance | To be tested |
|  | ListAutopilotReleases | Obtain the template instance list | To be tested |
|  | UploadAutopilotChart | Upload template | To be tested |
|  | DownloadAutopilotChart | Download Template | To be tested |
|  | UpdateAutopilotChart | Update Template | To be tested |
|  | CreateAutopilotRelease | Create a template instance | To be tested |
|  | ShowAutopilotRelease | Obtains a specified template instance | To be tested |
|  | ShowAutopilotUserChartsQuotas | Obtain the user template quota | To be tested |
|  | ShowAutopilotReleaseHistory | Query historical records of a specified template instance | To be tested |
|  | DeleteAutopilotChart | Delete a template | To be tested |
|  | ShowAutopilotChartValues | Obtain Template Values | To be tested |
|  | UpdateAutopilotRelease | Updates a specified template instance | To be tested |
|  | ListAutopilotCharts | Obtain the template list | To be tested |
|  | ShowAutopilotChart | Obtain the template | To be tested |

