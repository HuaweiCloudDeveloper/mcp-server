# DAS MCP Server 

## 版本信息
v0.1.0

## 产品描述

DAS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DAS交互的能力。可以基于自然语言对DAS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 云DBA | ChangeChargeMode | 设置付费实例 | To be tested |
|  | ListFullSqlTasks | 全量SQL开关打开后,查询SQL洞察任务列表。该功能仅支持付费实例。 | To be tested |
|  | ShowSqlSwitchStatus | 查询DAS收集全量SQL和慢SQL的开关状态。该功能仅支持付费实例。 | To be tested |
|  | DeleteSqlLimitRules | 删除SQL限流规则。目前仅支持MySQL和PostgreSQL数据库 | To be tested |
|  | ShowTuning | 获取诊断结果 | To be tested |
|  | DeleteDbUser | 删除注册在DAS里的数据库用户。此接口只是将注册的数据库用户在DAS系统里删除,不会真正删除数据库用户对象。 | To be tested |
|  | CreateSqlLimitRules | 添加SQL限流规则。目前仅支持MySQL和PostgreSQL数据库。 | To be tested |
|  | ListDbUsers | 查询注册在DAS里的数据库用户列表,后续调用其他接口时(如查询实例会话列表接口)需要用到此接口返回的db_user_id。此接口不会返回数据库实例上的数据库用户对象。 | To be tested |
|  | ShowSqlExecutionPlan | 查询SQL执行计划。 | To be tested |
|  | ListSqlLimitRules | 查询SQL限流规则。目前仅支持MySQL和PostgreSQL数据库。 | To be tested |
|  | SetThresholdForMetric | 设置指标阈值 | To be tested |
|  | ShowQuotas | 查询云DBA配额 | To be tested |
|  | SynchronizeInstances | 同步实例列表。 | To be tested |
|  | ListCloudDbaInstances | 获取DAS云DBA实例列表。 | To be tested |
|  | ListProcesses | 支持根据数据库、用户查询实例会话列表。 | To be tested |
|  | ExportFullSqlDetails | 全量SQL开关打开后,创建SQL洞察任务,支持按节点、用户名、数据库、操作类型等导出全量SQL明细数据。该功能仅支持付费实例。 | To be tested |
|  | ListRiskItems | 查询资源风险实例风险项 | To be tested |
|  | ChangeSqlSwitch | 打开或者关闭DAS收集全量SQL开关,开启后,实例的性能损耗在5%以内。开启全量SQL后,本服务会对SQL的文本内容进行存储,以便进行分析。用户可自行设置全量SQL的保存时间范围,到期后会自动删除;如果未设置,数据默认保留7天。 | To be tested |
|  | ListInstanceTopSlowLog | 查询实例的TOP慢SQL列表 | To be tested |
|  | ExportTopSqlTrendDetails | TopSQL开关打开后,导出SQL执行耗时区间数据。该功能仅支持付费实例。查询时间间隔最长六小时。 | To be tested |
|  | ChangeTransactionSwitchStatus | 开启/关闭历史事务开关,仅支持MySQL引擎,并且依赖开启全量SQL或者慢SQL功能 | To be tested |
|  | ShowSqlExplain | 查询SQL执行计划。 | To be tested |
|  | CreateTuning | 执行SQL诊断, | To be tested |
|  | CreateSpaceAnalysisTask | 创建空间分析任务,如触发重新分析,支持MySQL和GaussDB(for MySQL)引擎 | To be tested |
|  | ExportSlowSqlStatistics | 慢SQL开关打开后,导出慢SQL统计数据。 | To be tested |
|  | ListInnodbLocks | 查询InnoDB锁等待列表。 | To be tested |
|  | ExportSqlStatements | 全量SQL开关打开后,一次性导出指定时间范围内的全量SQL数据,支持分页滚动获取。该功能仅支持付费实例。 | To be tested |
|  | ShowTransactionSwitchStatus | 查询历史事务开关。 | To be tested |
|  | ListTopSlowLog | 查询TOP慢SQL列表 | To be tested |
|  | DeleteProcess | 查杀会话。支持按照用户、数据库、会话列表查杀会话,三个条件至少指定一个。 | To be tested |
|  | RegisterDbUser | 此接口是将数据库用户和密码注册进DAS系统,同时会返回一个数据库用户ID ,后续调用其他接口时(如查询实例会话列表接口)需要用到此数据库用户ID。密码为加密存储,且仅用于DAS API相关功能。此接口不会在数据库实例上创建数据库用户对象。请确保输入的用户名和密码是已经存在并且是正确的。 | To be tested |
|  | ExportSlowQueryLogs | DAS收集慢SQL开关打开后,一次性导出指定时间范围内的慢SQL数据,支持分页滚动获取。免费实例仅支持查看最近一小时数据。 | To be tested |
|  | ShowDbUser | 查询注册在DAS里的数据库用户信息。此接口不能查询数据库实例上的数据库用户对象。 | To be tested |
|  | ListSpaceAnalysis | 获取空间分析数据列表。实例级别数据来源于文件系统,库级别和表级别数据来源于information_schema.tables表。空间&元数据分析最多分析10000张表,若缺少库表空间数据,可能是因为数据库实例表个数过多或者账号未保存密码。如果为保存密码,请使用用户管理接口或页面录入数据库账号。 支持MySQL、GaussDB(for MySQL)和SQLServer引擎。 | To be tested |
|  | ExportSlowSqlTrendDetails | 慢SQL开关打开后,导出慢SQL数量趋势。免费实例仅支持查看最近一小时数据。查询时间间隔最长一天。 | To be tested |
|  | ParseSqlLimitRules | 根据原始SQL生成SQL限流关键字,目前支持MySQL、MariaDB、GaussDB(for MySQL)三种引擎。 | To be tested |
|  | ListInstanceMultiNodesSingleMetric | 获取多节点单指标数据 | To be tested |
|  | ListMetadataLocks | 查询元数据锁列表。 | To be tested |
|  | ListRiskTrend | 查询资源风险实例风险趋势 | To be tested |
|  | UpdateDbUser | 修改注册在DAS里的数据库用户名和密码。此接口不会修改数据库实例上的数据库用户对象的用户名和密码。请确保输入的用户名和密码是已经存在并且是正确的。 | To be tested |
|  | ListHealthReportTask | 查询实例健康诊断报告列表。 | To be tested |
|  | ShowSqlLimitJobInfo | 查询指定ID的SQL限流任务信息 | To be tested |
|  | ExportTopRiskInstances | 导出TOP风险实例列表,支持查看最近24小时数据。 | To be tested |
|  | AddFullSqlTask | 创建全量SQL明细解析任务 | To be tested |
|  | ListInstanceDistribution | 查询实例分布情况 | To be tested |
|  | ShowInstanceHealthReport | 获取实例健康诊断报告内容。 | To be tested |
|  | ShowSqlLimitSwitchStatus | 查询SQL限流的开关状态。目前仅支持MySQL实例 | To be tested |
|  | ListTransactions | 查询历史事务列表。 | To be tested |
|  | ChangeSqlLimitSwitchStatus | 设置SQL限流开关状态。目前仅支持MySQL数据库。 | To be tested |
|  | UpdateSqlLimitRules | 修改SQL限流规则。目前仅支持PostgreSQL数据库 | To be tested |
|  | ListInstanceNodesInfo | 获取单个实例节点信息 | To be tested |
|  | CreateHealthReportTask | 创建实例健康诊断任务。 | To be tested |
|  | ShowMetricNamesSupport | 多节点单指标支持指标信息 | To be tested |
|  | ExportTopSqlTemplatesDetails | TopSQL开关打开后,导出TopSQL模板列表。该功能仅支持付费实例。查询时间间隔最长一小时。 | To be tested |
|  | ExportSlowSqlTemplatesDetails | 慢SQL开关打开后,导出慢SQL模板列表。免费实例仅支持查看最近一小时数据。查询时间间隔最长一天。 | To be tested |
| 开发工具 | CancelShareConnections | 删除共享链接, | To be tested |
|  | CreateInstanceConnection | 创建实例连接 | To be tested |
|  | CreateShareConnections | 设置共享链接, | To be tested |
|  | ListConnections | 查询实例连接列表 | To be tested |
| 获取API版本 | ShowApiVersion | 查询指定的API版本信息 | To be tested |
|  | ListApiVersions | 查询API版本列表 | To be tested |
