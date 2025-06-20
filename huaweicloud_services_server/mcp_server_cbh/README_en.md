# CBH MCP Server 


## Version
v0.1.0

## Overview

CBH MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CBH. Full-chain management of CBH resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| CBH Management | StopCbhInstance | Stop the CBH instance. | To be tested |
|  | ResetLoginMethod | Reset the multi-factor authentication mode for the admin user. | To be tested |
|  | UpgradeCbhInstance | Upgrading CBH Instances | To be tested |
|  | InstallCbhEip | Bound an EIP to a CBH instance | To be tested |
|  | UninstallCbhEip | Unbind an EIP from a CBH instance. | To be tested |
|  | StartCbhInstance | Start the CBH instance. | To be tested |
|  | RestartCbhInstance | Restart the CBH instance. | To be tested |
|  | ChangeInstanceNetwork | Modify the CBH instance network. | To be tested |
| CBH information query | SearchQuota | Query the CBH quota information. | To be tested |
|  | ShowAvailableZoneInfo | Obtain the AZ information of the CBH service. | To be tested |
|  | ShowNetworkConfiguration | Check the CBH instance network information. | To be tested |
|  | ListCbhInstance | Obtain the CBH instance list of the current tenant. | To be tested |
|  | ListQuotaStatus | Obtains whether the ECSs corresponding to the AZ and performance specifications selected by the current tenant are available. | To be tested |
| DDM Instance Management | UpdateInstanceSecurityGroup | Modify the security group of a DDM instance. | To be tested |
| Database management | StartInstance | Starts the database and supports node-level startup operations. | To be tested |
| Entrusted Authorization | ShowAuthorization | Obtain the authorization information for the CBH service from the tenant. | To be tested |
|  | RegisterAuthorization | This API is used by the tenant to create or cancel the agency authorization for the CBH service. | To be tested |
| Exclusive Instance Management | CreateInstance | Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore | To be tested |
|  | DeleteInstance | Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
| Image Tag | ListTags | Query the image tag list based on different conditions. | To be tested |
| Instance Management | ResetPassword | Reset the password (only for instances with SSL enabled). | To be tested |
| Instance management | StopInstance | When an instance is stopped, you can temporarily stop the pay-per-use instance to save costs. By default, the instance will be stopped for seven days. | To be tested |
| Lifecycle Management | UpgradeInstance | Upgrading the Instance Kernel | To be tested |
|  | ListInstances | Query the instance list of a tenant. Query by condition is supported. | To be tested |
| Network Management | InstallInstanceEip | The CBH instance is bound to an EIP. | To be tested |
|  | UninstallInstanceEip | Unbind an EIP from a CBH instance. | To be tested |
|  | SwitchInstanceVpc | Switching a VPC on a bastion host | To be tested |
| Obtain the link for logging in to the IAM instance | LoginCbh | Obtain the login-free link for the current IAM user to log in to the bastion host. | To be tested |
| Operation management | ResetInstancePassword | Reset the password of user admin for logging in to the CBH instance web page. | To be tested |
|  | LoginInstanceAdmin | Log in to the console of the bastion host instance admin as the user. | To be tested |
|  | LoginInstance | Log in to the console of the bastion host instance as the IAM user. | To be tested |
|  | RebootInstance | Restart the CBH instance. | To be tested |
|  | ShowOmUrl | Obtain the O&M link. | To be tested |
|  | ResetInstanceLoginMethod | Reset the login mode of user admin of the bastion host instance. | To be tested |
|  | RollbackInstance | Roll back the CBH instance. | To be tested |
|  | ChangeInstanceType | Modify the type of a single-node bastion host instance. | To be tested |
| Order management | CreateCbh | Create a CBH instance. (Invoke this API before creating a CBH instance order.)  | To be tested |
|  | CreateInstanceOrder | Create a CBH instance order. (Before calling this API, call the API for creating a CBH instance. | To be tested |
|  | ChangeInstanceOrder | Create an order for changing CBH instances. (Before calling this API, call the API for creating and changing a CBH instance. Currently, this API is not open. | To be tested |
| Other interfaces | ListAvailableZones | When creating an instance, you need to configure the ID of the AZ where the instance is located. You can use this API to query the ID of the AZ. | To be tested |
| Pipeline management | ShowInstanceStatus | Check the pipeline creation status. | To be tested |
| Quota | ShowQuota | Query the network resource quotas of a single tenant in the VPC service, including the VPC quota, subnet quota, security group quota, security group rule quota, EIP quota, and VPN quota. | To be tested |
| Quota Management | ShowEcsQuota | Obtains whether the ECS specifications of the bastion host in the AZ selected by the current tenant are available. | To be tested |
| Specification Change Management | ResizeInstance | The instance specification is changed. | To be tested |
| Specification Management | ListSpecifications | Query CBH specifications. | To be tested |
| Tag Management | ListInstancesByTag | Filter instances by label. | To be tested |
|  | BatchCreateInstanceTag | Operate the resource tag of the bastion host instance. | To be tested |
|  | ShowInstanceTags | Query the label information of a specified DB instance. | To be tested |
|  | CountInstancesByTag | Count the number of instances that meet the label conditions. | To be tested |

