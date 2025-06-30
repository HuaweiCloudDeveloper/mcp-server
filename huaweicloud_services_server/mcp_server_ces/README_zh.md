# CES MCP Server 


## Version
v0.1.0

## Overview

CES MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CES. Full-chain management of CES resources can be carried out based on natural language.

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
                    <td rowspan="2">Agent任务相关接口</td>
                    <td>BatchCreateAgentInvocations</td>
                    <td>批量创建Agent任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgentInvocations</td>
                    <td>查询Agent任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">一键告警</td>
                    <td>ListOneClickAlarms</td>
                    <td>查询一键告警列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOneClickAlarm</td>
                    <td>创建一键告警</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOneClickAlarmNotifications</td>
                    <td>批量修改开启状态的一键告警关联告警规则的告警通知</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteOneClickAlarms</td>
                    <td>批量删除一键告警</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOneClickAlarmRules</td>
                    <td>查询一键告警关联告警规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateOneClickAlarmPoliciesEnabledState</td>
                    <td>批量修改一键告警关联告警规则策略的启用状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateOneClickAlarmsEnabledState</td>
                    <td>批量修改一键告警关联告警规则的启用状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">主机监控</td>
                    <td>ListMetrics</td>
                    <td>查询集群使用指标列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">事件监控</td>
                    <td>CreateEvents</td>
                    <td>上报自定义事件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventDetail</td>
                    <td>根据事件监控名称,查询该事件发生的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">函数测试事件</td>
                    <td>ListEvents</td>
                    <td>获取指定函数的测试事件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">告警模板</td>
                    <td>ListAlarmTemplates</td>
                    <td>查询告警模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAlarmTemplates</td>
                    <td>批量删除自定义告警模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlarmTemplate</td>
                    <td>创建自定义告警模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlarmTemplate</td>
                    <td>查询告警模板详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlarmTemplate</td>
                    <td>修改自定义告警模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">告警模板关联告警规则</td>
                    <td>ListAlarmTemplateAssociationAlarms</td>
                    <td>查询告警模板关联的告警规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">告警策略</td>
                    <td>UpdateAlarmRulePolicies</td>
                    <td>修改告警规则策略(全量修改)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmRulePolicies</td>
                    <td>根据告警规则ID查询策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">告警规则</td>
                    <td>BatchEnableAlarmRules</td>
                    <td>批量启停告警规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmRules</td>
                    <td>查询告警规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAlarmRules</td>
                    <td>批量删除告警规则V2接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlarmRules</td>
                    <td>创建告警规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">告警规则管理</td>
                    <td>ListAlarms</td>
                    <td>查询告警规则列表,可以指定分页条件限制结果数量,可以指定排序规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlarm</td>
                    <td>创建一条告警规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlarm</td>
                    <td>删除一条告警规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlarm</td>
                    <td>根据告警ID查询告警规则信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlarmTemplate</td>
                    <td>根据ID删除自定义告警模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlarmAction</td>
                    <td>启动或停止一条告警规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlarm</td>
                    <td>修改告警规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">告警记录</td>
                    <td>ListAlarmHistories</td>
                    <td>查询告警记录列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">告警资源</td>
                    <td>ListAlarmRuleResources</td>
                    <td>根据告警规则ID查询告警规则资源列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlarmRuleResources</td>
                    <td>批量删除告警规则资源(资源分组类型的告警规则不支持),资源分组类型的修改请使用资源分组管理相关接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAlarmRuleResources</td>
                    <td>批量增加告警规则资源(资源分组类型的告警规则不支持),资源分组类型的修改请使用资源分组管理相关接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">告警通知</td>
                    <td>UpdateAlarmNotifications</td>
                    <td>修改告警规则告警通知信息,告警策略&amp;资源请使用对应接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">告警通知屏蔽</td>
                    <td>BatchUpdateNotificationMaskTime</td>
                    <td>批量修改告警通知屏蔽规则的屏蔽时间</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotificationMasks</td>
                    <td>批量查询指定类型的通知屏蔽规则,目前最多支持100个通知屏蔽规则的批量查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteNotificationMasks</td>
                    <td>批量删除告警通知屏蔽规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateNotificationMasks</td>
                    <td>批量设置告警通知屏蔽规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNotificationMask</td>
                    <td>修改告警通知屏蔽规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotificationMaskResources</td>
                    <td>查询告警通知屏蔽资源列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">指标管理</td>
                    <td>ListAgentDimensionInfo</td>
                    <td>根据ECS/BMS资源ID查询磁盘、挂载点、进程、显卡、RAID控制器维度指标信息;维度NPU已经为原始值,不需要调用该接口进行额外查询获取指标信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">插件状态查询</td>
                    <td>ListAgentStatus</td>
                    <td>插件状态查询,包括uniagent状态以及插件状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">监控数据管理</td>
                    <td>BatchListMetricData</td>
                    <td>批量查询指定时间范围内指定指标的指定粒度的监控数据,目前最多支持500指标的批量查询。 对于不同的period取值和查询的指标数量,默认的最大查询区间(to-from)不同。 规则为"指标数量*(to-from)/监控周期&lt;=3000",若超出阈值,会自动调整from以满足规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMetricData</td>
                    <td>添加一条或多条指标监控数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEventData</td>
                    <td>查询指定时间范围指定事件类型的主机配置数据,可以通过参数指定需要查询的数据维度。注意:该接口提供给HANA场景下SAP Monitor查询主机配置数据,其他场景下查不到主机配置数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetricData</td>
                    <td>查询指定时间范围指定指标的指定粒度的监控数据,可以通过参数指定需要查询的数据维度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">监控看板</td>
                    <td>DeleteDashboards</td>
                    <td>批量删除监控看板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDashboard</td>
                    <td>修改监控看板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDashboardInfos</td>
                    <td>查询监控看板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOneDashboard</td>
                    <td>创建/复制监控看板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">监控视图</td>
                    <td>ListDashboardWidgets</td>
                    <td>查询指定监控看板下的监控视图列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWidget</td>
                    <td>查询指定监控视图信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateWidgets</td>
                    <td>批量更新监控视图</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDashboardWidgets</td>
                    <td>创建/复制/批量创建监控视图到指定的监控看板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOneWidget</td>
                    <td>删除指定监控视图</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">资源分组</td>
                    <td>BatchDeleteResourceGroups</td>
                    <td>批量删除资源分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceGroups</td>
                    <td>查询资源分组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResourceGroup</td>
                    <td>修改资源分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResourceGroupAssociationAlarmTemplate</td>
                    <td>提交资源分组批量关联自定义告警模板异步任务,由异步任务覆盖性创建告警规则。每个用户创建处于待执行状态的异步任务数量上限为100个,单个资源分组仅可有1个未完成的任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResourceGroup</td>
                    <td>创建资源分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceGroup</td>
                    <td>查询指定资源分组详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">资源分组关联资源</td>
                    <td>ListResourceGroupsServicesResources</td>
                    <td>查询资源分组下指定服务类别特定维度的资源列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteResources</td>
                    <td>给自定义资源分组,即类型为手动添加的资源分组,批量删除关联资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateResources</td>
                    <td>给自定义资源分组,即类型为手动添加的资源分组,批量增加关联资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">资源分组管理</td>
                    <td>DeleteResourceGroup</td>
                    <td>删除一条资源分组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceGroup</td>
                    <td>查询所创建的所有资源分组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资源标签管理</td>
                    <td>ListCesTargetProjectTags</td>
                    <td>查询CES指定项目指定资源类型标签列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowQuotas</td>
                    <td>查询当前项目下资源配额情况。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
