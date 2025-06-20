# DCS MCP Server 

## 版本信息
v0.1.0

## 产品描述

DCS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DCS交互的能力。可以基于自然语言对DCS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| IP白名单管理 | ShowIpWhitelist | 查询指定实例的IP白名单。 | To be tested |
|  | UpdateIpWhitelist | 为指定实例设置IP白名单分组,包含创建、停用、编辑、删除白名单四个功能 | To be tested |
| 会话管理 | HangUpKillAllClients | 下发kill指定节点或实例的全部会话任务 | To be tested |
|  | ListClients | 获取会话列表 | To be tested |
|  | HangUpClients | kill指定的会话 | To be tested |
|  | ScanClients | 下发查询会话列表任务 | To be tested |
| 其他接口 | ListMonitoredObjects | 查询主维度对象列表,主维度ID当前支持dcs_instance_id,dcs_memcached_instance_id。 | To be tested |
|  | ShowQuotaOfTenant | 查询租户默认可以创建的实例数和总内存的配额限制,以及可以申请配额的最大值和最小值。不同的租户在不同的区域配额可能不同。 | To be tested |
|  | ExecuteCommandMobilization | 登入web-cli,执行redis命令 | To be tested |
|  | ListMaintenanceWindows | 查询维护时间窗开始时间和结束时间。 | To be tested |
|  | ListFlavors | 在创建缓存实例时,需要配置订购的产品规格编码(spec_code),可通过该接口查询产品规格,查询条件不选时默认查询全部。 | To be tested |
|  | LoginWebCli | 登录webCli | To be tested |
|  | ListMonitoredObjectsOfInstance | 查询主维度下子维度监控对象列表,当前支持子维度的主维度ID的有 dcs_instance_id | To be tested |
|  | ListAvailableZones | 查询所在局点的可用区信息 | To be tested |
|  | LogoffWebCli | 登出webCli | To be tested |
| 分片与副本 | DeleteIpFromDomainName | 将只读副本的IP从域名中摘除,摘除成功后,只读域名不会再解析到该副本IP。 | To be tested |
|  | BatchShowNodesInformation | 批量查询指定项目所有实例的节点信息、有效实例个数及节点个数。 | To be tested |
|  | ListGroupReplicationInfo | 查询读写分离实例和集群实例的分片和副本信息,其中,读写分离实例仅Redis4.0和Redis5.0的主备实例支持。 | To be tested |
|  | ShowNodesInformation | 查询指定实例的节点信息。 | To be tested |
|  | UpdateSlavePriority | 设置副本优先级,主节点故障时,权重越小的备节点切换为主节点的优先级越高。 | To be tested |
|  | ShowReplicationStates | 获取副本状态 | To be tested |
| 参数管理 | ListConfigurations | 查询指定实例的配置参数信息。 | To be tested |
|  | UpdateConfigurations | 为了确保分布式缓存服务发挥出最优性能,您可以根据自己的业务情况对DCS缓存实例的运行参数进行调整。 | To be tested |
|  | UpdateInstanceConfig | 为了确保分布式缓存服务发挥出最优性能,您可以根据自己的业务情况对DCS缓存实例的运行参数进行调整。 | To be tested |
|  | ListConfigHistories | 查询实例的参数修改记录列表,支持按照关键字查询 | To be tested |
| 后台任务管理 | ExportExcelJob | 查询实例列表导出任务详情 | To be tested |
|  | DeleteBackgroundTask | 删除后台任务 | To be tested |
|  | ListBackgroundTask | 查询后台任务列表 | To be tested |
|  | StartInstanceResizeCheckJob | 提交前置检查任务 | To be tested |
|  | ListCenterTask | 查询任务中心任务列表 | To be tested |
|  | ShowBackgroundTaskProgress | 查询后台任务详细信息 | To be tested |
|  | ShowJobInfo | 查询租户Job执行结果 | To be tested |
|  | DeleteCenterTask | 删除任务中心任务 | To be tested |
| 备份与恢复 | RestoreInstance | 恢复指定的缓存实例。 | To be tested |
|  | ListBackupRecords | 查询指定缓存实例的备份信息列表。 | To be tested |
|  | CopyInstance | 备份指定的缓存实例。 | To be tested |
|  | DeleteBackupFile | 删除缓存实例已备份的文件。 | To be tested |
|  | ListRestoreRecords | 查询指定缓存实例的恢复记录列表。 | To be tested |
|  | ListBackupFileLinks | 获取指定实例的备份文件下载链接,下载备份文件。 | To be tested |
| 实例管理 | UpdatePassword | 修改缓存实例的密码。 | To be tested |
|  | MigrateAz | 迁移缓存实例可用区,完成单可用区实例跨可用区改造。 | To be tested |
|  | UpdateBandwidth | 修改实例分片带宽。 | To be tested |
|  | UpdateClientIpTransparentTransmission | 开启或关闭客户端ip透传 | To be tested |
|  | ShowBandwidths | 获取实例各个分片带宽。 | To be tested |
|  | ShowInstanceTopology | 查询集群实例拓扑关系图。 | To be tested |
|  | RestartOrFlushInstances | 重启运行中的DCS缓存实例。 | To be tested |
|  | UpdateInstanceBandwidth | 变更指定实例的带宽 | To be tested |
|  | ListNumberOfInstancesInDifferentStatus | 查询该租户在当前区域下不同状态的实例数。 | To be tested |
|  | UpgradeInstanceMinorVersion | 升级实例小版本。 | To be tested |
|  | ShowInstanceVersion | 获取对应实例内核版本号。 | To be tested |
|  | ChangeNodesStartStopStatus | 实例节点启停。执行节点关机操作前的24小时内,需要对实例(单机实例除外)进行数据备份。 | To be tested |
|  | DeleteInstanceBandwidthAutoScalingPolicy | 删除实例带宽弹性伸缩策略。 | To be tested |
|  | ExportInstancesTask | 异步导出实例资源 | To be tested |
|  | ListStatisticsOfRunningInstances | 查询当前租户下处于“运行中”状态的缓存实例的统计信息。 | To be tested |
|  | ResetPassword | 重置缓存实例的密码。 | To be tested |
|  | UpdateInstanceBandwidthAutoScalingPolicy | 更新实例带宽弹性伸缩策略。暂不支持实例带宽自动回缩。 | To be tested |
|  | ChangeMasterStandby | 切换实例主备节点,只有主备实例支持该操作。 | To be tested |
|  | ChangeMasterStandbyAsync | 异步交换实例主备节点 | To be tested |
|  | ShowConfigHistoryDetail | 查询实例参数修改记录详情 | To be tested |
|  | UpdatePublicIp | 开启/修改实例公网访问。 | To be tested |
|  | DeletePublicIp | 关闭实例公网访问。 | To be tested |
|  | ExecuteClusterSwitchover | 集群分片倒换,适用于proxy和cluster实例 | To be tested |
|  | ListInstanceOperations | 查询实例是否可以扩容 | To be tested |
|  | ShowInstanceBandwidthAutoScalingPolicy | 查询实例带宽弹性伸缩策略。 | To be tested |
| 实例诊断 | CreateDiagnosisTask | 诊断指定的缓存实例。 | To be tested |
|  | DeleteDiagnosisTask | 删除诊断记录。 | To be tested |
|  | ShowDiagnosisTaskDetails | 通过报告ID查询诊断报告的详细信息。 | To be tested |
|  | ListDiagnosisTasks | 查询指定缓存实例诊断任务列表。 | To be tested |
| 数据迁移 | StopMigrationTask | 停止数据迁移任务。 | To be tested |
|  | CreateMigrationTask | 创建数据迁移任务。 | To be tested |
|  | StopMigrationTaskSync | 同步停止数据迁移任务。 | To be tested |
|  | DeleteMigrationTask | 删除数据迁移任务。 | To be tested |
|  | ShowMigrationTask | 查询迁移任务详情。 | To be tested |
|  | BatchRestartOnlineMigrationTasks | 批量重启在线迁移任务,接口响应成功,返回重启在线迁移任务下发结果。 | To be tested |
|  | SetOnlineMigrationTask | 配置在线数据迁移任务。 | To be tested |
|  | ShowMigrationTaskStats | 查询在线迁移进度明细。 | To be tested |
|  | RollbackExchangeInstanceIp | IP交换回滚。 | To be tested |
|  | UpdateMigrationTask | 设置迁移任务自动重连 | To be tested |
|  | ExchangeInstanceIp | 进行IP交换 | To be tested |
|  | BatchStopMigrationTasks | 批量停止数据迁移任务,接口响应成功,仅表示下发任务成功。查询到迁移任务状态为TERMINATED时,即停止成功。 | To be tested |
|  | ListMigrationTaskLogs | 查询迁移日志列表 | To be tested |
|  | ListMigrationTask | 查询迁移任务列表。 | To be tested |
|  | CreateOnlineMigrationTask | 创建在线数据迁移任务。 | To be tested |
| 日志管理 | CreateRedislogDownloadLink | 获取日志下载链接。 | To be tested |
|  | ListSlowlog | 查询慢日志。 | To be tested |
|  | CreateRedislog | 采集Redis运行日志。 | To be tested |
|  | ListRedislog | 查询Redis运行日志列表。 | To be tested |
| 标签管理 | ListTagsOfTenant | 查询租户在指定Project中实例类型的所有资源标签集合。 | To be tested |
|  | ShowTags | 通过实例ID查询标签。 | To be tested |
|  | BatchCreateOrDeleteTags | 为指定实例批量添加标签,或批量删除标签。 | To be tested |
| 模板管理 | CreateCustomTemplate | 创建自定义模板 | To be tested |
|  | ShowConfigTemplate | 查询参数模板详情 | To be tested |
|  | DeleteConfigTemplate | 删除自定义模板 | To be tested |
|  | ListConfigTemplates | 查询租户的参数模板列表,支持按照条件查询 | To be tested |
|  | UpdateConfigTemplate | 修改自定义模板 | To be tested |
| 生命周期管理 | ResizeInstance | 用户可以为状态为“运行中”的DCS缓存实例进行规格变更,当前仅能支持按需实例的同副本或分片数量的实例规格变更。 | To be tested |
|  | CreateInstance | 创建缓存实例,该接口创建的缓存实例支持按需计费和包周期两种方式。 | To be tested |
|  | ShowInstance | 通过实例ID查询实例的详细信息。 | To be tested |
|  | UpdateInstance | 修改缓存实例的信息,可修改信息包括实例名称、描述、备份策略、维护时间窗开始和结束时间以及安全组。 | To be tested |
|  | CreateResizeOrder | 包周期实例变更规格 | To be tested |
|  | BatchDeleteInstances | 批量删除多个缓存实例。 | To be tested |
|  | ValidateDeletableReplica | 校验集群副本是否支持删除 | To be tested |
|  | ListInstances | 查询租户的缓存实例列表,支持按照条件查询。 | To be tested |
|  | DeleteSingleInstance | 删除指定的缓存实例,释放该实例的所有资源。 | To be tested |
| 离线全量key分析 | CreateOfflineKeyAnalysis | 创建离线全量key分析任务。离线全量key分析用于分析实例指定节点备份文件中的TOP100大key,每种数据类型前缀数量TOP50的key和每种数据类型key的内存占用和数量的分布情况。仅Redis 4.0、5.0、6.0版本及Redis企业版实例支持。 | To be tested |
|  | ShowOfflineKeyAnalysisTask | 查询离线全量key分析详情。 | To be tested |
|  | ListOfflineKeyAnalysisTask | 查询离线全量key分析任务列表,支持Redis4.0、5.0、6.0版本及Redis企业版。 | To be tested |
|  | DeleteOfflineKeyAnalysisTask | 删除离线全量key分析记录。 | To be tested |
| 缓存分析 | UpdateExpireAutoScanConfig | 修改自动扫描配置 | To be tested |
|  | DownloadHotKey | 下载热key。 | To be tested |
|  | ShowBigkeyAutoscanConfig | 查询大key自动分析配置。 | To be tested |
|  | ShowHotkeyAutoscanConfig | 查询热key自动分析配置。 | To be tested |
|  | ShowHotkeyTaskDetails | 查询热key分析详情。 | To be tested |
|  | CreateBigkeyScanTask | 为Redis实例创建大key分析任务。 | To be tested |
|  | CreateHotkeyScanTask | 创建热key分析任务,Redis 3.0 不支持热key分析。 | To be tested |
|  | UpdateHotkeyAutoScanConfig | 设置热key自动分析配置。 | To be tested |
|  | ShowExpireKeyScanInfo | 查询过期Key扫描记录 | To be tested |
|  | ListHotKeyScanTasks | 查询热key分析历史记录。 | To be tested |
|  | ListBigkeyScanTasks | 查询大key分析任务列表。 | To be tested |
|  | ShowExpireAutoScanConfig | 查询自动扫描配置 | To be tested |
|  | UpdateBigkeyAutoscanConfig | 设置大key自动分析配置。 | To be tested |
|  | DeleteBigkeyScanTask | 删除大key分析记录。 | To be tested |
|  | ShowBigkeyScanTaskDetails | 查询大key分析详情。 | To be tested |
|  | ScanExpireKey | 立刻扫描过期Key | To be tested |
|  | DeleteHotkeyScanTask | 删除热key分析任务。 | To be tested |
|  | CreateAutoExpireScanTask | 创建过期key扫描任务(Redis 3.0 不支持过期key扫描)。 | To be tested |
| 网络安全 | UpdateSslSwitch | 开启/关闭SSL。该接口目前仅针对Redis 6.0基础版版本实例。 | To be tested |
|  | UpdateIpWhitelistAsync | 为指定实例设置IP白名单分组,包含创建、停用、编辑、删除白名单四个功能。返回异步任务jobId,设置白名单分组信息会覆盖掉已有的白名单信息,因此在新增IP白名单分组时,需保留已有的白名单信息后再编辑新的白名单分组信息。 | To be tested |
|  | DownloadSslCert | 下载实例SSL证书。该接口目前仅针对Redis 6.0基础版版本实例。 | To be tested |
|  | ShowInstanceSslDetail | 查询实例SSL信息。该接口目前仅针对Redis 6.0基础版版本实例。 | To be tested |
| 账号管理 | CreateAclAccount | "为redis4.0/5.0实例(Cluster集群实例除外)创建权限访问账号,包含读写和只读权限。 | To be tested |
|  | UpdateAclAccountRemark | ACL账号修改备注 | To be tested |
|  | UpdateAclAccount | 修改用户的类型。 | To be tested |
|  | ListAclAccounts | 查询ACL账户列表。 | To be tested |
|  | UpdateAclAccountPassWord | 修改ACL账号密码。 | To be tested |
|  | DeleteAclAccount | 删除所创建的ACL普通账号 | To be tested |
|  | ResetAclAccountPassWord | 重置ACL账号密码。 | To be tested |
