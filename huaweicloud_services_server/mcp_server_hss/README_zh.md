# HSS MCP Server 


## Version
v0.1.0

## Overview

HSS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service HSS. Full-chain management of HSS resources can be carried out based on natural language.

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
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>查询租户在指定项目中指定资源类型下的所有标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">主机安装与配置</td>
                    <td>ListLoginWhiteIp</td>
                    <td>查询SSH登录IP白名单列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoginCommonLocation</td>
                    <td>查询常用登录地信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetTwoFactorLoginConfig</td>
                    <td>设置双因子登录配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTwoFactorLoginHost</td>
                    <td>查询双因子主机列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoginCommonIp</td>
                    <td>查询常用登录IP信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">主机管理</td>
                    <td>ListHostStatus</td>
                    <td>查询云服务器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicies</td>
                    <td>查询主机策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHostsGroup</td>
                    <td>删除服务器组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostGroups</td>
                    <td>查询服务器组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddHostsGroup</td>
                    <td>创建服务器组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeHostsGroup</td>
                    <td>编辑服务器组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchHostsProtectStatus</td>
                    <td>切换防护状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">事件管理</td>
                    <td>ChangeIsolatedFile</td>
                    <td>恢复已隔离文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryExportTask</td>
                    <td>查询导出任务信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBlockedIp</td>
                    <td>查询已拦截IP列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeBlockedIp</td>
                    <td>解除已拦截IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIsolatedFile</td>
                    <td>查询已隔离文件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDownloadExportedFile</td>
                    <td>下载导出文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIsolatedFile</td>
                    <td>删除已隔离文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLatestExportTaskByType</td>
                    <td>查询导出任务信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">入侵检测</td>
                    <td>ListSecurityEvents</td>
                    <td>查入侵事件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeEvent</td>
                    <td>处理告警事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">动态端口蜜罐</td>
                    <td>CreateDecoyPortPolicy</td>
                    <td>新增动态端口蜜罐策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDecoyPortPolicyDetails</td>
                    <td>查看动态端口蜜罐策略详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchDecoyPortHostPolicy</td>
                    <td>切换主机动态端口蜜罐策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDecoyPortPolicy</td>
                    <td>查看动态端口蜜罐策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDecoyPortHostPolicy</td>
                    <td>关闭主机动态端口蜜罐策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyDecoyPortPolicy</td>
                    <td>编辑动态端口蜜罐策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDecoyPortPolicy</td>
                    <td>删除动态端口蜜罐策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">勒索防护</td>
                    <td>StopProtection</td>
                    <td>关闭勒索病毒防护</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBackupPolicyInfo</td>
                    <td>修改存储库绑定的备份策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRansomwareProtectionNodes</td>
                    <td>查询勒索防护服务器列表,与云备份服务配合使用。因此使用勒索相关接口之前确保该局点有云备份服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectionServer</td>
                    <td>查询勒索防护服务器列表,与云备份服务配合使用。因此使用勒索相关接口之前确保该局点有云备份服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackupVaults</td>
                    <td>查询备份存储库列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupPolicyInfo</td>
                    <td>查询HSS存储库绑定的备份策略信息,确保已经购买了勒索防护存储库,可以从cbr云备份服务进行验证,确保已经存在HSS_projectid命名的存储库已经购买</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSingleBackupPolicyInfo</td>
                    <td>查询单个备份策略信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProtectionPolicy</td>
                    <td>修改勒索防护策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddProtectionPolicy</td>
                    <td>添加防护策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOperationLogsByVaultName</td>
                    <td>查询备份恢复任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectionPolicy</td>
                    <td>查询勒索病毒的防护策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartProtection</td>
                    <td>批量开启勒索病毒防护,若开启备份防护,请保证该region有cbr云备份服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProtectionPolicy</td>
                    <td>删除防护策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartProtection</td>
                    <td>开启勒索病毒防护,请保证该region有cbr云备份服务,勒索服务与云备份服务有关联关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">基线管理</td>
                    <td>ShowBaselineScanStatus</td>
                    <td>查询基线扫描手动检测结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangePasswordComplexityStatus</td>
                    <td>对口令复杂度检测未通过的主机进行忽略/取消忽略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRiskConfigs</td>
                    <td>查询租户的服务器安全配置检测结果列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPasswordComplexity</td>
                    <td>查询口令复杂度策略检测报告</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRiskConfigCheckRules</td>
                    <td>查询指定安全配置项的检查项列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRiskConfigDetail</td>
                    <td>查询指定安全配置项的检查结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWeakPasswordUsers</td>
                    <td>查询弱口令检测结果列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeCheckRuleAction</td>
                    <td>对未通过的配置检查项进行忽略/取消忽略/修复/验证操作</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRiskConfigHosts</td>
                    <td>查询指定安全配置项的受影响服务器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCheckRuleDetail</td>
                    <td>查询配置检查项检测报告</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">安全组</td>
                    <td>ListSecurityGroups</td>
                    <td>查询某租户下的安全组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">安全运营</td>
                    <td>ListAntivirusHandleHistory</td>
                    <td>查询病毒扫描历史处置记录列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventHandleHistory</td>
                    <td>查询告警事件历史处置记录列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVulHandleHistory</td>
                    <td>查询漏洞历史处置记录列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">安装配置</td>
                    <td>ListOrganizationTree</td>
                    <td>查询账号组织</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgentInstallScript</td>
                    <td>查询agent安装脚本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccounts</td>
                    <td>查询多账号列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAccount</td>
                    <td>删除账号</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddAccounts</td>
                    <td>批量添加账号</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">容器安装与配置</td>
                    <td>BatchUpgradeAgentDaemonset</td>
                    <td>批量升级集群daemonset</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMultiCloudClusterProxyScript</td>
                    <td>获取多云集群的代理安装脚本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAgentDaemonset</td>
                    <td>更新集群daemonset</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncMultiCloudClusterStatus</td>
                    <td>同步多云集群的接入状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgentDaemonsetDetailInfo</td>
                    <td>获取集群daemonset信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveMultiCloudClusters</td>
                    <td>删除多云集群</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMultiCloudClusterImageCommand</td>
                    <td>获取多云集群的上传镜像指令</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAgentDaemonset</td>
                    <td>批量卸载集群daemonset</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgentDaemonset</td>
                    <td>创建集群daemonset</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMultiCloudClusters</td>
                    <td>更新多云集群</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ParseMultiCloudClusterConfig</td>
                    <td>解析多云集群的配置文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAgentDaemonset</td>
                    <td>删除集群daemonset</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMultiCloudClusters</td>
                    <td>创建多云集群</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgentDaemonsetDeployTemplate</td>
                    <td>获取部署模板,在安装Daemonset的时候提供选择</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMultiCloudClusters</td>
                    <td>查询多云集群</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">容器管理</td>
                    <td>ShowContainerNodeStatistics</td>
                    <td>查询容器节点防护总览数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClustersInfo</td>
                    <td>同步集群信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchContainerProtectStatus</td>
                    <td>切换防护状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainers</td>
                    <td>查询容器基本信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKubernetesEndpointInfo</td>
                    <td>查询容器Kubernetes端点详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKubernetesServiceInfo</td>
                    <td>查询容器Kubernetes服务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerCmdLogs</td>
                    <td>查询容器内运行的命令列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListK8sPods</td>
                    <td>查询pod基本信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowK8sPodDetail</td>
                    <td>查询pod详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKubernetesServiceDetails</td>
                    <td>查询容器Kubernetes服务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportContainerList</td>
                    <td>创建容器导出任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowK8sContainerDetail</td>
                    <td>查询容器详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerLogs</td>
                    <td>查询容器日志列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKubernetesEndpointDetails</td>
                    <td>查询容器Kubernetes端点列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKubernetesClusterDetails</td>
                    <td>查询容器Kubernetes集群列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerNodes</td>
                    <td>查询容器节点列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">容器网络隔离信息</td>
                    <td>SyncClusterList</td>
                    <td>同步容器集群最新数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncContainerNetworkPolicyList</td>
                    <td>同步集群下容器网络策略最新数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncContainerNetworkNode</td>
                    <td>同步集群下容器网络策略最新数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateContainerNetworkPolicy</td>
                    <td>容器集群网络添加配置策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerNetworkClusters</td>
                    <td>查询容器防护的集群信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowContainerNetworkInfo</td>
                    <td>查询容器集群网络的网络信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkLoads</td>
                    <td>查询集群下某一命名空间下的工作负载</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncSecurityGroupPolicies</td>
                    <td>同步集群下安全组策略最新数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerNetworkPolicy</td>
                    <td>查询容器集群网络的策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityGroupPolicy</td>
                    <td>更新安全组策略(云原生网络模型)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityGroupPolicy</td>
                    <td>创建安全组策略(云原生网络模型)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerNetworkNodeList</td>
                    <td>查询容器集群网络的策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityGroupPolicies</td>
                    <td>查询云原生网络模式2.0的集群已配置的安全组策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityGroupPolicy</td>
                    <td>删除安全组策略(云原生网络模型)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateContainerNetworkPolicy</td>
                    <td>容器集群网络更新配置策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteContainerNetworkPolicy</td>
                    <td>容器集群网络删除配置策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNetworkStatistics</td>
                    <td>集群网络策略总览</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">容器资产</td>
                    <td>ListK8sCronJobs</td>
                    <td>查询cronjobs基本信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListK8sDeployments</td>
                    <td>查询deployment基本信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListK8sJobs</td>
                    <td>查询jobs基本信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListK8sDaemonSets</td>
                    <td>查询daemonsets基本信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListK8sStatefulSets</td>
                    <td>查询statefulset基本信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">容器镜像</td>
                    <td>ShowImageCheckRuleDetail</td>
                    <td>查询镜像配置检查项检测报告</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageVulnerabilities</td>
                    <td>查询镜像的漏洞信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSwrImageRepository</td>
                    <td>查询swr镜像仓库镜像列表,如果需要从swr同步最新镜像,需要先调用“从swr同步镜像”接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerImageLogs</td>
                    <td>查询容器镜像操作日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchScanSwrImage</td>
                    <td>镜像仓库镜像批量扫描</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunImageSynchronize</td>
                    <td>从SWR服务同步镜像列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVulnerabilityCve</td>
                    <td>漏洞对应cve信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageRiskConfigRules</td>
                    <td>查询镜像指定安全配置项的检查项列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageLocal</td>
                    <td>本地镜像列表查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageRiskConfigs</td>
                    <td>查询镜像安全配置检测结果列表,当前支持检测CentOS 7、Debian 10、EulerOS和Ubuntu16镜像的系统配置项、SSH应用配置项。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerImages</td>
                    <td>查询容器镜像列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">应用模板管理</td>
                    <td>ListApps</td>
                    <td>查询应用模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">应用防护</td>
                    <td>ListProtectionServers</td>
                    <td>查询防护服务器列表:查询防护服务器相关数据,包含服务器名称、ip地址、操作系统、服务器组名称、防护策略、防护状态、微服务防护状态、RASP防护状态、RASP攻击数量信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRaspProtectStatistics</td>
                    <td>防护数据统计:统计已添加防护服务器的数量以及近七天微服务RASP攻击数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppRaspSwitchStatus</td>
                    <td>查询应用防护开启状态:查询单台服务器的应用防护功能开启状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRaspEvents</td>
                    <td>查询应用防护事件列表:展示防护事件相关信息,包含告警级别、服务器名称、告警名称、告警时间、攻击源ip、攻击源url数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddPolicy</td>
                    <td>添加防护策略:创建防护策略,包含策略名称、相关规则开启状态、防护动作以及检测规则配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRaspPolicies</td>
                    <td>查询防护策略列表:查询创建的防护策略信息,包含防护策略名称、检测规则、关联服务器数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCheckFeatureRule</td>
                    <td>查询检测规则列表:查询默认检测规则信息,包含14种检测规则,默认都不开启</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRaspPolicyDetail</td>
                    <td>查询防护策略详情:查询防护策略配置的相关检测规则信息,包含14种检测规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRaspServerDetail</td>
                    <td>查询防护服务器java应用详情:查询防护服务器的java应用状态列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchRasp</td>
                    <td>开启/关闭应用防护,选择开启的防护策略,选择需要防护的服务器,下发防护策略,可传入端口号更新防护端口,关闭防护则清空策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">标签管理</td>
                    <td>DeleteResourceInstanceTag</td>
                    <td>删除单个资源下的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateTags</td>
                    <td>批量创建标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">漏洞管理</td>
                    <td>ShowVulScanPolicy</td>
                    <td>查询漏洞扫描策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeVulScanPolicy</td>
                    <td>修改漏洞扫描策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVulScanTask</td>
                    <td>查询漏洞扫描任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVulScanTaskHost</td>
                    <td>查询漏洞扫描任务对应的主机列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostVuls</td>
                    <td>查询单台服务器漏洞信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVulStatics</td>
                    <td>查询漏洞管理统计数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeVulStatus</td>
                    <td>修改漏洞的状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVulnerabilities</td>
                    <td>查询漏洞列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVulnerabilityScanTask</td>
                    <td>创建漏洞扫描任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportVuls</td>
                    <td>导出漏洞及漏洞影响的主机的相关信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVulHosts</td>
                    <td>查询单个漏洞影响的云服务器信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">病毒查杀</td>
                    <td>ShowAntivirusPayPerScanStatus</td>
                    <td>查询“病毒查杀按次计费”开关状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeAntivirusPolicy</td>
                    <td>编辑自定义查杀策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAntiVirusTask</td>
                    <td>查看病毒扫描任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAntivirusPolicy</td>
                    <td>删除自定义查杀策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportAntiVirusResult</td>
                    <td>导出病毒扫描结果列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>HandleAntiVirusResult</td>
                    <td>处置病毒扫描结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAntiVirusResult</td>
                    <td>查询病毒扫描结果列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAntiVirusTask</td>
                    <td>创建病毒扫描任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAntivirusStatistic</td>
                    <td>查询病毒查杀统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAntiVirusPolicy</td>
                    <td>查询自定义查杀策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAntiVirusPolicy</td>
                    <td>创建自定义查杀策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAntiVirusHost</td>
                    <td>查询病毒查杀可选服务器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">白名单管理</td>
                    <td>AddLoginWhiteList</td>
                    <td>添加登录白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveAlarmWhiteList</td>
                    <td>删除告警白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveLoginWhiteList</td>
                    <td>删除登录白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSystemUserWhiteList</td>
                    <td>修改系统用户白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSystemUserWhiteList</td>
                    <td>查询系统用户白名单列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveSystemUserWhiteList</td>
                    <td>删除系统用户白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoginWhiteList</td>
                    <td>查询登录白名单列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddSystemUserWhiteList</td>
                    <td>添加系统用户白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmWhiteList</td>
                    <td>查询告警白名单列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">端口</td>
                    <td>ListPorts</td>
                    <td>查询提交请求的租户的所有端口,单次查询最多返回2000条数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">策略管理</td>
                    <td>ListPolicyGroup</td>
                    <td>查询策略组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociatePolicyGroup</td>
                    <td>部署策略组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">组织管理</td>
                    <td>ListNamespaces</td>
                    <td>查询组织列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">网页防篡改</td>
                    <td>SetRaspSwitch</td>
                    <td>开启/关闭动态网页防篡改防护,下发/清空动态网页防篡改策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWtpProtectHost</td>
                    <td>查询防护列表:查询网页防篡改主机防护状态列表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostProtectHistoryInfo</td>
                    <td>查询主机静态网页防篡改防护动态:展示服务器名称、服务器ip、防护策略、检测时间、防护文件、事件描述信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostRaspProtectHistoryInfo</td>
                    <td>查询主机动态网页防篡改防护动态:包含告警级别、服务器ip、服务器名称、威胁类型、告警时间、攻击源ip、攻击源url信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetWtpProtectionStatusInfo</td>
                    <td>开启/关闭网页防篡改功能防护,下发/清空网页防篡改策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="28">资产管理</td>
                    <td>ListAutoLaunchs</td>
                    <td>查询自启动项的服务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWebSiteStatistics</td>
                    <td>资产管理-资产指纹-Web站点左侧树</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppChangeHistories</td>
                    <td>获取软件信息的历史变动记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProcessesHost</td>
                    <td>具备该进程的主机/容器信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWebAppAndServices</td>
                    <td>资产管理-资产指纹-右侧WebAppAndService资产信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJarPackageHostInfo</td>
                    <td>查询指定中间件的服务器列表,通过传入中间件名称参数,返回对应的中间件服务器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppStatistics</td>
                    <td>查询软件列表,支持通过软件名称查询对应的服务器数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAssetStatistic</td>
                    <td>资产统计信息,账号、端口、进程等</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHostAssetManualCollectStatus</td>
                    <td>查询单主机资产指纹采集状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPortHost</td>
                    <td>具备该端口的主机/容器信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsers</td>
                    <td>查询账号的服务器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProcessStatistics</td>
                    <td>查询进程列表,通过传入进程路径参数查询对应的服务器数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutoLaunchStatistics</td>
                    <td>查询自启动信息,支持通过传入自启动名称查询启动类型和服务器数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserChangeHistories</td>
                    <td>获取账户变动历史记录信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalAssetScanTask</td>
                    <td>查询资产全局扫描任务状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutoLaunchChangeHistories</td>
                    <td>获取自启动项的历史变动记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunHostAssetManualCollect</td>
                    <td>采集单主机资产指纹</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWebFrameworkStatistics</td>
                    <td>资产管理-资产指纹-Web框架左侧树</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCommonPort</td>
                    <td>呈现某一端口详细信息,如本地端口:80 类型:TCP 危险程度:正常 端口描述:常用于SSH(SecureShell)-远程登录协议,用于安全登录文件传输(SCP,SFTP)及端口重新定向。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKernelModuleHostInfo</td>
                    <td>资产管理-资产指纹-内核模块的服务器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWebAppAndServiceStatistics</td>
                    <td>资产管理-资产指纹-左侧WebAppAndService名称树信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWebFrameworkHostInfo</td>
                    <td>资产管理-资产指纹-Web框架的服务器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGlobalAssetScanTask</td>
                    <td>创建全局资产扫描任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserStatistics</td>
                    <td>查询账号信息列表,支持通过传入账号名称参数查询对应的服务器数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWebSiteHostInfo</td>
                    <td>资产管理-资产指纹-Web站点的服务器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKernelModuleStatistics</td>
                    <td>资产管理-资产指纹-内核模块左侧树</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPortStatistics</td>
                    <td>查询开放端口列表,支持通过传入端口或协议类型查询服务器数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJarPackageStatistics</td>
                    <td>查询中间件列表,支持通过中间件名称查询对应的服务器树</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">配额管理</td>
                    <td>CreateQuotasOrder</td>
                    <td>HSS服务创建订单订购配额,只支持包周期计费模式</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProductdataOfferingInfos</td>
                    <td>查询产商品信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceQuotas</td>
                    <td>查询配额信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQuotasDetail</td>
                    <td>查询配额详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">防护策略管理</td>
                    <td>UpdatePolicy</td>
                    <td>更新防护策略,请求体可只传需要更新的部分</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePolicy</td>
                    <td>删除防护策略,若策略正在使用,则需要先接解除域名与策略的绑定关系才能删除策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">集群管理</td>
                    <td>ListCceClusterDetectRisk</td>
                    <td>批量获取容器集群风险信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterAssetStatistics</td>
                    <td>查询集群资产统计数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddCceIntegrationProtection</td>
                    <td>新建cce集成防护配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCommonTips</td>
                    <td>获取部分提示信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCceClusterConfig</td>
                    <td>获取集群配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncClusterProtectionEvent</td>
                    <td>同步集群防护事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterAuditLogs</td>
                    <td>查询k8s集群审计日志列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterProtectPolicyTemplate</td>
                    <td>查询集群防护策略模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterEventLogs</td>
                    <td>查询k8s集群事件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectPolicyTemplates</td>
                    <td>查询集群防护策略模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">集群防护</td>
                    <td>DeleteClusterProtectionPolicy</td>
                    <td>删除集群防护策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClusterProtectionPolicy</td>
                    <td>新建集群防护策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeClusterEvents</td>
                    <td>修改告警状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectionItem</td>
                    <td>获取集群所有防护项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectOverview</td>
                    <td>集群防护概览</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectionInfo</td>
                    <td>查询集群防护信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeClusterProtectionPolicy</td>
                    <td>修改集群防护策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectionDefaultPolicy</td>
                    <td>获取集群防护默认策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectionPolicy</td>
                    <td>获取集群防护策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchClusterProtectionMode</td>
                    <td>操作集群防护模式</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterEvents</td>
                    <td>获取所有集群中告警事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectionPolicyDetail</td>
                    <td>查看指定策略的详情</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
