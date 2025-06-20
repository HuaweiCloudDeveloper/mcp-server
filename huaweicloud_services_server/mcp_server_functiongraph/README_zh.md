# FunctionGraph MCP Server 

## 版本信息
v0.1.0

## 产品描述

FunctionGraph MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务FunctionGraph交互的能力。可以基于自然语言对FunctionGraph资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 函数依赖包 | CreateDependencyVersion | 创建依赖包版本 | To be tested |
|  | ShowDependencyVersion | 获取依赖包版本详情 | To be tested |
|  | ListDependencyVersion | 获取依赖包版本列表 | To be tested |
|  | ListDependencies | 获取依赖包列表 | To be tested |
|  | DeleteDependencyVersion | 删除依赖包版本 | To be tested |
| 函数导入导出 | ExportFunction | 导出函数 | To be tested |
|  | ImportFunction | 导入函数 | To be tested |
| 函数应用中心 | ListFunctionApplications | 查询应用程序列表(该功能目前仅支持华北-北京四、华东-上海一) | To be tested |
|  | CreateFunctionApp | 创建应用程序(该功能目前仅支持华北-北京四、华东-上海一) | To be tested |
|  | ShowAppTemplate | 查询应用程序模板详情(该功能目前仅支持华北-北京四、华东-上海一) | To be tested |
|  | ShowFunctionApp | 查询应用程序详情(该功能目前仅支持华北-北京四、华东-上海一) | To be tested |
|  | DeleteFunctionApp | 删除应用程序(该功能目前仅支持华北-北京四、华东-上海一) | To be tested |
|  | ListAppTemplates | 查询应用程序模板列表(该功能目前仅支持华北-北京四、华东-上海一) | To be tested |
| 函数异步配置 | ListActiveAsyncInvocations | 获取函数异步调用活跃请求列表 | To be tested |
|  | ListAsyncInvocations | 获取函数异步调用请求列表 | To be tested |
|  | ListFunctionAsyncInvokeConfig | 获取指定函数所有版本的异步配置列表。。 | To be tested |
|  | ShowFunctionAsyncInvokeConfig | 获取指定函数某一版本的异步配置信息。 | To be tested |
|  | CancelAsyncInvocation | -| 当前仅支持参数recursive为false且force为true的函数。 在1:N的函数做并发异步调用的场景下调用停止异步请求接口时,同一函数实例同时在执行的其他请求也会被一并停止并返回4208 function invocation canceled | To be tested |
|  | UpdateFunctionAsyncInvokeConfig | 设置函数异步配置信息。 | To be tested |
|  | DeleteFunctionAsyncInvokeConfig | 删除函数异步配置信息。 | To be tested |
| 函数指标 | ListStatistics | 租户函数统计信息。 | To be tested |
|  | ShowFunctionMetrics | 查询函数流量指标。 | To be tested |
|  | ListFunctionAsMetric | 按指定指标排序的函数列表。 | To be tested |
|  | ShowFuncReservedInstanceMetrics | 查询函数实例使用情况指标。 | To be tested |
|  | ListFunctionStatistics | 获取指定时间段的函数运行指标。 | To be tested |
| 函数日志 | ShowProjectAsyncStatusLogInfo | 查询异步日志详情 | To be tested |
|  | EnableAsyncStatusLog | 允许异步状态通知。 | To be tested |
|  | EnableLtsLogs | 开通lts日志上报功能。 | To be tested |
|  | ShowLtsLogDetails | 获取指定函数的lts日志组日志流配置。 | To be tested |
| 函数模板 | ShowFunctionTemplate | 获取指定函数模板 | To be tested |
|  | ListFunctionTemplate | 获取函数模板列表 | To be tested |
| 函数流 | BatchDeleteWorkflows | 删除函数流 | To be tested |
|  | ListWorkflow | 查询函数流 | To be tested |
|  | ShowTenantMetric | 获取函数流指标 | To be tested |
|  | ShowWorkflowExecution | 获取指定函数流执行实例。 | To be tested |
|  | CreateWorkflow | 创建函数流 | To be tested |
|  | ShowWorkflowExecutionForPage | 分页获取指定函数流执行实例列表 | To be tested |
|  | ShowWorkFlow | 获取指定函数流实例的元数据 | To be tested |
|  | ShowWorkFlowMetric | 获取指定函数流指标 | To be tested |
|  | StartSyncWorkflowExecution | 以同步执行方式启动函数流(仅快速模式函数流支持) | To be tested |
|  | CreateCallbackWorkflow | 回调工作流 | To be tested |
|  | StartWorkflowExecution | 以异步执行方式启动函数流 | To be tested |
|  | UpdateWorkFlow | 修改指定函数流实例的元数据 | To be tested |
|  | StopWorkFlow | 停止函数流 | To be tested |
|  | RetryWorkFlow | 重试函数流 | To be tested |
|  | ListWorkflowExecutions | 获取指定函数流执行实例列表 | To be tested |
| 函数测试事件 | ShowEvent | 获取测试事件详细信息 | To be tested |
|  | ListEvents | 获取指定函数的测试事件列表 | To be tested |
|  | CreateEvent | 创建测试事件 | To be tested |
|  | UpdateEvent | 更新测试事件详细信息 | To be tested |
|  | DeleteEvent | 删除指定测试事件 | To be tested |
| 函数版本别名 | UpdateVersionAlias | 修改函数版本别名信息。 | To be tested |
|  | CreateVersionAlias | 创建函数灰度版本别名。 | To be tested |
|  | ListFunctionVersions | 获取指定函数的版本列表。 | To be tested |
|  | DeleteVersionAlias | 删除函数版本别名。 | To be tested |
|  | CreateFunctionVersion | 发布函数版本。 | To be tested |
|  | ShowVersionAlias | 获取函数指定的版本别名信息。 | To be tested |
|  | ListVersionAliases | 获取函数版本别名列表。 | To be tested |
| 函数生命周期管理 | CreateVpcEndpoint | 创建下沉入口。(该功能目前仅支持华北-北京四、华东-上海一、华东-上海二、西南-贵阳一) | To be tested |
|  | ListFunctions | 获取函数列表 | To be tested |
|  | UpdateFuncSnapshot | 禁用/启动函数快照,仅支持java运行时函数,且为非latest版本才能开启函数快照功能。 | To be tested |
|  | CreateFunction | 创建指定的函数。 | To be tested |
|  | ListFunctionTags | 查询函数标签列表 | To be tested |
|  | UpdateFunctionMaxInstanceConfig | 更新函数最大实例数 | To be tested |
|  | CreateTags | 创建资源标签。 | To be tested |
|  | ListBridgeVersions | 获取servicebridge可用的版本 | To be tested |
|  | ShowProjectTagsList | 查询资源标签。 | To be tested |
|  | ShowFuncSnapshotState | 查询函数快照制作状态。 | To be tested |
|  | ShowResInstanceInfo | 查询资源实例。 | To be tested |
|  | ShowFunctionCode | 获取指定函数的代码。 | To be tested |
|  | DeleteVpcEndpoint | 删除下沉入口。(该功能目前仅支持华北-北京四、华东-上海一、华东-上海二、西南-贵阳一) | To be tested |
|  | UpdateFunctionCode | 修改指定的函数的代码。 | To be tested |
|  | DeleteFunction | 删除指定的函数或者特定的版本(不允许删除latest版本)。 | To be tested |
|  | ShowFunctionConfig | 获取指定函数的metadata。 | To be tested |
|  | UpdateFunctionConfig | 修改指定的函数的metadata信息。 | To be tested |
|  | ListBridgeFunctions | 获取指定函数绑定的servicebridge函数列表信息。 | To be tested |
|  | UpdateFunctionCollectState | 更新函数置顶状态 | To be tested |
|  | DeleteTags | 删除资源标签。 | To be tested |
| 函数触发器 | DeleteFunctionTrigger | 删除触发器。 | To be tested |
|  | BatchDeleteFunctionTriggers | 删除指定函数所有触发器设置。 | To be tested |
|  | ShowFunctionTrigger | 获取特定触发器的信息。 | To be tested |
|  | ListFunctionTriggers | 获取指定函数的所有触发器设置。 | To be tested |
|  | CreateFunctionTrigger | 创建触发器。 | To be tested |
|  | UpdateTrigger | 更新触发器 | To be tested |
| 函数调用 | InvokeFunction | 同步调用指的是客户端请求需要明确等到响应结果,也就是说这样的请求必须得调用到用户的函数,并且等到调用完成才返回。 | To be tested |
|  | AsyncInvokeFunction | 异步执行函数。 | To be tested |
| 函数调用链 | ShowTracing | 获取函数调用链配置 | To be tested |
|  | UpdateTracing | 修改函数调用链配置,开通/修改传入aksk,关闭aksk传空 | To be tested |
| 函数配额 | ListQuotas | 查询租户配额 | To be tested |
| 函数预留实例 | ListReservedInstanceConfigs | 获取函数预留实例配置列表 | To be tested |
|  | ListFunctionReservedInstances | 获取函数预留实例数量。 | To be tested |
|  | UpdateFunctionReservedInstancesCount | 修改函数预留实例数量。 | To be tested |
