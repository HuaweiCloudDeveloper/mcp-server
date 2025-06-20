# CCE MCP Server 

## 版本信息
v0.1.0

## 产品描述

CCE MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CCE交互的能力。可以基于自然语言对CCE资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| API版本信息 | ShowVersion | 该API用于查询CCE服务当前支持的API版本信息列表。 | To be tested |
| 存储管理 | CreateCloudPersistentVolumeClaims | 该API用于在指定的Namespace下通过云存储服务中的云存储(EVS、SFS、OBS)去创建PVC(PersistentVolumeClaim)。该API待废弃,请使用Kubernetes PVC相关接口。 | To be tested |
|  | DeleteCloudPersistentVolumeClaims | 该API用于删除指定Namespace下的PVC(PersistentVolumeClaim)对象,并可以选择保留后端的云存储。该API待废弃,请使用Kubernetes PVC相关接口。 | To be tested |
| 插件管理 | UpdateAddonInstance | 更新插件实例的功能。 | To be tested |
|  | ListAddonTemplates | 插件模板查询接口,查询插件信息。 | To be tested |
|  | ListAddonInstances | 获取集群所有已安装插件实例 | To be tested |
|  | DeleteAddonInstance | 删除插件实例的功能。 | To be tested |
|  | CreateAddonInstance | 根据提供的插件模板,安装插件实例。 | To be tested |
|  | RollbackAddonInstance | 将插件实例回滚到升级前的版本。只有在当前插件实例版本支持回滚到升级前的版本(status.isRollbackable为true),且插件实例状态为running(运行中)、available(可用)、abnormal(不可用)、upgradeFailed(升级失败)、rollbackFailed(回滚失败)时支持回滚。 | To be tested |
|  | ShowAddonInstance | 获取插件实例详情。 | To be tested |
| 插件管理(Autopilot) | ShowAutopilotAddonInstance | 获取插件实例详情。 | To be tested |
|  | UpdateAutopilotAddonInstance | 更新插件实例的功能。 | To be tested |
|  | RollbackAutopilotAddonInstance | 将插件实例回滚到升级前的版本。只有在当前插件实例版本支持回滚到升级前的版本(status.isRollbackable为true),且插件实例状态为running(运行中)、available(可用)、abnormal(不可用)、upgradeFailed(升级失败)、rollbackFailed(回滚失败)时支持回滚。 | To be tested |
|  | ListAutopilotAddonTemplates | 插件模板查询接口,查询插件信息。 | To be tested |
|  | DeleteAutopilotAddonInstance | 删除插件实例的功能。 | To be tested |
|  | CreateAutopilotAddonInstance | 根据提供的插件模板,安装插件实例。 | To be tested |
|  | ListAutopilotAddonInstances | 获取集群所有已安装插件实例 | To be tested |
| 标签管理 | BatchCreateClusterTags | 该API用于批量添加指定集群的资源标签。 | To be tested |
|  | BatchDeleteClusterTags | 该API用于批量删除指定集群的资源标签。 | To be tested |
| 标签管理(Autopilot) | BatchDeleteAutopilotClusterTags | 该API用于批量删除指定集群的资源标签。 | To be tested |
|  | BatchCreateAutopilotClusterTags | 该API用于批量添加指定集群的资源标签。 | To be tested |
| 模板管理 | ShowChartValues | 获取模板Values | To be tested |
|  | UpdateChart | 更新模板 | To be tested |
|  | ShowChart | 获取模板 | To be tested |
|  | CreateRelease | 创建模板实例 | To be tested |
|  | DeleteRelease | 删除指定模板实例 | To be tested |
|  | ShowReleaseHistory | 查询指定模板实例历史记录 | To be tested |
|  | ShowRelease | 获取指定模板实例 | To be tested |
|  | DeleteChart | 删除模板 | To be tested |
|  | DownloadChart | 下载模板 | To be tested |
|  | UploadChart | 上传模板 | To be tested |
|  | ShowUserChartsQuotas | 获取用户模板配额 | To be tested |
|  | UpdateRelease | 更新指定模板实例 | To be tested |
|  | ListCharts | 获取模板列表 | To be tested |
|  | ListReleases | 获取模板实例列表 | To be tested |
| 模板管理(Autopilot) | DeleteAutopilotRelease | 删除指定模板实例 | To be tested |
|  | ListAutopilotReleases | 获取模板实例列表 | To be tested |
|  | UploadAutopilotChart | 上传模板 | To be tested |
|  | DownloadAutopilotChart | 下载模板 | To be tested |
|  | UpdateAutopilotChart | 更新模板 | To be tested |
|  | CreateAutopilotRelease | 创建模板实例 | To be tested |
|  | ShowAutopilotRelease | 获取指定模板实例 | To be tested |
|  | ShowAutopilotUserChartsQuotas | 获取用户模板配额 | To be tested |
|  | ShowAutopilotReleaseHistory | 查询指定模板实例历史记录 | To be tested |
|  | DeleteAutopilotChart | 删除模板 | To be tested |
|  | ShowAutopilotChartValues | 获取模板Values | To be tested |
|  | UpdateAutopilotRelease | 更新指定模板实例 | To be tested |
|  | ListAutopilotCharts | 获取模板列表 | To be tested |
|  | ShowAutopilotChart | 获取模板 | To be tested |
| 节点池管理 | UpgradeNodePool | 该API用于同步节点池中已有节点的配置 | To be tested |
|  | CreateNodePool | 该API用于在指定集群下创建节点池。仅支持集群在处于可用、扩容、缩容状态时调用。 | To be tested |
|  | ShowNodePool | 该API用于获取指定节点池的详细信息。 | To be tested |
|  | DeleteNodePool | 该API用于删除指定的节点池。 | To be tested |
|  | ListNodePools | 该API用于获取集群下所有节点池。 | To be tested |
|  | UpdateNodePool | 该API用于更新指定的节点池。仅支持集群在处于可用、扩容、缩容状态时调用。 | To be tested |
|  | ScaleNodePool | 该API用于伸缩指定的节点池 | To be tested |
| 节点管理 | UpdateNode | 该API用于更新指定的节点。 | To be tested |
|  | AddNodesToNodePool | 该API用于在指定集群自定义节点池下纳管节点。竞价实例不支持纳管。 | To be tested |
|  | CreateNode | 该API用于在指定集群下创建节点。 | To be tested |
|  | RemoveNode | 该API用于在指定集群下移除节点。 | To be tested |
|  | LockNodepoolNodeScaleDown | 该API用于节点开启缩容保护,开启缩容保护的节点无法通过修改节点池个数的方式被缩容。 | To be tested |
|  | ListNodes | 该API用于通过集群ID获取指定集群下所有节点的详细信息。 | To be tested |
|  | ShowNode | 该API用于通过节点ID获取指定节点的详细信息。 | To be tested |
|  | SyncNode | 该API用于同步节点。 | To be tested |
|  | ResetNode | 该API用于在指定集群下重置节点。 | To be tested |
|  | DeleteNode | 该API用于删除指定的节点。 | To be tested |
|  | AddNode | 该API用于在指定集群下纳管节点。 | To be tested |
|  | BatchSyncNodes | 该API用于批量同步节点。 | To be tested |
|  | UnlockNodepoolNodeScaleDown | 该API用于节点关闭缩容保护,关闭缩容保护的节点可以通过修改节点池个数的方式被缩容,只允许按需节点关闭缩容保护。 | To be tested |
|  | MigrateNode | 该API用于在指定集群下迁移节点到另一集群。 | To be tested |
| 配置管理 | ShowClusterSupportConfiguration | 该API用于根据集群版本类型等查询集群支持的详细配置项,用于集群创建时指定。 | To be tested |
|  | ShowNodePoolConfigurationDetails | 该API用于查询CCE服务下指定节点池支持配置的参数列表。 | To be tested |
|  | ShowNodePoolConfigurations | 该API用于查询指定节点池支持配置的参数内容。 | To be tested |
|  | ShowClusterConfigurationDetails | 该API用于查询CCE服务下指定集群支持配置的参数列表。 | To be tested |
|  | UpdateNodePoolConfiguration | 该API用于修改CCE服务下指定节点池配置参数的值。 | To be tested |
| 配额管理 | ShowQuotas | 该API用于查询CCE服务下的资源配额。 | To be tested |
| 配额管理(Autopilot) | ShowAutopilotQuotas | 该API用于查询CCE服务下的资源配额。 | To be tested |
| 镜像缓存管理 | ListImageCaches | 查询镜像缓存列表 | To be tested |
|  | ShowImageCache | 查询镜像缓存详情 | To be tested |
|  | CreateImageCache | 创建镜像缓存。创建过程会在指定集群中启动临时Pod进行镜像缓存构建,创建镜像缓存后,可在负载创建时通过使用镜像缓存功能大幅减少下载容器镜像的耗时,实现容器的快速启动。单租户创建镜像缓存数量上限为50。 | To be tested |
|  | DeleteImageCache | 删除镜像缓存 | To be tested |
| 集群升级 | ContinueUpgradeClusterTask | 继续执行被暂停的集群升级任务。 | To be tested |
|  | UpgradeWorkFlowUpdate | 该API用于更新指定集群升级引导任务状态,当前仅适用于取消升级流程 | To be tested |
|  | CreateClusterMasterSnapshot | 集群备份 | To be tested |
|  | ListUpgradeClusterTasks | 获取集群升级任务详情列表 | To be tested |
|  | CreatePostCheck | 集群升级后确认,该接口建议配合Console使用,主要用于升级步骤完成后,客户确认集群状态和业务正常后做反馈。 | To be tested |
|  | ShowClusterUpgradeInfo | 获取集群升级相关信息 | To be tested |
|  | CreateUpgradeWorkFlow | 该API用于创建一个集群升级流程引导任务。请在调用本接口完成引导任务创建之后,通过集群升级前检查开始检查任务。 | To be tested |
|  | ListClusterUpgradeFeatureGates | 获取集群升级特性开关配置 | To be tested |
|  | PauseUpgradeClusterTask | 暂停集群升级任务。 | To be tested |
|  | ShowPreCheck | 获取集群升级前检查任务详情,任务ID由调用集群检查API后从响应体中uid字段获取。 | To be tested |
|  | ShowUpgradeWorkFlow | 该API用于通过升级引导任务ID获取任务的详细信息。 | To be tested |
|  | UpgradeCluster | 集群升级。 | To be tested |
|  | ShowUpgradeClusterTask | 获取集群升级任务详情,任务ID由调用集群升级API后从响应体中uid字段获取。 | To be tested |
|  | ListClusterMasterSnapshotTasks | 获取集群备份任务详情列表 | To be tested |
|  | CreatePreCheck | 集群升级前检查 | To be tested |
|  | RetryUpgradeClusterTask | 重新执行失败的集群升级任务。 | To be tested |
|  | ListClusterUpgradePaths | 获取集群升级路径 | To be tested |
|  | ListPreCheckTasks | 获取集群升级前检查任务详情列表 | To be tested |
|  | ListUpgradeWorkFlows | 获取历史集群升级引导任务列表 | To be tested |
| 集群升级(Autopilot) | UpdateAutopilotMaintenanceWindow | 该API用于更新集群维护窗口。 | To be tested |
|  | ListAutopilotPreCheckTasks | 获取集群升级前检查任务详情列表 | To be tested |
|  | ShowAutopilotMaintenanceWindow | 该API用于获取集群维护窗口。 | To be tested |
|  | ListAutopilotClusterMasterSnapshotTasks | 获取集群备份任务详情列表 | To be tested |
|  | CreateAutopilotPreCheck | 集群升级前检查 | To be tested |
|  | ListAutopilotClusterUpgradePaths | 获取集群升级路径 | To be tested |
|  | ListAutopilotUpgradeClusterTasks | 获取集群升级任务详情列表 | To be tested |
|  | ShowAutopilotUpgradeClusterTask | 获取集群升级任务详情,任务ID由调用集群升级API后从响应体中uid字段获取。 | To be tested |
|  | RetryAutopilotUpgradeClusterTask | 重新执行失败的集群升级任务。 | To be tested |
|  | CreateAutopilotPostCheck | 集群升级后确认,该接口建议配合Console使用,主要用于升级步骤完成后,客户确认集群状态和业务正常后做反馈。 | To be tested |
|  | CreateAutopilotMaintenanceWindow | 该API用于创建集群维护窗口。 | To be tested |
|  | CreateAutopilotClusterMasterSnapshot | 集群备份 | To be tested |
|  | ListAutopilotUpgradePlans | 该API用于获取集群自动升级计划。 | To be tested |
|  | UpgradeAutopilotWorkFlowUpdate | 该API用于更新指定集群升级引导任务状态,当前仅适用于取消升级流程 | To be tested |
|  | CreateAutopilotUpgradeWorkFlow | 该API用于创建一个集群升级流程引导任务。请在调用本接口完成引导任务创建之后,通过集群升级前检查开始检查任务。 | To be tested |
|  | ListAutopilotClusterUpgradeFeatureGates | 获取集群升级特性开关配置 | To be tested |
|  | ShowAutopilotUpgradeWorkFlow | 该API用于通过升级引导任务ID获取任务的详细信息。 | To be tested |
|  | UpdateAutopilotUpgradePlan | 该API用于延期集群自动升级计划。 | To be tested |
|  | ShowAutopilotClusterUpgradeInfo | 获取集群升级相关信息 | To be tested |
|  | ListAutopilotUpgradeWorkFlows | 获取历史集群升级引导任务列表 | To be tested |
|  | UpgradeAutopilotCluster | 集群升级。 | To be tested |
|  | DeleteAutopilotMaintenanceWindow | 该API用于删除集群维护窗口。 | To be tested |
|  | ShowAutopilotPreCheck | 获取集群升级前检查任务详情,任务ID由调用集群检查API后从响应体中uid字段获取。 | To be tested |
| 集群管理 | AwakeCluster | 集群唤醒用于唤醒已休眠的集群,唤醒后,将继续收取控制节点资源费用。 | To be tested |
|  | HibernateCluster | 集群休眠用于将运行中的集群置于休眠状态,休眠后,将不再收取控制节点资源费用。 | To be tested |
|  | ListClusters | 该API用于获取指定项目下所有集群的详细信息。 | To be tested |
|  | ListPartitions | 获取分区列表 | To be tested |
|  | UpdateCluster | 该API用于更新指定的集群。 | To be tested |
|  | RevokeKubernetesClusterCert | 该API用于吊销指定集群的用户证书 | To be tested |
|  | ShowJob | 该API用于获取任务信息。通过某一任务请求下发后返回的jobID来查询指定任务的进度。 | To be tested |
|  | ShowClusterConfig | 获取集群组件上报的LTS的配置信息 | To be tested |
|  | CreateKubernetesClusterCert | 该API用于获取指定集群的证书信息。 | To be tested |
|  | CreatePartition | 创建分区 | To be tested |
|  | UpdatePartition | 更新分区 | To be tested |
|  | UpdateClusterEip | 该API用于通过集群ID绑定、解绑集群公网apiserver地址 | To be tested |
|  | ShowCluster | 该API用于获取指定集群的详细信息。 | To be tested |
|  | ShowPartition | 获取分区详情 | To be tested |
|  | ShowClusterEndpoints | 该API用于通过集群ID获取集群访问的地址,包括PrivateIP(HA集群返回VIP)与PublicIP | To be tested |
|  | UpdateClusterLogConfig | 用户可以选择集群管理节点上哪些组件的日志上报LTS | To be tested |
|  | ResizeCluster | 该API用于变更一个指定集群的规格。 | To be tested |
|  | CreateCluster | 该API用于创建一个空集群(即只有控制节点Master,没有工作节点Node)。请在调用本接口完成集群创建之后,通过[创建节点](cce_02_0242.xml)添加节点。 | To be tested |
|  | DeleteCluster | 该API用于删除一个指定的集群。 | To be tested |
| 集群管理(Autopilot) | ListAutopilotClusters | 该API用于获取指定项目下所有集群的详细信息。 | To be tested |
|  | CreateAutopilotCluster | 该API用于创建一个空集群(即只有控制节点Master,没有工作节点Node)。 | To be tested |
|  | CreateAutopilotKubernetesClusterCert | 该API用于获取指定集群的证书信息。 | To be tested |
|  | ShowAutopilotClusterEndpoints | 该API用于通过集群ID获取集群访问的地址,包括PrivateIP(HA集群返回VIP)与PublicIP | To be tested |
|  | DeleteAutopilotCluster | 该API用于删除一个指定的集群。 | To be tested |
|  | UpdateAutopilotClusterEip | 该API用于通过集群ID绑定、解绑集群公网apiserver地址 | To be tested |
|  | ShowAutopilotCluster | 该API用于获取指定集群的详细信息。 | To be tested |
|  | UpdateAutopilotCluster | 该API用于更新指定的集群。 | To be tested |
|  | ShowAutopilotJob | 该API用于获取任务信息。通过某一任务请求下发后返回的jobID来查询指定任务的进度。 | To be tested |
