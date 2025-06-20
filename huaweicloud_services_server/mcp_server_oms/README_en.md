# OMS MCP Server 


## Version
v0.1.0

## Overview

OMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service OMS. Full-chain management of OMS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Bucket operation | ShowBucketRegion | Query the region corresponding to a bucket. | To be tested |
|  | ShowBucketObjects | Query the bucket object list | To be tested |
|  | ShowBucketList | Query the bucket list | To be tested |
|  | CheckPrefix | Check whether the prefix exists in the source bucket. | To be tested |
|  | ShowCdnInfo | Query the CDN information corresponding to the bucket. | To be tested |
| Cloud Service | ShowCloudType | Query all supported cloud vendors | To be tested |
| ITaskController | DeleteTask | Delete a single task | To be tested |
|  | CreateTask | This interface is used to create a task. | To be tested |
|  | ListTasks | Obtain the task list | To be tested |
| Migration Task Group Management | StopTaskGroup | When a migration task group is being created or being monitored, this API is invoked to suspend the specified migration task group. | To be tested |
|  | DeleteTaskGroup | Delete a specified migration task group. | To be tested |
|  | UpdateTaskGroup | Modify the flow control policy of the migration task group before the execution of the migration task group is complete. | To be tested |
|  | ShowTaskGroup | Obtain the task group information with a specified ID. | To be tested |
|  | RetryTaskGroup | When a migration task group fails to be migrated, this API is invoked to restart the migration task group with the specified ID. | To be tested |
|  | StartTaskGroup | When a migration task group is suspended, this API is invoked to start the migration task group with the specified ID. | To be tested |
|  | CreateTaskGroup | Create a migration task group. After the migration task group is created successfully, the migration task group automatically creates a migration task. You do not need to invoke the task startup command. | To be tested |
|  | ListTaskGroup | Query the task group information under the user account | To be tested |
| Migration Task Management | BatchUpdateTasks | Updates migration tasks in batches. You can specify all migration tasks in a migration task group or execute the tasks by task ID. | To be tested |
|  | UpdateBandwidthPolicy | Modify the flow control policy of the migration task before the migration task is complete. | To be tested |
| Query API version information | ShowApiInfo | Query the API version of the Object Storage Migration Service. | To be tested |
| Query version operation | ListApiVersions | Query the TMS API version list. | To be tested |
| Region | ShowRegionInfo | Query the reigons supported by the cloud vendor | To be tested |
| Service Job Management | StopTask | This interface is used to stop a service job. | To be tested |
|  | ShowTask | This interface is used to query service jobs. | To be tested |
|  | StartTask | This interface is used to start a service job. | To be tested |
| Synchronization Task | DeleteSyncTask | This interface is invoked to delete a synchronization task. | To be tested |
|  | ListSyncTaskStatistic | Query the number of objects that receive synchronization requests, the number of objects that are successfully synchronized, the number of objects that fail to be synchronized, the number of objects that are skipped, and the capacity of objects that are successfully synchronized in a synchronization task with a specified ID. (Currently, only CN North-Beijing 4 and CN East-Shanghai 1 are supported.) | To be tested |
|  | CreateSyncTask | Create a synchronization task. After the task is created, the task is automatically started. You do not need to invoke the command for starting the task. | To be tested |
|  | CreateSyncEvents | When an object needs to be synchronized at the source end, this interface is invoked to create a synchronization event. The system synchronizes the object name contained in the synchronization event. (Currently, only CN North-Beijing 4 and CN East-Shanghai 1 are supported.) | To be tested |
|  | StopSyncTask | When a synchronization task is being synchronized, this interface is invoked to stop the task. (Currently, only CN North-Beijing 4 and CN East-Shanghai 1 are supported.) | To be tested |
|  | ListSyncTasks | Query the information about all synchronization tasks under the user name | To be tested |
|  | StartSyncTask | After a synchronization task is stopped, this interface is invoked to start the synchronization task. (Currently, only CN North-Beijing 4 and CN East-Shanghai 1 are supported.) | To be tested |
|  | ShowSyncTask | Query the details of a synchronization task with a specified ID. | To be tested |

