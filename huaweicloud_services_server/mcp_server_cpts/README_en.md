# CPTS MCP Server 


## Version
v0.1.0

## Overview

CPTS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CPTS. Full-chain management of CPTS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| All-Link Pressure Test Management | ShowAgentConfig | Configuration information obtained by the full-link pressure test probe | To be tested |
|  | UpdateAgentHealthStatus | Health status reported by the full-link pressure test probe | To be tested |
| Case management | CreateCase | Creating a test case (old version) | To be tested |
|  | CreateNewCase | Create a case | To be tested |
|  | DebugCase | Debugging case | To be tested |
|  | DeleteNewCase | Delete a test case | To be tested |
|  | UpdateCase | Modifying a test case (old version) | To be tested |
|  | DeleteCase | Delete a test case (old version) | To be tested |
|  | ShowCase | Query test cases | To be tested |
|  | UpdateNewCase | Modifying a test case | To be tested |
| Directory Management | UpdateDirectory | Modifying a directory | To be tested |
|  | DeleteDirectory | Delete a directory | To be tested |
|  | CreateDirectory | Create a directory | To be tested |
|  | ListProjectTestCase | Query the test case tree | To be tested |
| Global variable management | DeleteVariable | Delete a global variable | To be tested |
|  | UpdateVariable | Modify a variable | To be tested |
|  | CreateVariable | Create a variable | To be tested |
|  | ListVariables | Query global variables | To be tested |
| ITaskController | DeleteTask | Delete a single task | To be tested |
|  | CreateTask | This interface is used to create a task. | To be tested |
|  | UpdateTask | Task modification interface, used to modify task configurations | To be tested |
| PerfTest Project Management | DeleteProject | Delete a project | To be tested |
|  | CreateProject | Create a project | To be tested |
|  | ShowProcess | Query the import progress | To be tested |
|  | ListProjectSets | Querying a project set | To be tested |
|  | UpdateProject | Modifying a project | To be tested |
|  | ShowProject | Querying a project | To be tested |
| Report Management | ShowReport | Query report | To be tested |
|  | ShowMergeTaskCase | Query the test case list of the task report | To be tested |
|  | ShowMergeCaseDetail | Query the details of a case report | To be tested |
|  | ShowHistoryRunInfo | Query the PerfTest offline report list | To be tested |
|  | ShowTaskCaseAwChart | Query the AW curve chart of a case | To be tested |
| Service Job Management | ShowTask | This interface is used to query service jobs. | To be tested |
| Task Management | CreateNewTask | Create a task | To be tested |
|  | ListTaskCases | Obtain the list of test cases associated with a task | To be tested |
|  | UpdateTaskStatus | Update task status | To be tested |
|  | ShowTaskSet | Query a task set | To be tested |
|  | DeleteNewTask | Delete a task | To be tested |
|  | UpdateTaskRelatedTestCase | Modifying a test case associated with a task | To be tested |
|  | BatchUpdateTaskStatus | Start and stop tasks in batches | To be tested |
| Transaction management | CreateTemp | Create transaction | To be tested |
|  | ShowTemp | Query transaction | To be tested |
|  | ShowTempSet | Query transaction set | To be tested |
|  | DeleteTemp | Delete transaction | To be tested |
|  | UpdateTemp | Modifying a transaction | To be tested |

