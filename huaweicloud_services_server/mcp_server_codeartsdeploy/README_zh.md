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
                    <td>往上或者往下移动单个分组,用来在页面上调整分组位置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppGroups</td>
                    <td>修改分组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MoveAppToGroup</td>
                    <td>将应用移动至指定分组(支持批量)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppGroups</td>
                    <td>查询分组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppGroups</td>
                    <td>创建分组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppGroups</td>
                    <td>删除分组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">AppManagement</td>
                    <td>CreateApp</td>
                    <td>该接口用于用户创建应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">AppPermissionsController</td>
                    <td>BatchUpdateApplicationPermissions</td>
                    <td>批量修改应用权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplicationPermissions</td>
                    <td>查询应用实例级/项目级权限矩阵,传递app_id时,查询应用实例级权限矩阵;未传app_id,传递project_id时,查询应用项目级权限矩阵。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdatePermissionLevel</td>
                    <td>批量配置应用下鉴权级别为项目级或实例级。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckCanCreate</td>
                    <td>查询当前用户是否有项目下创建应用权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Application操作</td>
                    <td>DeleteApplication</td>
                    <td>删除平台应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">RecordMetricController</td>
                    <td>ShowProjectSuccessRate</td>
                    <td>获取指定项目的应用部署成功率。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskSuccessRate</td>
                    <td>获取指定应用的应用部署成功率。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">deploy-env-controller-v2</td>
                    <td>ShowExecutionParams</td>
                    <td>查询部署记录的执行参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeployTask</td>
                    <td>根据部署任务id删除应用。该接口于2024年09月30日后不再维护,推荐使用新版DeleteApplication接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteApp</td>
                    <td>批量删除项目下应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckIsDuplicateAppName</td>
                    <td>查询项目下是否存在同名应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartDeployTask</td>
                    <td>根据部署任务id部署应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeployTaskByTemplate</td>
                    <td>通过模板新建应用。该接口于2024年09月30日后不再维护,推荐使用新版CreateApp接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppInfo</td>
                    <td>更新应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDeployTasks</td>
                    <td>查询项目下应用列表。该接口于2024年09月30日后不再维护,推荐使用新版ListAllApp接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllApp</td>
                    <td>查询项目下应用列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyApplication</td>
                    <td>复制应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppDetailById</td>
                    <td>根据应用id获取应用详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppDisableStatus</td>
                    <td>禁用/取消禁用应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeployTaskDetail</td>
                    <td>根据部署任务id获取应用详情。该接口于2024年09月30日后不再维护,推荐使用新版ShowAppDetailById接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDeployTaskHistoryByDate</td>
                    <td>根据开始时间和结束时间查询项目下指定应用的历史部署记录列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">environment-controller-v2</td>
                    <td>UpdateEnvironment</td>
                    <td>应用下编辑环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvironments</td>
                    <td>查询应用下环境列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnvironment</td>
                    <td>应用下创建环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportHostToEnvironment</td>
                    <td>环境下导入主机。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnvironmentDetail</td>
                    <td>查询环境详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnvironment</td>
                    <td>删除应用下的环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvironmentHosts</td>
                    <td>查询环境内的主机列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHostFromEnvironment</td>
                    <td>环境下删除主机。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">environment-permission-controller-v2</td>
                    <td>ListEnvironmentPermissions</td>
                    <td>查询环境权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnvironmentPermission</td>
                    <td>编辑环境权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">hosts-controller-v2</td>
                    <td>ListNewHosts</td>
                    <td>根据主机集群id查询指定主机集群下的主机列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeploymentHost</td>
                    <td>根据主机id修改主机信息。该接口于2024年9月30日后不再维护。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteHosts</td>
                    <td>批量删除主机集群下的主机。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeploymentHostDetail</td>
                    <td>根据主机id查询主机详情。该接口于2024年09月30日后不再维护,推荐使用新版ShowHostDetail接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHostDetail</td>
                    <td>根据主机id查询主机详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeploymentHost</td>
                    <td>根据主机id删除主机。该接口于2024年9月30日后不再维护。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHostInfo</td>
                    <td>根据主机id编辑主机集群下主机信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeploymentHost</td>
                    <td>在指定主机集群下新建主机。该接口于2024年09月30日后不再维护,推荐使用新版CreateHost接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyHostsToTarget</td>
                    <td>批量复制主机至目标主机集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">hosts-group-controller-v2</td>
                    <td>ListHostGroupBaseInfos</td>
                    <td>查询应用下环境基本信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAssociateEnvironmentsInfos</td>
                    <td>查询主机集群关联环境信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHostClusterDetail</td>
                    <td>根据主机集群id查询主机集群详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHostCluster</td>
                    <td>根据主机集群id删除主机集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeploymentGroupDetail</td>
                    <td>根据主机集群id查询主机集群详情。该接口于2024年09月30日后不再维护,推荐使用新版ShowHostClusterDetail接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostClusters</td>
                    <td>按条件查询主机集群列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeploymentGroup</td>
                    <td>根据主机集群id删除主机集群。该接口于2024年9月30日后不再维护。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeploymentGroup</td>
                    <td>根据主机集群id修改主机集群信息。该接口于2024年9月30日后不再维护。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHostCluster</td>
                    <td>编辑主机集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHostCluster</td>
                    <td>在项目下新建主机集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeploymentGroup</td>
                    <td>在项目下新建主机集群。该接口于2024年09月30日后不再维护,推荐使用新版CreateHostCluster接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">hosts-group-permission-controller-v2</td>
                    <td>ListHostGroupPermissions</td>
                    <td>根据主机集群id查询主机集群权限矩阵。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHostGroupPermissions</td>
                    <td>根据主机集群id修改主机集群权限矩阵。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckWhetherHostGroupCanBeCreated</td>
                    <td>判断当前用户在项目下是否有权限创建主机集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">主机管理</td>
                    <td>ListHostGroups</td>
                    <td>查询服务器组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">云模式防护网站管理</td>
                    <td>DeleteHost</td>
                    <td>删除云模式防护域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHost</td>
                    <td>创建云模式防护域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">集群管理接口</td>
                    <td>ListHosts</td>
                    <td>该接口用于查询输入集群的主机列表详情。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
