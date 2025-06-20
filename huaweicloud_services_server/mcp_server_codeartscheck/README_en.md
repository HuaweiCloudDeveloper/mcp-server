# CodeArtsCheck MCP Server 


## Version
v0.1.0

## Overview

CodeArtsCheck MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeArtsCheck. Full-chain management of CodeArtsCheck resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Defect Management | ShowTaskCmetrics | Query the cmertrics defect summary based on the check task ID. | To be tested |
|  | ShowTaskDefects | Query defect details by task ID in pagination mode. | To be tested |
|  | UpdateDefectStatus | Change the status of the detected defect to fixed or ignored. | To be tested |
|  | ShowTaskDefectsStatistic | Query statistics on defect details based on the check task ID | To be tested |
|  | ShowTaskDetail | Query the defect summary based on the check task ID. Including problem overview, problem status, cyclomatic complexity, code repetition rate, etc. | To be tested |
| ITaskController | CreateTask | This interface is used to create a task. | To be tested |
|  | DeleteTask | Delete a single task | To be tested |
| Rule Management | SetDefaulTemplate | Set the default rule set configuration for each project language. | To be tested |
|  | ListTemplateRules | Query the rule list based on the project ID and rule set ID. | To be tested |
|  | DeleteRuleset | Delete a user-defined rule set. A rule set in use or a default rule set cannot be deleted. | To be tested |
|  | CreateRuleset | Flexible combination of rules as required. | To be tested |
|  | ListRulesets | Query the rule set list based on the project ID and language. | To be tested |
| Rule engine | ListRules | Query Rule | To be tested |
| Task Management | ShowTasksRulesets | Query the selected rule sets of a task. | To be tested |
|  | ShowTaskListByProjectId | Query the task list of the project based on DEVCLOUD_PROJECT_UUID. | To be tested |
|  | CheckRecord | Provides statistics on the number of issues scanned each time. | To be tested |
|  | ListTaskRuleset | Query the selected rule sets of a task. | To be tested |
|  | ShowTaskSettings | Advanced options for querying a task | To be tested |
|  | ShowTaskPathTree | Obtain the directory tree of a task | To be tested |
|  | ShowTasklog | Query task check failure logs. If execute_id is not specified, the latest check log is queried. | To be tested |
|  | UpdateTaskSettings | Configure advanced options, for example, customizing an image. | To be tested |
|  | ShowProgressDetail | Query the task execution status based on the task ID. Task status. The options are as follows: 0: checking; 1: failed; 2: successful; 3: aborted. Progress details are only available when being checked. | To be tested |
|  | CheckRulesetParameters | Query the check parameters of the task rule set | To be tested |
|  | StopTaskById | Stop the check task based on the task ID. | To be tested |
|  | ListTaskParameter | Task configuration check parameter | To be tested |
|  | UpdateTaskRuleset | Modifies a task rule set. | To be tested |
|  | RunTask | Manually trigger task scheduling | To be tested |
|  | CheckParameters | Query the check parameters of the task rule set | To be tested |
|  | UpdateIgnorePath | Task Configuration Shielded Directory | To be tested |

