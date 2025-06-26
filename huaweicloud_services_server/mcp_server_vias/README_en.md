# VIAS MCP Server 


## Version
v0.1.0

## Overview

VIAS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VIAS. Full-chain management of VIAS resources can be carried out based on natural language.

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
                    <td rowspan="4">IAlgorithmController</td>
                    <td>ShowServiceDetail</td>
                    <td>Obtain service details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopDeployAlgorithm</td>
                    <td>Stopping Algorithm Deployment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserServices</td>
                    <td>My algorithm service list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeployAlgorithm</td>
                    <td>Deployment algorithm</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">IBatchTaskController</td>
                    <td>CreateBatchTask</td>
                    <td>Add a batch task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBatchTask</td>
                    <td>Delete batch configurations</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBatchTasks</td>
                    <td>Obtain the batch configuration task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartStopTask</td>
                    <td>Start or stop a batch configuration task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBatchTask</td>
                    <td>Modifying a batch configuration task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">IEdgePoolController</td>
                    <td>CreateEdgePool</td>
                    <td>Create an edge resource pool</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgePoolInfo</td>
                    <td>Query details about an edge resource pool</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgePool</td>
                    <td>Delete an edge resource pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgePools</td>
                    <td>Query the edge resource pool list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">ITaskController</td>
                    <td>ShowTaskInfo</td>
                    <td>This interface is used to obtain the details of an intelligent video analysis task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTask</td>
                    <td>Delete a single task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTask</td>
                    <td>Task modification interface, used to modify task configurations</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTask</td>
                    <td>This interface is used to create a task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartStopTask</td>
                    <td>This interface is used to start or stop a task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTasks</td>
                    <td>Obtain the task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">IVideoGroupController</td>
                    <td>ShowVideoGroupDetail</td>
                    <td>Obtains video source group details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVideoGroup</td>
                    <td>Update the video source group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVideoGroup</td>
                    <td>Delete a video source group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVideoGroups</td>
                    <td>Obtain the video source group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVideoGroup</td>
                    <td>Creating a video source group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">IVideoSourceController</td>
                    <td>CreateVideoSource</td>
                    <td>Create a video source</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVideoSources</td>
                    <td>Obtain the video source list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVideoSource</td>
                    <td>Delete a video source</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVideoSourceDetail</td>
                    <td>Displays video source details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVideoSource</td>
                    <td>Modifying a video source</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
