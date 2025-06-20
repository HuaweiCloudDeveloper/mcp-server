# SDRS MCP Server 


## Version
v0.1.0

## Overview

SDRS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SDRS. Full-chain management of SDRS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| API version information | ShowSpecifiedApiVersion | Query the version of a specified SDRS API. | To be tested |
| Big screen management | ListRpoStatistics | Query the resource RPO exceeding trend list displayed on the big screen of the current tenant. | To be tested |
| Copy Pair | ListReplications | Query the list of all replication pairs in a specified protection group. If no protection group is specified, the list of all replication pairs in the current tenant is queried. | To be tested |
|  | DeleteReplication | Deletes a specified replication pair. | To be tested |
|  | CreateReplication | Create a replication pair and add it to the specified protection group. | To be tested |
|  | ShowReplication | Query details about a replication pair. | To be tested |
|  | UpdateReplicationName | Updates the replication pair name. | To be tested |
|  | ExpandReplication | Expand the capacity of the two disks in the replication pair. | To be tested |
| DR drill | ShowDisasterRecoveryDrill | Query the details about a DR drill. | To be tested |
|  | ListDisasterRecoveryDrills | Query the list of all DR drills in a specified protection group. If no protection group is specified, the list of all DR drills in the current tenant is queried. | To be tested |
|  | CreateDisasterRecoveryDrill | Create a DR drill. | To be tested |
|  | DeleteDisasterRecoveryDrill | Delete a specified DR drill. After deletion: | To be tested |
|  | UpdateDisasterRecoveryDrillName | Update the DR drill name. | To be tested |
| Job management | ShowJobStatus | Query the execution status of a job. | To be tested |
| Protected Instance | DeleteProtectedInstance | Delete a specified protected instance. | To be tested |
|  | ShowProtectedInstance | Query details about a protected instance, such as the name and ID. | To be tested |
|  | BatchCreateProtectedInstances | Typical scenario: no special operation scenario | To be tested |
|  | AttachProtectedInstanceReplication | Attach a specified replication pair to a specified protected instance. | To be tested |
|  | AddProtectedInstanceNic | This API is used to add a NIC to a specified protected instance. | To be tested |
|  | ListProtectedInstances | Query all protected instances of the current tenant. | To be tested |
|  | DetachProtectedInstanceReplication | Unmounts the specified replication pair from the specified protected instance. | To be tested |
|  | DeleteProtectedInstanceNic | Delete a specified NIC from a specified protected instance. | To be tested |
|  | UpdateProtectedInstanceName | This API is used to update the name of a protected instance. | To be tested |
|  | BatchDeleteProtectedInstances | Typical scenario: no special operation scenario | To be tested |
|  | CreateProtectedInstance | Create a protected instance. After the protected instance is created, the DR site ECS name is the same as the production site ECS name but different IDs. If you need to change the ECS name, click the ECS name on the protected instance details page to go to the ECS details page and change the name. | To be tested |
|  | ResizeProtectedInstance | This API is used to change the specifications of an ECS in a specified protected instance, including changing the specifications of both the production and DR sites. | To be tested |
| Protection group | StopProtectionGroup | Stopping a protection group. | To be tested |
|  | StartReverseProtectionGroup | You can switch the current production site of a protected group from the production site specified during the creation of the protected group to the DR site specified during the creation of the protected group. You can also switch services from the DR site specified during the creation of the protected group to the production site specified during the creation of the protected group. After the switchover, data at the production site and DR site is still protected, but the replication direction is opposite to that before the switchover. | To be tested |
|  | StartFailoverProtectionGroup | When the production site of a protected group is faulty, services will be switched from the production site to the current DR site, that is, the AZ at the other end, and resources such as EVS disks and ECSs will be enabled at the current DR site. | To be tested |
|  | ShowProtectionGroup | Query the details about a single protection group, such as the ID and name. | To be tested |
|  | DeleteProtectionGroup | Delete a specified protection group. | To be tested |
|  | UpdateProtectionGroupName | This API is used to update the name of a protected group. | To be tested |
|  | ListProtectionGroups | Query all protection groups of the current tenant. | To be tested |
|  | StartProtectionGroup | Enable protection or reprotection for a protected group. | To be tested |
|  | CreateProtectionGroup | Create a protection group. | To be tested |
| Query HyperMetro Domain | ListActiveActiveDomains | Query the HyperMetro domain. A HyperMetro domain consists of local and remote storage devices. Application servers can access data across sites through the HyperMetro domain. | To be tested |
| Query version operation | ListApiVersions | Query the TMS API version list. | To be tested |
| Quota | ShowQuota | Query the network resource quotas of a single tenant in the VPC service, including the VPC quota, subnet quota, security group quota, security group rule quota, EIP quota, and VPN quota. | To be tested |
| Tag Management | AddProtectedInstanceTags | A protected instance can have a maximum of 10 tags. This API is idempotent: If the created tag already exists (with the same key), the tag will be overwritten. | To be tested |
|  | ListProtectedInstancesByTags | Use labels to filter protected instances. | To be tested |
|  | ListProtectedInstancesProjectTags | Query the resource tag set of all protected instances of a tenant in a specified project. | To be tested |
|  | ListProtectedInstanceTags | Query the label information of a specified protected instance. | To be tested |
|  | DeleteProtectedInstanceTag | Idempotent interface: During deletion, the label character set is not verified. Before invoking the interface, encodeURI must be configured. The server must decodeURI for the interface URI. | To be tested |
|  | BatchAddTags | This API is used to add or delete tags for a specified protected instance in batches. A maximum of 10 labels can be placed on a resource. | To be tested |
|  | BatchDeleteTags | This API is used to delete tags for a specified protected instance in batches. A maximum of 10 labels can be placed on a resource. | To be tested |
| Task Center | DeleteServerGroupFailureJobs | Delete all failed tasks in a specified protection group, for example, the protected instance fails to be created, the replication pair fails to be created, the protected instance fails to be deleted, and the replication pair fails to be deleted. | To be tested |
|  | DeleteAllServerGroupFailureJobs | Delete failed tasks at all protection group levels, and fail to create or delete protection groups. | To be tested |
|  | DeleteFailureJob | Delete a single failed task. | To be tested |
|  | ListFailureJobs | Query the list of failed tasks in all protected groups or the list of failed tasks in a specified protected group. | To be tested |

