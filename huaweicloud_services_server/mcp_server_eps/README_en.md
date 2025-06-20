# EPS MCP Server 


## Version
v0.1.0

## Overview

EPS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EPS. Full-chain management of EPS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Enterprise Project Management Operation | ShowEnterpriseProjectQuota | Query the quota information of an enterprise project. | To be tested |
|  | EnableEnterpriseProject | Enable an enterprise project. | To be tested |
|  | ShowEnterpriseProject | Query enterprise project details. | To be tested |
|  | UpdateEnterpriseProject | Modify an enterprise project. Currently, only the name and description can be modified. | To be tested |
|  | MigrateResource | Migrate resources to the target enterprise project. | To be tested |
|  | CreateEnterpriseProject | Create an enterprise project. | To be tested |
|  | DisableEnterpriseProject | Disable an enterprise project. | To be tested |
|  | ShowResourceBindEnterpriseProject | Query details about resources bound to an enterprise project. | To be tested |
|  | ListEnterpriseProject | Query the list of authorized enterprise projects of the current user. The user can bind resources to the enterprise projects. | To be tested |
| Query services supported by tag management | ListProviders | Query the services supported by tag management. | To be tested |
| Query version operation | ShowApiVersion | Query the details about a specified TMS API version. | To be tested |
|  | ListApiVersions | Query the TMS API version list. | To be tested |

