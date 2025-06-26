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
                    <td>根据commit id查询提交差异信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCommits</td>
                    <td>根据仓库短ID获取提交信息,支持根据文件路径,查询这个路径下所有的commits列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSingleCommit</td>
                    <td>获取由commit id或分支或标记的名称标识的特定提交。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCommit</td>
                    <td>能够一次提交位于不同目录的多个文件,目录不存在时,能自动创建目录。支持强制覆盖选项,当选择强制覆盖标志为true时,忽略冲突,强制提交。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">DDM实例管理</td>
                    <td>CreateGroup</td>
                    <td>创建组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Discussion</td>
                    <td>CreateMergeRequestDiscussionNote</td>
                    <td>回复MR检视意见</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMergeRequestDiscussion</td>
                    <td>创建MR检视意见</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReviewSetting</td>
                    <td>获取检视意见设置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">File</td>
                    <td>ShowFile</td>
                    <td>获取仓库中文件的信息,如名称、大小、内容。请注意,文件内容是Base64编码的。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFilesByQuery</td>
                    <td>获取仓库中文件的信息,如名称、大小、内容。请注意,文件内容是Base64编码的。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Group</td>
                    <td>AssociateRepositoryUserGroup</td>
                    <td>关联仓库与成员组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGroup</td>
                    <td>删除代码组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListManageableGroups</td>
                    <td>项目下拥有创建权限的代码组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateGroupUserGroup</td>
                    <td>关联代码组与成员组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Project</td>
                    <td>ShowRepositoryNameExist</td>
                    <td>一般创建仓库时调用。通过传入项目ID,获取方式请参见[获取项目ID](codehub_api_0014.xml)。,仓库名,来判断仓库是否重名。仓库存在result:false,仓库不存在result:true。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetAllRepositoryByProjectId</td>
                    <td>获取仓库列表 模糊查询支持范围,如果未传入project_id,则支持按仓库名或项目名模糊查询,否则,只按仓库名模糊匹配。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetProductTemplates</td>
                    <td>获取一个项目下可以设置为公开状态的仓库列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProductTwoTemplates</td>
                    <td>获取一个项目下可以设置为公开状态的仓库列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">RepoMember</td>
                    <td>SetRepoRole</td>
                    <td>给仓库中成员设置仓库的操作权限,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRepoMember</td>
                    <td>删除仓库成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddRepoMembers</td>
                    <td>添加仓库成员。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRepoMembers</td>
                    <td>获取仓库成员列表,可通过关键字搜索某成员。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="44">Repository</td>
                    <td>ShowBranchesByTwoRepositoryId</td>
                    <td>查询指定仓库对应的分支。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRepository</td>
                    <td>根据仓库32位uuid删除指定的仓库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeployKeyV2</td>
                    <td>删除仓库部署密钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRepoId</td>
                    <td>获取仓库短id,用于获取仓库详情页面url</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTrustedIpAddresses</td>
                    <td>获取仓库ip白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubfiles</td>
                    <td>获取分支目录下的文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRepositoryArchive</td>
                    <td>按照指定格式下载仓库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRepository</td>
                    <td>用指定的名称在指定项目上创建仓库。传入参数:仓库名、模板id、是否导入项目成员、归属项目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRepositoryStatus</td>
                    <td>获取仓库状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrustedIpAddress</td>
                    <td>删除仓库ip白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDeployKey</td>
                    <td>添加部署密钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplatesTwo</td>
                    <td>设置仓库是公开状态还是私有状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMaster</td>
                    <td>判断用户是否有仓库的管理员权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMergeChangesTrees</td>
                    <td>获取变更文件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMergeRequestApprovalState</td>
                    <td>合并请求代码审核</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRepositoryByUuid</td>
                    <td>根据仓库UUID(由CreateRepository接口返回)获取仓库信息仓库信息。返回 包含id,name,组名,仓库访问URL。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDeployKeyV2</td>
                    <td>添加部署密钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRelatedCommits</td>
                    <td>获取关联工作项信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeployKey</td>
                    <td>删除仓库部署密钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetTemplates</td>
                    <td>获取公开示例模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStatisticCommit</td>
                    <td>获取指定日期内代码仓指定分支的代码提交行数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LockRepository</td>
                    <td>根据仓库短ID锁定仓库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCommitStatistics</td>
                    <td>获取仓库上一次的提交统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddProtectBranchV2</td>
                    <td>新建保护分支</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBranchesByRepositoryId</td>
                    <td>获取仓库分支列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStatisticCommitV3</td>
                    <td>获取指定日期内代码仓指定分支的代码提交行数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMergeRequest</td>
                    <td>获取仓库合并请求列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShareTemplates</td>
                    <td>设置仓库是公开状态还是私有状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnlockRepository</td>
                    <td>根据仓库短ID解锁仓库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFiles</td>
                    <td>获取一个仓库下特定分支指定文件内容</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTrustedIpAddress</td>
                    <td>添加仓库ip白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTagV2</td>
                    <td>新建标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTwoTemplates</td>
                    <td>获取公开示例模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMergeChanges</td>
                    <td>获取变更文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMergeRequestReviewers</td>
                    <td>根据仓库短ID和合并请求短ID获取检视人信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTrustedIpAddress</td>
                    <td>修改仓库ip白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCommitsByBranch</td>
                    <td>根据仓库组名、仓库名和分支获取提交列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBranchesByRepositoryId</td>
                    <td>根据仓库id获取指定仓库的分支列表.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetRepositoryByProjectId</td>
                    <td>不建议再使用,建议使用/{repository_uuid}/status</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageBlob</td>
                    <td>获取一个仓库下特定分支的图片文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCommitsByRepoId</td>
                    <td>根据仓库id查询仓库某分支对应的提交.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMergeRequest</td>
                    <td>获取仓库合并请求详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHasPipeline</td>
                    <td>修改被流水线引用的仓库状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRepositoryStatistics</td>
                    <td>根据仓库短id,查询仓库的代码提交记录统计</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">SSHKey</td>
                    <td>AddSshKey</td>
                    <td>添加ssh key</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSshKeys</td>
                    <td>获取ssh key列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSShkey</td>
                    <td>删除用户公钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateKeyVerify</td>
                    <td>检验私钥是否有拉取代码的权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Tenant</td>
                    <td>ListTenantTrustedIpAddresses</td>
                    <td>获取租户ip白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTenantTrustedIpAddress</td>
                    <td>修改租户ip白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTenantTrustedIpAddress</td>
                    <td>删除租户ip白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTenantTrustedIpAddress</td>
                    <td>添加租户ip白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">User</td>
                    <td>ValidateHttpsInfo</td>
                    <td>判断用户使用 https 上传/下载代码时输入的用户名和密码是否合法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateHttpsInfoV2</td>
                    <td>判断用户使用 https 上传/下载代码时输入的用户名和密码是否合法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">V2Project</td>
                    <td>ShowAllRepositoryByTwoProjectId</td>
                    <td>获取仓库列表,模糊查询支持范围,如果未传入project uuid,则支持按仓库名或项目名模糊查询,否则,只按仓库名模糊匹配</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectAndforkRepositories</td>
                    <td>创建仓库后fork仓库 传入参数:仓库名、是否导入项目成员、归属项目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectAndRepositories</td>
                    <td>创建项目后,创建仓库组由后台生成方式 传入参数:仓库名、模板id、是否导入项目成员、归属项目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserAllRepositories</td>
                    <td>获取用户的所有仓库信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateIssues</td>
                    <td>分支关联工作项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">WebHook</td>
                    <td>DeleteHooks</td>
                    <td>提交代码自动触发编译构建,删除仓库钩子</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHooks</td>
                    <td>获取仓库webhook</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddHooks</td>
                    <td>提交代码自动触发编译构建,添加仓库钩子</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">v2仓库管理</td>
                    <td>CreateNewBranch</td>
                    <td>根据仓库id在指定仓库中创建分支</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">实例管理</td>
                    <td>ShowStatisticalData</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">消费组管理</td>
                    <td>ShowGroup</td>
                    <td>查询指定消费组详情。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
