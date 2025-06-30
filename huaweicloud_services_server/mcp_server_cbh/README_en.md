# CBH MCP Server 


## Version
v0.1.0

## Overview

CBH MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CBH. Full-chain management of CBH resources can be carried out based on natural language.

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
                    <td rowspan="8">CBH Management</td>
                    <td>StopCbhInstance</td>
                    <td>Stop the CBH instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetLoginMethod</td>
                    <td>Reset the multi-factor authentication mode for the admin user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeCbhInstance</td>
                    <td>Upgrading CBH Instances</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InstallCbhEip</td>
                    <td>Bound an EIP to a CBH instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UninstallCbhEip</td>
                    <td>Unbind an EIP from a CBH instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartCbhInstance</td>
                    <td>Start the CBH instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartCbhInstance</td>
                    <td>Restart the CBH instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeInstanceNetwork</td>
                    <td>Modify the CBH instance network.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">CBH information query</td>
                    <td>SearchQuota</td>
                    <td>Query the CBH quota information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAvailableZoneInfo</td>
                    <td>Obtain the AZ information of the CBH service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNetworkConfiguration</td>
                    <td>Check the CBH instance network information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCbhInstance</td>
                    <td>Obtain the CBH instance list of the current tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQuotaStatus</td>
                    <td>Obtains whether the ECSs corresponding to the AZ and performance specifications selected by the current tenant are available.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">DDM Instance Management</td>
                    <td>UpdateInstanceSecurityGroup</td>
                    <td>Modify the security group of a DDM instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Database management</td>
                    <td>StartInstance</td>
                    <td>Starts the database and supports node-level startup operations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Entrusted Authorization</td>
                    <td>ShowAuthorization</td>
                    <td>Obtain the authorization information for the CBH service from the tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterAuthorization</td>
                    <td>This API is used by the tenant to create or cancel the agency authorization for the CBH service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Exclusive Instance Management</td>
                    <td>CreateInstance</td>
                    <td>Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Image Tag</td>
                    <td>ListTags</td>
                    <td>Query the image tag list based on different conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Instance Management</td>
                    <td>ResetPassword</td>
                    <td>Reset the password (only for instances with SSL enabled).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Instance management</td>
                    <td>StopInstance</td>
                    <td>When an instance is stopped, you can temporarily stop the pay-per-use instance to save costs. By default, the instance will be stopped for seven days.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Lifecycle Management</td>
                    <td>UpgradeInstance</td>
                    <td>Upgrading the Instance Kernel</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>Query the instance list of a tenant. Query by condition is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Network Management</td>
                    <td>InstallInstanceEip</td>
                    <td>The CBH instance is bound to an EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UninstallInstanceEip</td>
                    <td>Unbind an EIP from a CBH instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchInstanceVpc</td>
                    <td>Switching a VPC on a bastion host</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Obtain the link for logging in to the IAM instance</td>
                    <td>LoginCbh</td>
                    <td>Obtain the login-free link for the current IAM user to log in to the bastion host.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Operation management</td>
                    <td>ResetInstancePassword</td>
                    <td>Reset the password of user admin for logging in to the CBH instance web page.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LoginInstanceAdmin</td>
                    <td>Log in to the console of the bastion host instance admin as the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LoginInstance</td>
                    <td>Log in to the console of the bastion host instance as the IAM user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebootInstance</td>
                    <td>Restart the CBH instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOmUrl</td>
                    <td>Obtain the O&amp;M link.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetInstanceLoginMethod</td>
                    <td>Reset the login mode of user admin of the bastion host instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollbackInstance</td>
                    <td>Roll back the CBH instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeInstanceType</td>
                    <td>Modify the type of a single-node bastion host instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Order management</td>
                    <td>CreateCbh</td>
                    <td>Create a CBH instance. (Invoke this API before creating a CBH instance order.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceOrder</td>
                    <td>Create a CBH instance order. (Before calling this API, call the API for creating a CBH instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeInstanceOrder</td>
                    <td>Create an order for changing CBH instances. (Before calling this API, call the API for creating and changing a CBH instance. Currently, this API is not open.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Other interfaces</td>
                    <td>ListAvailableZones</td>
                    <td>When creating an instance, you need to configure the ID of the AZ where the instance is located. You can use this API to query the ID of the AZ.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Pipeline management</td>
                    <td>ShowInstanceStatus</td>
                    <td>Check the pipeline creation status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowQuota</td>
                    <td>Query the network resource quotas of a single tenant in the VPC service, including the VPC quota, subnet quota, security group quota, security group rule quota, EIP quota, and VPN quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota Management</td>
                    <td>ShowEcsQuota</td>
                    <td>Obtains whether the ECS specifications of the bastion host in the AZ selected by the current tenant are available.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Specification Change Management</td>
                    <td>ResizeInstance</td>
                    <td>The instance specification is changed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Specification Management</td>
                    <td>ListSpecifications</td>
                    <td>Query CBH specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Tag Management</td>
                    <td>ListInstancesByTag</td>
                    <td>Filter instances by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateInstanceTag</td>
                    <td>Operate the resource tag of the bastion host instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceTags</td>
                    <td>Query the label information of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountInstancesByTag</td>
                    <td>Count the number of instances that meet the label conditions.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
