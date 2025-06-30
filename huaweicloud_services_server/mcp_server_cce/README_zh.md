# CCE MCP Server 


## Version
v0.1.0

## Overview

CCE MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CCE. Full-chain management of CCE resources can be carried out based on natural language.

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
                    <td rowspan="1">DDM实例管理</td>
                    <td>ShowNode</td>
                    <td>查询DDM实例节点详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">存储管理</td>
                    <td>CreateCloudPersistentVolumeClaims</td>
                    <td>该API用于在指定的Namespace下通过云存储服务中的云存储(EVS、SFS、OBS)去创建PVC(PersistentVolumeClaim)。该API待废弃,请使用Kubernetes PVC相关接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCloudPersistentVolumeClaims</td>
                    <td>该API用于删除指定Namespace下的PVC(PersistentVolumeClaim)对象,并可以选择保留后端的云存储。该API待废弃,请使用Kubernetes PVC相关接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">实例管理</td>
                    <td>ShowCluster</td>
                    <td>查询Kafka集群元数据信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">已弃用-SQL作业相关API</td>
                    <td>ListPartitions</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">插件管理</td>
                    <td>UpdateAddonInstance</td>
                    <td>更新插件实例的功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAddonTemplates</td>
                    <td>插件模板查询接口,查询插件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAddonInstances</td>
                    <td>获取集群所有已安装插件实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAddonInstance</td>
                    <td>删除插件实例的功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAddonInstance</td>
                    <td>根据提供的插件模板,安装插件实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollbackAddonInstance</td>
                    <td>将插件实例回滚到升级前的版本。只有在当前插件实例版本支持回滚到升级前的版本(status.isRollbackable为true),且插件实例状态为running(运行中)、available(可用)、abnormal(不可用)、upgradeFailed(升级失败)、rollbackFailed(回滚失败)时支持回滚。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAddonInstance</td>
                    <td>获取插件实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">插件管理(Autopilot)</td>
                    <td>ShowAutopilotAddonInstance</td>
                    <td>获取插件实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutopilotAddonInstance</td>
                    <td>更新插件实例的功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollbackAutopilotAddonInstance</td>
                    <td>将插件实例回滚到升级前的版本。只有在当前插件实例版本支持回滚到升级前的版本(status.isRollbackable为true),且插件实例状态为running(运行中)、available(可用)、abnormal(不可用)、upgradeFailed(升级失败)、rollbackFailed(回滚失败)时支持回滚。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotAddonTemplates</td>
                    <td>插件模板查询接口,查询插件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAutopilotAddonInstance</td>
                    <td>删除插件实例的功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotAddonInstance</td>
                    <td>根据提供的插件模板,安装插件实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotAddonInstances</td>
                    <td>获取集群所有已安装插件实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">日志流图表</td>
                    <td>ListCharts</td>
                    <td>该接口用于查询日志流图表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询密钥API版本信息</td>
                    <td>ShowVersion</td>
                    <td>- 功能介绍:查指定API版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">标签管理(Autopilot)</td>
                    <td>BatchDeleteAutopilotClusterTags</td>
                    <td>该API用于批量删除指定集群的资源标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateAutopilotClusterTags</td>
                    <td>该API用于批量添加指定集群的资源标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">标签管理接口</td>
                    <td>BatchCreateClusterTags</td>
                    <td>为指定集群批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteClusterTags</td>
                    <td>为指定集群批量删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">模板管理</td>
                    <td>ShowChartValues</td>
                    <td>获取模板Values</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateChart</td>
                    <td>更新模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowChart</td>
                    <td>获取模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRelease</td>
                    <td>创建模板实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRelease</td>
                    <td>删除指定模板实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReleaseHistory</td>
                    <td>查询指定模板实例历史记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRelease</td>
                    <td>获取指定模板实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteChart</td>
                    <td>删除模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadChart</td>
                    <td>下载模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadChart</td>
                    <td>上传模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserChartsQuotas</td>
                    <td>获取用户模板配额</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRelease</td>
                    <td>更新指定模板实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReleases</td>
                    <td>获取模板实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">模板管理(Autopilot)</td>
                    <td>DeleteAutopilotRelease</td>
                    <td>删除指定模板实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotReleases</td>
                    <td>获取模板实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadAutopilotChart</td>
                    <td>上传模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadAutopilotChart</td>
                    <td>下载模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutopilotChart</td>
                    <td>更新模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotRelease</td>
                    <td>创建模板实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotRelease</td>
                    <td>获取指定模板实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotUserChartsQuotas</td>
                    <td>获取用户模板配额</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotReleaseHistory</td>
                    <td>查询指定模板实例历史记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAutopilotChart</td>
                    <td>删除模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotChartValues</td>
                    <td>获取模板Values</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutopilotRelease</td>
                    <td>更新指定模板实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotCharts</td>
                    <td>获取模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotChart</td>
                    <td>获取模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">联盟管理</td>
                    <td>ListNodes</td>
                    <td>功能描述:用户可以使用该接口查询联盟可信节点(包含聚合节点和计算节点)列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">节点变更</td>
                    <td>ResizeCluster</td>
                    <td>此接口用于扩容集群,亦可用于添加空闲节点。默认情况下:表示执行扩容操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">节点池管理</td>
                    <td>UpgradeNodePool</td>
                    <td>该API用于同步节点池中已有节点的配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNodePool</td>
                    <td>该API用于在指定集群下创建节点池。仅支持集群在处于可用、扩容、缩容状态时调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNodePool</td>
                    <td>该API用于获取指定节点池的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNodePool</td>
                    <td>该API用于删除指定的节点池。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodePools</td>
                    <td>该API用于获取集群下所有节点池。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNodePool</td>
                    <td>该API用于更新指定的节点池。仅支持集群在处于可用、扩容、缩容状态时调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ScaleNodePool</td>
                    <td>该API用于伸缩指定的节点池</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">节点管理</td>
                    <td>UpdateNode</td>
                    <td>该API用于更新指定的节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddNodesToNodePool</td>
                    <td>该API用于在指定集群自定义节点池下纳管节点。竞价实例不支持纳管。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNode</td>
                    <td>该API用于在指定集群下创建节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveNode</td>
                    <td>该API用于在指定集群下移除节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LockNodepoolNodeScaleDown</td>
                    <td>该API用于节点开启缩容保护,开启缩容保护的节点无法通过修改节点池个数的方式被缩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncNode</td>
                    <td>该API用于同步节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetNode</td>
                    <td>该API用于在指定集群下重置节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNode</td>
                    <td>该API用于删除指定的节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddNode</td>
                    <td>该API用于在指定集群下纳管节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSyncNodes</td>
                    <td>该API用于批量同步节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnlockNodepoolNodeScaleDown</td>
                    <td>该API用于节点关闭缩容保护,关闭缩容保护的节点可以通过修改节点池个数的方式被缩容,只允许按需节点关闭缩容保护。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateNode</td>
                    <td>该API用于在指定集群下迁移节点到另一集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">配置管理</td>
                    <td>ShowClusterSupportConfiguration</td>
                    <td>该API用于根据集群版本类型等查询集群支持的详细配置项,用于集群创建时指定。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNodePoolConfigurationDetails</td>
                    <td>该API用于查询CCE服务下指定节点池支持配置的参数列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNodePoolConfigurations</td>
                    <td>该API用于查询指定节点池支持配置的参数内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterConfigurationDetails</td>
                    <td>该API用于查询CCE服务下指定集群支持配置的参数列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNodePoolConfiguration</td>
                    <td>该API用于修改CCE服务下指定节点池配置参数的值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowQuotas</td>
                    <td>查询当前项目下资源配额情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额管理(Autopilot)</td>
                    <td>ShowAutopilotQuotas</td>
                    <td>该API用于查询CCE服务下的资源配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像任务</td>
                    <td>ShowJob</td>
                    <td>该接口为扩展接口,主要用于查询异步接口执行情况,比如查询导出镜像任务的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">镜像缓存管理</td>
                    <td>ListImageCaches</td>
                    <td>查询镜像缓存列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageCache</td>
                    <td>查询镜像缓存详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateImageCache</td>
                    <td>创建镜像缓存。创建过程会在指定集群中启动临时Pod进行镜像缓存构建,创建镜像缓存后,可在负载创建时通过使用镜像缓存功能大幅减少下载容器镜像的耗时,实现容器的快速启动。单租户创建镜像缓存数量上限为50。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteImageCache</td>
                    <td>删除镜像缓存</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="19">集群升级</td>
                    <td>ContinueUpgradeClusterTask</td>
                    <td>继续执行被暂停的集群升级任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeWorkFlowUpdate</td>
                    <td>该API用于更新指定集群升级引导任务状态,当前仅适用于取消升级流程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClusterMasterSnapshot</td>
                    <td>集群备份</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpgradeClusterTasks</td>
                    <td>获取集群升级任务详情列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostCheck</td>
                    <td>集群升级后确认,该接口建议配合Console使用,主要用于升级步骤完成后,客户确认集群状态和业务正常后做反馈。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterUpgradeInfo</td>
                    <td>获取集群升级相关信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUpgradeWorkFlow</td>
                    <td>该API用于创建一个集群升级流程引导任务。请在调用本接口完成引导任务创建之后,通过集群升级前检查开始检查任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterUpgradeFeatureGates</td>
                    <td>获取集群升级特性开关配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PauseUpgradeClusterTask</td>
                    <td>暂停集群升级任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPreCheck</td>
                    <td>获取集群升级前检查任务详情,任务ID由调用集群检查API后从响应体中uid字段获取。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeWorkFlow</td>
                    <td>该API用于通过升级引导任务ID获取任务的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeCluster</td>
                    <td>集群升级。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeClusterTask</td>
                    <td>获取集群升级任务详情,任务ID由调用集群升级API后从响应体中uid字段获取。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterMasterSnapshotTasks</td>
                    <td>获取集群备份任务详情列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePreCheck</td>
                    <td>集群升级前检查</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryUpgradeClusterTask</td>
                    <td>重新执行失败的集群升级任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterUpgradePaths</td>
                    <td>获取集群升级路径</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPreCheckTasks</td>
                    <td>获取集群升级前检查任务详情列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpgradeWorkFlows</td>
                    <td>获取历史集群升级引导任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="23">集群升级(Autopilot)</td>
                    <td>UpdateAutopilotMaintenanceWindow</td>
                    <td>该API用于更新集群维护窗口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotPreCheckTasks</td>
                    <td>获取集群升级前检查任务详情列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotMaintenanceWindow</td>
                    <td>该API用于获取集群维护窗口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotClusterMasterSnapshotTasks</td>
                    <td>获取集群备份任务详情列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotPreCheck</td>
                    <td>集群升级前检查</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotClusterUpgradePaths</td>
                    <td>获取集群升级路径</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotUpgradeClusterTasks</td>
                    <td>获取集群升级任务详情列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotUpgradeClusterTask</td>
                    <td>获取集群升级任务详情,任务ID由调用集群升级API后从响应体中uid字段获取。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryAutopilotUpgradeClusterTask</td>
                    <td>重新执行失败的集群升级任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotPostCheck</td>
                    <td>集群升级后确认,该接口建议配合Console使用,主要用于升级步骤完成后,客户确认集群状态和业务正常后做反馈。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotMaintenanceWindow</td>
                    <td>该API用于创建集群维护窗口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotClusterMasterSnapshot</td>
                    <td>集群备份</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotUpgradePlans</td>
                    <td>该API用于获取集群自动升级计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeAutopilotWorkFlowUpdate</td>
                    <td>该API用于更新指定集群升级引导任务状态,当前仅适用于取消升级流程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotUpgradeWorkFlow</td>
                    <td>该API用于创建一个集群升级流程引导任务。请在调用本接口完成引导任务创建之后,通过集群升级前检查开始检查任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotClusterUpgradeFeatureGates</td>
                    <td>获取集群升级特性开关配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotUpgradeWorkFlow</td>
                    <td>该API用于通过升级引导任务ID获取任务的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutopilotUpgradePlan</td>
                    <td>该API用于延期集群自动升级计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotClusterUpgradeInfo</td>
                    <td>获取集群升级相关信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutopilotUpgradeWorkFlows</td>
                    <td>获取历史集群升级引导任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeAutopilotCluster</td>
                    <td>集群升级。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAutopilotMaintenanceWindow</td>
                    <td>该API用于删除集群维护窗口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotPreCheck</td>
                    <td>获取集群升级前检查任务详情,任务ID由调用集群检查API后从响应体中uid字段获取。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">集群管理</td>
                    <td>AwakeCluster</td>
                    <td>集群唤醒用于唤醒已休眠的集群,唤醒后,将继续收取控制节点资源费用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>HibernateCluster</td>
                    <td>集群休眠用于将运行中的集群置于休眠状态,休眠后,将不再收取控制节点资源费用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCluster</td>
                    <td>该API用于更新指定的集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeKubernetesClusterCert</td>
                    <td>该API用于吊销指定集群的用户证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterConfig</td>
                    <td>获取集群组件上报的LTS的配置信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKubernetesClusterCert</td>
                    <td>该API用于获取指定集群的证书信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePartition</td>
                    <td>创建分区</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePartition</td>
                    <td>更新分区</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClusterEip</td>
                    <td>该API用于通过集群ID绑定、解绑集群公网apiserver地址</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPartition</td>
                    <td>获取分区详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterEndpoints</td>
                    <td>该API用于通过集群ID获取集群访问的地址,包括PrivateIP(HA集群返回VIP)与PublicIP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClusterLogConfig</td>
                    <td>用户可以选择集群管理节点上哪些组件的日志上报LTS</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">集群管理(Autopilot)</td>
                    <td>ListAutopilotClusters</td>
                    <td>该API用于获取指定项目下所有集群的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotCluster</td>
                    <td>该API用于创建一个空集群(即只有控制节点Master,没有工作节点Node)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutopilotKubernetesClusterCert</td>
                    <td>该API用于获取指定集群的证书信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotClusterEndpoints</td>
                    <td>该API用于通过集群ID获取集群访问的地址,包括PrivateIP(HA集群返回VIP)与PublicIP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAutopilotCluster</td>
                    <td>该API用于删除一个指定的集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutopilotClusterEip</td>
                    <td>该API用于通过集群ID绑定、解绑集群公网apiserver地址</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotCluster</td>
                    <td>该API用于获取指定集群的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutopilotCluster</td>
                    <td>该API用于更新指定的集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutopilotJob</td>
                    <td>该API用于获取任务信息。通过某一任务请求下发后返回的jobID来查询指定任务的进度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">集群管理接口</td>
                    <td>ListClusters</td>
                    <td>查看用户创建的集群列表信息。该接口不兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCluster</td>
                    <td>创建一个MRS集群,并在集群中提交一个作业。该接口不兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCluster</td>
                    <td>数据完成处理分析后或者集群运行异常无法提供服务时可删除集群服务。该接口兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
