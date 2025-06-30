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
                    <td rowspan="2">Agent task-related interfaces</td>
                    <td>BatchCreateAgentInvocations</td>
                    <td>Create Agent Tasks in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgentInvocations</td>
                    <td>Querying the Agent Task List</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Alarm Policy</td>
                    <td>UpdateAlarmRulePolicies</td>
                    <td>Modifying an alarm rule policy (full modification)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmRulePolicies</td>
                    <td>Query the policy list based on the alarm rule ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Alarm Record</td>
                    <td>ListAlarmHistories</td>
                    <td>Query the alarm list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Alarm Rule</td>
                    <td>BatchEnableAlarmRules</td>
                    <td>Start or stop alarm rules in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmRules</td>
                    <td>Query the alarm rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAlarmRules</td>
                    <td>V2 interface for deleting alarm rules in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlarmRules</td>
                    <td>Create an alarm rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Alarm Rule Management</td>
                    <td>ListAlarms</td>
                    <td>Query the alarm rule list. You can specify the pagination condition to limit the number of results and specify the sorting rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlarm</td>
                    <td>Create an alarm rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlarm</td>
                    <td>Delete an alarm rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlarm</td>
                    <td>Query alarm rule information based on the alarm ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlarmTemplate</td>
                    <td>Delete a user-defined alarm template by ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlarmAction</td>
                    <td>Starts or stops an alarm rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlarm</td>
                    <td>Modify an alarm rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Alarm notification</td>
                    <td>UpdateAlarmNotifications</td>
                    <td>Modify the alarm notification information about an alarm rule. Use the corresponding APIs for alarm policies and resources.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Alarm notification masking</td>
                    <td>BatchUpdateNotificationMaskTime</td>
                    <td>Modifying the masking time of alarm notification masking rules in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotificationMasks</td>
                    <td>Query notification masking rules of a specified type in batches. Currently, a maximum of 100 notification masking rules can be queried in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteNotificationMasks</td>
                    <td>Delete alarm notification masking rules in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateNotificationMasks</td>
                    <td>Set alarm notification masking rules in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNotificationMask</td>
                    <td>Modifying an alarm notification masking rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotificationMaskResources</td>
                    <td>Query the alarm notification masking resource list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Alarm resource</td>
                    <td>ListAlarmRuleResources</td>
                    <td>Query the alarm rule resource list based on the alarm rule ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlarmRuleResources</td>
                    <td>Delete alarm rule resources in batches (alarm rules of resource groups are not supported). To modify the resource group type, use the resource group management API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAlarmRuleResources</td>
                    <td>Adding alarm rule resources in batches (not supported by resource group alarm rules). To modify the resource group type, use the resource group management API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Alarm template</td>
                    <td>ListAlarmTemplates</td>
                    <td>Query the alarm template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAlarmTemplates</td>
                    <td>Delete user-defined alarm templates in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlarmTemplate</td>
                    <td>Create a custom alarm template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlarmTemplate</td>
                    <td>Query alarm template details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlarmTemplate</td>
                    <td>Modifying a user-defined alarm template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Alarm template association rule</td>
                    <td>ListAlarmTemplateAssociationAlarms</td>
                    <td>Query the list of alarm rules associated with an alarm template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Event Monitoring</td>
                    <td>CreateEvents</td>
                    <td>Report a customized event.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventDetail</td>
                    <td>Query details about an event by event name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Function test event</td>
                    <td>ListEvents</td>
                    <td>Obtain the test event list of a specified function</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Host monitoring</td>
                    <td>ListMetrics</td>
                    <td>Query the cluster usage indicator list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">KPI Management</td>
                    <td>ListAgentDimensionInfo</td>
                    <td>Query the disk, mount point, process, graphics card, and RAID controller metrics based on the ECS/BMS resource ID. The dimension NPU is the original value. You do not need to invoke this API to obtain the indicator information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Monitoring Dashboard</td>
                    <td>DeleteDashboards</td>
                    <td>Delete monitoring dashboards in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDashboard</td>
                    <td>Modifying a monitoring dashboard</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDashboardInfos</td>
                    <td>Query the monitoring dashboard list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOneDashboard</td>
                    <td>Creating or Copying a Monitoring Dashboard</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Monitoring Data Management</td>
                    <td>BatchListMetricData</td>
                    <td>Query monitoring data of a specified metric in a specified period of time. Currently, a maximum of 500 metrics can be queried in batches. The default maximum query interval (to-from) varies depending on the period value and the number of queried KQIs/KPIs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMetricData</td>
                    <td>Add one or more metrics monitoring data records.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEventData</td>
                    <td>Query the host configuration data of a specified event type within a specified time period. You can specify the data dimension to be queried by specifying the parameter. Note: This API is used by SAP Monitor to query host configuration data in HANA scenarios. In other scenarios, host configuration data cannot be queried.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetricData</td>
                    <td>Query the monitoring data of a specified metric in a specified period of time and at a specified granularity. You can specify the data dimension to be queried by specifying the parameter.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Monitoring View</td>
                    <td>ListDashboardWidgets</td>
                    <td>Query the monitoring view list in a specified monitoring dashboard</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWidget</td>
                    <td>Query information about a specified monitoring view</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateWidgets</td>
                    <td>Update monitoring views in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDashboardWidgets</td>
                    <td>Creating, copying, or batch creating monitoring views to a specified monitoring dashboard</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOneWidget</td>
                    <td>Delete a specified monitoring view</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">One-click alarm</td>
                    <td>ListOneClickAlarms</td>
                    <td>Query one-click alarm list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOneClickAlarm</td>
                    <td>Create one-click alarm</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOneClickAlarmNotifications</td>
                    <td>Modifying alarm notifications for enabled one-click alarm correlation rules in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteOneClickAlarms</td>
                    <td>Delete alarms in batches by one click</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOneClickAlarmRules</td>
                    <td>Query the list of associated alarm rules for one-click alarms</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateOneClickAlarmPoliciesEnabledState</td>
                    <td>Modifying the enabling status of one-click alarm correlation rule policies in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateOneClickAlarmsEnabledState</td>
                    <td>Modifying the enabling status of one-click alarm correlation rules in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query plug-in status</td>
                    <td>ListAgentStatus</td>
                    <td>Query the plug-in status, including the UniAgent status and plug-in status</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowQuotas</td>
                    <td>Query the resource quota of the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Resource Tag Management</td>
                    <td>ListCesTargetProjectTags</td>
                    <td>Query the tag list of a specified resource type in a specified project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Resource group</td>
                    <td>BatchDeleteResourceGroups</td>
                    <td>Delete resource groups in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceGroups</td>
                    <td>Query the resource group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResourceGroup</td>
                    <td>Modifying a resource group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResourceGroupAssociationAlarmTemplate</td>
                    <td>Submit an asynchronous task for associating resource groups with a customized alarm template in batches. The asynchronous task will overwrite the alarm rule creation. A maximum of 100 asynchronous tasks can be created by a user and a resource group can have only one unfinished task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResourceGroup</td>
                    <td>Create a resource group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceGroup</td>
                    <td>Query the details of a specified resource group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Resource group management</td>
                    <td>DeleteResourceGroup</td>
                    <td>Delete a resource group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceGroup</td>
                    <td>Query all created resource groups.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Resources associated with resource groups</td>
                    <td>ListResourceGroupsServicesResources</td>
                    <td>Query the resource list of a specified service type in a resource group by a specific dimension.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteResources</td>
                    <td>Delete associated resources in batches from a user-defined resource group, that is, manually added resource groups.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateResources</td>
                    <td>Add associated resources in batches to the customized resource group, that is, the resource group whose type is manually added.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
