# RDS MCP Server 

## 版本信息
v0.1.0

## 产品描述

RDS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务RDS交互的能力。可以基于自然语言对RDS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 任务管理 | DeleteJob |  | To be tested |
|  | ListJobInfo | 获取指定ID的任务信息。 | To be tested |
|  | ListJobInfoDetail | 获取指定实例和时间范围的任务信息(SQL Server)。 | To be tested |
| 参数配置 | ShowInstanceConfiguration | 获取指定实例的参数模板。 | To be tested |
|  | ListInstanceParamHistories | 实例参数修改历史。 | To be tested |
|  | EnableConfiguration | 应用参数模板。 | To be tested |
|  | ListConfigurations | 获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。 | To be tested |
|  | CreateConfiguration | 创建参数模板。 | To be tested |
|  | ShowConfiguration | 获取指定参数模板的参数。 | To be tested |
|  | CopyConfiguration | 复制参数模板 | To be tested |
|  | UpdateInstanceConfigurationAsync | 修改指定实例的参数。 | To be tested |
|  | UpdateConfiguration | 修改参数模板参数。 | To be tested |
|  | DeleteConfiguration | 删除参数模板。 | To be tested |
|  | UpdateInstanceConfiguration | 修改指定实例的参数。 | To be tested |
|  | ApplyConfigurationAsync | 应用参数模板。 | To be tested |
| 回收站 | ShowRecyclePolicy | 查询回收站的回收策略。 | To be tested |
|  | ListRecycleInstances | 查询回收站实例信息 | To be tested |
|  | StartRecyclePolicy | 设置回收站策略。 | To be tested |
| 备份与恢复 | BatchRestorePostgreSqlTables | 表级时间点恢复(PostgreSQL) | To be tested |
|  | ListHistoryDatabase | 查询指定时间点可恢复的库 | To be tested |
|  | RestoreExistInstance | 恢复到已有实例。 | To be tested |
|  | ShowBackupDownloadLink | 获取备份下载链接。 | To be tested |
|  | ListUpdateBackupEnhancePolicy | 查询高级备份策略,可查看自定义稀疏备份等 | To be tested |
|  | ListOffSiteBackups | 查询跨区域备份列表。 | To be tested |
|  | UpdateIncreBackupPolicy1 | 修改增备策略 | To be tested |
|  | DeleteManualBackup | 删除手动备份。 | To be tested |
|  | ShowBackupPolicy | 查询自动备份策略。 | To be tested |
|  | BatchDeleteManualBackup | 批量删除手动备份。 | To be tested |
|  | ShowOffSiteBackupPolicy | 查询跨区域备份策略。 | To be tested |
|  | ListInstancesSupportFastRestore | 批量获取实例是否能在库表恢复时使用极速恢复。 | To be tested |
|  | ListShareBackups | 查询共享备份列表 | To be tested |
|  | ShowIncreBackupPolicy1 | 获取增备策略 | To be tested |
|  | ListOffSiteRestoreTimes | 查询跨区域备份可恢复时间段。 | To be tested |
|  | RestoreToExistingInstance | 恢复到已有实例。 | To be tested |
|  | BatchRestoreDatabase | 库级时间点恢复 | To be tested |
|  | RestoreTablesNew | 表级时间点恢复(MySQL)。 | To be tested |
|  | SetBackupPolicy | 设置自动备份策略。 | To be tested |
|  | ShowDatabaseLevelDatabase | 查询库级备份包含的库 | To be tested |
|  | ListRestoreTimes | 查询可恢复时间段。 | To be tested |
|  | CreateManualBackup | 创建手动备份。 | To be tested |
|  | ListBackups | 获取备份列表。 | To be tested |
|  | ListPostgresqlListHistoryTables | 查询指定时间点可恢复的表(PostgreSQL) | To be tested |
|  | ListOffSiteInstances | 查询跨区域备份实例列表。 | To be tested |
|  | RestoreTables | 表级时间点恢复(MySQL)。 | To be tested |
|  | CreateRestoreInstance | 恢复到新实例。 | To be tested |
|  | SetOffSiteBackupPolicy | 设置跨区域备份策略。 | To be tested |
|  | StopBackup | 停止创建备份 | To be tested |
| 实例管理 | UpgradeDbVersionNew | 对实例进行小版本升级。 | To be tested |
|  | StartFailover | 手动倒换主备. | To be tested |
|  | ShowAutoUpgradePolicy | 查询实例内核小版本自动升级策略 | To be tested |
|  | ListUpgradeHistories | 查询实例大版本升级历史信息。 | To be tested |
|  | ListSqlLimit | 查询SQL限流列表 | To be tested |
|  | UpgradeDbVersion | 对实例进行小版本升级。 | To be tested |
|  | ListInstances | 查询数据库实例列表。 | To be tested |
|  | UpdateInstanceName | 修改实例名称。 | To be tested |
|  | ListFlavorsResize | 查询数据库可变更规格接口 | To be tested |
|  | MigrateFollower | 迁移主备实例的备机 | To be tested |
|  | ShowDnsName | 查询实例ipv6域名。 | To be tested |
|  | BatchStopInstance | 批量停止实例 | To be tested |
|  | UnlockNodeReadonlyStatus | 解除节点只读状态接口 | To be tested |
|  | SetAutoUpgradePolicy | 设置实例内核小版本自动升级策略 | To be tested |
|  | UpdateToPeriod | RDS实例按需转包周期 | To be tested |
|  | UpgradeDbMajorVersion | PostgreSQL数据库升级大版本。 | To be tested |
|  | ListReadOnlyReplayDatabase | 查询只读实例可恢复到主实例的库 | To be tested |
|  | UpdateSqlLimit | 修改SQL限流 | To be tested |
|  | StartResizeFlavorAction | 变更数据库实例的规格。 | To be tested |
|  | DeletePostgresqlHbaConf | 删除pg_hba.conf文件的单个或多个配置,以priority做唯一标识 | To be tested |
|  | ChangeFailoverMode | 更改主备实例的数据同步方式。 | To be tested |
|  | StartInstanceSingleToHaAction | 单机转主备实例。 | To be tested |
|  | ShowStorageUsedSpace | 查询实例磁盘空间使用量。 | To be tested |
|  | StartInstanceReduceVolumeAction | 数据库实例的磁盘空间缩容。 | To be tested |
|  | StartInstanceEnlargeVolumeAction | 扩容数据库实例的磁盘空间。 | To be tested |
|  | StopInstance | 实例进行关机,通过暂时停止按需实例以节省费用,实例默认停止七天。 | To be tested |
|  | UpdatePostgresqlInstanceAlias | 修改指定数据库实例的备注信息。 | To be tested |
|  | SetSecondLevelMonitor | 设置实例秒级监控策略,约五分钟后生效,对于1秒监控和5秒监控,计费方式为按需付费(每小时扣费一次)。 | To be tested |
|  | ShowAvailableVersion | 查询实例可升级的目标版本 | To be tested |
|  | ListInspectionHistories | 查询实例大版本升级检查历史。 | To be tested |
|  | ListPostgresqlHbaInfo | 查询实例的pg_hba.conf文件配置 | To be tested |
|  | ShowReplicationStatus | 获取实例的复制状态。 | To be tested |
|  | ChangeFailoverStrategy | 切换主备实例的倒换策略. | To be tested |
|  | ChangeOpsWindow | 设置可维护时间段 | To be tested |
|  | ListVolumeInfo | 查询实例的磁盘信息 | To be tested |
|  | ShowAutoEnlargePolicy | 查询实例存储空间自动扩容策略 | To be tested |
|  | StartupInstance | 停止实例以节省费用,在停止数据库实例后,支持手动重新开启实例。 | To be tested |
|  | AddPostgresqlHbaConf | 以传入配置全量覆盖当前pg_hba.conf文件内容,入参为空时用默认配置覆盖当前文件内容 | To be tested |
|  | ShowSecondLevelMonitoring | 查询实例秒级监控策略 | To be tested |
|  | CreateInstance | 创建数据库实例。 | To be tested |
|  | ListEngineFlavors | 查询实例可变更规格 | To be tested |
|  | StartInstanceRestartAction | 重启数据库实例。 | To be tested |
|  | DeleteSqlLimit | 删除SQL限流 | To be tested |
|  | DeleteInstance | 删除数据库实例。 | To be tested |
|  | ListInstancesInfoDiagnosis | 获取指定诊断项的诊断结果 | To be tested |
|  | CreateSqlLimit | 新增SQL限流 | To be tested |
|  | ShowDomainName | 查询实例ipv4域名 | To be tested |
|  | CreateInstanceIam5 | 创建数据库实例V5接口,仅支持IAM5的新平面认证方式(AK/SK认证方式) | To be tested |
|  | ModifyPostgresqlHbaConf | 修改/新增pg_hba.conf文件的单个或多个配置,以priority做唯一标识,priority不存在的新增,存在的修改 | To be tested |
|  | ListInstanceDiagnosis | 获取诊断后的实例数量 | To be tested |
|  | CreateDnsName | 申请域名 | To be tested |
|  | UpdateTdeStatus | sqlserverTDE开关。 | To be tested |
|  | ShowTdeStatus | 根据实例id查询sqlserver TDE状态 | To be tested |
|  | UpdateDnsName | 修改域名 | To be tested |
|  | UpgradeDbMajorVersionPreCheck | 大版本升级前进行升级检查。 | To be tested |
|  | ShowUpgradeDbMajorVersionStatus | 查询大版本检查状态或升级状态。 | To be tested |
|  | SetAutoEnlargePolicy | 设置实例存储空间自动扩容策略,按扩容量扣除存储费用。 | To be tested |
|  | AttachEip | 绑定和解绑弹性公网IP。 | To be tested |
|  | ListPostgresqlHbaInfoHistory | 查询实例的pg_hba.conf文件修改历史 | To be tested |
|  | ListCollations | 查询SQLServer可用字符集 | To be tested |
|  | SwitchSqlLimit | 开启/关闭/禁用所有SQL限流 | To be tested |
|  | ListSslCertDownloadLink | 获取SSL证书下载地址 | To be tested |
|  | ListSimplifiedInstances | 获取指定实例详情 | To be tested |
|  | RestoreLogReplayDatabase | 延迟库只读,恢复库到主实例 | To be tested |
| 引擎版本和规格 | ListStorageTypes | 查询数据库磁盘类型。 | To be tested |
|  | ListFlavors | 查询数据库规格。 | To be tested |
|  | ListDatastores | 查询数据库引擎的版本。 | To be tested |
| 数据库代理 | ListRdSforMysqlProxyFlavors | 查询数据库代理规格信息。 | To be tested |
|  | DeleteRdSforMySqlProxy | 关闭数据库代理。 | To be tested |
|  | SetInstancesProxyRestart | 重启数据库代理。 | To be tested |
|  | ListRdSforMySqlProxy | 查询数据库代理信息列表。 | To be tested |
|  | CreateRdSforMySqlProxy | 开启数据库代理。 | To be tested |
|  | ModifyRdSforMySqlProxyRouteMode | 设置读写分离路由模式。 | To be tested |
| 数据库代理(PostgreSQL) | ChangeProxyScale | 数据库代理实例进行规格变更。 | To be tested |
|  | ShowInformationAboutDatabaseProxy | 查询指定实例的数据库代理详细信息。 | To be tested |
|  | SearchQueryScaleFlavors | 查询数据库代理可变更的规格信息。 | To be tested |
|  | SearchQueryScaleComputeFlavors | 查询数据库代理可变更的规格信息。 | To be tested |
|  | StartDatabaseProxy | 为指定实例开启数据库代理。 | To be tested |
|  | UpdateReadWeight | 修改指定实例的读写分离权重。 | To be tested |
|  | ChangeTheDelayThreshold | 修改指定实例的读写分离延时阈值。 | To be tested |
|  | StopDatabaseProxy | 为指定实例关闭数据库代理。 | To be tested |
| 数据库安全性 | SetSecurityGroup | 修改安全组 | To be tested |
|  | UpdatePort | 修改数据库端口 | To be tested |
|  | SwitchSsl | 设置SSL数据加密。 | To be tested |
|  | UpdateDataIp | 修改内网地址 | To be tested |
| 日志 | ListErrorlogForLts | 查询实例的错误日志数据。 | To be tested |
|  | SetLogLtsConfigs | 关联LTS配置信息 | To be tested |
|  | ListLogLtsConfigs | 获取LTS配置信息 | To be tested |
|  | ListSlowLogStatisticsForLts | 查询实例慢日志的统计数据。 | To be tested |
|  | DeleteLogLtsConfigs | 解除LTS配置信息 | To be tested |
|  | ListSlowlogForLts | 查询实例的慢日志数据。 | To be tested |
| 查询API版本 | ListApiVersionNew | 查询API版本列表。 | To be tested |
|  | ListApiVersion | 查询API版本列表。 | To be tested |
|  | ShowApiVersion | 查询指定的API版本信息。 | To be tested |
| 标签管理 | BatchTagDelAction | 批量删除标签。 | To be tested |
|  | BatchTagAddAction | 批量添加标签。 | To be tested |
|  | ListInstanceTags | 查询实例标签。 | To be tested |
|  | ListPredefinedTag | 查询预定义标签 | To be tested |
|  | ListProjectTags | 查询项目标签。 | To be tested |
| 灾备实例 | ListDrInfos | 查询容灾管理列表。 | To be tested |
|  | ListDrRelations | 批量查询容灾实例信息 | To be tested |
|  | StartInstanceMasterDrAction | 建立跨云容灾关系时配置主实例的容灾能力。 | To be tested |
|  | DeleteDisasterRecovery | 解除实例容灾关系接口 | To be tested |
|  | StartInstanceDrToMasterAction | 实例间建立的跨云容灾关系出现异常后,将灾备实例升级为主实例。 | To be tested |
|  | StartInstanceSlaveDrAction | 实例建立跨云容灾关系时配置灾备实例的容灾能力。 | To be tested |
|  | ShowDrReplicaStatus | 建立跨云容灾关系后,查询主实例和灾备实例间的复制状态及延迟。 | To be tested |
| 管理数据库和用户(MySQL) | ResetPwd | 重置数据库密码. | To be tested |
|  | ListAuthorizedDatabases | 查询指定用户的已授权数据库。 | To be tested |
|  | DeleteDbUser | 删除数据库用户。 | To be tested |
|  | UpdateDatabase | 修改指定实例中的数据库备注。 | To be tested |
|  | DeleteDatabase | 删除数据库。 | To be tested |
|  | CreateDbUser | 在指定实例中创建数据库帐号。 | To be tested |
|  | ListDbUsers | 查询数据库用户列表。 | To be tested |
|  | SetDbUserPwd | 设置数据库账号密码 | To be tested |
|  | UpdateHostPrivilege | 修改实例下用户host信息。 | To be tested |
|  | UpdateDbUserComment | 修改数据库用户名备注 | To be tested |
|  | ListAuthorizedDbUsers | 查询指定数据库的已授权用户。 | To be tested |
|  | Revoke | 解除数据库帐号权限。 | To be tested |
|  | CreateDatabase | 创建数据库。 | To be tested |
|  | SetReadOnlySwitch | 根据业务需求,设置数据库用户只读 | To be tested |
|  | AllowDbUserPrivilege | 授权数据库帐号。 | To be tested |
|  | ListDatabases | 查询数据库列表。 | To be tested |
| 管理数据库和用户(PostgreSQL) | ListPostgresqlExtension | 获取指定数据库的插件信息。 | To be tested |
|  | ExecuteRevokeDatabaseUserRole | 撤回用户角色 | To be tested |
|  | UpdateDatabaseOwner | 修改数据库owner | To be tested |
|  | RevokePostgresqlDbPrivilege | 解除数据库帐号权限 | To be tested |
|  | UpdateDbUserPrivilege | 数据库帐号授权。 | To be tested |
|  | CreatePostgresqlDbUser | 在指定实例中创建数据库用户。 | To be tested |
|  | ListPostgresqlDbUserPaginated | 在指定实例中查询数据库用户列表。 | To be tested |
|  | CreatePostgresqlDatabaseSchema | 在指定实例的数据库中, 创建数据库schema。 | To be tested |
|  | ListPostgresqlDatabases | 查询指定实例中的数据库列表。 | To be tested |
|  | ListPostgresqlDatabaseSchemas | 查询指定实例的数据库SCHEMA列表。 | To be tested |
|  | SetPostgresqlDbUserPwd | 重置指定数据库帐号的密码。 | To be tested |
|  | CreatePostgresqlExtension | 在指定数据库上创建插件。 | To be tested |
|  | UpdatePostgresqlDbUserComment | 修改数据库用户名备注 | To be tested |
|  | DeletePostgresqlDatabase | 删除数据库。 | To be tested |
|  | DeletePostgresqlExtension | 在指定数据库上删除插件。 | To be tested |
|  | SetDatabaseUserPrivilege | 设置数据库用户权限:只读或可读写。 | To be tested |
|  | DeletePostgresqlDbUser | 删除数据库用户。 | To be tested |
|  | AllowDbPrivilege | 在指定实例的数据库中, 设置帐号的权限。 | To be tested |
|  | ShowPostgresqlParamValue | 获取实例指定参数的值。 | To be tested |
|  | UpdatePostgresqlParameterValue | 修改实例指定参数的值。 | To be tested |
|  | CreatePostgresqlDatabase | 在指定实例中创建数据库。 | To be tested |
|  | ListDatabaseUserRole | 查询数据库角色信息 | To be tested |
|  | UpdatePostgresqlExtension | 在指定数据库上更新插件。 | To be tested |
|  | ExecutePrivilegeDatabaseUserRole | 授予用户角色 | To be tested |
|  | UpdatePostgresqlDatabase | 修改指定实例中的数据库备注。 | To be tested |
| 管理数据库和用户(SQL Server) | ListAuthorizedSqlserverDbUsers | 查询指定数据库的已授权用户。 | To be tested |
|  | CreateSqlserverDatabase | 创建数据库。 | To be tested |
|  | DeleteSqlserverDbUser | 删除数据库用户。 | To be tested |
|  | DeleteMsdtcLocalHost | 删除MSDTC相关主机host地址 | To be tested |
|  | SetInstancesDbShrink | 收缩数据库日志 | To be tested |
|  | DeleteSqlserverDatabase | 删除数据库。 | To be tested |
|  | ListMsdtcHosts | 查询MSDTC的hosts信息 | To be tested |
|  | ListSqlserverDbUsers | 查询数据库用户列表。 | To be tested |
|  | ModifyCollation | 修改实例字符集。 | To be tested |
|  | BatchAddMsdtcs | 添加MSDTC相关主机host地址 | To be tested |
|  | DeleteSqlserverDatabaseEx | 删除数据库。 | To be tested |
|  | ListSqlserverDatabases | 查询数据库列表。 | To be tested |
|  | CreateSqlserverDbUser | 创建数据库用户。 | To be tested |
|  | RevokeSqlserverDbUserPrivilege | 解除数据库帐号权限。 | To be tested |
|  | AllowSqlserverDbUserPrivilege | 授权数据库帐号。 | To be tested |
|  | CopyDatabase | 复制数据库 | To be tested |
|  | SetInstancesNewDbShrink | 收缩数据库日志 | To be tested |
| 获取扩展日志下载信息 | CreateXelLogDownload | 获取扩展日志下载信息 | To be tested |
| 获取扩展日志文件列表 | ListXellogFiles | 查询扩展日志文件列表。 | To be tested |
| 获取日志信息 | DownloadSlowlog | 获取慢日志下载链接。 | To be tested |
|  | ListSlowLogs | 查询数据库慢日志。 | To be tested |
|  | ListSlowLogsNew | 查询数据库慢日志。(与原v3接口相比修改offset,符合华为云服务开放 API遵从性规范3.0) | To be tested |
|  | SetSensitiveSlowLog | V3慢日志敏感信息的开关 | To be tested |
|  | SetAuditlogPolicy | 设置审计日志策略。 | To be tested |
|  | ListErrorLogsNew | 查询数据库错误日志。(与原v3接口相比修改offset,符合华为云服务开放 API遵从性规范3.0) | To be tested |
|  | ListAuditlogs | 获取审计日志列表。 | To be tested |
|  | ShowBinlogClearPolicy | 查寻指定实例的binlog本地保留时长。 | To be tested |
|  | SetBinlogClearPolicy | 修改指定实例的binlog本地保留时长。 | To be tested |
|  | ListSlowlogStatistics | 获取慢日志统计信息 | To be tested |
|  | ShowAuditlogPolicy | 查询审计日志策略。 | To be tested |
|  | ListErrorLogs | 查询数据库错误日志。 | To be tested |
|  | DownloadErrorlog | 获取错误日志下载链接。 | To be tested |
|  | ListSlowLogFile | 查询慢日志文件列表。 | To be tested |
|  | ShowAuditlogDownloadLink | 生成审计日志下载链接。 | To be tested |
| 配置只读延迟库(PostgreSQL) | SwitchLogReplay | 中止/恢复wal日志回放 | To be tested |
|  | ShowRecoveryTimeWindow | 查询wal日志恢复时间窗 | To be tested |
|  | ShowReplayDelayStatus | 获取wal日志延迟回放状态 | To be tested |
| 配额 | ShowQuotas | 查询当前项目下资源配额情况。 | To be tested |
