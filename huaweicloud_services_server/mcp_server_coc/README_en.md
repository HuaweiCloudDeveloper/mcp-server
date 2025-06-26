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
                    <td rowspan="1">Application operation</td>
                    <td>ListApplications</td>
                    <td>Query the application platform list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">CustomEventMessageIntegration</td>
                    <td>CreateReportCustomEvent</td>
                    <td>Tenants can integrate their self-developed monitoring systems into the COC according to the standard format. After the integration, alarms will be reported to the COC alarm center in the standard format.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">DocumentManagement</td>
                    <td>UpdateDocument</td>
                    <td>Modifying a custom job</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDocument</td>
                    <td>Delete a user-defined job</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDocument</td>
                    <td>Create a custom job</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDocumentAtomics</td>
                    <td>Obtain the atomic capability list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDocuments</td>
                    <td>Query the list of customized jobs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteDocument</td>
                    <td>Executing a Customized Job</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetDocument</td>
                    <td>Query the details of a customized job</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetDocumentAtomicInfo</td>
                    <td>Obtain atom capability details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">EventMessageIntegration</td>
                    <td>CreateReportPrometheusEvent</td>
                    <td>Prometheus Event Access</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">ExecutionManagement</td>
                    <td>OperateExecution</td>
                    <td>Operation work order</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListExecutionSteps</td>
                    <td>Query the details about the work order step</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetExecution</td>
                    <td>Query job details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListExecutions</td>
                    <td>Query the work order list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListExecutionInstances</td>
                    <td>Query the batch instance of the work order step, for example, the ECS instance in the script batch operation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">ExternalCocIncident</td>
                    <td>ShowCocIncidentDetail</td>
                    <td>ShowCocIncidentDetail Get Event Ticket Details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>HandleCocIncident</td>
                    <td>HandleCocIncident processing event ticket</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCocTicketOperationHistories</td>
                    <td>ListCocTicketOperationHistories Get event ticket history</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCocIncident</td>
                    <td>CreateExternalIncident Creates an event ticket</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ExternalCocIssues</td>
                    <td>ShowCocIssuesDetail</td>
                    <td>ShowCocIssuesDetail Get Event Ticket Details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCocIssues</td>
                    <td>CreateExternalIssues Create a trouble ticket</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ListAuthorizableTicketsExternal</td>
                    <td>ListAuthorizableTicketsExternal</td>
                    <td>Query the COC list of authorized orders. (Change No., Event No., Warroom, and Alarm)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Resource Tag</td>
                    <td>ListResource</td>
                    <td>Filter resources by tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ResourceTagManagement</td>
                    <td>UpdateResourceTags</td>
                    <td>Update resource tags</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScriptResourceTags</td>
                    <td>Query the resource tag list</td>
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
                    <td rowspan="5">Script-related API</td>
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
                    <td rowspan="6">ScriptExecutionManagement</td>
                    <td>ListScriptJobBatches</td>
                    <td>Query: batch list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetScriptJobBatch</td>
                    <td>Query: This API is used to obtain the instance list in a batch by page.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScriptJobs</td>
                    <td>Query the work order list by page.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>OperateScriptJob</td>
                    <td>Operation type: canceling an instance, skipping a batch, canceling the entire work order, suspending the entire work order, and continuing the entire work order</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetScriptJobInfo</td>
                    <td>Query execution: basic information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetScriptJobStatistics</td>
                    <td>Query: Instance status statistics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">ScriptManagement</td>
                    <td>GetScript</td>
                    <td>Obtain script details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesBatch</td>
                    <td>Obtain the batching result based on the batching policy. Only automatic batching is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckScriptRisk</td>
                    <td>Assess job risks based on job content and returns related analysis results and information. The results are for reference only.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AcceptScript</td>
                    <td>Function: Approve the script.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ScriptPublicManagement</td>
                    <td>GetPublicScript</td>
                    <td>Displays public script details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecutePublicScript</td>
                    <td>Execute the public script</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublicScripts</td>
                    <td>Obtain the public script list. Pagination logic: Use limit+marker mode to improve pagination efficiency. Use the auto-increment ID as the marker parameter.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">WarRoom</td>
                    <td>ListWarRooms</td>
                    <td>Query the WarRoom information list in the tenant zone</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWarRoom</td>
                    <td>Create a WarRoom in the tenant zone</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">application-model</td>
                    <td>ListApplicationModel</td>
                    <td>Query the sub-application, component, and group of the next level</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">applicationview</td>
                    <td>BatchCreateApplicationView</td>
                    <td>Creating Application Views in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">compliant</td>
                    <td>ListInstanceCompliant</td>
                    <td>Obtain node compliance reports by page</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstancePatchItems</td>
                    <td>Obtain node patch details by page</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">multipleCloud</td>
                    <td>ListMultiCloudResources</td>
                    <td>Querying the resources of a user in the cloud vendor</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">resource</td>
                    <td>CountMultiResources</td>
                    <td>Query the total number of resources of a user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncResource</td>
                    <td>Synchronize all user resources from the RMS</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
