# ProjectMan MCP Server 

## 版本信息
v0.1.0

## 产品描述

ProjectMan MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务ProjectMan交互的能力。可以基于自然语言对ProjectMan资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Scrum项目的工作项 | ListAssociatedIssues | 查询当前工作项已经关联的工作项 | To be tested |
|  | ListIssueAssociatedCommits | 查询当前工作项已经关联的代码提交记录 / 分支创建记录 | To be tested |
|  | UploadIssueImg | 上传图片 | To be tested |
|  | ListIssueCustomFields | 查询Scrum工作项自定义字段的可选列表,符合custom_fields或者names条件的都返回,2个值都不传,返回所有的自定义字段列表 | To be tested |
|  | ListAssociatedWikis | 查询当前工作项已经关联的关联Wiki | To be tested |
|  | ShowIssueV4 | 查询工作项详情 | To be tested |
|  | ListStatusStatistic | 查询迭代下工作项状态的统计数据(处理人维度) | To be tested |
|  | ListIssueCommentsV4 | 获取工作项的评论 | To be tested |
|  | ListSpecIssueStayTimes | 获取指定工作项停留时间 | To be tested |
|  | ShowProjectWorkHours | 按用户查询工时(单项目) | To be tested |
|  | DownloadAttachment | 下载工作项附件 | To be tested |
|  | CreateCustomfields | 创建工作项类型自定义字段 | To be tested |
|  | ListProjectIssuesRecordsV4 | 查询项目下所有工作项的历史记录 | To be tested |
|  | SearchIssues | 高级查询我的待办工作项 | To be tested |
|  | ListIssuesV4 | 根据筛选条件查询工作项 | To be tested |
|  | UploadAttachments | 上传工作项附件 | To be tested |
|  | CreateIssueV4 | 创建工作项 | To be tested |
|  | ShowIssuesWrokFlowConfig | 查询Scrum项目的工作项流转配置 | To be tested |
|  | DownloadImageFile | 下载图片 | To be tested |
|  | ListIssueRecordsV4 | 获取工作项历史记录 | To be tested |
|  | ShowIssueCompletionRate | 获取工作项的完成率 | To be tested |
|  | UpdateIssueV4 | 更新工作项 | To be tested |
|  | CreateSystemIssueV4 | 拥有IAM细粒度权限(projectmanConfig:systemSettingField:set)且在devcloud项目中有创建工作项的权限的用户可以设置工作项的创建者 | To be tested |
|  | ListProjectWorkHoursType | 查询项目下的工时类型 | To be tested |
|  | BatchListAssociatedIssues | 查询当前项目下已经关联的工作项 | To be tested |
|  | ListIssuesSfV4 | 工作项类型id, 分页参数,创建时间查询项目的工作项 | To be tested |
|  | BatchDeleteIssuesV4 | 批量删除工作项 | To be tested |
|  | AddIssueWorkHours | 添加指定工作项工时 | To be tested |
|  | DeleteAttachment | 取消工作项与附件关联,如附件为工作项页面上传则删除附件 | To be tested |
|  | ListChildIssuesV4 | 获取子工作项 | To be tested |
|  | ListAssociatedTestCases | 查询关联用例 | To be tested |
|  | ListProjectWorkHours | 按用户查询工时(多项目) | To be tested |
|  | DeleteIssueV4 | 删除工作项 | To be tested |
| Scrum项目的模块 | DeleteProjectModule | 删除项目的模块 | To be tested |
|  | UpdateProjectModule | 更新项目的模块 | To be tested |
|  | CreateProjectModule | 查询项目的模块列表 | To be tested |
|  | ListProjectModules | 查询项目的模块列表 | To be tested |
| Scrum项目的状态 | ListScrumProjectStatuses | 查询项目的状态列表 | To be tested |
| Scrum项目的迭代 | ListIterationHistories | 查看迭代历史记录 | To be tested |
|  | UpdateIterationV4 | 更新Scrum项目迭代 | To be tested |
|  | DeleteIterationV4 | 删除项目迭代 | To be tested |
|  | BatchDeleteIterationsV4 | 批量删除项目的迭代 | To be tested |
|  | CreateIterationV4 | 创建Scrum项目迭代 | To be tested |
|  | ListProjectIterationsV4 | 获取项目迭代 | To be tested |
|  | ShowIterationV4 | 查看迭代详情 | To be tested |
| Scrum项目的领域 | ListProjectDomains | 查询项目的领域列表 | To be tested |
|  | CreateProjectDomain | 查询项目的领域列表 | To be tested |
|  | CancelProjectDomain | 取消领域与项目的关联关系 | To be tested |
|  | UpdateProjectDomain | 更新项目的领域 | To be tested |
| 用户信息 | UpdateNickNameV4 | 更新用户昵称 | To be tested |
|  | ShowCurUserInfo | 获取当前用户信息 | To be tested |
|  | ShowCurUserRole | 获取用户在项目中的角色 | To be tested |
|  | BatchUpdateChildNickNames | 拥有te_admin角色的用户可以更新其他用户的昵称 | To be tested |
| 看板项目的工作项 | ListWorkitemStatusRecordsV4 | 分页查询看板项目下工作项的状态历史记录 | To be tested |
|  | ShowWorkItemWrokflowConfig | 查询看板项目的工作项流转配置 | To be tested |
|  | ListWorkitems | 查询看板项目下的工作项 | To be tested |
| 项目信息 | CreateProjectV4 | 创建项目 | To be tested |
|  | DeleteProjectV4 | 删除项目 | To be tested |
|  | UpdateProjectV4 | 更新项目 | To be tested |
|  | CheckProjectNameV4 | 检查项目名称是否存在 | To be tested |
|  | ListDomainNotAddedProjectsV4 | 获取租户没有加入的项目 | To be tested |
|  | ListProjectsV4 | 查询项目列表 | To be tested |
|  | ShowProjectInfoV4 | 获取项目详情 | To be tested |
|  | ListTemplates | 查询项目模板 | To be tested |
| 项目成员 | AddApplyJoinProjectForAgc | AGC调用 当前用户申请加入项目, 申请的用户id写在header中 | To be tested |
|  | BatchDeleteMembersV4 | 批量删除项目成员 | To be tested |
|  | AddMemberV4 | 添加项目成员,可以添加跨租户成员 | To be tested |
|  | ListProjectMembersV4 | 获取项目成员列表 | To be tested |
|  | BatchAddMembersV4 | 批量添加项目成员,只能添加和项目创建者同一租户下的成员,不正确的用户id会略过,添加的用户超过权限的,默认角色设置为7 | To be tested |
|  | RemoveProject | 项目成员主动退出项目,项目创建者不能退出 | To be tested |
|  | UpdateMembesRoleV4 | 更新成员在项目中的角色 | To be tested |
| 项目指标 | ShowCompletionRate | 查询需求按时完成率 | To be tested |
|  | ShowBugsPerDeveloper | 查询人均bug | To be tested |
|  | ShowBugDensityV2 | 查询缺陷密度 | To be tested |
| 项目统计 | ListProjectDemandStaticV4 | 获取需求统计信息 | To be tested |
|  | ShowProjectSummaryV4 | 获取项目概览 | To be tested |
|  | ListProjectBugStaticsV4 | 获取bug统计信息,按模块统计 | To be tested |
