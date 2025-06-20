# DWS MCP Server 

## 版本信息
v0.1.0

## 产品描述

DWS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DWS交互的能力。可以基于自然语言对DWS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 主机监控 | ListMonitorIndicators | 查询性能监控指标。 | To be tested |
|  | ListMetrics | 查询集群使用指标列表。 | To be tested |
|  | ListQueries | 该接口用于查询实时SQL列表。 | To be tested |
|  | ListMetricsData | 获取指定指标相关采集数据。 | To be tested |
|  | ListHostDisk | openApi查询磁盘信息。 | To be tested |
|  | ListHostOverview | openApi查询主机概览。 | To be tested |
|  | ListMonitorIndicatorData | openApi查询历史监控数据。 | To be tested |
|  | ShowQueryDetail | 查询SQL执行信息。 | To be tested |
|  | ListHostNet | openapi获取网卡状态。 | To be tested |
|  | ListTablesStatistic | 该接口用于查询表倾斜或脏页率信息。 | To be tested |
| 事件管理 | ListEvents | 查询事件列表。 | To be tested |
|  | DeleteEventSub | 删除订阅的事件。 | To be tested |
|  | CreateEventSub | 添加订阅的事件。 | To be tested |
|  | ListEventSubs | 查询订阅的事件。 | To be tested |
|  | ListEventSpecs | 查询事件配置。 | To be tested |
|  | UpdateEventSub | 更新订阅事件。 | To be tested |
| 任务管理 | ListJobDetails | 查询任务进度信息。 | To be tested |
| 升级管理 | UpdateMaintenanceWindow | 您可以根据业务需求,设置可维护时间段。建议将可维护时间段设置在业务低峰期,避免业务在维护过程中异常中断。 | To be tested |
|  | ListUpdatableVersion | 获取集群可升级的目标版本。 | To be tested |
|  | ExecuteClusterUpgradeAction | 下发集群升级相关操作。 | To be tested |
|  | ListUpdateRecord | 通过此接口获取当前集群升级记录。 | To be tested |
| 参数配置 | ListClusterConfigurationsParameter | 查询集群所关联的参数组。 | To be tested |
|  | UpdateConfiguration | 修改集群使用的参数配置信息。 | To be tested |
|  | ListConfigurationsAuditRecords | 查询参数修改审计记录。 | To be tested |
|  | ListClusterConfigurations | 查询集群所关联的参数组。 | To be tested |
| 可用区 | ListAvailabilityZones | 在创建实例时,需要配置实例所在的可用区ID,可通过该接口查询可用区的ID。 | To be tested |
| 告警管理 | UpdateAlarmSub | 更新订阅的告警。 | To be tested |
|  | ListAlarmStatistic | 查询告警统计。 | To be tested |
|  | ListAlarmConfigs | 查询告警配置。 | To be tested |
|  | DeleteAlarmSub | 删除订阅的告警。 | To be tested |
|  | ListAlarmSubs | 查询订阅告警。 | To be tested |
|  | CreateAlarmSub | 创建告警订阅。 | To be tested |
|  | ListAlarmDetail | 查询告警详情列表。 | To be tested |
| 审计日志 | ListAuditLog | 查询审计日志记录。 | To be tested |
| 容灾管理 | DeleteDisasterRecovery | 该接口用于删除容灾操作。 | To be tested |
|  | ListAvailableDisasterClusters | 该接口用于查询可用的容灾集群列表。 | To be tested |
|  | UpdateDisasterInfo | 该接口用于更新容灾配置操作。 | To be tested |
|  | StartDisasterRecovery | 该接口用于启动容灾操作。 | To be tested |
|  | ShowDisasterDetail | 该接口用于查询单个容灾详情。 | To be tested |
|  | ShowDisasterProgress | 该接口用于查询容灾进度详情信息操作。 | To be tested |
|  | CreateDisasterRecovery | 该接口用于创建集群间容灾。 | To be tested |
|  | PauseDisasterRecovery | 该接口用于停止容灾操作。 | To be tested |
|  | ListDisasterRecover | 该接口用于查询容灾列表。 | To be tested |
|  | SwitchoverDisasterRecovery | 该接口用于容灾进行灾备切换操作。 | To be tested |
|  | CheckDisasterName | 该接口用于查询容灾名称是否可用。 | To be tested |
|  | RestoreDisaster | 该接口用于主备集群进行异常切换,备集群恢复可用状态后进行的容灾恢复操作。 | To be tested |
|  | SwitchFailoverDisaster | 该接口用于容灾异常场景下进行主备集群切换操作。 | To be tested |
| 快照管理 | ListSnapshotDetails | 该接口用于使用快照ID查询快照详情。 | To be tested |
|  | ListSnapshots | 该接口用于查询快照列表。 | To be tested |
|  | RestoreCluster | 该接口用于使用快照恢复集群。 | To be tested |
|  | AddSnapshotCrossRegionPolicy | 该接口用于设置跨区域备份配置。 | To be tested |
|  | CreateSnapshot | 该接口用于为指定集群创建快照。 | To be tested |
|  | ListSnapshotCrossRegion | 该接口用于获取跨区域快照可用局点。 | To be tested |
|  | DeleteSnapshotPolicy | 该接口用于删除一个快照策略。 | To be tested |
|  | CheckTableRestore | 该接口用于用户恢复表名检测。 | To be tested |
|  | ListClusterSnapshots | 该接口用于查询集群快照列表。 | To be tested |
|  | ListSnapshotStatistics | 快照统计信息。 | To be tested |
|  | CopySnapshot | 该接口用于复制一个自动快照。 | To be tested |
|  | CreateSnapshotPolicy | 该接口用于设置快照策略。 | To be tested |
|  | DeleteSnapshotCrossRegionPolicy | 该接口用于删除跨区域备份配置。 | To be tested |
|  | DeleteSnapshot | 该接口用于删除一个指定手动快照。 | To be tested |
|  | ListSnapshotCrossRegionPolicy | 该接口用于查询所有跨区域快照配置。 | To be tested |
|  | RestoreTable | 该接口用于恢复表。 | To be tested |
|  | ListSnapshotPolicy | 查询快照策略。 | To be tested |
| 数据库权限管理 | UpdateDatabaseAuthority | 修改数据库对象权限。 | To be tested |
|  | ListDatabaseUsers | 查询所有数据库用户/角色。 | To be tested |
|  | ListDatabaseUserAuthorities | 查询用户/角色拥有权限。 | To be tested |
|  | ShowDatabaseAuthority | 查询数据库对象权限。 | To be tested |
|  | ExecuteDatabaseOmUserAction | 进行数据库运维账户操作。 | To be tested |
|  | ShowDatabaseUser | 查询指定用户信息。 | To be tested |
|  | SyncIamUsers | 同步IAM用户到数据库。 | To be tested |
|  | ExportUserAuthority | 导出数据库用户/角色的权限列表,接口返回的是输出流,xlsx文件。 | To be tested |
|  | CreateDatabaseUser | 创建数据库用户/角色。 | To be tested |
|  | UpdateDatabaseUserInfo | 修改指定用户信息。 | To be tested |
|  | ShowDatabaseOmUserStatus | 获得数据库运维账户状态。 | To be tested |
|  | DeleteDatabaseUser | 删除数据库用户。 | To be tested |
|  | ListSyncRecords | 查询身份源同步记录。 | To be tested |
|  | ExportDatabaseUsers | 导出数据库用户/角色,接口返回的是输出流,xlsx文件。 | To be tested |
| 数据源 | ListDataSource | 该接口用于查询数据源。 | To be tested |
|  | DeleteDataSource | 该接口用于删除一个数据源。 | To be tested |
|  | CreateDataSource | 该接口用于创建一个数据源。 | To be tested |
|  | UpdateDataSource | 该接口用于更新一个数据源。 | To be tested |
| 日志管理 | DisableLtsLogs | 该接口用于关闭集群LTS云日志服务。 | To be tested |
|  | ListLtsLogs | 获取LTS日志列表。 | To be tested |
|  | EnableLtsLogs | 该接口用于开启集群LTS云日志服务。 | To be tested |
| 标签管理 | ListTags | 查询项目标签列表。 | To be tested |
|  | BatchCreateResourceTag | 为指定集群批量添加标签。 | To be tested |
|  | ListClusterTags | 查询指定集群的标签信息。 | To be tested |
|  | BatchDeleteResourceTag | 为指定集群批量删除标签。 | To be tested |
| 节点变更 | ShowClusterRedistribution | 该接口用于查看当前集群的重分布模式、重分布进度、数据表重分布详情等监控信息。 | To be tested |
|  | ResizeClusterWithExistedNodes | 此接口用于从空闲节点扩容。 | To be tested |
|  | ResizeCluster | 此接口用于扩容集群,亦可用于添加空闲节点。默认情况下:表示执行扩容操作。 | To be tested |
|  | ListClusterCn | 查询集群的CN节点列表。 | To be tested |
|  | ListTargetFlavors | 查询支持变更的目标规格列表。 | To be tested |
|  | DeleteClusterNodes | 此接口用于删除空闲节点。 | To be tested |
|  | ExecuteFlavorChange | 执行规格变更。 | To be tested |
|  | ExpandInstanceStorage | 随着客户业务的发展,磁盘空间往往最先出现资源瓶颈,在其他资源尚且充足的情况下,通过磁盘扩容可快速缓解存储资源瓶颈现象,操作过程中无需暂停业务,并且不会造成CPU、内存等资源浪费。   | To be tested |
|  | BatchDeleteClusterCn | 当用户集群创建后,实际需要的CN数量会随着业务需求而发生变化,因此管理CN节点功能的实现使用户可以根据实际需求动态调整集群CN数量。 | To be tested |
|  | ShowClusterStorageExpandRange | 此接口可用于查看磁盘扩容操作时支持的扩容范围。 | To be tested |
|  | StopRedistribution | 该接口用于暂停运行状态下的重分布操作,重分布暂停状态可设置重分布优先级,修改重分布并发数等操作。 | To be tested |
|  | CheckGrowCluster | 此接口用于集群扩容前检查,提前识别子网不足、权限不足等问题导致的扩容失败。 | To be tested |
|  | ListRedistributionSchema | 获取待重分布表所属模式信息。 | To be tested |
|  | ExecuteRedistributionCluster | 该接口用于集群扩容后将老节点数据均匀分布到新扩节点的数据重分布操作,数据“重分布”后将大大提升业务响应速率。 | To be tested |
|  | UpdateRedistributionConfigurations | 更新重分布配置。 | To be tested |
|  | SetRedistributionPriority | 更新重分布表优先级。 | To be tested |
|  | RestoreRedistribution | 此接口用于恢复暂停状态下的重分布操作,仅支持DWS2.0集群。 | To be tested |
|  | ShrinkCluster | 该接口用于缩容集群。 | To be tested |
|  | ListClusterNodes | 查询节点列表。 | To be tested |
|  | BatchCreateClusterCn | 当用户集群创建后,实际需要的CN数量会随着业务需求而发生变化,因此管理CN节点功能的实现使用户可以根据实际需求动态调整集群CN数量。 | To be tested |
|  | ListClusterScaleInNumbers | 查询合适的缩容数。 | To be tested |
|  | CheckClusterShrink | 缩容前检查,确保缩容前、缩容后均满足正常操作要求。 | To be tested |
| 资源管理 | ListWorkloadQueue | 查询工作负载队列。 | To be tested |
|  | ListSchemas | 查询集群模式空间信息。 | To be tested |
|  | ShowWorkloadPlanStage | 查询工作负载计划阶段详细信息。 | To be tested |
|  | ShowWorkloadPlan | 查询某个工作负载计划详细信息。 | To be tested |
|  | AddWorkloadPlanStage | 添加工作负载计划阶段。 | To be tested |
|  | ListWorkloadRules | 查询当前集群的异常规则列表。 | To be tested |
|  | UpdateQueueResources | 更新工作负载队列资源配置信息。 | To be tested |
|  | DeleteWorkloadPlanStage | 删除工作负载计划删除工作负载计划阶段。 | To be tested |
|  | CreateClusterWorkload | 打开或关闭资源管理功能,新集群默认是打开状态。 | To be tested |
|  | ShowWorkloadQueue | 获得工作负载队列详细信息。 | To be tested |
|  | CreateWorkloadPlan | 添加工作负载计划。 | To be tested |
|  | StopWorkloadPlan | 停止工作负载计划。 | To be tested |
|  | UpdateWorkloadPlanStage | 修改资源管理计划阶段。 | To be tested |
|  | DeleteWorkloadQueue | 该接口用于删除资源池。 | To be tested |
|  | ListClusterWorkload | 查询资管管理开关。 | To be tested |
|  | AddWorkloadRule | 添加异常规则。 | To be tested |
|  | ListWorkloadQueueUsers | 获得工作负载队列的绑定用户列表。 | To be tested |
|  | AddWorkloadQueue | 添加工作负载队列。 | To be tested |
|  | DeleteWorkloadPlan | 删除工作负载计划。 | To be tested |
|  | DeleteQueueUserList | 删除工作负载队列的绑定用户。 | To be tested |
|  | StartWorkloadPlan | 启动工作负载计划。 | To be tested |
|  | SwitchPlanStage | 切换工作负载计划阶段。 | To be tested |
|  | ListPlanExecLogs | 查看计划执行日志。 | To be tested |
|  | UpdateSchemas | 更新模式空间限额。 | To be tested |
|  | ListWorkloadPlans | 查询集群中所有资源管理计划。 | To be tested |
|  | AddQueueUserList | 添加工作负载队列的绑定用户。 | To be tested |
| 连接管理 | AssociateElb | 集群绑定Elb接口。 | To be tested |
|  | ListElbs | 查询集群可以关联的Elb列表。 | To be tested |
|  | DeleteClusterDns | 删除指定集群域名。 | To be tested |
|  | AssociateEip | 集群绑定Eip。 | To be tested |
|  | UpdateClusterDns | 为指定集群修改域名。 | To be tested |
|  | DisassociateElb | 集群解绑Elb接口。 | To be tested |
|  | CreateClusterDns | 为指定集群申请域名。 | To be tested |
|  | DisassociateEip | 集群解绑Eip。 | To be tested |
|  | ListClusterEndpoints | 查询连接信息。包括公网域名、内网域名等。 | To be tested |
| 逻辑集群管理 | ListLogicalClusterRings | 查询逻辑集群可用ring环节点信息。 | To be tested |
|  | EnableLogicalCluster | 此接口用于切换逻辑集群开关,仅用于控制逻辑集群相关功能模块是否在页面展示。在集群已经是逻辑集群的场景下,修改该接口无任何作用及影响。 | To be tested |
|  | ListLogicalClusterPlans | 此接口用于查询逻辑集群定时增删计划。 | To be tested |
|  | CreateLogicalClusterPlan | 此接口用于添加逻辑集群定时增删计划。 | To be tested |
|  | RestartLogicalCluster | 此接口用于重启逻辑集群。 | To be tested |
|  | ShrinkLogicalCluster | 逻辑集群缩容,支持从弹性池缩容,或是从逻辑集群中缩容。 | To be tested |
|  | ConvertToLogicalCluster | 物理集群转换到逻辑集群。 | To be tested |
|  | ListLogicalClusterVolumes | 查询逻辑集群磁盘信息。 | To be tested |
|  | EnableLogicalClusterPlan | 启用逻辑集群定时增删计划。 | To be tested |
|  | ListLogicalClusters | 查询逻辑集群列表。 | To be tested |
|  | DisableLogicalClusterPlan | 停用逻辑集群定时增删计划。 | To be tested |
|  | DeleteLogicalClusterPlan | 此接口用于删除逻辑集群定时增删计划。 | To be tested |
|  | CreateLogicalCluster | 创建逻辑集群。 | To be tested |
|  | UpdateLogicalCluster | 此接口用于编辑修改逻辑集群。 | To be tested |
|  | DeleteLogicalCluster | 此接口用于删除逻辑集群。 | To be tested |
|  | ListLogicalClusterTasks | 查询逻辑集群任务信息。 | To be tested |
|  | UpdateLogicalClusterPlan | 此接口用于编辑修改编辑逻辑集群增删计划。 | To be tested |
| 配额管理 | ListStatistics | 查询当前可用资源数量,其中包括“可用集群和总集群(个)”、“可用节点和总节点(个)”、“总容量(GB)”。 | To be tested |
|  | ListQuotas | 查询单租户在GaussDB(DWS)服务下的配额信息。 | To be tested |
| 集群管理 | ShowClusters | 该接口用于查询并显示集群列表。 | To be tested |
|  | SaveClusterDescriptionInfo | 修改集群描述信息。 | To be tested |
|  | DeleteDwsCluster | 此接口用于删除集群。集群删除后将释放此集群的所有资源,包括客户数据。为了安全起见,请在删除集群前为这个集群创建快照。 | To be tested |
|  | CreateClusterV2 | 该接口用于创建集群。 | To be tested |
|  | CheckCluster | 创建集群前预检查,提前识别子网不足、配额不足等问题,避免发起创建集群请求后创建失败。 | To be tested |
|  | ShowClusterEncryptInfo | 获取集群加密信息。非加密集群不支持该功能,返回信息为空。 | To be tested |
|  | ListTagsForResource | 查询指定集群的企业项目信息。 | To be tested |
|  | SwitchOverCluster | 当集群状态为“非均衡”时会出现某些节点主实例增多,从而负载压力较大。这种情况下集群状态是正常的,但整体性能要低于均衡状态。可进行集群主备恢复操作将集群状态切换为“可用“状态。 | To be tested |
|  | ShowClusterVolume | 查询租户侧节点磁盘使用情况信息。 | To be tested |
|  | ShowClusterFlavor | 查询集群使用的规格详情。 | To be tested |
|  | ShowResourceStatistics | 该接口用于查询资源统计。 | To be tested |
|  | ModifyClusterTimezone | 修改集群时区。该操作会将操作系统及数据库的时区都进行修改。 | To be tested |
|  | StopCluster | 停止集群。 | To be tested |
|  | ListClusterDetails | 该接口用于查询集群详情。 | To be tested |
|  | ListDssPools | 获取专属分布式存储池列表,只包括用户开通的SSD专属资源池信息。 | To be tested |
|  | ChangeSecurityGroup | 该接口用于修改集群安全组。 | To be tested |
|  | CreateCluster | 该接口用于创建集群。 | To be tested |
|  | ListTopoRings | 查询集群拓扑ring环节点信息。 | To be tested |
|  | RestartCluster | 此接口用于重启集群。 | To be tested |
|  | DeleteCluster | 此接口用于删除集群。集群删除后将释放此集群的所有资源,包括客户数据。为了安全起见,请在删除集群前为这个集群创建快照。 | To be tested |
|  | CancelReadonlyCluster | 当集群进入只读状态时,无法进行数据库相关操作,用户可以在管理控制台解除集群的只读状态。触发只读状态可能是由于磁盘使用率过高,因此需要对集群数据进行清理或扩容。 - 解除只读支持1.7.2及以上版本。 | To be tested |
|  | ResetPassword | 此接口用于重置集群管理员密码。 | To be tested |
|  | ListClusters | 该接口用于查询并显示集群列表。 | To be tested |
|  | EncryptCluster | 转加密集群。 | To be tested |
|  | ListClusterActions | 查询集群任务详情。 | To be tested |
|  | ListNodeTypes | 该接口用于查询所有GaussDB(DWS)服务支持的规格信息。 | To be tested |
|  | ShowInstance | 查询单个实例。 | To be tested |
|  | StartCluster | 启动集群。 | To be tested |
|  | ModifyClusterName | 修改集群名称。 | To be tested |
|  | RotateKey | 轮转加密集群密钥。 | To be tested |
