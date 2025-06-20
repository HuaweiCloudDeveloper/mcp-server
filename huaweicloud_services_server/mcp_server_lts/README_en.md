# LTS MCP Server 


## Version
v0.1.0

## Overview

LTS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service LTS. Full-chain management of LTS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AOM container logs are connected to LTS | DeleteAomMappingRules | This API is used to delete an lts access rule. | To be tested |
|  | ShowAomMappingRules | This interface is used to query all access LTS rules for AOM logs. | To be tested |
|  | CreateAomMappingRules | This interface is used to create an AOM log access LTS rule. | To be tested |
|  | ShowAomMappingRule | This interface is used to query a single AOM log. lts | To be tested |
|  | UpdateAomMappingRules | This interface is used to modify an access rule. | To be tested |
| Alarm List | DeleteActiveAlarms | This interface is used to delete active alarms. | To be tested |
|  | ListActiveOrHistoryAlarms | This interface is used to query the alarm list. | To be tested |
| Alarm Subject | ListNotificationTopics | This API is used to query SMN topics. | To be tested |
| Consumer group management | DeleteConsumerGroup | Delete a consumer group. | To be tested |
| Dashboard Management | CreateDashboardGroup | Creating a Dashboard Group | To be tested |
|  | CreateDashBoard | Create a dashboard | To be tested |
|  | DeleteDashboard | Delete a dashboard | To be tested |
| Host group management | UpdateHostGroup | Modifying a host group | To be tested |
|  | ListHostGroup | Query the host group list | To be tested |
|  | DeleteHostGroup | Delete a host group | To be tested |
|  | CreateHostGroup | Create a host group | To be tested |
| Keyword alarm rule | UpdateKeywordsAlarmRule | This interface is used to modify keyword alarms. | To be tested |
|  | DeleteKeywordsAlarmRule | This interface is used to delete keyword alarms. | To be tested |
|  | CreateKeywordsAlarmRule | This API is used to create keyword alarms. Currently, a maximum of 200 keyword alarms and SQL alarms can be created for each account. | To be tested |
|  | ListKeywordsAlarmRules | This interface is used to query keyword alarms. | To be tested |
| Log Dump | UpdateTransfer | This API is used to update OBS, DIS, and DMS dumping. | To be tested |
|  | RegisterDmsKafkaInstance | This API is used to register a DMS Kafka instance. | To be tested |
|  | CreateLogDumpObs | This API is used to dump logs of one or more specified log streams to OBS. | To be tested |
|  | ListTransfers | This API is used to query OBS, DIS, and DMS dump configurations. | To be tested |
|  | CreateTransfer | This API is used to create OBS, DIS, or DMS dumping. | To be tested |
|  | DeleteTransfer | This API is used to delete OBS, DIS, and DMS dumping. | To be tested |
| Log Flow Chart | ListCharts | This interface is used to query log flow charts. | To be tested |
| Log Group Management | ListLogGroups | This interface is used to query all log groups under an account. | To be tested |
|  | DeleteLogGroup | This API is used to delete a specified log group. If log dumping is configured for a log stream in a log group, you need to cancel the log dumping before deleting the log stream. | To be tested |
|  | CreateLogGroup | This interface is used to create a log group. | To be tested |
|  | UpdateLogGroup | This API is used to modify the log retention duration of a specified log group. | To be tested |
| Log Stream Management | UpdateLogStream | This interface is used to modify the log storage duration in a specified log flow. | To be tested |
|  | ListLogStream | This API is used to query all log streams in a specified log group. | To be tested |
|  | ListLogStreams | This interface is used to query LTS log flow information. | To be tested |
|  | CreateLogStream | This interface is used to create a log stream in a specified log group. | To be tested |
|  | DeleteLogStream | This interface is used to delete a specified log stream from a specified log group. If log dumping is configured for the log stream, you need to cancel the log dumping before deleting it. | To be tested |
|  | CreateLogStreamIndex | Creates an index for a specified flow. | To be tested |
| Log access | DeleteAccessConfig | Delete log access | To be tested |
|  | UpdateAccessConfig | Modify log access | To be tested |
|  | CreateAgencyAccess | New Cross-Account Log Access | To be tested |
|  | ListAccessConfig | Query the log access list | To be tested |
|  | CreateAccessConfig | Create log access | To be tested |
| Log management | ListLogContext | Querying Context Logs This interface is used to query the logs before and after specified logs. | To be tested |
|  | ListStructuredLogsWithTimeRange | This API is used to query the structured log content in a specified log flow (new version). | To be tested |
|  | ListLogHistogram | Query the number of keyword search records | To be tested |
|  | ListTopnTrafficStatistics | Count the traffic of top N log groups or log streams | To be tested |
|  | Deletefavorite | Cancel favorites | To be tested |
|  | ListTimeLineTrafficStatistics | Querying resources by time segment | To be tested |
|  | Createfavorite | Create log collection | To be tested |
|  | ListLogs | This interface is used to query logs in a specified log stream. | To be tested |
|  | ListQueryStructuredLogs | This API is used to query structured logs in a specified log flow. | To be tested |
| Message Template Management | UpdateNotificationTemplate | This interface is used to modify a notification template by name. | To be tested |
|  | ShowNotificationTemplate | This interface is used to query a notification template. | To be tested |
|  | DeleteNotificationTemplate | This interface is used to delete a notification template. | To be tested |
|  | ListNotificationTemplate | This interface is used to preview the email format of the notification template. | To be tested |
|  | ListNotificationTemplates | This interface is used to query notification templates. | To be tested |
|  | CreateNotificationTemplate | This interface is used to create notification templates. Currently, each account can create a maximum of 100 notification templates. The name of the created notification templates cannot be changed. | To be tested |
| Multi-account log aggregation | UpdateLogConvergeConfig | Only the administrator or delegated administrator can update the aggregation configuration. | To be tested |
|  | ShowLogConvergeConfig | Only the organization administrator or agency administrator invokes this interface to obtain the organization member aggregation configuration. | To be tested |
|  | ShowAdminConfig | Only administrators or delegated administrators can invoke this interface to obtain the log aggregation switch. | To be tested |
|  | UpdateSwitch | Only the administrator or delegated administrator can invoke the interface to modify the log aggregation switch. | To be tested |
|  | ShowMemberGroupAndStream | This interface can be invoked only by the administrator or delegated administrator to obtain the log streams of the organization member log group. | To be tested |
| Overcollected | EnableLogCollection | This interface is used to enable the over-collecting log function. | To be tested |
|  | DisableLogCollection | This interface is used to disable the log collection function. | To be tested |
| Protection Website Management in Cloud Mode | ListHost | Query the domain name list in cloud mode | To be tested |
| Quick query | CreateSearchCriterias | Adding a quick query | To be tested |
|  | ListQueryAllSearchCriterias | Query all quick queries in a log group | To be tested |
|  | ListCriterias | Quick query | To be tested |
|  | ListHistorySql | SQL for querying user history | To be tested |
|  | DeleteSearchCriterias | Delete a quick query | To be tested |
| SDK Streaming Consumption Open API | ListDetailsConsumerGroup | Query consumer group details | To be tested |
|  | ShowCursorByTime | Query the cursor by time | To be tested |
|  | UpdateCheckPoint | Update consumer group location | To be tested |
|  | CreateConsumerGroup | Create consumer group | To be tested |
|  | ConsumerGroupHeartBeat | The consumer sends a heartbeat message to the server. | To be tested |
|  | ShowCursorTime | Query the server time using the cursor | To be tested |
|  | ListConsumerGroup | Query the consumer group list | To be tested |
|  | ShowLogStreamShards | Obtains all query shards for stream consumption | To be tested |
| SQL alarm rule | UpdateAlarmRuleStatus | Change the alarm rule status. | To be tested |
|  | CreateSqlAlarmRule | This interface is used to create SQL alarms. Currently, each account can create a maximum of 200 keyword alarms and SQL alarms. | To be tested |
|  | ListSqlAlarmRules | This interface is used to query SQL alarms. | To be tested |
|  | DeleteSqlAlarmRule | This interface is used to delete SQL alarms. | To be tested |
|  | UpdateSqlAlarmRule | This interface is used to modify SQL alarms. | To be tested |
| Structured Configuration | DeleteStructTemplate | This API is used to delete the structured configuration of a specified log stream. | To be tested |
|  | ListStructTemplate | This interface is used to query structured templates. | To be tested |
|  | CreateStructConfig | This API is invoked to create structured configurations using a structured template. | To be tested |
|  | UpdateStructTemplate | This API is used to modify the structured configuration of a specified log stream. | To be tested |
|  | ShowStructTemplate | This interface is used to query the structured configuration of a specified log stream. | To be tested |
|  | CreateStructTemplate | This API is used to create a structured configuration for a specified log stream. | To be tested |
|  | UpdateStructConfig | This interface is invoked to modify structured configurations by using a structured template. | To be tested |
|  | ListBreifStructTemplate | This interface is used to query the brief list of structured templates. | To be tested |
| Tag Management | CreateTags | Add a tag | To be tested |

