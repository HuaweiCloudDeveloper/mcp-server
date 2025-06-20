# SA MCP Server 


## Version
v0.1.0

## Overview

SA MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SA. Full-chain management of SA resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

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
| Alerts | ChangeAlert | Edit the alarm and update the alarm based on the actual attribute modification. Columns that are not modified are not updated. | To be tested |
|  | ShowAlert | Obtain alarm details | To be tested |
|  | CreateAlert | Create alarm | To be tested |
|  | DeleteAlert | Delete an alarm | To be tested |
|  | CreateBatchOrderAlerts | Converting an alarm to an event | To be tested |
|  | ListAlerts | Searching for alarms | To be tested |
| Event management | ImportEvents | A maximum of 50 data records can be reported in batches. | To be tested |
| Incidents | CreateIncident | Create Event | To be tested |
|  | DeleteIncident | Create Event | To be tested |
|  | ListIncidents | Search event list | To be tested |
|  | ShowIncident | Obtain event details | To be tested |
|  | ListIncidentTypes | Obtain the event type list | To be tested |
|  | ChangeIncident | Edit the event. Update the attribute based on the actual modification. Columns that are not modified are not updated. | To be tested |
| Indicator | ShowIndicatorDetail | Query indicator details (only CN East-Shanghai1) | To be tested |
|  | CreateIndicator | Create an indicator (only CN East-Shanghai1) | To be tested |
|  | UpdateIndicator | Update metrics (only CN East-Shanghai1) | To be tested |
|  | DeleteIndicator | Delete an indicator (only for CN East-Shanghai1) | To be tested |
|  | ListIndicators | List all indicators | To be tested |
| Playbook | ListPlaybooks | List all playbooks. | To be tested |
|  | ShowPlaybookStatistics | Screenplay statistics | To be tested |
|  | DeletePlaybook | Delete playbook. | To be tested |
|  | ShowPlaybookMonitors | Monitoring script running | To be tested |
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
| Product Management | CheckProductHealthy | The SA provides the heartbeat interface. Integration products send heartbeat packets to the situational awareness at a scheduled time (every 5 minutes) to check whether the path between integration products and SA is normal. | To be tested |
| Relation | ListDataobjectRelation | List Dataobject Relation | To be tested |
|  | CreateDataobjectRelation | Create Dataobject Relation | To be tested |
|  | DeleteDataobjectRelation | Delete Dataobject Relation | To be tested |

