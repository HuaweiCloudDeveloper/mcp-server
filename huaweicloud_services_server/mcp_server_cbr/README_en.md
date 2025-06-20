# CBR MCP Server 


## Version
v0.1.0

## Overview

CBR MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CBR. Full-chain management of CBR resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Backend ECS | DeleteMember | Delete a backend ECS | To be tested |
| Backup | ShowBackup | Query a single copy based on the specified ID. | To be tested |
|  | ImportBackup | Synchronizing offline hybrid cloud VMware backup copies | To be tested |
|  | CopyBackup | Replicate backup across regions. | To be tested |
|  | UpdateBackup | Modifies a backup based on the backup ID. | To be tested |
|  | RestoreBackup | Restoring backup data | To be tested |
| Backup Share | AddMember | Add backup sharing members. Only CSBS backups can be shared among users in the same region. | To be tested |
|  | ShowMembersDetail | Obtain the backup share member list | To be tested |
|  | UpdateMemberStatus | Updates the status of a backup share member. This API needs to be executed by the recipient. | To be tested |
|  | ShowMemberDetail | Obtains details about a backup member. | To be tested |
| Backup and Restore | ListBackups | Obtain the backup list. | To be tested |
| Backup management API | DeleteBackup | Delete a backup. | To be tested |
| Checkpoint management | ShowCheckpoint | This API is used to query checkpoint details. | To be tested |
| Federated identity authentication management | ShowMetadata | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the metadata file imported by the identity provider to IAM. | To be tested |
| File application backup | UpdateAgent | Modifying the client status | To be tested |
|  | UnregisterAgent | Remove the client. All backups of the client will be deleted when the client is removed. Exercise caution when performing this operation. | To be tested |
|  | RegisterAgent | Register the client. This command is invoked by the Agent during installation and does not need to be manually registered. | To be tested |
|  | ListAgent | Query the client list | To be tested |
|  | RemoveAgentPath | Remove the added file backup path. | To be tested |
|  | ShowAgent | Query a specified client | To be tested |
|  | AddAgentPath | Add a backup path to the client. The system does not check whether the new path exists. | To be tested |
| Host management | ListPolicies | Query the host policy list | To be tested |
| Label | DeleteVaultTag | Idempotent interface: When deleting a tag that does not exist, return 404. Key cannot be empty or an empty string. | To be tested |
|  | ShowVaultTag | Query the label information of a specified DB instance. | To be tested |
|  | CreateVaultTags | A resource can have a maximum of 10 tags. | To be tested |
|  | ShowVaultResourceInstances | Filter instances by label | To be tested |
|  | ShowVaultProjectTag | Query all tags of a tenant in a specified region and instance type. | To be tested |
|  | BatchCreateAndDeleteVaultTags | Add or delete tags for specified DB instances in batches | To be tested |
| Measurement | ShowStorageUsage | Query capacity statistics | To be tested |
| Operation | ChangeVaultChargeMode | Change the resource payment mode. Currently, only pay-per-use resources can be changed to yearly/monthly resources. | To be tested |
|  | UpdateOrder | Order update. This interface is invoked to update the order information of a duration-based product after the CBC order is paid. This interface is deprecated. | To be tested |
|  | ChangeOrder | This API is invoked to update the order information of a duration-based product and return the order information to be paid. | To be tested |
| Organization Policy | DeleteOrganizationPolicy | Deleting an organization policy | To be tested |
|  | ListOrganizationPolicyDetail | Query the deployment status list of organization policies under each account. | To be tested |
|  | ShowOrganizationPolicy | Querying a specified organization policy | To be tested |
|  | UpdateOrganizationPolicy | Update organization policy | To be tested |
|  | ListOrganizationPolicies | Query the organization policy list | To be tested |
|  | CreateOrganizationPolicy | Create an organization policy | To be tested |
| Project | ListDomainProjects | Query the project list based on the specified tenant name. | To be tested |
|  | ShowMigrateStatus | Query the migration result | To be tested |
|  | ShowDomain | Internal API invoked by the console. This API is used to obtain the domain name of the source project_id only when a shared backup is queried. | To be tested |
|  | MigrateDomain | Migrate CSBS/VBS resources to the CBR. | To be tested |
|  | ListProjects | Query enterprise project information of a tenant | To be tested |
| Protectability | ShowReplicationCapabilities | Query the replication capability of the local region | To be tested |
|  | ListProtectable | Query the protection resource list | To be tested |
|  | CheckAgent | Check the status of the application consistency agent | To be tested |
|  | ShowProtectable | Query protectable resources by ID | To be tested |
| Protection Policy Management | DeletePolicy | To delete a protection policy, if the policy is in use, you need to unbind the domain name from the policy before deleting the policy. | To be tested |
|  | ShowPolicy | Query protection policies by ID | To be tested |
|  | UpdatePolicy | Update the protection policy. The request body can contain only the part to be updated. | To be tested |
|  | CreatePolicy | When creating a protection policy, the system configures some default configuration items when generating the policy. To modify the default configuration items, call the interface for updating the protection policy. | To be tested |
| Repository | ShowVault | Query a specified repository by ID | To be tested |
|  | UpdateVault | Modifies a repository based on the repository ID | To be tested |
|  | ListVault | Query the repository list | To be tested |
|  | DisassociateVaultPolicy | Repository removal policy | To be tested |
|  | MigrateVaultResource | Resources can be migrated to another repository without deleting backups. | To be tested |
|  | BatchUpdateVault | Modifying all repositories under a project in batches | To be tested |
|  | DeleteVault | Delete a repository. If you delete a repository, all backups in the repository will also be deleted. | To be tested |
|  | ListExternalVault | Query the repository list in other regions | To be tested |
|  | AssociateVaultPolicy | Repository Setting Policy | To be tested |
|  | CreatePostPaidVault | Create a yearly/monthly repository | To be tested |
|  | SetVaultResource | Set whether to automatically back up repository resources | To be tested |
|  | ShowSummary | Query the total capacity and usage of all repositories under a project | To be tested |
|  | RemoveVaultResource | Removes a resource from the repository. If a resource is removed, the backup of the resource in the repository will be deleted. | To be tested |
|  | CreateVault | Create a repository | To be tested |
|  | AddVaultResource | Adding a resource to the repository | To be tested |
| Restore Point | CreateCheckpoint | Back up the repository and generate a backup restoration point | To be tested |
|  | ImportCheckpoint | Synchronizing backup copies for the vault | To be tested |
|  | CopyCheckpoint | Replicate | To be tested |
| Task | ListOpLogs | Query the task list | To be tested |
|  | ShowOpLog | Query a task based on the specified task ID | To be tested |

