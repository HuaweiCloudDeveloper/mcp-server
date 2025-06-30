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
                    <td>Generate an interface test suite by importing files in the warehouse</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Attachments</td>
                    <td>ListAttachments</td>
                    <td>Query the connection list of an enterprise router instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Case Association Management</td>
                    <td>ListTestcasesByProjectIssuesRelation</td>
                    <td>Query the list of test cases associated with requirements under a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Customized test service access management</td>
                    <td>ShowRegisterService</td>
                    <td>A user obtains the registered service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAllFeatureChildren</td>
                    <td>Obtain the directory\Feature tree</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="43">Customized test service case management</td>
                    <td>ListAllBranches</td>
                    <td>Obtain the branch list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTestCaseComment</td>
                    <td>Modifying a test case review</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestCaseDetail</td>
                    <td>Obtain test case details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTestCase</td>
                    <td>Delete test cases of customized service types in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectTestCaseFields</td>
                    <td>Obtain the list of customized fields for project test cases</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserAccessInfo</td>
                    <td>Obtain the order information of the tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFreeDeclaration</td>
                    <td>Query the disclaimer record of a time-limited free user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTestCases</td>
                    <td>Query the test case list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProgress</td>
                    <td>Obtain the asynchronous progress.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateVersionTestCases</td>
                    <td>Updating test case attributes in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddCaseResultFour</td>
                    <td>Setting the test case result</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectBranch</td>
                    <td>Add a branch</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackgroundInfo</td>
                    <td>Setting the template for obtaining the test report</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourcePools</td>
                    <td>Obtain the resource pool list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTestCaseResult</td>
                    <td>Updating test case results in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRemoveTestCasesFromIterator</td>
                    <td>Remove cases in batches from the iteration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTestCase</td>
                    <td>Executing test cases in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDisclaimerRecord</td>
                    <td>Query the user disclaimer</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainInfo</td>
                    <td>Obtain the encrypted testbirdkey based on domainId.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResourceUri</td>
                    <td>Generate resource URI</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTestCase</td>
                    <td>Updating the case of the user-defined test service type</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsageInfos</td>
                    <td>Obtain the resource information used by the tenant order.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFeatureChildren</td>
                    <td>Obtain the directory\Feature tree</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVersionTestCase</td>
                    <td>Modifying a test case in a branch or test plan</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTestTypes</td>
                    <td>Obtain the test type list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTestCases</td>
                    <td>Delete test cases in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestCase</td>
                    <td>Query case details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateReport</td>
                    <td>Save a single customized report</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTestCaseComment</td>
                    <td>Add a test case review</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddResourcesForIterator</td>
                    <td>Adding resources to the iteration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestCaseReviews</td>
                    <td>Query review records by case</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTestCaseHistories</td>
                    <td>Query the historical modification records of test cases.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestCaseDetailV2</td>
                    <td>Obtain the test case details based on the test case ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTestCaseResultLog</td>
                    <td>Initializing the execution record of the test case</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllTestCases</td>
                    <td>Query the test case list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTestCase</td>
                    <td>Creating a test case of the customized service type</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestCasesChangeStatistics</td>
                    <td>Version test case change statistics (only branches are counted)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOwnTestCases</td>
                    <td>Obtain the test cases of the owner</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCaseResult</td>
                    <td>Query the test case result</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVersionTestCase</td>
                    <td>Create a test case under a branch or test plan</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTestCaseComments</td>
                    <td>Query test case comments</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectFieldConfigs</td>
                    <td>Query project field configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTestCaseComment</td>
                    <td>Delete a test case review</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Customized test service test suite management</td>
                    <td>ListTaskAssignCases</td>
                    <td>Obtain the details about the test suite associated with the test suite</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTaskDefaultResult</td>
                    <td>Initializing the execution records of the test task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskTestCases</td>
                    <td>Query the list of test tasks associated with a case</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Dialing Test Task Configuration Management</td>
                    <td>SaveTaskSetting</td>
                    <td>Save the task configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAllConfigValueByTypeAndKey</td>
                    <td>Query task configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Dialing test alarm information management</td>
                    <td>ShowIfTaskNameRepeat</td>
                    <td>Query whether the alarm template name is duplicate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlertGroupsByCondition</td>
                    <td>Query the alarm group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlertTemplates</td>
                    <td>Query alarm templates</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllConfigItemByType</td>
                    <td>Query the alarm information of a task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIfUserNameRepeat</td>
                    <td>Check whether the user name of the alarm group is duplicate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Dialog Dashboard Info Management</td>
                    <td>ListUsingGet</td>
                    <td>Query the dashboard of a dashboard user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMsgInfosUsing</td>
                    <td>The detailed information list of the MsgInfo is returned successfully. The return value is List of Model.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScattersUsing</td>
                    <td>Query the scatter chart data of the dashboard</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmStatisticsUsing</td>
                    <td>Query alarm statistics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOperationalDataCurrentMonthUsing</td>
                    <td>The running panel information is returned successfully.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLinesUsing</td>
                    <td>Query line chart data on a dashboard</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubTaskCaseOverstockUsing</td>
                    <td>The subtask case data stacking information is returned successfully.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Global variable management</td>
                    <td>ListVariables</td>
                    <td>Query global variables</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ITaskController</td>
                    <td>ListTasks</td>
                    <td>Obtain the task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">Interface Test Management</td>
                    <td>ListPublicLibAndAws</td>
                    <td>Obtain the public AW information associated with the project and the public AW library to which the public AW belongs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBasicAwInfoListSupportsSearch</td>
                    <td>Obtain the BasicAW list (including directories) of a project by page</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTestCaseAndScript</td>
                    <td>Update TMSS test cases and test case scripts</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApiTestcaseHistories</td>
                    <td>Obtain historical case execution data</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBasicAwById</td>
                    <td>Interface for modifying keyword information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserDnsMapping</td>
                    <td>Update the user DNS mapping, which is customized by the executor</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTestCaseScriptDetail</td>
                    <td>Obtain the details about the test case script</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUserDefinedUrlKeyWord</td>
                    <td>Adding a user-defined URL keyword</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserDnsMapping</td>
                    <td>Query the DNS mapping of a user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCasesStatus</td>
                    <td>Obtain case status in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBasicAw</td>
                    <td>Obtains a single basicAW by ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableConfig</td>
                    <td>Obtain whether the function is enabled at the current site.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBasicAwById</td>
                    <td>Deleting a single basicAw in the convergent version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Interface test package usage management</td>
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
                    <td rowspan="2">Query dialing test package status</td>
                    <td>ShowEchoTestPackageUsing</td>
                    <td>Query the online dialing test package status of a tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConcurrencyPackageUsing</td>
                    <td>Query the status of concurrent test packages of a tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query test task execution history by task URI</td>
                    <td>ListTaskResults</td>
                    <td>Query the execution history of a test task based on the task URI.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query the detailed result of a single test suite execution</td>
                    <td>ListTaskResultsDetail</td>
                    <td>Query the detailed execution result of a single test suite.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Report Management</td>
                    <td>ShowReport</td>
                    <td>Query report</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Service Management</td>
                    <td>CreateService</td>
                    <td>Create a service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteService</td>
                    <td>Delete a service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateService</td>
                    <td>Modifying a service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">Test Design Query</td>
                    <td>ShowStatisticById</td>
                    <td>Query the number of statistics based on the brain map ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckPermission</td>
                    <td>Check the project permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTemplateByPage</td>
                    <td>Obtain the template V3 by pagination based on conditions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMindmapCreatorName</td>
                    <td>Obtain the brain map creator V2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFacotrById</td>
                    <td>Deleting a factor</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMindmapByPage</td>
                    <td>Obtain the brain map object V3 by pagination based on conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSceneByPage</td>
                    <td>Obtain the scenario object V2 by pagination based on conditions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestcaseByPage</td>
                    <td>Obtain the test case object by pagination based on conditions V2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReviewByPage</td>
                    <td>Obtain review objects by pagination based on conditions V2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAsset</td>
                    <td>Obtain the asset list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSystemConfigs</td>
                    <td>Dynamic query for system configuration information based on input parameters</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAssetTree</td>
                    <td>Obtain the asset tree list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMindMapById</td>
                    <td>Obtain the brain map object based on the ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFactorByAssetId</td>
                    <td>Query factors by category</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTemplateById</td>
                    <td>Obtain template V2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFactorById</td>
                    <td>Obtain the factor based on the ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestpointByPage</td>
                    <td>Obtain the test point object V2 by pagination based on conditions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Test Report Management</td>
                    <td>ListTestReportsByCondition</td>
                    <td>Obtain the test report list based on the query conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTestReport</td>
                    <td>Delete a test report based on the test report URI list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRequirementsOverview</td>
                    <td>Quality report requirement test statistics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTestCaseAndDefectInfo</td>
                    <td>Query the statistics about defects associated with user test cases</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserExecuteTestCaseInfo</td>
                    <td>Query the execution status of test cases in the specified period.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectDataDashboard</td>
                    <td>Query quality report dashboard statistics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReports</td>
                    <td>Report display on the page</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="18">Test plan management</td>
                    <td>ListIssueTree</td>
                    <td>Query the requirement tree</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlanList</td>
                    <td>Querying the test plan list under a project v2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveIssuesFromIterator</td>
                    <td>Remove a requirement from the iteration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIterator</td>
                    <td>Add iteration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIteratorDetail</td>
                    <td>Query iteration plan details, including statistics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIterators</td>
                    <td>Query the iteration plan list, including statistics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllIterators</td>
                    <td>Query all iteration plans under a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIteratorIssueTree</td>
                    <td>Query the requirement list or tree associated with the iteration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlans</td>
                    <td>Query the test plan list under a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIssuesByPlanId</td>
                    <td>Query the requirement list under a test plan</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBranch</td>
                    <td>Obtain branch details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIteratorByDefect</td>
                    <td>Query the test plan associated with a defect</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlanJournals</td>
                    <td>Query the operation history of a test plan</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIterator</td>
                    <td>Modifying a test plan</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlan</td>
                    <td>Create a plan under a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTestCaseInPlan</td>
                    <td>Add test cases in batches in the plan</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainVisibleServices</td>
                    <td>Query the list of third-party services visible to the current tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBranches</td>
                    <td>Obtain the branch list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Test service association</td>
                    <td>BatchAddRelationsByOneCase</td>
                    <td>Adding the relationship between the requirement/defect and multiple test cases</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTestCasesByIssue</td>
                    <td>Query the test case list under the requirement</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRelationsByOneCase</td>
                    <td>Delete the association between a test case and multiple requirements/defects.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRelationsByOneCase</td>
                    <td>Add a test case and multiple requirements/defect relationships</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TestcaseManagement</td>
                    <td>ListTestcasePlans</td>
                    <td>Query the test plan corresponding to the test case based on the test case URI or case ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">attachment-controller</td>
                    <td>UploadStepImg</td>
                    <td>External API</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">environment-controller-v2</td>
                    <td>ListEnvironments</td>
                    <td>Query the environment list of an application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">test-item-controller</td>
                    <td>AddFeature</td>
                    <td>Adding catalog information</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
