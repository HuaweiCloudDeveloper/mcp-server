# SMNGLOBAL MCP Server 


## Version
v0.1.0

## Overview

SMNGLOBAL MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SMNGLOBAL. Full-chain management of SMNGLOBAL resources can be carried out based on natural language.

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
                    <td rowspan="4">订阅用户</td>
                    <td>UpdateSubscriptionUser</td>
                    <td>更新订阅用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubscriptionUser</td>
                    <td>添加订阅用户。如果订阅用户的状态为未确认,则会向订阅用户发送一条确认订阅消息。订阅用户点击订阅链接确认订阅后,则订阅用户的状态变更为已确认,同时会向订阅用户发送一条取消订阅消息,便于订阅用户随时可以取消订阅。订阅用户点击取消订阅链接后,则订阅用户的状态变更为已取消,同时会向订阅用户发送一条重新订阅消息,便于订阅用户可以重新订阅。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubscriptionUser</td>
                    <td>查询订阅用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubscriptionUser</td>
                    <td>删除订阅用户。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
