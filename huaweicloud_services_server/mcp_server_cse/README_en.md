# CSE MCP Server 


## Version
v0.1.0

## Overview

CSE MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CSE. Full-chain management of CSE resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Configuration Management | UploadKie | Importing the kie configuration | To be tested |
|  | DownloadKie | Exporting the kie configuration | To be tested |
| DDM Instance Management | ListEngines | Query the DDM engine details. | To be tested |
| Engine Management | ShowEngine | Query the details of a microservice engine | To be tested |
|  | DeleteEngine | Delete a microservice engine. | To be tested |
|  | UpgradeEngine | Upgrading the Microservice Engine | To be tested |
|  | RetryEngine | Retry the microservice engine. Currently, only ServiceComb is supported. | To be tested |
|  | ShowEngineQuotas | Query the CSE quota. | To be tested |
|  | ResizeEngine | Change the CSE specifications. | To be tested |
|  | UpgradeEngineConfig | Update the configuration of the CSE, including the configuration of the ServiceComb exclusive engine and the registration configuration center engine. | To be tested |
|  | CreateEngine | Create a microservice engine. You can create the ServiceComb exclusive edition, register with the configuration center, and AGW (open beta test). | To be tested |
|  | ShowEngineJob | Query the details of a CSE task. | To be tested |
| Engine version and specification | ListFlavors | Query database specifications. | To be tested |
| Governance | ListGovernancePolicyByPolicyId | Query governance policy details. | To be tested |
|  | CreateGovernancePolicy | Create a governance policy. | To be tested |
|  | UpdateGovernancePolicy | Modify a governance policy. | To be tested |
|  | CreateMicroserviceRouteRule | Create a gray release policy. | To be tested |
|  | DeleteGovernancePolicy | Delete a governance policy. | To be tested |
|  | DeleteMicroserviceRouteRule | Delete the dark launch policy. | To be tested |
|  | ListGovernancePolicys | Query the governance policy list. | To be tested |
|  | ListGovernancePolicy | Query the governance policy list of a specified type. | To be tested |
|  | ListMicroserviceRouteRule | Query the dark launch rules of a microservice. | To be tested |
| Plug-in management | DeletePlugin | Delete the plug-in. | To be tested |
|  | CreatePlugin | Create plug-in information. | To be tested |
| gateway | ModifyHttp2Rpc | Modify the HTTP-to-RPC conversion method. | To be tested |
|  | ShowPlugins | Query the plug-in list. | To be tested |
|  | ModifyPlugin | Modify the plug-in. | To be tested |
|  | CreateHttp2Rpc | Create an HTTP-to-RPC method. | To be tested |
|  | DeleteHttp2Rpc | The HTTP-to-RPC method is deleted. | To be tested |
|  | ShowHttp2Rpcs | Query the list of resources converted from HTTP to RPC. | To be tested |
|  | ShowSinglePlugin | Query a single plug-in. | To be tested |
| nacos | ListNacosNamespaces | Query the nacos namespace. | To be tested |
|  | DeleteNacosNamespaces | Delete the nacos namespace. | To be tested |
|  | UpdateNacosNamespaces | Update the nacos namespace. | To be tested |
|  | CreateNacosNamespaces | Create the nacos namespace. | To be tested |

