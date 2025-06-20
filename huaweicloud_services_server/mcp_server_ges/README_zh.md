# GES MCP Server 

## 版本信息
v0.1.0

## 产品描述

GES MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务GES交互的能力。可以基于自然语言对GES资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| GraphPlugins管理API | ListScenes2 | 查询scenes场景下的应用分析能力详情,可以获得对应场景下的application、参数和功能介绍详情。 | To be tested |
|  | DeregisterScenes2 | 取消订阅scenes场景应用分析能力,取消订阅后对应scene下的application业务面API将不能使用。 | To be tested |
|  | RegisterScenes2 | 订阅scenes应用场景分析能力,便于业务面API使用对应功能。 | To be tested |
| 任务中心API | ShowJob | 查询Job的执行状态。对创建图、关闭图、启动图、删除图、导入图等异步API命令下发后,会返回jobId,通过jobId查询任务的执行状态。 | To be tested |
|  | ShowJob2 | 查询Job的执行状态。对创建图、关闭图、启动图、删除图、导入图等异步API命令下发后,会返回jobId,通过jobId查询任务的执行状态。 | To be tested |
|  | ListJobs | 查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务,该API用于查询这些任务的详情。 | To be tested |
|  | ListJobs2 | 查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务,该API用于查询这些任务的详情。 | To be tested |
| 元数据管理API | DeleteMetadata2 | 删除元数据。 | To be tested |
|  | CreateMetadata | 新增元数据。 | To be tested |
|  | ShowMetadata2 | 查询某个元数据。 | To be tested |
|  | UploadFromObs2 | 从OBS导入元数据。 | To be tested |
|  | DeleteMetadata | 删除元数据。 | To be tested |
|  | ListMetadatas2 | 查询元数据列表。 | To be tested |
|  | CreateMetadata2 | 新增元数据。 | To be tested |
|  | ListMetadatas | 查询元数据列表。 | To be tested |
|  | UploadFromObs | 从OBS导入元数据。 | To be tested |
|  | ListGraphMetadatas | 查询某个图下的元数据。 | To be tested |
| 图管理API | ExpandGraph2 | 扩副本能力允许动态扩容多个从节点,扩容的从节点可以处理读请求,从而提高读请求性能。 | To be tested |
|  | DeleteGraph2 | 删除一个图。 | To be tested |
|  | ImportGraph2 | 增量导入图数据。 | To be tested |
|  | StopGraph | 关闭一个图。如果图创建好了,暂时不用可以先关闭,需要使用时再启用。 | To be tested |
|  | CreateGraph2 | 创建一个图。 | To be tested |
|  | StartGraph2 | 启动一个图。暂时不用的图可以先关闭,需要使用时再启动。 | To be tested |
|  | ExpandGraph | 扩副本能力允许动态扩容多个从节点,扩容的从节点可以处理读请求,从而提高读请求性能。 | To be tested |
|  | DetachEip2 | 当无需继续使用EIP时,您可通过解绑EIP来释放网络资源。 | To be tested |
|  | ResizeGraph2 | 变更图规格规格。 | To be tested |
|  | AttachEip | 可以通过绑定弹性公网IP(简称EIP)访问GES服务。 | To be tested |
|  | ClearGraph2 | 清空图中所有数据。 | To be tested |
|  | ListGraphs2 | 查询当前租户所有的图。 | To be tested |
|  | AttachEip2 | 可以通过绑定弹性公网IP(简称EIP)访问GES服务。 | To be tested |
|  | DeleteGraph | 删除一个图。 | To be tested |
|  | ShowGraph | 根据图ID查询某个图详情。 | To be tested |
|  | DetachEip | 当无需继续使用EIP时,您可通过解绑EIP来释放网络资源。 | To be tested |
|  | ListGraphs | 查询当前租户所有的图。 | To be tested |
|  | StartGraph | 启动一个图。暂时不用的图可以先关闭,需要使用时再启动。 | To be tested |
|  | UpgradeGraph | 升级图。图引擎服务会定期升级版本,用户可根据需要升级图。 | To be tested |
|  | UpgradeGraph2 | 升级图。图引擎服务会定期升级版本,用户可根据需要升级图。 | To be tested |
|  | ShowGraph2 | 根据图ID查询某个图详情。 | To be tested |
|  | StopGraph2 | 关闭一个图。如果图创建好了,暂时不用可以先关闭,需要使用时再启用。 | To be tested |
|  | ImportGraph | 增量导入图数据。 | To be tested |
|  | ExportGraph2 | 导出图。 | To be tested |
|  | ClearGraph | 清空图中所有数据。 | To be tested |
|  | RestartGraph2 | 强制启动一个图。针对导入、导出 、运行中 、清空中的图。强制重启图,会将该图执行中的异步任务变为失败,然后停止图、启动图到运行状态。 | To be tested |
|  | ChangeSecurityGroup | 该接口可以在图创建成功后,修改图的安全组。 | To be tested |
|  | ExportGraph | 导出图。 | To be tested |
|  | CreateGraph | 创建一个图。 | To be tested |
|  | ResizeGraph | 扩容图规格。 | To be tested |
|  | RestartGraph | 强制启动一个图。针对导入、导出 、运行中 、清空中的图。强制重启图,会将该图执行中的异步任务变为失败,然后停止图、启动图到运行状态。 | To be tested |
| 备份管理API | ListGraphBackups | 查询某个图下的备份列表。 | To be tested |
|  | DeleteBackup2 | 删除备份。 | To be tested |
|  | CreateBackup2 | 新增备份。当前图数据出现错误或故障时,可以启动备份图进行恢复。 | To be tested |
|  | ListBackups2 | 查询备份列表。 | To be tested |
|  | CreateBackup | 新增备份。当前图数据出现错误或故障时,可以启动备份图进行恢复。 | To be tested |
|  | ListGraphBackups2 | 查询某个图下的备份列表。 | To be tested |
|  | ImportBackup2 | 导入备份 | To be tested |
|  | DeleteBackup | 删除备份。 | To be tested |
|  | ExportBackup2 | 导出备份 | To be tested |
|  | ShowBackupDownloadLink | 获取备份下载链接 | To be tested |
|  | ListBackups | 查询备份列表。 | To be tested |
| 系统管理API | ListQuotas | 查询租户配额。 | To be tested |
|  | ListQuotas2 | 查询租户配额。 | To be tested |
