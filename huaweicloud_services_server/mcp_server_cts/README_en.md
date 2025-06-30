# CTS MCP Server 


## Version
v0.1.0

## Overview

CTS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CTS. Full-chain management of CTS resources can be carried out based on natural language.

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
                    <td rowspan="1">Event Management</td>
                    <td>ListTraces</td>
                    <td>You can query the resource operation records recorded in the last seven days through the event list query interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Key operation notification management</td>
                    <td>ListNotifications</td>
                    <td>Query the created key operation notification rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Other interfaces</td>
                    <td>ListUserResources</td>
                    <td>Query the operator list of the 30-day events.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOperations</td>
                    <td>Query the full operation list of a cloud service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckObsBuckets</td>
                    <td>Check whether data can be dumped to the configured OBS bucket.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTraceResources</td>
                    <td>Query the resource type list of the event.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota Management</td>
                    <td>ListQuotas</td>
                    <td>Obtain quota information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Subscription management operation</td>
                    <td>DeleteNotification</td>
                    <td>This interface is used to delete a specified subscription management.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNotification</td>
                    <td>This interface is used to modify the specified subscription management.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNotification</td>
                    <td>This API is used to create device operations under the corresponding application in a specified instance and subscribe to the operation to the specified topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tags</td>
                    <td>BatchCreateResourceTags</td>
                    <td>Adding tags to specified instances in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteResourceTags</td>
                    <td>Delete tags in batches for specified instances</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Tracker management</td>
                    <td>CreateTracker</td>
                    <td>After CTS is enabled, the system automatically creates a tracker to associate all operations recorded in the system. Currently, a cloud account supports the creation of one management tracker and multiple data trackers in a region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTracker</td>
                    <td>Currently, CTS supports deleting only created data trackers. Deleting a tracker has no impact on the existing operation records. After you enable CTS again, you can still view the existing operation records.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTracker</td>
                    <td>You can modify the configuration items of a created tracker, including OBS bucket dump, key event notification, trace dump encryption, LTS-based search for management events, trace file integrity check, and tracker start and stop status. Modifying a tracker does not affect the existing operation records. After the tracker is modified, the system immediately records the operation with the new rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTrackers</td>
                    <td>After CTS is enabled, you can view details about the tracker on the Tracker Information page. The details include the name of the tracker, name of the OBS bucket for storing operation events, and prefix of the trace file in the OBS bucket.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
