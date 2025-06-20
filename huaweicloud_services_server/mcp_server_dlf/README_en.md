# DLF MCP Server 


## Version
v0.1.0

## Overview

DLF MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DLF. Full-chain management of DLF resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| APIs related to the directory tree | ShowDirectoryTree |  | To be tested |
| Connection-related APIs | ExportConnections |  | To be tested |
|  | ImportConnections |  | To be tested |
|  | DeleteConnction |  | To be tested |
|  | ShowConnection |  | To be tested |
| Destination Connection Management | CreateConnection | Create the target connection. | To be tested |
|  | UpdateConnection | Update the target connection. | To be tested |
|  | ListConnections | Query the list of target connections. | To be tested |
| Instance Management | CreateJob | You can create a single task, such as live migration, real-time synchronization, and real-time DR based on the request parameters. | To be tested |
|  | UpdateJob | This API is used to update details about a task with a specified ID of a tenant. | To be tested |
| Job management | ShowJobStatus | Query the execution status of a job. | To be tested |
| Job management interface | StopJob | This API is used to terminate a specified job in the MRS cluster. | To be tested |
| Job-related API | ListSystemTasks |  | To be tested |
|  | ExportJob |  | To be tested |
|  | RunOnce |  | To be tested |
|  | RestoreJobInstance |  | To be tested |
|  | StopJobInstance |  | To be tested |
|  | ShowFileInfo |  | To be tested |
|  | ExportJobList |  | To be tested |
|  | ImportJob |  | To be tested |
|  | ShowJobInstance |  | To be tested |
|  | StartJob |  | To be tested |
|  | ListJobInstances |  | To be tested |
| Mirror Task | ShowJob | This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task. | To be tested |
| Resource | ListResources | Returns resources of a specific resource type under the current tenant. The current user must have the rms:resources:list permission. For example, if the ECS is queried, the resource type corresponding to the RMS resource type is ecs.cloudservers, where the provider is ecs and the type is cloudservers. For the types of services and resources supported by the RMS, see [Supported Services and Areas] (https://console.huaweicloud.com/eps/#/resources/supported). | To be tested |
| Resource-related APIs | UpdateResource |  | To be tested |
|  | CreateResource |  | To be tested |
|  | ShowResource |  | To be tested |
|  | DeleteResource |  | To be tested |
| Script-related API | ListScripts |  | To be tested |
|  | ShowScript |  | To be tested |
|  | CancelScript |  | To be tested |
|  | DeleteScript |  | To be tested |
|  | CreateScript |  | To be tested |
|  | UpdateScript |  | To be tested |
|  | ExecuteScript |  | To be tested |
|  | ListScriptResults |  | To be tested |
| Task Center API | ListJobs | Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph. | To be tested |
| Task Management | DeleteJob |  | To be tested |

