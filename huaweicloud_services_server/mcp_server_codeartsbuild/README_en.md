# CodeArtsBuild MCP Server 


## Version
v0.1.0

## Overview

CodeArtsBuild MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeArtsBuild. Full-chain management of CodeArtsBuild resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Background Task Management | ShowJobInfo | Query the job execution result of a tenant. | To be tested |
| CodeArtsBuild | ListOfficialTemplate | Query the official template | To be tested |
|  | ShowJobListByProjectId | View the build task list of users in a project. | To be tested |
|  | DownloadBuildLog | Download full build logs | To be tested |
|  | ShowKeystorePermission | File management query permission | To be tested |
|  | ShowBuildRecord | Query the details of a specified build record | To be tested |
|  | CreateBuildJob | Create build task  | To be tested |
|  | ShowJobConfig | Obtain build task details | To be tested |
|  | ShowBuildParamsList | Interface for obtaining the parameter type on the editing page | To be tested |
|  | EnableBuildJob | Recovery build task  | To be tested |
|  | ShowListHistory | View the build task construction history list | To be tested |
|  | StopBuildJob | Stopping the build task  | To be tested |
|  | ListProjectJobs | Query the project task list | To be tested |
|  | ShowJobConfigDiff | Obtain the difference in the build task configuration. | To be tested |
|  | UpdateBuildJob | Update build task  | To be tested |
|  | ShowDefaultBuildParameters | Obtain the default compilation and build parameters. | To be tested |
|  | ListNotice | Query notification | To be tested |
|  | CreateTemplates | Create a build template | To be tested |
|  | ShowImageTemplateList | Obtain the image template list | To be tested |
|  | ShowListPeriodHistory | View the build task construction history list based on the start time and end time. | To be tested |
|  | ListRecyclingJob | View the list of build task deleted from the recycle bin | To be tested |
|  | ListJobConfig | Obtain build task details | To be tested |
|  | ListRelatedProjectInfo | Obtain the project list | To be tested |
|  | DownloadTaskLog | Download the build step log | To be tested |
|  | ShowDockerfileTemplate | Obtain dockerfileTemplate | To be tested |
|  | ListBuildInfoRecordByJobId | Obtain the task construction record list v1 | To be tested |
|  | ShowProjectPermission | Obtain user permission | To be tested |
|  | ListBuildInfoRecord | Obtain the task construction record list | To be tested |
|  | ShowJobBuildSuccessRatio | Query the build success rate. | To be tested |
|  | DownloadRealTimeLog | Downloading real-time build logs | To be tested |
|  | ShowJobSystemParameters | View the predefined parameters of the system | To be tested |
|  | CheckJobNameIsExists | Check whether the task name exists in the project. | To be tested |
|  | DownloadKeystoreByName | File Management File Download | To be tested |
|  | ShowBuildRecordBuildScript | Obtains the build script of the build record | To be tested |
|  | DisableBuildJob | Disable build task  | To be tested |
|  | ShowRunningStatus | Check whether the task is being built | To be tested |
|  | ShowJobSuccessRatio | Query the build task build success rate based on the start time and end time. | To be tested |
|  | ShowLastHistory | Query the latest successful build history of a specified code repository. | To be tested |
|  | RunJob | Executing build task. User-defined parameters can be transferred. | To be tested |
|  | ShowRecordDetail | Obtain the build record information | To be tested |
|  | DeleteTemplates | Delete a build template | To be tested |
|  | ShowJobBuildTime | Insight construction duration | To be tested |
|  | DeleteBuildJob | Delete build task  | To be tested |
|  | ListRecords | Obtain the construction record list of a specified project | To be tested |
|  | ShowReportSummary | API for obtaining the coverage rate | To be tested |
|  | ListKeystore | Query files available to a user | To be tested |
|  | ShowBuildRecordFullStages | Obtain the task phase information | To be tested |
|  | ShowRelatedProject | Obtain the project information list of the current user. | To be tested |
|  | ShowOutputInfo | Obtain the details about the build product | To be tested |
|  | ShowYamlTemplate | Obtain the default template for code-based construction | To be tested |
|  | DisableNotice | Cancel notification | To be tested |
|  | ShowHistoryDetails | Interface for obtaining historical build details | To be tested |
|  | ShowJobNoticeConfigInfo | Obtain notification information | To be tested |
|  | DownloadKeystore | Download the KeyStore file of a specified tenant | To be tested |
|  | ShowBuildInfoRecord | Obtain the task construction record list | To be tested |
|  | ShowJobRolePermission | Obtain the role permission matrix information of the build task  | To be tested |
|  | UpdateNotice | Update notification | To be tested |
| Job management | ShowJobStatus | Query the execution status of a job. | To be tested |
| Job management interface | StopJob | This API is used to terminate a specified job in the MRS cluster. | To be tested |
| Offline | ShowRecordInfo | Obtain the build record information (to be brought offline) | To be tested |
|  | DownloadLogByRecordId | Downloading the build log (to be brought offline) | To be tested |
|  | ShowFlowGraph | Obtain the directed acyclic graph of the construction record (to be brought offline) | To be tested |
| Project Information | ListTemplates | Query project template | To be tested |

