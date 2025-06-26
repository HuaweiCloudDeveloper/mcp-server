# ProjectMan MCP Server 


## Version
v0.1.0

## Overview

ProjectMan MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ProjectMan. Full-chain management of ProjectMan resources can be carried out based on natural language.

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
                    <td rowspan="7">Iteration of Scrum Project</td>
                    <td>ListIterationHistories</td>
                    <td>View iteration history</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIterationV4</td>
                    <td>Update Scrum project iteration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIterationV4</td>
                    <td>Delete project iteration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteIterationsV4</td>
                    <td>Deleting iterations of projects in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIterationV4</td>
                    <td>Create Scrum project iteration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectIterationsV4</td>
                    <td>Obtain project iteration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIterationV4</td>
                    <td>View iteration details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Module for Scrum Project</td>
                    <td>DeleteProjectModule</td>
                    <td>Deleting a module from a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProjectModule</td>
                    <td>Update the module of the project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectModule</td>
                    <td>Query the module list of a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectModules</td>
                    <td>Query the module list of a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Project Indicator</td>
                    <td>ShowCompletionRate</td>
                    <td>Query on-time requirement completion rate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBugsPerDeveloper</td>
                    <td>Query per capita bug</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBugDensityV2</td>
                    <td>Query defect density</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Project Information</td>
                    <td>CreateProjectV4</td>
                    <td>Create Project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProjectV4</td>
                    <td>Delete a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProjectV4</td>
                    <td>Update Project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckProjectNameV4</td>
                    <td>Check whether the project name exists.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainNotAddedProjectsV4</td>
                    <td>Obtain projects that are not added to the tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectsV4</td>
                    <td>Query the project list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectInfoV4</td>
                    <td>Obtain project details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplates</td>
                    <td>Query project template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Project Member</td>
                    <td>AddApplyJoinProjectForAgc</td>
                    <td>The AGC invokes the current user to apply for joining the project. The applied user ID is written in the header.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteMembersV4</td>
                    <td>Delete project members in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddMemberV4</td>
                    <td>Add project members. Cross-tenant members can be added.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectMembersV4</td>
                    <td>Obtain the project member list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddMembersV4</td>
                    <td>Add project members in batches. Only members in the same tenant as the project creator can be added. If the user ID is incorrect, the role will be ignored. If the number of added users exceeds the permission, the default role is 7.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveProject</td>
                    <td>The project creator cannot exit the project because the project member exits the project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMembesRoleV4</td>
                    <td>Updates the role of a member in the project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Project Statistics</td>
                    <td>ListProjectDemandStaticV4</td>
                    <td>Obtain requirement statistics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectSummaryV4</td>
                    <td>Obtain the project overview</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectBugStaticsV4</td>
                    <td>Obtain bug statistics by module.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Scrum Project Domain</td>
                    <td>ListProjectDomains</td>
                    <td>Query the domain list of a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectDomain</td>
                    <td>Query the domain list of a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelProjectDomain</td>
                    <td>Cancel the association between a domain and a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProjectDomain</td>
                    <td>Update the domain of a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Scrum Project Status</td>
                    <td>ListScrumProjectStatuses</td>
                    <td>Query the project status list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">User information</td>
                    <td>UpdateNickNameV4</td>
                    <td>Update user nickname</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCurUserInfo</td>
                    <td>Obtain the current user information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCurUserRole</td>
                    <td>Obtain the role of a user in a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateChildNickNames</td>
                    <td>A user with the te_admin role can update the nicknames of other users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="33">Work Items for Scrum Project</td>
                    <td>ListAssociatedIssues</td>
                    <td>Query the work items associated with the current work item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIssueAssociatedCommits</td>
                    <td>Query the code submission records or branch creation records associated with the current work item.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadIssueImg</td>
                    <td>Upload image</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIssueCustomFields</td>
                    <td>Query the optional list of the customized fields of the Scrum work item. If the custom_fields or names conditions are met, all the customized fields are returned. If neither of the two values is transferred, the list of all the customized fields is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAssociatedWikis</td>
                    <td>Query the associated wikis associated with the current work item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIssueV4</td>
                    <td>Query work item details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStatusStatistic</td>
                    <td>Query the statistics of the work item status in the iteration (by handler)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIssueCommentsV4</td>
                    <td>Obtain the comments of a work item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSpecIssueStayTimes</td>
                    <td>Obtain the stay time of a specified work item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectWorkHours</td>
                    <td>Query work hours by user (single project)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadAttachment</td>
                    <td>Download the work item attachment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCustomfields</td>
                    <td>Create a customized field for the work item type</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectIssuesRecordsV4</td>
                    <td>Query historical records of all work items under a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchIssues</td>
                    <td>Advanced query of my to-do work items</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIssuesV4</td>
                    <td>Query work items based on filter criteria</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadAttachments</td>
                    <td>Upload work item attachment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIssueV4</td>
                    <td>Create a work item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIssuesWrokFlowConfig</td>
                    <td>Query the work item transfer configuration of a Scrum project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadImageFile</td>
                    <td>Download image</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIssueRecordsV4</td>
                    <td>Obtain historical work item records</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIssueCompletionRate</td>
                    <td>Obtain the completion rate of a work item.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIssueV4</td>
                    <td>Update work item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSystemIssueV4</td>
                    <td>Users with the IAM fine-grained permission (projectmanConfig:systemSettingField:set) and the permission to create work items in the devcloud project can set the work item creator.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectWorkHoursType</td>
                    <td>Query the work hour type under a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListAssociatedIssues</td>
                    <td>Query the associated work items of the current project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIssuesSfV4</td>
                    <td>Work item type ID, which is a pagination parameter. The work item is created at the query time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteIssuesV4</td>
                    <td>Delete work items in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddIssueWorkHours</td>
                    <td>Add the work hours of the specified work item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAttachment</td>
                    <td>Cancel the association between the work item and the attachment. If the attachment is uploaded on the work item page, delete the attachment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListChildIssuesV4</td>
                    <td>Obtain subwork items</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAssociatedTestCases</td>
                    <td>Query associated test cases</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectWorkHours</td>
                    <td>Query labor hours by user (multi-project)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIssueV4</td>
                    <td>Delete a work item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Work Items of Dashboard Project</td>
                    <td>ListWorkitemStatusRecordsV4</td>
                    <td>Query the historical status records of work items under a dashboard project in pagination mode</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkItemWrokflowConfig</td>
                    <td>Query the work item transfer configuration of a dashboard project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkitems</td>
                    <td>Query work items under a dashboard project</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
