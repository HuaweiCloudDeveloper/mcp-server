# EDS MCP Server 


## Version
v0.1.0

## Overview

EDS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EDS. Full-chain management of EDS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Audit Log | ShowAuditLog | Query audit logs of data assets | To be tested |
| Connector | ShowConnector | Query the connector details of a specified tenant | To be tested |
|  | ListConnectorsByInstanceUser | Query the connector list by space user | To be tested |
|  | ListConnectorsByInstanceManger | Query the connector list by space administrator | To be tested |
| Contract | CommitContract | Submit the contract | To be tested |
|  | CancelContract | Terminate the contract | To be tested |
|  | ShowContract | Query a contract | To be tested |
| offer | ListOffers | Query the offering list under a specified connector | To be tested |
|  | ShowOffer | Query the details of a specified offering | To be tested |
| user | AddConnectorUser | Assigning a subaccount | To be tested |
|  | DeleteConnectorUser | Reclaiming an account | To be tested |

