# TICS MCP Server 

## 版本信息
v0.1.0

## 产品描述

TICS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务TICS交互的能力。可以基于自然语言对TICS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 作业实例管理 | ShowJobInstanceDag | 获取实例执行图 | To be tested |
|  | ListInstanceHistory | 查询作业的历史实例列表 | To be tested |
|  | ShowInstanceReport | 查询实例执行报告 | To be tested |
| 可信节点管理 | ShowAgentDetail | 功能描述:用户可以使用该接口获取单个可信计算节点详情信息。 | To be tested |
|  | ListAgents | 功能描述:用户可以使用该接口获取可信节点信息列表。支持节点名称与联盟名称的模糊查询。 | To be tested |
| 审计日志管理 | ListAuditInfo | 查询审计日志信息 | To be tested |
| 数据集管理 | ListLeagueDatasets | 功能描述:用户可以使用该接口查询联盟已注册数据集列表。 | To be tested |
| 统计信息管理 | ShowOverview | 查询当前租户的联盟及代理统计数量 | To be tested |
|  | ShowPartnerStatistics | 功能描述:用户可以使用该接口进行联盟合作方统计。 | To be tested |
|  | ShowJobStatistics | 功能描述:用户可以使用该接口进行联盟作业统计。 | To be tested |
|  | ShowDatasetStatistics | 用户可以使用该接口进行联盟数据集统计。 | To be tested |
| 联盟管理 | ListNotices | 功能描述:用户可以使用该接口查询通知管理列表。 | To be tested |
|  | UpdateLeague | 功能描述:用户可以使用接口更新联盟信息(包含联盟描述,联盟版本,隐私保护等级,查分隐私开关)。 | To be tested |
|  | ListPartners | 功能描述:用户可以使用该接口获取联盟组员信息 | To be tested |
|  | ListNodes | 功能描述:用户可以使用该接口查询联盟可信节点(包含聚合节点和计算节点)列表。 | To be tested |
|  | ListLeagues | 功能描述:用户可以使用该接口获取联盟列表。 | To be tested |
|  | ShowLeague | 功能描述:用户可以使用该接口获取联盟详细信息。 | To be tested |
| 联邦分析作业管理 | ListSqlJob | 查询联邦分析作业列表 | To be tested |
| 联邦学习作业管理 | ListFlJob | 查询联邦学习作业列表 | To be tested |
