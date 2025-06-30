# FunctionGraph MCP Server 


## Version
v0.1.0

## Overview

FunctionGraph MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service FunctionGraph. Full-chain management of FunctionGraph resources can be carried out based on natural language.

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
                    <td rowspan="5">函数依赖包</td>
                    <td>CreateDependencyVersion</td>
                    <td>创建依赖包版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDependencyVersion</td>
                    <td>获取依赖包版本详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDependencyVersion</td>
                    <td>获取依赖包版本列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDependencies</td>
                    <td>获取依赖包列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDependencyVersion</td>
                    <td>删除依赖包版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">函数导入导出</td>
                    <td>ExportFunction</td>
                    <td>导出函数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportFunction</td>
                    <td>导入函数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">函数应用中心</td>
                    <td>ListFunctionApplications</td>
                    <td>查询应用程序列表(该功能目前仅支持华北-北京四、华东-上海一)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFunctionApp</td>
                    <td>创建应用程序(该功能目前仅支持华北-北京四、华东-上海一)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppTemplate</td>
                    <td>查询应用程序模板详情(该功能目前仅支持华北-北京四、华东-上海一)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFunctionApp</td>
                    <td>查询应用程序详情(该功能目前仅支持华北-北京四、华东-上海一)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFunctionApp</td>
                    <td>删除应用程序(该功能目前仅支持华北-北京四、华东-上海一)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppTemplates</td>
                    <td>查询应用程序模板列表(该功能目前仅支持华北-北京四、华东-上海一)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">函数异步配置</td>
                    <td>ListActiveAsyncInvocations</td>
                    <td>获取函数异步调用活跃请求列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAsyncInvocations</td>
                    <td>获取函数异步调用请求列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionAsyncInvokeConfig</td>
                    <td>获取指定函数所有版本的异步配置列表。。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFunctionAsyncInvokeConfig</td>
                    <td>获取指定函数某一版本的异步配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelAsyncInvocation</td>
                    <td>-| 当前仅支持参数recursive为false且force为true的函数。 在1:N的函数做并发异步调用的场景下调用停止异步请求接口时,同一函数实例同时在执行的其他请求也会被一并停止并返回4208 function invocation canceled</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunctionAsyncInvokeConfig</td>
                    <td>设置函数异步配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFunctionAsyncInvokeConfig</td>
                    <td>删除函数异步配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">函数指标</td>
                    <td>ShowFunctionMetrics</td>
                    <td>查询函数流量指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionAsMetric</td>
                    <td>按指定指标排序的函数列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFuncReservedInstanceMetrics</td>
                    <td>查询函数实例使用情况指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionStatistics</td>
                    <td>获取指定时间段的函数运行指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">函数日志</td>
                    <td>ShowProjectAsyncStatusLogInfo</td>
                    <td>查询异步日志详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableAsyncStatusLog</td>
                    <td>允许异步状态通知。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableLtsLogs</td>
                    <td>开通lts日志上报功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLtsLogDetails</td>
                    <td>获取指定函数的lts日志组日志流配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">函数模板</td>
                    <td>ShowFunctionTemplate</td>
                    <td>获取指定函数模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionTemplate</td>
                    <td>获取函数模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">函数流</td>
                    <td>BatchDeleteWorkflows</td>
                    <td>删除函数流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkflow</td>
                    <td>查询函数流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTenantMetric</td>
                    <td>获取函数流指标</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkflowExecution</td>
                    <td>获取指定函数流执行实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflow</td>
                    <td>创建函数流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkflowExecutionForPage</td>
                    <td>分页获取指定函数流执行实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkFlow</td>
                    <td>获取指定函数流实例的元数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkFlowMetric</td>
                    <td>获取指定函数流指标</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartSyncWorkflowExecution</td>
                    <td>以同步执行方式启动函数流(仅快速模式函数流支持)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCallbackWorkflow</td>
                    <td>回调工作流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartWorkflowExecution</td>
                    <td>以异步执行方式启动函数流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkFlow</td>
                    <td>修改指定函数流实例的元数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopWorkFlow</td>
                    <td>停止函数流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryWorkFlow</td>
                    <td>重试函数流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkflowExecutions</td>
                    <td>获取指定函数流执行实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">函数测试事件</td>
                    <td>ListEvents</td>
                    <td>获取指定函数的测试事件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEvent</td>
                    <td>创建测试事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEvent</td>
                    <td>更新测试事件详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEvent</td>
                    <td>删除指定测试事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">函数版本别名</td>
                    <td>UpdateVersionAlias</td>
                    <td>修改函数版本别名信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVersionAlias</td>
                    <td>创建函数灰度版本别名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionVersions</td>
                    <td>获取指定函数的版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVersionAlias</td>
                    <td>删除函数版本别名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFunctionVersion</td>
                    <td>发布函数版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVersionAlias</td>
                    <td>获取函数指定的版本别名信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVersionAliases</td>
                    <td>获取函数版本别名列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="19">函数生命周期管理</td>
                    <td>CreateVpcEndpoint</td>
                    <td>创建下沉入口。(该功能目前仅支持华北-北京四、华东-上海一、华东-上海二、西南-贵阳一)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctions</td>
                    <td>获取函数列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFuncSnapshot</td>
                    <td>禁用/启动函数快照,仅支持java运行时函数,且为非latest版本才能开启函数快照功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFunction</td>
                    <td>创建指定的函数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionTags</td>
                    <td>查询函数标签列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunctionMaxInstanceConfig</td>
                    <td>更新函数最大实例数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBridgeVersions</td>
                    <td>获取servicebridge可用的版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectTagsList</td>
                    <td>查询资源标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFuncSnapshotState</td>
                    <td>查询函数快照制作状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResInstanceInfo</td>
                    <td>查询资源实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFunctionCode</td>
                    <td>获取指定函数的代码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpcEndpoint</td>
                    <td>删除下沉入口。(该功能目前仅支持华北-北京四、华东-上海一、华东-上海二、西南-贵阳一)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunctionCode</td>
                    <td>修改指定的函数的代码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFunction</td>
                    <td>删除指定的函数或者特定的版本(不允许删除latest版本)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFunctionConfig</td>
                    <td>获取指定函数的metadata。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunctionConfig</td>
                    <td>修改指定的函数的metadata信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBridgeFunctions</td>
                    <td>获取指定函数绑定的servicebridge函数列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunctionCollectState</td>
                    <td>更新函数置顶状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTags</td>
                    <td>删除资源标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">函数触发器</td>
                    <td>DeleteFunctionTrigger</td>
                    <td>删除触发器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteFunctionTriggers</td>
                    <td>删除指定函数所有触发器设置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFunctionTrigger</td>
                    <td>获取特定触发器的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionTriggers</td>
                    <td>获取指定函数的所有触发器设置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFunctionTrigger</td>
                    <td>创建触发器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">函数调用</td>
                    <td>InvokeFunction</td>
                    <td>同步调用指的是客户端请求需要明确等到响应结果,也就是说这样的请求必须得调用到用户的函数,并且等到调用完成才返回。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AsyncInvokeFunction</td>
                    <td>异步执行函数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">函数调用链</td>
                    <td>ShowTracing</td>
                    <td>获取函数调用链配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTracing</td>
                    <td>修改函数调用链配置,开通/修改传入aksk,关闭aksk传空</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">函数预留实例</td>
                    <td>ListReservedInstanceConfigs</td>
                    <td>获取函数预留实例配置列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionReservedInstances</td>
                    <td>获取函数预留实例数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunctionReservedInstancesCount</td>
                    <td>修改函数预留实例数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">安全总览</td>
                    <td>ListStatistics</td>
                    <td>查询安全总览请求与攻击数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">标签管理</td>
                    <td>CreateTags</td>
                    <td>添加标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">触发器管理</td>
                    <td>UpdateTrigger</td>
                    <td>更新触发器配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额管理</td>
                    <td>ListQuotas</td>
                    <td>获取配额信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">防护事件管理</td>
                    <td>ShowEvent</td>
                    <td>查询指定事件id的防护事件详情</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
