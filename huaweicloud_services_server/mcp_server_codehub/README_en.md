# CodeHub MCP Server 


## Version
v0.1.0

## Overview

CodeHub MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeHub. Full-chain management of CodeHub resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Commit | ShowDiffCommit | Query the submission difference information based on the commit ID. | To be tested |
|  | ListCommits | Obtains the submission information based on the repository short ID. The list of all commits in the file path can be queried based on the file path. | To be tested |
|  | ShowSingleCommit | Gets a specific commit identified by the commit id or the name of a branch or tag. | To be tested |
|  | CreateCommit | You can submit multiple files in different directories at a time. If the directory does not exist, the directory is automatically created. The forcible overwrite option is supported. When the forcible overwrite flag is set to true, the conflict is ignored and the operation is forcibly committed. | To be tested |
| Consumer group management | ShowGroup | Query the details of a specified consumer group. | To be tested |
| DDM Instance Management | CreateGroup | Create a group | To be tested |
| Discussion | CreateMergeRequestDiscussionNote | Reply to MR review comments | To be tested |
|  | CreateMergeRequestDiscussion | Create MR review comments | To be tested |
|  | ShowReviewSetting | Obtain review comments. | To be tested |
| File | ShowFile | Obtain the file information in the repository, such as the name, size, and content. Note that the file contents are Base64 encoded. | To be tested |
|  | ListFilesByQuery | Obtain the file information in the repository, such as the name, size, and content. Note that the file contents are Base64 encoded. | To be tested |
| Group | AssociateRepositoryUserGroup | Associating warehouses with member groups | To be tested |
|  | DeleteGroup | Delete a code group | To be tested |
|  | ListManageableGroups | List of code groups that have the creation permission under the project | To be tested |
|  | AssociateGroupUserGroup | Associating code groups and member groups | To be tested |
| Instance Management | ShowStatisticalData |  | To be tested |
| Project | ShowRepositoryNameExist | Generally, this API is invoked during warehouse creation. Transfer the project ID. For details about how to obtain the project ID, see Obtaining the Project ID (codehub_api_0014.xml)., warehouse name, which is used to determine whether the warehouse name is duplicate. The warehouse contains result: false, and the warehouse does not contain result: true. | To be tested |
|  | GetAllRepositoryByProjectId | Obtains the supported scope for fuzzy query of warehouses. If project_id is not transferred, fuzzy query by warehouse name or project name is supported. Otherwise, fuzzy query by warehouse name is supported only. | To be tested |
|  | GetProductTemplates | Obtain the list of warehouses that can be set to public in a project. | To be tested |
|  | ListProductTwoTemplates | Obtain the list of warehouses that can be set to public in a project. | To be tested |
| RepoMember | SetRepoRole | Configure warehouse operation permissions for warehouse members. | To be tested |
|  | DeleteRepoMember | Deleting a warehouse member | To be tested |
|  | AddRepoMembers | Add warehouse members. | To be tested |
|  | ListRepoMembers | Obtain the warehouse member list. You can search for a member by keyword. | To be tested |
| Repository | ShowBranchesByTwoRepositoryId | Query the branch corresponding to a specified warehouse. | To be tested |
|  | DeleteRepository | Deletes a specified repository based on the 32-bit UUID of the repository. | To be tested |
|  | DeleteDeployKeyV2 | Delete a repository deployment key | To be tested |
|  | ShowRepoId | Obtain the warehouse short ID, which is used to obtain the warehouse details page URL | To be tested |
|  | ListTrustedIpAddresses | Obtain the repository IP address whitelist | To be tested |
|  | ListSubfiles | Obtain files in a branch directory | To be tested |
|  | ShowRepositoryArchive | Download the repository in the specified format | To be tested |
|  | CreateRepository | Creates a warehouse on a specified project with a specified name. Input parameters: warehouse name, template ID, whether to import project members, and project | To be tested |
|  | ListRepositoryStatus | Obtain the warehouse status. | To be tested |
|  | DeleteTrustedIpAddress | Delete the repository IP address whitelist | To be tested |
|  | AddDeployKey | Add a deployment key | To be tested |
|  | ListTemplatesTwo | Sets whether the warehouse is public or private. | To be tested |
|  | ShowMaster | Check whether the user has the permission to manage the warehouse. | To be tested |
|  | ListMergeChangesTrees | Obtain the list of changed files | To be tested |
|  | UpdateMergeRequestApprovalState | Combine request code review | To be tested |
|  | ShowRepositoryByUuid | Obtains warehouse information based on the warehouse UUID (returned by the CreateRepository interface). The returned information contains the id, name, group name, and repository access URL. | To be tested |
|  | AddDeployKeyV2 | Adding a deployment key | To be tested |
|  | ListRelatedCommits | Obtain associated work item information | To be tested |
|  | DeleteDeployKey | Delete the repository deployment key. | To be tested |
|  | GetTemplates | Obtain the public sample template list | To be tested |
|  | ShowStatisticCommit | Obtain the number of lines of code submitted by a specified branch in the code repository on a specified date. | To be tested |
|  | LockRepository | The warehouse is locked based on the warehouse short ID. | To be tested |
|  | ListCommitStatistics | Obtain the last submission statistics of the warehouse | To be tested |
|  | AddProtectBranchV2 | New protection branch | To be tested |
|  | ListBranchesByRepositoryId | Obtain the warehouse branch list | To be tested |
|  | ShowStatisticCommitV3 | Obtain the number of lines of code submitted by a specified branch in the code repository on a specified date. | To be tested |
|  | ListMergeRequest | Obtain the warehouse combination request list | To be tested |
|  | ShareTemplates | Sets whether the warehouse is public or private. | To be tested |
|  | UnlockRepository | Unlock the warehouse based on the warehouse short ID. | To be tested |
|  | ListFiles | Obtain the specified file content of a specific branch in a repository | To be tested |
|  | AddTrustedIpAddress | Adding the repository IP address whitelist | To be tested |
|  | AddTagV2 | New Tag | To be tested |
|  | ListTwoTemplates | Obtain the public sample template list | To be tested |
|  | ListMergeChanges | Obtain the change file | To be tested |
|  | ListMergeRequestReviewers | Obtain the inspector information based on the warehouse short ID and merge request short ID. | To be tested |
|  | UpdateTrustedIpAddress | Modifying the repository IP address whitelist | To be tested |
|  | ShowCommitsByBranch | Obtain the submission list based on the warehouse group name, warehouse name, and branch. | To be tested |
|  | ShowBranchesByRepositoryId | Obtains the branch list of a specified warehouse based on the warehouse ID. | To be tested |
|  | GetRepositoryByProjectId | You are advised not to use the /{repository_uuid}/status directory. | To be tested |
|  | ShowImageBlob | Obtain the image file of a specific branch in a repository | To be tested |
|  | ShowCommitsByRepoId | Query the submission of a branch in a warehouse based on the warehouse ID. | To be tested |
|  | ShowMergeRequest | Obtain the warehouse combination request details. | To be tested |
|  | ShowHasPipeline | Modify the status of the warehouse referenced by the pipeline. | To be tested |
|  | ShowRepositoryStatistics | Query the code submission statistics of the warehouse based on the warehouse short ID. | To be tested |
| SSHKey | AddSshKey | Add SSH key | To be tested |
|  | ListSshKeys | Obtain the SSH key list. | To be tested |
|  | DeleteSShkey | Delete the user public key. | To be tested |
|  | ShowPrivateKeyVerify | Check whether the private key has the permission to pull code | To be tested |
| Tenant | ListTenantTrustedIpAddresses | Obtain the tenant IP address whitelist | To be tested |
|  | UpdateTenantTrustedIpAddress | Modifying the IP address trustlist of a tenant | To be tested |
|  | DeleteTenantTrustedIpAddress | Delete a tenant IP address whitelist | To be tested |
|  | AddTenantTrustedIpAddress | Adding a tenant IP address whitelist | To be tested |
| User | ValidateHttpsInfo | Checks whether the user name and password entered when a user uploads or downloads code using HTTPS are valid. | To be tested |
|  | ValidateHttpsInfoV2 | Checks whether the user name and password entered when a user uploads or downloads code using HTTPS are valid. | To be tested |
| V2Project | ShowAllRepositoryByTwoProjectId | Obtains the warehouse list. If the project UUID is not transferred, fuzzy query by warehouse name or project name is supported. Otherwise, fuzzy query by warehouse name is supported. | To be tested |
|  | CreateProjectAndforkRepositories | After a warehouse is created, fork the warehouse, transfer the following parameters: warehouse name, whether to import project members, and project to which the warehouse belongs. | To be tested |
|  | CreateProjectAndRepositories | After a project is created, the following parameters are transferred to the warehouse group: warehouse name, template ID, whether to import project members, and project to which the warehouse group belongs. | To be tested |
|  | ListUserAllRepositories | Obtain all warehouse information of a user | To be tested |
|  | AssociateIssues | Associating branch work items | To be tested |
| WebHook | DeleteHooks | Submit the code to automatically trigger compilation and build and delete the repository hook. | To be tested |
|  | ListHooks | Obtain the repository webhook | To be tested |
|  | AddHooks | Submitting code automatically triggers compilation and build and adds the repository hook | To be tested |
| v2 warehouse management | CreateNewBranch | Creates a branch in a specified warehouse based on the warehouse ID. | To be tested |

