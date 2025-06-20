# RGC MCP Server 


## Version
v0.1.0

## Overview

RGC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RGC. Full-chain management of RGC resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Governance | DisableControl | Disable a control policy for a unit in an organization. | To be tested |
|  | ListControlsForOrganizationalUnit | Lists all control policies enabled by a registered OU in the organization. | To be tested |
|  | ShowControlOperate | Query the operation status based on the operation ID. | To be tested |
|  | EnableControl | Enable a control policy for a unit in an organization. | To be tested |
|  | ListEnabledControls | Lists all enabled control policies in the organization. | To be tested |
| ManagedOrganization | RegisterOrganizationalUnit | Register an OU in the organization with the RGC service. | To be tested |
|  | ShowOperation | Query the registration and deregistration process information in the RGC service. | To be tested |
|  | ShowManagedAccount | Query information about a management account in an organization. | To be tested |
|  | CreateAccount | Create an account under a registered OU in the organization. | To be tested |

