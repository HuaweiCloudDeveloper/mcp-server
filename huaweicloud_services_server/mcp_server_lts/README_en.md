# LTS MCP Server 


## Version
v0.1.0

## Overview

LTS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service LTS. Full-chain management of LTS resources can be carried out based on natural language.

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
                    <td rowspan="5">AOM container logs are connected to LTS</td>
                    <td>DeleteAomMappingRules</td>
                    <td>This API is used to delete an lts access rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAomMappingRules</td>
                    <td>This interface is used to query all access LTS rules for AOM logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAomMappingRules</td>
                    <td>This interface is used to create an AOM log access LTS rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAomMappingRule</td>
                    <td>This interface is used to query a single AOM log. lts</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAomMappingRules</td>
                    <td>This interface is used to modify an access rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Alarm List</td>
                    <td>DeleteActiveAlarms</td>
                    <td>This interface is used to delete active alarms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListActiveOrHistoryAlarms</td>
                    <td>This interface is used to query the alarm list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Alarm Subject</td>
                    <td>ListNotificationTopics</td>
                    <td>This API is used to query SMN topics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Consumer group management</td>
                    <td>DeleteConsumerGroup</td>
                    <td>Delete a consumer group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Dashboard Management</td>
                    <td>CreateDashboardGroup</td>
                    <td>Creating a Dashboard Group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDashBoard</td>
                    <td>Create a dashboard</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDashboard</td>
                    <td>Delete a dashboard</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Host group management</td>
                    <td>UpdateHostGroup</td>
                    <td>Modifying a host group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostGroup</td>
                    <td>Query the host group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHostGroup</td>
                    <td>Delete a host group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHostGroup</td>
                    <td>Create a host group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Keyword alarm rule</td>
                    <td>UpdateKeywordsAlarmRule</td>
                    <td>This interface is used to modify keyword alarms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKeywordsAlarmRule</td>
                    <td>This interface is used to delete keyword alarms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKeywordsAlarmRule</td>
                    <td>This API is used to create keyword alarms. Currently, a maximum of 200 keyword alarms and SQL alarms can be created for each account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeywordsAlarmRules</td>
                    <td>This interface is used to query keyword alarms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Log Dump</td>
                    <td>UpdateTransfer</td>
                    <td>This API is used to update OBS, DIS, and DMS dumping.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterDmsKafkaInstance</td>
                    <td>This API is used to register a DMS Kafka instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogDumpObs</td>
                    <td>This API is used to dump logs of one or more specified log streams to OBS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTransfers</td>
                    <td>This API is used to query OBS, DIS, and DMS dump configurations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTransfer</td>
                    <td>This API is used to create OBS, DIS, or DMS dumping.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTransfer</td>
                    <td>This API is used to delete OBS, DIS, and DMS dumping.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Log Flow Chart</td>
                    <td>ListCharts</td>
                    <td>This interface is used to query log flow charts.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Log Group Management</td>
                    <td>ListLogGroups</td>
                    <td>This interface is used to query all log groups under an account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogGroup</td>
                    <td>This API is used to delete a specified log group. If log dumping is configured for a log stream in a log group, you need to cancel the log dumping before deleting the log stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogGroup</td>
                    <td>This interface is used to create a log group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogGroup</td>
                    <td>This API is used to modify the log retention duration of a specified log group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Log Stream Management</td>
                    <td>UpdateLogStream</td>
                    <td>This interface is used to modify the log storage duration in a specified log flow.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogStream</td>
                    <td>This API is used to query all log streams in a specified log group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogStreams</td>
                    <td>This interface is used to query LTS log flow information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogStream</td>
                    <td>This interface is used to create a log stream in a specified log group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogStream</td>
                    <td>This interface is used to delete a specified log stream from a specified log group. If log dumping is configured for the log stream, you need to cancel the log dumping before deleting it.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogStreamIndex</td>
                    <td>Creates an index for a specified flow.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Log access</td>
                    <td>DeleteAccessConfig</td>
                    <td>Delete log access</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAccessConfig</td>
                    <td>Modify log access</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgencyAccess</td>
                    <td>New Cross-Account Log Access</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccessConfig</td>
                    <td>Query the log access list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAccessConfig</td>
                    <td>Create log access</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Log management</td>
                    <td>ListLogContext</td>
                    <td>Querying Context Logs This interface is used to query the logs before and after specified logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStructuredLogsWithTimeRange</td>
                    <td>This API is used to query the structured log content in a specified log flow (new version).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogHistogram</td>
                    <td>Query the number of keyword search records</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopnTrafficStatistics</td>
                    <td>Count the traffic of top N log groups or log streams</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Deletefavorite</td>
                    <td>Cancel favorites</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTimeLineTrafficStatistics</td>
                    <td>Querying resources by time segment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Createfavorite</td>
                    <td>Create log collection</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogs</td>
                    <td>This interface is used to query logs in a specified log stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryStructuredLogs</td>
                    <td>This API is used to query structured logs in a specified log flow.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Message Template Management</td>
                    <td>UpdateNotificationTemplate</td>
                    <td>This interface is used to modify a notification template by name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNotificationTemplate</td>
                    <td>This interface is used to query a notification template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNotificationTemplate</td>
                    <td>This interface is used to delete a notification template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotificationTemplate</td>
                    <td>This interface is used to preview the email format of the notification template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotificationTemplates</td>
                    <td>This interface is used to query notification templates.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNotificationTemplate</td>
                    <td>This interface is used to create notification templates. Currently, each account can create a maximum of 100 notification templates. The name of the created notification templates cannot be changed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Multi-account log aggregation</td>
                    <td>UpdateLogConvergeConfig</td>
                    <td>Only the administrator or delegated administrator can update the aggregation configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLogConvergeConfig</td>
                    <td>Only the organization administrator or agency administrator invokes this interface to obtain the organization member aggregation configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAdminConfig</td>
                    <td>Only administrators or delegated administrators can invoke this interface to obtain the log aggregation switch.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSwitch</td>
                    <td>Only the administrator or delegated administrator can invoke the interface to modify the log aggregation switch.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMemberGroupAndStream</td>
                    <td>This interface can be invoked only by the administrator or delegated administrator to obtain the log streams of the organization member log group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Overcollected</td>
                    <td>EnableLogCollection</td>
                    <td>This interface is used to enable the over-collecting log function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableLogCollection</td>
                    <td>This interface is used to disable the log collection function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Protection Website Management in Cloud Mode</td>
                    <td>ListHost</td>
                    <td>Query the domain name list in cloud mode</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Quick query</td>
                    <td>CreateSearchCriterias</td>
                    <td>Adding a quick query</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryAllSearchCriterias</td>
                    <td>Query all quick queries in a log group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCriterias</td>
                    <td>Quick query</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHistorySql</td>
                    <td>SQL for querying user history</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSearchCriterias</td>
                    <td>Delete a quick query</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">SDK Streaming Consumption Open API</td>
                    <td>ListDetailsConsumerGroup</td>
                    <td>Query consumer group details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCursorByTime</td>
                    <td>Query the cursor by time</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCheckPoint</td>
                    <td>Update consumer group location</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConsumerGroup</td>
                    <td>Create consumer group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConsumerGroupHeartBeat</td>
                    <td>The consumer sends a heartbeat message to the server.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCursorTime</td>
                    <td>Query the server time using the cursor</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConsumerGroup</td>
                    <td>Query the consumer group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLogStreamShards</td>
                    <td>Obtains all query shards for stream consumption</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">SQL alarm rule</td>
                    <td>UpdateAlarmRuleStatus</td>
                    <td>Change the alarm rule status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlAlarmRule</td>
                    <td>This interface is used to create SQL alarms. Currently, each account can create a maximum of 200 keyword alarms and SQL alarms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlAlarmRules</td>
                    <td>This interface is used to query SQL alarms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlAlarmRule</td>
                    <td>This interface is used to delete SQL alarms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSqlAlarmRule</td>
                    <td>This interface is used to modify SQL alarms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Structured Configuration</td>
                    <td>DeleteStructTemplate</td>
                    <td>This API is used to delete the structured configuration of a specified log stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStructTemplate</td>
                    <td>This interface is used to query structured templates.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStructConfig</td>
                    <td>This API is invoked to create structured configurations using a structured template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStructTemplate</td>
                    <td>This API is used to modify the structured configuration of a specified log stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStructTemplate</td>
                    <td>This interface is used to query the structured configuration of a specified log stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStructTemplate</td>
                    <td>This API is used to create a structured configuration for a specified log stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStructConfig</td>
                    <td>This interface is invoked to modify structured configurations by using a structured template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBreifStructTemplate</td>
                    <td>This interface is used to query the brief list of structured templates.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tag Management</td>
                    <td>CreateTags</td>
                    <td>Add a tag</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
