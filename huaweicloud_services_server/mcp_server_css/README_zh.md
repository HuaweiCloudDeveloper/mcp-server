# CSS MCP Server 

## 版本信息
v0.1.0

## 产品描述

CSS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CSS交互的能力。可以基于自然语言对CSS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Kibana公网访问接口 | StartKibanaPublic | 该接口用于开启Kibana公网访问。 | To be tested |
|  | StopPublicKibanaWhitelist | 该接口用于关闭Kibana公网访问控制。 | To be tested |
|  | UpdateCloseKibana | 该接口用于关闭Kibana公网访问。包周期类型集群不支持通过api进行关闭Kibana公网访问。 | To be tested |
|  | UpdateAlterKibana | 该接口用于修改Kibana公网带宽。 | To be tested |
|  | UpdatePublicKibanaWhitelist | 该接口通过修改kibana白名单,修改kibana的访问权限。 | To be tested |
| Logstash接口 | ShowCertsDetail | 该接口用于查询证书文件信息。 | To be tested |
|  | DeleteTemplate | 该接口用于删除自定义模板。 | To be tested |
|  | ListConfs | 该接口用于查询配置文件列表。 | To be tested |
|  | StartHotPipeline | 该接口用于热启动pipeline迁移数据。 | To be tested |
|  | ListActions | 该接口用于查询操作记录。 | To be tested |
|  | UploadCerts | 该接口用于上传证书文件。 | To be tested |
|  | ShowGetConfDetail | 该接口用于查询配置文件内容。 | To be tested |
|  | StartConnectivityTest | 该接口用于连通性测试。 | To be tested |
|  | CreateCnf | 该接口用于创建配置文件。 | To be tested |
|  | StartPipeline | 该接口用于启动pipeline迁移数据。 | To be tested |
|  | StopPipeline | 该接口用于停止pipeline迁移数据。 | To be tested |
|  | DeleteConf | 删除配置文件。 | To be tested |
|  | RebootCluster | 重启过程中集群不可用,请谨慎操作。 工作中状态的集群,重启过程会主动停止logstash进程,管道列表“是否保持常驻”值为否,会将所有运行中管道状态置为已停止。“是否保持常驻”值为是,会触发logstash进程恢复机制,将工作中的管道状态置为恢复中,若十分钟内重新拉起logstash进程,管道状态恢复为工作中,否则置为失败状态。 | To be tested |
|  | StopHotPipeline | 该接口用于热停止pipeline迁移数据。 | To be tested |
|  | UpdateRoute | 该接口用于更新集群路由。 | To be tested |
|  | ListCerts | 该接口用于查询证书列表。 | To be tested |
|  | GetRoutes | 该接口用于获取集群路由。 | To be tested |
|  | AddFavorite | 该接口用于添加到自定义模板。 | To be tested |
|  | ListPipelines | 该接口用于查询pipeline列表。 | To be tested |
|  | DeleteCerts | 该接口用于删除证书文件。 | To be tested |
|  | ListTemplates | 该接口用于查询模板列表。 | To be tested |
|  | UpdateCnf | 该接口用于更新配置文件。 | To be tested |
| 公网访问接口 | StopPublicWhitelist | 该接口用于关闭公网访问控制白名单。 | To be tested |
|  | CreateBindPublic | 该接口用于开启公网访问。 | To be tested |
|  | UpdateUnbindPublic | 该接口用于关闭公网访问。包周期类型的集群不支持通过api进行关闭公网访问。 | To be tested |
|  | UpdatePublicBandWidth | 该接口用于修改公网访问带宽。 | To be tested |
|  | StartPublicWhitelist | 该接口用于开启公网访问控制白名单。 | To be tested |
| 参数配置接口 | ListYmlsJob | 该接口可获取参数配置的任务操作列表。 | To be tested |
|  | ListYmls | 该接口用于获取当前集群现有的参数配置列表。 | To be tested |
|  | UpdateYmls | 该接口用于修改参数配置。 | To be tested |
| 快照管理接口 | CreateAutoCreatePolicy | 该接口用于设置自动创建快照,默认一天创建一个快照。 | To be tested |
|  | ShowAutoCreatePolicy | 该接口用于查询自动创建快照策略。 | To be tested |
|  | RestoreSnapshot | 该接口用于手动恢复一个快照。 | To be tested |
|  | StartAutoCreateSnapshots | 该接口用于打开自动备份功能 | To be tested |
|  | UpdateSnapshotSetting | 该接口用于修改集群快照的基础配置,可修改OBS桶和IAM委托。 | To be tested |
|  | StartAutoSetting | 该接口用于自动设置集群快照的基础配置,包括配置OBS桶和IAM委托。 | To be tested |
|  | StopAutoCreateSnapshots | 该接口用于关闭自动备份功能。 | To be tested |
|  | StopSnapshot | 该接口用于停用快照功能。 | To be tested |
|  | CreateSnapshot | 该接口用于手动创建一个快照。 | To be tested |
|  | DeleteSnapshot | 该接口用于删除快照。 | To be tested |
|  | ListSnapshots | 该接口用于查询集群的所有快照。 | To be tested |
| 日志管理接口 | StopLogAutoBackupPolicy | 该接口用于日志自动备份策略关闭。 | To be tested |
|  | StopLogs | 该接口用于关闭日志功能。 | To be tested |
|  | StartLogAutoBackupPolicy | 该接口用于日志自动备份策略开启。 | To be tested |
|  | StartTargetClusterConnectivityTest | 该接口用于连通性测试。 | To be tested |
|  | ListLogsJob | 该接口用于查询具体某个集群的日志任务记录列表。 | To be tested |
|  | UpdateLogSetting | 该接口用于修改日志基础配置。 | To be tested |
|  | ShowLogBackup | 该接口用于查询日志信息。 | To be tested |
|  | CreateLogBackup | 该接口用于备份日志。 | To be tested |
|  | StartLogs | 该接口用于开启日志功能。 | To be tested |
|  | ShowGetLogSetting | 该接口用于日志基础配置查询。 | To be tested |
| 智能运维 | DeleteAiOps | 该接口用于删除一个检测任务记录。 | To be tested |
|  | ListSmnTopics | 该接口用于获取智能运维告警可用的SMN主题。 | To be tested |
|  | CreateAiOps | 该接口用于创建一个集群检测任务。 | To be tested |
|  | ListAiOps | 该接口用于获取智能运维任务列表及详情。 | To be tested |
| 终端节点接口 | ShowVpcepConnection | 该接口用于获取终端节点连接。 | To be tested |
|  | StopVpecp | 该接口用于关闭终端节点服务。 | To be tested |
|  | UpdateVpcepConnection | 该接口用于更新终端节点连接。 | To be tested |
|  | StartVpecp | 该接口用于开启终端节点服务。 | To be tested |
|  | UpdateVpcepWhitelist | 该接口用于修改终端节点服务白名单。 | To be tested |
| 词库管理接口 | ShowIkThesaurus | 该接口用于查询自定义词库的加载状态。 | To be tested |
|  | CreateLoadIkThesaurus | 该接口用于加载存放于OBS的自定义词库。 | To be tested |
|  | DeleteIkThesaurus | 该接口用于删除自定义词库。 | To be tested |
| 负载均衡 | ListElbCerts | 该接口用于查询证书列表。 | To be tested |
|  | CreateElbListener | 该接口用于es监听器配置。 | To be tested |
|  | EnableOrDisableElb | 该接口打开或关闭es负载均衡器。 | To be tested |
|  | UpdateEsListener | 该接口用于更新es监听器。 | To be tested |
|  | ListElbs | 展示查询集群支持的elbv3负载均衡器 | To be tested |
|  | ShowElbDetail | 该接口用于获取该esELB的信息,以及页面需要展示健康检查状态。 | To be tested |
| 集群管理接口 | UpdateInstance | 该接口用于替换失败节点。 | To be tested |
|  | UpdateShrinkNodes | 该接口可以对集群现有节点中指定节点进行缩容。包周期类型的集群不支持通过api进行指定节点缩容操作。 | To be tested |
|  | ResetPassword | 该接口用于修改集群密码。 | To be tested |
|  | ChangeSecurityGroup | 该接口可以在集群创建成功后,修改安全组。 | To be tested |
|  | UpdateClusterName | 该接口用于修改集群名称。 | To be tested |
|  | UpdateFlavor | 该接口用于变更集群规格。只支持变更ess节点类型。 | To be tested |
|  | UpdateOndemandClusterToPeriod | 该接口用于按需集群转包周期集群。 | To be tested |
|  | AddIndependentNode | 由于集群数据面业务的增长或者不确定性,很难在一开始就能够把集群的规模形态想明白,该接口能够在非独立master和client的集群上面独立master、client角色。 | To be tested |
|  | UpdateExtendInstanceStorage | 该接口用于集群扩容不同类型实例的个数以及存储容量。已经存在独立Master、Client、冷数据节点的集群使用该接口扩容。 | To be tested |
|  | ListClustersDetails | 该接口用于查询并显示集群列表以及集群的状态。 | To be tested |
|  | ShowClusterTag | 该接口用于查询指定集群的标签信息。 | To be tested |
|  | DownloadCert | 该接口用于下载安全证书。 | To be tested |
|  | ShowClusterDetail | 该接口用于查询并显示单个集群详情。 | To be tested |
|  | UpdateFlavorByType | 修改集群规格。支持修改: | To be tested |
|  | DeleteClustersTags | 此接口用于删除集群标签。 | To be tested |
|  | RetryUpgradeTask | 由于升级过程时间较长,可能由于网络等原因导致升级失败,可以通过该接口重试该任务或终止该任务的影响。 | To be tested |
|  | UpdateShrinkCluster | 该接口用于集群对不同类型实例的个数以及存储容量进行缩容。包周期类型的集群不支持通过api进行指定节点类型缩容操作。 | To be tested |
|  | RollingRestart | 该接口会一个一个重启节点,在索引数量比较多的情况下耗时较长 | To be tested |
|  | UpgradeDetail | 由于升级过程时间较长,该接口可以展示当前升级(切换AZ)节点的各个阶段信息。 | To be tested |
|  | UpdateBatchClustersTags | 该接口用于对集群批量添加或删除标签。 | To be tested |
|  | ListClustersTags | 该接口用于查询指定region下的所有标签集合。 | To be tested |
|  | UpdateAzByInstanceType | 该接口通过指定节点类型切换AZ。 | To be tested |
|  | UpgradeCore | 该接口用于将低版本的ES升级到高版本或同版本ES。 | To be tested |
|  | CreateCluster | 该接口用于创建拥有多种不同节点类型(ess,ess-cold,ess-client,ess-master)组合的集群。 | To be tested |
|  | ChangeMode | 该接口用于切换集群的安全模式。 | To be tested |
|  | UpdateExtendCluster | 该接口用于集群扩容实例(仅支持扩容elasticsearch实例)。只扩容普通节点,且只针对要扩容的集群实例不存在特殊节点(Master、Client、冷数据节点)的情况。 | To be tested |
|  | ListImages | 该接口用于获取当前集群的可升级目标镜像ID。 | To be tested |
|  | DeleteCluster | 此接口用于删除集群。集群删除将释放此集群的所有资源,包括客户数据。如果需要保留客户集群数据,建议在删除集群前先创建快照。 | To be tested |
|  | ListFlavors | 该接口用于查询并显示支持的实例规格对应的ID。 | To be tested |
|  | RestartCluster | 该接口可以用于重启当前集群拥有的全部节点类型,或部分节点类型组合的节点。 | To be tested |
|  | CreateClustersTags | 该接口用于给指定集群添加标签。 | To be tested |
