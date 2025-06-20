# AOM MCP Server 


## Version
v0.1.0

## Overview

AOM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service AOM. Full-chain management of AOM resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Alarm | PushEvents | This interface is used to report the events and alarms of the corresponding user. | To be tested |
|  | ListNotifiedHistories | Obtain the alarm sending result. | To be tested |
|  | UpdateEventRule | Updates an event alarm rule. | To be tested |
|  | ListMetricOrEventAlarmRule | Query the AOM2.0 metric or event alarm rule list. (Note: Currently, the region where the API is opened is CN East-Shanghai1.) | To be tested |
|  | DeleteEvent2alarmRule | To delete an event alarm rule,  | To be tested |
|  | ListEvent2alarmRule | Query the event alarm rule list. | To be tested |
|  | AddEvent2alarmRule | Add an event alarm rule. | To be tested |
|  | DeleteMetricOrEventAlarmRule | This API is used to delete AOM2.0 metric or event alarm rules. (Note: Currently, the API is open to the region: CN East-Shanghai1.) | To be tested |
|  | ListActionRule | Obtain the alarm action rule list. | To be tested |
|  | DeleteMuteRules | Delete a silence rule. | To be tested |
|  | AddMuteRules | Add a silence rule. | To be tested |
|  | UpdateActionRule | Modify an alarm action rule. | To be tested |
|  | AddActionRule | Add an alarm action rule. | To be tested |
|  | DeleteActionRule | Delete an alarm action rule. | To be tested |
|  | ListMuteRule | Obtain the silence rule list. | To be tested |
|  | ShowActionRule | Obtain the alarm action rule based on the rule name. | To be tested |
|  | UpdateMuteRule | Modify the silence rule. | To be tested |
|  | CountEvents | This interface is used to collect statistics on events and alarms under specified conditions by segment. | To be tested |
|  | AddOrUpdateMetricOrEventAlarmRule | Add or modify AOM2.0 metric or event alarm rules. (Note: Currently, the region where the API is opened is CN East-Shanghai1.) | To be tested |
| App Template Management | DeleteApp | Delete an application template | To be tested |
| AppManagement | CreateApp | This interface is used by users to create application information. | To be tested |
|  | UpdateApp | This interface is used by users to modify application information. | To be tested |
|  | ShowApp | This interface is used by users to query application details. | To be tested |
| Application Resource Management (AOM2.0 Interface) | ListResourceUnderNode | This API is used to query the list of resources bound to a node. | To be tested |
|  | DeleteEnv | This interface is used to delete an environment. | To be tested |
|  | ShowEnvByName | This interface is used to query environment details. | To be tested |
|  | CreateEnv | This interface is used to create an environment. | To be tested |
|  | UpdateEnv | This interface is used to modify the environment. | To be tested |
|  | ShowAppByName | This API is used to query application details. | To be tested |
|  | UpdateSubApp | This interface is used to modify a subapplication. | To be tested |
|  | CreateSubApp | This interface is used to add a subapplication. | To be tested |
|  | DeleteSubApp | This interface is used to delete a subapplication. | To be tested |
|  | ShowComponentByName | This API is used to query component details. | To be tested |
|  | ShowEnv | This interface is used to query environment details. | To be tested |
| Automatic O&M | SearchTemplateById | This API is used to query execution scheme details based on the execution scheme ID. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou). | To be tested |
|  | ListTemplateByJobId | This interface can be used to query execution schemes by job ID and return the execution scheme list by page. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou). | To be tested |
|  | StartPausingWorkflowExecutions | This interface is used to retry, skip, or suspend a task and return the operation result. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou). | To be tested |
|  | CreateFastExecuteScript | This interface is used to create a quick script execution task. You can specify the script type, execution user, script parameters, execution host, and script content, and execute the script on the specified host. (Note: Currently, the region where the API is opened is CN East-Suzhou 201). | To be tested |
|  | ExecuteWorkflow | This interface is used to deliver and execute a specified task. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou). | To be tested |
|  | ListAllJobByName | This API is used to query created jobs. You can specify the job name and job creator to perform exact query and return the job list. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou). | To be tested |
|  | ListAllVersionByVersionId | This interface is used to query all versions of a script with a specified ID and return the script version list. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou). | To be tested |
|  | UpdateWorkflowTriggerStatus | Updates the start and stop status of a scheduled task. You can start or stop a scheduled task and return the operation result. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou). | To be tested |
|  | SearchWorkflowExecutionDetail | This interface is used to obtain the execution details of a task. You can query the corresponding task by specifying the workflow ID and execution ID and return the task execution details. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou). | To be tested |
|  | ListAllScriptByName | This interface is used to query the script home page. You can specify the script name and script creator to perform exact query and return the list data that contains basic script information. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou). | To be tested |
|  | StopExecution | This interface is used to terminate a task that is being executed. The workflow ID and execution ID are specified to terminate the corresponding task and the termination status is returned. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou). | To be tested |
| Component | CreateComponent | Create a component. | To be tested |
|  | ShowComponent | Obtains component details. | To be tested |
|  | UpdateComponent | Update the component. | To be tested |
|  | DeleteComponent | Delete a component. | To be tested |
| Function Flow | ListWorkflowExecutions | Obtains the list of execution instances of a specified function flow. | To be tested |
|  | CreateWorkflow | Create a function flow | To be tested |
|  | ListWorkflow | Query function flow | To be tested |
| Function test event | ListEvents | Obtain the test event list of a specified function | To be tested |
| Log | ListLogItems | This API is used to query logs by different dimensions (such as clusters, IP addresses, and applications). The query can be performed on multiple pages. | To be tested |
| Monitoring | DeleteserviceDiscoveryRules | This API is used to delete a service discovery rule. | To be tested |
|  | ShowAlarmRule | This API is used to query a single threshold rule. | To be tested |
|  | ListServiceDiscoveryRules | This API is used to query existing service discovery rules in the system. | To be tested |
|  | AddMetricData | This interface is used to add one or more monitoring data records to the server. | To be tested |
|  | DeleteAlarmRule | This API is used to delete a threshold rule. | To be tested |
|  | ListAlarmRule | This API is used to query the threshold rule list. | To be tested |
|  | AddOrUpdateServiceDiscoveryRules | This API is used to add or modify one or more service discovery rules. A maximum of 100 rules can be added to the same project ID. | To be tested |
|  | ListSeries | This interface is used to query the list of time series that can be monitored by the system. The namespace, name, dimension, and resource ID of the time series can be specified. The format is resType_resId. Start position and maximum number of returned records for pagination query. | To be tested |
|  | DeleteAlarmRules | This interface is used to delete threshold rules in batches. | To be tested |
|  | ListMetricItems | This API is used to query the list of metrics that can be monitored by the system. The metric namespace, metric name, dimension, and resource ID can be specified. The format is resType_resId. Start position and maximum number of returned records for pagination query. | To be tested |
|  | ShowMetricsData | This API is used to query the monitoring data of metrics within a specified time range. You can specify the data dimension and data period to be queried by specifying parameters. | To be tested |
|  | UpdateAlarmRule | This API is used to modify a threshold rule. | To be tested |
|  | AddAlarmRule | This API is used to add a threshold rule. | To be tested |
|  | ListSample | This API is used to query monitoring time series data within a specified time range. You can specify the data dimension and data period to be queried by using parameters. | To be tested |
| Permission | ListPermissions | Retrieves the shared resource permission list of the specified resource type. | To be tested |
| Prometheus Instance | DeletePromInstance | This API is used to uninstall a managed Prometheus instance. | To be tested |
|  | CreateRecordingRule | This API is used to create a pre-aggregation rule for a Prometheus instance. | To be tested |
|  | CreatePromInstance | This API is used to add a Prometheus instance. | To be tested |
|  | ListAccessCode | This API is used to obtain the call credential of a Prometheus instance. | To be tested |
|  | ListPromInstance | This API is used to query Prometheus instances. | To be tested |
| Prometheus Monitor | ListRangeQueryAomPromPost | This interface uses the POST method to query the calculation results returned by Prometheus Query Language (PromQL) within a specified period. | To be tested |
|  | ListInstantQueryAomPromPost | This interface uses the POST method to query the PromQL (Prometheus Query Language) calculation result at a specific time point. | To be tested |
|  | ListMetadataAomPromGet | This API is used to query the metadata of a sequence and sequence label. | To be tested |
|  | ListLabelsAomPromGet | This interface uses the GET method to obtain the tag name list. | To be tested |
|  | ListInstantQueryAomPromGet | This interface uses the GET method to query the PromQL (Prometheus Query Language) calculation result at a specific time point. | To be tested |
|  | ListLabelsAomPromPost | This API uses the POST method to obtain the tag name list. | To be tested |
|  | ListRangeQueryAomPromGet | This interface uses the GET method to query the calculation result returned by the Prometheus Query Language (PromQL) within a specified period. | To be tested |
|  | ListLabelValuesAomPromGet | This API is used to query the list of time series with a specified tag. | To be tested |
| Trusted Node Management | ListAgents | Function description: This API is used to obtain the list of trusted nodes. Supports fuzzy search by node name and confederation name. | To be tested |
| UniAgent Management | BatchImportAgent | This interface is used to deliver UniAgent installation tasks in batches. | To be tested |
|  | ShowAgentInfos | This interface is used to query the list of hosts where the UniAgent installation task has been executed. | To be tested |
|  | BatchUpdateAgent | This interface is used to deliver UniAgent batch upgrade tasks. | To be tested |

