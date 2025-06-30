# COC MCP Server 


## Version
v0.1.0

## Overview

COC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service COC. Full-chain management of COC resources can be carried out based on natural language.

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
                    <td rowspan="1">Application操作</td>
                    <td>ListApplications</td>
                    <td>查询应用平台列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">CustomEventMessageIntegration</td>
                    <td>CreateReportCustomEvent</td>
                    <td>支持租户将自开发的监控系统按照标准化集成至COC,集成后告警会按照标准格式上报至COC告警中心</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">DocumentManagement</td>
                    <td>UpdateDocument</td>
                    <td>修改自定义作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDocument</td>
                    <td>删除自定义作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDocument</td>
                    <td>创建自定义作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDocumentAtomics</td>
                    <td>获取原子能力列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDocuments</td>
                    <td>查询自定义作业列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteDocument</td>
                    <td>执行自定义作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetDocument</td>
                    <td>查询自定义作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetDocumentAtomicInfo</td>
                    <td>获取原子能力详细</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">EventMessageIntegration</td>
                    <td>CreateReportPrometheusEvent</td>
                    <td>Prometheus事件接入</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">ExecutionManagement</td>
                    <td>OperateExecution</td>
                    <td>操作工单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListExecutionSteps</td>
                    <td>查询工单步骤详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetExecution</td>
                    <td>查询作业工单详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListExecutions</td>
                    <td>查询作业工单列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListExecutionInstances</td>
                    <td>查询工单步骤批次实例,如脚本分批操作里的ECS实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">ExternalCocIncident</td>
                    <td>ShowCocIncidentDetail</td>
                    <td>ShowCocIncidentDetail 获取事件单详细</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>HandleCocIncident</td>
                    <td>HandleCocIncident 处理事件单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCocTicketOperationHistories</td>
                    <td>ListCocTicketOperationHistories 获取事件单历史</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCocIncident</td>
                    <td>CreateExternalIncident 创建事件单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ExternalCocIssues</td>
                    <td>ShowCocIssuesDetail</td>
                    <td>ShowCocIssuesDetail 获取事件单详细</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCocIssues</td>
                    <td>CreateExternalIssues 创建问题单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ListAuthorizableTicketsExternal</td>
                    <td>ListAuthorizableTicketsExternal</td>
                    <td>查询COC可授权单列表(变更单号、事件单号、warroom和告警)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ResourceTagManagement</td>
                    <td>UpdateResourceTags</td>
                    <td>更新资源标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScriptResourceTags</td>
                    <td>查询资源标签列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">ScheduledTask</td>
                    <td>EnableScheduledTask</td>
                    <td>Enable scheduled task by id</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScheduledTask</td>
                    <td>Get ScheduledTask info by id</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScheduledTask</td>
                    <td>Get ScheduledTask infos</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateScheduledTask</td>
                    <td>Update ScheduledTask</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableScheduledTask</td>
                    <td>Disable scheduled task by id</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScheduledTask</td>
                    <td>Create Scheduled Task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScheduledTask</td>
                    <td>Delete scheduled task by id</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScheduledTaskHistory</td>
                    <td>get scheduled task history list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">ScriptExecutionManagement</td>
                    <td>ListScriptJobBatches</td>
                    <td>查询:批次列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetScriptJobBatch</td>
                    <td>查询:批次详情,分页获取批次中的实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScriptJobs</td>
                    <td>查询作业工单列表,分页查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>OperateScriptJob</td>
                    <td>操作类型:取消实例、跳过批次、取消整个工单、暂停整个工单、继续整个工单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetScriptJobInfo</td>
                    <td>查询执行:基本信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetScriptJobStatistics</td>
                    <td>查询:实例状态统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">ScriptManagement</td>
                    <td>GetScript</td>
                    <td>获取脚本详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesBatch</td>
                    <td>根据分批策略获取分批结果,只支持自动分批:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckScriptRisk</td>
                    <td>根据作业内容,对作业评估风险,返回相关分析的结果和信息,结果仅供参考。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AcceptScript</td>
                    <td>功能:审批脚本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ScriptPublicManagement</td>
                    <td>GetPublicScript</td>
                    <td>展示公共脚本详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecutePublicScript</td>
                    <td>执行公共脚本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublicScripts</td>
                    <td>获取公共脚本列表,分页逻辑:采用limit+marker方式,提高分页效率。用自增id作为marker参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">WarRoom</td>
                    <td>ListWarRooms</td>
                    <td>查询租户区WarRoom信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWarRoom</td>
                    <td>创建租户区WarRoom</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">application-model</td>
                    <td>ListApplicationModel</td>
                    <td>查询下一级的子应用、组件、分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">applicationview</td>
                    <td>BatchCreateApplicationView</td>
                    <td>批量创建应用视图</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">compliant</td>
                    <td>ListInstanceCompliant</td>
                    <td>分页获取节点合规性报告</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstancePatchItems</td>
                    <td>分页获取节点补丁详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">multipleCloud</td>
                    <td>ListMultiCloudResources</td>
                    <td>查询用户在云厂商中的资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">resource</td>
                    <td>CountMultiResources</td>
                    <td>查询用户各种资源总数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncResource</td>
                    <td>从RMS同步用户所有资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">脚本相关的API</td>
                    <td>UpdateScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScripts</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资源标签</td>
                    <td>ListResource</td>
                    <td>根据标签过滤资源。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
