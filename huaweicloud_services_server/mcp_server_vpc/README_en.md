# VPC MCP Server 


## Version
v0.1.0

## Overview

VPC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VPC. Full-chain management of VPC resources can be carried out based on natural language.

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
                    <td rowspan="7">Auxiliary elastic NIC</td>
                    <td>DeleteSubNetworkInterface</td>
                    <td>Delete the secondary elastic NIC</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubNetworkInterfaces</td>
                    <td>Query the list of auxiliary elastic NICs. A maximum of 2000 records can be returned at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubNetworkInterface</td>
                    <td>Create an auxiliary elastic NIC</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubNetworkInterfacesQuantity</td>
                    <td>Query the number of auxiliary elastic NICs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateSubNetworkInterface</td>
                    <td>Create secondary elastic NICs in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubNetworkInterface</td>
                    <td>Query the details about the secondary elastic NIC</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubNetworkInterface</td>
                    <td>Update the secondary elastic NIC</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">FDR</td>
                    <td>UpdateFlowLog</td>
                    <td>Update FDR</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFlowLog</td>
                    <td>Create an FDR.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlowLog</td>
                    <td>Query FDR details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlowLogs</td>
                    <td>Query the list of all FDRs of the tenant that submits the request and filter the FDRs based on the filter criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFlowLog</td>
                    <td>Delete the FDR</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">IP address group</td>
                    <td>ShowAddressGroup</td>
                    <td>Query the details of an address group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAddressGroup</td>
                    <td>Create an address group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAddressGroup</td>
                    <td>Query the address group list based on the filter criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIpAddressGroupForce</td>
                    <td>Forcibly delete an address group. When the address group to be deleted is associated with a security group rule, the associated security group rule will be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAddressGroup</td>
                    <td>This command is used to delete an address group. Ensure that the address group is not referenced by other resources.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAddressGroup</td>
                    <td>Update the address group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Network ACL</td>
                    <td>ShowFirewall</td>
                    <td>Query the network ACL details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFirewall</td>
                    <td>Delete a network ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFirewallRules</td>
                    <td>Network ACL Update Rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateSubnetFirewall</td>
                    <td>Binding a Network ACL to a Subnet</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFirewall</td>
                    <td>Create a network ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddFirewallRules</td>
                    <td>Adding a rule to a network ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFirewall</td>
                    <td>Update the network ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateSubnetFirewall</td>
                    <td>Unbinding a subnet from a network ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveFirewallRules</td>
                    <td>Deleting a Network ACL Rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFirewall</td>
                    <td>Query the network ACL list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Network ACL Resource Tag Management</td>
                    <td>BatchCreateFirewallTags</td>
                    <td>Add labels to specified network ACL resource instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFirewallTag</td>
                    <td>Deletes the label information of a resource instance in a specified IP address group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFirewallTag</td>
                    <td>Adds a label to a resource instance in a specified IP address group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFirewallTags</td>
                    <td>Query the resource tag set of a tenant instance type in a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountFirewallsByTags</td>
                    <td>Query the number of ACL instances by label filtering.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFirewallTags</td>
                    <td>Query the label information of a specified ACL instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFirewallsByTags</td>
                    <td>Query ACL instances by label filtering.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteFirewallTags</td>
                    <td>This command is used to delete tags from specified network ACL resource instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">OpenStack - API version information</td>
                    <td>ListApiVersion</td>
                    <td>All available API versions (only for native OpenStack APIs) are returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">OpenStack - Network ACL</td>
                    <td>NeutronListFirewallRules</td>
                    <td>Query information about all network ACL rules that the tenant who submits the request has the permission to perform operations on. A maximum of 2000 data records can be returned in a query. If the number of data records exceeds 2000, a page-by-page flag is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowFirewallPolicy</td>
                    <td>Query the details about a specific network ACL policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteFirewallPolicy</td>
                    <td>Delete a network ACL policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateFirewallGroup</td>
                    <td>Update the network ACL group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteFirewallRule</td>
                    <td>Delete a network ACL rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowFirewallGroup</td>
                    <td>Query the details of a specific network ACL group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateFirewallGroup</td>
                    <td>Create a network ACL group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronRemoveFirewallRule</td>
                    <td>Removes a network ACL rule from a network ACL policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronAddFirewallRule</td>
                    <td>Insert a network ACL rule to a network ACL policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateFirewallPolicy</td>
                    <td>Update the network ACL policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListFirewallGroups</td>
                    <td>Query information about all network ACL groups that the tenant who submits the request has the permission to perform operations on. A maximum of 2000 data records can be returned in a query. If the number of data records exceeds 2000, the page-by-page flag will be returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateFirewallRule</td>
                    <td>Create a network ACL rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateFirewallPolicy</td>
                    <td>Create a network ACL policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListFirewallPolicies</td>
                    <td>Query information about all network ACL policies that the tenant who submits the request has the permission to operate. A maximum of 2000 data records can be returned in a query. If the number of data records exceeds 2000, a page-by-page flag will be returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateFirewallRule</td>
                    <td>Update the network ACL rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteFirewallGroup</td>
                    <td>Delete a network ACL group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowFirewallRule</td>
                    <td>Query the ACL rule for a specific network.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">OpenStack - Port</td>
                    <td>NeutronDeletePort</td>
                    <td>Delete a port.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdatePort</td>
                    <td>Update Port</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowPort</td>
                    <td>Query port details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListPorts</td>
                    <td>Query all ports of the tenant that submits the request. A maximum of 2000 records can be returned at a time. If the number of records exceeds 2000, a pagination flag is returned. For details about pagination query, see pagination query.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreatePort</td>
                    <td>Create a port.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">OpenStack - Subnet</td>
                    <td>NeutronShowSubnet</td>
                    <td>Query subnet details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateSubnet</td>
                    <td>Create a subnet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateSubnet</td>
                    <td>Update Subnet</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListSubnets</td>
                    <td>Query all subnets of the tenant that submits the request. A maximum of 2000 records can be returned at a time. If the number of records exceeds 2000, a pagination flag is returned. For details about pagination query, see pagination query.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteSubnet</td>
                    <td>Delete a subnet</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">OpenStack-Network</td>
                    <td>NeutronShowNetwork</td>
                    <td>Query the details of a specified network</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteNetwork</td>
                    <td>Delete a network</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateNetwork</td>
                    <td>Create a network</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListNetworks</td>
                    <td>Query all networks of the tenant that submits the request. A maximum of 2000 data records can be returned at a time. If the number of data records exceeds 2000, a pagination mark is returned. For details about pagination query, see pagination query.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateNetwork</td>
                    <td>Update the network</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">OpenStack-Security Group</td>
                    <td>NeutronCreateSecurityGroupRule</td>
                    <td>Create a security group rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowSecurityGroup</td>
                    <td>Query security group details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateSecurityGroup</td>
                    <td>Create a security group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowSecurityGroupRule</td>
                    <td>Query security group rule details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListSecurityGroupRules</td>
                    <td>Query all security group rules that the tenant who submits the request has the permission to view. A maximum of 2000 data records can be returned in a query. If the number of data records exceeds 2000, a paged mark is returned. For details about pagination query, see pagination query.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateSecurityGroup</td>
                    <td>Update a security group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListSecurityGroups</td>
                    <td>Query all security groups of the tenant that submits the request. A maximum of 2000 records can be returned at a time. If the number of records exceeds 2000, a pagination mark is returned. For details about pagination query, see pagination query.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteSecurityGroup</td>
                    <td>Delete a security group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteSecurityGroupRule</td>
                    <td>Deleting a security group rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">OpenStack-router</td>
                    <td>NeutronRemoveRouterInterface</td>
                    <td>Delete a router interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateRouter</td>
                    <td>Create a router.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowRouter</td>
                    <td>Query router details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateRouter</td>
                    <td>Update the router.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListRouters</td>
                    <td>Query information about all routers that the tenant who submits the request has the permission to perform operations. A maximum of 2000 records can be returned at a time. If the number of records exceeds 2000 records, a pagination flag is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronAddRouterInterface</td>
                    <td>Add a router interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteRouter</td>
                    <td>Delete a router</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Port</td>
                    <td>UpdatePort</td>
                    <td>Update the port number.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePort</td>
                    <td>Create a port.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPort</td>
                    <td>Query the details of a single port.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddSecurityGroups</td>
                    <td>Port insertion into a security group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePort</td>
                    <td>Delete a port.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveSecurityGroups</td>
                    <td>Removing a security group from a port</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPorts</td>
                    <td>Query all ports of the tenant that submits the request. A maximum of 2000 records can be returned at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Port Resource Label Management</td>
                    <td>CountPortsByTags</td>
                    <td>Query the number of port instances by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreatePortTags</td>
                    <td>Add tags to specified ports in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPortsByTags</td>
                    <td>Query ports by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePortTag</td>
                    <td>Delete label information about a specified port</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePortTag</td>
                    <td>Add label information to the specified port resource instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPortTags</td>
                    <td>Query the collection of all resource tags of a tenant instance type in a specified project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePortTags</td>
                    <td>This command is used to delete labels for specified port resource instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPortTags</td>
                    <td>Query the label information about a specified port.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Private IP</td>
                    <td>DeletePrivateip</td>
                    <td>Delete a private IP address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePrivateip</td>
                    <td>Apply for a private IP address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateips</td>
                    <td>Query the list of private IP addresses in a specified subnet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateip</td>
                    <td>Query a private IP address by using a specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query network IP address usage</td>
                    <td>ShowNetworkIpAvailabilities</td>
                    <td>Displays the IPv4 address usage on a specified network.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowQuota</td>
                    <td>Query the network resource quotas of a single tenant in the VPC service, including the VPC quota, subnet quota, security group quota, security group rule quota, EIP quota, and VPN quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Routing table</td>
                    <td>ShowRouteTable</td>
                    <td>Query the routing table details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRouteTable</td>
                    <td>Updates the routing table, including the name and description of the routing table, and adds, updates, and deletes routing entries.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRouteTables</td>
                    <td>Query the list of all routing tables of the account that submits the request and filter the routing tables based on the filtering conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRouteTable</td>
                    <td>Associate the routing table with the subnet. A subnet is associated with routing table A and then associated with routing table B. It does not need to be disassociated from routing table A and then associated with routing table B.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRouteTable</td>
                    <td>Create a routing table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateRouteTable</td>
                    <td>Disassociating a Subnet from the Routing Table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRouteTable</td>
                    <td>Delete the routing table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Security Group Resource Tag Management</td>
                    <td>ListSecurityGroupTags</td>
                    <td>Query all tags of a tenant in a specified region and instance type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityGroupTag</td>
                    <td>Deletes the tag information of a specified security group resource instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateSecurityGroupTags</td>
                    <td>This API is used to add tags to specified security group resource instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityGroupTag</td>
                    <td>This API is used to add tags to a specified security group resource instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityGroupTags</td>
                    <td>Query the tag information of a specified security group instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityGroupsByTags</td>
                    <td>Filter instances by label</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteSecurityGroupTags</td>
                    <td>Delete tags for specified security group resource instances in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Security group</td>
                    <td>ListSecurityGroups</td>
                    <td>Query the security group list of a tenant.</td>
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
                    <td>ShowSecurityGroup</td>
                    <td>Query details about a security group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityGroup</td>
                    <td>Update a security group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Security group rule</td>
                    <td>ListSecurityGroupRules</td>
                    <td>Query the security group rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityGroupRule</td>
                    <td>Deleting a security group rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityGroupRule</td>
                    <td>Query a security group rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateSecurityGroupRules</td>
                    <td>Create security group rules in batches under a specified security group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityGroupRule</td>
                    <td>Create a security group rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Subnet</td>
                    <td>ShowSubnet</td>
                    <td>Query subnet details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubnet</td>
                    <td>Update the subnet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubnet</td>
                    <td>Create a subnet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubnet</td>
                    <td>Delete a subnet</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubnets</td>
                    <td>Query the subnet list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Subnet Resource Tag Management</td>
                    <td>BatchDeleteSubnetTags</td>
                    <td>Delete tags for specified subnet resource instances in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubnetTags</td>
                    <td>Query the label information of a specified subnet instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubnetTags</td>
                    <td>Query all tags of a tenant in a specified region and instance type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubnetsByTags</td>
                    <td>Filter instances by label</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubnetTag</td>
                    <td>Deletes the label information of a specified subnet resource instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateSubnetTags</td>
                    <td>Add tags to specified subnet resource instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubnetTag</td>
                    <td>Add a label to a specified subnet resource instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Traffic mirroring filter criteria</td>
                    <td>ListTrafficMirrorFilters</td>
                    <td>Query the filter criteria list of traffic mirroring</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTrafficMirrorFilter</td>
                    <td>Update the filter criteria for traffic mirroring</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrafficMirrorFilter</td>
                    <td>Create a filter condition for traffic mirroring</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrafficMirrorFilter</td>
                    <td>Query the details of the traffic mirroring filter criteria</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrafficMirrorFilter</td>
                    <td>Delete the filter criteria for traffic mirroring.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Traffic mirroring filtering rule</td>
                    <td>UpdateTrafficMirrorFilterRule</td>
                    <td>Updating a traffic mirroring filtering rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrafficMirrorFilterRule</td>
                    <td>Query details about a traffic mirroring filtering rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrafficMirrorFilterRule</td>
                    <td>Create a traffic mirroring filtering rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrafficMirrorFilterRule</td>
                    <td>Delete a traffic mirroring filtering rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTrafficMirrorFilterRules</td>
                    <td>Query the traffic mirroring filtering rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Traffic mirroring session</td>
                    <td>AddSourcesToTrafficMirrorSession</td>
                    <td>Adding a mirror source to a traffic mirroring session</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrafficMirrorSession</td>
                    <td>Create a traffic mirroring session</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrafficMirrorSession</td>
                    <td>Query details about a traffic mirroring session</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTrafficMirrorSession</td>
                    <td>Updating a traffic mirroring session</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrafficMirrorSession</td>
                    <td>Delete a traffic mirroring session</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveSourcesFromTrafficMirrorSession</td>
                    <td>The mirror source is removed from the traffic mirroring session.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTrafficMirrorSessions</td>
                    <td>Query the traffic mirroring session list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">VPC</td>
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
                    <td>AddVpcExtendCidr</td>
                    <td>Adding the extended VPC network segment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveVpcExtendCidr</td>
                    <td>Remove the extended VPC network segment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">VPC Resource Tag Management</td>
                    <td>BatchDeleteVpcTags</td>
                    <td>This API is used to delete tags for specified VPC resource instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcsByTags</td>
                    <td>Filter instances by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcTags</td>
                    <td>Query all tags of a tenant in a specified region and instance type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateVpcTags</td>
                    <td>This API is used to add tags to specified VPC resource instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpcResourceTag</td>
                    <td>Adds a tag to a specified VPC resource instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpcTag</td>
                    <td>Deletes the tag information of a specified VPC resource instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpcTags</td>
                    <td>Query the tag information of a specified VPC instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">VPC Route</td>
                    <td>DeleteVpcRoute</td>
                    <td>Delete a route</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpcRoute</td>
                    <td>Query route details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcRoutes</td>
                    <td>Query the list of all routes of the tenant that submits the request and filter the routes based on the filter criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpcRoute</td>
                    <td>Create a route</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">VPC peering connection</td>
                    <td>ShowVpcPeering</td>
                    <td>Query details about a VPC peering connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpcPeering</td>
                    <td>Delete the VPC peering connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AcceptVpcPeering</td>
                    <td>The VPC of tenant A applies for a VPC peering connection with the VPC of tenant B. Tenant B needs to accept the request. This API is used by a tenant to accept the VPC peering connection request from another tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcPeerings</td>
                    <td>Query all VPC peering connections of the tenant that submits the request. Filter by the filter criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpcPeering</td>
                    <td>Create a VPC peering connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpcPeering</td>
                    <td>Update the VPC peering connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RejectVpcPeering</td>
                    <td>The VPC of tenant A applies for establishing a VPC peering connection with the VPC of tenant B. Tenant B needs to accept the request. This API is used by a tenant to reject the VPC peering connection request initiated by other tenants.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
