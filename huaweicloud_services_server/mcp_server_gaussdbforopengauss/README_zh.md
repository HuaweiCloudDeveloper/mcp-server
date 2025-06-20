# GaussDBforopenGauss MCP Server 

## 版本信息
v0.1.0

## 产品描述

GaussDBforopenGauss MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务GaussDBforopenGauss交互的能力。可以基于自然语言对GaussDBforopenGauss资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| SQL限流 | ListLimitTask | 根据指定条件查询限流任务列表 | To be tested |
|  | DeleteLimitTask | 根据task_id进行限流任务的删除 | To be tested |
|  | CreateLimitTask | 根据具体范围和类型,进行限流任务的创建 | To be tested |
|  | ShowLimitTask | 查询限流任务详情 | To be tested |
|  | SyncLimitData | 同步内核侧sql限流数据至管控侧 | To be tested |
|  | ListNodeLimitSqlModel | 查询节点的sql模板列表 | To be tested |
|  | UpdateLimitTask | 根据新的条件进行限流任务的更新 | To be tested |
| 任务管理 | ListScheduleTask | 查看定时任务列表 | To be tested |
|  | CancelScheduleTask | 取消定时任务 | To be tested |
|  | DeleteScheduleTask | 删除定时任务信息 | To be tested |
|  | ListTasks | 获取任务中心的任务列表。 | To be tested |
|  | ShowJobDetail | 获取指定ID的任务信息。 | To be tested |
|  | DeleteJob | 删除任务记录。 | To be tested |
| 参数配置 | CreateConfigurationTemplate | 创建参数模板。 | To be tested |
|  | UpdateInstanceConfiguration | 修改指定实例的参数。 | To be tested |
|  | ShowInstanceConfiguration | 获取指定实例的参数模板。 | To be tested |
|  | ListParamGroupTemplates | 获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。 | To be tested |
|  | CopyConfiguration | 复制参数模板。 | To be tested |
|  | ListConfigurationsDiff | 获取两个参数配置模板的差异列表。 | To be tested |
|  | ListHistoryOperations | 查询参数模板的修改历史记录。 | To be tested |
|  | ShowConfigurationDetail | 根据参数模板ID获取指定参数模板详情。 | To be tested |
|  | ListParameterGroupTemplates | 获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。 | To be tested |
|  | ListAppliedHistories | 查询参数模板的应用记录,以实例级别为维度。 | To be tested |
|  | SwitchConfiguration | 指定实例变更参数模板。 | To be tested |
|  | ListApplicableInstances | 查询可应用当前参数组模板的实例列表。 | To be tested |
|  | ShowInstanceParamGroup | 获取指定实例的参数模板。 | To be tested |
|  | ValidateParaGroupName | 校验参数组名称是否存在。 | To be tested |
|  | ShowInstanceParamGroupDetail | 获取指定实例的参数模板。 | To be tested |
|  | ShowParameterGroupDetail | 根据参数模板ID获取指定参数模板详情。 | To be tested |
|  | ListConfigurations | 获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。 | To be tested |
|  | ResetConfiguration | 重置参数模板。 | To be tested |
|  | DeleteConfiguration | 删除参数模板。 | To be tested |
| 回收站 | ShowRecyclePolicy | 查看回收站的回收策略。 | To be tested |
|  | ListRecycleInstancesDetails | 查询回收站所有引擎实例列表。 | To be tested |
|  | ListRecycleInstances | 查询回收站所有引擎实例列表。 | To be tested |
|  | SetRecyclePolicy | 设置回收站策略。 | To be tested |
| 备份管理 | ShowInstanceSnapshot | 根据时间点或者备份文件查询原实例信息。 | To be tested |
|  | ListRestorableInstancesDetails | 查询可用于备份恢复的实例列表,实例信息要符合备份条件。 | To be tested |
|  | RestoreInstance | 备份恢复到当前实例 | To be tested |
|  | CreateManualBackup | 创建手动备份。 | To be tested |
|  | ShowBackupPolicy | 查询自动备份策略。 | To be tested |
|  | CreateRestoreInstance | 根据备份恢复新实例。 | To be tested |
|  | DeleteManualBackup | 删除手动备份。 | To be tested |
|  | SetNewBackupPolicy | 设置自动备份策略 | To be tested |
|  | DownloadBackup | 获取备份下载链接。 | To be tested |
|  | ListRestorableInstances | 查询可用于备份恢复的实例列表,实例信息要符合备份条件。 | To be tested |
|  | SetBackupPolicy | 设置自动备份策略。 | To be tested |
|  | ListBackupsDetails | 获取备份列表。 | To be tested |
|  | ListBackups | 获取备份列表。 | To be tested |
|  | ConfirmRestoredData | 确认备份恢复到目标实例的数据正常。 | To be tested |
|  | ListRestoreTimes | 查询可恢复时间段。 | To be tested |
|  | ListDbBackups | 获取备份列表。 | To be tested |
|  | StopBackup | 停止进行中的备份,包括全备和差备。 | To be tested |
|  | ShowSourceInstanceDetail | 根据时间点或者备份文件查询原实例信息。 | To be tested |
| 实例管理 | CreateGaussDbInstance | 创建数据库实例,仅支持IAM5的新平面认证方式(AK/SK认证方式)。 | To be tested |
|  | AttachEip | 实例下的节点绑定弹性公网IP/解绑弹性公网IP | To be tested |
|  | SearchAutoEnlargePolicy | 查询磁盘自动扩容策略 | To be tested |
|  | ShowDeploymentForm | 根据解决方案模板名称或实例ID查询副本数、分片数、节点数 | To be tested |
|  | DeleteInstance | 删除数据库实例。 | To be tested |
|  | ListDatabaseInstances | 查询数据库实例列表/查询实例详情 | To be tested |
|  | ValidateWeakPassword | 校验数据库root用户密码的安全性。 | To be tested |
|  | ListCnInfosBeforeReduce | 查询协调节点列表 | To be tested |
|  | UpdateMysqlCompatibility | 更新指定实例的M兼容端口服务配置。 | To be tested |
|  | ListInstancesDetails | 查询数据库实例列表/查询实例详情 | To be tested |
|  | ResizeInstanceFlavor | GaussDB数据库实例规格变更 | To be tested |
|  | RunInstanceAction | CN横向扩容/DN分片扩容/磁盘扩容 | To be tested |
|  | ResetPwd | 重置数据库密码。 | To be tested |
|  | ShowProjectQuotas |  | To be tested |
|  | ListInstances | 查询数据库实例列表/查询实例详情 | To be tested |
|  | ShowSslCertDownloadLink | 查询实例SSL证书下载地址。 | To be tested |
|  | CreateDbInstance | 创建数据库实例 | To be tested |
|  | ShowBalanceStatus | 查询实例是否发生过主备切换而导致主机负载不均衡。 | To be tested |
|  | SwitchShard | 支持用户对单个或多个DN分片做主备切换,同一分组内只能指定一个新的备节点进行升主操作。 | To be tested |
|  | RestartInstance | 重启数据库实例。 | To be tested |
|  | ListBindedEips | 查询实例已绑定EIP列表。 | To be tested |
|  | StartMysqlCompatibility | 开启指定实例的M兼容端口。 | To be tested |
|  | ListFeatures | 查询当前实例高级特性列表。 | To be tested |
|  | CreateInstance | 创建数据库企业版和集中式实例 | To be tested |
|  | CreateDatabaseInstance | 创建数据库实例 | To be tested |
|  | UpdateInstanceName | 修改实例名称。 | To be tested |
|  | ListComponentInfos | 查询实例的组件列表 | To be tested |
|  | UpdateFeatures | 打开高级特性开关。 | To be tested |
|  | ListInstanceDetails | 查询数据库实例列表/查询实例详情 | To be tested |
| 容灾管理 | ShowCrossCloudDisasterInstanceMonitor | 查询实例容灾监控实时状态。 | To be tested |
|  | ExecuteCrossCloudDisasterRecoveryFailover | 容灾升主failover(灾备实例端下发)。 | To be tested |
|  | ShowCrossCloudDisasterRelations | 查询容灾关系列表。 | To be tested |
|  | ExecuteCrossCloudReleaseDisaster | 解除容灾(从容灾主集群下发)。 | To be tested |
|  | ExecuteCrossCloudDisasterDataCacheEnd | 结束stream流式容灾的日志保持功能,目前只有stream流容灾支持。 | To be tested |
|  | ExecuteCrossCloudDisasterDataCacheStart | 主实例开始容灾日志保持,目前只有stream流容灾支持。 | To be tested |
|  | ListDisasterRecoveryRecord | 查询容灾操作记录。 | To be tested |
|  | ExecuteCrossCloudDisasterSwitchover | 容灾switchover(可在主备任一一端下发)。 | To be tested |
|  | ExecuteCrossCloudDisasterRestore | 流容灾备升主选择支持容灾回切,实现容灾关系的重建任务。 | To be tested |
|  | ExecuteCrossCloudDisasterStartSimulation | 开始容灾演练,目前只有stream流容灾支持。 | To be tested |
|  | ResetDrConfig | 重置容灾网络等配置。1.将自动“创建委托”以授权DBS云服务访问VPC资源信息、查询IAAS接口。2.重置实例容灾网络等配置。 | To be tested |
|  | ExecuteCrossCloudDisasterEndSimulation | 灾备实例结束容灾演练,目前只有stream流容灾支持。 | To be tested |
|  | CreateCrossCloudConstructDisaster | 搭建容灾关系(从主实例端下发)。 | To be tested |
| 引擎版本和规格 | ListFlavors | 查询数据库的规格信息。 | To be tested |
|  | ListDatastores | 查询指定数据库引擎对应的版本信息。 | To be tested |
|  | ListAvailableFlavors | 查询实例可变更规格列表。 | To be tested |
|  | ListFlavorsDetails | 查询数据库的规格信息。 | To be tested |
|  | ListInstanceEngineDetail | 查看实例引擎版本分布 | To be tested |
|  | ListDatastoresDetails | 查询引擎列表。 | To be tested |
|  | ListDbFlavors | 查询数据库的规格信息。 | To be tested |
|  | ListGaussDbDatastores | 查询引擎列表。 | To be tested |
| 插件管理 | ListKernelPlugins | 查询实例已安装的插件列表 | To be tested |
|  | ListPluginExtensions | 查询实例插件拓展信息 | To be tested |
|  | ResumePluginExtensions | 配置插件拓展能力 | To be tested |
|  | InstallKernelPlugin | 安装插件 | To be tested |
|  | ListSupportKernelPlugins | 查询支持的插件列表 | To be tested |
|  | SetKernelPluginLicense | 配置插件license | To be tested |
| 数据库磁盘类型 | ListStorageTypes | 查询指定数据库引擎对应的磁盘类型。 | To be tested |
| 数据库管理 | StopInstance | 停止数据库,同时支持节点级别的停止操作 | To be tested |
|  | StartInstance | 启动数据库,同时支持节点级别的启动操作 | To be tested |
| 日志管理 | ShowErrorLogSwitchStatus | 查询数据库错误日志采集的开关状态。 | To be tested |
|  | ListInstanceErrorLogs | 查询数据库错误日志下载链接。 | To be tested |
|  | CreateSlowLogDownload | 创建慢日志下载信息 | To be tested |
|  | ShowSlowLogDownload | 查询慢日志下载信息 | To be tested |
| 标签管理 | DeleteInstanceTag | 删除实例标签 | To be tested |
|  | ListProjectTags | 查询项目下所有用户标签信息。 | To be tested |
|  | ListPredefinedTags | 查询预预定义标签。 | To be tested |
|  | ListInstanceTags | 查询指定实例的用户标签信息。 | To be tested |
|  | AddInstanceTags | 对指定实例添加用户标签信息。 | To be tested |
| 版本升级 | UpgradeInstanceVersion | GaussDB(for openGauss)实例版本升级。包括灰度升级,就地升级,热补丁升级等三种升级方式。  | To be tested |
|  | ShowBatchUpgradeCandidateVersions | 查询批量实例可升级的版本和升级类型。 | To be tested |
|  | ShowUpgradeCandidateVersions | 查询实例可升级版本。 | To be tested |
|  | BatchShowUpgradeCandidateVersions | 查询批量实例可升级的版本和升级类型。 | To be tested |
|  | ShowUpgradeCandidateVersionsDetails | 查询实例可升级版本。 | To be tested |
|  | UpgradeInstancesVersion | GaussDB批量实例版本升级。包括灰度升级,就地升级、热补丁升级三种升级方式。 | To be tested |
|  | CreateScheduleTask | 批量实例内核版本定时升级 | To be tested |
| 磁盘管理 | ShowInstanceDisk | 查询指定实例的存储使用空间和最大空间。 | To be tested |
| 管理数据库和用户 | CreateDatabaseSchemas | 在指定实例的数据库中, 创建数据库schema。 | To be tested |
|  | CreateDatabase | 在指定实例中创建数据库。 | To be tested |
|  | AllowDbRolePrivileges | 在数据库中设置角色的权限。 | To be tested |
|  | CreateDbUser | 在指定实例中创建数据库用户。 | To be tested |
|  | ListDatabaseRoles | 查询数据库角色列表。 | To be tested |
|  | DeleteDatabase | 删除指定实例的数据库。 | To be tested |
|  | SetDbUserPwd | 重置指定数据库帐号的密码。 | To be tested |
|  | CreateDbRole | 创建数据库角色。 | To be tested |
|  | AllowDbPrivileges | 在指定实例的数据库中, 设置帐号的权限。 | To be tested |
|  | ListDatabaseSchemas | 查询指定实例的数据库SCHEMA列表。 | To be tested |
|  | ListDatabases | 查询指定实例中的数据库列表。 | To be tested |
|  | DeleteDatabaseSchema | 删除数据库schema。 | To be tested |
|  | ListDbUsers | 在指定实例中查询数据库用户列表。 | To be tested |
| 配额管理 | ListEpsQuotas | 查询企业项目配额组信息。 | To be tested |
|  | ModifyEpsQuota | 修改企业项目配额。 | To be tested |
