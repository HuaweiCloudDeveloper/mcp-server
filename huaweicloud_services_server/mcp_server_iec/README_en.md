# IEC MCP Server 


## Version
v0.1.0

## Overview

IEC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IEC. Full-chain management of IEC resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Bandwidth | ListBandwidths | Query the bandwidth list. | To be tested |
|  | ListBandwidthTypes | Query the shared bandwidth type list. | To be tested |
|  | DeleteBandwidth | Delete the bandwidth. | To be tested |
|  | ShowBandwidth | Query bandwidth details. | To be tested |
|  | UpdateBandwidth | Update the bandwidth. | To be tested |
| Deployment Management | ListDeployments | Query the deployment list | To be tested |
|  | DeleteDeployment | Delete an application deployment | To be tested |
| EIP | ListPublicIps | Obtain the EIP list. | To be tested |
|  | CreatePublicIp | Create an EIP based on the user request. | To be tested |
|  | DeletePublicIp | Delete an EIP based on the EIP ID. | To be tested |
|  | UpdatePublicIp | Updates EIP information, which is used to unbind EIPs and bind relationships between EIPs and VIPs. | To be tested |
|  | ShowPublicIp | Obtain the EIP details. | To be tested |
| Edge Instance | DeleteNics | Delete a network adapter. | To be tested |
|  | AddNics | Add a network adapter. | To be tested |
|  | ChangeOs | Switch the OS of an edge instance. After the edge instance is created, the OS can be reinstalled with the IP address and data disk unchanged. | To be tested |
|  | BatchStartInstance | Start edge instances in batches. | To be tested |
|  | DeleteInstances | This API is used to delete edge instances in batches. | To be tested |
|  | BatchRebootInstance | Restart edge instances in batches. | To be tested |
| Edge Mirror | DeleteImage | Delete the edge private image with the specified ID. | To be tested |
|  | ListCloudImages | Query the list of visible images of a tenant in a cloud region. | To be tested |
|  | ShowImage | Query image details. | To be tested |
|  | RebuildImage | Retry the edge mirroring task. | To be tested |
| Edge Site | ListSites | Query the edge site list. | To be tested |
| Edge disk | ListVolume | Query the disk list. | To be tested |
|  | ShowVolumeTypes | Query the disk type list. | To be tested |
|  | ShowVolume | Query disk details. | To be tested |
| Edge service | CreateDeployment | To facilitate unified management and resource management across edge sites, IEC defines edge services based on service scenarios. | To be tested |
|  | ShowEdgeCloud | Query the details about the edge service. | To be tested |
|  | ExecuteDeployment | Execute the deployment plan and create an edge service. A single tenant can create 10 edge services by default. | To be tested |
|  | DeleteEdgeCloud | Delete the edge service. | To be tested |
|  | ExpandEdgecloud | Execute the deployment plan to expand the capacity of edge services. | To be tested |
|  | ListEdgeCloud | Query the edge service list. | To be tested |
| Engine version and specification | ListFlavors | Query database specifications. | To be tested |
| Exclusive Instance Management | CreateInstance | Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore | To be tested |
|  | ShowInstance | Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
| Instance management | BatchStopInstance | Stopping instances in batches | To be tested |
| Key Pair Management | ListKeypairs | Query the SSH key pair list | To be tested |
|  | DeleteKeypair | Delete the SSH key pair. | To be tested |
|  | CreateKeypair | Create and import an SSH key pair | To be tested |
| Key pair | ShowKeypair | Query the key information list. | To be tested |
| Lifecycle Management | ListInstances | Query the instance list of a tenant. Query by condition is supported. | To be tested |
|  | UpdateInstance | Modifies the name and description of an instance. | To be tested |
| Mirror | ListImages | Query the image list based on different conditions. | To be tested |
|  | CreateImage | This API is used to create private images. The following functions are supported: | To be tested |
|  | RegisterImage | This API is used to register an image file as an uninitialized private image on the cloud platform. | To be tested |
| Misc | ListQuota | Query the resource sharing quota information of the current account. | To be tested |
| Network ACL | ShowFirewall | Query the network ACL details | To be tested |
|  | CreateFirewall | Create a network ACL | To be tested |
|  | DeleteFirewall | Delete a network ACL | To be tested |
|  | ListFirewalls | Query the network ACL list. | To be tested |
|  | UpdateFirewall | Update the network ACL | To be tested |
|  | UpdateFirewallRule | Update the network ACL rule. | To be tested |
| Port | UpdatePort | Update the port number. | To be tested |
|  | ShowPort | Query the details of a single port. | To be tested |
|  | ListPorts | Query all ports of the tenant that submits the request. A maximum of 2000 records can be returned at a time. | To be tested |
|  | CreatePort | Create a port. | To be tested |
|  | DeletePort | Delete a port. | To be tested |
| Routing table | DisassociateSubnet | Disassociate the routing table from the subnet | To be tested |
|  | AssociateSubnet | Associate the routing table with the subnet | To be tested |
|  | DeleteRoutes | Delete a route | To be tested |
|  | UpdateRoutes | Update routing information | To be tested |
|  | ListRoutes | Query the route list | To be tested |
|  | ListRoutetables | Query the route list | To be tested |
|  | CreateRoutes | Create a route | To be tested |
|  | UpdateRoutetable | Updates the basic information about the routing table | To be tested |
|  | ShowRoutetable | Query routing table details | To be tested |
|  | DeleteRoutetable | Delete the routing table | To be tested |
|  | CreateRoutetable | Create the routing table | To be tested |
| Security group | ListSecurityGroups | Query the security group list of a tenant. | To be tested |
|  | ShowSecurityGroup | Query details about a security group | To be tested |
|  | CreateSecurityGroup | Create a security group | To be tested |
|  | DeleteSecurityGroup | Delete a security group | To be tested |
| Security group rule | DeleteSecurityGroupRule | Deleting a security group rule | To be tested |
|  | CreateSecurityGroupRule | Create a security group rule | To be tested |
|  | ListSecurityGroupRules | Query the security group rule list | To be tested |
|  | ShowSecurityGroupRule | Query a security group rule | To be tested |
| Subnet | UpdateSubnet | Update the subnet. | To be tested |
|  | DeleteSubnet | Delete a subnet | To be tested |
|  | ListRelatedRoutetables | Query the routing table associated with the subnet. | To be tested |
|  | ListSubnets | Query the subnet list | To be tested |
|  | CreateSubnet | Create a subnet. | To be tested |
|  | ShowSubnet | Query subnet details. | To be tested |
| VPC | DeleteVpc | Delete a VPC. | To be tested |
|  | UpdateVpc | Updates a VPC. | To be tested |
|  | CreateVpc | Create a VPC. | To be tested |
|  | ListVpcs | Query the VPC list | To be tested |
|  | ShowVpc | Query VPC details | To be tested |
| port | AttachVipBandwidth | A virtual IPv6 address or a private IPv6 address is bound to a bandwidth, which supports public network access. | To be tested |
|  | DetachVipBandwidth | Unbind bandwidth from a virtual IPv6 address or private IPv6 address. | To be tested |

