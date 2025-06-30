# DDS MCP Server 


## Version
v0.1.0

## Overview

DDS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DDS. Full-chain management of DDS resources can be carried out based on natural language.

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
                    <td rowspan="1">ITaskController</td>
                    <td>ListTasks</td>
                    <td>获取任务列表</td>
                    <td>To be tested</td>
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
                    <td rowspan="1">任务管理</td>
                    <td>ShowJobDetail</td>
                    <td>查询job的执行状态。 可用于查询SFS Turbo异步API的执行状态。例如:可使用调用创建并绑定ldap配置接口时返回的jobId,通过该接口查询job的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">参数配置</td>
                    <td>ShowInstanceConfigurationModifyHistory</td>
                    <td>查询实例参数的修改历史。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppliedInstances</td>
                    <td>查询指定参数模板可被应用的实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateConfigurationName</td>
                    <td>校验参数模板名称是否存在。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetConfiguration</td>
                    <td>重置参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurations</td>
                    <td>获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationAppliedHistory</td>
                    <td>查询参数模板应用历史</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEntityConfiguration</td>
                    <td>修改指定实例的参数,可以是实例,组,节点的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEntityConfiguration</td>
                    <td>获取指定实例的参数,可以是实例,组,节点的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CompareConfiguration</td>
                    <td>比较两个参数模板之间的差异。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchConfiguration</td>
                    <td>指定实例变更参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfigurationParameter</td>
                    <td>修改指定参数模板的参数信息,包括名称、描述、指定参数的值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyConfiguration</td>
                    <td>复制参数模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConfiguration</td>
                    <td>创建参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationModifyHistory</td>
                    <td>查询参数模板修改历史。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConfiguration</td>
                    <td>删除参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationParameter</td>
                    <td>获取参数模板的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">回收站</td>
                    <td>ShowRecyclePolicy</td>
                    <td>查询回收站的回收策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetRecyclePolicy</td>
                    <td>设置回收站策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecycleInstances</td>
                    <td>查询回收站实例信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">备份与恢复</td>
                    <td>BatchDeleteBackup</td>
                    <td>批量删除数据库实例的手动备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackups</td>
                    <td>获取备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateManualBackup</td>
                    <td>创建手动备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupDownloadLink</td>
                    <td>获取备份下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreDatabases</td>
                    <td>获取可恢复的数据库列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreCollections</td>
                    <td>获取可恢复的数据库集合列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreInstanceFromCollection</td>
                    <td>库表级时间点恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopBackup</td>
                    <td>停止创建备份</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreNewInstance</td>
                    <td>根据备份恢复新实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBackupPolicy</td>
                    <td>设置自动备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreTimes</td>
                    <td>查询可恢复时间段。</td>
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
                    <td rowspan="1">备份管理</td>
                    <td>RestoreInstance</td>
                    <td>备份恢复到当前实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">安全组</td>
                    <td>UpdateSecurityGroup</td>
                    <td>更新安全组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">定时任务</td>
                    <td>ListScheduledTasks</td>
                    <td>根据指定条件查询定时任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelScheduledTask</td>
                    <td>根据任务ID取消定时任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="37">实例管理</td>
                    <td>UpdateInstanceName</td>
                    <td>修改实例名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckWeakPassword</td>
                    <td>检查弱密码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandReplicasetNode</td>
                    <td>扩容指定副本集实例的节点数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchoverReplicaSet</td>
                    <td>切换副本集实例下的主备节点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeOpsWindow</td>
                    <td>设置可维护时间段</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLtsConfig</td>
                    <td>将实例日志与LTS日志流关联,后台将自动上传实例日志到关联的LTS日志流里。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLtsConfigs</td>
                    <td>查询LTS日志配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelEip</td>
                    <td>解绑实例下节点已经绑定的弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoEnlargePolicy</td>
                    <td>查询实例存储空间自动扩容策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeDuration</td>
                    <td>查询数据库补丁升级预估时长</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeInstanceVolume</td>
                    <td>扩容实例相关的存储容量大小。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachInternalIp</td>
                    <td>修改实例的内网地址</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteReadonlyNode</td>
                    <td>当副本集添加了只读节点后,需要删除对应的只读节点需要调用此API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMongosNode</td>
                    <td>当集群实例需要缩减mongos节点时,需要调用此API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClientNetwork</td>
                    <td>查询副本集跨网段访问配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSslCertDownloadAddress</td>
                    <td>获取SSL证书下载地址</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClientNetwork</td>
                    <td>副本集跨网段访问配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceRemark</td>
                    <td>修改实例备注。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShrinkInstanceNodes</td>
                    <td>删除实例的节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachEip</td>
                    <td>绑定和解绑弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstancePort</td>
                    <td>修改数据库实例的端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPassword</td>
                    <td>重置密码(只针对开通SSL的实例)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchSecondLevelMonitoring</td>
                    <td>开启或关闭指定实例的秒级监控。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAz2Migrate</td>
                    <td>查询实例可迁移到的可用区。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetAutoEnlargePolicies</td>
                    <td>设置磁盘自动扩容策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLtsConfig</td>
                    <td>将实例日志与LTS日志流解除关联,后台将取消上传实例日志到的LTS日志流里。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeDatabaseVersion</td>
                    <td>升级数据库补丁版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReplSetName</td>
                    <td>查询数据库复制集名称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddReadonlyNode</td>
                    <td>DDS副本集实例新增只读节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIp</td>
                    <td>创建集群的Shard/Config IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateAz</td>
                    <td>实例可用区迁移。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpgradeDatabaseVersion</td>
                    <td>批量升级数据库补丁版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddShardingNode</td>
                    <td>扩容指定集群实例的节点数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecondLevelMonitoringStatus</td>
                    <td>查询秒级监控配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDiskUsage</td>
                    <td>查询实例磁盘信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateReplSetName</td>
                    <td>修改数据库复制集名称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartInstance</td>
                    <td>重启指定实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">引擎版本和规格</td>
                    <td>ListFlavorInfos</td>
                    <td>查询指定条件下的实例规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatastoreVersions</td>
                    <td>查询指定实例类型的数据库版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStorageType</td>
                    <td>查询当前区域下的数据库磁盘类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlavors</td>
                    <td>查询数据库规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">数据库安全性</td>
                    <td>SwitchSsl</td>
                    <td>设置SSL数据加密。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">数据库权限管理</td>
                    <td>CreateDatabaseUser</td>
                    <td>创建数据库用户/角色。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseUsers</td>
                    <td>查询所有数据库用户/角色。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabaseUser</td>
                    <td>删除数据库用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">数据库运维</td>
                    <td>SwitchInstancePrimary</td>
                    <td>支持副本集、shard和config备节点强制升主。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKillOpRuleList</td>
                    <td>删除killOp规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKillOpRuleRuleList</td>
                    <td>获取killOp规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKillOpRule</td>
                    <td>启用/禁用killOp规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKillOpRule</td>
                    <td>创建killOp规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询版本操作</td>
                    <td>ShowApiVersion</td>
                    <td>查询指定的标签管理服务API版本号详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">标签管理</td>
                    <td>ListInstanceTags</td>
                    <td>查询实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesByTags</td>
                    <td>根据标签查询指定的数据库实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchTagAction</td>
                    <td>批量添加删除资源标签。</td>
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
                    <td rowspan="7">管理数据库和用户</td>
                    <td>ListDatabaseRoles</td>
                    <td>查询数据库角色列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckPassword</td>
                    <td>检查数据库密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabaseRole</td>
                    <td>创建数据库角色。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBalancerSwitch</td>
                    <td>设置集群均衡开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabaseRole</td>
                    <td>删除数据库角色。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBalancerWindow</td>
                    <td>设置集群均衡活动时间窗。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowShardingBalancer</td>
                    <td>查询集群均衡设置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">管理数据库和用户(MySQL)</td>
                    <td>ListDatabases</td>
                    <td>查询数据库列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">获取日志信息</td>
                    <td>ListLtsErrorLogs</td>
                    <td>查询数据库错误日志信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadErrorlog</td>
                    <td>获取错误日志下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchSlowlogDesensitization</td>
                    <td>设置实例的慢日志明文开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadSlowlog</td>
                    <td>获取慢日志下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLtsSlowLogs</td>
                    <td>查询数据库慢日志信息。</td>
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
                    <td>ListAuditlogs</td>
                    <td>获取审计日志列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetAuditlogPolicy</td>
                    <td>设置审计日志策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditlogLinks</td>
                    <td>获取审计日志下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAuditLog</td>
                    <td>删除审计日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSlowlogDesensitizationSwitch</td>
                    <td>查询慢日志明文开关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowLogs</td>
                    <td>查询数据库慢日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">规格变更管理</td>
                    <td>ResizeInstance</td>
                    <td>实例规格变更。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">连接管理</td>
                    <td>ShowConnectionStatistics</td>
                    <td>查询客户端IP访问至DDS数据库实例的连接数统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSession</td>
                    <td>终结实例节点会话。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSessions</td>
                    <td>查询实例节点会话。</td>
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
