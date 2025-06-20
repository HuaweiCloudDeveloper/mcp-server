# CMS MCP Server 


## Version
v0.1.0

## Overview

CMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CMS. Full-chain management of CMS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Lifecycle Management | ListInstances | Query the instance list of a tenant. Query by condition is supported. | To be tested |
| Smart Buying Group Management | CreateAutoLaunchGroup | Create Smart Buying Group | To be tested |
|  | ShowAutoLaunchGroup | Query the details about a specified smart purchase group | To be tested |
|  | DeleteAutoLaunchGroup | Delete a specified smart buying group | To be tested |
|  | ListAutoLaunchGroups | Obtain all smart purchase groups created by the tenant. | To be tested |
|  | UpdateAutoLaunchGroup | Update the information about a specified smart purchase group | To be tested |
| Specification Recommendation Management | ListSupplyRecommendation | Recommend the region and specifications of ECS resources. The recommendation result is displayed in the form of scores. A higher score indicates a higher recommendation degree. | To be tested |

