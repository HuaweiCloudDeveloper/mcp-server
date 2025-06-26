# DWS MCP Server 


## Version
v0.1.0

## Overview

DWS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DWS. Full-chain management of DWS resources can be carried out based on natural language.

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
                    <td rowspan="1">ClusterManagement</td>
                    <td>ShrinkCluster</td>
                    <td>对MRS集群进行缩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query</td>
                    <td>ListSchemas</td>
                    <td>List Schemas</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">VpnGateway</td>
                    <td>ListAvailabilityZones</td>
                    <td>查询VPN网关可用区</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">主机监控</td>
                    <td>ListMonitorIndicators</td>
                    <td>查询性能监控指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetrics</td>
                    <td>查询集群使用指标列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueries</td>
                    <td>该接口用于查询实时SQL列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetricsData</td>
                    <td>获取指定指标相关采集数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostDisk</td>
                    <td>openApi查询磁盘信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostOverview</td>
                    <td>openApi查询主机概览。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMonitorIndicatorData</td>
                    <td>openApi查询历史监控数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowQueryDetail</td>
                    <td>查询SQL执行信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostNet</td>
                    <td>openapi获取网卡状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTablesStatistic</td>
                    <td>该接口用于查询表倾斜或脏页率信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">事件管理</td>
                    <td>DeleteEventSub</td>
                    <td>删除订阅的事件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEventSub</td>
                    <td>添加订阅的事件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventSubs</td>
                    <td>查询订阅的事件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventSpecs</td>
                    <td>查询事件配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEventSub</td>
                    <td>更新订阅事件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">云硬盘快照</td>
                    <td>ListSnapshots</td>
                    <td>查询云硬盘快照详细列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSnapshot</td>
                    <td>创建云硬盘快照。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSnapshot</td>
                    <td>删除云硬盘快照。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">任务管理</td>
                    <td>ListJobDetails</td>
                    <td>查询任务进度信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">函数日志</td>
                    <td>EnableLtsLogs</td>
                    <td>开通lts日志上报功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">函数测试事件</td>
                    <td>ListEvents</td>
                    <td>获取指定函数的测试事件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">升级管理</td>
                    <td>UpdateMaintenanceWindow</td>
                    <td>您可以根据业务需求,设置可维护时间段。建议将可维护时间段设置在业务低峰期,避免业务在维护过程中异常中断。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpdatableVersion</td>
                    <td>获取集群可升级的目标版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteClusterUpgradeAction</td>
                    <td>下发集群升级相关操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpdateRecord</td>
                    <td>通过此接口获取当前集群升级记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">参数配置</td>
                    <td>ListClusterConfigurationsParameter</td>
                    <td>查询集群所关联的参数组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfiguration</td>
                    <td>修改参数模板参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurationsAuditRecords</td>
                    <td>查询参数修改审计记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterConfigurations</td>
                    <td>查询集群所关联的参数组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">告警管理</td>
                    <td>UpdateAlarmSub</td>
                    <td>更新订阅的告警。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmStatistic</td>
                    <td>查询告警统计。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmConfigs</td>
                    <td>查询告警配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlarmSub</td>
                    <td>删除订阅的告警。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmSubs</td>
                    <td>查询订阅告警。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlarmSub</td>
                    <td>创建告警订阅。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmDetail</td>
                    <td>查询告警详情列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">安全总览</td>
                    <td>ListStatistics</td>
                    <td>查询安全总览请求与攻击数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">实例管理</td>
                    <td>ResetPassword</td>
                    <td>重置密码(只针对开通SSL的实例)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">审计日志</td>
                    <td>ListAuditLog</td>
                    <td>查询审计日志记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">容灾管理</td>
                    <td>ListAvailableDisasterClusters</td>
                    <td>该接口用于查询可用的容灾集群列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDisasterInfo</td>
                    <td>该接口用于更新容灾配置操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartDisasterRecovery</td>
                    <td>该接口用于启动容灾操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDisasterDetail</td>
                    <td>该接口用于查询单个容灾详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDisasterProgress</td>
                    <td>该接口用于查询容灾进度详情信息操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDisasterRecovery</td>
                    <td>该接口用于创建集群间容灾。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PauseDisasterRecovery</td>
                    <td>该接口用于停止容灾操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDisasterRecover</td>
                    <td>该接口用于查询容灾列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchoverDisasterRecovery</td>
                    <td>该接口用于容灾进行灾备切换操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckDisasterName</td>
                    <td>该接口用于查询容灾名称是否可用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreDisaster</td>
                    <td>该接口用于主备集群进行异常切换,备集群恢复可用状态后进行的容灾恢复操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchFailoverDisaster</td>
                    <td>该接口用于容灾异常场景下进行主备集群切换操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">快照管理</td>
                    <td>ListSnapshotDetails</td>
                    <td>该接口用于使用快照ID查询快照详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreCluster</td>
                    <td>该接口用于使用快照恢复集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddSnapshotCrossRegionPolicy</td>
                    <td>该接口用于设置跨区域备份配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshotCrossRegion</td>
                    <td>该接口用于获取跨区域快照可用局点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSnapshotPolicy</td>
                    <td>该接口用于删除一个快照策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckTableRestore</td>
                    <td>该接口用于用户恢复表名检测。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterSnapshots</td>
                    <td>该接口用于查询集群快照列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshotStatistics</td>
                    <td>快照统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopySnapshot</td>
                    <td>该接口用于复制一个自动快照。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSnapshotPolicy</td>
                    <td>该接口用于设置快照策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSnapshotCrossRegionPolicy</td>
                    <td>该接口用于删除跨区域备份配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshotCrossRegionPolicy</td>
                    <td>该接口用于查询所有跨区域快照配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreTable</td>
                    <td>该接口用于恢复表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshotPolicy</td>
                    <td>查询快照策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">数据库权限管理</td>
                    <td>UpdateDatabaseAuthority</td>
                    <td>修改数据库对象权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseUsers</td>
                    <td>查询所有数据库用户/角色。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseUserAuthorities</td>
                    <td>查询用户/角色拥有权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatabaseAuthority</td>
                    <td>查询数据库对象权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteDatabaseOmUserAction</td>
                    <td>进行数据库运维账户操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatabaseUser</td>
                    <td>查询指定用户信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncIamUsers</td>
                    <td>同步IAM用户到数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportUserAuthority</td>
                    <td>导出数据库用户/角色的权限列表,接口返回的是输出流,xlsx文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabaseUser</td>
                    <td>创建数据库用户/角色。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDatabaseUserInfo</td>
                    <td>修改指定用户信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatabaseOmUserStatus</td>
                    <td>获得数据库运维账户状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabaseUser</td>
                    <td>删除数据库用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSyncRecords</td>
                    <td>查询身份源同步记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportDatabaseUsers</td>
                    <td>导出数据库用户/角色,接口返回的是输出流,xlsx文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">数据源</td>
                    <td>ListDataSource</td>
                    <td>该接口用于查询数据源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">数据源管理</td>
                    <td>DeleteDataSource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataSource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataSource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">日志管理</td>
                    <td>DisableLtsLogs</td>
                    <td>该接口用于关闭集群LTS云日志服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLtsLogs</td>
                    <td>获取LTS日志列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">标签管理</td>
                    <td>BatchCreateResourceTag</td>
                    <td>为指定集群批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteResourceTag</td>
                    <td>为指定集群批量删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">标签管理接口</td>
                    <td>ListClusterTags</td>
                    <td>查询指定集群的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">灾备实例</td>
                    <td>DeleteDisasterRecovery</td>
                    <td>解除实例容灾关系接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">独享实例管理</td>
                    <td>ShowInstance</td>
                    <td>查询WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="21">节点变更</td>
                    <td>ShowClusterRedistribution</td>
                    <td>该接口用于查看当前集群的重分布模式、重分布进度、数据表重分布详情等监控信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeClusterWithExistedNodes</td>
                    <td>此接口用于从空闲节点扩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeCluster</td>
                    <td>此接口用于扩容集群,亦可用于添加空闲节点。默认情况下:表示执行扩容操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterCn</td>
                    <td>查询集群的CN节点列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTargetFlavors</td>
                    <td>查询支持变更的目标规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClusterNodes</td>
                    <td>此接口用于删除空闲节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteFlavorChange</td>
                    <td>执行规格变更。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandInstanceStorage</td>
                    <td>随着客户业务的发展,磁盘空间往往最先出现资源瓶颈,在其他资源尚且充足的情况下,通过磁盘扩容可快速缓解存储资源瓶颈现象,操作过程中无需暂停业务,并且不会造成CPU、内存等资源浪费。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteClusterCn</td>
                    <td>当用户集群创建后,实际需要的CN数量会随着业务需求而发生变化,因此管理CN节点功能的实现使用户可以根据实际需求动态调整集群CN数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterStorageExpandRange</td>
                    <td>此接口可用于查看磁盘扩容操作时支持的扩容范围。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopRedistribution</td>
                    <td>该接口用于暂停运行状态下的重分布操作,重分布暂停状态可设置重分布优先级,修改重分布并发数等操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckGrowCluster</td>
                    <td>此接口用于集群扩容前检查,提前识别子网不足、权限不足等问题导致的扩容失败。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRedistributionSchema</td>
                    <td>获取待重分布表所属模式信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteRedistributionCluster</td>
                    <td>该接口用于集群扩容后将老节点数据均匀分布到新扩节点的数据重分布操作,数据“重分布”后将大大提升业务响应速率。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRedistributionConfigurations</td>
                    <td>更新重分布配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetRedistributionPriority</td>
                    <td>更新重分布表优先级。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreRedistribution</td>
                    <td>此接口用于恢复暂停状态下的重分布操作,仅支持DWS2.0集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterNodes</td>
                    <td>查询节点列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateClusterCn</td>
                    <td>当用户集群创建后,实际需要的CN数量会随着业务需求而发生变化,因此管理CN节点功能的实现使用户可以根据实际需求动态调整集群CN数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterScaleInNumbers</td>
                    <td>查询合适的缩容数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckClusterShrink</td>
                    <td>缩容前检查,确保缩容前、缩容后均满足正常操作要求。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="25">资源管理</td>
                    <td>ListWorkloadQueue</td>
                    <td>查询工作负载队列。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkloadPlanStage</td>
                    <td>查询工作负载计划阶段详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkloadPlan</td>
                    <td>查询某个工作负载计划详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddWorkloadPlanStage</td>
                    <td>添加工作负载计划阶段。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkloadRules</td>
                    <td>查询当前集群的异常规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateQueueResources</td>
                    <td>更新工作负载队列资源配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkloadPlanStage</td>
                    <td>删除工作负载计划删除工作负载计划阶段。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClusterWorkload</td>
                    <td>打开或关闭资源管理功能,新集群默认是打开状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkloadQueue</td>
                    <td>获得工作负载队列详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkloadPlan</td>
                    <td>添加工作负载计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopWorkloadPlan</td>
                    <td>停止工作负载计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkloadPlanStage</td>
                    <td>修改资源管理计划阶段。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkloadQueue</td>
                    <td>该接口用于删除资源池。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterWorkload</td>
                    <td>查询资管管理开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddWorkloadRule</td>
                    <td>添加异常规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkloadQueueUsers</td>
                    <td>获得工作负载队列的绑定用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddWorkloadQueue</td>
                    <td>添加工作负载队列。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkloadPlan</td>
                    <td>删除工作负载计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteQueueUserList</td>
                    <td>删除工作负载队列的绑定用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartWorkloadPlan</td>
                    <td>启动工作负载计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchPlanStage</td>
                    <td>切换工作负载计划阶段。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlanExecLogs</td>
                    <td>查看计划执行日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSchemas</td>
                    <td>更新模式空间限额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkloadPlans</td>
                    <td>查询集群中所有资源管理计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddQueueUserList</td>
                    <td>添加工作负载队列的绑定用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">连接管理</td>
                    <td>AssociateElb</td>
                    <td>集群绑定Elb接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListElbs</td>
                    <td>查询集群可以关联的Elb列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClusterDns</td>
                    <td>删除指定集群域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateEip</td>
                    <td>集群绑定Eip。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeSecurityGroup</td>
                    <td>修改SFS Turbo文件系统绑定的安全组。修改安全组为异步任务,可以通过“查询单个文件系统”返回的子状态字段“sub_status”来判断是否修改安全组状态,子状态为“232”即为修改安全组成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClusterDns</td>
                    <td>为指定集群修改域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateElb</td>
                    <td>集群解绑Elb接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClusterDns</td>
                    <td>为指定集群申请域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateEip</td>
                    <td>集群解绑Eip。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterEndpoints</td>
                    <td>查询连接信息。包括公网域名、内网域名等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">逻辑集群管理</td>
                    <td>ListLogicalClusterRings</td>
                    <td>查询逻辑集群可用ring环节点信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableLogicalCluster</td>
                    <td>此接口用于切换逻辑集群开关,仅用于控制逻辑集群相关功能模块是否在页面展示。在集群已经是逻辑集群的场景下,修改该接口无任何作用及影响。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogicalClusterPlans</td>
                    <td>此接口用于查询逻辑集群定时增删计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogicalClusterPlan</td>
                    <td>此接口用于添加逻辑集群定时增删计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartLogicalCluster</td>
                    <td>此接口用于重启逻辑集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShrinkLogicalCluster</td>
                    <td>逻辑集群缩容,支持从弹性池缩容,或是从逻辑集群中缩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConvertToLogicalCluster</td>
                    <td>物理集群转换到逻辑集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogicalClusterVolumes</td>
                    <td>查询逻辑集群磁盘信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableLogicalClusterPlan</td>
                    <td>启用逻辑集群定时增删计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogicalClusters</td>
                    <td>查询逻辑集群列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableLogicalClusterPlan</td>
                    <td>停用逻辑集群定时增删计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogicalClusterPlan</td>
                    <td>此接口用于删除逻辑集群定时增删计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogicalCluster</td>
                    <td>创建逻辑集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogicalCluster</td>
                    <td>此接口用于编辑修改逻辑集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogicalCluster</td>
                    <td>此接口用于删除逻辑集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogicalClusterTasks</td>
                    <td>查询逻辑集群任务信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogicalClusterPlan</td>
                    <td>此接口用于编辑修改编辑逻辑集群增删计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额管理</td>
                    <td>ListQuotas</td>
                    <td>获取配额信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像标签</td>
                    <td>ListTags</td>
                    <td>根据不同条件查询镜像标签列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="24">集群管理</td>
                    <td>ShowClusters</td>
                    <td>该接口用于查询并显示集群列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveClusterDescriptionInfo</td>
                    <td>修改集群描述信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDwsCluster</td>
                    <td>此接口用于删除集群。集群删除后将释放此集群的所有资源,包括客户数据。为了安全起见,请在删除集群前为这个集群创建快照。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClusterV2</td>
                    <td>该接口用于创建集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckCluster</td>
                    <td>创建集群前预检查,提前识别子网不足、配额不足等问题,避免发起创建集群请求后创建失败。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterEncryptInfo</td>
                    <td>获取集群加密信息。非加密集群不支持该功能,返回信息为空。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagsForResource</td>
                    <td>查询指定集群的企业项目信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchOverCluster</td>
                    <td>当集群状态为“非均衡”时会出现某些节点主实例增多,从而负载压力较大。这种情况下集群状态是正常的,但整体性能要低于均衡状态。可进行集群主备恢复操作将集群状态切换为“可用“状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterVolume</td>
                    <td>查询租户侧节点磁盘使用情况信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterFlavor</td>
                    <td>查询集群使用的规格详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceStatistics</td>
                    <td>该接口用于查询资源统计。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyClusterTimezone</td>
                    <td>修改集群时区。该操作会将操作系统及数据库的时区都进行修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopCluster</td>
                    <td>停止集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterDetails</td>
                    <td>该接口用于查询集群详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDssPools</td>
                    <td>获取专属分布式存储池列表,只包括用户开通的SSD专属资源池信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopoRings</td>
                    <td>查询集群拓扑ring环节点信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartCluster</td>
                    <td>此接口用于重启集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelReadonlyCluster</td>
                    <td>当集群进入只读状态时,无法进行数据库相关操作,用户可以在管理控制台解除集群的只读状态。触发只读状态可能是由于磁盘使用率过高,因此需要对集群数据进行清理或扩容。 - 解除只读支持1.7.2及以上版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EncryptCluster</td>
                    <td>转加密集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterActions</td>
                    <td>查询集群任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodeTypes</td>
                    <td>该接口用于查询所有GaussDB(DWS)服务支持的规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartCluster</td>
                    <td>启动集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyClusterName</td>
                    <td>修改集群名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RotateKey</td>
                    <td>轮转加密集群密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">集群管理接口</td>
                    <td>CreateCluster</td>
                    <td>创建一个MRS集群,并在集群中提交一个作业。该接口不兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCluster</td>
                    <td>数据完成处理分析后或者集群运行异常无法提供服务时可删除集群服务。该接口兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusters</td>
                    <td>查看用户创建的集群列表信息。该接口不兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
