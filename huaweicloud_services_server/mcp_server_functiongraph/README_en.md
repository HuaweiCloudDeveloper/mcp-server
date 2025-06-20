# FunctionGraph MCP Server 


## Version
v0.1.0

## Overview

FunctionGraph MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service FunctionGraph. Full-chain management of FunctionGraph resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Function Application Center | ListFunctionApplications | Query the application list. (Currently, this function is available only in CN North-Beijing 4 and CN East-Shanghai 1.) | To be tested |
|  | CreateFunctionApp | Create an application. (Currently, this function is available only in CN North-Beijing 4 and CN East-Shanghai 1.) | To be tested |
|  | ShowAppTemplate | Query application template details. (Currently, this function is available only in CN North-Beijing 4 and CN East-Shanghai 1.) | To be tested |
|  | ShowFunctionApp | Query application details. (Currently, this function is available only in CN North-Beijing 4 and CN East-Shanghai 1.) | To be tested |
|  | DeleteFunctionApp | Delete an application. (Currently, this function is available only in CN North-Beijing 4 and CN East-Shanghai 1.) | To be tested |
|  | ListAppTemplates | Query the application template list. (Only CN North-Beijing 4 and CN East-Shanghai 1 are supported.) | To be tested |
| Function Asynchronous Configuration | ListActiveAsyncInvocations | Obtain the list of active asynchronous function invoking requests. | To be tested |
|  | ListAsyncInvocations | Obtain the list of asynchronous function invoking requests. | To be tested |
|  | ListFunctionAsyncInvokeConfig | Obtains the asynchronous configuration list of all versions of a specified function. | To be tested |
|  | ShowFunctionAsyncInvokeConfig | Obtains the asynchronous configuration information of a specified function version. | To be tested |
|  | CancelAsyncInvocation | -|Currently, only functions whose recursive and force are false and true are supported. When the API for stopping asynchronous requests is invoked in the scenario where 1:N functions are concurrently invoked, other requests that are being executed by the same function instance will be stopped and 4208 function invocation canceled is returned. | To be tested |
|  | UpdateFunctionAsyncInvokeConfig | Sets the asynchronous function configuration information. | To be tested |
|  | DeleteFunctionAsyncInvokeConfig | Delete the asynchronous function configuration information. | To be tested |
| Function Call | InvokeFunction | Synchronous invoking indicates that a client request needs to wait for the response result. That is, such a request must invoke a user function and return a response only after the invoking is complete. | To be tested |
|  | AsyncInvokeFunction | Execute the function asynchronously. | To be tested |
| Function Call Chain | ShowTracing | Obtain the function call chain configuration. | To be tested |
|  | UpdateTracing | Modify the function call chain configuration. Enable or modify the function call chain configuration. Transfer the AK/S and leave the AK/S blank. | To be tested |
| Function Dependency Package | CreateDependencyVersion | Create a dependency package version | To be tested |
|  | ShowDependencyVersion | Obtain the dependency package version details | To be tested |
|  | ListDependencyVersion | Obtain the dependency package version list | To be tested |
|  | ListDependencies | Obtain the dependency package list | To be tested |
|  | DeleteDependencyVersion | Delete the dependency package version | To be tested |
| Function Flow | BatchDeleteWorkflows | Delete a function flow | To be tested |
|  | ListWorkflow | Query function flow | To be tested |
|  | ShowTenantMetric | Obtain function flow metrics | To be tested |
|  | ShowWorkflowExecution | Obtains the execution instance of a specified function flow. | To be tested |
|  | CreateWorkflow | Create a function flow | To be tested |
|  | ShowWorkflowExecutionForPage | Obtain the execution instance list of a specified function flow by page. | To be tested |
|  | ShowWorkFlow | Obtain the metadata of a specified function flow instance | To be tested |
|  | ShowWorkFlowMetric | Obtains a specified function flow metric | To be tested |
|  | StartSyncWorkflowExecution | Start the function flow in synchronous execution mode (supported only by the function flow in quick mode) | To be tested |
|  | CreateCallbackWorkflow | Callback workflow | To be tested |
|  | StartWorkflowExecution | Start the function flow in asynchronous execution mode | To be tested |
|  | UpdateWorkFlow | Modifies the metadata of a specified function flow instance. | To be tested |
|  | StopWorkFlow | Stop the function flow | To be tested |
|  | RetryWorkFlow | Retry the function flow | To be tested |
|  | ListWorkflowExecutions | Obtains the list of execution instances of a specified function flow. | To be tested |
| Function Indicator | ShowFunctionMetrics | Query the function traffic metrics. | To be tested |
|  | ListFunctionAsMetric | List of functions sorted by the specified indicator. | To be tested |
|  | ShowFuncReservedInstanceMetrics | Query the function instance usage metrics. | To be tested |
|  | ListFunctionStatistics | Obtain the function running metrics in a specified period. | To be tested |
| Function Lifecycle Management | CreateVpcEndpoint | Create a sinking entry. (This function is supported only by CN North-Beijing 4, CN East-Shanghai1, CN East-Shanghai2, and Southwest-Guiyang1). | To be tested |
|  | ListFunctions | Obtain the function list | To be tested |
|  | UpdateFuncSnapshot | Disable or enable the function snapshot function. The function snapshot function can be enabled only when the Java runtime function is not the latest version. | To be tested |
|  | CreateFunction | Creates the specified function. | To be tested |
|  | ListFunctionTags | Query the function tag list | To be tested |
|  | UpdateFunctionMaxInstanceConfig | Updating the maximum number of function instances | To be tested |
|  | ListBridgeVersions | Obtain the available version of the servicebridge | To be tested |
|  | ShowProjectTagsList | Query resource tags. | To be tested |
|  | ShowFuncSnapshotState | Query the function snapshot creation status. | To be tested |
|  | ShowResInstanceInfo | Query resource instances. | To be tested |
|  | ShowFunctionCode | Obtains the code of a specified function. | To be tested |
|  | DeleteVpcEndpoint | Delete the sinking entry. (This function is supported only by CN North-Beijing 4, CN East-Shanghai1, CN East-Shanghai2, and Southwest-Guiyang1). | To be tested |
|  | UpdateFunctionCode | Modifies the code of a specified function. | To be tested |
|  | DeleteFunction | Delete the specified function or version. The latest version cannot be deleted. | To be tested |
|  | ShowFunctionConfig | Obtains the metadata of a specified function. | To be tested |
|  | UpdateFunctionConfig | Modifies the metadata of a specified function. | To be tested |
|  | ListBridgeFunctions | Obtains the list of servicebridge functions bound to a specified function. | To be tested |
|  | UpdateFunctionCollectState | Update the pinning status of a function | To be tested |
|  | DeleteTags | Delete a resource tag. | To be tested |
| Function Log | ShowProjectAsyncStatusLogInfo | Query asynchronous log details | To be tested |
|  | EnableAsyncStatusLog | Asynchronous status notification is allowed. | To be tested |
|  | EnableLtsLogs | Enable the lts log reporting function. | To be tested |
|  | ShowLtsLogDetails | Obtains the log stream configuration of the lts log group of a specified function. | To be tested |
| Function Template | ShowFunctionTemplate | Obtain a specified function template | To be tested |
|  | ListFunctionTemplate | Obtain the function template list | To be tested |
| Function Trigger | DeleteFunctionTrigger | Delete a trigger. | To be tested |
|  | BatchDeleteFunctionTriggers | Deletes all trigger settings of a specified function. | To be tested |
|  | ShowFunctionTrigger | Obtain the information about a specific trigger. | To be tested |
|  | ListFunctionTriggers | Obtains all trigger settings of a specified function. | To be tested |
|  | CreateFunctionTrigger | Create a trigger. | To be tested |
| Function import and export | ExportFunction | Export function | To be tested |
|  | ImportFunction | Import function | To be tested |
| Function test event | ListEvents | Obtain the test event list of a specified function | To be tested |
|  | CreateEvent | Create a test event | To be tested |
|  | UpdateEvent | Updating the details of a test event | To be tested |
|  | DeleteEvent | Delete a specified test event | To be tested |
| Function version alias | UpdateVersionAlias | Modifies the alias information of the function version. | To be tested |
|  | CreateVersionAlias | Create the alias of the gray version of the function. | To be tested |
|  | ListFunctionVersions | Obtains the version list of a specified function. | To be tested |
|  | DeleteVersionAlias | Delete the alias of a function version. | To be tested |
|  | CreateFunctionVersion | Release the function version. | To be tested |
|  | ShowVersionAlias | Obtains the version alias information specified by a function. | To be tested |
|  | ListVersionAliases | Obtains the alias list of function versions. | To be tested |
| Protection Event Management | ShowEvent | Query the details of a protection event with a specified ID. | To be tested |
| Quota Management | ListQuotas | Obtain quota information | To be tested |
| Reserved function instance | ListReservedInstanceConfigs | Obtain the configuration list of function reserved instances | To be tested |
|  | ListFunctionReservedInstances | Obtains the number of function reserved instances. | To be tested |
|  | UpdateFunctionReservedInstancesCount | Change the number of reserved function instances. | To be tested |
| Security Overview | ListStatistics | Query the number of security overview requests and attacks. | To be tested |
| Tag Management | CreateTags | Add a tag | To be tested |
| Trigger Management | UpdateTrigger | Update trigger configuration | To be tested |

