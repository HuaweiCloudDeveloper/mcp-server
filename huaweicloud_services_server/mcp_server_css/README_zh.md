# CSS MCP Server 


## Version
v0.1.0

## Overview

CSS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CSS. Full-chain management of CSS resources can be carried out based on natural language.

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
                    <td rowspan="5">Kibana公网访问接口</td>
                    <td>StartKibanaPublic</td>
                    <td>该接口用于开启Kibana公网访问。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopPublicKibanaWhitelist</td>
                    <td>该接口用于关闭Kibana公网访问控制。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCloseKibana</td>
                    <td>该接口用于关闭Kibana公网访问。包周期类型集群不支持通过api进行关闭Kibana公网访问。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlterKibana</td>
                    <td>该接口用于修改Kibana公网带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublicKibanaWhitelist</td>
                    <td>该接口通过修改kibana白名单,修改kibana的访问权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="20">Logstash接口</td>
                    <td>ShowCertsDetail</td>
                    <td>该接口用于查询证书文件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfs</td>
                    <td>该接口用于查询配置文件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartHotPipeline</td>
                    <td>该接口用于热启动pipeline迁移数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListActions</td>
                    <td>该接口用于查询操作记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadCerts</td>
                    <td>该接口用于上传证书文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGetConfDetail</td>
                    <td>该接口用于查询配置文件内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartConnectivityTest</td>
                    <td>该接口用于连通性测试。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCnf</td>
                    <td>该接口用于创建配置文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartPipeline</td>
                    <td>该接口用于启动pipeline迁移数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopPipeline</td>
                    <td>该接口用于停止pipeline迁移数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConf</td>
                    <td>删除配置文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebootCluster</td>
                    <td>重启过程中集群不可用,请谨慎操作。 工作中状态的集群,重启过程会主动停止logstash进程,管道列表“是否保持常驻”值为否,会将所有运行中管道状态置为已停止。“是否保持常驻”值为是,会触发logstash进程恢复机制,将工作中的管道状态置为恢复中,若十分钟内重新拉起logstash进程,管道状态恢复为工作中,否则置为失败状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopHotPipeline</td>
                    <td>该接口用于热停止pipeline迁移数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRoute</td>
                    <td>该接口用于更新集群路由。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCerts</td>
                    <td>该接口用于查询证书列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetRoutes</td>
                    <td>该接口用于获取集群路由。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddFavorite</td>
                    <td>该接口用于添加到自定义模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPipelines</td>
                    <td>该接口用于查询pipeline列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCerts</td>
                    <td>该接口用于删除证书文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCnf</td>
                    <td>该接口用于更新配置文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TemplateManagement</td>
                    <td>DeleteTemplate</td>
                    <td>该接口用于用户删除已创建的模板信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">云硬盘快照</td>
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
                    <td>ListSnapshots</td>
                    <td>查询云硬盘快照详细列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">公网访问接口</td>
                    <td>StopPublicWhitelist</td>
                    <td>该接口用于关闭公网访问控制白名单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBindPublic</td>
                    <td>该接口用于开启公网访问。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUnbindPublic</td>
                    <td>该接口用于关闭公网访问。包周期类型的集群不支持通过api进行关闭公网访问。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublicBandWidth</td>
                    <td>该接口用于修改公网访问带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartPublicWhitelist</td>
                    <td>该接口用于开启公网访问控制白名单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">参数配置接口</td>
                    <td>ListYmlsJob</td>
                    <td>该接口可获取参数配置的任务操作列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListYmls</td>
                    <td>该接口用于获取当前集群现有的参数配置列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateYmls</td>
                    <td>该接口用于修改参数配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">实例管理</td>
                    <td>ResetPassword</td>
                    <td>重置密码(只针对开通SSL的实例)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">引擎版本和规格</td>
                    <td>ListFlavors</td>
                    <td>查询数据库规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">快照管理接口</td>
                    <td>CreateAutoCreatePolicy</td>
                    <td>该接口用于设置自动创建快照,默认一天创建一个快照。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoCreatePolicy</td>
                    <td>该接口用于查询自动创建快照策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreSnapshot</td>
                    <td>该接口用于手动恢复一个快照。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartAutoCreateSnapshots</td>
                    <td>该接口用于打开自动备份功能</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSnapshotSetting</td>
                    <td>该接口用于修改集群快照的基础配置,可修改OBS桶和IAM委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartAutoSetting</td>
                    <td>该接口用于自动设置集群快照的基础配置,包括配置OBS桶和IAM委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopAutoCreateSnapshots</td>
                    <td>该接口用于关闭自动备份功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopSnapshot</td>
                    <td>该接口用于停用快照功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">日志管理接口</td>
                    <td>StopLogAutoBackupPolicy</td>
                    <td>该接口用于日志自动备份策略关闭。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopLogs</td>
                    <td>该接口用于关闭日志功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartLogAutoBackupPolicy</td>
                    <td>该接口用于日志自动备份策略开启。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartTargetClusterConnectivityTest</td>
                    <td>该接口用于连通性测试。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogsJob</td>
                    <td>该接口用于查询具体某个集群的日志任务记录列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogSetting</td>
                    <td>该接口用于修改日志基础配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLogBackup</td>
                    <td>该接口用于查询日志信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogBackup</td>
                    <td>该接口用于备份日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartLogs</td>
                    <td>该接口用于开启日志功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGetLogSetting</td>
                    <td>该接口用于日志基础配置查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">智能运维</td>
                    <td>DeleteAiOps</td>
                    <td>该接口用于删除一个检测任务记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSmnTopics</td>
                    <td>该接口用于获取智能运维告警可用的SMN主题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAiOps</td>
                    <td>该接口用于创建一个集群检测任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAiOps</td>
                    <td>该接口用于获取智能运维任务列表及详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">生命周期管理</td>
                    <td>UpdateInstance</td>
                    <td>修改实例的名称和描述信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">终端节点接口</td>
                    <td>ShowVpcepConnection</td>
                    <td>该接口用于获取终端节点连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopVpecp</td>
                    <td>该接口用于关闭终端节点服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpcepConnection</td>
                    <td>该接口用于更新终端节点连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartVpecp</td>
                    <td>该接口用于开启终端节点服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpcepWhitelist</td>
                    <td>该接口用于修改终端节点服务白名单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">词库管理接口</td>
                    <td>ShowIkThesaurus</td>
                    <td>该接口用于查询自定义词库的加载状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLoadIkThesaurus</td>
                    <td>该接口用于加载存放于OBS的自定义词库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIkThesaurus</td>
                    <td>该接口用于删除自定义词库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">负载均衡</td>
                    <td>ListElbCerts</td>
                    <td>该接口用于查询证书列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateElbListener</td>
                    <td>该接口用于es监听器配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableOrDisableElb</td>
                    <td>该接口打开或关闭es负载均衡器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEsListener</td>
                    <td>该接口用于更新es监听器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowElbDetail</td>
                    <td>该接口用于获取该esELB的信息,以及页面需要展示健康检查状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">连接管理</td>
                    <td>ChangeSecurityGroup</td>
                    <td>修改SFS Turbo文件系统绑定的安全组。修改安全组为异步任务,可以通过“查询单个文件系统”返回的子状态字段“sub_status”来判断是否修改安全组状态,子状态为“232”即为修改安全组成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListElbs</td>
                    <td>查询集群可以关联的Elb列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像</td>
                    <td>ListImages</td>
                    <td>根据不同条件查询镜像列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">集群管理</td>
                    <td>RestartCluster</td>
                    <td>此接口用于重启集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="25">集群管理接口</td>
                    <td>UpdateShrinkNodes</td>
                    <td>该接口可以对集群现有节点中指定节点进行缩容。包周期类型的集群不支持通过api进行指定节点缩容操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClusterName</td>
                    <td>修改集群名称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlavor</td>
                    <td>该接口用于变更集群规格。只支持变更ess节点类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOndemandClusterToPeriod</td>
                    <td>该接口用于按需集群转包周期集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddIndependentNode</td>
                    <td>由于集群数据面业务的增长或者不确定性,很难在一开始就能够把集群的规模形态想明白,该接口能够在非独立master和client的集群上面独立master、client角色。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateExtendInstanceStorage</td>
                    <td>该接口用于集群扩容不同类型实例的个数以及存储容量。已经存在独立Master、Client、冷数据节点的集群使用该接口扩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClustersDetails</td>
                    <td>该接口用于查询并显示集群列表以及集群的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterTag</td>
                    <td>该接口用于查询指定集群的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadCert</td>
                    <td>该接口用于下载安全证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterDetail</td>
                    <td>该接口用于查询并显示单个集群详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlavorByType</td>
                    <td>修改集群规格。支持修改:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClustersTags</td>
                    <td>此接口用于删除集群标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryUpgradeTask</td>
                    <td>由于升级过程时间较长,可能由于网络等原因导致升级失败,可以通过该接口重试该任务或终止该任务的影响。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateShrinkCluster</td>
                    <td>该接口用于集群对不同类型实例的个数以及存储容量进行缩容。包周期类型的集群不支持通过api进行指定节点类型缩容操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollingRestart</td>
                    <td>该接口会一个一个重启节点,在索引数量比较多的情况下耗时较长</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeDetail</td>
                    <td>由于升级过程时间较长,该接口可以展示当前升级(切换AZ)节点的各个阶段信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBatchClustersTags</td>
                    <td>该接口用于对集群批量添加或删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClustersTags</td>
                    <td>该接口用于查询指定region下的所有标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAzByInstanceType</td>
                    <td>该接口通过指定节点类型切换AZ。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeCore</td>
                    <td>该接口用于将低版本的ES升级到高版本或同版本ES。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCluster</td>
                    <td>创建一个MRS集群,并在集群中提交一个作业。该接口不兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeMode</td>
                    <td>该接口用于切换集群的安全模式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateExtendCluster</td>
                    <td>该接口用于集群扩容实例(仅支持扩容elasticsearch实例)。只扩容普通节点,且只针对要扩容的集群实例不存在特殊节点(Master、Client、冷数据节点)的情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCluster</td>
                    <td>数据完成处理分析后或者集群运行异常无法提供服务时可删除集群服务。该接口兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClustersTags</td>
                    <td>该接口用于给指定集群添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">项目信息</td>
                    <td>ListTemplates</td>
                    <td>查询项目模板</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
