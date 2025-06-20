# VPCEP MCP Server 


## Version
v0.1.0

## Overview

VPCEP MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VPCEP. Full-chain management of VPCEP resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Resource Quota Function | ListQuotaDetails | Query the resource quota of a user, including the VPC endpoint service and VPC endpoint. | To be tested |
| TAG Function | BatchAddOrRemoveResourceInstance | This API is used to add or delete tags for a specified endpoint service or endpoint in batches. | To be tested |
|  | ListQueryProjectResourceTags | Obtain the resource tags of a tenant based on the tenant ID and resource type. | To be tested |
|  | ListResourceInstances | Query resource instances of a tenant by tag. | To be tested |
| VPC Endpoint Function | UpdateEndpointPolicy | Modify the VPC endpoint policy. | To be tested |
|  | DeleteEndpoint | Delete the VPC endpoint. | To be tested |
|  | DeleteEndpointPolicy | This API is used to delete a gateway VPC endpoint policy. This API is not recommended because it will be brought offline. | To be tested |
|  | UpdateEndpointWhite | Updates or deletes the trustlist that can access the VPC endpoint. | To be tested |
|  | UpdateEndpointRoutetable | Modifies the routing table of the VPC endpoint. | To be tested |
|  | ListEndpointInfoDetails | Query detailed information about a VPC endpoint. | To be tested |
|  | ListEndpoints | Query the list of VPC endpoints of the current user. | To be tested |
|  | CreateEndpoint | Create a VPC endpoint so that it can access the VPC endpoint service. | To be tested |
| VPC endpoint service function | DeleteEndpointService | Delete the VPC endpoint service. | To be tested |
|  | ListServiceConnections | Query the list of connections to a VPC endpoint service of the current user. marker_id is the unique identification of the connection. | To be tested |
|  | UpgradeEndpointService | Upgrade the VPC endpoint service so that the VPC endpoint service supports the creation of professional VPC endpoint instances. | To be tested |
|  | AddOrRemoveServicePermissions | Adding or removing the trustlist of the VPC endpoint services of the current user in batches. | To be tested |
|  | ListServicePublicDetails | Query the list of public VPC endpoint services. Public VPC endpoint services are visible and accessible to all users. | To be tested |
|  | BatchRemoveEndpointServicePermissions | Delete the trustlist of VPC endpoint services of the current user in batches | To be tested |
|  | UpdateEndpointService | Modify the VPC endpoint service. | To be tested |
|  | CreateEndpointService | Create a VPC endpoint service, allowing other users to create VPC endpoints and connect to the VPC endpoint service. | To be tested |
|  | ListServicePermissionsDetails | Query the trustlist of the VPC endpoint service of the current user. | To be tested |
|  | BatchAddEndpointServicePermissions | This API is used to add the trustlist of VPC endpoint services of the current user in batches. Description information can be added. | To be tested |
|  | ListEndpointService | Query the list of VPC endpoint services of the current user. | To be tested |
|  | UpdateEndpointServicePermissionDesc | Updates the description of the VPC endpoint service trustlist of the current user. | To be tested |
|  | ListServiceDescribeDetails | Query the summary information about the VPC endpoint service. This API is used by the VPC endpoint creation user to query the VPC endpoint service to be connected. This API helps other users to query the summary information about your VPC endpoint service and prevents the details of your VPC endpoint service from being exposed to other users. | To be tested |
|  | UpdateEndpointConnectionsDesc | Updates the description of the VPC endpoint connected to the VPC endpoint service. | To be tested |
|  | AcceptOrRejectEndpoint | Accepts or rejects the connection from the VPC endpoint to the current VPC endpoint service. | To be tested |
|  | ListServiceDetails | Query details about the VPC endpoint service. | To be tested |
|  | UpdateEndpointServiceName | Change the VPC endpoint service name. | To be tested |
| Version Management | ListVersionDetails | Query the VPCEP API version list. | To be tested |
|  | ListSpecifiedVersionDetails | Query the API version information of a specified VPCEP node. | To be tested |

