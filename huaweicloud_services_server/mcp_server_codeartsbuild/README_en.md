# CodeArtsBuild MCP Server 


## Version
v0.1.0

## Overview

CodeArtsBuild MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeArtsBuild. Full-chain management of CodeArtsBuild resources can be carried out based on natural language.

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
                    <td rowspan="1">Background Task Management</td>
                    <td>ShowJobInfo</td>
                    <td>Query the job execution result of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="56">CodeArtsBuild</td>
                    <td>ListOfficialTemplate</td>
                    <td>Query the official template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobListByProjectId</td>
                    <td>View the build task list of users in a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadBuildLog</td>
                    <td>Download full build logs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKeystorePermission</td>
                    <td>File management query permission</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBuildRecord</td>
                    <td>Query the details of a specified build record</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBuildJob</td>
                    <td>Create build task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobConfig</td>
                    <td>Obtain build task details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBuildParamsList</td>
                    <td>Interface for obtaining the parameter type on the editing page</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableBuildJob</td>
                    <td>Recovery build task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowListHistory</td>
                    <td>View the build task construction history list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopBuildJob</td>
                    <td>Stopping the build task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectJobs</td>
                    <td>Query the project task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobConfigDiff</td>
                    <td>Obtain the difference in the build task configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBuildJob</td>
                    <td>Update build task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDefaultBuildParameters</td>
                    <td>Obtain the default compilation and build parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotice</td>
                    <td>Query notification</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemplates</td>
                    <td>Create a build template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageTemplateList</td>
                    <td>Obtain the image template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowListPeriodHistory</td>
                    <td>View the build task construction history list based on the start time and end time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecyclingJob</td>
                    <td>View the list of build task deleted from the recycle bin</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobConfig</td>
                    <td>Obtain build task details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRelatedProjectInfo</td>
                    <td>Obtain the project list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadTaskLog</td>
                    <td>Download the build step log</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDockerfileTemplate</td>
                    <td>Obtain dockerfileTemplate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBuildInfoRecordByJobId</td>
                    <td>Obtain the task construction record list v1</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectPermission</td>
                    <td>Obtain user permission</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBuildInfoRecord</td>
                    <td>Obtain the task construction record list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobBuildSuccessRatio</td>
                    <td>Query the build success rate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadRealTimeLog</td>
                    <td>Downloading real-time build logs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobSystemParameters</td>
                    <td>View the predefined parameters of the system</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckJobNameIsExists</td>
                    <td>Check whether the task name exists in the project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadKeystoreByName</td>
                    <td>File Management File Download</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBuildRecordBuildScript</td>
                    <td>Obtains the build script of the build record</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableBuildJob</td>
                    <td>Disable build task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRunningStatus</td>
                    <td>Check whether the task is being built</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobSuccessRatio</td>
                    <td>Query the build task build success rate based on the start time and end time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLastHistory</td>
                    <td>Query the latest successful build history of a specified code repository.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunJob</td>
                    <td>Executing build task. User-defined parameters can be transferred.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordDetail</td>
                    <td>Obtain the build record information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTemplates</td>
                    <td>Delete a build template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobBuildTime</td>
                    <td>Insight construction duration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBuildJob</td>
                    <td>Delete build task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecords</td>
                    <td>Obtain the construction record list of a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReportSummary</td>
                    <td>API for obtaining the coverage rate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeystore</td>
                    <td>Query files available to a user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBuildRecordFullStages</td>
                    <td>Obtain the task phase information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRelatedProject</td>
                    <td>Obtain the project information list of the current user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOutputInfo</td>
                    <td>Obtain the details about the build product</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowYamlTemplate</td>
                    <td>Obtain the default template for code-based construction</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableNotice</td>
                    <td>Cancel notification</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHistoryDetails</td>
                    <td>Interface for obtaining historical build details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobNoticeConfigInfo</td>
                    <td>Obtain notification information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadKeystore</td>
                    <td>Download the KeyStore file of a specified tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBuildInfoRecord</td>
                    <td>Obtain the task construction record list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobRolePermission</td>
                    <td>Obtain the role permission matrix information of the build task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNotice</td>
                    <td>Update notification</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job management</td>
                    <td>ShowJobStatus</td>
                    <td>Query the execution status of a job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job management interface</td>
                    <td>StopJob</td>
                    <td>This API is used to terminate a specified job in the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Offline</td>
                    <td>ShowRecordInfo</td>
                    <td>Obtain the build record information (to be brought offline)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadLogByRecordId</td>
                    <td>Downloading the build log (to be brought offline)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlowGraph</td>
                    <td>Obtain the directed acyclic graph of the construction record (to be brought offline)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Project Information</td>
                    <td>ListTemplates</td>
                    <td>Query project template</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
