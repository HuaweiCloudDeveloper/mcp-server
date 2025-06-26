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
                    <td rowspan="4">Subscriber</td>
                    <td>UpdateSubscriptionUser</td>
                    <td>Update the subscriber.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubscriptionUser</td>
                    <td>Add a subscriber. If the status of the subscriber is Unacknowledged, a subscription confirmation message is sent to the subscriber. After a subscriber clicks the subscription link to confirm the subscription, the status of the subscriber changes to Confirmed. At the same time, a message is sent to the subscriber so that the subscriber can cancel the subscription at any time. After the subscriber clicks the unsubscription link, the status of the subscriber changes to Canceled. At the same time, a re-subscription message is sent to the subscriber so that the subscriber can subscribe again.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubscriptionUser</td>
                    <td>Query the list of subscribers.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubscriptionUser</td>
                    <td>Delete the subscriber.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
