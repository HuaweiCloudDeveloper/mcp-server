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
                    <td>任务修改接口,用于修改任务配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTask</td>
                    <td>删除单个任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">服务作业管理</td>
                    <td>ListTasksDetails</td>
                    <td>该接口用于获取服务作业列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopTask</td>
                    <td>该接口用于停止服务作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTask</td>
                    <td>该接口用于查询服务作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartTask</td>
                    <td>该接口用于启动服务作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTasks</td>
                    <td>该接口用于创建服务作业</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
