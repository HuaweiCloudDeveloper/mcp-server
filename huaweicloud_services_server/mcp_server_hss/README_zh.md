# HSS MCP Server 

## 版本信息
v0.1.0

## 产品描述

HSS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务HSS交互的能力。可以基于自然语言对HSS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 主机安装与配置 | ListLoginWhiteIp | 查询SSH登录IP白名单列表 | To be tested |
|  | ListLoginCommonLocation | 查询常用登录地信息 | To be tested |
|  | SetTwoFactorLoginConfig | 设置双因子登录配置 | To be tested |
|  | ListTwoFactorLoginHost | 查询双因子主机列表 | To be tested |
|  | ListLoginCommonIp | 查询常用登录IP信息 | To be tested |
| 主机管理 | ListHostStatus | 查询云服务器列表 | To be tested |
|  | ListPolicies | 查询主机策略列表 | To be tested |
|  | DeleteHostsGroup | 删除服务器组 | To be tested |
|  | ListHostGroups | 查询服务器组列表 | To be tested |
|  | AddHostsGroup | 创建服务器组 | To be tested |
|  | ChangeHostsGroup | 编辑服务器组 | To be tested |
|  | SwitchHostsProtectStatus | 切换防护状态 | To be tested |
| 事件管理 | ChangeIsolatedFile | 恢复已隔离文件 | To be tested |
|  | ListQueryExportTask | 查询导出任务信息 | To be tested |
|  | ListBlockedIp | 查询已拦截IP列表 | To be tested |
|  | ChangeBlockedIp | 解除已拦截IP | To be tested |
|  | ListIsolatedFile | 查询已隔离文件列表 | To be tested |
|  | ListDownloadExportedFile | 下载导出文件 | To be tested |
|  | DeleteIsolatedFile | 删除已隔离文件 | To be tested |
|  | ShowLatestExportTaskByType | 查询导出任务信息 | To be tested |
| 入侵检测 | ListSecurityEvents | 查入侵事件列表 | To be tested |
|  | ChangeEvent | 处理告警事件 | To be tested |
| 动态端口蜜罐 | CreateDecoyPortPolicy | 新增动态端口蜜罐策略 | To be tested |
|  | ShowDecoyPortPolicyDetails | 查看动态端口蜜罐策略详情 | To be tested |
|  | SwitchDecoyPortHostPolicy | 切换主机动态端口蜜罐策略 | To be tested |
|  | ListDecoyPortPolicy | 查看动态端口蜜罐策略 | To be tested |
|  | DeleteDecoyPortHostPolicy | 关闭主机动态端口蜜罐策略 | To be tested |
|  | ModifyDecoyPortPolicy | 编辑动态端口蜜罐策略 | To be tested |
|  | DeleteDecoyPortPolicy | 删除动态端口蜜罐策略 | To be tested |
| 勒索防护 | StopProtection | 关闭勒索病毒防护 | To be tested |
|  | UpdateBackupPolicyInfo | 修改存储库绑定的备份策略 | To be tested |
|  | ListRansomwareProtectionNodes | 查询勒索防护服务器列表,与云备份服务配合使用。因此使用勒索相关接口之前确保该局点有云备份服务 | To be tested |
|  | ListProtectionServer | 查询勒索防护服务器列表,与云备份服务配合使用。因此使用勒索相关接口之前确保该局点有云备份服务 | To be tested |
|  | ListBackupVaults | 查询备份存储库列表 | To be tested |
|  | ShowBackupPolicyInfo | 查询HSS存储库绑定的备份策略信息,确保已经购买了勒索防护存储库,可以从cbr云备份服务进行验证,确保已经存在HSS_projectid命名的存储库已经购买 | To be tested |
|  | ShowSingleBackupPolicyInfo | 查询单个备份策略信息 | To be tested |
|  | UpdateProtectionPolicy | 修改勒索防护策略 | To be tested |
|  | AddProtectionPolicy | 添加防护策略 | To be tested |
|  | ListOperationLogsByVaultName | 查询备份恢复任务列表 | To be tested |
|  | ListProtectionPolicy | 查询勒索病毒的防护策略列表 | To be tested |
|  | BatchStartProtection | 批量开启勒索病毒防护,若开启备份防护,请保证该region有cbr云备份服务 | To be tested |
|  | DeleteProtectionPolicy | 删除防护策略 | To be tested |
|  | StartProtection | 开启勒索病毒防护,请保证该region有cbr云备份服务,勒索服务与云备份服务有关联关系 | To be tested |
| 基线管理 | ShowBaselineScanStatus | 查询基线扫描手动检测结果 | To be tested |
|  | ChangePasswordComplexityStatus | 对口令复杂度检测未通过的主机进行忽略/取消忽略 | To be tested |
|  | ListRiskConfigs | 查询租户的服务器安全配置检测结果列表 | To be tested |
|  | ListPasswordComplexity | 查询口令复杂度策略检测报告 | To be tested |
|  | ListRiskConfigCheckRules | 查询指定安全配置项的检查项列表 | To be tested |
|  | ShowRiskConfigDetail | 查询指定安全配置项的检查结果 | To be tested |
|  | ListWeakPasswordUsers | 查询弱口令检测结果列表 | To be tested |
|  | ChangeCheckRuleAction | 对未通过的配置检查项进行忽略/取消忽略/修复/验证操作 | To be tested |
|  | ListRiskConfigHosts | 查询指定安全配置项的受影响服务器列表 | To be tested |
|  | ShowCheckRuleDetail | 查询配置检查项检测报告 | To be tested |
| 安全运营 | ListAntivirusHandleHistory | 查询病毒扫描历史处置记录列表 | To be tested |
|  | ListEventHandleHistory | 查询告警事件历史处置记录列表 | To be tested |
|  | ListVulHandleHistory | 查询漏洞历史处置记录列表 | To be tested |
| 安装配置 | ListOrganizationTree | 查询账号组织 | To be tested |
|  | ListAgentInstallScript | 查询agent安装脚本 | To be tested |
|  | ListAccounts | 查询多账号列表 | To be tested |
|  | DeleteAccount | 删除账号 | To be tested |
|  | BatchAddAccounts | 批量添加账号 | To be tested |
| 容器安装与配置 | BatchUpgradeAgentDaemonset | 批量升级集群daemonset | To be tested |
|  | ShowMultiCloudClusterProxyScript | 获取多云集群的代理安装脚本 | To be tested |
|  | UpdateAgentDaemonset | 更新集群daemonset | To be tested |
|  | SyncMultiCloudClusterStatus | 同步多云集群的接入状态 | To be tested |
|  | ShowAgentDaemonsetDetailInfo | 获取集群daemonset信息 | To be tested |
|  | RemoveMultiCloudClusters | 删除多云集群 | To be tested |
|  | ShowMultiCloudClusterImageCommand | 获取多云集群的上传镜像指令 | To be tested |
|  | BatchDeleteAgentDaemonset | 批量卸载集群daemonset | To be tested |
|  | CreateAgentDaemonset | 创建集群daemonset | To be tested |
|  | UpdateMultiCloudClusters | 更新多云集群 | To be tested |
|  | ParseMultiCloudClusterConfig | 解析多云集群的配置文件 | To be tested |
|  | DeleteAgentDaemonset | 删除集群daemonset | To be tested |
|  | CreateMultiCloudClusters | 创建多云集群 | To be tested |
|  | ShowAgentDaemonsetDeployTemplate | 获取部署模板,在安装Daemonset的时候提供选择 | To be tested |
|  | ListMultiCloudClusters | 查询多云集群 | To be tested |
| 容器管理 | ShowContainerNodeStatistics | 查询容器节点防护总览数据 | To be tested |
|  | CreateClustersInfo | 同步集群信息 | To be tested |
|  | SwitchContainerProtectStatus | 切换防护状态 | To be tested |
|  | ListContainers | 查询容器基本信息列表 | To be tested |
|  | ShowKubernetesEndpointInfo | 查询容器Kubernetes端点详情 | To be tested |
|  | ShowKubernetesServiceInfo | 查询容器Kubernetes服务详情 | To be tested |
|  | ListContainerCmdLogs | 查询容器内运行的命令列表 | To be tested |
|  | ListK8sPods | 查询pod基本信息列表 | To be tested |
|  | ShowK8sPodDetail | 查询pod详细信息 | To be tested |
|  | ListKubernetesServiceDetails | 查询容器Kubernetes服务列表 | To be tested |
|  | ExportContainerList | 创建容器导出任务 | To be tested |
|  | ShowK8sContainerDetail | 查询容器详细信息 | To be tested |
|  | ListContainerLogs | 查询容器日志列表 | To be tested |
|  | ListKubernetesEndpointDetails | 查询容器Kubernetes端点列表 | To be tested |
|  | ListKubernetesClusterDetails | 查询容器Kubernetes集群列表 | To be tested |
|  | ListContainerNodes | 查询容器节点列表 | To be tested |
| 容器网络隔离信息 | SyncClusterList | 同步容器集群最新数据 | To be tested |
|  | SyncContainerNetworkPolicyList | 同步集群下容器网络策略最新数据 | To be tested |
|  | SyncContainerNetworkNode | 同步集群下容器网络策略最新数据 | To be tested |
|  | CreateContainerNetworkPolicy | 容器集群网络添加配置策略 | To be tested |
|  | ListContainerNetworkClusters | 查询容器防护的集群信息 | To be tested |
|  | ShowContainerNetworkInfo | 查询容器集群网络的网络信息 | To be tested |
|  | ListNamespaces | 获取集群下的namespace | To be tested |
|  | ListWorkLoads | 查询集群下某一命名空间下的工作负载 | To be tested |
|  | SyncSecurityGroupPolicies | 同步集群下安全组策略最新数据 | To be tested |
|  | ListContainerNetworkPolicy | 查询容器集群网络的策略列表 | To be tested |
|  | UpdateSecurityGroupPolicy | 更新安全组策略(云原生网络模型) | To be tested |
|  | CreateSecurityGroupPolicy | 创建安全组策略(云原生网络模型) | To be tested |
|  | ListContainerNetworkNodeList | 查询容器集群网络的策略列表 | To be tested |
|  | ListSecurityGroupPolicies | 查询云原生网络模式2.0的集群已配置的安全组策略 | To be tested |
|  | DeleteSecurityGroupPolicy | 删除安全组策略(云原生网络模型) | To be tested |
|  | UpdateContainerNetworkPolicy | 容器集群网络更新配置策略 | To be tested |
|  | DeleteContainerNetworkPolicy | 容器集群网络删除配置策略 | To be tested |
|  | ShowNetworkStatistics | 集群网络策略总览 | To be tested |
|  | ListSecurityGroups | 查询企业项目下所有的安全组列表 | To be tested |
| 容器资产 | ListK8sCronJobs | 查询cronjobs基本信息列表 | To be tested |
|  | ListK8sDeployments | 查询deployment基本信息列表 | To be tested |
|  | ListK8sJobs | 查询jobs基本信息列表 | To be tested |
|  | ListK8sDaemonSets | 查询daemonsets基本信息列表 | To be tested |
|  | ListK8sStatefulSets | 查询statefulset基本信息列表 | To be tested |
| 容器镜像 | ShowImageCheckRuleDetail | 查询镜像配置检查项检测报告 | To be tested |
|  | ListImageVulnerabilities | 查询镜像的漏洞信息 | To be tested |
|  | ListSwrImageRepository | 查询swr镜像仓库镜像列表,如果需要从swr同步最新镜像,需要先调用“从swr同步镜像”接口 | To be tested |
|  | ListContainerImageLogs | 查询容器镜像操作日志 | To be tested |
|  | BatchScanSwrImage | 镜像仓库镜像批量扫描 | To be tested |
|  | RunImageSynchronize | 从SWR服务同步镜像列表 | To be tested |
|  | ListVulnerabilityCve | 漏洞对应cve信息 | To be tested |
|  | ListImageRiskConfigRules | 查询镜像指定安全配置项的检查项列表 | To be tested |
|  | ListImageLocal | 本地镜像列表查询 | To be tested |
|  | ListImageRiskConfigs | 查询镜像安全配置检测结果列表,当前支持检测CentOS 7、Debian 10、EulerOS和Ubuntu16镜像的系统配置项、SSH应用配置项。 | To be tested |
|  | ListContainerImages | 查询容器镜像列表 | To be tested |
| 应用防护 | ListProtectionServers | 查询防护服务器列表:查询防护服务器相关数据,包含服务器名称、ip地址、操作系统、服务器组名称、防护策略、防护状态、微服务防护状态、RASP防护状态、RASP攻击数量信息 | To be tested |
|  | ShowRaspProtectStatistics | 防护数据统计:统计已添加防护服务器的数量以及近七天微服务RASP攻击数量 | To be tested |
|  | ShowAppRaspSwitchStatus | 查询应用防护开启状态:查询单台服务器的应用防护功能开启状态 | To be tested |
|  | UpdatePolicy | 修改防护策略:修改防护策略内容,包含策略名称、相关规则开启状态、防护动作以及检测规则配置,同时给使用该策略的服务器下发新的策略 | To be tested |
|  | ListRaspEvents | 查询应用防护事件列表:展示防护事件相关信息,包含告警级别、服务器名称、告警名称、告警时间、攻击源ip、攻击源url数据 | To be tested |
|  | AddPolicy | 添加防护策略:创建防护策略,包含策略名称、相关规则开启状态、防护动作以及检测规则配置 | To be tested |
|  | ListRaspPolicies | 查询防护策略列表:查询创建的防护策略信息,包含防护策略名称、检测规则、关联服务器数量 | To be tested |
|  | ListCheckFeatureRule | 查询检测规则列表:查询默认检测规则信息,包含14种检测规则,默认都不开启 | To be tested |
|  | ShowRaspPolicyDetail | 查询防护策略详情:查询防护策略配置的相关检测规则信息,包含14种检测规则 | To be tested |
|  | DeletePolicy | 删除防护策略:删除策略,已经在使用的防护策略不能删除 | To be tested |
|  | ShowRaspServerDetail | 查询防护服务器java应用详情:查询防护服务器的java应用状态列表 | To be tested |
|  | SwitchRasp | 开启/关闭应用防护,选择开启的防护策略,选择需要防护的服务器,下发防护策略,可传入端口号更新防护端口,关闭防护则清空策略 | To be tested |
| 标签管理 | ListProjectTags | 查询租户当前项目下所有用过的标签 | To be tested |
|  | DeleteResourceInstanceTag | 删除单个资源下的标签 | To be tested |
|  | BatchCreateTags | 批量创建标签 | To be tested |
| 漏洞管理 | ShowVulScanPolicy | 查询漏洞扫描策略 | To be tested |
|  | ChangeVulScanPolicy | 修改漏洞扫描策略 | To be tested |
|  | ListVulScanTask | 查询漏洞扫描任务列表 | To be tested |
|  | ListVulScanTaskHost | 查询漏洞扫描任务对应的主机列表 | To be tested |
|  | ListHostVuls | 查询单台服务器漏洞信息 | To be tested |
|  | ShowVulStatics | 查询漏洞管理统计数据 | To be tested |
|  | ChangeVulStatus | 修改漏洞的状态 | To be tested |
|  | ListVulnerabilities | 查询漏洞列表 | To be tested |
|  | CreateVulnerabilityScanTask | 创建漏洞扫描任务 | To be tested |
|  | ExportVuls | 导出漏洞及漏洞影响的主机的相关信息 | To be tested |
|  | ListVulHosts | 查询单个漏洞影响的云服务器信息 | To be tested |
| 病毒查杀 | ShowAntivirusPayPerScanStatus | 查询“病毒查杀按次计费”开关状态 | To be tested |
|  | ChangeAntivirusPolicy | 编辑自定义查杀策略 | To be tested |
|  | ListAntiVirusTask | 查看病毒扫描任务列表 | To be tested |
|  | DeleteAntivirusPolicy | 删除自定义查杀策略 | To be tested |
|  | ExportAntiVirusResult | 导出病毒扫描结果列表 | To be tested |
|  | HandleAntiVirusResult | 处置病毒扫描结果 | To be tested |
|  | ListAntiVirusResult | 查询病毒扫描结果列表 | To be tested |
|  | CreateAntiVirusTask | 创建病毒扫描任务 | To be tested |
|  | ShowAntivirusStatistic | 查询病毒查杀统计信息 | To be tested |
|  | ListAntiVirusPolicy | 查询自定义查杀策略列表 | To be tested |
|  | CreateAntiVirusPolicy | 创建自定义查杀策略 | To be tested |
|  | ListAntiVirusHost | 查询病毒查杀可选服务器列表 | To be tested |
| 白名单管理 | AddLoginWhiteList | 添加登录白名单 | To be tested |
|  | RemoveAlarmWhiteList | 删除告警白名单 | To be tested |
|  | RemoveLoginWhiteList | 删除登录白名单 | To be tested |
|  | UpdateSystemUserWhiteList | 修改系统用户白名单 | To be tested |
|  | ListSystemUserWhiteList | 查询系统用户白名单列表 | To be tested |
|  | RemoveSystemUserWhiteList | 删除系统用户白名单 | To be tested |
|  | ListLoginWhiteList | 查询登录白名单列表 | To be tested |
|  | AddSystemUserWhiteList | 添加系统用户白名单 | To be tested |
|  | ListAlarmWhiteList | 查询告警白名单列表 | To be tested |
| 策略管理 | ListPolicyGroup | 查询策略组列表 | To be tested |
|  | AssociatePolicyGroup | 部署策略组 | To be tested |
| 网页防篡改 | SetRaspSwitch | 开启/关闭动态网页防篡改防护,下发/清空动态网页防篡改策略 | To be tested |
|  | ListWtpProtectHost | 查询防护列表:查询网页防篡改主机防护状态列表信息 | To be tested |
|  | ListHostProtectHistoryInfo | 查询主机静态网页防篡改防护动态:展示服务器名称、服务器ip、防护策略、检测时间、防护文件、事件描述信息 | To be tested |
|  | ListHostRaspProtectHistoryInfo | 查询主机动态网页防篡改防护动态:包含告警级别、服务器ip、服务器名称、威胁类型、告警时间、攻击源ip、攻击源url信息 | To be tested |
|  | SetWtpProtectionStatusInfo | 开启/关闭网页防篡改功能防护,下发/清空网页防篡改策略 | To be tested |
| 资产管理 | ListAutoLaunchs | 查询自启动项的服务列表 | To be tested |
|  | ListWebSiteStatistics | 资产管理-资产指纹-Web站点左侧树 | To be tested |
|  | ListAppChangeHistories | 获取软件信息的历史变动记录 | To be tested |
|  | ListProcessesHost | 具备该进程的主机/容器信息 | To be tested |
|  | ListWebAppAndServices | 资产管理-资产指纹-右侧WebAppAndService资产信息 | To be tested |
|  | ListJarPackageHostInfo | 查询指定中间件的服务器列表,通过传入中间件名称参数,返回对应的中间件服务器列表 | To be tested |
|  | ListAppStatistics | 查询软件列表,支持通过软件名称查询对应的服务器数 | To be tested |
|  | ShowAssetStatistic | 资产统计信息,账号、端口、进程等 | To be tested |
|  | ShowHostAssetManualCollectStatus | 查询单主机资产指纹采集状态 | To be tested |
|  | ListPortHost | 具备该端口的主机/容器信息 | To be tested |
|  | ListUsers | 查询账号的服务器列表 | To be tested |
|  | ListProcessStatistics | 查询进程列表,通过传入进程路径参数查询对应的服务器数 | To be tested |
|  | ListAutoLaunchStatistics | 查询自启动信息,支持通过传入自启动名称查询启动类型和服务器数 | To be tested |
|  | ListUserChangeHistories | 获取账户变动历史记录信息 | To be tested |
|  | ListGlobalAssetScanTask | 查询资产全局扫描任务状态 | To be tested |
|  | ListApps | 查询软件的服务器列表 | To be tested |
|  | ListAutoLaunchChangeHistories | 获取自启动项的历史变动记录 | To be tested |
|  | RunHostAssetManualCollect | 采集单主机资产指纹 | To be tested |
|  | ListWebFrameworkStatistics | 资产管理-资产指纹-Web框架左侧树 | To be tested |
|  | ShowCommonPort | 呈现某一端口详细信息,如本地端口:80                      类型:TCP 危险程度:正常 端口描述:常用于SSH(SecureShell)-远程登录协议,用于安全登录文件传输(SCP,SFTP)及端口重新定向。 | To be tested |
|  | ListKernelModuleHostInfo | 资产管理-资产指纹-内核模块的服务器列表 | To be tested |
|  | ListWebAppAndServiceStatistics | 资产管理-资产指纹-左侧WebAppAndService名称树信息 | To be tested |
|  | ListWebFrameworkHostInfo | 资产管理-资产指纹-Web框架的服务器列表 | To be tested |
|  | CreateGlobalAssetScanTask | 创建全局资产扫描任务 | To be tested |
|  | ListPorts | 查询单服务器的开放端口列表 | To be tested |
|  | ListUserStatistics | 查询账号信息列表,支持通过传入账号名称参数查询对应的服务器数 | To be tested |
|  | ListWebSiteHostInfo | 资产管理-资产指纹-Web站点的服务器列表 | To be tested |
|  | ListKernelModuleStatistics | 资产管理-资产指纹-内核模块左侧树 | To be tested |
|  | ListPortStatistics | 查询开放端口列表,支持通过传入端口或协议类型查询服务器数 | To be tested |
|  | ListJarPackageStatistics | 查询中间件列表,支持通过中间件名称查询对应的服务器树 | To be tested |
| 配额管理 | CreateQuotasOrder | HSS服务创建订单订购配额,只支持包周期计费模式 | To be tested |
|  | ShowProductdataOfferingInfos | 查询产商品信息 | To be tested |
|  | ShowResourceQuotas | 查询配额信息 | To be tested |
|  | ListQuotasDetail | 查询配额详情 | To be tested |
| 集群管理 | ListCceClusterDetectRisk | 批量获取容器集群风险信息 | To be tested |
|  | ShowClusterAssetStatistics | 查询集群资产统计数量 | To be tested |
|  | AddCceIntegrationProtection | 新建cce集成防护配置 | To be tested |
|  | ListCommonTips | 获取部分提示信息 | To be tested |
|  | ListCceClusterConfig | 获取集群配置 | To be tested |
|  | SyncClusterProtectionEvent | 同步集群防护事件 | To be tested |
|  | ListClusterAuditLogs | 查询k8s集群审计日志列表 | To be tested |
|  | ShowClusterProtectPolicyTemplate | 查询集群防护策略模板 | To be tested |
|  | ListClusterEventLogs | 查询k8s集群事件列表 | To be tested |
|  | ListClusterProtectPolicyTemplates | 查询集群防护策略模板列表 | To be tested |
| 集群防护 | DeleteClusterProtectionPolicy | 删除集群防护策略 | To be tested |
|  | CreateClusterProtectionPolicy | 新建集群防护策略 | To be tested |
|  | ChangeClusterEvents | 修改告警状态 | To be tested |
|  | ListClusterProtectionItem | 获取集群所有防护项 | To be tested |
|  | ListClusterProtectOverview | 集群防护概览 | To be tested |
|  | ListClusterProtectionInfo | 查询集群防护信息 | To be tested |
|  | ChangeClusterProtectionPolicy | 修改集群防护策略 | To be tested |
|  | ListClusterProtectionDefaultPolicy | 获取集群防护默认策略列表 | To be tested |
|  | ListClusterProtectionPolicy | 获取集群防护策略列表 | To be tested |
|  | SwitchClusterProtectionMode | 操作集群防护模式 | To be tested |
|  | ListClusterEvents | 获取所有集群中告警事件 | To be tested |
|  | ListClusterProtectionPolicyDetail | 查看指定策略的详情 | To be tested |
