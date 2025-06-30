# OMS MCP Server 


## Version
v0.1.0

## Overview

OMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service OMS. Full-chain management of OMS resources can be carried out based on natural language.

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
                    <td rowspan="5">Bucket operation</td>
                    <td>ShowBucketRegion</td>
                    <td>Query the region corresponding to a bucket.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBucketObjects</td>
                    <td>Query the bucket object list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBucketList</td>
                    <td>Query the bucket list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckPrefix</td>
                    <td>Check whether the prefix exists in the source bucket.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCdnInfo</td>
                    <td>Query the CDN information corresponding to the bucket.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Cloud Service</td>
                    <td>ShowCloudType</td>
                    <td>Query all supported cloud vendors</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ITaskController</td>
                    <td>DeleteTask</td>
                    <td>Delete a single task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTask</td>
                    <td>This interface is used to create a task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTasks</td>
                    <td>Obtain the task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Migration Task Group Management</td>
                    <td>StopTaskGroup</td>
                    <td>When a migration task group is being created or being monitored, this API is invoked to suspend the specified migration task group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTaskGroup</td>
                    <td>Delete a specified migration task group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskGroup</td>
                    <td>Modify the flow control policy of the migration task group before the execution of the migration task group is complete.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskGroup</td>
                    <td>Obtain the task group information with a specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryTaskGroup</td>
                    <td>When a migration task group fails to be migrated, this API is invoked to restart the migration task group with the specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartTaskGroup</td>
                    <td>When a migration task group is suspended, this API is invoked to start the migration task group with the specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTaskGroup</td>
                    <td>Create a migration task group. After the migration task group is created successfully, the migration task group automatically creates a migration task. You do not need to invoke the task startup command.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskGroup</td>
                    <td>Query the task group information under the user account</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Migration Task Management</td>
                    <td>BatchUpdateTasks</td>
                    <td>Updates migration tasks in batches. You can specify all migration tasks in a migration task group or execute the tasks by task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBandwidthPolicy</td>
                    <td>Modify the flow control policy of the migration task before the migration task is complete.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query API version information</td>
                    <td>ShowApiInfo</td>
                    <td>Query the API version of the Object Storage Migration Service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query version operation</td>
                    <td>ListApiVersions</td>
                    <td>Query the TMS API version list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Region</td>
                    <td>ShowRegionInfo</td>
                    <td>Query the reigons supported by the cloud vendor</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Service Job Management</td>
                    <td>StopTask</td>
                    <td>This interface is used to stop a service job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTask</td>
                    <td>This interface is used to query service jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartTask</td>
                    <td>This interface is used to start a service job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Synchronization Task</td>
                    <td>DeleteSyncTask</td>
                    <td>This interface is invoked to delete a synchronization task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSyncTaskStatistic</td>
                    <td>Query the number of objects that receive synchronization requests, the number of objects that are successfully synchronized, the number of objects that fail to be synchronized, the number of objects that are skipped, and the capacity of objects that are successfully synchronized in a synchronization task with a specified ID. (Currently, only CN North-Beijing 4 and CN East-Shanghai 1 are supported.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSyncTask</td>
                    <td>Create a synchronization task. After the task is created, the task is automatically started. You do not need to invoke the command for starting the task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSyncEvents</td>
                    <td>When an object needs to be synchronized at the source end, this interface is invoked to create a synchronization event. The system synchronizes the object name contained in the synchronization event. (Currently, only CN North-Beijing 4 and CN East-Shanghai 1 are supported.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopSyncTask</td>
                    <td>When a synchronization task is being synchronized, this interface is invoked to stop the task. (Currently, only CN North-Beijing 4 and CN East-Shanghai 1 are supported.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSyncTasks</td>
                    <td>Query the information about all synchronization tasks under the user name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartSyncTask</td>
                    <td>After a synchronization task is stopped, this interface is invoked to start the synchronization task. (Currently, only CN North-Beijing 4 and CN East-Shanghai 1 are supported.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSyncTask</td>
                    <td>Query the details of a synchronization task with a specified ID.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
