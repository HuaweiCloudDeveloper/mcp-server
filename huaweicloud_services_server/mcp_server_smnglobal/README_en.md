# SMNGLOBAL MCP Server 


## Version
v0.1.0

## Overview

SMNGLOBAL MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SMNGLOBAL. Full-chain management of SMNGLOBAL resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Subscriber | UpdateSubscriptionUser | Update the subscriber. | To be tested |
|  | CreateSubscriptionUser | Add a subscriber. If the status of the subscriber is Unacknowledged, a subscription confirmation message is sent to the subscriber. After a subscriber clicks the subscription link to confirm the subscription, the status of the subscriber changes to Confirmed. At the same time, a message is sent to the subscriber so that the subscriber can cancel the subscription at any time. After the subscriber clicks the unsubscription link, the status of the subscriber changes to Canceled. At the same time, a re-subscription message is sent to the subscriber so that the subscriber can subscribe again. | To be tested |
|  | ListSubscriptionUser | Query the list of subscribers. | To be tested |
|  | DeleteSubscriptionUser | Delete the subscriber. | To be tested |

