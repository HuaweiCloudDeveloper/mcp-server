# CloudTest MCP Server 


## Version
v0.1.0

## Overview

CloudTest MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CloudTest. Full-chain management of CloudTest resources can be carried out based on natural language.

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
                    <td rowspan="1">ApigAutoInitController</td>
                    <td>CreateApiTestSuiteByRepoFile</td>
                    <td>通过导入仓库中的文件生成接口测试套</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Attachments</td>
                    <td>ListAttachments</td>
                    <td>查询企业路由器实例下的连接列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ITaskController</td>
                    <td>ListTasks</td>
                    <td>获取任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TestcaseManagement</td>
                    <td>ListTestcasePlans</td>
                    <td>根据测试用例URI或用例编号查询测试用例对应的测试计划</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">attachment-controller</td>
                    <td>UploadStepImg</td>
                    <td>对外API</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">environment-controller-v2</td>
                    <td>ListEnvironments</td>
                    <td>查询应用下环境列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">test-item-controller</td>
                    <td>AddFeature</td>
                    <td>添加目录信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">全局变量管理</td>
                    <td>ListVariables</td>
                    <td>查询全局变量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">报告管理</td>
                    <td>ShowReport</td>
                    <td>查询报告</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">拨测仪表盘信息管理</td>
                    <td>ListUsingGet</td>
                    <td>查询仪表盘用户的看板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMsgInfosUsing</td>
                    <td>成功返回MsgInfo的详细信息列表,返回值为Model的List</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScattersUsing</td>
                    <td>查询仪表盘散点图数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmStatisticsUsing</td>
                    <td>查询告警统计数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOperationalDataCurrentMonthUsing</td>
                    <td>成功返回运行面板信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLinesUsing</td>
                    <td>查询仪表盘折线图数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubTaskCaseOverstockUsing</td>
                    <td>成功返回子任务用例数据积压信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">拨测任务配置管理</td>
                    <td>SaveTaskSetting</td>
                    <td>保存任务配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAllConfigValueByTypeAndKey</td>
                    <td>查询任务配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">拨测告警信息管理</td>
                    <td>ShowIfTaskNameRepeat</td>
                    <td>查询告警模板名称是否重复</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlertGroupsByCondition</td>
                    <td>查询告警组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlertTemplates</td>
                    <td>查询告警模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllConfigItemByType</td>
                    <td>查询任务告警信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIfUserNameRepeat</td>
                    <td>查询告警组用户名是否重复</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">拨测套餐状态查询</td>
                    <td>ShowEchoTestPackageUsing</td>
                    <td>查询租户在线拨测套餐状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConcurrencyPackageUsing</td>
                    <td>查询租户测试并发套餐状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">接口测试套餐用量管理</td>
                    <td>ListUserPackageUsage</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserPopupInfo</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">接口测试管理</td>
                    <td>ListPublicLibAndAws</td>
                    <td>获取工程关联的公共aw信息和公共aw所属公共aw库信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBasicAwInfoListSupportsSearch</td>
                    <td>分页获取工程BasicAW列表(含目录)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTestCaseAndScript</td>
                    <td>更新tmss用例和用例脚本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApiTestcaseHistories</td>
                    <td>获取用例历史执行数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBasicAwById</td>
                    <td>修改关键字信息接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserDnsMapping</td>
                    <td>更新用户DNS映射,执行器自定义映射</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTestCaseScriptDetail</td>
                    <td>获取用例脚本详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUserDefinedUrlKeyWord</td>
                    <td>新增用户自定义URL关键字</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserDnsMapping</td>
                    <td>查询用户DNS映射</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCasesStatus</td>
                    <td>批量获取用例状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBasicAw</td>
                    <td>根据id获取单个basicAW信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableConfig</td>
                    <td>获取当前局点功能是否开启</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBasicAwById</td>
                    <td>融合版本删除单个basicAw</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">服务管理</td>
                    <td>CreateService</td>
                    <td>创建服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteService</td>
                    <td>删除服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateService</td>
                    <td>修改服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询单次测试套执行的详细结果</td>
                    <td>ListTaskResultsDetail</td>
                    <td>查询单次测试套执行的详细结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">根据任务uri查询测试任务执行历史</td>
                    <td>ListTaskResults</td>
                    <td>根据任务uri查询测试任务执行历史</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">测试报表管理</td>
                    <td>ListTestReportsByCondition</td>
                    <td>根据查询条件获取测试报告列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTestReport</td>
                    <td>根据测试报告uri列表,删除测试报告</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRequirementsOverview</td>
                    <td>质量报告需求测试情况统计</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestCaseAndDefectInfo</td>
                    <td>查询用户用例关联缺陷的统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserExecuteTestCaseInfo</td>
                    <td>查询时段内用例的执行情况</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectDataDashboard</td>
                    <td>查询质量报告看板统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReports</td>
                    <td>页面报表展示</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">测试服务关联关系</td>
                    <td>BatchAddRelationsByOneCase</td>
                    <td>添加需求/缺陷和多个用例关联关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTestCasesByIssue</td>
                    <td>查询需求下的用例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRelationsByOneCase</td>
                    <td>删除一个用例和多个需求/缺陷关联关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRelationsByOneCase</td>
                    <td>添加一个用例和多个需求/缺陷关联关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="18">测试计划管理</td>
                    <td>ListIssueTree</td>
                    <td>查询需求树</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlanList</td>
                    <td>项目下查询测试计划列表v2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveIssuesFromIterator</td>
                    <td>从迭代中移除需求</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIterator</td>
                    <td>新增迭代</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIteratorDetail</td>
                    <td>查询迭代计划详情,包含统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIterators</td>
                    <td>查询迭代计划列表,包含统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllIterators</td>
                    <td>查询项目下所有迭代计划</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIteratorIssueTree</td>
                    <td>查询迭代关联的需求列表或树</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlans</td>
                    <td>项目下查询测试计划列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIssuesByPlanId</td>
                    <td>查询某个测试计划下的需求列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBranch</td>
                    <td>获取分支详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIteratorByDefect</td>
                    <td>查询缺陷相关联测试计划</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlanJournals</td>
                    <td>查询某测试计划下的操作历史</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIterator</td>
                    <td>修改测试计划</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlan</td>
                    <td>项目下创建计划</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTestCaseInPlan</td>
                    <td>计划中批量添加测试用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainVisibleServices</td>
                    <td>查询当前租户可见的第三方服务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBranches</td>
                    <td>获取分支列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">测试设计查询</td>
                    <td>ShowStatisticById</td>
                    <td>根据脑图id查询统计数目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckPermission</td>
                    <td>检查项目权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTemplateByPage</td>
                    <td>根据条件分页获取模板V3</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMindmapCreatorName</td>
                    <td>获取脑图创建人V2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFacotrById</td>
                    <td>删除因子</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMindmapByPage</td>
                    <td>根据条件分页获取脑图对象V3</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSceneByPage</td>
                    <td>根据条件分页获取场景对象V2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestcaseByPage</td>
                    <td>根据条件分页获取测试用例对象V2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReviewByPage</td>
                    <td>根据条件分页获取评审对象V2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAsset</td>
                    <td>获取资产列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSystemConfigs</td>
                    <td>根据入参动态查询系统配置中的信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAssetTree</td>
                    <td>获取资产树列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMindMapById</td>
                    <td>根据id获取脑图对象</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFactorByAssetId</td>
                    <td>根据目录查询因子</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTemplateById</td>
                    <td>获取模板V2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFactorById</td>
                    <td>根据id获取因子</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestpointByPage</td>
                    <td>根据条件分页获取测试点对象V2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">用例关联关系管理</td>
                    <td>ListTestcasesByProjectIssuesRelation</td>
                    <td>查询项目下关联了需求的用例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">自定义测试服务接入管理</td>
                    <td>ShowRegisterService</td>
                    <td>用户获取自己当前已经注册的服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAllFeatureChildren</td>
                    <td>获取目录\特性树</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">自定义测试服务测试套件管理</td>
                    <td>ListTaskAssignCases</td>
                    <td>获取测试套关联用例详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTaskDefaultResult</td>
                    <td>初始化测试任务执行记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskTestCases</td>
                    <td>查询用例关联的测试任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="43">自定义测试服务用例管理</td>
                    <td>ListAllBranches</td>
                    <td>获取分支列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTestCaseComment</td>
                    <td>修改用例评论</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestCaseDetail</td>
                    <td>获取测试用例详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTestCase</td>
                    <td>批量删除自定义测试服务类型用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectTestCaseFields</td>
                    <td>获取项目测试用例自定义字段列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserAccessInfo</td>
                    <td>获取租户订单信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFreeDeclaration</td>
                    <td>查询限时免费用户免责声明记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTestCases</td>
                    <td>查询用例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProgress</td>
                    <td>获取异步进度</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateVersionTestCases</td>
                    <td>批量更新用例属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddCaseResultFour</td>
                    <td>设置用例结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectBranch</td>
                    <td>新增分支</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackgroundInfo</td>
                    <td>获取测试报告的模板设置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourcePools</td>
                    <td>获取资源池列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTestCaseResult</td>
                    <td>批量更新测试用例结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRemoveTestCasesFromIterator</td>
                    <td>从迭代中批量移除用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTestCase</td>
                    <td>批量执行测试用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDisclaimerRecord</td>
                    <td>查询用户免责声明</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainInfo</td>
                    <td>根据domainId获取加密的testbirdkey</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResourceUri</td>
                    <td>生成资源URI</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTestCase</td>
                    <td>更新自定义测试服务类型用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsageInfos</td>
                    <td>获取租户订单已用资源信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFeatureChildren</td>
                    <td>获取目录\特性树</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVersionTestCase</td>
                    <td>在分支或者测试计划下修改用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTestTypes</td>
                    <td>获取测试类型列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTestCases</td>
                    <td>批量删除用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestCase</td>
                    <td>查询用例详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateReport</td>
                    <td>保存单个自定义报表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTestCaseComment</td>
                    <td>新增用例评论</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddResourcesForIterator</td>
                    <td>向迭代中添加资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestCaseReviews</td>
                    <td>根据用例查询评审记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTestCaseHistories</td>
                    <td>查询用例修改历史记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestCaseDetailV2</td>
                    <td>通过用例编号获取测试用例详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTestCaseResultLog</td>
                    <td>初始化用例执行记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllTestCases</td>
                    <td>查询用例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTestCase</td>
                    <td>创建自定义测试服务类型用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestCasesChangeStatistics</td>
                    <td>版本测试用例变更统计(只统计分支,不统计基线)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOwnTestCases</td>
                    <td>获取责任人是自己的测试用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCaseResult</td>
                    <td>查询用例结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVersionTestCase</td>
                    <td>在分支或者测试计划下创建用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTestCaseComments</td>
                    <td>查询用例评论</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectFieldConfigs</td>
                    <td>查询项目字段配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTestCaseComment</td>
                    <td>删除用例评论</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
