# COC MCP Server 

## 版本信息
v0.1.0

## 产品描述

COC MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务COC交互的能力。可以基于自然语言对COC资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| CustomEventMessageIntegration | CreateReportCustomEvent | 支持租户将自开发的监控系统按照标准化集成至COC,集成后告警会按照标准格式上报至COC告警中心 | To be tested |
| DocumentManagement | UpdateDocument | 修改自定义作业 | To be tested |
|  | DeleteDocument | 删除自定义作业 | To be tested |
|  | CreateDocument | 创建自定义作业 | To be tested |
|  | ListDocumentAtomics | 获取原子能力列表 | To be tested |
|  | ListDocuments | 查询自定义作业列表 | To be tested |
|  | ExecuteDocument | 执行自定义作业 | To be tested |
|  | GetDocument | 查询自定义作业详情 | To be tested |
|  | GetDocumentAtomicInfo | 获取原子能力详细 | To be tested |
| EventMessageIntegration | CreateReportPrometheusEvent | Prometheus事件接入 | To be tested |
| ExecutionManagement | OperateExecution | 操作工单 | To be tested |
|  | ListExecutionSteps | 查询工单步骤详情 | To be tested |
|  | GetExecution | 查询作业工单详情 | To be tested |
|  | ListExecutions | 查询作业工单列表 | To be tested |
|  | ListExecutionInstances | 查询工单步骤批次实例,如脚本分批操作里的ECS实例 | To be tested |
| ExternalCocIncident | ShowCocIncidentDetail | ShowCocIncidentDetail  获取事件单详细 | To be tested |
|  | HandleCocIncident | HandleCocIncident 处理事件单 | To be tested |
|  | ListCocTicketOperationHistories | ListCocTicketOperationHistories  获取事件单历史 | To be tested |
|  | CreateCocIncident | CreateExternalIncident 创建事件单 | To be tested |
| ExternalCocIssues | ShowCocIssuesDetail | ShowCocIssuesDetail  获取事件单详细 | To be tested |
|  | CreateCocIssues | CreateExternalIssues 创建问题单 | To be tested |
| ListAuthorizableTicketsExternal | ListAuthorizableTicketsExternal | 查询COC可授权单列表(变更单号、事件单号、warroom和告警) | To be tested |
| ResourceTagManagement | UpdateResourceTags | 更新资源标签 | To be tested |
|  | ListScriptResourceTags | 查询资源标签列表 | To be tested |
| ScheduledTask | EnableScheduledTask | Enable scheduled task by id | To be tested |
|  | ShowScheduledTask | Get ScheduledTask info by id | To be tested |
|  | ListScheduledTask | Get ScheduledTask infos | To be tested |
|  | UpdateScheduledTask | Update ScheduledTask | To be tested |
|  | DisableScheduledTask | Disable scheduled task by id | To be tested |
|  | CreateScheduledTask | Create Scheduled Task | To be tested |
|  | DeleteScheduledTask | Delete scheduled task by id | To be tested |
|  | ListScheduledTaskHistory | get scheduled task history list | To be tested |
| ScriptExecutionManagement | ListScriptJobBatches | 查询:批次列表 | To be tested |
|  | GetScriptJobBatch | 查询:批次详情,分页获取批次中的实例列表。 | To be tested |
|  | ListScriptJobs | 查询作业工单列表,分页查询 | To be tested |
|  | OperateScriptJob | 操作类型:取消实例、跳过批次、取消整个工单、暂停整个工单、继续整个工单 | To be tested |
|  | GetScriptJobInfo | 查询执行:基本信息 | To be tested |
|  | GetScriptJobStatistics | 查询:实例状态统计信息。 | To be tested |
| ScriptManagement | GetScript | 获取脚本详情 | To be tested |
|  | UpdateScript | 修改作业脚本:自定义脚本 | To be tested |
|  | ListInstancesBatch | 根据分批策略获取分批结果,只支持自动分批: | To be tested |
|  | CheckScriptRisk | 根据作业内容,对作业评估风险,返回相关分析的结果和信息,结果仅供参考。 | To be tested |
|  | DeleteScript | 删除作业脚本:自定义脚本。 | To be tested |
|  | CreateScript | 创建作业脚本:自定义脚本 | To be tested |
|  | ExecuteScript | 执行脚本 | To be tested |
|  | AcceptScript | 功能:审批脚本。 | To be tested |
|  | ListScripts | 作业脚本列表:自定义脚本 | To be tested |
| ScriptPublicManagement | GetPublicScript | 展示公共脚本详情 | To be tested |
|  | ExecutePublicScript | 执行公共脚本 | To be tested |
|  | ListPublicScripts | 获取公共脚本列表,分页逻辑:采用limit+marker方式,提高分页效率。用自增id作为marker参数 | To be tested |
| WarRoom | ListWarRooms | 查询租户区WarRoom信息列表 | To be tested |
|  | CreateWarRoom | 创建租户区WarRoom | To be tested |
| application | ListApplications | 查询应用 | To be tested |
| application-model | ListApplicationModel | 查询下一级的子应用、组件、分组 | To be tested |
| applicationview | BatchCreateApplicationView | 批量创建应用视图 | To be tested |
| compliant | ListInstanceCompliant | 分页获取节点合规性报告 | To be tested |
|  | ShowInstancePatchItems | 分页获取节点补丁详情 | To be tested |
| multipleCloud | ListMultiCloudResources | 查询用户在云厂商中的资源 | To be tested |
| resource | CountMultiResources | 查询用户各种资源总数 | To be tested |
|  | ListResource | 查询用户所有资源 | To be tested |
|  | SyncResource | 从RMS同步用户所有资源 | To be tested |
