# CES MCP Server 


## Version
v0.1.0

## Overview

CES MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CES. Full-chain management of CES resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Agent task-related interfaces | BatchCreateAgentInvocations | Create Agent Tasks in Batches | To be tested |
|  | ListAgentInvocations | Querying the Agent Task List | To be tested |
| Alarm Policy | UpdateAlarmRulePolicies | Modifying an alarm rule policy (full modification) | To be tested |
|  | ListAlarmRulePolicies | Query the policy list based on the alarm rule ID. | To be tested |
| Alarm Record | ListAlarmHistories | Query the alarm list | To be tested |
| Alarm Rule | BatchEnableAlarmRules | Start or stop alarm rules in batches | To be tested |
|  | ListAlarmRules | Query the alarm rule list | To be tested |
|  | BatchDeleteAlarmRules | V2 interface for deleting alarm rules in batches | To be tested |
|  | CreateAlarmRules | Create an alarm rule | To be tested |
| Alarm Rule Management | ListAlarms | Query the alarm rule list. You can specify the pagination condition to limit the number of results and specify the sorting rule. | To be tested |
|  | CreateAlarm | Create an alarm rule. | To be tested |
|  | DeleteAlarm | Delete an alarm rule. | To be tested |
|  | ShowAlarm | Query alarm rule information based on the alarm ID. | To be tested |
|  | DeleteAlarmTemplate | Delete a user-defined alarm template by ID. | To be tested |
|  | UpdateAlarmAction | Starts or stops an alarm rule. | To be tested |
|  | UpdateAlarm | Modify an alarm rule. | To be tested |
| Alarm notification | UpdateAlarmNotifications | Modify the alarm notification information about an alarm rule. Use the corresponding APIs for alarm policies and resources. | To be tested |
| Alarm notification masking | BatchUpdateNotificationMaskTime | Modifying the masking time of alarm notification masking rules in batches | To be tested |
|  | ListNotificationMasks | Query notification masking rules of a specified type in batches. Currently, a maximum of 100 notification masking rules can be queried in batches. | To be tested |
|  | BatchDeleteNotificationMasks | Delete alarm notification masking rules in batches | To be tested |
|  | BatchUpdateNotificationMasks | Set alarm notification masking rules in batches | To be tested |
|  | UpdateNotificationMask | Modifying an alarm notification masking rule | To be tested |
|  | ListNotificationMaskResources | Query the alarm notification masking resource list | To be tested |
| Alarm resource | ListAlarmRuleResources | Query the alarm rule resource list based on the alarm rule ID | To be tested |
|  | DeleteAlarmRuleResources | Delete alarm rule resources in batches (alarm rules of resource groups are not supported). To modify the resource group type, use the resource group management API. | To be tested |
|  | AddAlarmRuleResources | Adding alarm rule resources in batches (not supported by resource group alarm rules). To modify the resource group type, use the resource group management API. | To be tested |
| Alarm template | ListAlarmTemplates | Query the alarm template list | To be tested |
|  | BatchDeleteAlarmTemplates | Delete user-defined alarm templates in batches | To be tested |
|  | CreateAlarmTemplate | Create a custom alarm template | To be tested |
|  | ShowAlarmTemplate | Query alarm template details | To be tested |
|  | UpdateAlarmTemplate | Modifying a user-defined alarm template | To be tested |
| Alarm template association rule | ListAlarmTemplateAssociationAlarms | Query the list of alarm rules associated with an alarm template | To be tested |
| Event Monitoring | CreateEvents | Report a customized event. | To be tested |
|  | ListEventDetail | Query details about an event by event name. | To be tested |
| Function test event | ListEvents | Obtain the test event list of a specified function | To be tested |
| Host monitoring | ListMetrics | Query the cluster usage indicator list. | To be tested |
| KPI Management | ListAgentDimensionInfo | Query the disk, mount point, process, graphics card, and RAID controller metrics based on the ECS/BMS resource ID. The dimension NPU is the original value. You do not need to invoke this API to obtain the indicator information. | To be tested |
| Monitoring Dashboard | DeleteDashboards | Delete monitoring dashboards in batches | To be tested |
|  | UpdateDashboard | Modifying a monitoring dashboard | To be tested |
|  | ListDashboardInfos | Query the monitoring dashboard list | To be tested |
|  | CreateOneDashboard | Creating or Copying a Monitoring Dashboard | To be tested |
| Monitoring Data Management | BatchListMetricData | Query monitoring data of a specified metric in a specified period of time. Currently, a maximum of 500 metrics can be queried in batches. The default maximum query interval (to-from) varies depending on the period value and the number of queried KQIs/KPIs. | To be tested |
|  | CreateMetricData | Add one or more metrics monitoring data records. | To be tested |
|  | ShowEventData | Query the host configuration data of a specified event type within a specified time period. You can specify the data dimension to be queried by specifying the parameter. Note: This API is used by SAP Monitor to query host configuration data in HANA scenarios. In other scenarios, host configuration data cannot be queried. | To be tested |
|  | ShowMetricData | Query the monitoring data of a specified metric in a specified period of time and at a specified granularity. You can specify the data dimension to be queried by specifying the parameter. | To be tested |
| Monitoring View | ListDashboardWidgets | Query the monitoring view list in a specified monitoring dashboard | To be tested |
|  | ShowWidget | Query information about a specified monitoring view | To be tested |
|  | BatchUpdateWidgets | Update monitoring views in batches | To be tested |
|  | CreateDashboardWidgets | Creating, copying, or batch creating monitoring views to a specified monitoring dashboard | To be tested |
|  | DeleteOneWidget | Delete a specified monitoring view | To be tested |
| One-click alarm | ListOneClickAlarms | Query one-click alarm list | To be tested |
|  | CreateOneClickAlarm | Create one-click alarm | To be tested |
|  | UpdateOneClickAlarmNotifications | Modifying alarm notifications for enabled one-click alarm correlation rules in batches | To be tested |
|  | BatchDeleteOneClickAlarms | Delete alarms in batches by one click | To be tested |
|  | ListOneClickAlarmRules | Query the list of associated alarm rules for one-click alarms | To be tested |
|  | BatchUpdateOneClickAlarmPoliciesEnabledState | Modifying the enabling status of one-click alarm correlation rule policies in batches | To be tested |
|  | BatchUpdateOneClickAlarmsEnabledState | Modifying the enabling status of one-click alarm correlation rules in batches | To be tested |
| Query plug-in status | ListAgentStatus | Query the plug-in status, including the UniAgent status and plug-in status | To be tested |
| Quota | ShowQuotas | Query the resource quota of the current project. | To be tested |
| Resource Tag Management | ListCesTargetProjectTags | Query the tag list of a specified resource type in a specified project. | To be tested |
| Resource group | BatchDeleteResourceGroups | Delete resource groups in batches | To be tested |
|  | ListResourceGroups | Query the resource group list | To be tested |
|  | UpdateResourceGroup | Modifying a resource group | To be tested |
|  | UpdateResourceGroupAssociationAlarmTemplate | Submit an asynchronous task for associating resource groups with a customized alarm template in batches. The asynchronous task will overwrite the alarm rule creation. A maximum of 100 asynchronous tasks can be created by a user and a resource group can have only one unfinished task.  | To be tested |
|  | CreateResourceGroup | Create a resource group | To be tested |
|  | ShowResourceGroup | Query the details of a specified resource group | To be tested |
| Resource group management | DeleteResourceGroup | Delete a resource group. | To be tested |
|  | ListResourceGroup | Query all created resource groups. | To be tested |
| Resources associated with resource groups | ListResourceGroupsServicesResources | Query the resource list of a specified service type in a resource group by a specific dimension. | To be tested |
|  | BatchDeleteResources | Delete associated resources in batches from a user-defined resource group, that is, manually added resource groups. | To be tested |
|  | BatchCreateResources | Add associated resources in batches to the customized resource group, that is, the resource group whose type is manually added. | To be tested |

