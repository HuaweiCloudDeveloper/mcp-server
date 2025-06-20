# CodeHub MCP Server 

## 版本信息
v0.1.0

## 产品描述

CodeHub MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CodeHub交互的能力。可以基于自然语言对CodeHub资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Commit | ShowDiffCommit | 根据commit id查询提交差异信息。 | To be tested |
|  | ListCommits | 根据仓库短ID获取提交信息,支持根据文件路径,查询这个路径下所有的commits列表。 | To be tested |
|  | ShowSingleCommit | 获取由commit id或分支或标记的名称标识的特定提交。 | To be tested |
|  | CreateCommit | 能够一次提交位于不同目录的多个文件,目录不存在时,能自动创建目录。支持强制覆盖选项,当选择强制覆盖标志为true时,忽略冲突,强制提交。 | To be tested |
| Discussion | CreateMergeRequestDiscussionNote | 回复MR检视意见 | To be tested |
|  | CreateMergeRequestDiscussion | 创建MR检视意见 | To be tested |
|  | ShowReviewSetting | 获取检视意见设置 | To be tested |
| File | ShowFile | 获取仓库中文件的信息,如名称、大小、内容。请注意,文件内容是Base64编码的。 | To be tested |
|  | ListFilesByQuery | 获取仓库中文件的信息,如名称、大小、内容。请注意,文件内容是Base64编码的。 | To be tested |
| Group | AssociateRepositoryUserGroup | 关联仓库与成员组 | To be tested |
|  | DeleteGroup | 删除代码组 | To be tested |
|  | ListManageableGroups | 项目下拥有创建权限的代码组列表 | To be tested |
|  | ShowGroup | 获取代码组信息 | To be tested |
|  | CreateGroup | 创建代码组 | To be tested |
|  | AssociateGroupUserGroup | 关联代码组与成员组 | To be tested |
| Project | ShowRepositoryNameExist | 一般创建仓库时调用。通过传入项目ID,获取方式请参见[获取项目ID](codehub_api_0014.xml)。,仓库名,来判断仓库是否重名。仓库存在result:false,仓库不存在result:true。 | To be tested |
|  | GetAllRepositoryByProjectId | 获取仓库列表 模糊查询支持范围,如果未传入project_id,则支持按仓库名或项目名模糊查询,否则,只按仓库名模糊匹配。 | To be tested |
|  | GetProductTemplates | 获取一个项目下可以设置为公开状态的仓库列表 | To be tested |
|  | ListProductTwoTemplates | 获取一个项目下可以设置为公开状态的仓库列表 | To be tested |
| RepoMember | SetRepoRole | 给仓库中成员设置仓库的操作权限, | To be tested |
|  | DeleteRepoMember | 删除仓库成员 | To be tested |
|  | AddRepoMembers | 添加仓库成员。 | To be tested |
|  | ListRepoMembers | 获取仓库成员列表,可通过关键字搜索某成员。 | To be tested |
| Repository | ShowBranchesByTwoRepositoryId | 查询指定仓库对应的分支。 | To be tested |
|  | ShowStatisticalData | 获取仓库统计数据 | To be tested |
|  | DeleteRepository | 根据仓库32位uuid删除指定的仓库 | To be tested |
|  | DeleteDeployKeyV2 | 删除仓库部署密钥 | To be tested |
|  | ShowRepoId | 获取仓库短id,用于获取仓库详情页面url | To be tested |
|  | ListTrustedIpAddresses | 获取仓库ip白名单 | To be tested |
|  | ListSubfiles | 获取分支目录下的文件 | To be tested |
|  | ShowRepositoryArchive | 按照指定格式下载仓库 | To be tested |
|  | CreateRepository | 用指定的名称在指定项目上创建仓库。传入参数:仓库名、模板id、是否导入项目成员、归属项目 | To be tested |
|  | ListRepositoryStatus | 获取仓库状态。 | To be tested |
|  | DeleteTrustedIpAddress | 删除仓库ip白名单 | To be tested |
|  | AddDeployKey | 添加部署密钥 | To be tested |
|  | ListTemplatesTwo | 设置仓库是公开状态还是私有状态 | To be tested |
|  | ShowMaster | 判断用户是否有仓库的管理员权限 | To be tested |
|  | ListMergeChangesTrees | 获取变更文件列表 | To be tested |
|  | UpdateMergeRequestApprovalState | 合并请求代码审核 | To be tested |
|  | ShowRepositoryByUuid | 根据仓库UUID(由CreateRepository接口返回)获取仓库信息仓库信息。返回 包含id,name,组名,仓库访问URL。 | To be tested |
|  | AddDeployKeyV2 | 添加部署密钥 | To be tested |
|  | ListRelatedCommits | 获取关联工作项信息 | To be tested |
|  | DeleteDeployKey | 删除仓库部署密钥 | To be tested |
|  | GetTemplates | 获取公开示例模板列表 | To be tested |
|  | ShowStatisticCommit | 获取指定日期内代码仓指定分支的代码提交行数 | To be tested |
|  | LockRepository | 根据仓库短ID锁定仓库 | To be tested |
|  | ListCommitStatistics | 获取仓库上一次的提交统计信息 | To be tested |
|  | AddProtectBranchV2 | 新建保护分支 | To be tested |
|  | ListBranchesByRepositoryId | 获取仓库分支列表 | To be tested |
|  | ShowStatisticCommitV3 | 获取指定日期内代码仓指定分支的代码提交行数 | To be tested |
|  | ListMergeRequest | 获取仓库合并请求列表 | To be tested |
|  | ShareTemplates | 设置仓库是公开状态还是私有状态 | To be tested |
|  | UnlockRepository | 根据仓库短ID解锁仓库 | To be tested |
|  | ListFiles | 获取一个仓库下特定分支指定文件内容 | To be tested |
|  | AddTrustedIpAddress | 添加仓库ip白名单 | To be tested |
|  | AddTagV2 | 新建标签 | To be tested |
|  | ListTwoTemplates | 获取公开示例模板列表 | To be tested |
|  | ListMergeChanges | 获取变更文件 | To be tested |
|  | ListMergeRequestReviewers | 根据仓库短ID和合并请求短ID获取检视人信息 | To be tested |
|  | UpdateTrustedIpAddress | 修改仓库ip白名单 | To be tested |
|  | ShowCommitsByBranch | 根据仓库组名、仓库名和分支获取提交列表。 | To be tested |
|  | ShowBranchesByRepositoryId | 根据仓库id获取指定仓库的分支列表. | To be tested |
|  | GetRepositoryByProjectId | 不建议再使用,建议使用/{repository_uuid}/status | To be tested |
|  | ShowImageBlob | 获取一个仓库下特定分支的图片文件 | To be tested |
|  | ShowCommitsByRepoId | 根据仓库id查询仓库某分支对应的提交. | To be tested |
|  | ShowMergeRequest | 获取仓库合并请求详情 | To be tested |
|  | ShowHasPipeline | 修改被流水线引用的仓库状态 | To be tested |
|  | ShowRepositoryStatistics | 根据仓库短id,查询仓库的代码提交记录统计 | To be tested |
| SSHKey | AddSshKey | 添加ssh key | To be tested |
|  | ListSshKeys | 获取ssh key列表。 | To be tested |
|  | DeleteSShkey | 删除用户公钥。 | To be tested |
|  | ShowPrivateKeyVerify | 检验私钥是否有拉取代码的权限 | To be tested |
| Tenant | ListTenantTrustedIpAddresses | 获取租户ip白名单 | To be tested |
|  | UpdateTenantTrustedIpAddress | 修改租户ip白名单 | To be tested |
|  | DeleteTenantTrustedIpAddress | 删除租户ip白名单 | To be tested |
|  | AddTenantTrustedIpAddress | 添加租户ip白名单 | To be tested |
| User | ValidateHttpsInfo | 判断用户使用 https 上传/下载代码时输入的用户名和密码是否合法。 | To be tested |
|  | ValidateHttpsInfoV2 | 判断用户使用 https 上传/下载代码时输入的用户名和密码是否合法。 | To be tested |
| V2Project | ShowAllRepositoryByTwoProjectId | 获取仓库列表,模糊查询支持范围,如果未传入project uuid,则支持按仓库名或项目名模糊查询,否则,只按仓库名模糊匹配 | To be tested |
|  | CreateProjectAndforkRepositories | 创建仓库后fork仓库 传入参数:仓库名、是否导入项目成员、归属项目 | To be tested |
|  | CreateProjectAndRepositories | 创建项目后,创建仓库组由后台生成方式 传入参数:仓库名、模板id、是否导入项目成员、归属项目 | To be tested |
|  | ListUserAllRepositories | 获取用户的所有仓库信息 | To be tested |
|  | AssociateIssues | 分支关联工作项 | To be tested |
| WebHook | DeleteHooks | 提交代码自动触发编译构建,删除仓库钩子 | To be tested |
|  | ListHooks | 获取仓库webhook | To be tested |
|  | AddHooks | 提交代码自动触发编译构建,添加仓库钩子 | To be tested |
| v2仓库管理 | CreateNewBranch | 根据仓库id在指定仓库中创建分支 | To be tested |
