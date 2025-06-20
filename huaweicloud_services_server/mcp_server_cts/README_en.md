# CTS MCP Server 


## Version
v0.1.0

## Overview

CTS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CTS. Full-chain management of CTS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Event Management | ListTraces | You can query the resource operation records recorded in the last seven days through the event list query interface. | To be tested |
| Key operation notification management | ListNotifications | Query the created key operation notification rule. | To be tested |
| Other interfaces | ListUserResources | Query the operator list of the 30-day events. | To be tested |
|  | ListOperations | Query the full operation list of a cloud service. | To be tested |
|  | CheckObsBuckets | Check whether data can be dumped to the configured OBS bucket. | To be tested |
|  | ListTraceResources | Query the resource type list of the event. | To be tested |
| Quota Management | ListQuotas | Obtain quota information | To be tested |
| Subscription management operation | DeleteNotification | This interface is used to delete a specified subscription management. | To be tested |
|  | UpdateNotification | This interface is used to modify the specified subscription management. | To be tested |
|  | CreateNotification | This API is used to create device operations under the corresponding application in a specified instance and subscribe to the operation to the specified topic. | To be tested |
| Tags | BatchCreateResourceTags | Adding tags to specified instances in batches | To be tested |
|  | BatchDeleteResourceTags | Delete tags in batches for specified instances | To be tested |
| Tracker management | CreateTracker | After CTS is enabled, the system automatically creates a tracker to associate all operations recorded in the system. Currently, a cloud account supports the creation of one management tracker and multiple data trackers in a region. | To be tested |
|  | DeleteTracker | Currently, CTS supports deleting only created data trackers. Deleting a tracker has no impact on the existing operation records. After you enable CTS again, you can still view the existing operation records. | To be tested |
|  | UpdateTracker | You can modify the configuration items of a created tracker, including OBS bucket dump, key event notification, trace dump encryption, LTS-based search for management events, trace file integrity check, and tracker start and stop status. Modifying a tracker does not affect the existing operation records. After the tracker is modified, the system immediately records the operation with the new rule. | To be tested |
|  | ListTrackers | After CTS is enabled, you can view details about the tracker on the Tracker Information page. The details include the name of the tracker, name of the OBS bucket for storing operation events, and prefix of the trace file in the OBS bucket. | To be tested |

