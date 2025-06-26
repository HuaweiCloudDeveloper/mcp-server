# RDS MCP Server 


## Version
v0.1.0

## Overview

RDS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RDS. Full-chain management of RDS resources can be carried out based on natural language.

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
                    <td rowspan="1">OpenStack - API版本信息</td>
                    <td>ListApiVersion</td>
                    <td>返回当前API所有可用的版本(仅针对OpenStack原生接口)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>查询租户在指定项目中指定资源类型下的所有标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">任务管理</td>
                    <td>DeleteJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobInfo</td>
                    <td>获取指定ID的任务信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobInfoDetail</td>
                    <td>获取指定实例和时间范围的任务信息(SQL Server)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">参数配置</td>
                    <td>ShowInstanceConfiguration</td>
                    <td>获取指定实例的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceParamHistories</td>
                    <td>实例参数修改历史。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableConfiguration</td>
                    <td>应用参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurations</td>
                    <td>获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConfiguration</td>
                    <td>创建参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfiguration</td>
                    <td>获取指定参数模板的参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyConfiguration</td>
                    <td>复制参数模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConfigurationAsync</td>
                    <td>修改指定实例的参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfiguration</td>
                    <td>修改参数模板参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConfiguration</td>
                    <td>删除参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConfiguration</td>
                    <td>修改指定实例的参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplyConfigurationAsync</td>
                    <td>应用参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">回收站</td>
                    <td>ShowRecyclePolicy</td>
                    <td>查询回收站的回收策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecycleInstances</td>
                    <td>查询回收站实例信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartRecyclePolicy</td>
                    <td>设置回收站策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="29">备份与恢复</td>
                    <td>BatchRestorePostgreSqlTables</td>
                    <td>表级时间点恢复(PostgreSQL)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHistoryDatabase</td>
                    <td>查询指定时间点可恢复的库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreExistInstance</td>
                    <td>恢复到已有实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupDownloadLink</td>
                    <td>获取备份下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpdateBackupEnhancePolicy</td>
                    <td>查询高级备份策略,可查看自定义稀疏备份等</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOffSiteBackups</td>
                    <td>查询跨区域备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIncreBackupPolicy1</td>
                    <td>修改增备策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteManualBackup</td>
                    <td>删除手动备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupPolicy</td>
                    <td>查询自动备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteManualBackup</td>
                    <td>批量删除手动备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOffSiteBackupPolicy</td>
                    <td>查询跨区域备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesSupportFastRestore</td>
                    <td>批量获取实例是否能在库表恢复时使用极速恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListShareBackups</td>
                    <td>查询共享备份列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIncreBackupPolicy1</td>
                    <td>获取增备策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOffSiteRestoreTimes</td>
                    <td>查询跨区域备份可恢复时间段。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreToExistingInstance</td>
                    <td>恢复到已有实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRestoreDatabase</td>
                    <td>库级时间点恢复</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreTablesNew</td>
                    <td>表级时间点恢复(MySQL)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBackupPolicy</td>
                    <td>设置自动备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatabaseLevelDatabase</td>
                    <td>查询库级备份包含的库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreTimes</td>
                    <td>查询可恢复时间段。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateManualBackup</td>
                    <td>创建手动备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackups</td>
                    <td>获取备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPostgresqlListHistoryTables</td>
                    <td>查询指定时间点可恢复的表(PostgreSQL)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOffSiteInstances</td>
                    <td>查询跨区域备份实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreTables</td>
                    <td>表级时间点恢复(MySQL)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRestoreInstance</td>
                    <td>恢复到新实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetOffSiteBackupPolicy</td>
                    <td>设置跨区域备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopBackup</td>
                    <td>停止创建备份</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="61">实例管理</td>
                    <td>UpgradeDbVersionNew</td>
                    <td>对实例进行小版本升级。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartFailover</td>
                    <td>手动倒换主备.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoUpgradePolicy</td>
                    <td>查询实例内核小版本自动升级策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpgradeHistories</td>
                    <td>查询实例大版本升级历史信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlLimit</td>
                    <td>查询SQL限流列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeDbVersion</td>
                    <td>对实例进行小版本升级。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceName</td>
                    <td>修改实例名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlavorsResize</td>
                    <td>查询数据库可变更规格接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateFollower</td>
                    <td>迁移主备实例的备机</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDnsName</td>
                    <td>查询实例ipv6域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopInstance</td>
                    <td>批量停止实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnlockNodeReadonlyStatus</td>
                    <td>解除节点只读状态接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetAutoUpgradePolicy</td>
                    <td>设置实例内核小版本自动升级策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateToPeriod</td>
                    <td>RDS实例按需转包周期</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeDbMajorVersion</td>
                    <td>PostgreSQL数据库升级大版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReadOnlyReplayDatabase</td>
                    <td>查询只读实例可恢复到主实例的库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSqlLimit</td>
                    <td>修改SQL限流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartResizeFlavorAction</td>
                    <td>变更数据库实例的规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePostgresqlHbaConf</td>
                    <td>删除pg_hba.conf文件的单个或多个配置,以priority做唯一标识</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeFailoverMode</td>
                    <td>更改主备实例的数据同步方式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceSingleToHaAction</td>
                    <td>单机转主备实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStorageUsedSpace</td>
                    <td>查询实例磁盘空间使用量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceReduceVolumeAction</td>
                    <td>数据库实例的磁盘空间缩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceEnlargeVolumeAction</td>
                    <td>扩容数据库实例的磁盘空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopInstance</td>
                    <td>实例进行关机,通过暂时停止按需实例以节省费用,实例默认停止七天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePostgresqlInstanceAlias</td>
                    <td>修改指定数据库实例的备注信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetSecondLevelMonitor</td>
                    <td>设置实例秒级监控策略,约五分钟后生效,对于1秒监控和5秒监控,计费方式为按需付费(每小时扣费一次)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAvailableVersion</td>
                    <td>查询实例可升级的目标版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInspectionHistories</td>
                    <td>查询实例大版本升级检查历史。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPostgresqlHbaInfo</td>
                    <td>查询实例的pg_hba.conf文件配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReplicationStatus</td>
                    <td>获取实例的复制状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeFailoverStrategy</td>
                    <td>切换主备实例的倒换策略.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeOpsWindow</td>
                    <td>设置可维护时间段</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVolumeInfo</td>
                    <td>查询实例的磁盘信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoEnlargePolicy</td>
                    <td>查询实例存储空间自动扩容策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartupInstance</td>
                    <td>停止实例以节省费用,在停止数据库实例后,支持手动重新开启实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddPostgresqlHbaConf</td>
                    <td>以传入配置全量覆盖当前pg_hba.conf文件内容,入参为空时用默认配置覆盖当前文件内容</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecondLevelMonitoring</td>
                    <td>查询实例秒级监控策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEngineFlavors</td>
                    <td>查询实例可变更规格</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceRestartAction</td>
                    <td>重启数据库实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlLimit</td>
                    <td>删除SQL限流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesInfoDiagnosis</td>
                    <td>获取指定诊断项的诊断结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlLimit</td>
                    <td>新增SQL限流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainName</td>
                    <td>查询实例ipv4域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceIam5</td>
                    <td>创建数据库实例V5接口,仅支持IAM5的新平面认证方式(AK/SK认证方式)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyPostgresqlHbaConf</td>
                    <td>修改/新增pg_hba.conf文件的单个或多个配置,以priority做唯一标识,priority不存在的新增,存在的修改</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceDiagnosis</td>
                    <td>获取诊断后的实例数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDnsName</td>
                    <td>申请域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTdeStatus</td>
                    <td>sqlserverTDE开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTdeStatus</td>
                    <td>根据实例id查询sqlserver TDE状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDnsName</td>
                    <td>修改域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeDbMajorVersionPreCheck</td>
                    <td>大版本升级前进行升级检查。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeDbMajorVersionStatus</td>
                    <td>查询大版本检查状态或升级状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetAutoEnlargePolicy</td>
                    <td>设置实例存储空间自动扩容策略,按扩容量扣除存储费用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachEip</td>
                    <td>绑定和解绑弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPostgresqlHbaInfoHistory</td>
                    <td>查询实例的pg_hba.conf文件修改历史</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCollations</td>
                    <td>查询SQLServer可用字符集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchSqlLimit</td>
                    <td>开启/关闭/禁用所有SQL限流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSslCertDownloadLink</td>
                    <td>获取SSL证书下载地址</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSimplifiedInstances</td>
                    <td>获取指定实例详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreLogReplayDatabase</td>
                    <td>延迟库只读,恢复库到主实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">引擎版本和规格</td>
                    <td>ListStorageTypes</td>
                    <td>查询数据库磁盘类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlavors</td>
                    <td>查询数据库规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatastores</td>
                    <td>查询数据库引擎的版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">数据库代理</td>
                    <td>ListRdSforMysqlProxyFlavors</td>
                    <td>查询数据库代理规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRdSforMySqlProxy</td>
                    <td>关闭数据库代理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetInstancesProxyRestart</td>
                    <td>重启数据库代理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRdSforMySqlProxy</td>
                    <td>查询数据库代理信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRdSforMySqlProxy</td>
                    <td>开启数据库代理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyRdSforMySqlProxyRouteMode</td>
                    <td>设置读写分离路由模式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">数据库代理(PostgreSQL)</td>
                    <td>ChangeProxyScale</td>
                    <td>数据库代理实例进行规格变更。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInformationAboutDatabaseProxy</td>
                    <td>查询指定实例的数据库代理详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchQueryScaleFlavors</td>
                    <td>查询数据库代理可变更的规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchQueryScaleComputeFlavors</td>
                    <td>查询数据库代理可变更的规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartDatabaseProxy</td>
                    <td>为指定实例开启数据库代理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateReadWeight</td>
                    <td>修改指定实例的读写分离权重。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeTheDelayThreshold</td>
                    <td>修改指定实例的读写分离延时阈值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopDatabaseProxy</td>
                    <td>为指定实例关闭数据库代理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">数据库安全性</td>
                    <td>SetSecurityGroup</td>
                    <td>修改安全组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchSsl</td>
                    <td>设置SSL数据加密。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataIp</td>
                    <td>修改内网地址</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">日志</td>
                    <td>ListErrorlogForLts</td>
                    <td>查询实例的错误日志数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetLogLtsConfigs</td>
                    <td>关联LTS配置信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogLtsConfigs</td>
                    <td>获取LTS配置信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowLogStatisticsForLts</td>
                    <td>查询实例慢日志的统计数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogLtsConfigs</td>
                    <td>解除LTS配置信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowlogForLts</td>
                    <td>查询实例的慢日志数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询API版本</td>
                    <td>ListApiVersionNew</td>
                    <td>查询API版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询版本操作</td>
                    <td>ShowApiVersion</td>
                    <td>查询指定的标签管理服务API版本号详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">标签管理</td>
                    <td>BatchTagDelAction</td>
                    <td>批量删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchTagAddAction</td>
                    <td>批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceTags</td>
                    <td>查询实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPredefinedTag</td>
                    <td>查询预定义标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">灾备实例</td>
                    <td>ListDrInfos</td>
                    <td>查询容灾管理列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDrRelations</td>
                    <td>批量查询容灾实例信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceMasterDrAction</td>
                    <td>建立跨云容灾关系时配置主实例的容灾能力。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDisasterRecovery</td>
                    <td>解除实例容灾关系接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceDrToMasterAction</td>
                    <td>实例间建立的跨云容灾关系出现异常后,将灾备实例升级为主实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceSlaveDrAction</td>
                    <td>实例建立跨云容灾关系时配置灾备实例的容灾能力。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDrReplicaStatus</td>
                    <td>建立跨云容灾关系后,查询主实例和灾备实例间的复制状态及延迟。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">独享实例管理</td>
                    <td>CreateInstance</td>
                    <td>创建WAF独享引擎实例。独享模式支持的局点包括:华东-青岛、中东-利雅得、华北-北京一、华北-北京四、华北-乌兰察布一、华东-上海一、华东-上海二、华南-广州、华南-深圳、中国-香港、西南-贵阳一、亚太-曼谷、 亚太-新加坡、非洲约翰内斯堡、土耳其-伊斯坦布尔;普通租户类独享支持的局点:华北-北京四、华东-上海一、华南-广州、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>删除WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">生命周期管理</td>
                    <td>ListInstances</td>
                    <td>查询租户的实例列表,支持按照条件查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">端口</td>
                    <td>UpdatePort</td>
                    <td>更新端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">管理数据库和用户(MySQL)</td>
                    <td>ResetPwd</td>
                    <td>重置数据库密码.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuthorizedDatabases</td>
                    <td>查询指定用户的已授权数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDbUser</td>
                    <td>删除数据库用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDatabase</td>
                    <td>修改指定实例中的数据库备注。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabase</td>
                    <td>删除数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDbUser</td>
                    <td>在指定实例中创建数据库帐号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbUsers</td>
                    <td>查询数据库用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetDbUserPwd</td>
                    <td>设置数据库账号密码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHostPrivilege</td>
                    <td>修改实例下用户host信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDbUserComment</td>
                    <td>修改数据库用户名备注</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuthorizedDbUsers</td>
                    <td>查询指定数据库的已授权用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Revoke</td>
                    <td>解除数据库帐号权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabase</td>
                    <td>创建数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetReadOnlySwitch</td>
                    <td>根据业务需求,设置数据库用户只读</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowDbUserPrivilege</td>
                    <td>授权数据库帐号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabases</td>
                    <td>查询数据库列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="25">管理数据库和用户(PostgreSQL)</td>
                    <td>ListPostgresqlExtension</td>
                    <td>获取指定数据库的插件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteRevokeDatabaseUserRole</td>
                    <td>撤回用户角色</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDatabaseOwner</td>
                    <td>修改数据库owner</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokePostgresqlDbPrivilege</td>
                    <td>解除数据库帐号权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDbUserPrivilege</td>
                    <td>数据库帐号授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostgresqlDbUser</td>
                    <td>在指定实例中创建数据库用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPostgresqlDbUserPaginated</td>
                    <td>在指定实例中查询数据库用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostgresqlDatabaseSchema</td>
                    <td>在指定实例的数据库中, 创建数据库schema。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPostgresqlDatabases</td>
                    <td>查询指定实例中的数据库列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPostgresqlDatabaseSchemas</td>
                    <td>查询指定实例的数据库SCHEMA列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetPostgresqlDbUserPwd</td>
                    <td>重置指定数据库帐号的密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostgresqlExtension</td>
                    <td>在指定数据库上创建插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePostgresqlDbUserComment</td>
                    <td>修改数据库用户名备注</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePostgresqlDatabase</td>
                    <td>删除数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePostgresqlExtension</td>
                    <td>在指定数据库上删除插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetDatabaseUserPrivilege</td>
                    <td>设置数据库用户权限:只读或可读写。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePostgresqlDbUser</td>
                    <td>删除数据库用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowDbPrivilege</td>
                    <td>在指定实例的数据库中, 设置帐号的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPostgresqlParamValue</td>
                    <td>获取实例指定参数的值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePostgresqlParameterValue</td>
                    <td>修改实例指定参数的值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostgresqlDatabase</td>
                    <td>在指定实例中创建数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseUserRole</td>
                    <td>查询数据库角色信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePostgresqlExtension</td>
                    <td>在指定数据库上更新插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecutePrivilegeDatabaseUserRole</td>
                    <td>授予用户角色</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePostgresqlDatabase</td>
                    <td>修改指定实例中的数据库备注。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">管理数据库和用户(SQL Server)</td>
                    <td>ListAuthorizedSqlserverDbUsers</td>
                    <td>查询指定数据库的已授权用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlserverDatabase</td>
                    <td>创建数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlserverDbUser</td>
                    <td>删除数据库用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMsdtcLocalHost</td>
                    <td>删除MSDTC相关主机host地址</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetInstancesDbShrink</td>
                    <td>收缩数据库日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlserverDatabase</td>
                    <td>删除数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMsdtcHosts</td>
                    <td>查询MSDTC的hosts信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlserverDbUsers</td>
                    <td>查询数据库用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyCollation</td>
                    <td>修改实例字符集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddMsdtcs</td>
                    <td>添加MSDTC相关主机host地址</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlserverDatabaseEx</td>
                    <td>删除数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlserverDatabases</td>
                    <td>查询数据库列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlserverDbUser</td>
                    <td>创建数据库用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeSqlserverDbUserPrivilege</td>
                    <td>解除数据库帐号权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowSqlserverDbUserPrivilege</td>
                    <td>授权数据库帐号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyDatabase</td>
                    <td>复制数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetInstancesNewDbShrink</td>
                    <td>收缩数据库日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">获取扩展日志下载信息</td>
                    <td>CreateXelLogDownload</td>
                    <td>获取扩展日志下载信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">获取扩展日志文件列表</td>
                    <td>ListXellogFiles</td>
                    <td>查询扩展日志文件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">获取日志信息</td>
                    <td>DownloadSlowlog</td>
                    <td>获取慢日志下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowLogs</td>
                    <td>查询数据库慢日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowLogsNew</td>
                    <td>查询数据库慢日志。(与原v3接口相比修改offset,符合华为云服务开放 API遵从性规范3.0)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetSensitiveSlowLog</td>
                    <td>V3慢日志敏感信息的开关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetAuditlogPolicy</td>
                    <td>设置审计日志策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListErrorLogsNew</td>
                    <td>查询数据库错误日志。(与原v3接口相比修改offset,符合华为云服务开放 API遵从性规范3.0)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditlogs</td>
                    <td>获取审计日志列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBinlogClearPolicy</td>
                    <td>查寻指定实例的binlog本地保留时长。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBinlogClearPolicy</td>
                    <td>修改指定实例的binlog本地保留时长。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowlogStatistics</td>
                    <td>获取慢日志统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAuditlogPolicy</td>
                    <td>查询审计日志策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListErrorLogs</td>
                    <td>查询数据库错误日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadErrorlog</td>
                    <td>获取错误日志下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowLogFile</td>
                    <td>查询慢日志文件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAuditlogDownloadLink</td>
                    <td>生成审计日志下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">配置只读延迟库(PostgreSQL)</td>
                    <td>SwitchLogReplay</td>
                    <td>中止/恢复wal日志回放</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecoveryTimeWindow</td>
                    <td>查询wal日志恢复时间窗</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReplayDelayStatus</td>
                    <td>获取wal日志延迟回放状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowQuotas</td>
                    <td>查询当前项目下资源配额情况。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
