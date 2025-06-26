# AOM MCP Server 


## Version
v0.1.0

## Overview

AOM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service AOM. Full-chain management of AOM resources can be carried out based on natural language.

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
                    <td rowspan="19">Alarm</td>
                    <td>PushEvents</td>
                    <td>This interface is used to report the events and alarms of the corresponding user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotifiedHistories</td>
                    <td>Obtain the alarm sending result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEventRule</td>
                    <td>Updates an event alarm rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetricOrEventAlarmRule</td>
                    <td>Query the AOM2.0 metric or event alarm rule list. (Note: Currently, the region where the API is opened is CN East-Shanghai1.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEvent2alarmRule</td>
                    <td>To delete an event alarm rule,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEvent2alarmRule</td>
                    <td>Query the event alarm rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddEvent2alarmRule</td>
                    <td>Add an event alarm rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMetricOrEventAlarmRule</td>
                    <td>This API is used to delete AOM2.0 metric or event alarm rules. (Note: Currently, the API is open to the region: CN East-Shanghai1.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListActionRule</td>
                    <td>Obtain the alarm action rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMuteRules</td>
                    <td>Delete a silence rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddMuteRules</td>
                    <td>Add a silence rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateActionRule</td>
                    <td>Modify an alarm action rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddActionRule</td>
                    <td>Add an alarm action rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteActionRule</td>
                    <td>Delete an alarm action rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMuteRule</td>
                    <td>Obtain the silence rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowActionRule</td>
                    <td>Obtain the alarm action rule based on the rule name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMuteRule</td>
                    <td>Modify the silence rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountEvents</td>
                    <td>This interface is used to collect statistics on events and alarms under specified conditions by segment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddOrUpdateMetricOrEventAlarmRule</td>
                    <td>Add or modify AOM2.0 metric or event alarm rules. (Note: Currently, the region where the API is opened is CN East-Shanghai1.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">App Template Management</td>
                    <td>DeleteApp</td>
                    <td>Delete an application template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">AppManagement</td>
                    <td>CreateApp</td>
                    <td>This interface is used by users to create application information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApp</td>
                    <td>This interface is used by users to modify application information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApp</td>
                    <td>This interface is used by users to query application details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Application Resource Management (AOM2.0 Interface)</td>
                    <td>ListResourceUnderNode</td>
                    <td>This API is used to query the list of resources bound to a node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnv</td>
                    <td>This interface is used to delete an environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnvByName</td>
                    <td>This interface is used to query environment details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnv</td>
                    <td>This interface is used to create an environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnv</td>
                    <td>This interface is used to modify the environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppByName</td>
                    <td>This API is used to query application details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubApp</td>
                    <td>This interface is used to modify a subapplication.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubApp</td>
                    <td>This interface is used to add a subapplication.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubApp</td>
                    <td>This interface is used to delete a subapplication.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowComponentByName</td>
                    <td>This API is used to query component details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnv</td>
                    <td>This interface is used to query environment details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Automatic O&amp;M</td>
                    <td>SearchTemplateById</td>
                    <td>This API is used to query execution scheme details based on the execution scheme ID. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplateByJobId</td>
                    <td>This interface can be used to query execution schemes by job ID and return the execution scheme list by page. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartPausingWorkflowExecutions</td>
                    <td>This interface is used to retry, skip, or suspend a task and return the operation result. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFastExecuteScript</td>
                    <td>This interface is used to create a quick script execution task. You can specify the script type, execution user, script parameters, execution host, and script content, and execute the script on the specified host. (Note: Currently, the region where the API is opened is CN East-Suzhou 201).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteWorkflow</td>
                    <td>This interface is used to deliver and execute a specified task. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllJobByName</td>
                    <td>This API is used to query created jobs. You can specify the job name and job creator to perform exact query and return the job list. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllVersionByVersionId</td>
                    <td>This interface is used to query all versions of a script with a specified ID and return the script version list. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkflowTriggerStatus</td>
                    <td>Updates the start and stop status of a scheduled task. You can start or stop a scheduled task and return the operation result. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchWorkflowExecutionDetail</td>
                    <td>This interface is used to obtain the execution details of a task. You can query the corresponding task by specifying the workflow ID and execution ID and return the task execution details. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllScriptByName</td>
                    <td>This interface is used to query the script home page. You can specify the script name and script creator to perform exact query and return the list data that contains basic script information. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopExecution</td>
                    <td>This interface is used to terminate a task that is being executed. The workflow ID and execution ID are specified to terminate the corresponding task and the termination status is returned. (Note: Currently, the APIs are available in the following regions: CN North-Beijing 4, CN East-Shanghai 1, CN East-Shanghai 2, and CN South-Guangzhou).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Component</td>
                    <td>CreateComponent</td>
                    <td>Create a component.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowComponent</td>
                    <td>Obtains component details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateComponent</td>
                    <td>Update the component.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteComponent</td>
                    <td>Delete a component.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Function Flow</td>
                    <td>ListWorkflowExecutions</td>
                    <td>Obtains the list of execution instances of a specified function flow.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflow</td>
                    <td>Create a function flow</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkflow</td>
                    <td>Query function flow</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Function test event</td>
                    <td>ListEvents</td>
                    <td>Obtain the test event list of a specified function</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Log</td>
                    <td>ListLogItems</td>
                    <td>This API is used to query logs by different dimensions (such as clusters, IP addresses, and applications). The query can be performed on multiple pages.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Monitoring</td>
                    <td>DeleteserviceDiscoveryRules</td>
                    <td>This API is used to delete a service discovery rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlarmRule</td>
                    <td>This API is used to query a single threshold rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceDiscoveryRules</td>
                    <td>This API is used to query existing service discovery rules in the system.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddMetricData</td>
                    <td>This interface is used to add one or more monitoring data records to the server.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlarmRule</td>
                    <td>This API is used to delete a threshold rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmRule</td>
                    <td>This API is used to query the threshold rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddOrUpdateServiceDiscoveryRules</td>
                    <td>This API is used to add or modify one or more service discovery rules. A maximum of 100 rules can be added to the same project ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSeries</td>
                    <td>This interface is used to query the list of time series that can be monitored by the system. The namespace, name, dimension, and resource ID of the time series can be specified. The format is resType_resId. Start position and maximum number of returned records for pagination query.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlarmRules</td>
                    <td>This interface is used to delete threshold rules in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetricItems</td>
                    <td>This API is used to query the list of metrics that can be monitored by the system. The metric namespace, metric name, dimension, and resource ID can be specified. The format is resType_resId. Start position and maximum number of returned records for pagination query.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetricsData</td>
                    <td>This API is used to query the monitoring data of metrics within a specified time range. You can specify the data dimension and data period to be queried by specifying parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlarmRule</td>
                    <td>This API is used to modify a threshold rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAlarmRule</td>
                    <td>This API is used to add a threshold rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSample</td>
                    <td>This API is used to query monitoring time series data within a specified time range. You can specify the data dimension and data period to be queried by using parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Permission</td>
                    <td>ListPermissions</td>
                    <td>Retrieves the shared resource permission list of the specified resource type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Prometheus Instance</td>
                    <td>DeletePromInstance</td>
                    <td>This API is used to uninstall a managed Prometheus instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRecordingRule</td>
                    <td>This API is used to create a pre-aggregation rule for a Prometheus instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePromInstance</td>
                    <td>This API is used to add a Prometheus instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccessCode</td>
                    <td>This API is used to obtain the call credential of a Prometheus instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPromInstance</td>
                    <td>This API is used to query Prometheus instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Prometheus Monitor</td>
                    <td>ListRangeQueryAomPromPost</td>
                    <td>This interface uses the POST method to query the calculation results returned by Prometheus Query Language (PromQL) within a specified period.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstantQueryAomPromPost</td>
                    <td>This interface uses the POST method to query the PromQL (Prometheus Query Language) calculation result at a specific time point.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetadataAomPromGet</td>
                    <td>This API is used to query the metadata of a sequence and sequence label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLabelsAomPromGet</td>
                    <td>This interface uses the GET method to obtain the tag name list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstantQueryAomPromGet</td>
                    <td>This interface uses the GET method to query the PromQL (Prometheus Query Language) calculation result at a specific time point.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLabelsAomPromPost</td>
                    <td>This API uses the POST method to obtain the tag name list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRangeQueryAomPromGet</td>
                    <td>This interface uses the GET method to query the calculation result returned by the Prometheus Query Language (PromQL) within a specified period.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLabelValuesAomPromGet</td>
                    <td>This API is used to query the list of time series with a specified tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Trusted Node Management</td>
                    <td>ListAgents</td>
                    <td>Function description: This API is used to obtain the list of trusted nodes. Supports fuzzy search by node name and confederation name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">UniAgent Management</td>
                    <td>BatchImportAgent</td>
                    <td>This interface is used to deliver UniAgent installation tasks in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgentInfos</td>
                    <td>This interface is used to query the list of hosts where the UniAgent installation task has been executed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateAgent</td>
                    <td>This interface is used to deliver UniAgent batch upgrade tasks.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
