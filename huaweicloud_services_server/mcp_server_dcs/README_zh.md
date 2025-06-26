# DCS MCP Server 


## Version
v0.1.0

## Overview

DCS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DCS. Full-chain management of DCS resources can be carried out based on natural language.

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
                    <td rowspan="2">IP白名单管理</td>
                    <td>ShowIpWhitelist</td>
                    <td>查询指定实例的IP白名单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIpWhitelist</td>
                    <td>为指定实例设置IP白名单分组,包含创建、停用、编辑、删除白名单四个功能</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">会话管理</td>
                    <td>HangUpKillAllClients</td>
                    <td>下发kill指定节点或实例的全部会话任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClients</td>
                    <td>获取会话列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>HangUpClients</td>
                    <td>kill指定的会话</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ScanClients</td>
                    <td>下发查询会话列表任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">其他接口</td>
                    <td>ListMonitoredObjects</td>
                    <td>查询主维度对象列表,主维度ID当前支持dcs_instance_id,dcs_memcached_instance_id。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowQuotaOfTenant</td>
                    <td>查询租户默认可以创建的实例数和总内存的配额限制,以及可以申请配额的最大值和最小值。不同的租户在不同的区域配额可能不同。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCommandMobilization</td>
                    <td>登入web-cli,执行redis命令</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMaintenanceWindows</td>
                    <td>查询维护时间窗开始时间和结束时间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LoginWebCli</td>
                    <td>登录webCli</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMonitoredObjectsOfInstance</td>
                    <td>查询主维度下子维度监控对象列表,当前支持子维度的主维度ID的有 dcs_instance_id</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableZones</td>
                    <td>在创建实例时,需要配置实例所在的可用区ID,可通过该接口查询可用区的ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LogoffWebCli</td>
                    <td>登出webCli</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">分片与副本</td>
                    <td>DeleteIpFromDomainName</td>
                    <td>将只读副本的IP从域名中摘除,摘除成功后,只读域名不会再解析到该副本IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowNodesInformation</td>
                    <td>批量查询指定项目所有实例的节点信息、有效实例个数及节点个数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGroupReplicationInfo</td>
                    <td>查询读写分离实例和集群实例的分片和副本信息,其中,读写分离实例仅Redis4.0和Redis5.0的主备实例支持。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNodesInformation</td>
                    <td>查询指定实例的节点信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSlavePriority</td>
                    <td>设置副本优先级,主节点故障时,权重越小的备节点切换为主节点的优先级越高。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReplicationStates</td>
                    <td>获取副本状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">参数管理</td>
                    <td>UpdateConfigurations</td>
                    <td>为了确保分布式缓存服务发挥出最优性能,您可以根据自己的业务情况对DCS缓存实例的运行参数进行调整。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConfig</td>
                    <td>为了确保分布式缓存服务发挥出最优性能,您可以根据自己的业务情况对DCS缓存实例的运行参数进行调整。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigHistories</td>
                    <td>查询实例的参数修改记录列表,支持按照关键字查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">参数配置</td>
                    <td>ListConfigurations</td>
                    <td>获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">后台任务管理</td>
                    <td>ExportExcelJob</td>
                    <td>查询实例列表导出任务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackgroundTask</td>
                    <td>删除后台任务管理中的指定记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackgroundTask</td>
                    <td>查询后台任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstanceResizeCheckJob</td>
                    <td>提交前置检查任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCenterTask</td>
                    <td>查询任务中心任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackgroundTaskProgress</td>
                    <td>查询后台任务详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobInfo</td>
                    <td>查询租户Job执行结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCenterTask</td>
                    <td>删除任务中心任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">备份与恢复</td>
                    <td>ListBackupRecords</td>
                    <td>查询指定缓存实例的备份信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyInstance</td>
                    <td>备份指定的缓存实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackupFile</td>
                    <td>删除缓存实例已备份的文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreRecords</td>
                    <td>查询指定缓存实例的恢复记录列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackupFileLinks</td>
                    <td>获取指定实例的备份文件下载链接,下载备份文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">备份管理</td>
                    <td>RestoreInstance</td>
                    <td>备份恢复到当前实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="22">实例管理</td>
                    <td>UpdatePassword</td>
                    <td>修改缓存实例的密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateAz</td>
                    <td>实例可用区迁移。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClientIpTransparentTransmission</td>
                    <td>开启或关闭客户端ip透传</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBandwidths</td>
                    <td>获取实例各个分片带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceTopology</td>
                    <td>查询集群实例拓扑关系图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartOrFlushInstances</td>
                    <td>重启运行中的DCS缓存实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceBandwidth</td>
                    <td>变更指定实例的带宽</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNumberOfInstancesInDifferentStatus</td>
                    <td>查询该租户在当前区域下不同状态的实例数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeInstanceMinorVersion</td>
                    <td>升级实例小版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceVersion</td>
                    <td>获取对应实例内核版本号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeNodesStartStopStatus</td>
                    <td>实例节点启停。执行节点关机操作前的24小时内,需要对实例(单机实例除外)进行数据备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstanceBandwidthAutoScalingPolicy</td>
                    <td>删除实例带宽弹性伸缩策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportInstancesTask</td>
                    <td>异步导出实例资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStatisticsOfRunningInstances</td>
                    <td>查询当前租户下处于“运行中”状态的缓存实例的统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPassword</td>
                    <td>重置密码(只针对开通SSL的实例)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceBandwidthAutoScalingPolicy</td>
                    <td>更新实例带宽弹性伸缩策略。暂不支持实例带宽自动回缩。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeMasterStandby</td>
                    <td>切换实例主备节点,只有主备实例支持该操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeMasterStandbyAsync</td>
                    <td>异步交换实例主备节点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigHistoryDetail</td>
                    <td>查询实例参数修改记录详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteClusterSwitchover</td>
                    <td>集群分片倒换,适用于proxy和cluster实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceOperations</td>
                    <td>查询实例是否可以扩容</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceBandwidthAutoScalingPolicy</td>
                    <td>查询实例带宽弹性伸缩策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">实例诊断</td>
                    <td>CreateDiagnosisTask</td>
                    <td>诊断指定的缓存实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDiagnosisTask</td>
                    <td>删除诊断记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDiagnosisTaskDetails</td>
                    <td>通过报告ID查询诊断报告的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDiagnosisTasks</td>
                    <td>查询指定缓存实例诊断任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">带宽</td>
                    <td>UpdateBandwidth</td>
                    <td>更新带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">引擎版本和规格</td>
                    <td>ListFlavors</td>
                    <td>查询数据库规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">弹性公网IP</td>
                    <td>UpdatePublicIp</td>
                    <td>更新弹性公网IP的信息,主要用于解绑和绑定EIP和VIP之间的关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePublicIp</td>
                    <td>根据弹性公网IP的ID,删除对应的弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">数据迁移</td>
                    <td>StopMigrationTask</td>
                    <td>停止数据迁移任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMigrationTask</td>
                    <td>创建数据迁移任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopMigrationTaskSync</td>
                    <td>同步停止数据迁移任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMigrationTask</td>
                    <td>删除数据迁移任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMigrationTask</td>
                    <td>查询迁移任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRestartOnlineMigrationTasks</td>
                    <td>批量重启在线迁移任务,接口响应成功,返回重启在线迁移任务下发结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetOnlineMigrationTask</td>
                    <td>配置在线数据迁移任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMigrationTaskStats</td>
                    <td>查询在线迁移进度明细。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollbackExchangeInstanceIp</td>
                    <td>IP交换回滚。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMigrationTask</td>
                    <td>设置迁移任务自动重连</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExchangeInstanceIp</td>
                    <td>进行IP交换</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopMigrationTasks</td>
                    <td>批量停止数据迁移任务,接口响应成功,仅表示下发任务成功。查询到迁移任务状态为TERMINATED时,即停止成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMigrationTaskLogs</td>
                    <td>查询迁移日志列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMigrationTask</td>
                    <td>查询迁移任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOnlineMigrationTask</td>
                    <td>创建在线数据迁移任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">日志管理</td>
                    <td>CreateRedislogDownloadLink</td>
                    <td>获取日志下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowlog</td>
                    <td>查询慢日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRedislog</td>
                    <td>采集Redis运行日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRedislog</td>
                    <td>查询Redis运行日志列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">标签管理</td>
                    <td>ListTagsOfTenant</td>
                    <td>查询租户在指定Project中实例类型的所有资源标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTags</td>
                    <td>通过实例ID查询标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">模板管理</td>
                    <td>CreateCustomTemplate</td>
                    <td>创建自定义模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigTemplate</td>
                    <td>查询参数模板详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConfigTemplate</td>
                    <td>删除自定义模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigTemplates</td>
                    <td>查询租户的参数模板列表,支持按照条件查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfigTemplate</td>
                    <td>修改自定义模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">独享实例管理</td>
                    <td>CreateInstance</td>
                    <td>创建WAF独享引擎实例。独享模式支持的局点包括:华东-青岛、中东-利雅得、华北-北京一、华北-北京四、华北-乌兰察布一、华东-上海一、华东-上海二、华南-广州、华南-深圳、中国-香港、西南-贵阳一、亚太-曼谷、 亚太-新加坡、非洲约翰内斯堡、土耳其-伊斯坦布尔;普通租户类独享支持的局点:华北-北京四、华东-上海一、华南-广州、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>查询WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">生命周期管理</td>
                    <td>UpdateInstance</td>
                    <td>修改实例的名称和描述信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResizeOrder</td>
                    <td>包周期实例变更规格</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteInstances</td>
                    <td>批量删除实例。**实例删除后,实例中原有的数据将被删除,且没有备份,请谨慎操作。**</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateDeletableReplica</td>
                    <td>校验集群副本是否支持删除</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>查询租户的实例列表,支持按照条件查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSingleInstance</td>
                    <td>删除指定的缓存实例,释放该实例的所有资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">离线全量key分析</td>
                    <td>CreateOfflineKeyAnalysis</td>
                    <td>创建离线全量key分析任务。离线全量key分析用于分析实例指定节点备份文件中的TOP100大key,每种数据类型前缀数量TOP50的key和每种数据类型key的内存占用和数量的分布情况。仅Redis 4.0、5.0、6.0版本及Redis企业版实例支持。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOfflineKeyAnalysisTask</td>
                    <td>查询离线全量key分析详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOfflineKeyAnalysisTask</td>
                    <td>查询离线全量key分析任务列表,支持Redis4.0、5.0、6.0版本及Redis企业版。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOfflineKeyAnalysisTask</td>
                    <td>删除离线全量key分析记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="18">缓存分析</td>
                    <td>UpdateExpireAutoScanConfig</td>
                    <td>修改自动扫描配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadHotKey</td>
                    <td>下载热key。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBigkeyAutoscanConfig</td>
                    <td>查询大key自动分析配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHotkeyAutoscanConfig</td>
                    <td>查询热key自动分析配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHotkeyTaskDetails</td>
                    <td>查询热key分析详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBigkeyScanTask</td>
                    <td>为Redis实例创建大key分析任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHotkeyScanTask</td>
                    <td>创建热key分析任务,Redis 3.0 不支持热key分析。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHotkeyAutoScanConfig</td>
                    <td>设置热key自动分析配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowExpireKeyScanInfo</td>
                    <td>查询过期Key扫描记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHotKeyScanTasks</td>
                    <td>查询热key分析历史记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBigkeyScanTasks</td>
                    <td>查询大key分析任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowExpireAutoScanConfig</td>
                    <td>查询自动扫描配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBigkeyAutoscanConfig</td>
                    <td>设置大key自动分析配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBigkeyScanTask</td>
                    <td>删除大key分析记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBigkeyScanTaskDetails</td>
                    <td>查询大key分析详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ScanExpireKey</td>
                    <td>立刻扫描过期Key</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHotkeyScanTask</td>
                    <td>删除热key分析任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutoExpireScanTask</td>
                    <td>创建过期key扫描任务(Redis 3.0 不支持过期key扫描)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">网络安全</td>
                    <td>UpdateSslSwitch</td>
                    <td>开启/关闭SSL。该接口目前仅针对Redis 6.0基础版版本实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIpWhitelistAsync</td>
                    <td>为指定实例设置IP白名单分组,包含创建、停用、编辑、删除白名单四个功能。返回异步任务jobId,设置白名单分组信息会覆盖掉已有的白名单信息,因此在新增IP白名单分组时,需保留已有的白名单信息后再编辑新的白名单分组信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadSslCert</td>
                    <td>下载实例SSL证书。该接口目前仅针对Redis 6.0基础版版本实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceSslDetail</td>
                    <td>查询实例SSL信息。该接口目前仅针对Redis 6.0基础版版本实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">规格变更管理</td>
                    <td>ResizeInstance</td>
                    <td>实例规格变更。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">证书标签管理</td>
                    <td>BatchCreateOrDeleteTags</td>
                    <td>批量创建或删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">账号管理</td>
                    <td>CreateAclAccount</td>
                    <td>"为redis4.0/5.0实例(Cluster集群实例除外)创建权限访问账号,包含读写和只读权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAclAccountRemark</td>
                    <td>ACL账号修改备注</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAclAccount</td>
                    <td>修改用户的类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAclAccounts</td>
                    <td>查询ACL账户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAclAccountPassWord</td>
                    <td>修改ACL账号密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAclAccount</td>
                    <td>删除所创建的ACL普通账号</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetAclAccountPassWord</td>
                    <td>重置ACL账号密码。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
