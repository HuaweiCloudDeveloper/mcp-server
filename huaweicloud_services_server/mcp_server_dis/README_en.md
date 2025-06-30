# DIS MCP Server 


## Version
v0.1.0

## Overview

DIS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DIS. Full-chain management of DIS resources can be carried out based on natural language.

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
                    <td rowspan="2">App Management</td>
                    <td>ListApp</td>
                    <td>This API is used to query the app list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConsumerState</td>
                    <td>This interface is used to query the app consumption status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">App Template Management</td>
                    <td>DeleteApp</td>
                    <td>Delete an application template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">AppManagement</td>
                    <td>ShowApp</td>
                    <td>This interface is used by users to query application details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApp</td>
                    <td>This interface is used by users to create application information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Channel management</td>
                    <td>CreatePolicies</td>
                    <td>This API is used to add a permission policy to a specified stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStream</td>
                    <td>This API is used to query details about a specified stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePartitionCount</td>
                    <td>This API is used to change the number of partitions in a specified stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Checkpoint management</td>
                    <td>CommitCheckpoint</td>
                    <td>This interface is used to submit checkpoints.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCheckpoint</td>
                    <td>This API is used to delete a checkpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCheckpoint</td>
                    <td>This API is used to query checkpoint details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Data management</td>
                    <td>SendRecords</td>
                    <td>This API is used to upload data to a DIS stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConsumeRecords</td>
                    <td>This API is used to download data from the DIS stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCursor</td>
                    <td>This interface is used to obtain data cursors.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Dump Task Management</td>
                    <td>BatchStartTransferTask</td>
                    <td>This interface is used to start dump tasks in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTransferTask</td>
                    <td>This interface is used to delete a dump task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTransferTask</td>
                    <td>Query dump task details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopTransferTask</td>
                    <td>This interface is used to suspend dump tasks in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDliTransferTask</td>
                    <td>This API is used to add a DLI dump task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateObsTransferTask</td>
                    <td>This API is used to add an OBS dump task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTransferTasks</td>
                    <td>This interface is used to query the dump task list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMrsTransferTask</td>
                    <td>This interface is used to add MRS dump tasks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCloudTableTransferTask</td>
                    <td>This API is used to add a CloudTable dump task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDwsTransferTask</td>
                    <td>This API is used to add a DWS dump task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Host management</td>
                    <td>ListPolicies</td>
                    <td>Query the host policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Image Tag</td>
                    <td>ListTags</td>
                    <td>Query the image tag list based on different conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Key Tag Management</td>
                    <td>DeleteTag</td>
                    <td>- Function description: This API is used to delete a key tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Monitoring management</td>
                    <td>ShowPartitionMetrics</td>
                    <td>This API is used to query the monitoring data of a specified partition of a stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStreamMetrics</td>
                    <td>This API is used to query the monitoring data of a specified channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Tag Management</td>
                    <td>BatchDeleteTags</td>
                    <td>This API is used to delete tags for a specified protected instance in batches. A maximum of 10 labels can be placed on a resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStreamTags</td>
                    <td>This API is used to query the label information of a specified channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTag</td>
                    <td>Add a tag to a resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateTags</td>
                    <td>Create tags in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListResourcesByTags</td>
                    <td>Query the resource instance list by tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Video Stream Management</td>
                    <td>ListStreams</td>
                    <td>This interface is used to obtain details about all video streams.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStream</td>
                    <td>This interface is used to create video streams. include RTMP and HTTP-FLV type video stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStream</td>
                    <td>This interface is used to delete a specified video stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStream</td>
                    <td>This interface is used to update details about video streams, including RTMP and HTTP-FLV video streams.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
