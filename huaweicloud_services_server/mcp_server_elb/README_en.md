# ELB MCP Server 


## Version
v0.1.0

## Overview

ELB MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ELB. Full-chain management of ELB resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
|  active/standby Backend Server Group | ShowMasterSlavePool | Details of the active/standby backend server group. | To be tested |
|  | ListMasterSlavePools | List of active/standby backend server groups. | To be tested |
|  | CreateMasterSlavePool | Create a active/standby backend server group. | To be tested |
|  | DeleteMasterSlavePool | Delete the active/standby backend server group. | To be tested |
| Address Group Management | UpdateIpGroup | Modifying an IP address group | To be tested |
|  | CreateIpGroup | Create an IP address group | To be tested |
|  | ShowIpGroup | Query IP address group details | To be tested |
|  | DeleteIpGroup | Delete an IP address group | To be tested |
| Backend ECS | UpdateMember | Update backend ECS | To be tested |
|  | ListMembers | Query the backend ECSs in a backend ECS group. | To be tested |
|  | DeleteMember | Delete a backend ECS | To be tested |
|  | ShowMember | This API is used to query details about a backend ECS based on the specified ID. | To be tested |
| Backend ECS group | UpdatePool | Update the backend ECS group. | To be tested |
|  | ShowPool | Query details about a backend ECS group based on the specified ID. | To be tested |
|  | ListPools | Query the list of backend ECS groups. | To be tested |
|  | CreatePool | Create a backend ECS group. After multiple backend ECSs are added to a backend ECS group, requests are distributed among backend ECSs based on the load balancing algorithm and weight of the backend ECS group. | To be tested |
|  | DeletePool | Delete a backend ECS group. | To be tested |
| Backend Server | CreateMemberHealthCheckJob | Create a backend server detection task. Check the configuration of the backend server, ACL rules, and security group rules. | To be tested |
|  | ListAllMembers | Query the list of backend servers in the current project. | To be tested |
|  | CreateMember | Create a backend server. | To be tested |
|  | BatchCreateMembers | Create backend servers in a specified pool in batches. A maximum of 200 can be created at a time. | To be tested |
|  | ShowMemberHealthCheckJob | Query the result of a backend server detection task. | To be tested |
| Backend server group | DeletePoolCascade | If a backend server group is deleted, all backend servers and health check items in the group will be deleted. | To be tested |
| Certificate | ShowCertificatePrivateKeyEcho | Query the status of the certificate private key display switch, which can be enabled or disabled. | To be tested |
|  | CreateCertificatePrivateKeyEcho | Enables or disables the display of the certificate private key field. | To be tested |
| Certificate Management | ListCertificates | Query the certificate list | To be tested |
|  | DeleteCertificate | Delete a certificate | To be tested |
|  | UpdateCertificate | Modifying a Certificate | To be tested |
|  | CreateCertificate | Create Certificate | To be tested |
|  | ShowCertificate | Querying a certificate | To be tested |
| Cloud Log | ShowLogtank | Cloud log details. | To be tested |
|  | ListLogtanks | Query the cloud log list. | To be tested |
| Engine version and specification | ListFlavors | Query database specifications. | To be tested |
| Feature Configuration | ListLoadbalancerFeature | Query the feature configuration of a specified ELB instance. | To be tested |
|  | ListFeatureConfigs | Query the feature configuration of the ELB service of the current tenant. | To be tested |
| Forwarding Policy | CreateL7policy | Create the forwarding policy associated with the listener. | To be tested |
|  | BatchUpdatePoliciesPriority | Update the priorities of forwarding policies in batches. | To be tested |
|  | ShowL7Policy | Query details about a Layer 7 forwarding policy. | To be tested |
|  | DeleteL7policy | Delete a forwarding policy | To be tested |
|  | ListL7Policies | Query the Layer 7 forwarding policy list. | To be tested |
|  | UpdateL7Policy | The Layer 7 forwarding policy was updated. | To be tested |
|  | UpdateL7policies | Update the forwarding policy | To be tested |
| Forwarding Rule | ListL7rules | Query the forwarding rule list associated with a specified forwarding policy | To be tested |
|  | UpdateL7Rule | Update the Layer 7 forwarding rule. | To be tested |
|  | CreateL7Rule | Create a Layer 7 forwarding rule. | To be tested |
|  | ShowL7rule | Query details about forwarding rules associated with a specified forwarding policy based on the specified ID. | To be tested |
|  | DeleteL7rule | Deleting a forwarding rule | To be tested |
| Health Check | CreateHealthMonitor | Create a health check. | To be tested |
|  | ShowHealthmonitors | Query the health check details based on the specified ID. | To be tested |
|  | DeleteHealthMonitor | Delete the health check. | To be tested |
|  | ShowHealthMonitor | Query the health check details. | To be tested |
|  | ListHealthmonitors | Query the health check list | To be tested |
|  | UpdateHealthMonitor | Update the health check. | To be tested |
| IP address group | ShowIpGroupRelatedListeners | Query the listener list associated with an IP address group. | To be tested |
|  | BatchDeleteIpList | This API is used to delete the IP address list in an IP address group in batches. | To be tested |
|  | ListIpGroups | Query the IP address group list. | To be tested |
|  | UpdateIpList | Add an IP address to the IP address list of the IP address group, or update the description of the existing IP address. | To be tested |
| Image sharing | BatchUpdateMembers | This API is an extended API. It is used to update the status of multiple image members in batches when a user accepts or rejects multiple shared images. | To be tested |
|  | BatchDeleteMembers | This API is an extended API and is used to cancel image sharing. | To be tested |
| Listener | DeleteListenerForce | Delete a listener and delete its sub-resources in cascade mode. (Delete the listener, forwarding policy, and unbind the backend server group.) | To be tested |
|  | ListListeners | Query the listener list. Filtered query and pagination query are supported. You can query a listener by the listener ID, protocol type, listening port number, and IP address of the associated backend ECS. | To be tested |
|  | UpdateListener | Update the listener. | To be tested |
|  | CreateListener | Create a listener bound to the load balancer. | To be tested |
|  | DeleteListener | Delete the listener. | To be tested |
|  | ShowListener | Query details about a listener based on the specified ID. | To be tested |
| Load Balancer | BatchAddAvailableZones | This API is used to add an AZ to the load balancer. | To be tested |
|  | ListLoadbalancers | Query the load balancer list. | To be tested |
|  | CreateLoadbalancer | Create an enhanced load balancer of the private network type. After the enhanced load balancer is created successfully, the interface returns details such as the ID, subnet ID, and IP address of the enhanced load balancer. To create an enhanced load balancer of the public network type, you need to call the API for creating a floating IP address and bind the floating IP address to the vip_port_id of the private network load balancer. | To be tested |
|  | ShowLoadbalancersStatus | Query the load balancer status tree. You can use this API to query the listener, backend ECS group, backend ECS, health check, forwarding policy, and forwarding rule information associated with a load balancer and learn the topology of resources on the load balancer. | To be tested |
|  | UpdateLoadbalancer | Update the load balancer. | To be tested |
|  | CloneLoadbalancer | Copy an existing load balancer instance. | To be tested |
|  | BatchRemoveAvailableZones | Remove the AZ of the load balancer. | To be tested |
|  | DeleteLoadBalancerCascade | Delete a load balancer and delete its sub-resources in cascade mode. (Delete the load balancer and its bound listeners and backend servers.) Delete or unbind the EIPs associated with the backend server group and LB as required. | To be tested |
|  | UpgradeLoadbalancer | Upgrade the load balancer type. A shared ELB can be upgraded to an exclusive ELB, but cannot be downgraded to a shared ELB. | To be tested |
|  | DeleteLoadBalancer | Deletes a load balancer. | To be tested |
|  | BatchCreateLoadBalancers | Create exclusive or shared load balancers in batches, including pay-per-use and yearly/monthly load balancers. | To be tested |
|  | ShowLoadBalancerStatus | Query the status tree of a load balancer, including the status of the load balancer and its associated subresources. | To be tested |
|  | DeleteLoadBalancerForce | Delete a load balancer and delete its sub-resources in the cascade. (delete the load balancer and its bound listeners, backend server groups, and backend servers.) | To be tested |
|  | ShowLoadBalancer | Query details about a load balancer. | To be tested |
|  | ChangeLoadbalancerChargeMode | The billing mode of the load balancer is changed. Currently, the supported billing mode is changed to: | To be tested |
| Log operation | DeleteLogtank | Unbind the cloud logs from a specified topic. | To be tested |
|  | CreateLogtank | Bind a cloud log to a specified topic to record the message sending status of the topic. | To be tested |
|  | UpdateLogtank | This API is used to update the cloud logs bound to a specified topic. | To be tested |
| Mirror Task | ShowJob | This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task. | To be tested |
| Preoccupied IP address | CountPreoccupyIpNum | Calculate the number of preoccupied IP addresses in the following scenarios: | To be tested |
| Query version operation | ListApiVersions | Query the TMS API version list. | To be tested |
| Quota | ShowQuota | Query the network resource quotas of a single tenant in the VPC service, including the VPC quota, subnet quota, security group quota, security group rule quota, EIP quota, and VPN quota. | To be tested |
| Recycle bin | UpdateRecycleBinEnable | Enable or disable the recycle bin function. After the function is enabled, the deleted LB can go to the recycle bin. Otherwise, the LB will not go to the recycle bin and will be deleted and cannot be restored. Before closing the recycle bin, restore or destroy the instance in the recycle bin. | To be tested |
|  | ListRecycleBinLoadBalancers | Query the load balancers in the recycle bin. | To be tested |
|  | DeleteRecycleLoadBalancer | Destroys the load balancer in the recycle bin. It cannot be restored after destruction. | To be tested |
|  | UpdateRecycleBinPolicy | Updates the recycle bin configuration. If the recycle bin is not enabled, an error will be reported during the update. | To be tested |
|  | RestoreLoadbalancer | Restore the load balancer from the recycle bin | To be tested |
|  | ShowRecycleBin | Query the recycle bin configuration | To be tested |
| Resource Quota Function | ListQuotaDetails | Query the resource quota of a user, including the VPC endpoint service and VPC endpoint. | To be tested |
| Security Policy | ShowSecurityPolicy | Query details about a user-defined security policy. | To be tested |
|  | ListSecurityPolicies | Query the user-defined security policy list. | To be tested |
|  | DeleteSecurityPolicy | Delete a user-defined security policy. | To be tested |
|  | UpdateSecurityPolicy | Update the user-defined security policy. | To be tested |
|  | ListSystemSecurityPolicies | Query the system security policy list. | To be tested |
|  | CreateSecurityPolicy | Create a user-defined security policy. Specifies the security_policy_id parameter in the request parameter when creating an HTTPS listener to set a user-defined security policy for the listener. | To be tested |
| Specification | ShowFlavor | Query the details about a specification. | To be tested |
| Tag Management | BatchDeleteListenerTags | Delete listener tags in batches. | To be tested |
|  | ShowListenerTags | Query all tags of a specified listener. | To be tested |
|  | BatchDeleteLoadbalancerTags | Deletes labels for load balancers in batches. | To be tested |
|  | ListListenerTags | Query the tag list of all listeners in a specified project | To be tested |
|  | CreateListenerTags | Adds a tag to a specified listener. | To be tested |
|  | BatchCreateListenerTags | Add listener tags in batches. | To be tested |
|  | DeleteLoadbalancerTags | Delete the tag corresponding to a key of the load balancer. | To be tested |
|  | ListLoadbalancerTags | Query the tag list of all load balancers in a specified project | To be tested |
|  | DeleteListenerTags | Delete the tag corresponding to a key of the listener. | To be tested |
|  | ListLoadbalancersByTags | This API is used to query ELB instances by tag. | To be tested |
|  | ShowLoadbalancerTags | Query all tags of a specified load balancer | To be tested |
|  | ListListenersByTags | Query the listener instance by label. | To be tested |
|  | BatchCreateLoadbalancerTags | Add labels for load balancers in batches. | To be tested |
|  | CreateLoadbalancerTags | Adds a label to a specified load balancer. | To be tested |
| Task Center API | ListJobs | Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph. | To be tested |
| VpnGateway | ListAvailabilityZones | Querying the AZ of the VPN gateway | To be tested |
| Whitelist | UpdateWhitelist | Update the trustlist. You can turn the trustlist on or off, or update the IP for access control. | To be tested |
|  | ShowWhitelist | Query trustlist details based on a specified ID. | To be tested |
|  | ListWhitelists | Query the trustlist. Filtered query and pagination query are supported. | To be tested |
|  | DeleteWhitelist | Delete the whitelist | To be tested |
|  | CreateWhitelist | Create a trustlist to control the access permission of listeners. If the trustlist function is enabled, only the bypassed IP addresses in the trustlist can access the backend service of the listener. | To be tested |

