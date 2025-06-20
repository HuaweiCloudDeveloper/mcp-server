# SA MCP Server 

## 版本信息
v0.1.0

## 产品描述

SA MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务SA交互的能力。可以基于自然语言对SA资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AlertRules | EnableAlertRule | Enable alert rule | To be tested |
|  | CreateAlertRuleSimulation | Simulate alert rule | To be tested |
|  | ListAlertRules | List alert rules | To be tested |
|  | ShowAlertRuleTemplate | List alert rule templates | To be tested |
|  | DeleteAlertRule | Delete alert rule | To be tested |
|  | DisableAlertRule | Disable alert rule | To be tested |
|  | ShowAlertRule | Get alert rule | To be tested |
|  | CreateAlertRule | Create alert rule | To be tested |
|  | ListAlertRuleTemplates | List alert rule templates | To be tested |
|  | ListAlertRuleMetrics | List alert rule metrics | To be tested |
|  | UpdateAlertRule | Update alert rule | To be tested |
| Alerts | ChangeAlert | 编辑告警,根据实际修改的属性更新,未修改的列不更新 | To be tested |
|  | ShowAlert | 获取告警详情 | To be tested |
|  | CreateAlert | 创建告警 | To be tested |
|  | DeleteAlert | 删除告警 | To be tested |
|  | CreateBatchOrderAlerts | 告警转事件 | To be tested |
|  | ListAlerts | 搜索告警列表 | To be tested |
| Incidents | CreateIncident | 创建事件 | To be tested |
|  | DeleteIncident | 创建事件 | To be tested |
|  | ListIncidents | 搜索事件列表 | To be tested |
|  | ShowIncident | 获取事件详情 | To be tested |
|  | ListIncidentTypes | 获取事件的类型列表 | To be tested |
|  | ChangeIncident | 编辑事件,根据实际修改的属性更新,未修改的列不更新 | To be tested |
| Indicator | ShowIndicatorDetail | 查询指标详情(仅支持华东-上海一使用) | To be tested |
|  | CreateIndicator | 创建指标(仅支持华东-上海一使用) | To be tested |
|  | UpdateIndicator | 更新指标(仅支持华东-上海一使用) | To be tested |
|  | DeleteIndicator | 删除指标(仅支持华东-上海一使用) | To be tested |
|  | ListIndicators | List all indicators | To be tested |
| Playbook | ListPlaybooks | List all playbooks. | To be tested |
|  | ShowPlaybookStatistics | 剧本统计数据 | To be tested |
|  | DeletePlaybook | Delete playbook. | To be tested |
|  | ShowPlaybookMonitors | 剧本运行监控 | To be tested |
|  | ShowPlaybook | Show playbook | To be tested |
|  | UpdatePlaybook | Update playbook. | To be tested |
|  | CreatePlaybook | Create playbook. | To be tested |
| Playbook action | UpdatePlaybookAction | Update action. | To be tested |
|  | ListPlaybookActions | List all actions. | To be tested |
|  | CreatePlaybookAction | Create action. | To be tested |
|  | DeletePlaybookAction | Delete action. | To be tested |
| Playbook approve | ListPlaybookApproves | List approves. | To be tested |
|  | CreatePlaybookApprove | Create playbook approve. | To be tested |
| Playbook instance | ShowPlaybookInstance | Show playbook instance | To be tested |
|  | ShowPlaybookTopology | Show playbook Topology | To be tested |
|  | ListPlaybookAuditLogs | List audit logs. | To be tested |
|  | ChangePlaybookInstance | Operation Playbook Instance. | To be tested |
|  | ListPlaybookInstances | List playbook instances | To be tested |
| Playbook rule | UpdatePlaybookRule | Update rule. | To be tested |
|  | CreatePlaybookRule | Create rule. | To be tested |
|  | DeletePlaybookRule | Delete rule. | To be tested |
|  | ShowPlaybookRule | Show rule formation. | To be tested |
| Playbook version | UpdatePlaybookVersion | Update playbook version. | To be tested |
|  | CreatePlaybookVersion | Create playbook version. | To be tested |
|  | ShowPlaybookVersion | Show playbook version version | To be tested |
|  | ListPlaybookVersions | List all versions of playbook. | To be tested |
|  | DeletePlaybookVersion | Delete playbook version. | To be tested |
|  | CopyPlaybookVersion | Copy Playbook and version to a new one | To be tested |
| Relation | ListDataobjectRelation | List Dataobject Relation | To be tested |
|  | CreateDataobjectRelation | Create Dataobject Relation | To be tested |
|  | DeleteDataobjectRelation | Delete Dataobject Relation | To be tested |
| 事件管理 | ImportEvents | 批量数据上报,每批次最多不超过50条。 | To be tested |
| 产品管理 | CheckProductHealthy | SA提供心跳接口,集成产品定时(每五分钟)发送心跳报文到态势感知,用来确认集成产品与态势感知之间的通路是否健康。 | To be tested |
