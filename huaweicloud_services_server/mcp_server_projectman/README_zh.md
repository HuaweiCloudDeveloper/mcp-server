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
                    <td rowspan="33">Scrum项目的工作项</td>
                    <td>ListAssociatedIssues</td>
                    <td>查询当前工作项已经关联的工作项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIssueAssociatedCommits</td>
                    <td>查询当前工作项已经关联的代码提交记录 / 分支创建记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadIssueImg</td>
                    <td>上传图片</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIssueCustomFields</td>
                    <td>查询Scrum工作项自定义字段的可选列表,符合custom_fields或者names条件的都返回,2个值都不传,返回所有的自定义字段列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAssociatedWikis</td>
                    <td>查询当前工作项已经关联的关联Wiki</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIssueV4</td>
                    <td>查询工作项详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStatusStatistic</td>
                    <td>查询迭代下工作项状态的统计数据(处理人维度)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIssueCommentsV4</td>
                    <td>获取工作项的评论</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSpecIssueStayTimes</td>
                    <td>获取指定工作项停留时间</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectWorkHours</td>
                    <td>按用户查询工时(单项目)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadAttachment</td>
                    <td>下载工作项附件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCustomfields</td>
                    <td>创建工作项类型自定义字段</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectIssuesRecordsV4</td>
                    <td>查询项目下所有工作项的历史记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchIssues</td>
                    <td>高级查询我的待办工作项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIssuesV4</td>
                    <td>根据筛选条件查询工作项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadAttachments</td>
                    <td>上传工作项附件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIssueV4</td>
                    <td>创建工作项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIssuesWrokFlowConfig</td>
                    <td>查询Scrum项目的工作项流转配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadImageFile</td>
                    <td>下载图片</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIssueRecordsV4</td>
                    <td>获取工作项历史记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIssueCompletionRate</td>
                    <td>获取工作项的完成率</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIssueV4</td>
                    <td>更新工作项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSystemIssueV4</td>
                    <td>拥有IAM细粒度权限(projectmanConfig:systemSettingField:set)且在devcloud项目中有创建工作项的权限的用户可以设置工作项的创建者</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectWorkHoursType</td>
                    <td>查询项目下的工时类型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListAssociatedIssues</td>
                    <td>查询当前项目下已经关联的工作项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIssuesSfV4</td>
                    <td>工作项类型id, 分页参数,创建时间查询项目的工作项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteIssuesV4</td>
                    <td>批量删除工作项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddIssueWorkHours</td>
                    <td>添加指定工作项工时</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAttachment</td>
                    <td>取消工作项与附件关联,如附件为工作项页面上传则删除附件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListChildIssuesV4</td>
                    <td>获取子工作项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAssociatedTestCases</td>
                    <td>查询关联用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectWorkHours</td>
                    <td>按用户查询工时(多项目)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIssueV4</td>
                    <td>删除工作项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Scrum项目的模块</td>
                    <td>DeleteProjectModule</td>
                    <td>删除项目的模块</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProjectModule</td>
                    <td>更新项目的模块</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectModule</td>
                    <td>查询项目的模块列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectModules</td>
                    <td>查询项目的模块列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Scrum项目的状态</td>
                    <td>ListScrumProjectStatuses</td>
                    <td>查询项目的状态列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Scrum项目的迭代</td>
                    <td>ListIterationHistories</td>
                    <td>查看迭代历史记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIterationV4</td>
                    <td>更新Scrum项目迭代</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIterationV4</td>
                    <td>删除项目迭代</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteIterationsV4</td>
                    <td>批量删除项目的迭代</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIterationV4</td>
                    <td>创建Scrum项目迭代</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectIterationsV4</td>
                    <td>获取项目迭代</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIterationV4</td>
                    <td>查看迭代详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Scrum项目的领域</td>
                    <td>ListProjectDomains</td>
                    <td>查询项目的领域列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectDomain</td>
                    <td>查询项目的领域列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelProjectDomain</td>
                    <td>取消领域与项目的关联关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProjectDomain</td>
                    <td>更新项目的领域</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">用户信息</td>
                    <td>UpdateNickNameV4</td>
                    <td>更新用户昵称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCurUserInfo</td>
                    <td>获取当前用户信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCurUserRole</td>
                    <td>获取用户在项目中的角色</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateChildNickNames</td>
                    <td>拥有te_admin角色的用户可以更新其他用户的昵称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">看板项目的工作项</td>
                    <td>ListWorkitemStatusRecordsV4</td>
                    <td>分页查询看板项目下工作项的状态历史记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkItemWrokflowConfig</td>
                    <td>查询看板项目的工作项流转配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkitems</td>
                    <td>查询看板项目下的工作项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">项目信息</td>
                    <td>CreateProjectV4</td>
                    <td>创建项目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProjectV4</td>
                    <td>删除项目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProjectV4</td>
                    <td>更新项目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckProjectNameV4</td>
                    <td>检查项目名称是否存在</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainNotAddedProjectsV4</td>
                    <td>获取租户没有加入的项目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectsV4</td>
                    <td>查询项目列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectInfoV4</td>
                    <td>获取项目详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplates</td>
                    <td>查询项目模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">项目成员</td>
                    <td>AddApplyJoinProjectForAgc</td>
                    <td>AGC调用 当前用户申请加入项目, 申请的用户id写在header中</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteMembersV4</td>
                    <td>批量删除项目成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddMemberV4</td>
                    <td>添加项目成员,可以添加跨租户成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectMembersV4</td>
                    <td>获取项目成员列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddMembersV4</td>
                    <td>批量添加项目成员,只能添加和项目创建者同一租户下的成员,不正确的用户id会略过,添加的用户超过权限的,默认角色设置为7</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveProject</td>
                    <td>项目成员主动退出项目,项目创建者不能退出</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMembesRoleV4</td>
                    <td>更新成员在项目中的角色</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">项目指标</td>
                    <td>ShowCompletionRate</td>
                    <td>查询需求按时完成率</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBugsPerDeveloper</td>
                    <td>查询人均bug</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBugDensityV2</td>
                    <td>查询缺陷密度</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">项目统计</td>
                    <td>ListProjectDemandStaticV4</td>
                    <td>获取需求统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectSummaryV4</td>
                    <td>获取项目概览</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectBugStaticsV4</td>
                    <td>获取bug统计信息,按模块统计</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
