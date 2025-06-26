# GES MCP Server 


## Version
v0.1.0

## Overview

GES MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GES. Full-chain management of GES resources can be carried out based on natural language.

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
                    <td rowspan="2">Backup and Restore</td>
                    <td>ShowBackupDownloadLink</td>
                    <td>Obtain the backup download link.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackups</td>
                    <td>Obtain the backup list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Backup management API</td>
                    <td>ListGraphBackups</td>
                    <td>Query the backup list of a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackup2</td>
                    <td>Delete a backup.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBackup2</td>
                    <td>Add a backup. If the current graph data is incorrect or faulty, you can start the backup graph to restore the data.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackups2</td>
                    <td>Query the backup list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBackup</td>
                    <td>Add a backup. If the current graph data is incorrect or faulty, you can start the backup graph to restore the data.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGraphBackups2</td>
                    <td>Query the backup list of a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportBackup2</td>
                    <td>Import backup</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackup</td>
                    <td>Delete a backup.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportBackup2</td>
                    <td>Export backup</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Connection management</td>
                    <td>ChangeSecurityGroup</td>
                    <td>Modify the security group bound to the SFS Turbo file system. If the security group modification task is an asynchronous task, you can determine whether to modify the security group status based on the sub_status field returned by Querying a Single File System. If the sub_status field is 232, the security group is successfully modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Federated identity authentication management</td>
                    <td>CreateMetadata</td>
                    <td>This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to import a metadata file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="29">Graph management API</td>
                    <td>ExpandGraph2</td>
                    <td>The replica capacity can be dynamically expanded to multiple slave nodes. The new slave nodes can process read requests, improving read request performance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGraph2</td>
                    <td>Delete a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportGraph2</td>
                    <td>Import graph data incrementally.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopGraph</td>
                    <td>Closes a graph. If the diagram is created, you can disable it temporarily and enable it when needed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGraph2</td>
                    <td>Create a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartGraph2</td>
                    <td>Starts a graph. You can close the diagrams that are not used temporarily and start them when you need them.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandGraph</td>
                    <td>The replica expansion capability allows you to dynamically expand the capacity of multiple slave nodes. The new slave nodes can process read requests, improving read request performance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachEip2</td>
                    <td>You can unbind an EIP to release network resources if you do not need to use it.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeGraph2</td>
                    <td>Change the image specification.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ClearGraph2</td>
                    <td>Clears all data in the graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGraphs2</td>
                    <td>Query all graphs of the current tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachEip2</td>
                    <td>You can access GES by binding an elastic public IP address (EIP for short).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGraph</td>
                    <td>Delete a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGraph</td>
                    <td>Query details about a graph based on the graph ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachEip</td>
                    <td>You can unbind an EIP to release network resources if you do not need to use it.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGraphs</td>
                    <td>Query all graphs of the current tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartGraph</td>
                    <td>Starts a graph. You can close the diagrams that are not used temporarily and start them when you need to use them.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeGraph</td>
                    <td>Upgrade diagram. GES periodically upgrades the version. You can upgrade the graph as required.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeGraph2</td>
                    <td>Upgrade diagram. GES periodically upgrades the version. You can upgrade the graph as required.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGraph2</td>
                    <td>Query details about a graph based on the graph ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopGraph2</td>
                    <td>Closes a graph. If the diagram is created, you can disable it temporarily and enable it when needed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportGraph</td>
                    <td>Import graph data incrementally.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportGraph2</td>
                    <td>Export the graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ClearGraph</td>
                    <td>Clears all data in the graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartGraph2</td>
                    <td>Forcibly start a graph. For imported, exported, running, and air-clearing charts. If the graph is forcibly restarted, the asynchronous tasks in the graph will fail, and then the graph will be stopped and started to the running state.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportGraph</td>
                    <td>Export a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGraph</td>
                    <td>Create a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeGraph</td>
                    <td>Expansion diagram specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartGraph</td>
                    <td>Forcibly start a graph. For imported, exported, running, and air-clearing charts. Forcibly restarting a graph will change the asynchronous task in the graph execution to failed, and then stop the graph and start the graph to the running state.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">GraphPlugins management API</td>
                    <td>ListScenes2</td>
                    <td>Query details about the application analysis capability in the scenes scenario to obtain details about the application, parameters, and functions in the corresponding scenario.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeregisterScenes2</td>
                    <td>Unsubscribe from the application analysis capability in the scenes scenario. After the subscription is canceled, the application service plane APIs in the corresponding scene cannot be used.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterScenes2</td>
                    <td>Subscribe to the scene application scenario analysis capability so that APIs on the service plane can use the corresponding function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Instance management</td>
                    <td>AttachEip</td>
                    <td>Associate and unbind an EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Metadata management API</td>
                    <td>DeleteMetadata2</td>
                    <td>Delete metadata.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetadata2</td>
                    <td>Query a metadata.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadFromObs2</td>
                    <td>Import metadata from OBS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMetadata</td>
                    <td>Delete metadata.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetadatas2</td>
                    <td>Query the metadata list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMetadata2</td>
                    <td>Add metadata.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetadatas</td>
                    <td>Query the metadata list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadFromObs</td>
                    <td>Import metadata from OBS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGraphMetadatas</td>
                    <td>Query the metadata of a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Mirror Task</td>
                    <td>ShowJob</td>
                    <td>This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota Management</td>
                    <td>ListQuotas</td>
                    <td>Obtain quota information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">System management API</td>
                    <td>ListQuotas2</td>
                    <td>Query the tenant quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Task Center API</td>
                    <td>ShowJob2</td>
                    <td>Query the execution status of a job. After asynchronous API commands, such as creating, closing, starting, deleting, and importing graphs, are issued, jobId is returned. You can query the execution status of the task based on jobId.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobs</td>
                    <td>Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobs2</td>
                    <td>Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
