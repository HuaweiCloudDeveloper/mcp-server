# VPC MCP Server 


## Version
v0.1.0

## Overview

VPC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VPC. Full-chain management of VPC resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Auxiliary elastic NIC | DeleteSubNetworkInterface | Delete the secondary elastic NIC | To be tested |
|  | ListSubNetworkInterfaces | Query the list of auxiliary elastic NICs. A maximum of 2000 records can be returned at a time. | To be tested |
|  | CreateSubNetworkInterface | Create an auxiliary elastic NIC | To be tested |
|  | ShowSubNetworkInterfacesQuantity | Query the number of auxiliary elastic NICs | To be tested |
|  | BatchCreateSubNetworkInterface | Create secondary elastic NICs in batches | To be tested |
|  | ShowSubNetworkInterface | Query the details about the secondary elastic NIC | To be tested |
|  | UpdateSubNetworkInterface | Update the secondary elastic NIC | To be tested |
| FDR | UpdateFlowLog | Update FDR | To be tested |
|  | CreateFlowLog | Create an FDR. | To be tested |
|  | ShowFlowLog | Query FDR details | To be tested |
|  | ListFlowLogs | Query the list of all FDRs of the tenant that submits the request and filter the FDRs based on the filter criteria. | To be tested |
|  | DeleteFlowLog | Delete the FDR | To be tested |
| IP address group | ShowAddressGroup | Query the details of an address group. | To be tested |
|  | CreateAddressGroup | Create an address group | To be tested |
|  | ListAddressGroup | Query the address group list based on the filter criteria. | To be tested |
|  | DeleteIpAddressGroupForce | Forcibly delete an address group. When the address group to be deleted is associated with a security group rule, the associated security group rule will be deleted. | To be tested |
|  | DeleteAddressGroup | This command is used to delete an address group. Ensure that the address group is not referenced by other resources. | To be tested |
|  | UpdateAddressGroup | Update the address group. | To be tested |
| Network ACL | ShowFirewall | Query the network ACL details | To be tested |
|  | DeleteFirewall | Delete a network ACL | To be tested |
|  | UpdateFirewallRules | Network ACL Update Rule | To be tested |
|  | AssociateSubnetFirewall | Binding a Network ACL to a Subnet | To be tested |
|  | CreateFirewall | Create a network ACL | To be tested |
|  | AddFirewallRules | Adding a rule to a network ACL | To be tested |
|  | UpdateFirewall | Update the network ACL | To be tested |
|  | DisassociateSubnetFirewall | Unbinding a subnet from a network ACL | To be tested |
|  | RemoveFirewallRules | Deleting a Network ACL Rule | To be tested |
|  | ListFirewall | Query the network ACL list | To be tested |
| Network ACL Resource Tag Management | BatchCreateFirewallTags | Add labels to specified network ACL resource instances in batches. | To be tested |
|  | DeleteFirewallTag | Deletes the label information of a resource instance in a specified IP address group | To be tested |
|  | CreateFirewallTag | Adds a label to a resource instance in a specified IP address group. | To be tested |
|  | ListFirewallTags | Query the resource tag set of a tenant instance type in a specified project | To be tested |
|  | CountFirewallsByTags | Query the number of ACL instances by label filtering. | To be tested |
|  | ShowFirewallTags | Query the label information of a specified ACL instance | To be tested |
|  | ListFirewallsByTags | Query ACL instances by label filtering. | To be tested |
|  | BatchDeleteFirewallTags | This command is used to delete tags from specified network ACL resource instances in batches. | To be tested |
| OpenStack - API version information | ListApiVersion | All available API versions (only for native OpenStack APIs) are returned. | To be tested |
| OpenStack - Network ACL | NeutronListFirewallRules | Query information about all network ACL rules that the tenant who submits the request has the permission to perform operations on. A maximum of 2000 data records can be returned in a query. If the number of data records exceeds 2000, a page-by-page flag is returned. | To be tested |
|  | NeutronShowFirewallPolicy | Query the details about a specific network ACL policy. | To be tested |
|  | NeutronDeleteFirewallPolicy | Delete a network ACL policy. | To be tested |
|  | NeutronUpdateFirewallGroup | Update the network ACL group. | To be tested |
|  | NeutronDeleteFirewallRule | Delete a network ACL rule. | To be tested |
|  | NeutronShowFirewallGroup | Query the details of a specific network ACL group. | To be tested |
|  | NeutronCreateFirewallGroup | Create a network ACL group | To be tested |
|  | NeutronRemoveFirewallRule | Removes a network ACL rule from a network ACL policy. | To be tested |
|  | NeutronAddFirewallRule | Insert a network ACL rule to a network ACL policy. | To be tested |
|  | NeutronUpdateFirewallPolicy | Update the network ACL policy. | To be tested |
|  | NeutronListFirewallGroups | Query information about all network ACL groups that the tenant who submits the request has the permission to perform operations on. A maximum of 2000 data records can be returned in a query. If the number of data records exceeds 2000, the page-by-page flag will be returned. | To be tested |
|  | NeutronCreateFirewallRule | Create a network ACL rule. | To be tested |
|  | NeutronCreateFirewallPolicy | Create a network ACL policy. | To be tested |
|  | NeutronListFirewallPolicies | Query information about all network ACL policies that the tenant who submits the request has the permission to operate. A maximum of 2000 data records can be returned in a query. If the number of data records exceeds 2000, a page-by-page flag will be returned. | To be tested |
|  | NeutronUpdateFirewallRule | Update the network ACL rule. | To be tested |
|  | NeutronDeleteFirewallGroup | Delete a network ACL group | To be tested |
|  | NeutronShowFirewallRule | Query the ACL rule for a specific network. | To be tested |
| OpenStack - Port | NeutronDeletePort | Delete a port. | To be tested |
|  | NeutronUpdatePort | Update Port | To be tested |
|  | NeutronShowPort | Query port details. | To be tested |
|  | NeutronListPorts | Query all ports of the tenant that submits the request. A maximum of 2000 records can be returned at a time. If the number of records exceeds 2000, a pagination flag is returned. For details about pagination query, see pagination query. | To be tested |
|  | NeutronCreatePort | Create a port. | To be tested |
| OpenStack - Subnet | NeutronShowSubnet | Query subnet details | To be tested |
|  | NeutronCreateSubnet | Create a subnet. | To be tested |
|  | NeutronUpdateSubnet | Update Subnet | To be tested |
|  | NeutronListSubnets | Query all subnets of the tenant that submits the request. A maximum of 2000 records can be returned at a time. If the number of records exceeds 2000, a pagination flag is returned. For details about pagination query, see pagination query. | To be tested |
|  | NeutronDeleteSubnet | Delete a subnet | To be tested |
| OpenStack-Network | NeutronShowNetwork | Query the details of a specified network | To be tested |
|  | NeutronDeleteNetwork | Delete a network | To be tested |
|  | NeutronCreateNetwork | Create a network | To be tested |
|  | NeutronListNetworks | Query all networks of the tenant that submits the request. A maximum of 2000 data records can be returned at a time. If the number of data records exceeds 2000, a pagination mark is returned. For details about pagination query, see pagination query. | To be tested |
|  | NeutronUpdateNetwork | Update the network | To be tested |
| OpenStack-Security Group | NeutronCreateSecurityGroupRule | Create a security group rule | To be tested |
|  | NeutronShowSecurityGroup | Query security group details | To be tested |
|  | NeutronCreateSecurityGroup | Create a security group | To be tested |
|  | NeutronShowSecurityGroupRule | Query security group rule details. | To be tested |
|  | NeutronListSecurityGroupRules | Query all security group rules that the tenant who submits the request has the permission to view. A maximum of 2000 data records can be returned in a query. If the number of data records exceeds 2000, a paged mark is returned. For details about pagination query, see pagination query. | To be tested |
|  | NeutronUpdateSecurityGroup | Update a security group | To be tested |
|  | NeutronListSecurityGroups | Query all security groups of the tenant that submits the request. A maximum of 2000 records can be returned at a time. If the number of records exceeds 2000, a pagination mark is returned. For details about pagination query, see pagination query. | To be tested |
|  | NeutronDeleteSecurityGroup | Delete a security group | To be tested |
|  | NeutronDeleteSecurityGroupRule | Deleting a security group rule | To be tested |
| OpenStack-router | NeutronRemoveRouterInterface | Delete a router interface. | To be tested |
|  | NeutronCreateRouter | Create a router. | To be tested |
|  | NeutronShowRouter | Query router details. | To be tested |
|  | NeutronUpdateRouter | Update the router. | To be tested |
|  | NeutronListRouters | Query information about all routers that the tenant who submits the request has the permission to perform operations. A maximum of 2000 records can be returned at a time. If the number of records exceeds 2000 records, a pagination flag is returned. | To be tested |
|  | NeutronAddRouterInterface | Add a router interface. | To be tested |
|  | NeutronDeleteRouter | Delete a router | To be tested |
| Port | UpdatePort | Update the port number. | To be tested |
|  | CreatePort | Create a port. | To be tested |
|  | ShowPort | Query the details of a single port. | To be tested |
|  | AddSecurityGroups | Port insertion into a security group | To be tested |
|  | DeletePort | Delete a port. | To be tested |
|  | RemoveSecurityGroups | Removing a security group from a port | To be tested |
|  | ListPorts | Query all ports of the tenant that submits the request. A maximum of 2000 records can be returned at a time. | To be tested |
| Port Resource Label Management | CountPortsByTags | Query the number of port instances by label. | To be tested |
|  | BatchCreatePortTags | Add tags to specified ports in batches. | To be tested |
|  | ListPortsByTags | Query ports by label. | To be tested |
|  | DeletePortTag | Delete label information about a specified port | To be tested |
|  | CreatePortTag | Add label information to the specified port resource instance | To be tested |
|  | ListPortTags | Query the collection of all resource tags of a tenant instance type in a specified project. | To be tested |
|  | BatchDeletePortTags | This command is used to delete labels for specified port resource instances in batches. | To be tested |
|  | ShowPortTags | Query the label information about a specified port. | To be tested |
| Private IP | DeletePrivateip | Delete a private IP address. | To be tested |
|  | CreatePrivateip | Apply for a private IP address. | To be tested |
|  | ListPrivateips | Query the list of private IP addresses in a specified subnet. | To be tested |
|  | ShowPrivateip | Query a private IP address by using a specified ID. | To be tested |
| Query network IP address usage | ShowNetworkIpAvailabilities | Displays the IPv4 address usage on a specified network. | To be tested |
| Quota | ShowQuota | Query the network resource quotas of a single tenant in the VPC service, including the VPC quota, subnet quota, security group quota, security group rule quota, EIP quota, and VPN quota. | To be tested |
| Routing table | ShowRouteTable | Query the routing table details | To be tested |
|  | UpdateRouteTable | Updates the routing table, including the name and description of the routing table, and adds, updates, and deletes routing entries. | To be tested |
|  | ListRouteTables | Query the list of all routing tables of the account that submits the request and filter the routing tables based on the filtering conditions. | To be tested |
|  | AssociateRouteTable | Associate the routing table with the subnet. A subnet is associated with routing table A and then associated with routing table B. It does not need to be disassociated from routing table A and then associated with routing table B. | To be tested |
|  | CreateRouteTable | Create a routing table | To be tested |
|  | DisassociateRouteTable | Disassociating a Subnet from the Routing Table | To be tested |
|  | DeleteRouteTable | Delete the routing table | To be tested |
| Security Group Resource Tag Management | ListSecurityGroupTags | Query all tags of a tenant in a specified region and instance type. | To be tested |
|  | DeleteSecurityGroupTag | Deletes the tag information of a specified security group resource instance. | To be tested |
|  | BatchCreateSecurityGroupTags | This API is used to add tags to specified security group resource instances in batches. | To be tested |
|  | CreateSecurityGroupTag | This API is used to add tags to a specified security group resource instance. | To be tested |
|  | ShowSecurityGroupTags | Query the tag information of a specified security group instance. | To be tested |
|  | ListSecurityGroupsByTags | Filter instances by label | To be tested |
|  | BatchDeleteSecurityGroupTags | Delete tags for specified security group resource instances in batches | To be tested |
| Security group | ListSecurityGroups | Query the security group list of a tenant. | To be tested |
|  | CreateSecurityGroup | Create a security group | To be tested |
|  | DeleteSecurityGroup | Delete a security group | To be tested |
|  | ShowSecurityGroup | Query details about a security group | To be tested |
|  | UpdateSecurityGroup | Update a security group | To be tested |
| Security group rule | ListSecurityGroupRules | Query the security group rule list | To be tested |
|  | DeleteSecurityGroupRule | Deleting a security group rule | To be tested |
|  | ShowSecurityGroupRule | Query a security group rule | To be tested |
|  | BatchCreateSecurityGroupRules | Create security group rules in batches under a specified security group | To be tested |
|  | CreateSecurityGroupRule | Create a security group rule | To be tested |
| Subnet | ShowSubnet | Query subnet details. | To be tested |
|  | UpdateSubnet | Update the subnet. | To be tested |
|  | CreateSubnet | Create a subnet. | To be tested |
|  | DeleteSubnet | Delete a subnet | To be tested |
|  | ListSubnets | Query the subnet list | To be tested |
| Subnet Resource Tag Management | BatchDeleteSubnetTags | Delete tags for specified subnet resource instances in batches | To be tested |
|  | ShowSubnetTags | Query the label information of a specified subnet instance. | To be tested |
|  | ListSubnetTags | Query all tags of a tenant in a specified region and instance type. | To be tested |
|  | ListSubnetsByTags | Filter instances by label | To be tested |
|  | DeleteSubnetTag | Deletes the label information of a specified subnet resource instance. | To be tested |
|  | BatchCreateSubnetTags | Add tags to specified subnet resource instances in batches. | To be tested |
|  | CreateSubnetTag | Add a label to a specified subnet resource instance. | To be tested |
| Traffic mirroring filter criteria | ListTrafficMirrorFilters | Query the filter criteria list of traffic mirroring | To be tested |
|  | UpdateTrafficMirrorFilter | Update the filter criteria for traffic mirroring | To be tested |
|  | CreateTrafficMirrorFilter | Create a filter condition for traffic mirroring | To be tested |
|  | ShowTrafficMirrorFilter | Query the details of the traffic mirroring filter criteria | To be tested |
|  | DeleteTrafficMirrorFilter | Delete the filter criteria for traffic mirroring. | To be tested |
| Traffic mirroring filtering rule | UpdateTrafficMirrorFilterRule | Updating a traffic mirroring filtering rule | To be tested |
|  | ShowTrafficMirrorFilterRule | Query details about a traffic mirroring filtering rule | To be tested |
|  | CreateTrafficMirrorFilterRule | Create a traffic mirroring filtering rule | To be tested |
|  | DeleteTrafficMirrorFilterRule | Delete a traffic mirroring filtering rule | To be tested |
|  | ListTrafficMirrorFilterRules | Query the traffic mirroring filtering rule list | To be tested |
| Traffic mirroring session | AddSourcesToTrafficMirrorSession | Adding a mirror source to a traffic mirroring session | To be tested |
|  | CreateTrafficMirrorSession | Create a traffic mirroring session | To be tested |
|  | ShowTrafficMirrorSession | Query details about a traffic mirroring session | To be tested |
|  | UpdateTrafficMirrorSession | Updating a traffic mirroring session | To be tested |
|  | DeleteTrafficMirrorSession | Delete a traffic mirroring session | To be tested |
|  | RemoveSourcesFromTrafficMirrorSession | The mirror source is removed from the traffic mirroring session. | To be tested |
|  | ListTrafficMirrorSessions | Query the traffic mirroring session list | To be tested |
| VPC | DeleteVpc | Delete a VPC. | To be tested |
|  | UpdateVpc | Updates a VPC. | To be tested |
|  | CreateVpc | Create a VPC. | To be tested |
|  | ListVpcs | Query the VPC list | To be tested |
|  | ShowVpc | Query VPC details | To be tested |
|  | AddVpcExtendCidr | Adding the extended VPC network segment | To be tested |
|  | RemoveVpcExtendCidr | Remove the extended VPC network segment. | To be tested |
| VPC Resource Tag Management | BatchDeleteVpcTags | This API is used to delete tags for specified VPC resource instances in batches. | To be tested |
|  | ListVpcsByTags | Filter instances by label. | To be tested |
|  | ListVpcTags | Query all tags of a tenant in a specified region and instance type. | To be tested |
|  | BatchCreateVpcTags | This API is used to add tags to specified VPC resource instances in batches. | To be tested |
|  | CreateVpcResourceTag | Adds a tag to a specified VPC resource instance. | To be tested |
|  | DeleteVpcTag | Deletes the tag information of a specified VPC resource instance. | To be tested |
|  | ShowVpcTags | Query the tag information of a specified VPC instance. | To be tested |
| VPC Route | DeleteVpcRoute | Delete a route | To be tested |
|  | ShowVpcRoute | Query route details | To be tested |
|  | ListVpcRoutes | Query the list of all routes of the tenant that submits the request and filter the routes based on the filter criteria. | To be tested |
|  | CreateVpcRoute | Create a route | To be tested |
| VPC peering connection | ShowVpcPeering | Query details about a VPC peering connection. | To be tested |
|  | DeleteVpcPeering | Delete the VPC peering connection. | To be tested |
|  | AcceptVpcPeering | The VPC of tenant A applies for a VPC peering connection with the VPC of tenant B. Tenant B needs to accept the request. This API is used by a tenant to accept the VPC peering connection request from another tenant. | To be tested |
|  | ListVpcPeerings | Query all VPC peering connections of the tenant that submits the request. Filter by the filter criteria. | To be tested |
|  | CreateVpcPeering | Create a VPC peering connection. | To be tested |
|  | UpdateVpcPeering | Update the VPC peering connection. | To be tested |
|  | RejectVpcPeering | The VPC of tenant A applies for establishing a VPC peering connection with the VPC of tenant B. Tenant B needs to accept the request. This API is used by a tenant to reject the VPC peering connection request initiated by other tenants. | To be tested |

