# APM MCP Server 


## Version
v0.1.0

## Overview

APM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service APM. Full-chain management of APM resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AKSK | ShowAkSks | Query the AK/SK of a tenant. | To be tested |
|  | CreateAkSk | Create an AK/SK. | To be tested |
|  | DeleteAkSk | Delete the AK/SK. | To be tested |
| ALARM | ListAlarmNotify | Query the triggering details and history of a single alarm. | To be tested |
|  | ListAlarmData | Query alarms in the system. | To be tested |
| APM | ChangeAgentStatus | Changes the collection status of a specified instance, that is, enabled or disabled. | To be tested |
|  | ShowMasterAddress | Obtain the POLB address of the master service in the region based on the region name. | To be tested |
|  | DeleteAgent | Delete an agent | To be tested |
|  | SaveMonitorItemConfig | Save the monitoring item. | To be tested |
|  | ListEnvMonitorItem | Query the monitoring item list. | To be tested |
|  | ListAkSk | Obtain the AK/SK list created by the user. | To be tested |
|  | ListBusiness | This interface is used to query applications of a user. | To be tested |
|  | SearchAgent | This interface is used to search for all probes in an application. | To be tested |
|  | SearchApplication | Search for components, environments, and probes in a specified region. | To be tested |
| App Template Management | ListApps | Query the application template list | To be tested |
|  | DeleteApp | Delete an application template | To be tested |
| CMDB | ShowSubBusinessDetail | Query details about a single subapplication. | To be tested |
|  | ListAppEnvs | Obtain the environment list of the component. | To be tested |
|  | ListEnvTags | API for querying environment labels. | To be tested |
|  | ShowBusinessDetail | Query details about a single application. | To be tested |
|  | ShowTopologyTree | Obtain the application tree. | To be tested |
| Profiling | ShowFlameLineTree |  | To be tested |
| REGION | ListOpenRegion | This interface is used to query the information about the region enabled by a user. | To be tested |
|  | ListSupportedRegion | Query information about all supported regions. | To be tested |
| TOPOLOGY | SearchEnvTopology | Query the environment-level global topology information of a component. | To be tested |
|  | SearchBusinessTopology | Query application-level global topology information. | To be tested |
| TRACING | ShowToken | Obtain the token of the link trace application. | To be tested |
|  | CreateBusiness | Create a link trace application | To be tested |
|  | ShowAccessPoint | Obtain the access address of the link trace application | To be tested |
| TRANSACTION | SearchTransactionConfig | Query the configured URL tracing configuration list. | To be tested |
|  | ListBusinessEnv | Query the list of environments where URL tracing is enabled in the selected region. | To be tested |
|  | SearchTransaction | Query the list of invoked URL tracing views. | To be tested |
|  | ShowTransactionDetail | Query the details of a URL tracing view. | To be tested |
| VIEW | ShowEnvMonitorItems | Obtain monitoring item information. | To be tested |
|  | ShowRawTable | Obtain the original data table. | To be tested |
|  | ShowMonitorItemDetail | Obtains details about a monitoring item. | To be tested |
|  | ShowMonitorItemViewConfig | Query the configuration information about a monitoring item. | To be tested |
|  | ShowSpanSearch | Interface for querying span data. | To be tested |
|  | ShowTopology | Call chain topology. | To be tested |
|  | ShowClobDetail | Obtain raw data details. | To be tested |
|  | ListEnvInstances | Obtains the instance list. | To be tested |
|  | ShowTrend | Obtain the trend chart. | To be tested |
|  | ShowSumTable | Obtains summary table data. | To be tested |
|  | ShowTraceEvents | Obtains all call chain data of a trace. | To be tested |
|  | ShowEventDetail | Obtains details about an event. | To be tested |

