# DBSS MCP Server 

## 版本信息
v0.1.0

## 产品描述

DBSS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DBSS交互的能力。可以基于自然语言对DBSS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| TMS标签 | BatchDeleteResourceTag | 批量删除资源标签 | To be tested |
|  | CountResourceInstanceByTag | 根据标签查询资源实例数量 | To be tested |
|  | ListProjectResourceTags | 查询项目标签 | To be tested |
|  | ListResourceInstanceByTag | 根据标签查询资源实例列表 | To be tested |
|  | BatchAddResourceTag | 批量添加资源标签 | To be tested |
| 审计Agent | DownloadAuditAgent | 下载审计Agent | To be tested |
|  | ListAuditAgent | 查询数据库Agent列表 | To be tested |
|  | AddAuditAgent | 添加审计数据库Agent | To be tested |
|  | DeleteAuditAgent | 删除数据库Agent | To be tested |
|  | SwitchAgent | 用于开启和关闭Agent审计的功能,当开启后,开始抓取用户的访问信息。 | To be tested |
| 审计实例 | ListAuditInstanceJobs | 查询实例创建任务信息 | To be tested |
|  | DeleteInstances | 只有按需计费模式实例没有任务时 或 包周期模式实例状态为故障时,才能执行此操作。 | To be tested |
|  | UpdateAuditSecurityGroup | 修改实例安全组 | To be tested |
|  | RebootAuditInstance | 重启审计实例 | To be tested |
|  | CreateInstancesPeriodOrder | 包年包月计费模式创建审计实例 | To be tested |
|  | StopAuditInstance | 关闭审计实例 | To be tested |
|  | ListAuditInstances | 查询审计实例列表 | To be tested |
|  | UpdateAuditInstance | 更新审计实例信息 | To be tested |
|  | StartAuditInstance | 开启审计实例 | To be tested |
| 审计数据库 | DeleteAuditDatabase | 删除数据库 | To be tested |
|  | AddRdsDatabase | 添加RDS数据库 | To be tested |
|  | ListRdsDatabases | 查询RDS数据库列表 | To be tested |
|  | ListAuditDatabases | 查询数据库列表 | To be tested |
|  | SwitchAuditDatabase | 开启关闭数据库 | To be tested |
|  | AddAuditDatabase | 添加自建数据库 | To be tested |
| 审计规则 | SwitchRiskRule | 开启关闭风险规则 | To be tested |
|  | ListSqlInjectionRules | 查询SQL注入规则策略 | To be tested |
|  | ShowAuditRuleRisk | 查询指定风险规则策略 | To be tested |
|  | ListAuditRuleScopes | 查询审计范围策略列表 | To be tested |
|  | ListAuditRuleRisks | 查询风险规则策略 | To be tested |
|  | ListAuditSensitiveMasks | 查询隐私数据脱敏规则 | To be tested |
| 待下线接口 | AddRdsNoAgentDatabase | 添加RDS数据库。V1版本已不再维护,待下线。 | To be tested |
| 数据分析 | ListAuditSummaryInfos | 查询审计汇总信息 | To be tested |
|  | ListAuditAlarmLog | 查询审计告警信息 | To be tested |
|  | ListAuditSqls | 查询审计SQL语句 | To be tested |
| 管理侧查询 | ListAvailabilityZoneInfos | 查询可用区信息 | To be tested |
|  | ShowAuditQuota | 查询账户配额信息 | To be tested |
|  | ListEcsSpecification | 查询ECS服务器规格信息 | To be tested |
|  | ListAuditOperateLogs | 查询用户操作日志信息 | To be tested |
