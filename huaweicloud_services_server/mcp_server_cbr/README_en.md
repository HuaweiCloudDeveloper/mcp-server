# CBR MCP Server 


## Version
v0.1.0

## Overview

CBR MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CBR. Full-chain management of CBR resources can be carried out based on natural language.

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
                    <td rowspan="1">Backend ECS</td>
                    <td>DeleteMember</td>
                    <td>Delete a backend ECS</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Backup</td>
                    <td>ShowBackup</td>
                    <td>Query a single copy based on the specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportBackup</td>
                    <td>Synchronizing offline hybrid cloud VMware backup copies</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyBackup</td>
                    <td>Replicate backup across regions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBackup</td>
                    <td>Modifies a backup based on the backup ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreBackup</td>
                    <td>Restoring backup data</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Backup Share</td>
                    <td>AddMember</td>
                    <td>Add backup sharing members. Only CSBS backups can be shared among users in the same region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMembersDetail</td>
                    <td>Obtain the backup share member list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMemberStatus</td>
                    <td>Updates the status of a backup share member. This API needs to be executed by the recipient.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMemberDetail</td>
                    <td>Obtains details about a backup member.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Backup and Restore</td>
                    <td>ListBackups</td>
                    <td>Obtain the backup list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Backup management API</td>
                    <td>DeleteBackup</td>
                    <td>Delete a backup.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Checkpoint management</td>
                    <td>ShowCheckpoint</td>
                    <td>This API is used to query checkpoint details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Federated identity authentication management</td>
                    <td>ShowMetadata</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the metadata file imported by the identity provider to IAM.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">File application backup</td>
                    <td>UpdateAgent</td>
                    <td>Modifying the client status</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnregisterAgent</td>
                    <td>Remove the client. All backups of the client will be deleted when the client is removed. Exercise caution when performing this operation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterAgent</td>
                    <td>Register the client. This command is invoked by the Agent during installation and does not need to be manually registered.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgent</td>
                    <td>Query the client list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveAgentPath</td>
                    <td>Remove the added file backup path.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgent</td>
                    <td>Query a specified client</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAgentPath</td>
                    <td>Add a backup path to the client. The system does not check whether the new path exists.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Host management</td>
                    <td>ListPolicies</td>
                    <td>Query the host policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Label</td>
                    <td>DeleteVaultTag</td>
                    <td>Idempotent interface: When deleting a tag that does not exist, return 404. Key cannot be empty or an empty string.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVaultTag</td>
                    <td>Query the label information of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVaultTags</td>
                    <td>A resource can have a maximum of 10 tags.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVaultResourceInstances</td>
                    <td>Filter instances by label</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVaultProjectTag</td>
                    <td>Query all tags of a tenant in a specified region and instance type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateAndDeleteVaultTags</td>
                    <td>Add or delete tags for specified DB instances in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Measurement</td>
                    <td>ShowStorageUsage</td>
                    <td>Query capacity statistics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Operation</td>
                    <td>ChangeVaultChargeMode</td>
                    <td>Change the resource payment mode. Currently, only pay-per-use resources can be changed to yearly/monthly resources.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOrder</td>
                    <td>Order update. This interface is invoked to update the order information of a duration-based product after the CBC order is paid. This interface is deprecated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeOrder</td>
                    <td>This API is invoked to update the order information of a duration-based product and return the order information to be paid.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Organization Policy</td>
                    <td>DeleteOrganizationPolicy</td>
                    <td>Deleting an organization policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOrganizationPolicyDetail</td>
                    <td>Query the deployment status list of organization policies under each account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOrganizationPolicy</td>
                    <td>Querying a specified organization policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOrganizationPolicy</td>
                    <td>Update organization policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOrganizationPolicies</td>
                    <td>Query the organization policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrganizationPolicy</td>
                    <td>Create an organization policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Project</td>
                    <td>ListDomainProjects</td>
                    <td>Query the project list based on the specified tenant name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMigrateStatus</td>
                    <td>Query the migration result</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomain</td>
                    <td>Internal API invoked by the console. This API is used to obtain the domain name of the source project_id only when a shared backup is queried.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateDomain</td>
                    <td>Migrate CSBS/VBS resources to the CBR.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjects</td>
                    <td>Query enterprise project information of a tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Protectability</td>
                    <td>ShowReplicationCapabilities</td>
                    <td>Query the replication capability of the local region</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectable</td>
                    <td>Query the protection resource list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckAgent</td>
                    <td>Check the status of the application consistency agent</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProtectable</td>
                    <td>Query protectable resources by ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Protection Policy Management</td>
                    <td>DeletePolicy</td>
                    <td>To delete a protection policy, if the policy is in use, you need to unbind the domain name from the policy before deleting the policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPolicy</td>
                    <td>Query protection policies by ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicy</td>
                    <td>Update the protection policy. The request body can contain only the part to be updated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePolicy</td>
                    <td>When creating a protection policy, the system configures some default configuration items when generating the policy. To modify the default configuration items, call the interface for updating the protection policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">Repository</td>
                    <td>ShowVault</td>
                    <td>Query a specified repository by ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVault</td>
                    <td>Modifies a repository based on the repository ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVault</td>
                    <td>Query the repository list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateVaultPolicy</td>
                    <td>Repository removal policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateVaultResource</td>
                    <td>Resources can be migrated to another repository without deleting backups.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateVault</td>
                    <td>Modifying all repositories under a project in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVault</td>
                    <td>Delete a repository. If you delete a repository, all backups in the repository will also be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListExternalVault</td>
                    <td>Query the repository list in other regions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateVaultPolicy</td>
                    <td>Repository Setting Policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostPaidVault</td>
                    <td>Create a yearly/monthly repository</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetVaultResource</td>
                    <td>Set whether to automatically back up repository resources</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSummary</td>
                    <td>Query the total capacity and usage of all repositories under a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveVaultResource</td>
                    <td>Removes a resource from the repository. If a resource is removed, the backup of the resource in the repository will be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVault</td>
                    <td>Create a repository</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddVaultResource</td>
                    <td>Adding a resource to the repository</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Restore Point</td>
                    <td>CreateCheckpoint</td>
                    <td>Back up the repository and generate a backup restoration point</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportCheckpoint</td>
                    <td>Synchronizing backup copies for the vault</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyCheckpoint</td>
                    <td>Replicate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Task</td>
                    <td>ListOpLogs</td>
                    <td>Query the task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOpLog</td>
                    <td>Query a task based on the specified task ID</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
