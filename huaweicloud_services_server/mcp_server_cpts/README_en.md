# CPTS MCP Server 


## Version
v0.1.0

## Overview

CPTS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CPTS. Full-chain management of CPTS resources can be carried out based on natural language.

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
                    <td rowspan="2">All-Link Pressure Test Management</td>
                    <td>ShowAgentConfig</td>
                    <td>Configuration information obtained by the full-link pressure test probe</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAgentHealthStatus</td>
                    <td>Health status reported by the full-link pressure test probe</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Case management</td>
                    <td>CreateCase</td>
                    <td>Creating a test case (old version)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNewCase</td>
                    <td>Create a case</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DebugCase</td>
                    <td>Debugging case</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNewCase</td>
                    <td>Delete a test case</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCase</td>
                    <td>Modifying a test case (old version)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCase</td>
                    <td>Delete a test case (old version)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCase</td>
                    <td>Query test cases</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNewCase</td>
                    <td>Modifying a test case</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Directory Management</td>
                    <td>UpdateDirectory</td>
                    <td>Modifying a directory</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDirectory</td>
                    <td>Delete a directory</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDirectory</td>
                    <td>Create a directory</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectTestCase</td>
                    <td>Query the test case tree</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Global variable management</td>
                    <td>DeleteVariable</td>
                    <td>Delete a global variable</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVariable</td>
                    <td>Modify a variable</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVariable</td>
                    <td>Create a variable</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVariables</td>
                    <td>Query global variables</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ITaskController</td>
                    <td>DeleteTask</td>
                    <td>Delete a single task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTask</td>
                    <td>This interface is used to create a task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTask</td>
                    <td>Task modification interface, used to modify task configurations</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">PerfTest Project Management</td>
                    <td>DeleteProject</td>
                    <td>Delete a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProject</td>
                    <td>Create a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProcess</td>
                    <td>Query the import progress</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectSets</td>
                    <td>Querying a project set</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProject</td>
                    <td>Modifying a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProject</td>
                    <td>Querying a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Report Management</td>
                    <td>ShowReport</td>
                    <td>Query report</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMergeTaskCase</td>
                    <td>Query the test case list of the task report</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMergeCaseDetail</td>
                    <td>Query the details of a case report</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHistoryRunInfo</td>
                    <td>Query the PerfTest offline report list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskCaseAwChart</td>
                    <td>Query the AW curve chart of a case</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Service Job Management</td>
                    <td>ShowTask</td>
                    <td>This interface is used to query service jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Task Management</td>
                    <td>CreateNewTask</td>
                    <td>Create a task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskCases</td>
                    <td>Obtain the list of test cases associated with a task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskStatus</td>
                    <td>Update task status</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskSet</td>
                    <td>Query a task set</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNewTask</td>
                    <td>Delete a task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskRelatedTestCase</td>
                    <td>Modifying a test case associated with a task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateTaskStatus</td>
                    <td>Start and stop tasks in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Transaction management</td>
                    <td>CreateTemp</td>
                    <td>Create transaction</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTemp</td>
                    <td>Query transaction</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTempSet</td>
                    <td>Query transaction set</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTemp</td>
                    <td>Delete transaction</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTemp</td>
                    <td>Modifying a transaction</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
