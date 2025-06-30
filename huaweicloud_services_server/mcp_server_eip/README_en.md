# EIP MCP Server 


## Version
v0.1.0

## Overview

EIP MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EIP. Full-chain management of EIP resources can be carried out based on natural language.

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
                    <td rowspan="14">Bandwidth</td>
                    <td>AddPublicipsIntoSharedBandwidth</td>
                    <td>The EIP is inserted into the shared bandwidth.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrePaidBandwidth</td>
                    <td>Update the bandwidth.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBandwidth</td>
                    <td>Update the bandwidth.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidths</td>
                    <td>Query the bandwidth list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeBandwidthToPeriod</td>
                    <td>On-demand subcontracting API for tenants.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSharedBandwidth</td>
                    <td>Delete the shared bandwidth.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemovePublicipsFromSharedBandwidth</td>
                    <td>The EIP is removed from the shared bandwidth.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEipBandwidths</td>
                    <td>Query the bandwidth list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBandwidth</td>
                    <td>Query bandwidth details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSharedBandwidth</td>
                    <td>Create a shared bandwidth.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchModifyBandwidth</td>
                    <td>This API is not applicable to batch bandwidth, shared bandwidth, and yearly/monthly bandwidth update.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateSharedBandwidths</td>
                    <td>Create shared bandwidths in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidth</td>
                    <td>Query the bandwidth list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidthsLimit</td>
                    <td>Obtains the EIP bandwidth limit list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Bandwidth add-on package</td>
                    <td>ListBandwidthPkg</td>
                    <td>Query the bandwidth add-on package list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Binding relationship between GEIP and instances</td>
                    <td>ListProjectGeipBindings</td>
                    <td>Query the list of tenants bound to GEIPs and instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">EIP</td>
                    <td>DeletePublicip</td>
                    <td>This API is used to delete an EIP that is bound to an EIP. The EIP cannot be deleted directly.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublicips</td>
                    <td>Query the EIP list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableNat64</td>
                    <td>Disable NAT64 for EIPs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangePublicipToPeriod</td>
                    <td>On-demand subcontracting API for tenants.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachBatchPublicIp</td>
                    <td>Adding shared bandwidths to EIPs in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPublicip</td>
                    <td>Query EIP details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountEipAvailableResources</td>
                    <td>The IP address pool is used to query the number of available public IP addresses.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociatePublicips</td>
                    <td>Unbinding an EIP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableNat64</td>
                    <td>Enable NAT64 for EIPs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociatePublicips</td>
                    <td>Bound an EIP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachShareBandwidth</td>
                    <td>Remove an EIP from the shared bandwidth</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePublicip</td>
                    <td>Apply for an EIP. Both IPv4 and IPv6 are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePrePaidPublicip</td>
                    <td>Applying for a yearly/monthly EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublicip</td>
                    <td>Update EIP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachShareBandwidth</td>
                    <td>Adding the shared bandwidth to an EIP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachBatchPublicIp</td>
                    <td>Remove EIPs from Shared Bandwidth in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">EIP Tag Management</td>
                    <td>ShowPublicipTags</td>
                    <td>Query the tag information of a specified EIP instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePublicipTags</td>
                    <td>This API is used to delete tags for specified EIP instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePublicipTag</td>
                    <td>This API is used to add tags to a specified EIP resource instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreatePublicipTags</td>
                    <td>This API is used to add tags to specified EIP instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublicipsByTags</td>
                    <td>Filter EIPs by tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePublicipTag</td>
                    <td>This API is used to delete the tag information of a specified EIP. In the preceding command, project_id indicates the project ID, and publicip_id indicates the ID of the EIP to be operated. key is the key of the label to be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublicipTags</td>
                    <td>Query all tags of a tenant in a specified region and instance type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Elastic IP address auxiliary interface</td>
                    <td>ShowPublicIpType</td>
                    <td>Query the public IP type</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountPublicIp</td>
                    <td>Query the number of public IP addresses.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountPublicIpInstance</td>
                    <td>Query the number of PublicIp instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">OpenStack-Floating IP address</td>
                    <td>NeutronUpdateFloatingIp</td>
                    <td>Update the floating IP address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowFloatingIp</td>
                    <td>Query floating IP address details, including the floating IP address status, ID of the router to which the floating IP address belongs, and external network ID of the floating IP address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteFloatingIp</td>
                    <td>Delete a specified floating IP address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListFloatingIps</td>
                    <td>Query all the floating IP addresses that the tenant who submits the request has the permission to perform operations on.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateFloatingIp</td>
                    <td>UUID of the external network for creating a floating IP address. Obtain the UUID using GET /v2.0/networks?router:external=True or neutron net-external-list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Operate EIPs in batches</td>
                    <td>BatchDisassociatePublicips</td>
                    <td>Unbinding EIPs in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePublicIp</td>
                    <td>Deleting EIPs in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreatePublicips</td>
                    <td>Creating EIPs in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Public pool</td>
                    <td>ListPublicipPool</td>
                    <td>Query all public IP address pools</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCommonPools</td>
                    <td>Query the public pool list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPublicipPool</td>
                    <td>Query the details of a public IP address pool</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query Job Status</td>
                    <td>ShowResourcesJobDetail</td>
                    <td>Interface for querying the job status</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota Management</td>
                    <td>ListQuotas</td>
                    <td>Obtain quota information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Shared bandwidth type</td>
                    <td>ListShareBandwidthTypes</td>
                    <td>Query the list of shared bandwidth types of a specified tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">virtual igw</td>
                    <td>ListTenantVpcIgws</td>
                    <td>Query the virtual IGW list of a specified tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTenantVpcIgw</td>
                    <td>Delete a virtual IGW</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTenantVpcIgw</td>
                    <td>Create a virtual IGW</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTenantVpcIgw</td>
                    <td>Modifying a virtual IGW</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInternalVpcIgw</td>
                    <td>Query virtual IGW details</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
