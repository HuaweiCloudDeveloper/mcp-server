# VIAS MCP Server 


## Version
v0.1.0

## Overview

VIAS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VIAS. Full-chain management of VIAS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| IAlgorithmController | ShowServiceDetail | Obtain service details | To be tested |
|  | StopDeployAlgorithm | Stopping Algorithm Deployment | To be tested |
|  | ListUserServices | My algorithm service list | To be tested |
|  | DeployAlgorithm | Deployment algorithm | To be tested |
| IBatchTaskController | CreateBatchTask | Add a batch task | To be tested |
|  | DeleteBatchTask | Delete batch configurations | To be tested |
|  | ListBatchTasks | Obtain the batch configuration task list | To be tested |
|  | BatchStartStopTask | Start or stop a batch configuration task | To be tested |
|  | UpdateBatchTask | Modifying a batch configuration task | To be tested |
| IEdgePoolController | CreateEdgePool | Create an edge resource pool | To be tested |
|  | ShowEdgePoolInfo | Query details about an edge resource pool | To be tested |
|  | DeleteEdgePool | Delete an edge resource pool. | To be tested |
|  | ListEdgePools | Query the edge resource pool list | To be tested |
| ITaskController | ShowTaskInfo | This interface is used to obtain the details of an intelligent video analysis task. | To be tested |
|  | DeleteTask | Delete a single task | To be tested |
|  | UpdateTask | Task modification interface, used to modify task configurations | To be tested |
|  | CreateTask | This interface is used to create a task. | To be tested |
|  | StartStopTask | This interface is used to start or stop a task. | To be tested |
|  | ListTasks | Obtain the task list | To be tested |
| IVideoGroupController | ShowVideoGroupDetail | Obtains video source group details. | To be tested |
|  | UpdateVideoGroup | Update the video source group | To be tested |
|  | DeleteVideoGroup | Delete a video source group | To be tested |
|  | ListVideoGroups | Obtain the video source group list | To be tested |
|  | CreateVideoGroup | Creating a video source group | To be tested |
| IVideoSourceController | CreateVideoSource | Create a video source | To be tested |
|  | ListVideoSources | Obtain the video source list. | To be tested |
|  | DeleteVideoSource | Delete a video source | To be tested |
|  | ShowVideoSourceDetail | Displays video source details. | To be tested |
|  | UpdateVideoSource | Modifying a video source | To be tested |

