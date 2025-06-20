# CloudTest MCP Server 

## 版本信息
v0.1.0

## 产品描述

CloudTest MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CloudTest交互的能力。可以基于自然语言对CloudTest资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| ApigAutoInitController | CreateApiTestSuiteByRepoFile | 通过导入仓库中的文件生成接口测试套 | To be tested |
| ApigVariableGroupController | ListEnvironments | 获取环境参数分组列表 | To be tested |
| TestcaseManagement | ListTestcasePlans | 根据测试用例URI或用例编号查询测试用例对应的测试计划 | To be tested |
| attachment-controller | UploadStepImg | 对外API | To be tested |
| test-item-controller | AddFeature | 添加目录信息 | To be tested |
| 拨测仪表盘信息管理 | ListUsingGet | 查询仪表盘用户的看板 | To be tested |
|  | ListMsgInfosUsing | 成功返回MsgInfo的详细信息列表,返回值为Model的List | To be tested |
|  | ListScattersUsing | 查询仪表盘散点图数据 | To be tested |
|  | ListAlarmStatisticsUsing | 查询告警统计数据 | To be tested |
|  | ShowOperationalDataCurrentMonthUsing | 成功返回运行面板信息 | To be tested |
|  | ListLinesUsing | 查询仪表盘折线图数据 | To be tested |
|  | ListSubTaskCaseOverstockUsing | 成功返回子任务用例数据积压信息 | To be tested |
| 拨测任务配置管理 | SaveTaskSetting | 保存任务配置 | To be tested |
|  | ShowAllConfigValueByTypeAndKey | 查询任务配置 | To be tested |
| 拨测告警信息管理 | ShowIfTaskNameRepeat | 查询告警模板名称是否重复 | To be tested |
|  | ListAlertGroupsByCondition | 查询告警组列表 | To be tested |
|  | ListAlertTemplates | 查询告警模板 | To be tested |
|  | ListAllConfigItemByType | 查询任务告警信息 | To be tested |
|  | ShowIfUserNameRepeat | 查询告警组用户名是否重复 | To be tested |
| 拨测套餐状态查询 | ShowEchoTestPackageUsing | 查询租户在线拨测套餐状态 | To be tested |
|  | ShowConcurrencyPackageUsing | 查询租户测试并发套餐状态 | To be tested |
| 接口测试套餐用量管理 | ListUserPackageUsage |  | To be tested |
|  | ListUserPopupInfo |  | To be tested |
| 接口测试管理 | ListPublicLibAndAws | 获取工程关联的公共aw信息和公共aw所属公共aw库信息 | To be tested |
|  | ListBasicAwInfoListSupportsSearch | 分页获取工程BasicAW列表(含目录) | To be tested |
|  | UpdateTestCaseAndScript | 更新tmss用例和用例脚本 | To be tested |
|  | ShowApiTestcaseHistories | 获取用例历史执行数据 | To be tested |
|  | UpdateBasicAwById | 修改关键字信息接口 | To be tested |
|  | UpdateUserDnsMapping | 更新用户DNS映射,执行器自定义映射 | To be tested |
|  | ListTestCaseScriptDetail | 获取用例脚本详细信息 | To be tested |
|  | CreateUserDefinedUrlKeyWord | 新增用户自定义URL关键字 | To be tested |
|  | ListVariables | 查询全局变量参数列表V4 | To be tested |
|  | ListUserDnsMapping | 查询用户DNS映射 | To be tested |
|  | ListCasesStatus | 批量获取用例状态 | To be tested |
|  | ListBasicAw | 根据id获取单个basicAW信息 | To be tested |
|  | ListAvailableConfig | 获取当前局点功能是否开启 | To be tested |
|  | DeleteBasicAwById | 融合版本删除单个basicAw | To be tested |
| 查询单次测试套执行的详细结果 | ListTaskResultsDetail | 查询单次测试套执行的详细结果 | To be tested |
| 根据任务uri查询测试任务执行历史 | ListTaskResults | 根据任务uri查询测试任务执行历史 | To be tested |
| 测试报表管理 | ListTestReportsByCondition | 根据查询条件获取测试报告列表 | To be tested |
|  | BatchDeleteTestReport | 根据测试报告uri列表,删除测试报告 | To be tested |
|  | ShowRequirementsOverview | 质量报告需求测试情况统计 | To be tested |
|  | ShowTestCaseAndDefectInfo | 查询用户用例关联缺陷的统计信息 | To be tested |
|  | ShowUserExecuteTestCaseInfo | 查询时段内用例的执行情况 | To be tested |
|  | ShowProjectDataDashboard | 查询质量报告看板统计信息 | To be tested |
|  | ListReports | 页面报表展示 | To be tested |
|  | ShowReport | 实时计算单个自定义报表 | To be tested |
| 测试服务关联关系 | BatchAddRelationsByOneCase | 添加需求/缺陷和多个用例关联关系 | To be tested |
|  | ListTestCasesByIssue | 查询需求下的用例列表 | To be tested |
|  | DeleteRelationsByOneCase | 删除一个用例和多个需求/缺陷关联关系 | To be tested |
|  | CreateRelationsByOneCase | 添加一个用例和多个需求/缺陷关联关系 | To be tested |
| 测试计划管理 | ListIssueTree | 查询需求树 | To be tested |
|  | ShowPlanList | 项目下查询测试计划列表v2 | To be tested |
|  | RemoveIssuesFromIterator | 从迭代中移除需求 | To be tested |
|  | CreateIterator | 新增迭代 | To be tested |
|  | ShowIteratorDetail | 查询迭代计划详情,包含统计信息 | To be tested |
|  | ListIterators | 查询迭代计划列表,包含统计信息 | To be tested |
|  | ListAllIterators | 查询项目下所有迭代计划 | To be tested |
|  | ListIteratorIssueTree | 查询迭代关联的需求列表或树 | To be tested |
|  | ShowPlans | 项目下查询测试计划列表 | To be tested |
|  | ShowIssuesByPlanId | 查询某个测试计划下的需求列表 | To be tested |
|  | ShowBranch | 获取分支详情 | To be tested |
|  | ShowIteratorByDefect | 查询缺陷相关联测试计划 | To be tested |
|  | ShowPlanJournals | 查询某测试计划下的操作历史 | To be tested |
|  | UpdateIterator | 修改测试计划 | To be tested |
|  | CreatePlan | 项目下创建计划 | To be tested |
|  | CreateTestCaseInPlan | 计划中批量添加测试用例 | To be tested |
|  | ListDomainVisibleServices | 查询当前租户可见的第三方服务列表 | To be tested |
|  | ListBranches | 获取分支列表 | To be tested |
| 测试设计查询 | ShowStatisticById | 根据脑图id查询统计数目 | To be tested |
|  | CheckPermission | 检查项目权限 | To be tested |
|  | ShowTemplateByPage | 根据条件分页获取模板V3 | To be tested |
|  | ShowMindmapCreatorName | 获取脑图创建人V2 | To be tested |
|  | DeleteFacotrById | 删除因子 | To be tested |
|  | ShowMindmapByPage | 根据条件分页获取脑图对象V3 | To be tested |
|  | ShowSceneByPage | 根据条件分页获取场景对象V2 | To be tested |
|  | ShowTestcaseByPage | 根据条件分页获取测试用例对象V2 | To be tested |
|  | ShowReviewByPage | 根据条件分页获取评审对象V2 | To be tested |
|  | ShowAsset | 获取资产列表 | To be tested |
|  | ShowSystemConfigs | 根据入参动态查询系统配置中的信息 | To be tested |
|  | ShowAssetTree | 获取资产树列表 | To be tested |
|  | ShowMindMapById | 根据id获取脑图对象 | To be tested |
|  | ShowFactorByAssetId | 根据目录查询因子 | To be tested |
|  | ShowTemplateById | 获取模板V2 | To be tested |
|  | ShowFactorById | 根据id获取因子 | To be tested |
|  | ShowTestpointByPage | 根据条件分页获取测试点对象V2 | To be tested |
| 用例关联关系管理 | ListTestcasesByProjectIssuesRelation | 查询项目下关联了需求的用例列表 | To be tested |
| 自定义测试服务接入管理 | CreateService | 通过接口CreateService注册成为自定义服务。 注册完成后界面将会出现此自定义测试类型。 | To be tested |
|  | DeleteService | 删除已注册服务 | To be tested |
|  | UpdateService | 更新已注册服务 | To be tested |
|  | ShowRegisterService | 用户获取自己当前已经注册的服务 | To be tested |
|  | ShowAllFeatureChildren | 获取目录\特性树 | To be tested |
| 自定义测试服务测试套件管理 | ListTaskAssignCases | 获取测试套关联用例详情 | To be tested |
|  | CreateTaskDefaultResult | 初始化测试任务执行记录 | To be tested |
|  | ListTasks | 查询测试任务列表 | To be tested |
|  | ListTaskTestCases | 查询用例关联的测试任务列表 | To be tested |
| 自定义测试服务用例管理 | ListAllBranches | 获取分支列表 | To be tested |
|  | UpdateTestCaseComment | 修改用例评论 | To be tested |
|  | ShowTestCaseDetail | 获取测试用例详情 | To be tested |
|  | BatchDeleteTestCase | 批量删除自定义测试服务类型用例 | To be tested |
|  | ListProjectTestCaseFields | 获取项目测试用例自定义字段列表 | To be tested |
|  | ShowUserAccessInfo | 获取租户订单信息 | To be tested |
|  | ShowFreeDeclaration | 查询限时免费用户免责声明记录 | To be tested |
|  | ListTestCases | 查询用例列表 | To be tested |
|  | ShowProgress | 获取异步进度 | To be tested |
|  | BatchUpdateVersionTestCases | 批量更新用例属性 | To be tested |
|  | AddCaseResultFour | 设置用例结果 | To be tested |
|  | CreateProjectBranch | 新增分支 | To be tested |
|  | ShowBackgroundInfo | 获取测试报告的模板设置 | To be tested |
|  | ListResourcePools | 获取资源池列表 | To be tested |
|  | UpdateTestCaseResult | 批量更新测试用例结果 | To be tested |
|  | BatchRemoveTestCasesFromIterator | 从迭代中批量移除用例 | To be tested |
|  | RunTestCase | 批量执行测试用例 | To be tested |
|  | ShowDisclaimerRecord | 查询用户免责声明 | To be tested |
|  | ShowDomainInfo | 根据domainId获取加密的testbirdkey | To be tested |
|  | CreateResourceUri | 生成资源URI | To be tested |
|  | UpdateTestCase | 更新自定义测试服务类型用例 | To be tested |
|  | ListUsageInfos | 获取租户订单已用资源信息 | To be tested |
|  | ShowFeatureChildren | 获取目录\特性树 | To be tested |
|  | UpdateVersionTestCase | 在分支或者测试计划下修改用例 | To be tested |
|  | ListTestTypes | 获取测试类型列表 | To be tested |
|  | BatchDeleteTestCases | 批量删除用例 | To be tested |
|  | ListAttachments | 查询附件列表 | To be tested |
|  | ShowTestCase | 查询用例详情 | To be tested |
|  | CreateReport | 保存单个自定义报表 | To be tested |
|  | AddTestCaseComment | 新增用例评论 | To be tested |
|  | BatchAddResourcesForIterator | 向迭代中添加资源 | To be tested |
|  | ShowTestCaseReviews | 根据用例查询评审记录 | To be tested |
|  | ListTestCaseHistories | 查询用例修改历史记录 | To be tested |
|  | ShowTestCaseDetailV2 | 通过用例编号获取测试用例详情 | To be tested |
|  | AddTestCaseResultLog | 初始化用例执行记录 | To be tested |
|  | ListAllTestCases | 查询用例列表 | To be tested |
|  | CreateTestCase | 创建自定义测试服务类型用例 | To be tested |
|  | ShowTestCasesChangeStatistics | 版本测试用例变更统计(只统计分支,不统计基线) | To be tested |
|  | ListOwnTestCases | 获取责任人是自己的测试用例 | To be tested |
|  | ShowCaseResult | 查询用例结果 | To be tested |
|  | CreateVersionTestCase | 在分支或者测试计划下创建用例 | To be tested |
|  | ListTestCaseComments | 查询用例评论 | To be tested |
|  | ListProjectFieldConfigs | 查询项目字段配置 | To be tested |
|  | DeleteTestCaseComment | 删除用例评论 | To be tested |
