# SA MCP Server 


## Version
v0.1.0

## Overview

SA MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SA. Full-chain management of SA resources can be carried out based on natural language.

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
                    <td rowspan="11">AlertRules</td>
                    <td>EnableAlertRule</td>
                    <td>Enable alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlertRuleSimulation</td>
                    <td>Simulate alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlertRules</td>
                    <td>List alert rules</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlertRuleTemplate</td>
                    <td>List alert rule templates</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlertRule</td>
                    <td>Delete alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableAlertRule</td>
                    <td>Disable alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlertRule</td>
                    <td>Get alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlertRule</td>
                    <td>Create alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlertRuleTemplates</td>
                    <td>List alert rule templates</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlertRuleMetrics</td>
                    <td>List alert rule metrics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlertRule</td>
                    <td>Update alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Alerts</td>
                    <td>ChangeAlert</td>
                    <td>编辑告警,根据实际修改的属性更新,未修改的列不更新</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlert</td>
                    <td>获取告警详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlert</td>
                    <td>创建告警</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlert</td>
                    <td>删除告警</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBatchOrderAlerts</td>
                    <td>告警转事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlerts</td>
                    <td>搜索告警列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Incidents</td>
                    <td>CreateIncident</td>
                    <td>创建事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIncident</td>
                    <td>创建事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIncidents</td>
                    <td>搜索事件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIncident</td>
                    <td>获取事件详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIncidentTypes</td>
                    <td>获取事件的类型列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeIncident</td>
                    <td>编辑事件,根据实际修改的属性更新,未修改的列不更新</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Indicator</td>
                    <td>ShowIndicatorDetail</td>
                    <td>查询指标详情(仅支持华东-上海一使用)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIndicator</td>
                    <td>创建指标(仅支持华东-上海一使用)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIndicator</td>
                    <td>更新指标(仅支持华东-上海一使用)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIndicator</td>
                    <td>删除指标(仅支持华东-上海一使用)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIndicators</td>
                    <td>List all indicators</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Playbook</td>
                    <td>ListPlaybooks</td>
                    <td>List all playbooks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlaybookStatistics</td>
                    <td>剧本统计数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePlaybook</td>
                    <td>Delete playbook.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlaybookMonitors</td>
                    <td>剧本运行监控</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlaybook</td>
                    <td>Show playbook</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePlaybook</td>
                    <td>Update playbook.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlaybook</td>
                    <td>Create playbook.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Playbook action</td>
                    <td>UpdatePlaybookAction</td>
                    <td>Update action.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlaybookActions</td>
                    <td>List all actions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlaybookAction</td>
                    <td>Create action.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePlaybookAction</td>
                    <td>Delete action.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Playbook approve</td>
                    <td>ListPlaybookApproves</td>
                    <td>List approves.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlaybookApprove</td>
                    <td>Create playbook approve.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Playbook instance</td>
                    <td>ShowPlaybookInstance</td>
                    <td>Show playbook instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlaybookTopology</td>
                    <td>Show playbook Topology</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlaybookAuditLogs</td>
                    <td>List audit logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangePlaybookInstance</td>
                    <td>Operation Playbook Instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlaybookInstances</td>
                    <td>List playbook instances</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Playbook rule</td>
                    <td>UpdatePlaybookRule</td>
                    <td>Update rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlaybookRule</td>
                    <td>Create rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePlaybookRule</td>
                    <td>Delete rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlaybookRule</td>
                    <td>Show rule formation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Playbook version</td>
                    <td>UpdatePlaybookVersion</td>
                    <td>Update playbook version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlaybookVersion</td>
                    <td>Create playbook version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlaybookVersion</td>
                    <td>Show playbook version version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlaybookVersions</td>
                    <td>List all versions of playbook.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePlaybookVersion</td>
                    <td>Delete playbook version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyPlaybookVersion</td>
                    <td>Copy Playbook and version to a new one</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Relation</td>
                    <td>ListDataobjectRelation</td>
                    <td>List Dataobject Relation</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataobjectRelation</td>
                    <td>Create Dataobject Relation</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDataobjectRelation</td>
                    <td>Delete Dataobject Relation</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">事件管理</td>
                    <td>ImportEvents</td>
                    <td>批量数据上报,每批次最多不超过50条。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">产品管理</td>
                    <td>CheckProductHealthy</td>
                    <td>SA提供心跳接口,集成产品定时(每五分钟)发送心跳报文到态势感知,用来确认集成产品与态势感知之间的通路是否健康。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
