# DIS MCP Server 


## Version
v0.1.0

## Overview

DIS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DIS. Full-chain management of DIS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| App Management | ListApp | This API is used to query the app list. | To be tested |
|  | ShowConsumerState | This interface is used to query the app consumption status. | To be tested |
| App Template Management | DeleteApp | Delete an application template | To be tested |
| AppManagement | ShowApp | This interface is used by users to query application details. | To be tested |
|  | CreateApp | This interface is used by users to create application information. | To be tested |
| Channel management | CreatePolicies | This API is used to add a permission policy to a specified stream. | To be tested |
|  | ShowStream | This API is used to query details about a specified stream. | To be tested |
|  | UpdatePartitionCount | This API is used to change the number of partitions in a specified stream. | To be tested |
| Checkpoint management | CommitCheckpoint | This interface is used to submit checkpoints. | To be tested |
|  | DeleteCheckpoint | This API is used to delete a checkpoint. | To be tested |
|  | ShowCheckpoint | This API is used to query checkpoint details. | To be tested |
| Data management | SendRecords | This API is used to upload data to a DIS stream. | To be tested |
|  | ConsumeRecords | This API is used to download data from the DIS stream. | To be tested |
|  | ShowCursor | This interface is used to obtain data cursors. | To be tested |
| Dump Task Management | BatchStartTransferTask | This interface is used to start dump tasks in batches. | To be tested |
|  | DeleteTransferTask | This interface is used to delete a dump task. | To be tested |
|  | ShowTransferTask | Query dump task details. | To be tested |
|  | BatchStopTransferTask | This interface is used to suspend dump tasks in batches. | To be tested |
|  | CreateDliTransferTask | This API is used to add a DLI dump task. | To be tested |
|  | CreateObsTransferTask | This API is used to add an OBS dump task. | To be tested |
|  | ListTransferTasks | This interface is used to query the dump task list. | To be tested |
|  | CreateMrsTransferTask | This interface is used to add MRS dump tasks. | To be tested |
|  | CreateCloudTableTransferTask | This API is used to add a CloudTable dump task. | To be tested |
|  | CreateDwsTransferTask | This API is used to add a DWS dump task. | To be tested |
| Host management | ListPolicies | Query the host policy list | To be tested |
| Image Tag | ListTags | Query the image tag list based on different conditions. | To be tested |
| Key Tag Management | DeleteTag | - Function description: This API is used to delete a key tag. | To be tested |
| Monitoring management | ShowPartitionMetrics | This API is used to query the monitoring data of a specified partition of a stream. | To be tested |
|  | ShowStreamMetrics | This API is used to query the monitoring data of a specified channel. | To be tested |
| Tag Management | BatchDeleteTags | This API is used to delete tags for a specified protected instance in batches. A maximum of 10 labels can be placed on a resource. | To be tested |
|  | ShowStreamTags | This API is used to query the label information of a specified channel. | To be tested |
|  | CreateTag | Add a tag to a resource. | To be tested |
|  | BatchCreateTags | Create tags in batches | To be tested |
| Tags | ListResourcesByTags | Query the resource instance list by tag | To be tested |
| Video Stream Management | ListStreams | This interface is used to obtain details about all video streams. | To be tested |
|  | CreateStream | This interface is used to create video streams. include RTMP and HTTP-FLV type video stream. | To be tested |
|  | DeleteStream | This interface is used to delete a specified video stream. | To be tested |
|  | UpdateStream | This interface is used to update details about video streams, including RTMP and HTTP-FLV video streams. | To be tested |

