# CodeArtsDeploy MCP Server 

## 版本信息
v0.1.0

## 产品描述

CodeArtsDeploy MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CodeArtsDeploy交互的能力。可以基于自然语言对CodeArtsDeploy资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AppGroupsController | MoveAppGroups | 往上或者往下移动单个分组,用来在页面上调整分组位置。 | To be tested |
|  | UpdateAppGroups | 修改分组。 | To be tested |
|  | MoveAppToGroup | 将应用移动至指定分组(支持批量)。 | To be tested |
|  | ListAppGroups | 查询分组列表。 | To be tested |
|  | CreateAppGroups | 创建分组。 | To be tested |
|  | DeleteAppGroups | 删除分组。 | To be tested |
| AppPermissionsController | BatchUpdateApplicationPermissions | 批量修改应用权限。 | To be tested |
|  | ListApplicationPermissions | 查询应用实例级/项目级权限矩阵,传递app_id时,查询应用实例级权限矩阵;未传app_id,传递project_id时,查询应用项目级权限矩阵。 | To be tested |
|  | BatchUpdatePermissionLevel | 批量配置应用下鉴权级别为项目级或实例级。 | To be tested |
|  | CheckCanCreate | 查询当前用户是否有项目下创建应用权限。 | To be tested |
| RecordMetricController | ShowProjectSuccessRate | 获取指定项目的应用部署成功率。 | To be tested |
|  | ListTaskSuccessRate | 获取指定应用的应用部署成功率。 | To be tested |
| deploy-env-controller-v2 | ShowExecutionParams | 查询部署记录的执行参数。 | To be tested |
|  | DeleteDeployTask | 根据部署任务id删除应用。该接口于2024年09月30日后不再维护,推荐使用新版DeleteApplication接口。 | To be tested |
|  | BatchDeleteApp | 批量删除项目下应用。 | To be tested |
|  | CreateApp | 新建应用。 | To be tested |
|  | CheckIsDuplicateAppName | 查询项目下是否存在同名应用。 | To be tested |
|  | StartDeployTask | 根据部署任务id部署应用。 | To be tested |
|  | CreateDeployTaskByTemplate | 通过模板新建应用。该接口于2024年09月30日后不再维护,推荐使用新版CreateApp接口。 | To be tested |
|  | UpdateAppInfo | 更新应用。 | To be tested |
|  | ListDeployTasks | 查询项目下应用列表。该接口于2024年09月30日后不再维护,推荐使用新版ListAllApp接口。 | To be tested |
|  | ListAllApp | 查询项目下应用列表。 | To be tested |
|  | CopyApplication | 复制应用。 | To be tested |
|  | ShowAppDetailById | 根据应用id获取应用详情。 | To be tested |
|  | UpdateAppDisableStatus | 禁用/取消禁用应用。 | To be tested |
|  | ShowDeployTaskDetail | 根据部署任务id获取应用详情。该接口于2024年09月30日后不再维护,推荐使用新版ShowAppDetailById接口。 | To be tested |
|  | DeleteApplication | 根据应用id删除应用。 | To be tested |
|  | ListDeployTaskHistoryByDate | 根据开始时间和结束时间查询项目下指定应用的历史部署记录列表。 | To be tested |
| environment-controller-v2 | UpdateEnvironment | 应用下编辑环境。 | To be tested |
|  | ListEnvironments | 查询应用下环境列表。 | To be tested |
|  | CreateEnvironment | 应用下创建环境。 | To be tested |
|  | ImportHostToEnvironment | 环境下导入主机。 | To be tested |
|  | ShowEnvironmentDetail | 查询环境详情。 | To be tested |
|  | DeleteEnvironment | 删除应用下的环境。 | To be tested |
|  | ListEnvironmentHosts | 查询环境内的主机列表。 | To be tested |
|  | DeleteHostFromEnvironment | 环境下删除主机。 | To be tested |
| environment-permission-controller-v2 | ListEnvironmentPermissions | 查询环境权限。 | To be tested |
|  | UpdateEnvironmentPermission | 编辑环境权限。 | To be tested |
| hosts-controller-v2 | DeleteHost | 根据主机id删除主机集群下主机。 | To be tested |
|  | ListNewHosts | 根据主机集群id查询指定主机集群下的主机列表。 | To be tested |
|  | UpdateDeploymentHost | 根据主机id修改主机信息。该接口于2024年9月30日后不再维护。 | To be tested |
|  | ListHosts | 根据主机集群id查询指定主机集群下的主机列表。该接口于2024年09月30日后不再维护,推荐使用新版ListNewHosts接口。 | To be tested |
|  | BatchDeleteHosts | 批量删除主机集群下的主机。 | To be tested |
|  | ShowDeploymentHostDetail | 根据主机id查询主机详情。该接口于2024年09月30日后不再维护,推荐使用新版ShowHostDetail接口。 | To be tested |
|  | ShowHostDetail | 根据主机id查询主机详情。 | To be tested |
|  | DeleteDeploymentHost | 根据主机id删除主机。该接口于2024年9月30日后不再维护。 | To be tested |
|  | UpdateHostInfo | 根据主机id编辑主机集群下主机信息。 | To be tested |
|  | CreateHost | 在指定主机集群下新建主机。 | To be tested |
|  | CreateDeploymentHost | 在指定主机集群下新建主机。该接口于2024年09月30日后不再维护,推荐使用新版CreateHost接口。 | To be tested |
|  | CopyHostsToTarget | 批量复制主机至目标主机集群。 | To be tested |
| hosts-group-controller-v2 | ListHostGroupBaseInfos | 查询应用下环境基本信息列表。 | To be tested |
|  | ListAssociateEnvironmentsInfos | 查询主机集群关联环境信息。 | To be tested |
|  | ShowHostClusterDetail | 根据主机集群id查询主机集群详情。 | To be tested |
|  | DeleteHostCluster | 根据主机集群id删除主机集群。 | To be tested |
|  | ShowDeploymentGroupDetail | 根据主机集群id查询主机集群详情。该接口于2024年09月30日后不再维护,推荐使用新版ShowHostClusterDetail接口。 | To be tested |
|  | ListHostClusters | 按条件查询主机集群列表。 | To be tested |
|  | DeleteDeploymentGroup | 根据主机集群id删除主机集群。该接口于2024年9月30日后不再维护。 | To be tested |
|  | UpdateDeploymentGroup | 根据主机集群id修改主机集群信息。该接口于2024年9月30日后不再维护。 | To be tested |
|  | ListHostGroups | 按条件查询主机集群列表。该接口于2024年09月30日后不再维护,推荐使用新版ListHostClusters接口。 | To be tested |
|  | UpdateHostCluster | 编辑主机集群。 | To be tested |
|  | CreateHostCluster | 在项目下新建主机集群。 | To be tested |
|  | CreateDeploymentGroup | 在项目下新建主机集群。该接口于2024年09月30日后不再维护,推荐使用新版CreateHostCluster接口。 | To be tested |
| hosts-group-permission-controller-v2 | ListHostGroupPermissions | 根据主机集群id查询主机集群权限矩阵。 | To be tested |
|  | UpdateHostGroupPermissions | 根据主机集群id修改主机集群权限矩阵。 | To be tested |
|  | CheckWhetherHostGroupCanBeCreated | 判断当前用户在项目下是否有权限创建主机集群。 | To be tested |
