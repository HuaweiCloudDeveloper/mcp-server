# MRS MCP Server 

## 版本信息
v0.1.0

## 产品描述

MRS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务MRS交互的能力。可以基于自然语言对MRS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AvailableZone | ListAvailableZones | 在创建集群时,需要配置实例所在的可用区ID,可通过该接口查询可用区的ID。 | To be tested |
| ClusterManagement | ExpandCluster | 对MRS集群进行扩容。 | To be tested |
|  | ListNodes | 查询集群节点列表。 | To be tested |
|  | AddComponent | 集群添加组件 | To be tested |
|  | ShrinkCluster | 对MRS集群进行缩容。 | To be tested |
| DataConnectorManagement | UpdateDataConnector | 更新数据连接 | To be tested |
|  | ListDataConnector | 查询数据连接列表 | To be tested |
|  | CreateDataConnector | 创建数据连接 | To be tested |
|  | DeleteDataConnector | 删除数据连接 | To be tested |
| IAMSyncManagement | UpdateSyncIamUser | 将IAM用户和用户组同步到manager,指定用户的情况下,会将该用户关联的IAM用户组也同步到manager。 | To be tested |
|  | CancelSyncIamUser | 指定用户、用户组取消同步 | To be tested |
|  | ShowSyncIamUser | 获取已经同步的IAM用户和用户组 | To be tested |
| SQL接口 | CancelSql | 在MRS集群中取消一条SQL的执行任务。 | To be tested |
|  | ShowSqlResult | 在MRS集群中查询一条SQL的执行结果。 | To be tested |
|  | ExecuteSql | 在MRS集群中提交并执行一条SQL语句。 | To be tested |
| TagManagement | SwitchClusterTags | 对已有集群启用或关闭集群默认标签。开启后,集群内节点会打上集群默认标签。 | To be tested |
|  | ShowTagQuota | 查询标签配额信息 | To be tested |
|  | ShowTagStatus | 查询集群默认标签状态 | To be tested |
| VersionMetaQuery | ShowMrsVersionList | 展示MRS版本列表 | To be tested |
|  | ShowMrsFlavors | 查询MRS集群版本可用的规格 | To be tested |
|  | ShowMrsVersionMetadata | 查询对应版本元数据。如果参数里指定集群id,则可查询集群更新过补丁之后的最新元数据。 | To be tested |
| 作业管理接口 | ShowJobExeListNew | 在MRS指定集群中查询作业列表信息。 | To be tested |
|  | ShowSingleJobExe | 在MRS集群中查询指定作业的详细信息。 | To be tested |
|  | ShowSqlResultWithJob | 在MRS集群中查询SparkSql和SparkScript两种类型作业的SQL语句运行完成后返回的查询结果。 | To be tested |
|  | BatchDeleteJobs | 在MRS集群中批量删除作业。 | To be tested |
|  | StopJob | 在MRS集群中终止指定作业。 | To be tested |
|  | CreateExecuteJob | 在MRS集群中新增并提交一个作业。 | To be tested |
| 委托管理 | UpdateAgencyMapping | 更新用户(组)与IAM委托之间的映射关系。 | To be tested |
|  | ShowAgencyMapping | 获取用户(组)与IAM委托之间的映射关系的详细信息。 | To be tested |
| 弹性伸缩接口 | DeleteAutoScalingPolicy | 删除弹性伸缩策略。 | To be tested |
|  | CreateScalingPolicy | 对弹性伸缩规则进行编辑。 | To be tested |
|  | UpdateAutoScalingPolicy | 更新弹性伸缩策略。 | To be tested |
|  | ShowAutoScalingPolicy | 查看指定集群的所有的弹性伸缩策略信息。 | To be tested |
|  | CreateAutoScalingPolicy | 创建弹性伸缩策略。 | To be tested |
| 标签管理接口 | CreateClusterTag | 为特定的集群添加一个tag。 | To be tested |
|  | ListClustersByTags | 使用标签过滤集群。 | To be tested |
|  | ListClusterTags | 查询指定集群的标签信息。 | To be tested |
|  | BatchDeleteClusterTags | 为指定集群批量删除标签。 | To be tested |
|  | ListAllTags | 查询租户在指定Region下的所有标签集合 。 | To be tested |
|  | DeleteClusterTag | 删除特定集群的标签。 | To be tested |
|  | BatchCreateClusterTags | 为指定集群批量添加标签。 | To be tested |
| 集群HDFS文件接口 | ShowHdfsFileList | 在MRS集群中获取指定目录文件列表。 | To be tested |
| 集群管理接口 | UpdateClusterScaling | 创建集群后,扩容/缩容集群Core节点或者Task节点。MRS集群创建成功后不支持调整Master节点数量,即不支持扩缩容Master节点。该接口不兼容Sahara。 | To be tested |
|  | RunJobFlow | 创建一个MRS集群并提交作业,并支持作业完成后删除集群,支持MRS 1.8.9及以上集群版本使用。使用接口前,您需要先获取下的资源信息。 | To be tested |
|  | DeleteCluster | 数据完成处理分析后或者集群运行异常无法提供服务时可删除集群服务。该接口兼容Sahara。 | To be tested |
|  | ListClusters | 查看用户创建的集群列表信息。该接口不兼容Sahara。 | To be tested |
|  | ListHosts | 该接口用于查询输入集群的主机列表详情。 | To be tested |
|  | CreateCluster | 创建一个MRS集群,并在集群中提交一个作业。该接口不兼容Sahara。 | To be tested |
|  | ShowClusterDetails | 查看指定集群的详细信息。该接口不兼容Sahara。 | To be tested |
|  | UpdateClusterName | 修改集群名称 | To be tested |
