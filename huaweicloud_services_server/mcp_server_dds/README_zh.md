# DDS MCP Server 

## 版本信息
v0.1.0

## 产品描述

DDS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DDS交互的能力。可以基于自然语言对DDS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 任务管理 | ShowJobDetail | 获取DDS任务中心指定ID的任务信息。 | To be tested |
|  | ListTasks | 根据指定条件查询任务中心中的任务列表和详情。 | To be tested |
| 参数配置 | ShowInstanceConfigurationModifyHistory | 查询实例参数的修改历史。 | To be tested |
|  | ListAppliedInstances | 查询指定参数模板可被应用的实例。 | To be tested |
|  | ValidateConfigurationName | 校验参数模板名称是否存在。 | To be tested |
|  | ResetConfiguration | 重置参数模板。 | To be tested |
|  | ListConfigurations | 获取参数模板列表,包括DDS数据库的所有默认参数模板和用户创建的参数模板。 | To be tested |
|  | ShowConfigurationAppliedHistory | 查询参数模板应用历史 | To be tested |
|  | UpdateEntityConfiguration | 修改指定实例的参数,可以是实例,组,节点的参数模板。 | To be tested |
|  | ShowEntityConfiguration | 获取指定实例的参数,可以是实例,组,节点的参数模板。 | To be tested |
|  | CompareConfiguration | 比较两个参数模板之间的差异。 | To be tested |
|  | SwitchConfiguration | 指定实例变更参数模板。 | To be tested |
|  | UpdateConfigurationParameter | 修改指定参数模板的参数信息,包括名称、描述、指定参数的值。 | To be tested |
|  | CopyConfiguration | 复制参数模板。 | To be tested |
|  | CreateConfiguration | 创建参数模板。 | To be tested |
|  | ShowConfigurationModifyHistory | 查询参数模板修改历史。 | To be tested |
|  | DeleteConfiguration | 删除参数模板。 | To be tested |
|  | ShowConfigurationParameter | 获取参数模板的详情。 | To be tested |
| 备份与恢复 | BatchDeleteBackup | 批量删除数据库实例的手动备份。 | To be tested |
|  | ListBackups | 根据指定条件查询备份列表。 | To be tested |
|  | RestoreInstance | 恢复到当前实例。 | To be tested |
|  | CreateManualBackup | 创建数据库实例的手动备份。 | To be tested |
|  | ShowBackupDownloadLink | 获取备份下载链接。 | To be tested |
|  | ListRestoreDatabases | 获取可恢复的数据库列表。 | To be tested |
|  | ListRestoreCollections | 获取可恢复的数据库集合列表。 | To be tested |
|  | RestoreInstanceFromCollection | 库表级时间点恢复。 | To be tested |
|  | StopBackup | 支持紧急情况下停止备份功能。 | To be tested |
|  | RestoreNewInstance | 根据备份恢复新实例。 | To be tested |
|  | SetBackupPolicy | 设置自动备份策略。 | To be tested |
|  | ListRestoreTimes | 查询实例的可恢复时间段。 | To be tested |
|  | DeleteManualBackup | 删除数据库实例的手动备份。 | To be tested |
|  | ShowBackupPolicy | 查询自动备份策略。 | To be tested |
| 定时任务 | ListScheduledTasks | 根据指定条件查询定时任务列表。 | To be tested |
|  | CancelScheduledTask | 根据任务ID取消定时任务。 | To be tested |
| 实例管理 | UpdateInstanceName | 修改实例名称 | To be tested |
|  | CheckWeakPassword | 检查弱密码 | To be tested |
|  | ShowRecyclePolicy | 查询实例回收站策略 | To be tested |
|  | ExpandReplicasetNode | 扩容指定副本集实例的节点数量 | To be tested |
|  | SwitchoverReplicaSet | 切换副本集实例下的主备节点 | To be tested |
|  | SetRecyclePolicy | 设置实例回收站策略 | To be tested |
|  | ChangeOpsWindow | 修改用户允许启动某项对数据库实例运行有影响的任务的时间范围,例如操作系统升级和数据库软件版本升级的时间窗。 | To be tested |
|  | UpdateLtsConfig | 将实例日志与LTS日志流关联,后台将自动上传实例日志到关联的LTS日志流里。 | To be tested |
|  | ListInstances | 根据指定条件查询实例列表和详情。 | To be tested |
|  | ListLtsConfigs | 查询LTS日志配置信息。 | To be tested |
|  | CancelEip | 解绑实例下节点已经绑定的弹性公网IP。 | To be tested |
|  | ShowAutoEnlargePolicy | 查询磁盘自动扩容策略。 | To be tested |
|  | ShowUpgradeDuration | 查询数据库补丁升级预估时长 | To be tested |
|  | ResizeInstanceVolume | 扩容实例相关的存储容量大小。 | To be tested |
|  | AttachInternalIp | 修改实例的内网地址 | To be tested |
|  | DeleteReadonlyNode | 当副本集添加了只读节点后,需要删除对应的只读节点需要调用此API。 | To be tested |
|  | DeleteMongosNode | 当集群实例需要缩减mongos节点时,需要调用此API。 | To be tested |
|  | ShowClientNetwork | 查询副本集跨网段访问配置 | To be tested |
|  | ListSslCertDownloadAddress | 获取SSL证书下载地址 | To be tested |
|  | UpdateClientNetwork | 副本集跨网段访问配置。 | To be tested |
|  | CreateInstance | 创建文档数据库实例,包括集群实例、副本集实例、以及单节点实例。 | To be tested |
|  | UpdateInstanceRemark | 修改实例备注。 | To be tested |
|  | ShrinkInstanceNodes | 删除实例的节点。 | To be tested |
|  | AttachEip | 为实例下的节点绑定弹性公网IP。 | To be tested |
|  | UpdateInstancePort | 修改数据库实例的端口。 | To be tested |
|  | SwitchSecondLevelMonitoring | 开启或关闭指定实例的秒级监控。 | To be tested |
|  | ListAz2Migrate | 查询实例可迁移到的可用区。 | To be tested |
|  | UpdateSecurityGroup | 变更实例关联的安全组 | To be tested |
|  | SetAutoEnlargePolicies | 设置磁盘自动扩容策略。 | To be tested |
|  | DeleteLtsConfig | 将实例日志与LTS日志流解除关联,后台将取消上传实例日志到的LTS日志流里。 | To be tested |
|  | SwitchSsl | 切换实例的SSL开关 | To be tested |
|  | UpgradeDatabaseVersion | 升级数据库补丁版本。 | To be tested |
|  | ListRecycleInstances | 查询回收站实例列表 | To be tested |
|  | ShowReplSetName | 查询数据库复制集名称 | To be tested |
|  | AddReadonlyNode | DDS副本集实例新增只读节点。 | To be tested |
|  | ResizeInstance | 变更实例的规格。 | To be tested |
|  | CreateIp | 创建集群的Shard/Config IP | To be tested |
|  | MigrateAz | 实例可用区迁移。 | To be tested |
|  | BatchUpgradeDatabaseVersion | 批量升级数据库补丁版本。 | To be tested |
|  | DeleteInstance | 删除数据库实例。 | To be tested |
|  | AddShardingNode | 扩容指定集群实例的节点数量。 | To be tested |
|  | ShowSecondLevelMonitoringStatus | 查询秒级监控配置。 | To be tested |
|  | ShowDiskUsage | 查询实例磁盘信息 | To be tested |
|  | UpdateReplSetName | 修改数据库复制集名称 | To be tested |
|  | RestartInstance | 重启实例的数据库服务。 | To be tested |
| 引擎版本和规格 | ListFlavorInfos | 查询指定条件下的实例规格信息。 | To be tested |
|  | ListDatastoreVersions | 查询指定实例类型的数据库版本信息。 | To be tested |
|  | ListStorageType | 查询当前区域下的数据库磁盘类型。 | To be tested |
|  | ListFlavors | 查询指定条件下的所有实例规格信息。 | To be tested |
| 数据库运维 | SwitchInstancePrimary | 支持副本集、shard和config备节点强制升主。 | To be tested |
|  | DeleteKillOpRuleList | 删除killOp规则。 | To be tested |
|  | ShowKillOpRuleRuleList | 获取killOp规则列表。 | To be tested |
|  | UpdateKillOpRule | 启用/禁用killOp规则。 | To be tested |
|  | CreateKillOpRule | 创建killOp规则。 | To be tested |
| 查询API版本 | ShowApiVersion | 查询指定API版本信息。 | To be tested |
|  | ListApiVersion | 查询当前支持的API版本信息列表。 | To be tested |
| 标签管理 | ListInstanceTags | 查询指定实例的标签信息。 | To be tested |
|  | ListInstancesByTags | 根据标签查询指定的数据库实例。 | To be tested |
|  | BatchTagAction | 批量添加或删除指定实例的标签。 | To be tested |
|  | ListProjectTags | 查询指定project ID下实例的所有标签集合。 | To be tested |
| 管理数据库和用户 | ListDatabaseRoles | 查询数据库角色列表。 | To be tested |
|  | CheckPassword | 检查数据库密码。 | To be tested |
|  | CreateDatabaseUser | 创建数据库用户。 | To be tested |
|  | CreateDatabaseRole | 创建数据库角色。 | To be tested |
|  | ResetPassword | 修改数据库用户密码。 | To be tested |
|  | SetBalancerSwitch | 设置集群均衡开关。 | To be tested |
|  | DeleteDatabaseRole | 删除数据库角色。 | To be tested |
|  | SetBalancerWindow | 设置集群均衡活动时间窗。 | To be tested |
|  | ListDatabases | 查询数据库列表。 | To be tested |
|  | ListDatabaseUsers | 查询数据库用户列表。 | To be tested |
|  | ShowShardingBalancer | 查询集群均衡设置。 | To be tested |
|  | DeleteDatabaseUser | 删除数据库用户。 | To be tested |
| 获取日志信息 | ListLtsErrorLogs | 查询数据库错误日志信息。 | To be tested |
|  | DownloadErrorlog | 获取错误日志下载链接。 | To be tested |
|  | SwitchSlowlogDesensitization | 设置实例的慢日志明文开关。 | To be tested |
|  | DownloadSlowlog | 获取慢日志下载链接。 | To be tested |
|  | ListLtsSlowLogs | 查询数据库慢日志信息。 | To be tested |
|  | ShowAuditlogPolicy | 查询审计日志策略。 | To be tested |
|  | ListErrorLogs | 查询数据库错误信息。 | To be tested |
|  | ListAuditlogs | 获取审计日志列表。 | To be tested |
|  | SetAuditlogPolicy | 设置审计日志策略。 | To be tested |
|  | ListAuditlogLinks | 获取审计日志下载链接。 | To be tested |
|  | DeleteAuditLog | 删除审计日志 | To be tested |
|  | ShowSlowlogDesensitizationSwitch | 查询慢日志明文开关 | To be tested |
|  | ListSlowLogs | 查询数据库慢日志信息。 | To be tested |
| 连接管理 | ShowConnectionStatistics | 查询客户端IP访问至DDS数据库实例的连接数统计信息。 | To be tested |
|  | DeleteSession | 终结实例节点会话。 | To be tested |
|  | ListSessions | 查询实例节点会话。 | To be tested |
| 配额管理 | ShowQuotas | 查询单租户在DDS服务下的资源配额,包括单节点实例配额、副本集实例配额、集群实例配额等。 | To be tested |
