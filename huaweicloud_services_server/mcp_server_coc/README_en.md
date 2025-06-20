# COC MCP Server 


## Version
v0.1.0

## Overview

COC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service COC. Full-chain management of COC resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Application operation | ListApplications | Query the application platform list. | To be tested |
| CustomEventMessageIntegration | CreateReportCustomEvent | Tenants can integrate their self-developed monitoring systems into the COC according to the standard format. After the integration, alarms will be reported to the COC alarm center in the standard format. | To be tested |
| DocumentManagement | UpdateDocument | Modifying a custom job | To be tested |
|  | DeleteDocument | Delete a user-defined job | To be tested |
|  | CreateDocument | Create a custom job | To be tested |
|  | ListDocumentAtomics | Obtain the atomic capability list | To be tested |
|  | ListDocuments | Query the list of customized jobs | To be tested |
|  | ExecuteDocument | Executing a Customized Job | To be tested |
|  | GetDocument | Query the details of a customized job | To be tested |
|  | GetDocumentAtomicInfo | Obtain atom capability details | To be tested |
| EventMessageIntegration | CreateReportPrometheusEvent | Prometheus Event Access | To be tested |
| ExecutionManagement | OperateExecution | Operation work order | To be tested |
|  | ListExecutionSteps | Query the details about the work order step | To be tested |
|  | GetExecution | Query job details | To be tested |
|  | ListExecutions | Query the work order list | To be tested |
|  | ListExecutionInstances | Query the batch instance of the work order step, for example, the ECS instance in the script batch operation. | To be tested |
| ExternalCocIncident | ShowCocIncidentDetail | ShowCocIncidentDetail Get Event Ticket Details | To be tested |
|  | HandleCocIncident | HandleCocIncident processing event ticket | To be tested |
|  | ListCocTicketOperationHistories | ListCocTicketOperationHistories Get event ticket history | To be tested |
|  | CreateCocIncident | CreateExternalIncident Creates an event ticket | To be tested |
| ExternalCocIssues | ShowCocIssuesDetail | ShowCocIssuesDetail Get Event Ticket Details | To be tested |
|  | CreateCocIssues | CreateExternalIssues Create a trouble ticket | To be tested |
| ListAuthorizableTicketsExternal | ListAuthorizableTicketsExternal | Query the COC list of authorized orders. (Change No., Event No., Warroom, and Alarm) | To be tested |
| Resource Tag | ListResource | Filter resources by tag. | To be tested |
| ResourceTagManagement | UpdateResourceTags | Update resource tags | To be tested |
|  | ListScriptResourceTags | Query the resource tag list | To be tested |
| ScheduledTask | EnableScheduledTask | Enable scheduled task by id | To be tested |
|  | ShowScheduledTask | Get ScheduledTask info by id | To be tested |
|  | ListScheduledTask | Get ScheduledTask infos | To be tested |
|  | UpdateScheduledTask | Update ScheduledTask | To be tested |
|  | DisableScheduledTask | Disable scheduled task by id | To be tested |
|  | CreateScheduledTask | Create Scheduled Task | To be tested |
|  | DeleteScheduledTask | Delete scheduled task by id | To be tested |
|  | ListScheduledTaskHistory | get scheduled task history list | To be tested |
| Script-related API | UpdateScript |  | To be tested |
|  | DeleteScript |  | To be tested |
|  | CreateScript |  | To be tested |
|  | ExecuteScript |  | To be tested |
|  | ListScripts |  | To be tested |
| ScriptExecutionManagement | ListScriptJobBatches | Query: batch list | To be tested |
|  | GetScriptJobBatch | Query: This API is used to obtain the instance list in a batch by page. | To be tested |
|  | ListScriptJobs | Query the work order list by page. | To be tested |
|  | OperateScriptJob | Operation type: canceling an instance, skipping a batch, canceling the entire work order, suspending the entire work order, and continuing the entire work order | To be tested |
|  | GetScriptJobInfo | Query execution: basic information | To be tested |
|  | GetScriptJobStatistics | Query: Instance status statistics. | To be tested |
| ScriptManagement | GetScript | Obtain script details | To be tested |
|  | ListInstancesBatch | Obtain the batching result based on the batching policy. Only automatic batching is supported. | To be tested |
|  | CheckScriptRisk | Assess job risks based on job content and returns related analysis results and information. The results are for reference only. | To be tested |
|  | AcceptScript | Function: Approve the script. | To be tested |
| ScriptPublicManagement | GetPublicScript | Displays public script details. | To be tested |
|  | ExecutePublicScript | Execute the public script | To be tested |
|  | ListPublicScripts | Obtain the public script list. Pagination logic: Use limit+marker mode to improve pagination efficiency. Use the auto-increment ID as the marker parameter. | To be tested |
| WarRoom | ListWarRooms | Query the WarRoom information list in the tenant zone | To be tested |
|  | CreateWarRoom | Create a WarRoom in the tenant zone | To be tested |
| application-model | ListApplicationModel | Query the sub-application, component, and group of the next level | To be tested |
| applicationview | BatchCreateApplicationView | Creating Application Views in Batches | To be tested |
| compliant | ListInstanceCompliant | Obtain node compliance reports by page | To be tested |
|  | ShowInstancePatchItems | Obtain node patch details by page | To be tested |
| multipleCloud | ListMultiCloudResources | Querying the resources of a user in the cloud vendor | To be tested |
| resource | CountMultiResources | Query the total number of resources of a user | To be tested |
|  | SyncResource | Synchronize all user resources from the RMS | To be tested |

