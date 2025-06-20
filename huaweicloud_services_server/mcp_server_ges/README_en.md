# GES MCP Server 


## Version
v0.1.0

## Overview

GES MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GES. Full-chain management of GES resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Backup and Restore | ShowBackupDownloadLink | Obtain the backup download link. | To be tested |
|  | ListBackups | Obtain the backup list. | To be tested |
| Backup management API | ListGraphBackups | Query the backup list of a graph. | To be tested |
|  | DeleteBackup2 | Delete a backup. | To be tested |
|  | CreateBackup2 | Add a backup. If the current graph data is incorrect or faulty, you can start the backup graph to restore the data. | To be tested |
|  | ListBackups2 | Query the backup list. | To be tested |
|  | CreateBackup | Add a backup. If the current graph data is incorrect or faulty, you can start the backup graph to restore the data. | To be tested |
|  | ListGraphBackups2 | Query the backup list of a graph. | To be tested |
|  | ImportBackup2 | Import backup | To be tested |
|  | DeleteBackup | Delete a backup. | To be tested |
|  | ExportBackup2 | Export backup | To be tested |
| Connection management | ChangeSecurityGroup | Modify the security group bound to the SFS Turbo file system. If the security group modification task is an asynchronous task, you can determine whether to modify the security group status based on the sub_status field returned by Querying a Single File System. If the sub_status field is 232, the security group is successfully modified. | To be tested |
| Federated identity authentication management | CreateMetadata | This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to import a metadata file. | To be tested |
| Graph management API | ExpandGraph2 | The replica capacity can be dynamically expanded to multiple slave nodes. The new slave nodes can process read requests, improving read request performance. | To be tested |
|  | DeleteGraph2 | Delete a graph. | To be tested |
|  | ImportGraph2 | Import graph data incrementally. | To be tested |
|  | StopGraph | Closes a graph. If the diagram is created, you can disable it temporarily and enable it when needed. | To be tested |
|  | CreateGraph2 | Create a graph. | To be tested |
|  | StartGraph2 | Starts a graph. You can close the diagrams that are not used temporarily and start them when you need them. | To be tested |
|  | ExpandGraph | The replica expansion capability allows you to dynamically expand the capacity of multiple slave nodes. The new slave nodes can process read requests, improving read request performance. | To be tested |
|  | DetachEip2 | You can unbind an EIP to release network resources if you do not need to use it. | To be tested |
|  | ResizeGraph2 | Change the image specification. | To be tested |
|  | ClearGraph2 | Clears all data in the graph. | To be tested |
|  | ListGraphs2 | Query all graphs of the current tenant. | To be tested |
|  | AttachEip2 | You can access GES by binding an elastic public IP address (EIP for short). | To be tested |
|  | DeleteGraph | Delete a graph. | To be tested |
|  | ShowGraph | Query details about a graph based on the graph ID. | To be tested |
|  | DetachEip | You can unbind an EIP to release network resources if you do not need to use it. | To be tested |
|  | ListGraphs | Query all graphs of the current tenant. | To be tested |
|  | StartGraph | Starts a graph. You can close the diagrams that are not used temporarily and start them when you need to use them. | To be tested |
|  | UpgradeGraph | Upgrade diagram. GES periodically upgrades the version. You can upgrade the graph as required. | To be tested |
|  | UpgradeGraph2 | Upgrade diagram. GES periodically upgrades the version. You can upgrade the graph as required. | To be tested |
|  | ShowGraph2 | Query details about a graph based on the graph ID. | To be tested |
|  | StopGraph2 | Closes a graph. If the diagram is created, you can disable it temporarily and enable it when needed. | To be tested |
|  | ImportGraph | Import graph data incrementally. | To be tested |
|  | ExportGraph2 | Export the graph. | To be tested |
|  | ClearGraph | Clears all data in the graph. | To be tested |
|  | RestartGraph2 | Forcibly start a graph. For imported, exported, running, and air-clearing charts. If the graph is forcibly restarted, the asynchronous tasks in the graph will fail, and then the graph will be stopped and started to the running state. | To be tested |
|  | ExportGraph | Export a graph. | To be tested |
|  | CreateGraph | Create a graph. | To be tested |
|  | ResizeGraph | Expansion diagram specifications. | To be tested |
|  | RestartGraph | Forcibly start a graph. For imported, exported, running, and air-clearing charts. Forcibly restarting a graph will change the asynchronous task in the graph execution to failed, and then stop the graph and start the graph to the running state. | To be tested |
| GraphPlugins management API | ListScenes2 | Query details about the application analysis capability in the scenes scenario to obtain details about the application, parameters, and functions in the corresponding scenario. | To be tested |
|  | DeregisterScenes2 | Unsubscribe from the application analysis capability in the scenes scenario. After the subscription is canceled, the application service plane APIs in the corresponding scene cannot be used. | To be tested |
|  | RegisterScenes2 | Subscribe to the scene application scenario analysis capability so that APIs on the service plane can use the corresponding function. | To be tested |
| Instance management | AttachEip | Associate and unbind an EIP. | To be tested |
| Metadata management API | DeleteMetadata2 | Delete metadata. | To be tested |
|  | ShowMetadata2 | Query a metadata. | To be tested |
|  | UploadFromObs2 | Import metadata from OBS. | To be tested |
|  | DeleteMetadata | Delete metadata. | To be tested |
|  | ListMetadatas2 | Query the metadata list. | To be tested |
|  | CreateMetadata2 | Add metadata. | To be tested |
|  | ListMetadatas | Query the metadata list. | To be tested |
|  | UploadFromObs | Import metadata from OBS. | To be tested |
|  | ListGraphMetadatas | Query the metadata of a graph. | To be tested |
| Mirror Task | ShowJob | This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task. | To be tested |
| Quota Management | ListQuotas | Obtain quota information | To be tested |
| System management API | ListQuotas2 | Query the tenant quota. | To be tested |
| Task Center API | ShowJob2 | Query the execution status of a job. After asynchronous API commands, such as creating, closing, starting, deleting, and importing graphs, are issued, jobId is returned. You can query the execution status of the task based on jobId. | To be tested |
|  | ListJobs | Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph. | To be tested |
|  | ListJobs2 | Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph. | To be tested |

