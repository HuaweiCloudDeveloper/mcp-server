# VPCEP MCP Server 


## Version
v0.1.0

## Overview

VPCEP MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VPCEP. Full-chain management of VPCEP resources can be carried out based on natural language.

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
                    <td rowspan="1">Resource Quota Function</td>
                    <td>ListQuotaDetails</td>
                    <td>Query the resource quota of a user, including the VPC endpoint service and VPC endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">TAG Function</td>
                    <td>BatchAddOrRemoveResourceInstance</td>
                    <td>This API is used to add or delete tags for a specified endpoint service or endpoint in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryProjectResourceTags</td>
                    <td>Obtain the resource tags of a tenant based on the tenant ID and resource type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceInstances</td>
                    <td>Query resource instances of a tenant by tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">VPC Endpoint Function</td>
                    <td>UpdateEndpointPolicy</td>
                    <td>Modify the VPC endpoint policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEndpoint</td>
                    <td>Delete the VPC endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEndpointPolicy</td>
                    <td>This API is used to delete a gateway VPC endpoint policy. This API is not recommended because it will be brought offline.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpointWhite</td>
                    <td>Updates or deletes the trustlist that can access the VPC endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpointRoutetable</td>
                    <td>Modifies the routing table of the VPC endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpointInfoDetails</td>
                    <td>Query detailed information about a VPC endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpoints</td>
                    <td>Query the list of VPC endpoints of the current user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEndpoint</td>
                    <td>Create a VPC endpoint so that it can access the VPC endpoint service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">VPC endpoint service function</td>
                    <td>DeleteEndpointService</td>
                    <td>Delete the VPC endpoint service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceConnections</td>
                    <td>Query the list of connections to a VPC endpoint service of the current user. marker_id is the unique identification of the connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeEndpointService</td>
                    <td>Upgrade the VPC endpoint service so that the VPC endpoint service supports the creation of professional VPC endpoint instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddOrRemoveServicePermissions</td>
                    <td>Adding or removing the trustlist of the VPC endpoint services of the current user in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServicePublicDetails</td>
                    <td>Query the list of public VPC endpoint services. Public VPC endpoint services are visible and accessible to all users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRemoveEndpointServicePermissions</td>
                    <td>Delete the trustlist of VPC endpoint services of the current user in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpointService</td>
                    <td>Modify the VPC endpoint service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEndpointService</td>
                    <td>Create a VPC endpoint service, allowing other users to create VPC endpoints and connect to the VPC endpoint service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServicePermissionsDetails</td>
                    <td>Query the trustlist of the VPC endpoint service of the current user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddEndpointServicePermissions</td>
                    <td>This API is used to add the trustlist of VPC endpoint services of the current user in batches. Description information can be added.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpointService</td>
                    <td>Query the list of VPC endpoint services of the current user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpointServicePermissionDesc</td>
                    <td>Updates the description of the VPC endpoint service trustlist of the current user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceDescribeDetails</td>
                    <td>Query the summary information about the VPC endpoint service. This API is used by the VPC endpoint creation user to query the VPC endpoint service to be connected. This API helps other users to query the summary information about your VPC endpoint service and prevents the details of your VPC endpoint service from being exposed to other users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpointConnectionsDesc</td>
                    <td>Updates the description of the VPC endpoint connected to the VPC endpoint service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AcceptOrRejectEndpoint</td>
                    <td>Accepts or rejects the connection from the VPC endpoint to the current VPC endpoint service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceDetails</td>
                    <td>Query details about the VPC endpoint service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpointServiceName</td>
                    <td>Change the VPC endpoint service name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Version Management</td>
                    <td>ListVersionDetails</td>
                    <td>Query the VPCEP API version list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSpecifiedVersionDetails</td>
                    <td>Query the API version information of a specified VPCEP node.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
