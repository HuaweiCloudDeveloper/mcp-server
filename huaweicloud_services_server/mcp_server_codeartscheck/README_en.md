# CodeArtsCheck MCP Server 


## Version
v0.1.0

## Overview

CodeArtsCheck MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeArtsCheck. Full-chain management of CodeArtsCheck resources can be carried out based on natural language.

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
                    <td rowspan="5">Defect Management</td>
                    <td>ShowTaskCmetrics</td>
                    <td>Query the cmertrics defect summary based on the check task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskDefects</td>
                    <td>Query defect details by task ID in pagination mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDefectStatus</td>
                    <td>Change the status of the detected defect to fixed or ignored.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskDefectsStatistic</td>
                    <td>Query statistics on defect details based on the check task ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskDetail</td>
                    <td>Query the defect summary based on the check task ID. Including problem overview, problem status, cyclomatic complexity, code repetition rate, etc.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ITaskController</td>
                    <td>CreateTask</td>
                    <td>This interface is used to create a task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTask</td>
                    <td>Delete a single task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Rule Management</td>
                    <td>SetDefaulTemplate</td>
                    <td>Set the default rule set configuration for each project language.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplateRules</td>
                    <td>Query the rule list based on the project ID and rule set ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRuleset</td>
                    <td>Delete a user-defined rule set. A rule set in use or a default rule set cannot be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRuleset</td>
                    <td>Flexible combination of rules as required.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRulesets</td>
                    <td>Query the rule set list based on the project ID and language.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Rule engine</td>
                    <td>ListRules</td>
                    <td>Query Rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">Task Management</td>
                    <td>ShowTasksRulesets</td>
                    <td>Query the selected rule sets of a task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskListByProjectId</td>
                    <td>Query the task list of the project based on DEVCLOUD_PROJECT_UUID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckRecord</td>
                    <td>Provides statistics on the number of issues scanned each time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskRuleset</td>
                    <td>Query the selected rule sets of a task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskSettings</td>
                    <td>Advanced options for querying a task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskPathTree</td>
                    <td>Obtain the directory tree of a task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTasklog</td>
                    <td>Query task check failure logs. If execute_id is not specified, the latest check log is queried.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskSettings</td>
                    <td>Configure advanced options, for example, customizing an image.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProgressDetail</td>
                    <td>Query the task execution status based on the task ID. Task status. The options are as follows: 0: checking; 1: failed; 2: successful; 3: aborted. Progress details are only available when being checked.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckRulesetParameters</td>
                    <td>Query the check parameters of the task rule set</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopTaskById</td>
                    <td>Stop the check task based on the task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskParameter</td>
                    <td>Task configuration check parameter</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskRuleset</td>
                    <td>Modifies a task rule set.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTask</td>
                    <td>Manually trigger task scheduling</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckParameters</td>
                    <td>Query the check parameters of the task rule set</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIgnorePath</td>
                    <td>Task Configuration Shielded Directory</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
