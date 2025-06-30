# GaussDBforopenGauss MCP Server 


## Version
v0.1.0

## Overview

GaussDBforopenGauss MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GaussDBforopenGauss. Full-chain management of GaussDBforopenGauss resources can be carried out based on natural language.

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
                    <td rowspan="7">SQL限流</td>
                    <td>ListLimitTask</td>
                    <td>根据指定条件查询限流任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLimitTask</td>
                    <td>根据task_id进行限流任务的删除</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLimitTask</td>
                    <td>根据具体范围和类型,进行限流任务的创建</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLimitTask</td>
                    <td>查询限流任务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncLimitData</td>
                    <td>同步内核侧sql限流数据至管控侧</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodeLimitSqlModel</td>
                    <td>查询节点的sql模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLimitTask</td>
                    <td>根据新的条件进行限流任务的更新</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>查询租户在指定项目中指定资源类型下的所有标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">任务管理</td>
                    <td>ListScheduleTask</td>
                    <td>查看定时任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelScheduleTask</td>
                    <td>取消定时任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScheduleTask</td>
                    <td>删除定时任务信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobDetail</td>
                    <td>查询job的执行状态。 可用于查询SFS Turbo异步API的执行状态。例如:可使用调用创建并绑定ldap配置接口时返回的jobId,通过该接口查询job的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="19">参数配置</td>
                    <td>CreateConfigurationTemplate</td>
                    <td>创建参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConfiguration</td>
                    <td>修改指定实例的参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceConfiguration</td>
                    <td>获取指定实例的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListParamGroupTemplates</td>
                    <td>获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyConfiguration</td>
                    <td>复制参数模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurationsDiff</td>
                    <td>获取两个参数配置模板的差异列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHistoryOperations</td>
                    <td>查询参数模板的修改历史记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationDetail</td>
                    <td>根据参数模板ID获取指定参数模板详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListParameterGroupTemplates</td>
                    <td>获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppliedHistories</td>
                    <td>查询参数模板的应用记录,以实例级别为维度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchConfiguration</td>
                    <td>指定实例变更参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplicableInstances</td>
                    <td>查询可应用当前参数组模板的实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceParamGroup</td>
                    <td>获取指定实例的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateParaGroupName</td>
                    <td>校验参数组名称是否存在。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceParamGroupDetail</td>
                    <td>获取指定实例的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowParameterGroupDetail</td>
                    <td>根据参数模板ID获取指定参数模板详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurations</td>
                    <td>获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetConfiguration</td>
                    <td>重置参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConfiguration</td>
                    <td>删除参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">回收站</td>
                    <td>ShowRecyclePolicy</td>
                    <td>查询回收站的回收策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecycleInstancesDetails</td>
                    <td>查询回收站所有引擎实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecycleInstances</td>
                    <td>查询回收站实例信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetRecyclePolicy</td>
                    <td>设置回收站策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">备份与恢复</td>
                    <td>CreateManualBackup</td>
                    <td>创建手动备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupPolicy</td>
                    <td>查询自动备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRestoreInstance</td>
                    <td>恢复到新实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteManualBackup</td>
                    <td>删除手动备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBackupPolicy</td>
                    <td>设置自动备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackups</td>
                    <td>获取备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreTimes</td>
                    <td>查询可恢复时间段。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopBackup</td>
                    <td>停止创建备份</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">备份管理</td>
                    <td>ShowInstanceSnapshot</td>
                    <td>根据时间点或者备份文件查询原实例信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestorableInstancesDetails</td>
                    <td>查询可用于备份恢复的实例列表,实例信息要符合备份条件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreInstance</td>
                    <td>备份恢复到当前实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetNewBackupPolicy</td>
                    <td>设置自动备份策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadBackup</td>
                    <td>获取备份下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestorableInstances</td>
                    <td>查询可用于备份恢复的实例列表,实例信息要符合备份条件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackupsDetails</td>
                    <td>获取备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConfirmRestoredData</td>
                    <td>确认备份恢复到目标实例的数据正常。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbBackups</td>
                    <td>获取备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSourceInstanceDetail</td>
                    <td>根据时间点或者备份文件查询原实例信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="26">实例管理</td>
                    <td>CreateGaussDbInstance</td>
                    <td>创建数据库实例,仅支持IAM5的新平面认证方式(AK/SK认证方式)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachEip</td>
                    <td>绑定和解绑弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopInstance</td>
                    <td>实例进行关机,通过暂时停止按需实例以节省费用,实例默认停止七天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchAutoEnlargePolicy</td>
                    <td>查询磁盘自动扩容策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeploymentForm</td>
                    <td>根据解决方案模板名称或实例ID查询副本数、分片数、节点数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseInstances</td>
                    <td>查询数据库实例列表/查询实例详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateWeakPassword</td>
                    <td>校验数据库root用户密码的安全性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCnInfosBeforeReduce</td>
                    <td>查询协调节点列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMysqlCompatibility</td>
                    <td>更新指定实例的M兼容端口服务配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesDetails</td>
                    <td>查询数据库实例列表/查询实例详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeInstanceFlavor</td>
                    <td>GaussDB数据库实例规格变更</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunInstanceAction</td>
                    <td>CN横向扩容/DN分片扩容/磁盘扩容</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectQuotas</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSslCertDownloadLink</td>
                    <td>查询实例SSL证书下载地址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDbInstance</td>
                    <td>创建数据库实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBalanceStatus</td>
                    <td>查询实例是否发生过主备切换而导致主机负载不均衡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchShard</td>
                    <td>支持用户对单个或多个DN分片做主备切换,同一分组内只能指定一个新的备节点进行升主操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartInstance</td>
                    <td>重启指定实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBindedEips</td>
                    <td>查询实例已绑定EIP列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartMysqlCompatibility</td>
                    <td>开启指定实例的M兼容端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFeatures</td>
                    <td>查询当前实例高级特性列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabaseInstance</td>
                    <td>创建数据库实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceName</td>
                    <td>修改实例名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComponentInfos</td>
                    <td>查询实例的组件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFeatures</td>
                    <td>打开高级特性开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceDetails</td>
                    <td>查询数据库实例列表/查询实例详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">容灾管理</td>
                    <td>ShowCrossCloudDisasterInstanceMonitor</td>
                    <td>查询实例容灾监控实时状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterRecoveryFailover</td>
                    <td>容灾升主failover(灾备实例端下发)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCrossCloudDisasterRelations</td>
                    <td>查询容灾关系列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudReleaseDisaster</td>
                    <td>解除容灾(从容灾主集群下发)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterDataCacheEnd</td>
                    <td>结束stream流式容灾的日志保持功能,目前只有stream流容灾支持。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterDataCacheStart</td>
                    <td>主实例开始容灾日志保持,目前只有stream流容灾支持。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDisasterRecoveryRecord</td>
                    <td>查询容灾操作记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterSwitchover</td>
                    <td>容灾switchover(可在主备任一一端下发)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterRestore</td>
                    <td>流容灾备升主选择支持容灾回切,实现容灾关系的重建任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterStartSimulation</td>
                    <td>开始容灾演练,目前只有stream流容灾支持。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetDrConfig</td>
                    <td>重置容灾网络等配置。1.将自动“创建委托”以授权DBS云服务访问VPC资源信息、查询IAAS接口。2.重置实例容灾网络等配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCrossCloudDisasterEndSimulation</td>
                    <td>灾备实例结束容灾演练,目前只有stream流容灾支持。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCrossCloudConstructDisaster</td>
                    <td>搭建容灾关系(从主实例端下发)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">引擎版本和规格</td>
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
                    <td>ListAvailableFlavors</td>
                    <td>查询实例可变更规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlavorsDetails</td>
                    <td>查询数据库的规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceEngineDetail</td>
                    <td>查看实例引擎版本分布</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatastoresDetails</td>
                    <td>查询引擎列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStorageTypes</td>
                    <td>查询数据库磁盘类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbFlavors</td>
                    <td>查询数据库的规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGaussDbDatastores</td>
                    <td>查询引擎列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">插件管理</td>
                    <td>ListKernelPlugins</td>
                    <td>查询实例已安装的插件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPluginExtensions</td>
                    <td>查询实例插件拓展信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResumePluginExtensions</td>
                    <td>配置插件拓展能力</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InstallKernelPlugin</td>
                    <td>安装插件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSupportKernelPlugins</td>
                    <td>查询支持的插件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetKernelPluginLicense</td>
                    <td>配置插件license</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">数据库管理</td>
                    <td>StartInstance</td>
                    <td>启动数据库,同时支持节点级别的启动操作</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">日志管理</td>
                    <td>ShowErrorLogSwitchStatus</td>
                    <td>查询数据库错误日志采集的开关状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceErrorLogs</td>
                    <td>查询数据库错误日志下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSlowLogDownload</td>
                    <td>创建慢日志下载信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSlowLogDownload</td>
                    <td>查询慢日志下载信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">标签管理</td>
                    <td>DeleteInstanceTag</td>
                    <td>删除实例标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPredefinedTags</td>
                    <td>查询预预定义标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceTags</td>
                    <td>查询实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddInstanceTags</td>
                    <td>对指定实例添加用户标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">版本升级</td>
                    <td>UpgradeInstanceVersion</td>
                    <td>GaussDB(for openGauss)实例版本升级。包括灰度升级,就地升级,热补丁升级等三种升级方式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBatchUpgradeCandidateVersions</td>
                    <td>查询批量实例可升级的版本和升级类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeCandidateVersions</td>
                    <td>查询实例可升级版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowUpgradeCandidateVersions</td>
                    <td>查询批量实例可升级的版本和升级类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeCandidateVersionsDetails</td>
                    <td>查询实例可升级版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeInstancesVersion</td>
                    <td>GaussDB批量实例版本升级。包括灰度升级,就地升级、热补丁升级三种升级方式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScheduleTask</td>
                    <td>批量实例内核版本定时升级</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">独享实例管理</td>
                    <td>DeleteInstance</td>
                    <td>删除WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstance</td>
                    <td>创建WAF独享引擎实例。独享模式支持的局点包括:华东-青岛、中东-利雅得、华北-北京一、华北-北京四、华北-乌兰察布一、华东-上海一、华东-上海二、华南-广州、华南-深圳、中国-香港、西南-贵阳一、亚太-曼谷、 亚太-新加坡、非洲约翰内斯堡、土耳其-伊斯坦布尔;普通租户类独享支持的局点:华北-北京四、华东-上海一、华南-广州、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">生命周期管理</td>
                    <td>ListInstances</td>
                    <td>查询租户的实例列表,支持按照条件查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">磁盘管理</td>
                    <td>ShowInstanceDisk</td>
                    <td>查询指定实例的存储使用空间和最大空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">管理数据库和用户</td>
                    <td>CreateDatabaseSchemas</td>
                    <td>在指定实例的数据库中, 创建数据库schema。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowDbRolePrivileges</td>
                    <td>在数据库中设置角色的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseRoles</td>
                    <td>查询数据库角色列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDbRole</td>
                    <td>创建数据库角色。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowDbPrivileges</td>
                    <td>在指定实例的数据库中, 设置帐号的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseSchemas</td>
                    <td>查询指定实例的数据库SCHEMA列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabaseSchema</td>
                    <td>删除数据库schema。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">管理数据库和用户(MySQL)</td>
                    <td>CreateDatabase</td>
                    <td>创建数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDbUser</td>
                    <td>在指定实例中创建数据库帐号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabase</td>
                    <td>删除数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPwd</td>
                    <td>重置数据库密码.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetDbUserPwd</td>
                    <td>设置数据库账号密码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabases</td>
                    <td>查询数据库列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbUsers</td>
                    <td>查询数据库用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">配额管理</td>
                    <td>ListEpsQuotas</td>
                    <td>查询企业项目配额组信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyEpsQuota</td>
                    <td>修改企业项目配额。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
