# ProjectMan MCP Server 


## Version
v0.1.0

## Overview

ProjectMan MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ProjectMan. Full-chain management of ProjectMan resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Iteration of Scrum Project | ListIterationHistories | View iteration history | To be tested |
|  | UpdateIterationV4 | Update Scrum project iteration | To be tested |
|  | DeleteIterationV4 | Delete project iteration | To be tested |
|  | BatchDeleteIterationsV4 | Deleting iterations of projects in batches | To be tested |
|  | CreateIterationV4 | Create Scrum project iteration | To be tested |
|  | ListProjectIterationsV4 | Obtain project iteration | To be tested |
|  | ShowIterationV4 | View iteration details | To be tested |
| Module for Scrum Project | DeleteProjectModule | Deleting a module from a project | To be tested |
|  | UpdateProjectModule | Update the module of the project | To be tested |
|  | CreateProjectModule | Query the module list of a project | To be tested |
|  | ListProjectModules | Query the module list of a project | To be tested |
| Project Indicator | ShowCompletionRate | Query on-time requirement completion rate | To be tested |
|  | ShowBugsPerDeveloper | Query per capita bug | To be tested |
|  | ShowBugDensityV2 | Query defect density | To be tested |
| Project Information | CreateProjectV4 | Create Project | To be tested |
|  | DeleteProjectV4 | Delete a project | To be tested |
|  | UpdateProjectV4 | Update Project | To be tested |
|  | CheckProjectNameV4 | Check whether the project name exists. | To be tested |
|  | ListDomainNotAddedProjectsV4 | Obtain projects that are not added to the tenant. | To be tested |
|  | ListProjectsV4 | Query the project list | To be tested |
|  | ShowProjectInfoV4 | Obtain project details | To be tested |
|  | ListTemplates | Query project template | To be tested |
| Project Member | AddApplyJoinProjectForAgc | The AGC invokes the current user to apply for joining the project. The applied user ID is written in the header. | To be tested |
|  | BatchDeleteMembersV4 | Delete project members in batches | To be tested |
|  | AddMemberV4 | Add project members. Cross-tenant members can be added. | To be tested |
|  | ListProjectMembersV4 | Obtain the project member list | To be tested |
|  | BatchAddMembersV4 | Add project members in batches. Only members in the same tenant as the project creator can be added. If the user ID is incorrect, the role will be ignored. If the number of added users exceeds the permission, the default role is 7. | To be tested |
|  | RemoveProject | The project creator cannot exit the project because the project member exits the project. | To be tested |
|  | UpdateMembesRoleV4 | Updates the role of a member in the project. | To be tested |
| Project Statistics | ListProjectDemandStaticV4 | Obtain requirement statistics | To be tested |
|  | ShowProjectSummaryV4 | Obtain the project overview | To be tested |
|  | ListProjectBugStaticsV4 | Obtain bug statistics by module. | To be tested |
| Scrum Project Domain | ListProjectDomains | Query the domain list of a project | To be tested |
|  | CreateProjectDomain | Query the domain list of a project | To be tested |
|  | CancelProjectDomain | Cancel the association between a domain and a project | To be tested |
|  | UpdateProjectDomain | Update the domain of a project | To be tested |
| Scrum Project Status | ListScrumProjectStatuses | Query the project status list | To be tested |
| User information | UpdateNickNameV4 | Update user nickname | To be tested |
|  | ShowCurUserInfo | Obtain the current user information | To be tested |
|  | ShowCurUserRole | Obtain the role of a user in a project. | To be tested |
|  | BatchUpdateChildNickNames | A user with the te_admin role can update the nicknames of other users. | To be tested |
| Work Items for Scrum Project | ListAssociatedIssues | Query the work items associated with the current work item | To be tested |
|  | ListIssueAssociatedCommits | Query the code submission records or branch creation records associated with the current work item. | To be tested |
|  | UploadIssueImg | Upload image | To be tested |
|  | ListIssueCustomFields | Query the optional list of the customized fields of the Scrum work item. If the custom_fields or names conditions are met, all the customized fields are returned. If neither of the two values is transferred, the list of all the customized fields is returned. | To be tested |
|  | ListAssociatedWikis | Query the associated wikis associated with the current work item | To be tested |
|  | ShowIssueV4 | Query work item details | To be tested |
|  | ListStatusStatistic | Query the statistics of the work item status in the iteration (by handler) | To be tested |
|  | ListIssueCommentsV4 | Obtain the comments of a work item | To be tested |
|  | ListSpecIssueStayTimes | Obtain the stay time of a specified work item | To be tested |
|  | ShowProjectWorkHours | Query work hours by user (single project) | To be tested |
|  | DownloadAttachment | Download the work item attachment | To be tested |
|  | CreateCustomfields | Create a customized field for the work item type | To be tested |
|  | ListProjectIssuesRecordsV4 | Query historical records of all work items under a project | To be tested |
|  | SearchIssues | Advanced query of my to-do work items | To be tested |
|  | ListIssuesV4 | Query work items based on filter criteria | To be tested |
|  | UploadAttachments | Upload work item attachment | To be tested |
|  | CreateIssueV4 | Create a work item | To be tested |
|  | ShowIssuesWrokFlowConfig | Query the work item transfer configuration of a Scrum project | To be tested |
|  | DownloadImageFile | Download image | To be tested |
|  | ListIssueRecordsV4 | Obtain historical work item records | To be tested |
|  | ShowIssueCompletionRate | Obtain the completion rate of a work item. | To be tested |
|  | UpdateIssueV4 | Update work item | To be tested |
|  | CreateSystemIssueV4 | Users with the IAM fine-grained permission (projectmanConfig:systemSettingField:set) and the permission to create work items in the devcloud project can set the work item creator. | To be tested |
|  | ListProjectWorkHoursType | Query the work hour type under a project | To be tested |
|  | BatchListAssociatedIssues | Query the associated work items of the current project | To be tested |
|  | ListIssuesSfV4 | Work item type ID, which is a pagination parameter. The work item is created at the query time. | To be tested |
|  | BatchDeleteIssuesV4 | Delete work items in batches | To be tested |
|  | AddIssueWorkHours | Add the work hours of the specified work item | To be tested |
|  | DeleteAttachment | Cancel the association between the work item and the attachment. If the attachment is uploaded on the work item page, delete the attachment. | To be tested |
|  | ListChildIssuesV4 | Obtain subwork items | To be tested |
|  | ListAssociatedTestCases | Query associated test cases | To be tested |
|  | ListProjectWorkHours | Query labor hours by user (multi-project) | To be tested |
|  | DeleteIssueV4 | Delete a work item | To be tested |
| Work Items of Dashboard Project | ListWorkitemStatusRecordsV4 | Query the historical status records of work items under a dashboard project in pagination mode | To be tested |
|  | ShowWorkItemWrokflowConfig | Query the work item transfer configuration of a dashboard project | To be tested |
|  | ListWorkitems | Query work items under a dashboard project | To be tested |

