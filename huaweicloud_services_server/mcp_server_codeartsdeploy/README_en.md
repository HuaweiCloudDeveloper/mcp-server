# CodeArtsDeploy MCP Server 


## Version
v0.1.0

## Overview

CodeArtsDeploy MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeArtsDeploy. Full-chain management of CodeArtsDeploy resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AppGroupsController | MoveAppGroups | Move a single group up or down to adjust the group position on the page. | To be tested |
|  | UpdateAppGroups | Modify a group. | To be tested |
|  | MoveAppToGroup | Move applications to a specified group (batch applications are supported). | To be tested |
|  | ListAppGroups | Query the group list. | To be tested |
|  | CreateAppGroups | Create a group. | To be tested |
|  | DeleteAppGroups | Delete a group. | To be tested |
| AppManagement | CreateApp | This interface is used by users to create application information. | To be tested |
| AppPermissionsController | BatchUpdateApplicationPermissions | Modify application permissions in batches. | To be tested |
|  | ListApplicationPermissions | Query the application instance-level/project-level permission matrix. When app_id is transferred, the application instance-level permission matrix is queried. If app_id is not transferred and project_id is transferred, the application project-level permission matrix will be queried. | To be tested |
|  | BatchUpdatePermissionLevel | Configure the authentication level of applications in batches to project-level or instance-level. | To be tested |
|  | CheckCanCreate | Check whether the current user has the permission to create applications in the project. | To be tested |
| Application operation | DeleteApplication | Delete a platform application. | To be tested |
| Cluster management interface | ListHosts | This API is used to query details about the host list in the input cluster. | To be tested |
| Host management | ListHostGroups | Query the server group list | To be tested |
| Protection Website Management in Cloud Mode | DeleteHost | Delete the domain name in cloud mode. | To be tested |
|  | CreateHost | Creating a domain name in cloud mode | To be tested |
| RecordMetricController | ShowProjectSuccessRate | Obtain the application deployment success rate of a specified project. | To be tested |
|  | ListTaskSuccessRate | Obtain the application deployment success rate of a specified application. | To be tested |
| deploy-env-controller-v2 | ShowExecutionParams | Query the execution parameters of a deployment record. | To be tested |
|  | DeleteDeployTask | Delete an application based on the deployment task ID. This interface will no longer be maintained after September 30, 2024. You are advised to use the new DeleteApplication interface. | To be tested |
|  | BatchDeleteApp | Delete applications in a project in batches. | To be tested |
|  | CheckIsDuplicateAppName | Query whether an application with the same name exists in the project. | To be tested |
|  | StartDeployTask | Deploy the application based on the deployment task ID. | To be tested |
|  | CreateDeployTaskByTemplate | Create an application using a template. This interface will not be maintained after September 30, 2024. You are advised to use the new CreateApp interface. | To be tested |
|  | UpdateAppInfo | Update the application. | To be tested |
|  | ListDeployTasks | Query the application list under a project. This interface will no longer be maintained after September 30, 2024. You are advised to use the new ListAllApp interface. | To be tested |
|  | ListAllApp | Query the application list under a project. | To be tested |
|  | CopyApplication | Copy the application. | To be tested |
|  | ShowAppDetailById | This API is used to obtain application details based on the application ID. | To be tested |
|  | UpdateAppDisableStatus | Disable or undisable an application. | To be tested |
|  | ShowDeployTaskDetail | Obtain application details based on the deployment task ID. This interface will not be maintained after September 30, 2024. You are advised to use the ShowAppDetailById interface of the new version. | To be tested |
|  | ListDeployTaskHistoryByDate | Query the historical deployment records of a specified application in a project based on the start time and end time. | To be tested |
| environment-controller-v2 | UpdateEnvironment | Editing environment in the application. | To be tested |
|  | ListEnvironments | Query the environment list of an application. | To be tested |
|  | CreateEnvironment | Create an environment under the application. | To be tested |
|  | ImportHostToEnvironment | Import the host in the environment. | To be tested |
|  | ShowEnvironmentDetail | Query environment details. | To be tested |
|  | DeleteEnvironment | Delete the environment of the application. | To be tested |
|  | ListEnvironmentHosts | Query the host list in the environment. | To be tested |
|  | DeleteHostFromEnvironment | Delete a host in the environment. | To be tested |
| environment-permission-controller-v2 | ListEnvironmentPermissions | Query the environment permission. | To be tested |
|  | UpdateEnvironmentPermission | Edit the environment permission. | To be tested |
| hosts-controller-v2 | ListNewHosts | Query the host list in a specified host cluster based on the host cluster ID. | To be tested |
|  | UpdateDeploymentHost | Modify host information based on the host ID. This interface will no longer be maintained after September 30, 2024. | To be tested |
|  | BatchDeleteHosts | Delete hosts in a host cluster in batches. | To be tested |
|  | ShowDeploymentHostDetail | Query host details based on the host ID. This interface will no longer be maintained after September 30, 2024. You are advised to use the ShowHostDetail interface of the new version. | To be tested |
|  | ShowHostDetail | Query host details based on the host ID. | To be tested |
|  | DeleteDeploymentHost | Delete a host based on the host ID. This interface will no longer be maintained after September 30, 2024. | To be tested |
|  | UpdateHostInfo | Edit host information in the host cluster based on the host ID. | To be tested |
|  | CreateDeploymentHost | This API is used to create a host in a specified host cluster. This interface will no longer be maintained after September 30, 2024. You are advised to use the new CreateHost interface. | To be tested |
|  | CopyHostsToTarget | Replicate hosts to the target host cluster in batches. | To be tested |
| hosts-group-controller-v2 | ListHostGroupBaseInfos | Query the basic environment information list of the application. | To be tested |
|  | ListAssociateEnvironmentsInfos | Query the environment information associated with a host cluster. | To be tested |
|  | ShowHostClusterDetail | Query details about a host cluster based on the host cluster ID. | To be tested |
|  | DeleteHostCluster | Delete a host cluster based on the host cluster ID. | To be tested |
|  | ShowDeploymentGroupDetail | Query details about a host cluster based on the host cluster ID. This interface will not be maintained after September 30, 2024. You are advised to use the new ShowHostClusterDetail interface. | To be tested |
|  | ListHostClusters | Query the host cluster list by criteria. | To be tested |
|  | DeleteDeploymentGroup | Delete a host cluster based on the host cluster ID. This interface will no longer be maintained after September 30, 2024. | To be tested |
|  | UpdateDeploymentGroup | Modify the host cluster information based on the host cluster ID. This interface will no longer be maintained after September 30, 2024. | To be tested |
|  | UpdateHostCluster | Edit the host cluster. | To be tested |
|  | CreateHostCluster | Create a host cluster in the project. | To be tested |
|  | CreateDeploymentGroup | Create a host cluster in the project. This interface will no longer be maintained after September 30, 2024. You are advised to use the new CreateHostCluster interface. | To be tested |
| hosts-group-permission-controller-v2 | ListHostGroupPermissions | Query the host cluster permission matrix based on the host cluster ID. | To be tested |
|  | UpdateHostGroupPermissions | Modify the host cluster permission matrix based on the host cluster ID. | To be tested |
|  | CheckWhetherHostGroupCanBeCreated | Check whether the current user has the permission to create a host cluster in the project. | To be tested |

