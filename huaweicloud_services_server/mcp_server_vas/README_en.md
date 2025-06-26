# VAS MCP Server 


## Version
v0.1.0

## Overview

VAS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VAS. Full-chain management of VAS resources can be carried out based on natural language.

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
                    <td rowspan="2">ITaskController</td>
                    <td>UpdateTask</td>
                    <td>Task modification interface, used to modify task configurations</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTask</td>
                    <td>Delete a single task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Service Job Management</td>
                    <td>ListTasksDetails</td>
                    <td>This interface is used to obtain the service job list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopTask</td>
                    <td>This interface is used to stop a service job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTask</td>
                    <td>This interface is used to query service jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartTask</td>
                    <td>This interface is used to start a service job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTasks</td>
                    <td>This API is used to create a service job.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
