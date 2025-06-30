# CodeHub MCP Server 


## Version
v0.1.0

## Overview

CodeHub MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeHub. Full-chain management of CodeHub resources can be carried out based on natural language.

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
                    <td rowspan="4">Commit</td>
                    <td>ShowDiffCommit</td>
                    <td>Query the submission difference information based on the commit ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCommits</td>
                    <td>Obtains the submission information based on the repository short ID. The list of all commits in the file path can be queried based on the file path.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSingleCommit</td>
                    <td>Gets a specific commit identified by the commit id or the name of a branch or tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCommit</td>
                    <td>You can submit multiple files in different directories at a time. If the directory does not exist, the directory is automatically created. The forcible overwrite option is supported. When the forcible overwrite flag is set to true, the conflict is ignored and the operation is forcibly committed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Consumer group management</td>
                    <td>ShowGroup</td>
                    <td>Query the details of a specified consumer group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">DDM Instance Management</td>
                    <td>CreateGroup</td>
                    <td>Create a group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Discussion</td>
                    <td>CreateMergeRequestDiscussionNote</td>
                    <td>Reply to MR review comments</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMergeRequestDiscussion</td>
                    <td>Create MR review comments</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReviewSetting</td>
                    <td>Obtain review comments.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">File</td>
                    <td>ShowFile</td>
                    <td>Obtain the file information in the repository, such as the name, size, and content. Note that the file contents are Base64 encoded.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFilesByQuery</td>
                    <td>Obtain the file information in the repository, such as the name, size, and content. Note that the file contents are Base64 encoded.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Group</td>
                    <td>AssociateRepositoryUserGroup</td>
                    <td>Associating warehouses with member groups</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGroup</td>
                    <td>Delete a code group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListManageableGroups</td>
                    <td>List of code groups that have the creation permission under the project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateGroupUserGroup</td>
                    <td>Associating code groups and member groups</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Instance Management</td>
                    <td>ShowStatisticalData</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Project</td>
                    <td>ShowRepositoryNameExist</td>
                    <td>Generally, this API is invoked during warehouse creation. Transfer the project ID. For details about how to obtain the project ID, see Obtaining the Project ID (codehub_api_0014.xml)., warehouse name, which is used to determine whether the warehouse name is duplicate. The warehouse contains result: false, and the warehouse does not contain result: true.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetAllRepositoryByProjectId</td>
                    <td>Obtains the supported scope for fuzzy query of warehouses. If project_id is not transferred, fuzzy query by warehouse name or project name is supported. Otherwise, fuzzy query by warehouse name is supported only.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetProductTemplates</td>
                    <td>Obtain the list of warehouses that can be set to public in a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProductTwoTemplates</td>
                    <td>Obtain the list of warehouses that can be set to public in a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">RepoMember</td>
                    <td>SetRepoRole</td>
                    <td>Configure warehouse operation permissions for warehouse members.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRepoMember</td>
                    <td>Deleting a warehouse member</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddRepoMembers</td>
                    <td>Add warehouse members.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRepoMembers</td>
                    <td>Obtain the warehouse member list. You can search for a member by keyword.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="44">Repository</td>
                    <td>ShowBranchesByTwoRepositoryId</td>
                    <td>Query the branch corresponding to a specified warehouse.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRepository</td>
                    <td>Deletes a specified repository based on the 32-bit UUID of the repository.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeployKeyV2</td>
                    <td>Delete a repository deployment key</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRepoId</td>
                    <td>Obtain the warehouse short ID, which is used to obtain the warehouse details page URL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTrustedIpAddresses</td>
                    <td>Obtain the repository IP address whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubfiles</td>
                    <td>Obtain files in a branch directory</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRepositoryArchive</td>
                    <td>Download the repository in the specified format</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRepository</td>
                    <td>Creates a warehouse on a specified project with a specified name. Input parameters: warehouse name, template ID, whether to import project members, and project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRepositoryStatus</td>
                    <td>Obtain the warehouse status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrustedIpAddress</td>
                    <td>Delete the repository IP address whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDeployKey</td>
                    <td>Add a deployment key</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplatesTwo</td>
                    <td>Sets whether the warehouse is public or private.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMaster</td>
                    <td>Check whether the user has the permission to manage the warehouse.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMergeChangesTrees</td>
                    <td>Obtain the list of changed files</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMergeRequestApprovalState</td>
                    <td>Combine request code review</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRepositoryByUuid</td>
                    <td>Obtains warehouse information based on the warehouse UUID (returned by the CreateRepository interface). The returned information contains the id, name, group name, and repository access URL.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDeployKeyV2</td>
                    <td>Adding a deployment key</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRelatedCommits</td>
                    <td>Obtain associated work item information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeployKey</td>
                    <td>Delete the repository deployment key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetTemplates</td>
                    <td>Obtain the public sample template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStatisticCommit</td>
                    <td>Obtain the number of lines of code submitted by a specified branch in the code repository on a specified date.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LockRepository</td>
                    <td>The warehouse is locked based on the warehouse short ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCommitStatistics</td>
                    <td>Obtain the last submission statistics of the warehouse</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddProtectBranchV2</td>
                    <td>New protection branch</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBranchesByRepositoryId</td>
                    <td>Obtain the warehouse branch list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStatisticCommitV3</td>
                    <td>Obtain the number of lines of code submitted by a specified branch in the code repository on a specified date.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMergeRequest</td>
                    <td>Obtain the warehouse combination request list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShareTemplates</td>
                    <td>Sets whether the warehouse is public or private.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnlockRepository</td>
                    <td>Unlock the warehouse based on the warehouse short ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFiles</td>
                    <td>Obtain the specified file content of a specific branch in a repository</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTrustedIpAddress</td>
                    <td>Adding the repository IP address whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTagV2</td>
                    <td>New Tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTwoTemplates</td>
                    <td>Obtain the public sample template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMergeChanges</td>
                    <td>Obtain the change file</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMergeRequestReviewers</td>
                    <td>Obtain the inspector information based on the warehouse short ID and merge request short ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTrustedIpAddress</td>
                    <td>Modifying the repository IP address whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCommitsByBranch</td>
                    <td>Obtain the submission list based on the warehouse group name, warehouse name, and branch.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBranchesByRepositoryId</td>
                    <td>Obtains the branch list of a specified warehouse based on the warehouse ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetRepositoryByProjectId</td>
                    <td>You are advised not to use the /{repository_uuid}/status directory.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageBlob</td>
                    <td>Obtain the image file of a specific branch in a repository</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCommitsByRepoId</td>
                    <td>Query the submission of a branch in a warehouse based on the warehouse ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMergeRequest</td>
                    <td>Obtain the warehouse combination request details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHasPipeline</td>
                    <td>Modify the status of the warehouse referenced by the pipeline.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRepositoryStatistics</td>
                    <td>Query the code submission statistics of the warehouse based on the warehouse short ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">SSHKey</td>
                    <td>AddSshKey</td>
                    <td>Add SSH key</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSshKeys</td>
                    <td>Obtain the SSH key list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSShkey</td>
                    <td>Delete the user public key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateKeyVerify</td>
                    <td>Check whether the private key has the permission to pull code</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Tenant</td>
                    <td>ListTenantTrustedIpAddresses</td>
                    <td>Obtain the tenant IP address whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTenantTrustedIpAddress</td>
                    <td>Modifying the IP address trustlist of a tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTenantTrustedIpAddress</td>
                    <td>Delete a tenant IP address whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTenantTrustedIpAddress</td>
                    <td>Adding a tenant IP address whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">User</td>
                    <td>ValidateHttpsInfo</td>
                    <td>Checks whether the user name and password entered when a user uploads or downloads code using HTTPS are valid.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateHttpsInfoV2</td>
                    <td>Checks whether the user name and password entered when a user uploads or downloads code using HTTPS are valid.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">V2Project</td>
                    <td>ShowAllRepositoryByTwoProjectId</td>
                    <td>Obtains the warehouse list. If the project UUID is not transferred, fuzzy query by warehouse name or project name is supported. Otherwise, fuzzy query by warehouse name is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectAndforkRepositories</td>
                    <td>After a warehouse is created, fork the warehouse, transfer the following parameters: warehouse name, whether to import project members, and project to which the warehouse belongs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectAndRepositories</td>
                    <td>After a project is created, the following parameters are transferred to the warehouse group: warehouse name, template ID, whether to import project members, and project to which the warehouse group belongs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserAllRepositories</td>
                    <td>Obtain all warehouse information of a user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateIssues</td>
                    <td>Associating branch work items</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">WebHook</td>
                    <td>DeleteHooks</td>
                    <td>Submit the code to automatically trigger compilation and build and delete the repository hook.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHooks</td>
                    <td>Obtain the repository webhook</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddHooks</td>
                    <td>Submitting code automatically triggers compilation and build and adds the repository hook</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">v2 warehouse management</td>
                    <td>CreateNewBranch</td>
                    <td>Creates a branch in a specified warehouse based on the warehouse ID.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
