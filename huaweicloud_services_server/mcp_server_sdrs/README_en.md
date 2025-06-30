# SDRS MCP Server 


## Version
v0.1.0

## Overview

SDRS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SDRS. Full-chain management of SDRS resources can be carried out based on natural language.

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
                    <td rowspan="1">API version information</td>
                    <td>ShowSpecifiedApiVersion</td>
                    <td>Query the version of a specified SDRS API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Big screen management</td>
                    <td>ListRpoStatistics</td>
                    <td>Query the resource RPO exceeding trend list displayed on the big screen of the current tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Copy Pair</td>
                    <td>ListReplications</td>
                    <td>Query the list of all replication pairs in a specified protection group. If no protection group is specified, the list of all replication pairs in the current tenant is queried.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteReplication</td>
                    <td>Deletes a specified replication pair.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateReplication</td>
                    <td>Create a replication pair and add it to the specified protection group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReplication</td>
                    <td>Query details about a replication pair.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateReplicationName</td>
                    <td>Updates the replication pair name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandReplication</td>
                    <td>Expand the capacity of the two disks in the replication pair.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">DR drill</td>
                    <td>ShowDisasterRecoveryDrill</td>
                    <td>Query the details about a DR drill.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDisasterRecoveryDrills</td>
                    <td>Query the list of all DR drills in a specified protection group. If no protection group is specified, the list of all DR drills in the current tenant is queried.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDisasterRecoveryDrill</td>
                    <td>Create a DR drill.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDisasterRecoveryDrill</td>
                    <td>Delete a specified DR drill. After deletion:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDisasterRecoveryDrillName</td>
                    <td>Update the DR drill name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job management</td>
                    <td>ShowJobStatus</td>
                    <td>Query the execution status of a job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Protected Instance</td>
                    <td>DeleteProtectedInstance</td>
                    <td>Delete a specified protected instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProtectedInstance</td>
                    <td>Query details about a protected instance, such as the name and ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateProtectedInstances</td>
                    <td>Typical scenario: no special operation scenario</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachProtectedInstanceReplication</td>
                    <td>Attach a specified replication pair to a specified protected instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddProtectedInstanceNic</td>
                    <td>This API is used to add a NIC to a specified protected instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectedInstances</td>
                    <td>Query all protected instances of the current tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachProtectedInstanceReplication</td>
                    <td>Unmounts the specified replication pair from the specified protected instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProtectedInstanceNic</td>
                    <td>Delete a specified NIC from a specified protected instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProtectedInstanceName</td>
                    <td>This API is used to update the name of a protected instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteProtectedInstances</td>
                    <td>Typical scenario: no special operation scenario</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProtectedInstance</td>
                    <td>Create a protected instance. After the protected instance is created, the DR site ECS name is the same as the production site ECS name but different IDs. If you need to change the ECS name, click the ECS name on the protected instance details page to go to the ECS details page and change the name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeProtectedInstance</td>
                    <td>This API is used to change the specifications of an ECS in a specified protected instance, including changing the specifications of both the production and DR sites.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Protection group</td>
                    <td>StopProtectionGroup</td>
                    <td>Stopping a protection group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartReverseProtectionGroup</td>
                    <td>You can switch the current production site of a protected group from the production site specified during the creation of the protected group to the DR site specified during the creation of the protected group. You can also switch services from the DR site specified during the creation of the protected group to the production site specified during the creation of the protected group. After the switchover, data at the production site and DR site is still protected, but the replication direction is opposite to that before the switchover.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartFailoverProtectionGroup</td>
                    <td>When the production site of a protected group is faulty, services will be switched from the production site to the current DR site, that is, the AZ at the other end, and resources such as EVS disks and ECSs will be enabled at the current DR site.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProtectionGroup</td>
                    <td>Query the details about a single protection group, such as the ID and name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProtectionGroup</td>
                    <td>Delete a specified protection group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProtectionGroupName</td>
                    <td>This API is used to update the name of a protected group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectionGroups</td>
                    <td>Query all protection groups of the current tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartProtectionGroup</td>
                    <td>Enable protection or reprotection for a protected group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProtectionGroup</td>
                    <td>Create a protection group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query HyperMetro Domain</td>
                    <td>ListActiveActiveDomains</td>
                    <td>Query the HyperMetro domain. A HyperMetro domain consists of local and remote storage devices. Application servers can access data across sites through the HyperMetro domain.</td>
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
                    <td rowspan="7">Tag Management</td>
                    <td>AddProtectedInstanceTags</td>
                    <td>A protected instance can have a maximum of 10 tags. This API is idempotent: If the created tag already exists (with the same key), the tag will be overwritten.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectedInstancesByTags</td>
                    <td>Use labels to filter protected instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectedInstancesProjectTags</td>
                    <td>Query the resource tag set of all protected instances of a tenant in a specified project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectedInstanceTags</td>
                    <td>Query the label information of a specified protected instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProtectedInstanceTag</td>
                    <td>Idempotent interface: During deletion, the label character set is not verified. Before invoking the interface, encodeURI must be configured. The server must decodeURI for the interface URI.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddTags</td>
                    <td>This API is used to add or delete tags for a specified protected instance in batches. A maximum of 10 labels can be placed on a resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTags</td>
                    <td>This API is used to delete tags for a specified protected instance in batches. A maximum of 10 labels can be placed on a resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Task Center</td>
                    <td>DeleteServerGroupFailureJobs</td>
                    <td>Delete all failed tasks in a specified protection group, for example, the protected instance fails to be created, the replication pair fails to be created, the protected instance fails to be deleted, and the replication pair fails to be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAllServerGroupFailureJobs</td>
                    <td>Delete failed tasks at all protection group levels, and fail to create or delete protection groups.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFailureJob</td>
                    <td>Delete a single failed task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFailureJobs</td>
                    <td>Query the list of failed tasks in all protected groups or the list of failed tasks in a specified protected group.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
