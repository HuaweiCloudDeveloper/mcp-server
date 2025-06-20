# LTS MCP Server 

## 版本信息
v0.1.0

## 产品描述

LTS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务LTS交互的能力。可以基于自然语言对LTS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AOM容器日志接入LTS | DeleteAomMappingRules | 该接口用于删除lts接入规则。 | To be tested |
|  | ShowAomMappingRules | 该接口用于查询aom日志所有接入lts规则 | To be tested |
|  | CreateAomMappingRules | 该接口用于创建aom日志接入lts规则 | To be tested |
|  | ShowAomMappingRule | 该接口用于查询单个aom日志接入lts | To be tested |
|  | UpdateAomMappingRules | 该接口用于修改接入规则 | To be tested |
| SDK流式消费开放API | ListDetailsConsumerGroup | 查询消费组详情 | To be tested |
|  | ShowCursorByTime | 通过时间查询cursor | To be tested |
|  | UpdateCheckPoint | 更新消费组位点 | To be tested |
|  | CreateConsumerGroup | 创建消费组 | To be tested |
|  | ConsumerGroupHeartBeat | 消费者发送心跳到服务端 | To be tested |
|  | ShowCursorTime | 通过cursor查询服务端时间 | To be tested |
|  | DeleteConsumerGroup | 删除消费组 | To be tested |
|  | ListConsumerGroup | 查询消费组列表 | To be tested |
|  | ShowLogStreamShards | 流消费获取所有的query shards | To be tested |
| SQL告警规则 | UpdateAlarmRuleStatus | 改变告警规则状态 | To be tested |
|  | CreateSqlAlarmRule | 该接口用于创建SQL告警,目前每个帐户最多可以创建共200个关键词告警与SQL告警 | To be tested |
|  | ListSqlAlarmRules | 该接口用于查询SQL告警 | To be tested |
|  | DeleteSqlAlarmRule | 该接口用于删除SQL告警 | To be tested |
|  | UpdateSqlAlarmRule | 该接口用于修改SQL告警 | To be tested |
| 主机组管理 | UpdateHostGroup | 修改主机组 | To be tested |
|  | ListHostGroup | 查询主机组列表 | To be tested |
|  | DeleteHostGroup | 删除主机组 | To be tested |
|  | ListHost | 查询主机列表 | To be tested |
|  | CreateHostGroup | 创建主机组 | To be tested |
| 仪表盘管理 | CreateDashboardGroup | 创建仪表盘分组 | To be tested |
|  | CreateDashBoard | 创建仪表盘 | To be tested |
|  | DeleteDashboard | 删除仪表盘 | To be tested |
| 关键词告警规则 | UpdateKeywordsAlarmRule | 该接口用于修改关键词告警。 | To be tested |
|  | DeleteKeywordsAlarmRule | 该接口用于删除关键词告警。 | To be tested |
|  | CreateKeywordsAlarmRule | 该接口用于创建关键词告警,目前每个帐户最多可以创建共200个关键词告警与SQL告警。 | To be tested |
|  | ListKeywordsAlarmRules | 该接口用于查询关键词告警。 | To be tested |
| 告警主题 | ListNotificationTopics | 该接口用于查询SMN主题 | To be tested |
| 告警列表 | DeleteActiveAlarms | 该接口用于删除活动告警 | To be tested |
|  | ListActiveOrHistoryAlarms | 该接口用于查询告警列表 | To be tested |
| 多账号日志汇聚 | UpdateLogConvergeConfig | 只能由管理员或者委托管理员 ,更新汇聚配置 | To be tested |
|  | ShowLogConvergeConfig | 只能由组织管理员或者委托管理员调用    获取组织成员汇聚配置 | To be tested |
|  | ShowAdminConfig | 只能由管理员或者委托管理员调用    获取日志汇聚开关 | To be tested |
|  | UpdateSwitch | 只能由管理员或者委托管理员调用     修改日志汇聚开关 | To be tested |
|  | ShowMemberGroupAndStream | 只能由管理员或者委托管理员调用,获取组织成员日志组日志流 | To be tested |
| 快速查询 | CreateSearchCriterias | 添加快速查询 | To be tested |
|  | ListQueryAllSearchCriterias | 查询日志组下所有快速查询 | To be tested |
|  | ListCriterias | 获取快速查询 | To be tested |
|  | ListHistorySql | 查询用户历史sql | To be tested |
|  | DeleteSearchCriterias | 删除快速查询 | To be tested |
| 日志接入 | DeleteAccessConfig | 删除日志接入 | To be tested |
|  | UpdateAccessConfig | 修改日志接入 | To be tested |
|  | CreateAgencyAccess | 新建跨账号日志接入 | To be tested |
|  | ListAccessConfig | 查询日志接入列表 | To be tested |
|  | CreateAccessConfig | 创建日志接入 | To be tested |
| 日志流图表 | ListCharts | 该接口用于查询日志流图表 | To be tested |
| 日志流管理 | UpdateLogStream | 该接口用于修改指定日志流下的日志存储时长。 | To be tested |
|  | ListLogStream | 该接口用于查询指定日志组下的所有日志流信息。 | To be tested |
|  | ListLogStreams | 该接口用于查询LTS日志流信息。 | To be tested |
|  | CreateLogStream | 该接口用于创建某个指定日志组下的日志流 | To be tested |
|  | DeleteLogStream | 该接口用于删除指定日志组下的指定日志流。当该日志流配置了日志转储,需要取消日志转储后才可删除。 | To be tested |
|  | CreateLogStreamIndex | 向指定流创建索引 | To be tested |
| 日志管理 | ListLogContext | 查询上下文日志 该接口用于查询指定日志前(上文)后(下文)的若干条日志。 | To be tested |
|  | ListStructuredLogsWithTimeRange | 该接口用于查询指定日志流下的结构化日志内容(新版)。 | To be tested |
|  | ListLogHistogram | 查询关键词搜索条数 | To be tested |
|  | ListTopnTrafficStatistics | 统计top n的日志组或日志流流量 | To be tested |
|  | Deletefavorite | 取消收藏 | To be tested |
|  | ListTimeLineTrafficStatistics | 按时间段统计查询资源 | To be tested |
|  | Createfavorite | 创建日志收藏 | To be tested |
|  | ListLogs | 该接口用于查询指定日志流下的日志内容。 | To be tested |
|  | ListQueryStructuredLogs | 该接口用于查询指定日志流下的结构化日志内容。 | To be tested |
| 日志组管理 | ListLogGroups | 该接口用于查询账号下所有日志组。 | To be tested |
|  | DeleteLogGroup | 该接口用于删除指定日志组。当日志组中的日志流配置了日志转储,需要取消日志转储后才可删除。 | To be tested |
|  | CreateLogGroup | 该接口用于创建一个日志组 | To be tested |
|  | UpdateLogGroup | 该接口用于修改指定日志组下的日志存储时长。 | To be tested |
| 日志转储 | UpdateTransfer | 该接口用于更新OBS转储,DIS转储,DMS转储。 | To be tested |
|  | RegisterDmsKafkaInstance | 该接口用于注册DMS kafka实例。 | To be tested |
|  | CreateLogDumpObs | 该接口用于将指定的一个或多个日志流的日志转储到OBS服务。 | To be tested |
|  | ListTransfers | 该接口用于查询OBS转储,DIS转储,DMS转储配置。 | To be tested |
|  | CreateTransfer | 该接口用于创建OBS转储,DIS转储,DMS转储。 | To be tested |
|  | DeleteTransfer | 该接口用于删除OBS转储,DIS转储,DMS转储。 | To be tested |
| 标签管理 | CreateTags | 添加标签 | To be tested |
| 消息模板管理 | UpdateNotificationTemplate | 该接口用于修改通知模板,根据名称进行修改。 | To be tested |
|  | ShowNotificationTemplate | 该接口用于查询单个通知模板 | To be tested |
|  | DeleteNotificationTemplate | 该接口用于删除通知模板。 | To be tested |
|  | ListNotificationTemplate | 该接口用于预览通知模板邮件格式 | To be tested |
|  | ListNotificationTemplates | 该接口用于查询通知模板。 | To be tested |
|  | CreateNotificationTemplate | 该接口用于创建通知模板,目前每个帐户最多可以创建共100个通知模板,创建后名称不可修改。 | To be tested |
| 结构化配置 | DeleteStructTemplate | 该接口用于删除指定日志流下的结构化配置。 | To be tested |
|  | ListStructTemplate | 该接口用于查询结构化模板。 | To be tested |
|  | CreateStructConfig | 该接口通过结构化模板创建结构化配置。 | To be tested |
|  | UpdateStructTemplate | 该接口用于修改指定日志流下的结构化配置。 | To be tested |
|  | ShowStructTemplate | 该接口用于查询指定日志流下的结构化配置内容。 | To be tested |
|  | CreateStructTemplate | 该接口用于创建指定日志流下的结构化配置。 | To be tested |
|  | UpdateStructConfig | 该接口通过结构化模板修改结构化配置 | To be tested |
|  | ListBreifStructTemplate | 该接口用于查询结构化模板简略列表。 | To be tested |
| 超额采集 | EnableLogCollection | 该接口用于将超额采集日志功能打开。 | To be tested |
|  | DisableLogCollection | 该接口用于将超额采集日志功能关闭。 | To be tested |
