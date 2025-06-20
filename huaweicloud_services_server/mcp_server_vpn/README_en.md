# VPN MCP Server 


## Version
v0.1.0

## Overview

VPN MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VPN. Full-chain management of VPN resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| ClientCaCertificate | CheckClientCaCertificate | When creating a server, you can invoke the pre-verification API of the client CA to check the validity of the CA. | To be tested |
|  | UpdateClientCa | Modifying the CA certificate of the client | To be tested |
|  | ImportClientCa | Importing the CA Certificate of the Client | To be tested |
|  | DeleteClientCa | Delete the client CA certificate | To be tested |
|  | ShowClientCa | Querying the CA certificate of the client | To be tested |
| ConnectionMonitor | ListConnectionMonitors | Query the VPN connection monitoring list | To be tested |
|  | ShowConnectionMonitor | Query a specified VPN connection based on the VPN connection monitoring ID. | To be tested |
|  | DeleteConnectionMonitor | Deletes a specified VPN connection monitoring task based on the VPN connection monitoring ID. | To be tested |
|  | CreateConnectionMonitor | Create a VPN connection monitoring task. | To be tested |
| CustomerGateway | ShowCgw | Query the specified peer gateway based on the peer gateway ID. | To be tested |
|  | DeleteCgw | Delete the specified peer gateway based on the peer gateway ID. | To be tested |
|  | CreateCgw | Create the peer gateway used by the tenant to connect to the VPN gateway. | To be tested |
|  | UpdateCgw | Update the specified peer gateway based on the peer gateway ID. | To be tested |
|  | ListCgws | Query the peer gateway list | To be tested |
| P2cVpnGateway | DeleteP2cVgwConnection | Disconnecting the P2C VPN Gateway | To be tested |
|  | ListP2cVgwAvailabilityZones | Querying the P2C VPN Gateway AZ | To be tested |
|  | ListP2cVgwConnections | List p2c vpn gateway connections | To be tested |
|  | ListP2cVgws | Query the P2C VPN gateway list | To be tested |
|  | ShowP2cVgw | Query the specified VPN gateway based on the P2C VPN gateway ID. | To be tested |
|  | UpdateP2cVgw | Updates the specified P2C VPN gateway based on the P2C VPN gateway ID. | To be tested |
| Tags | ShowResourceTags | Query the label information of a specified DB instance | To be tested |
|  | BatchCreateResourceTags | Adding tags to specified instances in batches | To be tested |
|  | ListResourcesByTags | Query the resource instance list by tag | To be tested |
|  | ListProjectTags | Query all tags of a specified resource type in a specified project | To be tested |
|  | BatchDeleteResourceTags | Delete tags in batches for specified instances | To be tested |
|  | CountResourcesByTags | Query the number of resource instances by tag | To be tested |
| VpnAccessPolicy | UpdateVpnAccessPolicy | Modifying a VPN access policy | To be tested |
|  | DeleteVpnAccessPolicy | Delete a VPN access policy | To be tested |
|  | ListVpnAccessPolicies | Query the VPN access policy list | To be tested |
|  | CreateVpnAccessPolicy | Create a VPN access policy | To be tested |
|  | ShowVpnAccessPolicy | Query VPN access policies | To be tested |
| VpnConnection | ShowVpnConnection | Query the parameters of a specified VPN connection based on the connection ID. | To be tested |
|  | UpdateVpnConnection | Updates the parameters of a specified VPN connection based on the connection ID. | To be tested |
|  | ResetVpnConnection | Resets a specified VPN connection based on the connection ID. | To be tested |
|  | CreateVpnConnection | Create a VPN connection between the VPN gateway and the peer gateway. | To be tested |
|  | ShowVpnConnectionLog | Query the specified VPN connection logs based on the connection ID. | To be tested |
|  | ListVpnConnections | Query the VPN connection list | To be tested |
|  | DeleteVpnConnection | Delete a specified VPN connection based on the connection ID. | To be tested |
| VpnConnectionsLogConfig | ShowVpnConnectionsLogConfig | Query VPN connection log configuration | To be tested |
|  | DeleteVpnConnectionsLogConfig | Delete VPN connection log configuration | To be tested |
|  | UpdateVpnConnectionsLogConfig | Updating VPN connection log configurations | To be tested |
| VpnGateway | ShowVgw | Query the specified VPN gateway based on the VPN gateway ID. | To be tested |
|  | ListExtendedAvailabilityZones | Querying the AZ of the VPN gateway | To be tested |
|  | ShowVpnGatewayRoutingTable |  | To be tested |
|  | UpdatePostpaidVgwSpecification | Modify the specifications of a single gateway. The configuration can be increased or decreased. | To be tested |
|  | ListAvailabilityZones | Querying the AZ of the VPN gateway | To be tested |
|  | CreateVgw | Create a VPN gateway. | To be tested |
|  | UpdateVgw | Updates a specified VPN gateway based on the VPN gateway ID. | To be tested |
|  | ListVgws | Query the VPN gateway list | To be tested |
|  | DeleteVgw | Deletes a specified VPN gateway based on the VPN gateway ID. | To be tested |
| VpnGatewayCertificate | ShowVpnGatewayCertificate | Query the specified VPN gateway certificate based on the VPN gateway ID. | To be tested |
|  | UpdateVgwCertificate | Update the certificates used by the tenant VPN gateway, including the signature certificate, signature private key, encryption certificate, encryption private key, and CA certificate chain. Currently, only the Chinese secret certificate is supported. | To be tested |
|  | CreateVgwCertificate | Import the certificates used by the tenant VPN gateway, including the signature certificate, signature private key, encryption certificate, encryption private key, and CA certificate chain. Currently, only the Chinese secret certificate is supported. | To be tested |
| VpnQuota | ShowQuotasInfo | Query the quota of a specified tenant | To be tested |
| VpnServer | ListVpnServersByVgw | Query the server information of a gateway | To be tested |
|  | UpdateVpnServer | Updates a specified VPN server | To be tested |
|  | ExportClientConfig | Export client configuration information | To be tested |
|  | CreateVpnServer | Create a VPN server. | To be tested |
|  | ListVpnServersByProject | Query information about all servers of a tenant | To be tested |
| VpnUser | ListVpnUsers | Query the VPN user list | To be tested |
|  | UpdateVpnUser | Modifying a VPN User | To be tested |
|  | CreateVpnUser | Create a VPN user | To be tested |
|  | BatchCreateVpnUsers | Creating P2C VPN Users in Batches | To be tested |
|  | UpdateVpnUserPassword | Change the VPN user password | To be tested |
|  | ShowVpnUser | Querying VPN Users | To be tested |
|  | DeleteVpnUser | Deleting a VPN User | To be tested |
|  | ResetVpnUserPassword | Resetting the VPN User Password | To be tested |
|  | BatchDeleteVpnUsers | Deleting P2C VPN Users in Batches | To be tested |
| VpnUserGroup | AddVpnUsersToGroup | Adding a VPN User to a Group | To be tested |
|  | CreateVpnUserGroup | Create a VPN user group | To be tested |
|  | ListVpnUserGroups | Query the VPN user group list | To be tested |
|  | DeleteVpnUserGroup | Delete a VPN user group | To be tested |
|  | UpdateVpnUserGroup | Modifying a VPN User Group | To be tested |
|  | ListVpnUsersInGroup | Query VPN users in a group | To be tested |
|  | RemoveVpnUsersFromGroup | Deleting a VPN User from a Group | To be tested |
|  | ShowVpnUserGroup | Query VPN user groups | To be tested |

