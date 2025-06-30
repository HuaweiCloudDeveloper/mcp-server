# DLF MCP Server 


## Version
v0.1.0

## Overview

DLF MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DLF. Full-chain management of DLF resources can be carried out based on natural language.

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
                    <td rowspan="1">APIs related to the directory tree</td>
                    <td>ShowDirectoryTree</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Connection-related APIs</td>
                    <td>ExportConnections</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportConnections</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnction</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConnection</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Destination Connection Management</td>
                    <td>CreateConnection</td>
                    <td>Create the target connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConnection</td>
                    <td>Update the target connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConnections</td>
                    <td>Query the list of target connections.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Instance Management</td>
                    <td>CreateJob</td>
                    <td>You can create a single task, such as live migration, real-time synchronization, and real-time DR based on the request parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateJob</td>
                    <td>This API is used to update details about a task with a specified ID of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job management</td>
                    <td>ShowJobStatus</td>
                    <td>Query the execution status of a job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job management interface</td>
                    <td>StopJob</td>
                    <td>This API is used to terminate a specified job in the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Job-related API</td>
                    <td>ListSystemTasks</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunOnce</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreJobInstance</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopJobInstance</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFileInfo</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportJobList</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobInstance</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobInstances</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Mirror Task</td>
                    <td>ShowJob</td>
                    <td>This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Resource</td>
                    <td>ListResources</td>
                    <td>Returns resources of a specific resource type under the current tenant. The current user must have the rms:resources:list permission. For example, if the ECS is queried, the resource type corresponding to the RMS resource type is ecs.cloudservers, where the provider is ecs and the type is cloudservers. For the types of services and resources supported by the RMS, see [Supported Services and Areas] (https://console.huaweicloud.com/eps/#/resources/supported).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Resource-related APIs</td>
                    <td>UpdateResource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Script-related API</td>
                    <td>ListScripts</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScriptResults</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Task Center API</td>
                    <td>ListJobs</td>
                    <td>Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Task Management</td>
                    <td>DeleteJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
