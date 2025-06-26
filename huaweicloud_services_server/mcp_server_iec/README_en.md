# IEC MCP Server 


## Version
v0.1.0

## Overview

IEC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IEC. Full-chain management of IEC resources can be carried out based on natural language.

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
                    <td rowspan="5">Bandwidth</td>
                    <td>ListBandwidths</td>
                    <td>Query the bandwidth list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidthTypes</td>
                    <td>Query the shared bandwidth type list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBandwidth</td>
                    <td>Delete the bandwidth.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBandwidth</td>
                    <td>Query bandwidth details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBandwidth</td>
                    <td>Update the bandwidth.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Deployment Management</td>
                    <td>ListDeployments</td>
                    <td>Query the deployment list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeployment</td>
                    <td>Delete an application deployment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">EIP</td>
                    <td>ListPublicIps</td>
                    <td>Obtain the EIP list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePublicIp</td>
                    <td>Create an EIP based on the user request.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePublicIp</td>
                    <td>Delete an EIP based on the EIP ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublicIp</td>
                    <td>Updates EIP information, which is used to unbind EIPs and bind relationships between EIPs and VIPs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPublicIp</td>
                    <td>Obtain the EIP details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Edge Instance</td>
                    <td>DeleteNics</td>
                    <td>Delete a network adapter.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddNics</td>
                    <td>Add a network adapter.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeOs</td>
                    <td>Switch the OS of an edge instance. After the edge instance is created, the OS can be reinstalled with the IP address and data disk unchanged.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartInstance</td>
                    <td>Start edge instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstances</td>
                    <td>This API is used to delete edge instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRebootInstance</td>
                    <td>Restart edge instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Edge Mirror</td>
                    <td>DeleteImage</td>
                    <td>Delete the edge private image with the specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudImages</td>
                    <td>Query the list of visible images of a tenant in a cloud region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImage</td>
                    <td>Query image details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebuildImage</td>
                    <td>Retry the edge mirroring task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Edge Site</td>
                    <td>ListSites</td>
                    <td>Query the edge site list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Edge disk</td>
                    <td>ListVolume</td>
                    <td>Query the disk list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVolumeTypes</td>
                    <td>Query the disk type list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVolume</td>
                    <td>Query disk details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Edge service</td>
                    <td>CreateDeployment</td>
                    <td>To facilitate unified management and resource management across edge sites, IEC defines edge services based on service scenarios.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeCloud</td>
                    <td>Query the details about the edge service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteDeployment</td>
                    <td>Execute the deployment plan and create an edge service. A single tenant can create 10 edge services by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeCloud</td>
                    <td>Delete the edge service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandEdgecloud</td>
                    <td>Execute the deployment plan to expand the capacity of edge services.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeCloud</td>
                    <td>Query the edge service list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Engine version and specification</td>
                    <td>ListFlavors</td>
                    <td>Query database specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Exclusive Instance Management</td>
                    <td>CreateInstance</td>
                    <td>Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Instance management</td>
                    <td>BatchStopInstance</td>
                    <td>Stopping instances in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Key Pair Management</td>
                    <td>ListKeypairs</td>
                    <td>Query the SSH key pair list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKeypair</td>
                    <td>Delete the SSH key pair.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKeypair</td>
                    <td>Create and import an SSH key pair</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Key pair</td>
                    <td>ShowKeypair</td>
                    <td>Query the key information list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Lifecycle Management</td>
                    <td>ListInstances</td>
                    <td>Query the instance list of a tenant. Query by condition is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstance</td>
                    <td>Modifies the name and description of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Mirror</td>
                    <td>ListImages</td>
                    <td>Query the image list based on different conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateImage</td>
                    <td>This API is used to create private images. The following functions are supported:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterImage</td>
                    <td>This API is used to register an image file as an uninitialized private image on the cloud platform.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Misc</td>
                    <td>ListQuota</td>
                    <td>Query the resource sharing quota information of the current account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Network ACL</td>
                    <td>ShowFirewall</td>
                    <td>Query the network ACL details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFirewall</td>
                    <td>Create a network ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFirewall</td>
                    <td>Delete a network ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFirewalls</td>
                    <td>Query the network ACL list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFirewall</td>
                    <td>Update the network ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFirewallRule</td>
                    <td>Update the network ACL rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Port</td>
                    <td>UpdatePort</td>
                    <td>Update the port number.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPort</td>
                    <td>Query the details of a single port.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPorts</td>
                    <td>Query all ports of the tenant that submits the request. A maximum of 2000 records can be returned at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePort</td>
                    <td>Create a port.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePort</td>
                    <td>Delete a port.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Routing table</td>
                    <td>DisassociateSubnet</td>
                    <td>Disassociate the routing table from the subnet</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateSubnet</td>
                    <td>Associate the routing table with the subnet</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRoutes</td>
                    <td>Delete a route</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRoutes</td>
                    <td>Update routing information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRoutes</td>
                    <td>Query the route list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRoutetables</td>
                    <td>Query the route list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRoutes</td>
                    <td>Create a route</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRoutetable</td>
                    <td>Updates the basic information about the routing table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRoutetable</td>
                    <td>Query routing table details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRoutetable</td>
                    <td>Delete the routing table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRoutetable</td>
                    <td>Create the routing table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Security group</td>
                    <td>ListSecurityGroups</td>
                    <td>Query the security group list of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityGroup</td>
                    <td>Query details about a security group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityGroup</td>
                    <td>Create a security group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityGroup</td>
                    <td>Delete a security group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Security group rule</td>
                    <td>DeleteSecurityGroupRule</td>
                    <td>Deleting a security group rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityGroupRule</td>
                    <td>Create a security group rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityGroupRules</td>
                    <td>Query the security group rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityGroupRule</td>
                    <td>Query a security group rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Subnet</td>
                    <td>UpdateSubnet</td>
                    <td>Update the subnet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubnet</td>
                    <td>Delete a subnet</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRelatedRoutetables</td>
                    <td>Query the routing table associated with the subnet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubnets</td>
                    <td>Query the subnet list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubnet</td>
                    <td>Create a subnet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubnet</td>
                    <td>Query subnet details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">VPC</td>
                    <td>DeleteVpc</td>
                    <td>Delete a VPC.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpc</td>
                    <td>Updates a VPC.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpc</td>
                    <td>Create a VPC.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcs</td>
                    <td>Query the VPC list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpc</td>
                    <td>Query VPC details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">port</td>
                    <td>AttachVipBandwidth</td>
                    <td>A virtual IPv6 address or a private IPv6 address is bound to a bandwidth, which supports public network access.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachVipBandwidth</td>
                    <td>Unbind bandwidth from a virtual IPv6 address or private IPv6 address.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
