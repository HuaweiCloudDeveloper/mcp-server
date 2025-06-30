# CodeArtsDeploy MCP Server 


## Version
v0.1.0

## Overview

CodeArtsDeploy MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeArtsDeploy. Full-chain management of CodeArtsDeploy resources can be carried out based on natural language.

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
                    <td rowspan="6">AppGroupsController</td>
                    <td>MoveAppGroups</td>
                    <td>Move a single group up or down to adjust the group position on the page.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppGroups</td>
                    <td>Modify a group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MoveAppToGroup</td>
                    <td>Move applications to a specified group (batch applications are supported).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppGroups</td>
                    <td>Query the group list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppGroups</td>
                    <td>Create a group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppGroups</td>
                    <td>Delete a group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">AppManagement</td>
                    <td>CreateApp</td>
                    <td>This interface is used by users to create application information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">AppPermissionsController</td>
                    <td>BatchUpdateApplicationPermissions</td>
                    <td>Modify application permissions in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplicationPermissions</td>
                    <td>Query the application instance-level/project-level permission matrix. When app_id is transferred, the application instance-level permission matrix is queried. If app_id is not transferred and project_id is transferred, the application project-level permission matrix will be queried.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdatePermissionLevel</td>
                    <td>Configure the authentication level of applications in batches to project-level or instance-level.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckCanCreate</td>
                    <td>Check whether the current user has the permission to create applications in the project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Application operation</td>
                    <td>DeleteApplication</td>
                    <td>Delete a platform application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Cluster management interface</td>
                    <td>ListHosts</td>
                    <td>This API is used to query details about the host list in the input cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Host management</td>
                    <td>ListHostGroups</td>
                    <td>Query the server group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Protection Website Management in Cloud Mode</td>
                    <td>DeleteHost</td>
                    <td>Delete the domain name in cloud mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHost</td>
                    <td>Creating a domain name in cloud mode</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">RecordMetricController</td>
                    <td>ShowProjectSuccessRate</td>
                    <td>Obtain the application deployment success rate of a specified project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskSuccessRate</td>
                    <td>Obtain the application deployment success rate of a specified application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">deploy-env-controller-v2</td>
                    <td>ShowExecutionParams</td>
                    <td>Query the execution parameters of a deployment record.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeployTask</td>
                    <td>Delete an application based on the deployment task ID. This interface will no longer be maintained after September 30, 2024. You are advised to use the new DeleteApplication interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteApp</td>
                    <td>Delete applications in a project in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckIsDuplicateAppName</td>
                    <td>Query whether an application with the same name exists in the project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartDeployTask</td>
                    <td>Deploy the application based on the deployment task ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeployTaskByTemplate</td>
                    <td>Create an application using a template. This interface will not be maintained after September 30, 2024. You are advised to use the new CreateApp interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppInfo</td>
                    <td>Update the application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDeployTasks</td>
                    <td>Query the application list under a project. This interface will no longer be maintained after September 30, 2024. You are advised to use the new ListAllApp interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllApp</td>
                    <td>Query the application list under a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyApplication</td>
                    <td>Copy the application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppDetailById</td>
                    <td>This API is used to obtain application details based on the application ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppDisableStatus</td>
                    <td>Disable or undisable an application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeployTaskDetail</td>
                    <td>Obtain application details based on the deployment task ID. This interface will not be maintained after September 30, 2024. You are advised to use the ShowAppDetailById interface of the new version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDeployTaskHistoryByDate</td>
                    <td>Query the historical deployment records of a specified application in a project based on the start time and end time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">environment-controller-v2</td>
                    <td>UpdateEnvironment</td>
                    <td>Editing environment in the application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvironments</td>
                    <td>Query the environment list of an application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnvironment</td>
                    <td>Create an environment under the application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportHostToEnvironment</td>
                    <td>Import the host in the environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnvironmentDetail</td>
                    <td>Query environment details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnvironment</td>
                    <td>Delete the environment of the application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvironmentHosts</td>
                    <td>Query the host list in the environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHostFromEnvironment</td>
                    <td>Delete a host in the environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">environment-permission-controller-v2</td>
                    <td>ListEnvironmentPermissions</td>
                    <td>Query the environment permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnvironmentPermission</td>
                    <td>Edit the environment permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">hosts-controller-v2</td>
                    <td>ListNewHosts</td>
                    <td>Query the host list in a specified host cluster based on the host cluster ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeploymentHost</td>
                    <td>Modify host information based on the host ID. This interface will no longer be maintained after September 30, 2024.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteHosts</td>
                    <td>Delete hosts in a host cluster in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeploymentHostDetail</td>
                    <td>Query host details based on the host ID. This interface will no longer be maintained after September 30, 2024. You are advised to use the ShowHostDetail interface of the new version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHostDetail</td>
                    <td>Query host details based on the host ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeploymentHost</td>
                    <td>Delete a host based on the host ID. This interface will no longer be maintained after September 30, 2024.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHostInfo</td>
                    <td>Edit host information in the host cluster based on the host ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeploymentHost</td>
                    <td>This API is used to create a host in a specified host cluster. This interface will no longer be maintained after September 30, 2024. You are advised to use the new CreateHost interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyHostsToTarget</td>
                    <td>Replicate hosts to the target host cluster in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">hosts-group-controller-v2</td>
                    <td>ListHostGroupBaseInfos</td>
                    <td>Query the basic environment information list of the application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAssociateEnvironmentsInfos</td>
                    <td>Query the environment information associated with a host cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHostClusterDetail</td>
                    <td>Query details about a host cluster based on the host cluster ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHostCluster</td>
                    <td>Delete a host cluster based on the host cluster ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeploymentGroupDetail</td>
                    <td>Query details about a host cluster based on the host cluster ID. This interface will not be maintained after September 30, 2024. You are advised to use the new ShowHostClusterDetail interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostClusters</td>
                    <td>Query the host cluster list by criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeploymentGroup</td>
                    <td>Delete a host cluster based on the host cluster ID. This interface will no longer be maintained after September 30, 2024.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeploymentGroup</td>
                    <td>Modify the host cluster information based on the host cluster ID. This interface will no longer be maintained after September 30, 2024.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHostCluster</td>
                    <td>Edit the host cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHostCluster</td>
                    <td>Create a host cluster in the project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeploymentGroup</td>
                    <td>Create a host cluster in the project. This interface will no longer be maintained after September 30, 2024. You are advised to use the new CreateHostCluster interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">hosts-group-permission-controller-v2</td>
                    <td>ListHostGroupPermissions</td>
                    <td>Query the host cluster permission matrix based on the host cluster ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHostGroupPermissions</td>
                    <td>Modify the host cluster permission matrix based on the host cluster ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckWhetherHostGroupCanBeCreated</td>
                    <td>Check whether the current user has the permission to create a host cluster in the project.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
