# FunctionGraph MCP Server 


## Version
v0.1.0

## Overview

FunctionGraph MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service FunctionGraph. Full-chain management of FunctionGraph resources can be carried out based on natural language.

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
                    <td rowspan="6">Function Application Center</td>
                    <td>ListFunctionApplications</td>
                    <td>Query the application list. (Currently, this function is available only in CN North-Beijing 4 and CN East-Shanghai 1.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFunctionApp</td>
                    <td>Create an application. (Currently, this function is available only in CN North-Beijing 4 and CN East-Shanghai 1.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppTemplate</td>
                    <td>Query application template details. (Currently, this function is available only in CN North-Beijing 4 and CN East-Shanghai 1.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFunctionApp</td>
                    <td>Query application details. (Currently, this function is available only in CN North-Beijing 4 and CN East-Shanghai 1.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFunctionApp</td>
                    <td>Delete an application. (Currently, this function is available only in CN North-Beijing 4 and CN East-Shanghai 1.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppTemplates</td>
                    <td>Query the application template list. (Only CN North-Beijing 4 and CN East-Shanghai 1 are supported.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Function Asynchronous Configuration</td>
                    <td>ListActiveAsyncInvocations</td>
                    <td>Obtain the list of active asynchronous function invoking requests.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAsyncInvocations</td>
                    <td>Obtain the list of asynchronous function invoking requests.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionAsyncInvokeConfig</td>
                    <td>Obtains the asynchronous configuration list of all versions of a specified function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFunctionAsyncInvokeConfig</td>
                    <td>Obtains the asynchronous configuration information of a specified function version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelAsyncInvocation</td>
                    <td>-|Currently, only functions whose recursive and force are false and true are supported. When the API for stopping asynchronous requests is invoked in the scenario where 1:N functions are concurrently invoked, other requests that are being executed by the same function instance will be stopped and 4208 function invocation canceled is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunctionAsyncInvokeConfig</td>
                    <td>Sets the asynchronous function configuration information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFunctionAsyncInvokeConfig</td>
                    <td>Delete the asynchronous function configuration information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Function Call</td>
                    <td>InvokeFunction</td>
                    <td>Synchronous invoking indicates that a client request needs to wait for the response result. That is, such a request must invoke a user function and return a response only after the invoking is complete.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AsyncInvokeFunction</td>
                    <td>Execute the function asynchronously.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Function Call Chain</td>
                    <td>ShowTracing</td>
                    <td>Obtain the function call chain configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTracing</td>
                    <td>Modify the function call chain configuration. Enable or modify the function call chain configuration. Transfer the AK/S and leave the AK/S blank.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Function Dependency Package</td>
                    <td>CreateDependencyVersion</td>
                    <td>Create a dependency package version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDependencyVersion</td>
                    <td>Obtain the dependency package version details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDependencyVersion</td>
                    <td>Obtain the dependency package version list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDependencies</td>
                    <td>Obtain the dependency package list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDependencyVersion</td>
                    <td>Delete the dependency package version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">Function Flow</td>
                    <td>BatchDeleteWorkflows</td>
                    <td>Delete a function flow</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkflow</td>
                    <td>Query function flow</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTenantMetric</td>
                    <td>Obtain function flow metrics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkflowExecution</td>
                    <td>Obtains the execution instance of a specified function flow.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflow</td>
                    <td>Create a function flow</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkflowExecutionForPage</td>
                    <td>Obtain the execution instance list of a specified function flow by page.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkFlow</td>
                    <td>Obtain the metadata of a specified function flow instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkFlowMetric</td>
                    <td>Obtains a specified function flow metric</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartSyncWorkflowExecution</td>
                    <td>Start the function flow in synchronous execution mode (supported only by the function flow in quick mode)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCallbackWorkflow</td>
                    <td>Callback workflow</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartWorkflowExecution</td>
                    <td>Start the function flow in asynchronous execution mode</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkFlow</td>
                    <td>Modifies the metadata of a specified function flow instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopWorkFlow</td>
                    <td>Stop the function flow</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryWorkFlow</td>
                    <td>Retry the function flow</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkflowExecutions</td>
                    <td>Obtains the list of execution instances of a specified function flow.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Function Indicator</td>
                    <td>ShowFunctionMetrics</td>
                    <td>Query the function traffic metrics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionAsMetric</td>
                    <td>List of functions sorted by the specified indicator.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFuncReservedInstanceMetrics</td>
                    <td>Query the function instance usage metrics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionStatistics</td>
                    <td>Obtain the function running metrics in a specified period.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="19">Function Lifecycle Management</td>
                    <td>CreateVpcEndpoint</td>
                    <td>Create a sinking entry. (This function is supported only by CN North-Beijing 4, CN East-Shanghai1, CN East-Shanghai2, and Southwest-Guiyang1).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctions</td>
                    <td>Obtain the function list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFuncSnapshot</td>
                    <td>Disable or enable the function snapshot function. The function snapshot function can be enabled only when the Java runtime function is not the latest version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFunction</td>
                    <td>Creates the specified function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionTags</td>
                    <td>Query the function tag list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunctionMaxInstanceConfig</td>
                    <td>Updating the maximum number of function instances</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBridgeVersions</td>
                    <td>Obtain the available version of the servicebridge</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectTagsList</td>
                    <td>Query resource tags.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFuncSnapshotState</td>
                    <td>Query the function snapshot creation status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResInstanceInfo</td>
                    <td>Query resource instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFunctionCode</td>
                    <td>Obtains the code of a specified function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpcEndpoint</td>
                    <td>Delete the sinking entry. (This function is supported only by CN North-Beijing 4, CN East-Shanghai1, CN East-Shanghai2, and Southwest-Guiyang1).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunctionCode</td>
                    <td>Modifies the code of a specified function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFunction</td>
                    <td>Delete the specified function or version. The latest version cannot be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFunctionConfig</td>
                    <td>Obtains the metadata of a specified function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunctionConfig</td>
                    <td>Modifies the metadata of a specified function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBridgeFunctions</td>
                    <td>Obtains the list of servicebridge functions bound to a specified function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunctionCollectState</td>
                    <td>Update the pinning status of a function</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTags</td>
                    <td>Delete a resource tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Function Log</td>
                    <td>ShowProjectAsyncStatusLogInfo</td>
                    <td>Query asynchronous log details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableAsyncStatusLog</td>
                    <td>Asynchronous status notification is allowed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableLtsLogs</td>
                    <td>Enable the lts log reporting function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLtsLogDetails</td>
                    <td>Obtains the log stream configuration of the lts log group of a specified function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Function Template</td>
                    <td>ShowFunctionTemplate</td>
                    <td>Obtain a specified function template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionTemplate</td>
                    <td>Obtain the function template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Function Trigger</td>
                    <td>DeleteFunctionTrigger</td>
                    <td>Delete a trigger.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteFunctionTriggers</td>
                    <td>Deletes all trigger settings of a specified function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFunctionTrigger</td>
                    <td>Obtain the information about a specific trigger.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionTriggers</td>
                    <td>Obtains all trigger settings of a specified function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFunctionTrigger</td>
                    <td>Create a trigger.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Function import and export</td>
                    <td>ExportFunction</td>
                    <td>Export function</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportFunction</td>
                    <td>Import function</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Function test event</td>
                    <td>ListEvents</td>
                    <td>Obtain the test event list of a specified function</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEvent</td>
                    <td>Create a test event</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEvent</td>
                    <td>Updating the details of a test event</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEvent</td>
                    <td>Delete a specified test event</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Function version alias</td>
                    <td>UpdateVersionAlias</td>
                    <td>Modifies the alias information of the function version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVersionAlias</td>
                    <td>Create the alias of the gray version of the function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionVersions</td>
                    <td>Obtains the version list of a specified function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVersionAlias</td>
                    <td>Delete the alias of a function version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFunctionVersion</td>
                    <td>Release the function version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVersionAlias</td>
                    <td>Obtains the version alias information specified by a function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVersionAliases</td>
                    <td>Obtains the alias list of function versions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Protection Event Management</td>
                    <td>ShowEvent</td>
                    <td>Query the details of a protection event with a specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota Management</td>
                    <td>ListQuotas</td>
                    <td>Obtain quota information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Reserved function instance</td>
                    <td>ListReservedInstanceConfigs</td>
                    <td>Obtain the configuration list of function reserved instances</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionReservedInstances</td>
                    <td>Obtains the number of function reserved instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunctionReservedInstancesCount</td>
                    <td>Change the number of reserved function instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Security Overview</td>
                    <td>ListStatistics</td>
                    <td>Query the number of security overview requests and attacks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tag Management</td>
                    <td>CreateTags</td>
                    <td>Add a tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Trigger Management</td>
                    <td>UpdateTrigger</td>
                    <td>Update trigger configuration</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
