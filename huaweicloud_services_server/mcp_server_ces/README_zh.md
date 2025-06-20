# CES MCP Server 

## 版本信息
v0.1.0

## 产品描述

CES MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CES交互的能力。可以基于自然语言对CES资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Agent任务相关接口 | BatchCreateAgentInvocations | 批量创建Agent任务 | To be tested |
|  | ListAgentInvocations | 查询Agent任务列表 | To be tested |
| 一键告警 | ListOneClickAlarms | 查询一键告警列表 | To be tested |
|  | CreateOneClickAlarm | 创建一键告警 | To be tested |
|  | UpdateOneClickAlarmNotifications | 批量修改开启状态的一键告警关联告警规则的告警通知 | To be tested |
|  | BatchDeleteOneClickAlarms | 批量删除一键告警 | To be tested |
|  | ListOneClickAlarmRules | 查询一键告警关联告警规则列表 | To be tested |
|  | BatchUpdateOneClickAlarmPoliciesEnabledState | 批量修改一键告警关联告警规则策略的启用状态 | To be tested |
|  | BatchUpdateOneClickAlarmsEnabledState | 批量修改一键告警关联告警规则的启用状态 | To be tested |
| 事件监控 | CreateEvents | 上报自定义事件。 | To be tested |
|  | ListEventDetail | 根据事件监控名称,查询该事件发生的详细信息。 | To be tested |
|  | ListEvents | 查询事件监控列表,包括系统事件和自定义事件。 | To be tested |
| 告警模板 | ListAlarmTemplates | 查询告警模板列表 | To be tested |
|  | BatchDeleteAlarmTemplates | 批量删除自定义告警模板 | To be tested |
|  | CreateAlarmTemplate | 创建自定义告警模板 | To be tested |
|  | ShowAlarmTemplate | 查询告警模板详情 | To be tested |
|  | UpdateAlarmTemplate | 修改自定义告警模板 | To be tested |
| 告警模板关联告警规则 | ListAlarmTemplateAssociationAlarms | 查询告警模板关联的告警规则列表 | To be tested |
| 告警策略 | UpdateAlarmRulePolicies | 修改告警规则策略(全量修改) | To be tested |
|  | ListAlarmRulePolicies | 根据告警规则ID查询策略列表 | To be tested |
| 告警规则 | BatchEnableAlarmRules | 批量启停告警规则 | To be tested |
|  | ListAlarmRules | 查询告警规则列表 | To be tested |
|  | BatchDeleteAlarmRules | 批量删除告警规则V2接口 | To be tested |
|  | CreateAlarmRules | 创建告警规则 | To be tested |
| 告警规则管理 | ListAlarms | 查询告警规则列表,可以指定分页条件限制结果数量,可以指定排序规则。 | To be tested |
|  | CreateAlarm | 创建一条告警规则。 | To be tested |
|  | DeleteAlarm | 删除一条告警规则。 | To be tested |
|  | ShowAlarm | 根据告警ID查询告警规则信息。 | To be tested |
|  | DeleteAlarmTemplate | 根据ID删除自定义告警模板。 | To be tested |
|  | UpdateAlarmAction | 启动或停止一条告警规则。 | To be tested |
|  | UpdateAlarm | 修改告警规则。 | To be tested |
| 告警记录 | ListAlarmHistories | 查询告警记录列表 | To be tested |
| 告警资源 | ListAlarmRuleResources | 根据告警规则ID查询告警规则资源列表 | To be tested |
|  | DeleteAlarmRuleResources | 批量删除告警规则资源(资源分组类型的告警规则不支持),资源分组类型的修改请使用资源分组管理相关接口 | To be tested |
|  | AddAlarmRuleResources | 批量增加告警规则资源(资源分组类型的告警规则不支持),资源分组类型的修改请使用资源分组管理相关接口 | To be tested |
| 告警通知 | UpdateAlarmNotifications | 修改告警规则告警通知信息,告警策略&资源请使用对应接口 | To be tested |
| 告警通知屏蔽 | BatchUpdateNotificationMaskTime | 批量修改告警通知屏蔽规则的屏蔽时间 | To be tested |
|  | ListNotificationMasks | 批量查询指定类型的通知屏蔽规则,目前最多支持100个通知屏蔽规则的批量查询。 | To be tested |
|  | BatchDeleteNotificationMasks | 批量删除告警通知屏蔽规则 | To be tested |
|  | BatchUpdateNotificationMasks | 批量设置告警通知屏蔽规则 | To be tested |
|  | UpdateNotificationMask | 修改告警通知屏蔽规则 | To be tested |
|  | ListNotificationMaskResources | 查询告警通知屏蔽资源列表 | To be tested |
| 指标管理 | ListAgentDimensionInfo | 根据ECS/BMS资源ID查询磁盘、挂载点、进程、显卡、RAID控制器维度指标信息;维度NPU已经为原始值,不需要调用该接口进行额外查询获取指标信息 | To be tested |
|  | ListMetrics | 查询系统当前可监控指标列表,可以指定指标命名空间、指标名称、维度、排序方式,起始记录和最大记录条数过滤查询结果。 | To be tested |
| 插件状态查询 | ListAgentStatus | 插件状态查询,包括uniagent状态以及插件状态 | To be tested |
| 监控数据管理 | BatchListMetricData | 批量查询指定时间范围内指定指标的指定粒度的监控数据,目前最多支持500指标的批量查询。 对于不同的period取值和查询的指标数量,默认的最大查询区间(to-from)不同。 规则为"指标数量*(to-from)/监控周期<=3000",若超出阈值,会自动调整from以满足规则。 | To be tested |
|  | CreateMetricData | 添加一条或多条指标监控数据。 | To be tested |
|  | ShowEventData | 查询指定时间范围指定事件类型的主机配置数据,可以通过参数指定需要查询的数据维度。注意:该接口提供给HANA场景下SAP Monitor查询主机配置数据,其他场景下查不到主机配置数据。 | To be tested |
|  | ShowMetricData | 查询指定时间范围指定指标的指定粒度的监控数据,可以通过参数指定需要查询的数据维度。 | To be tested |
| 监控看板 | DeleteDashboards | 批量删除监控看板 | To be tested |
|  | UpdateDashboard | 修改监控看板 | To be tested |
|  | ListDashboardInfos | 查询监控看板列表 | To be tested |
|  | CreateOneDashboard | 创建/复制监控看板 | To be tested |
| 监控视图 | ListDashboardWidgets | 查询指定监控看板下的监控视图列表 | To be tested |
|  | ShowWidget | 查询指定监控视图信息 | To be tested |
|  | BatchUpdateWidgets | 批量更新监控视图 | To be tested |
|  | CreateDashboardWidgets | 创建/复制/批量创建监控视图到指定的监控看板 | To be tested |
|  | DeleteOneWidget | 删除指定监控视图 | To be tested |
| 资源分组 | BatchDeleteResourceGroups | 批量删除资源分组 | To be tested |
|  | ListResourceGroups | 查询资源分组列表 | To be tested |
|  | UpdateResourceGroup | 修改资源分组 | To be tested |
|  | UpdateResourceGroupAssociationAlarmTemplate | 提交资源分组批量关联自定义告警模板异步任务,由异步任务覆盖性创建告警规则。每个用户创建处于待执行状态的异步任务数量上限为100个,单个资源分组仅可有1个未完成的任务。 | To be tested |
|  | CreateResourceGroup | 创建资源分组 | To be tested |
|  | ShowResourceGroup | 查询指定资源分组详情 | To be tested |
| 资源分组关联资源 | ListResourceGroupsServicesResources | 查询资源分组下指定服务类别特定维度的资源列表 | To be tested |
|  | BatchDeleteResources | 给自定义资源分组,即类型为手动添加的资源分组,批量删除关联资源 | To be tested |
|  | BatchCreateResources | 给自定义资源分组,即类型为手动添加的资源分组,批量增加关联资源 | To be tested |
| 资源分组管理 | DeleteResourceGroup | 删除一条资源分组。 | To be tested |
|  | ListResourceGroup | 查询所创建的所有资源分组。 | To be tested |
| 资源标签管理 | ListCesTargetProjectTags | 查询CES指定项目指定资源类型标签列表。 | To be tested |
| 配额管理 | ShowQuotas | 查询用户可以创建的资源配额总数及当前使用量,当前仅有告警规则一种资源类型。 | To be tested |
