# ELB MCP Server 


## Version
v0.1.0

## Overview

ELB MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ELB. Full-chain management of ELB resources can be carried out based on natural language.

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
                    <td rowspan="4">active/standby Backend Server Group</td>
                    <td>ShowMasterSlavePool</td>
                    <td>Details of the active/standby backend server group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMasterSlavePools</td>
                    <td>List of active/standby backend server groups.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMasterSlavePool</td>
                    <td>Create a active/standby backend server group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMasterSlavePool</td>
                    <td>Delete the active/standby backend server group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Address Group Management</td>
                    <td>UpdateIpGroup</td>
                    <td>Modifying an IP address group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIpGroup</td>
                    <td>Create an IP address group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIpGroup</td>
                    <td>Query IP address group details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIpGroup</td>
                    <td>Delete an IP address group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Backend ECS</td>
                    <td>UpdateMember</td>
                    <td>Update backend ECS</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMembers</td>
                    <td>Query the backend ECSs in a backend ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMember</td>
                    <td>Delete a backend ECS</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMember</td>
                    <td>This API is used to query details about a backend ECS based on the specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Backend ECS group</td>
                    <td>UpdatePool</td>
                    <td>Update the backend ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPool</td>
                    <td>Query details about a backend ECS group based on the specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPools</td>
                    <td>Query the list of backend ECS groups.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePool</td>
                    <td>Create a backend ECS group. After multiple backend ECSs are added to a backend ECS group, requests are distributed among backend ECSs based on the load balancing algorithm and weight of the backend ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePool</td>
                    <td>Delete a backend ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Backend Server</td>
                    <td>CreateMemberHealthCheckJob</td>
                    <td>Create a backend server detection task. Check the configuration of the backend server, ACL rules, and security group rules.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllMembers</td>
                    <td>Query the list of backend servers in the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMember</td>
                    <td>Create a backend server.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateMembers</td>
                    <td>Create backend servers in a specified pool in batches. A maximum of 200 can be created at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMemberHealthCheckJob</td>
                    <td>Query the result of a backend server detection task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Backend server group</td>
                    <td>DeletePoolCascade</td>
                    <td>If a backend server group is deleted, all backend servers and health check items in the group will be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Certificate</td>
                    <td>ShowCertificatePrivateKeyEcho</td>
                    <td>Query the status of the certificate private key display switch, which can be enabled or disabled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificatePrivateKeyEcho</td>
                    <td>Enables or disables the display of the certificate private key field.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Certificate Management</td>
                    <td>ListCertificates</td>
                    <td>Query the certificate list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCertificate</td>
                    <td>Delete a certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCertificate</td>
                    <td>Modifying a Certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificate</td>
                    <td>Create Certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificate</td>
                    <td>Querying a certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Cloud Log</td>
                    <td>ShowLogtank</td>
                    <td>Cloud log details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogtanks</td>
                    <td>Query the cloud log list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Engine version and specification</td>
                    <td>ListFlavors</td>
                    <td>Query database specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Feature Configuration</td>
                    <td>ListLoadbalancerFeature</td>
                    <td>Query the feature configuration of a specified ELB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFeatureConfigs</td>
                    <td>Query the feature configuration of the ELB service of the current tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Forwarding Policy</td>
                    <td>CreateL7policy</td>
                    <td>Create the forwarding policy associated with the listener.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdatePoliciesPriority</td>
                    <td>Update the priorities of forwarding policies in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowL7Policy</td>
                    <td>Query details about a Layer 7 forwarding policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteL7policy</td>
                    <td>Delete a forwarding policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListL7Policies</td>
                    <td>Query the Layer 7 forwarding policy list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateL7Policy</td>
                    <td>The Layer 7 forwarding policy was updated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateL7policies</td>
                    <td>Update the forwarding policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Forwarding Rule</td>
                    <td>ListL7rules</td>
                    <td>Query the forwarding rule list associated with a specified forwarding policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateL7Rule</td>
                    <td>Update the Layer 7 forwarding rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateL7Rule</td>
                    <td>Create a Layer 7 forwarding rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowL7rule</td>
                    <td>Query details about forwarding rules associated with a specified forwarding policy based on the specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteL7rule</td>
                    <td>Deleting a forwarding rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Health Check</td>
                    <td>CreateHealthMonitor</td>
                    <td>Create a health check.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHealthmonitors</td>
                    <td>Query the health check details based on the specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHealthMonitor</td>
                    <td>Delete the health check.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHealthMonitor</td>
                    <td>Query the health check details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHealthmonitors</td>
                    <td>Query the health check list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHealthMonitor</td>
                    <td>Update the health check.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">IP address group</td>
                    <td>ShowIpGroupRelatedListeners</td>
                    <td>Query the listener list associated with an IP address group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteIpList</td>
                    <td>This API is used to delete the IP address list in an IP address group in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIpGroups</td>
                    <td>Query the IP address group list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIpList</td>
                    <td>Add an IP address to the IP address list of the IP address group, or update the description of the existing IP address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Image sharing</td>
                    <td>BatchUpdateMembers</td>
                    <td>This API is an extended API. It is used to update the status of multiple image members in batches when a user accepts or rejects multiple shared images.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteMembers</td>
                    <td>This API is an extended API and is used to cancel image sharing.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Listener</td>
                    <td>DeleteListenerForce</td>
                    <td>Delete a listener and delete its sub-resources in cascade mode. (Delete the listener, forwarding policy, and unbind the backend server group.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListListeners</td>
                    <td>Query the listener list. Filtered query and pagination query are supported. You can query a listener by the listener ID, protocol type, listening port number, and IP address of the associated backend ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateListener</td>
                    <td>Update the listener.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateListener</td>
                    <td>Create a listener bound to the load balancer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteListener</td>
                    <td>Delete the listener.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowListener</td>
                    <td>Query details about a listener based on the specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">Load Balancer</td>
                    <td>BatchAddAvailableZones</td>
                    <td>This API is used to add an AZ to the load balancer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoadbalancers</td>
                    <td>Query the load balancer list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLoadbalancer</td>
                    <td>Create an enhanced load balancer of the private network type. After the enhanced load balancer is created successfully, the interface returns details such as the ID, subnet ID, and IP address of the enhanced load balancer. To create an enhanced load balancer of the public network type, you need to call the API for creating a floating IP address and bind the floating IP address to the vip_port_id of the private network load balancer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLoadbalancersStatus</td>
                    <td>Query the load balancer status tree. You can use this API to query the listener, backend ECS group, backend ECS, health check, forwarding policy, and forwarding rule information associated with a load balancer and learn the topology of resources on the load balancer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLoadbalancer</td>
                    <td>Update the load balancer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CloneLoadbalancer</td>
                    <td>Copy an existing load balancer instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRemoveAvailableZones</td>
                    <td>Remove the AZ of the load balancer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLoadBalancerCascade</td>
                    <td>Delete a load balancer and delete its sub-resources in cascade mode. (Delete the load balancer and its bound listeners and backend servers.) Delete or unbind the EIPs associated with the backend server group and LB as required.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeLoadbalancer</td>
                    <td>Upgrade the load balancer type. A shared ELB can be upgraded to an exclusive ELB, but cannot be downgraded to a shared ELB.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLoadBalancer</td>
                    <td>Deletes a load balancer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateLoadBalancers</td>
                    <td>Create exclusive or shared load balancers in batches, including pay-per-use and yearly/monthly load balancers.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLoadBalancerStatus</td>
                    <td>Query the status tree of a load balancer, including the status of the load balancer and its associated subresources.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLoadBalancerForce</td>
                    <td>Delete a load balancer and delete its sub-resources in the cascade. (delete the load balancer and its bound listeners, backend server groups, and backend servers.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLoadBalancer</td>
                    <td>Query details about a load balancer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeLoadbalancerChargeMode</td>
                    <td>The billing mode of the load balancer is changed. Currently, the supported billing mode is changed to:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Log operation</td>
                    <td>DeleteLogtank</td>
                    <td>Unbind the cloud logs from a specified topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogtank</td>
                    <td>Bind a cloud log to a specified topic to record the message sending status of the topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogtank</td>
                    <td>This API is used to update the cloud logs bound to a specified topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Mirror Task</td>
                    <td>ShowJob</td>
                    <td>This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Preoccupied IP address</td>
                    <td>CountPreoccupyIpNum</td>
                    <td>Calculate the number of preoccupied IP addresses in the following scenarios:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query version operation</td>
                    <td>ListApiVersions</td>
                    <td>Query the TMS API version list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowQuota</td>
                    <td>Query the network resource quotas of a single tenant in the VPC service, including the VPC quota, subnet quota, security group quota, security group rule quota, EIP quota, and VPN quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Recycle bin</td>
                    <td>UpdateRecycleBinEnable</td>
                    <td>Enable or disable the recycle bin function. After the function is enabled, the deleted LB can go to the recycle bin. Otherwise, the LB will not go to the recycle bin and will be deleted and cannot be restored. Before closing the recycle bin, restore or destroy the instance in the recycle bin.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecycleBinLoadBalancers</td>
                    <td>Query the load balancers in the recycle bin.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRecycleLoadBalancer</td>
                    <td>Destroys the load balancer in the recycle bin. It cannot be restored after destruction.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRecycleBinPolicy</td>
                    <td>Updates the recycle bin configuration. If the recycle bin is not enabled, an error will be reported during the update.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreLoadbalancer</td>
                    <td>Restore the load balancer from the recycle bin</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecycleBin</td>
                    <td>Query the recycle bin configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Resource Quota Function</td>
                    <td>ListQuotaDetails</td>
                    <td>Query the resource quota of a user, including the VPC endpoint service and VPC endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Security Policy</td>
                    <td>ShowSecurityPolicy</td>
                    <td>Query details about a user-defined security policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityPolicies</td>
                    <td>Query the user-defined security policy list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityPolicy</td>
                    <td>Delete a user-defined security policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityPolicy</td>
                    <td>Update the user-defined security policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSystemSecurityPolicies</td>
                    <td>Query the system security policy list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityPolicy</td>
                    <td>Create a user-defined security policy. Specifies the security_policy_id parameter in the request parameter when creating an HTTPS listener to set a user-defined security policy for the listener.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Specification</td>
                    <td>ShowFlavor</td>
                    <td>Query the details about a specification.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Tag Management</td>
                    <td>BatchDeleteListenerTags</td>
                    <td>Delete listener tags in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowListenerTags</td>
                    <td>Query all tags of a specified listener.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteLoadbalancerTags</td>
                    <td>Deletes labels for load balancers in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListListenerTags</td>
                    <td>Query the tag list of all listeners in a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateListenerTags</td>
                    <td>Adds a tag to a specified listener.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateListenerTags</td>
                    <td>Add listener tags in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLoadbalancerTags</td>
                    <td>Delete the tag corresponding to a key of the load balancer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoadbalancerTags</td>
                    <td>Query the tag list of all load balancers in a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteListenerTags</td>
                    <td>Delete the tag corresponding to a key of the listener.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoadbalancersByTags</td>
                    <td>This API is used to query ELB instances by tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLoadbalancerTags</td>
                    <td>Query all tags of a specified load balancer</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListListenersByTags</td>
                    <td>Query the listener instance by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateLoadbalancerTags</td>
                    <td>Add labels for load balancers in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLoadbalancerTags</td>
                    <td>Adds a label to a specified load balancer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Task Center API</td>
                    <td>ListJobs</td>
                    <td>Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">VpnGateway</td>
                    <td>ListAvailabilityZones</td>
                    <td>Querying the AZ of the VPN gateway</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Whitelist</td>
                    <td>UpdateWhitelist</td>
                    <td>Update the trustlist. You can turn the trustlist on or off, or update the IP for access control.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWhitelist</td>
                    <td>Query trustlist details based on a specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWhitelists</td>
                    <td>Query the trustlist. Filtered query and pagination query are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWhitelist</td>
                    <td>Delete the whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWhitelist</td>
                    <td>Create a trustlist to control the access permission of listeners. If the trustlist function is enabled, only the bypassed IP addresses in the trustlist can access the backend service of the listener.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
