# VPN MCP Server 


## Version
v0.1.0

## Overview

VPN MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VPN. Full-chain management of VPN resources can be carried out based on natural language.

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
                    <td rowspan="5">ClientCaCertificate</td>
                    <td>CheckClientCaCertificate</td>
                    <td>When creating a server, you can invoke the pre-verification API of the client CA to check the validity of the CA.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClientCa</td>
                    <td>Modifying the CA certificate of the client</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportClientCa</td>
                    <td>Importing the CA Certificate of the Client</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClientCa</td>
                    <td>Delete the client CA certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClientCa</td>
                    <td>Querying the CA certificate of the client</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">ConnectionMonitor</td>
                    <td>ListConnectionMonitors</td>
                    <td>Query the VPN connection monitoring list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConnectionMonitor</td>
                    <td>Query a specified VPN connection based on the VPN connection monitoring ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnectionMonitor</td>
                    <td>Deletes a specified VPN connection monitoring task based on the VPN connection monitoring ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnectionMonitor</td>
                    <td>Create a VPN connection monitoring task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">CustomerGateway</td>
                    <td>ShowCgw</td>
                    <td>Query the specified peer gateway based on the peer gateway ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCgw</td>
                    <td>Delete the specified peer gateway based on the peer gateway ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCgw</td>
                    <td>Create the peer gateway used by the tenant to connect to the VPN gateway.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCgw</td>
                    <td>Update the specified peer gateway based on the peer gateway ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCgws</td>
                    <td>Query the peer gateway list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">P2cVpnGateway</td>
                    <td>DeleteP2cVgwConnection</td>
                    <td>Disconnecting the P2C VPN Gateway</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListP2cVgwAvailabilityZones</td>
                    <td>Querying the P2C VPN Gateway AZ</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListP2cVgwConnections</td>
                    <td>List p2c vpn gateway connections</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListP2cVgws</td>
                    <td>Query the P2C VPN gateway list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowP2cVgw</td>
                    <td>Query the specified VPN gateway based on the P2C VPN gateway ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateP2cVgw</td>
                    <td>Updates the specified P2C VPN gateway based on the P2C VPN gateway ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Tags</td>
                    <td>ShowResourceTags</td>
                    <td>Query the label information of a specified DB instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateResourceTags</td>
                    <td>Adding tags to specified instances in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourcesByTags</td>
                    <td>Query the resource instance list by tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectTags</td>
                    <td>Query all tags of a specified resource type in a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteResourceTags</td>
                    <td>Delete tags in batches for specified instances</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountResourcesByTags</td>
                    <td>Query the number of resource instances by tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">VpnAccessPolicy</td>
                    <td>UpdateVpnAccessPolicy</td>
                    <td>Modifying a VPN access policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpnAccessPolicy</td>
                    <td>Delete a VPN access policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpnAccessPolicies</td>
                    <td>Query the VPN access policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpnAccessPolicy</td>
                    <td>Create a VPN access policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpnAccessPolicy</td>
                    <td>Query VPN access policies</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">VpnConnection</td>
                    <td>ShowVpnConnection</td>
                    <td>Query the parameters of a specified VPN connection based on the connection ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpnConnection</td>
                    <td>Updates the parameters of a specified VPN connection based on the connection ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetVpnConnection</td>
                    <td>Resets a specified VPN connection based on the connection ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpnConnection</td>
                    <td>Create a VPN connection between the VPN gateway and the peer gateway.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpnConnectionLog</td>
                    <td>Query the specified VPN connection logs based on the connection ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpnConnections</td>
                    <td>Query the VPN connection list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpnConnection</td>
                    <td>Delete a specified VPN connection based on the connection ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">VpnConnectionsLogConfig</td>
                    <td>ShowVpnConnectionsLogConfig</td>
                    <td>Query VPN connection log configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpnConnectionsLogConfig</td>
                    <td>Delete VPN connection log configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpnConnectionsLogConfig</td>
                    <td>Updating VPN connection log configurations</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">VpnGateway</td>
                    <td>ShowVgw</td>
                    <td>Query the specified VPN gateway based on the VPN gateway ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListExtendedAvailabilityZones</td>
                    <td>Querying the AZ of the VPN gateway</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpnGatewayRoutingTable</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePostpaidVgwSpecification</td>
                    <td>Modify the specifications of a single gateway. The configuration can be increased or decreased.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailabilityZones</td>
                    <td>Querying the AZ of the VPN gateway</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVgw</td>
                    <td>Create a VPN gateway.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVgw</td>
                    <td>Updates a specified VPN gateway based on the VPN gateway ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVgws</td>
                    <td>Query the VPN gateway list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVgw</td>
                    <td>Deletes a specified VPN gateway based on the VPN gateway ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">VpnGatewayCertificate</td>
                    <td>ShowVpnGatewayCertificate</td>
                    <td>Query the specified VPN gateway certificate based on the VPN gateway ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVgwCertificate</td>
                    <td>Update the certificates used by the tenant VPN gateway, including the signature certificate, signature private key, encryption certificate, encryption private key, and CA certificate chain. Currently, only the Chinese secret certificate is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVgwCertificate</td>
                    <td>Import the certificates used by the tenant VPN gateway, including the signature certificate, signature private key, encryption certificate, encryption private key, and CA certificate chain. Currently, only the Chinese secret certificate is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">VpnQuota</td>
                    <td>ShowQuotasInfo</td>
                    <td>Query the quota of a specified tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">VpnServer</td>
                    <td>ListVpnServersByVgw</td>
                    <td>Query the server information of a gateway</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpnServer</td>
                    <td>Updates a specified VPN server</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportClientConfig</td>
                    <td>Export client configuration information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpnServer</td>
                    <td>Create a VPN server.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpnServersByProject</td>
                    <td>Query information about all servers of a tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">VpnUser</td>
                    <td>ListVpnUsers</td>
                    <td>Query the VPN user list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpnUser</td>
                    <td>Modifying a VPN User</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpnUser</td>
                    <td>Create a VPN user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateVpnUsers</td>
                    <td>Creating P2C VPN Users in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpnUserPassword</td>
                    <td>Change the VPN user password</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpnUser</td>
                    <td>Querying VPN Users</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpnUser</td>
                    <td>Deleting a VPN User</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetVpnUserPassword</td>
                    <td>Resetting the VPN User Password</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteVpnUsers</td>
                    <td>Deleting P2C VPN Users in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">VpnUserGroup</td>
                    <td>AddVpnUsersToGroup</td>
                    <td>Adding a VPN User to a Group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpnUserGroup</td>
                    <td>Create a VPN user group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpnUserGroups</td>
                    <td>Query the VPN user group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpnUserGroup</td>
                    <td>Delete a VPN user group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpnUserGroup</td>
                    <td>Modifying a VPN User Group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpnUsersInGroup</td>
                    <td>Query VPN users in a group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveVpnUsersFromGroup</td>
                    <td>Deleting a VPN User from a Group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpnUserGroup</td>
                    <td>Query VPN user groups</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
