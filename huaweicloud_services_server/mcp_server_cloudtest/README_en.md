# CloudTest MCP Server 


## Version
v0.1.0

## Overview

CloudTest MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CloudTest. Full-chain management of CloudTest resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| ApigAutoInitController | CreateApiTestSuiteByRepoFile | Generate an interface test suite by importing files in the warehouse | To be tested |
| Attachments | ListAttachments | Query the connection list of an enterprise router instance. | To be tested |
| Case Association Management | ListTestcasesByProjectIssuesRelation | Query the list of test cases associated with requirements under a project | To be tested |
| Customized test service access management | ShowRegisterService | A user obtains the registered service. | To be tested |
|  | ShowAllFeatureChildren | Obtain the directory\Feature tree | To be tested |
| Customized test service case management | ListAllBranches | Obtain the branch list | To be tested |
|  | UpdateTestCaseComment | Modifying a test case review | To be tested |
|  | ShowTestCaseDetail | Obtain test case details | To be tested |
|  | BatchDeleteTestCase | Delete test cases of customized service types in batches | To be tested |
|  | ListProjectTestCaseFields | Obtain the list of customized fields for project test cases | To be tested |
|  | ShowUserAccessInfo | Obtain the order information of the tenant. | To be tested |
|  | ShowFreeDeclaration | Query the disclaimer record of a time-limited free user | To be tested |
|  | ListTestCases | Query the test case list | To be tested |
|  | ShowProgress | Obtain the asynchronous progress. | To be tested |
|  | BatchUpdateVersionTestCases | Updating test case attributes in batches | To be tested |
|  | AddCaseResultFour | Setting the test case result | To be tested |
|  | CreateProjectBranch | Add a branch | To be tested |
|  | ShowBackgroundInfo | Setting the template for obtaining the test report | To be tested |
|  | ListResourcePools | Obtain the resource pool list | To be tested |
|  | UpdateTestCaseResult | Updating test case results in batches | To be tested |
|  | BatchRemoveTestCasesFromIterator | Remove cases in batches from the iteration | To be tested |
|  | RunTestCase | Executing test cases in batches | To be tested |
|  | ShowDisclaimerRecord | Query the user disclaimer | To be tested |
|  | ShowDomainInfo | Obtain the encrypted testbirdkey based on domainId. | To be tested |
|  | CreateResourceUri | Generate resource URI | To be tested |
|  | UpdateTestCase | Updating the case of the user-defined test service type | To be tested |
|  | ListUsageInfos | Obtain the resource information used by the tenant order. | To be tested |
|  | ShowFeatureChildren | Obtain the directory\Feature tree | To be tested |
|  | UpdateVersionTestCase | Modifying a test case in a branch or test plan | To be tested |
|  | ListTestTypes | Obtain the test type list | To be tested |
|  | BatchDeleteTestCases | Delete test cases in batches | To be tested |
|  | ShowTestCase | Query case details | To be tested |
|  | CreateReport | Save a single customized report | To be tested |
|  | AddTestCaseComment | Add a test case review | To be tested |
|  | BatchAddResourcesForIterator | Adding resources to the iteration | To be tested |
|  | ShowTestCaseReviews | Query review records by case | To be tested |
|  | ListTestCaseHistories | Query the historical modification records of test cases. | To be tested |
|  | ShowTestCaseDetailV2 | Obtain the test case details based on the test case ID. | To be tested |
|  | AddTestCaseResultLog | Initializing the execution record of the test case | To be tested |
|  | ListAllTestCases | Query the test case list | To be tested |
|  | CreateTestCase | Creating a test case of the customized service type | To be tested |
|  | ShowTestCasesChangeStatistics | Version test case change statistics (only branches are counted) | To be tested |
|  | ListOwnTestCases | Obtain the test cases of the owner | To be tested |
|  | ShowCaseResult | Query the test case result | To be tested |
|  | CreateVersionTestCase | Create a test case under a branch or test plan | To be tested |
|  | ListTestCaseComments | Query test case comments | To be tested |
|  | ListProjectFieldConfigs | Query project field configuration | To be tested |
|  | DeleteTestCaseComment | Delete a test case review | To be tested |
| Customized test service test suite management | ListTaskAssignCases | Obtain the details about the test suite associated with the test suite | To be tested |
|  | CreateTaskDefaultResult | Initializing the execution records of the test task | To be tested |
|  | ListTaskTestCases | Query the list of test tasks associated with a case | To be tested |
| Dialing Test Task Configuration Management | SaveTaskSetting | Save the task configuration | To be tested |
|  | ShowAllConfigValueByTypeAndKey | Query task configuration | To be tested |
| Dialing test alarm information management | ShowIfTaskNameRepeat | Query whether the alarm template name is duplicate. | To be tested |
|  | ListAlertGroupsByCondition | Query the alarm group list | To be tested |
|  | ListAlertTemplates | Query alarm templates | To be tested |
|  | ListAllConfigItemByType | Query the alarm information of a task | To be tested |
|  | ShowIfUserNameRepeat | Check whether the user name of the alarm group is duplicate. | To be tested |
| Dialog Dashboard Info Management | ListUsingGet | Query the dashboard of a dashboard user | To be tested |
|  | ListMsgInfosUsing | The detailed information list of the MsgInfo is returned successfully. The return value is List of Model. | To be tested |
|  | ListScattersUsing | Query the scatter chart data of the dashboard | To be tested |
|  | ListAlarmStatisticsUsing | Query alarm statistics | To be tested |
|  | ShowOperationalDataCurrentMonthUsing | The running panel information is returned successfully. | To be tested |
|  | ListLinesUsing | Query line chart data on a dashboard | To be tested |
|  | ListSubTaskCaseOverstockUsing | The subtask case data stacking information is returned successfully. | To be tested |
| Global variable management | ListVariables | Query global variables | To be tested |
| ITaskController | ListTasks | Obtain the task list | To be tested |
| Interface Test Management | ListPublicLibAndAws | Obtain the public AW information associated with the project and the public AW library to which the public AW belongs | To be tested |
|  | ListBasicAwInfoListSupportsSearch | Obtain the BasicAW list (including directories) of a project by page | To be tested |
|  | UpdateTestCaseAndScript | Update TMSS test cases and test case scripts | To be tested |
|  | ShowApiTestcaseHistories | Obtain historical case execution data | To be tested |
|  | UpdateBasicAwById | Interface for modifying keyword information | To be tested |
|  | UpdateUserDnsMapping | Update the user DNS mapping, which is customized by the executor | To be tested |
|  | ListTestCaseScriptDetail | Obtain the details about the test case script | To be tested |
|  | CreateUserDefinedUrlKeyWord | Adding a user-defined URL keyword | To be tested |
|  | ListUserDnsMapping | Query the DNS mapping of a user | To be tested |
|  | ListCasesStatus | Obtain case status in batches | To be tested |
|  | ListBasicAw | Obtains a single basicAW by ID | To be tested |
|  | ListAvailableConfig | Obtain whether the function is enabled at the current site. | To be tested |
|  | DeleteBasicAwById | Deleting a single basicAw in the convergent version | To be tested |
| Interface test package usage management | ListUserPackageUsage |  | To be tested |
|  | ListUserPopupInfo |  | To be tested |
| Query dialing test package status | ShowEchoTestPackageUsing | Query the online dialing test package status of a tenant | To be tested |
|  | ShowConcurrencyPackageUsing | Query the status of concurrent test packages of a tenant | To be tested |
| Query test task execution history by task URI | ListTaskResults | Query the execution history of a test task based on the task URI. | To be tested |
| Query the detailed result of a single test suite execution | ListTaskResultsDetail | Query the detailed execution result of a single test suite. | To be tested |
| Report Management | ShowReport | Query report | To be tested |
| Service Management | CreateService | Create a service | To be tested |
|  | DeleteService | Delete a service | To be tested |
|  | UpdateService | Modifying a service | To be tested |
| Test Design Query | ShowStatisticById | Query the number of statistics based on the brain map ID. | To be tested |
|  | CheckPermission | Check the project permission. | To be tested |
|  | ShowTemplateByPage | Obtain the template V3 by pagination based on conditions | To be tested |
|  | ShowMindmapCreatorName | Obtain the brain map creator V2 | To be tested |
|  | DeleteFacotrById | Deleting a factor | To be tested |
|  | ShowMindmapByPage | Obtain the brain map object V3 by pagination based on conditions. | To be tested |
|  | ShowSceneByPage | Obtain the scenario object V2 by pagination based on conditions | To be tested |
|  | ShowTestcaseByPage | Obtain the test case object by pagination based on conditions V2 | To be tested |
|  | ShowReviewByPage | Obtain review objects by pagination based on conditions V2 | To be tested |
|  | ShowAsset | Obtain the asset list | To be tested |
|  | ShowSystemConfigs | Dynamic query for system configuration information based on input parameters | To be tested |
|  | ShowAssetTree | Obtain the asset tree list | To be tested |
|  | ShowMindMapById | Obtain the brain map object based on the ID. | To be tested |
|  | ShowFactorByAssetId | Query factors by category | To be tested |
|  | ShowTemplateById | Obtain template V2 | To be tested |
|  | ShowFactorById | Obtain the factor based on the ID. | To be tested |
|  | ShowTestpointByPage | Obtain the test point object V2 by pagination based on conditions | To be tested |
| Test Report Management | ListTestReportsByCondition | Obtain the test report list based on the query conditions. | To be tested |
|  | BatchDeleteTestReport | Delete a test report based on the test report URI list. | To be tested |
|  | ShowRequirementsOverview | Quality report requirement test statistics | To be tested |
|  | ShowTestCaseAndDefectInfo | Query the statistics about defects associated with user test cases | To be tested |
|  | ShowUserExecuteTestCaseInfo | Query the execution status of test cases in the specified period. | To be tested |
|  | ShowProjectDataDashboard | Query quality report dashboard statistics | To be tested |
|  | ListReports | Report display on the page | To be tested |
| Test plan management | ListIssueTree | Query the requirement tree | To be tested |
|  | ShowPlanList | Querying the test plan list under a project v2 | To be tested |
|  | RemoveIssuesFromIterator | Remove a requirement from the iteration | To be tested |
|  | CreateIterator | Add iteration | To be tested |
|  | ShowIteratorDetail | Query iteration plan details, including statistics. | To be tested |
|  | ListIterators | Query the iteration plan list, including statistics. | To be tested |
|  | ListAllIterators | Query all iteration plans under a project | To be tested |
|  | ListIteratorIssueTree | Query the requirement list or tree associated with the iteration | To be tested |
|  | ShowPlans | Query the test plan list under a project | To be tested |
|  | ShowIssuesByPlanId | Query the requirement list under a test plan | To be tested |
|  | ShowBranch | Obtain branch details | To be tested |
|  | ShowIteratorByDefect | Query the test plan associated with a defect | To be tested |
|  | ShowPlanJournals | Query the operation history of a test plan | To be tested |
|  | UpdateIterator | Modifying a test plan | To be tested |
|  | CreatePlan | Create a plan under a project | To be tested |
|  | CreateTestCaseInPlan | Add test cases in batches in the plan | To be tested |
|  | ListDomainVisibleServices | Query the list of third-party services visible to the current tenant | To be tested |
|  | ListBranches | Obtain the branch list | To be tested |
| Test service association | BatchAddRelationsByOneCase | Adding the relationship between the requirement/defect and multiple test cases | To be tested |
|  | ListTestCasesByIssue | Query the test case list under the requirement | To be tested |
|  | DeleteRelationsByOneCase | Delete the association between a test case and multiple requirements/defects. | To be tested |
|  | CreateRelationsByOneCase | Add a test case and multiple requirements/defect relationships | To be tested |
| TestcaseManagement | ListTestcasePlans | Query the test plan corresponding to the test case based on the test case URI or case ID | To be tested |
| attachment-controller | UploadStepImg | External API | To be tested |
| environment-controller-v2 | ListEnvironments | Query the environment list of an application. | To be tested |
| test-item-controller | AddFeature | Adding catalog information | To be tested |

