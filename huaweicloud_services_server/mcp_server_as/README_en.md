# AS MCP Server 


## Version
v0.1.0

## Overview

AS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service AS. Full-chain management of AS resources can be carried out based on natural language.

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
                    <td rowspan="5">Auto Scaling Configuration</td>
                    <td>BatchDeleteScalingConfigs</td>
                    <td>This API is used to delete specified AS configurations in batches. The AS configuration used by the AS group cannot be deleted. A maximum of 50 AS configurations can be deleted at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScalingConfig</td>
                    <td>This API is used to delete a specified AS configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScalingConfigs</td>
                    <td>Query AS configurations based on the entered conditions. Query results are displayed on multiple pages. You can filter the AS configuration by name, image ID, start row number, and number of records. If no filtering condition is specified, a maximum of 20 AS configurations can be queried by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScalingConfig</td>
                    <td>Query details about an AS configuration by AS configuration ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScalingConfig</td>
                    <td>Create an AS configuration. An AS configuration is a template for instances (ECSs) in an AS group. It defines the specifications of the instances to be added to the AS group. AS configurations are decoupled from AS groups. One AS configuration can be used by multiple AS groups. By default, a maximum of 100 AS configurations can be created.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Auto Scaling Group Management</td>
                    <td>PauseScalingGroup</td>
                    <td>This API is used to enable or disable a specified AS group. A disabled AS group does not automatically trigger any scaling action. If an AS group is being scaled, the ongoing scaling action will not stop immediately even if it is disabled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScalingGroup</td>
                    <td>Query the details of a specified AS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScalingGroup</td>
                    <td>An AS group is a collection of instances with the same application scenario. It is the basic unit for starting or stopping scaling policies and performing scaling actions. An AS group defines the maximum number of instances, expected number of instances, minimum number of instances, VPC, subnet, and load balancer. By default, a maximum of 10 AS groups can be created. If load balancing is configured for the AS group, the load balancing listener is automatically bound to or unbound from the instance when you add or remove an instance. If the AS group uses the load balancer health check mode, the instance in the AS group can pass the health check only after the listening port of the load balancer is enabled. Ports can be enabled in the security group. For details, see Adding a Security Group Rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScalingGroups</td>
                    <td>Query the AS group list based on the specified conditions. Query results are displayed on multiple pages. You can filter the AS group name, AS configuration ID, AS group status, enterprise project ID, start row number, and number of records. If no filter criteria are specified, a maximum of 20 AS groups can be queried by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResumeScalingGroup</td>
                    <td>This API is used to enable or disable a specified AS group. A disabled AS group does not automatically trigger any scaling action. If the AS group is being scaled, the ongoing scaling action will not be stopped immediately even if it is disabled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateScalingGroup</td>
                    <td>This API is used to modify information about a specified AS group. If the AS configuration is changed, the existing ECSs created using the original AS configuration in the AS group will not be affected. If no scaling action is in progress for an AS group, you can modify the subnet, AZ, and load balancing configuration of the AS group. When the expected number of instances in the AS group changes, the AS action will be triggered to add or remove instances. The number of expected instances must be greater than or equal to the minimum number of instances, and must be less than or equal to the maximum number of instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScalingGroup</td>
                    <td>This API is used to delete a specified AS group. The force_delete property specifies whether to forcibly delete the AS group, remove the ECS instance, and release the ECS instance if the AS group has ECS instances or the scaling action is being performed. The default value is no, indicating that the AS group is not forcibly deleted. If the value of force_delete is no, the AS group can be deleted only when the following conditions are met:Condition 1: No scaling action is in progress in the AS group. Condition 2: The number of ECS instances in the AS group (current_instance_number) is 0. If the value of force_delete is yes, the AS group enters the DELETING state and refuses to receive new AS action requests. After the existing AS actions are complete, all ECS instances in the AS group are removed from the AS group. (The ECS instances manually added by the user will be removed from the AS group, and the ECS instances automatically created by the AS will be automatically deleted.) and delete the AS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Auto Scaling Policy Management</td>
                    <td>UpdateScalingPolicy</td>
                    <td>Modifies a specified AS policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResumeScalingPolicy</td>
                    <td>This API is used to immediately execute, enable, or stop a specified AS policy. The AS policy can be executed only when the AS group and policy are in the INSERVICE state. Otherwise, the AS policy will fail to be executed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteScalingPolicy</td>
                    <td>This API is used to immediately execute, enable, or stop a specified AS policy. The AS policy can be executed only when the AS group and policy are in the INSERVICE state. Otherwise, the AS policy will fail to be executed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchPauseScalingPolicies</td>
                    <td>This API is used to enable, disable, or delete AS policies in batches. A maximum of 20 AS policies can be operated at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScalingPolicy</td>
                    <td>This API is used to delete a specified AS policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScalingPolicy</td>
                    <td>Query the information about a specified AS policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchResumeScalingPolicies</td>
                    <td>This API is used to enable, disable, or delete AS policies in batches. A maximum of 20 AS policies can be operated at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScalingPolicies</td>
                    <td>Query AS policies based on the entered conditions. Query results are displayed on multiple pages. You can search for AS policies by AS policy name, policy type, AS policy ID, start row number, and number of records. If no filtering condition is specified, a maximum of 20 AS policies in the specified AS group of the tenant are queried by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PauseScalingPolicy</td>
                    <td>This API is used to immediately execute, enable, or stop a specified AS policy. The AS policy can be executed only when the AS group and policy are in the INSERVICE state. Otherwise, the AS policy will fail to be executed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteScalingPolicies</td>
                    <td>This API is used to enable, disable, or delete AS policies in batches. A maximum of 20 AS policies can be operated at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Auto Scaling Policy Management V2</td>
                    <td>ListAllScalingV2Policies</td>
                    <td>Query AS policies based on the entered conditions. All AS policies of the current tenant can be queried. Query results are displayed on multiple pages. You can query the AS resource by AS resource ID, AS resource type, AS policy name, AS policy ID, alarm ID, enterprise project ID, start row number, number of records, and sorting mode. If no filtering is added, a maximum of 20 AS policies can be queried by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateScalingV2Policy</td>
                    <td>Modifies a specified AS policy. Modifying an AS PolicyThe difference between V2 and V1 is that V2 supports the modification of the AS resource type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScalingV2Policy</td>
                    <td>You can create AS policies for different types of resources, such as AS groups and bandwidths. Creating an AS PolicyThe difference between V2 and V1 is that V2 allows you to create a policy for adjusting bandwidth resources and differentiate scaling resources by scaling resource type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScalingV2Policy</td>
                    <td>Query the information about a specified AS policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScalingV2Policies</td>
                    <td>Query AS policies based on the entered conditions. Query results are displayed on multiple pages. The difference between V2 and V1 is that the response for querying an AS policy contains the scaling resource type. You can search for AS policies by AS policy name, policy type, AS policy ID, start row number, and number of records. If no filtering condition is specified, a maximum of 20 AS policies can be queried for specified resources of the tenant by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">AutoScaling Instance Management</td>
                    <td>ListScalingInstances</td>
                    <td>Query instances in an AS group based on the specified conditions. Query results are displayed on multiple pages. You can query instances based on the lifecycle status, health status, protection status, start row number, and number of records of the instances in the AS group. If no filter condition is specified, a maximum of 20 instances can be queried by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUnsetScalingInstancesStantby</td>
                    <td>This API is used to remove instances from an AS group in batches or add instances outside the AS group in batches. This API is used to set or cancel instance protection for instances in an AS group in batches. This interface is used to transfer instances in an AS group to or from the standby state in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUnprotectScalingInstances</td>
                    <td>This API is used to remove instances from an AS group in batches or add instances outside the AS group in batches. This API is used to set or cancel instance protection for instances in an AS group in batches. This interface is used to transfer instances in an AS group to or from the standby state in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetScalingInstancesStandby</td>
                    <td>This API is used to remove instances from an AS group in batches or add instances outside the AS group in batches. This API is used to set or cancel instance protection for instances in an AS group in batches. This API is used to transfer instances in an AS group to or from the standby state in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScalingInstance</td>
                    <td>This API is used to remove an instance from the AS group. You can remove an instance only when the instance is in the INSERVICE state and the number of instances to be removed must be greater than or equal to the minimum number of instances in the AS group. You can remove an AS instance only when no scaling action has been performed in the AS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRemoveScalingInstances</td>
                    <td>This API is used to remove instances from an AS group in batches or add instances outside the AS group in batches. This API is used to set or cancel instance protection for instances in an AS group in batches. This API is used to transfer instances in an AS group to or from the standby state in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchProtectScalingInstances</td>
                    <td>This API is used to remove instances from an AS group in batches or add instances outside the AS group in batches. This API is used to set or cancel instance protection for instances in an AS group in batches. This interface is used to transfer instances in an AS group to or from the standby state in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddScalingInstances</td>
                    <td>This API is used to remove instances from an AS group in batches or add instances outside the AS group in batches. This API is used to set or cancel instance protection for instances in an AS group in batches. This API is used to transfer instances in an AS group to or from the standby state in batches. Note: - A maximum of 10 instances can be operated in a batch at a time. The number of instances added in batches cannot be greater than the maximum number of instances in the AS group. The number of instances removed in batches cannot be less than the minimum number of instances in the AS group. - Instances can be added only when the AS group is in the INSERVICE state and no scaling action has been performed. - An AS instance can be removed only when no scaling action has been performed in the AS group. - When adding an instance to an AS group, ensure that the AZ where the instance resides is contained in the AZ of the AS group. - You can remove, set, or cancel the protection attributes of an instance only when the instance is in the INSERVICE state. - When the AS group is automatically scaled in, the instances with instance protection enabled will not be removed from the AS group. - When instances are removed from an AS group in batches, if the listener bound to the instances is the same as the listener in the AS group, the instances will be detached from the listener. If the listener bound to the instance when the instance is added to the AS group is different from the listener in the AS group, the binding relationship between the instance and the listener will be retained.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Autoscaling interface</td>
                    <td>CreateScalingPolicy</td>
                    <td>Edit the AS rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Lifecycle Hook Management</td>
                    <td>AttachCallbackInstanceLifeCycleHook</td>
                    <td>Use the lifecycle operation token or the instance ID and lifecycle hook name to call back the hook specified by the AS instance. If the custom operation has been completed before the timeout period expires, select Terminate or Continue to complete the lifecycle operation. If you need more time to complete the custom operation, select Extend the timeout period. The waiting time for the instance will be increased by 1 hour. Callback operations can be performed only when the lifecycle hook status of the instance is Hanging.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLifeCycleHooks</td>
                    <td>Query the lifecycle hook list based on the AS group ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLifyCycleHook</td>
                    <td>Create a lifecycle hook. You can add one or more lifecycle hooks for an AS group. A maximum of five lifecycle hooks can be added. After the lifecycle hook is added, the instance will be suspended by the lifecycle hook and put in the waiting state (being added to or removed from the AS group) when the AS group performs scaling. The instance remains in the waiting state until the timeout period expires or the user manually invokes the instance. Users can perform custom actions during the time period that the instance remains in the waiting state, for example, they can install or configure software on a newly started instance, or download log files from the instance before the instance terminates.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLifecycleHook</td>
                    <td>Deletes a specified life cycle hook. You cannot delete the lifecycle hook in the AS group when performing the scaling action.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLifeCycleHook</td>
                    <td>Modifies information in a specified life cycle hook.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHookInstances</td>
                    <td>After the lifecycle hook is added, the hook suspends the instance and puts it in the waiting state when the AS group performs scaling. You can query the suspension information about the instance in the AS group based on the entered conditions. You can query DB instances by DB instance ID. If no filter criteria are specified, the suspension information about all instances in the specified AS group is displayed by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLifeCycleHook</td>
                    <td>Query details about a specified life cycle hook based on the AS group ID and life cycle hook name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Notification management</td>
                    <td>DeleteScalingNotification</td>
                    <td>Delete the specified notification in the AS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScalingNotifications</td>
                    <td>Query the notification list of a specified AS group based on the AS group ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScalingNotification</td>
                    <td>Configure the notification function for the AS group. Each time this API is invoked, a notification topic and notification scenario are configured for the AS group. A maximum of five topics can be added to each AS group. A notification topic is created and subscribed to by users in advance. When the notification scenario corresponding to the notification topic occurs, the AS group sends a notification to the user's subscription terminal.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Planned Task</td>
                    <td>DeleteGroupScheduledTask</td>
                    <td>Delete a scheduled task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGroupScheduledTask</td>
                    <td>Update a scheduled task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGroupScheduledTask</td>
                    <td>Create a scheduled task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGroupScheduledTasks</td>
                    <td>Query the list of scheduled tasks</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Query version operation</td>
                    <td>ShowApiVersion</td>
                    <td>Query the details about a specified TMS API version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersions</td>
                    <td>Query the TMS API version list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Quota Management</td>
                    <td>ShowResourceQuota</td>
                    <td>Query the total and used quotas of AS groups, AS configurations, AS bandwidth policies, AS policies, and AS instances of a specified tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPolicyAndInstanceQuota</td>
                    <td>Query the total and used quotas of AS policies and instances in a specified AS group based on the AS group ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Scaling Policy Log Management</td>
                    <td>ListScalingPolicyExecuteLogs</td>
                    <td>Query historical policy execution records based on the entered conditions. The query results are displayed on multiple pages. You can filter and query logs by log ID, scaling resource type, scaling resource ID, policy execution type, start time, end time, start line number, and number of records. If no filter condition is specified, a maximum of 20 policy execution logs are displayed by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Scaling action log management</td>
                    <td>ListScalingActivityLogs</td>
                    <td>Query scaling action logs based on the specified conditions. Query results are displayed on multiple pages. You can filter the records by the start time, end time, start line number, and number of records. If no filter criteria are specified, a maximum of 20 scaling action logs are queried by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScalingActivityV2Logs</td>
                    <td>Query scaling action logs based on the entered conditions. You can query scaling, ELB migration, and instance backup activities. Query results are displayed on multiple pages. Querying AS Action Logs V2 is different from V1 in that V2 displays more detailed instance scaling logs, such as ELB migration logs and standby instance logs. You can filter the query by the start time, end time, start row number, number of records, or scaling action type. If no filter criteria are specified, a maximum of 20 scaling action logs are queried by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TAG Function</td>
                    <td>ListResourceInstances</td>
                    <td>Query resource instances of a tenant by tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Tag Management</td>
                    <td>ListScalingTagInfosByResourceId</td>
                    <td>Query the resource tag list of a specified resource type based on the project ID and resource ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScalingTagInfo</td>
                    <td>Creates or deletes a resource tag. A maximum of 10 tags can be added to each AS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScalingTagInfo</td>
                    <td>Creates or deletes a resource tag. A maximum of 10 tags can be added to each AS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScalingTagInfosByTenantId</td>
                    <td>Query the tag list of a specified resource type based on the project ID.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
