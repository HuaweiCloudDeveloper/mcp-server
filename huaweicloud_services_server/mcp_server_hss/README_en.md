# HSS MCP Server 


## Version
v0.1.0

## Overview

HSS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service HSS. Full-chain management of HSS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| App Template Management | ListApps | Query the application template list | To be tested |
| Application protection | ListProtectionServers | Querying the protection server list: Query the protection server data, including the server name, IP address, OS, server group name, protection policy, protection status, microservice protection status, RASP protection status, and number of RASP attacks. | To be tested |
|  | ShowRaspProtectStatistics | Protection data statistics: collects the number of added protection servers and the number of microservice RASP attacks in the last seven days. | To be tested |
|  | ShowAppRaspSwitchStatus | Querying the status of the application protection function: Query the status of the application protection function on a single server | To be tested |
|  | ListRaspEvents | Querying the application protection event list: Displays the event information, including the alarm severity, server name, alarm name, alarm time, attack source IP address, and attack source URL. | To be tested |
|  | AddPolicy | Adding a protection policy: Create a protection policy, including the policy name, rule enabling status, protection action, and detection rule configuration. | To be tested |
|  | ListRaspPolicies | Querying the protection policy list: Query the information about the created protection policy, including the policy name, detection rule, and number of associated servers. | To be tested |
|  | ListCheckFeatureRule | Querying the detection rule list: Query the information about the default detection rule, including 14 types of detection rules, which are disabled by default. | To be tested |
|  | ShowRaspPolicyDetail | Querying the details of a protection policy: Query the detection rule information about the protection policy, including 14 types of detection rules. | To be tested |
|  | ShowRaspServerDetail | Querying Java Application Details of the Protection Server: Querying the Java Application Status List of the Protection Server | To be tested |
|  | SwitchRasp | To enable or disable application protection, select the protection policy to be enabled, select the server to be protected, and deliver the protection policy. You can import the port number to update the protection port. If the protection policy is disabled, the policy is cleared. | To be tested |
| Asset Management | ListAutoLaunchs | Query the service list of the self-startup item | To be tested |
|  | ListWebSiteStatistics | Asset Management-Asset Fingerprint-Website navigation tree on the left | To be tested |
|  | ListAppChangeHistories | Obtain historical change records of software information | To be tested |
|  | ListProcessesHost | Information about the host or container that has the process | To be tested |
|  | ListWebAppAndServices | Asset Management > Asset Fingerprint > WebAppAndService Asset Information on the Right | To be tested |
|  | ListJarPackageHostInfo | Query the server list of a specified middleware. The middleware name parameter is transferred and the corresponding middleware server list is returned. | To be tested |
|  | ListAppStatistics | Query the software list. The number of servers can be queried by software name. | To be tested |
|  | ShowAssetStatistic | Asset statistics, including accounts, ports, and processes | To be tested |
|  | ShowHostAssetManualCollectStatus | Query the asset fingerprint collection status of a single host | To be tested |
|  | ListPortHost | Information about the host or container that has the port | To be tested |
|  | ListUsers | Query the server list of the account | To be tested |
|  | ListProcessStatistics | Query the process list. Query the number of servers based on the input process path parameter. | To be tested |
|  | ListAutoLaunchStatistics | Query the auto-startup information. The startup type and number of servers can be queried based on the auto-startup name. | To be tested |
|  | ListUserChangeHistories | Obtain historical account change records | To be tested |
|  | ListGlobalAssetScanTask | Query the status of global asset scanning tasks. | To be tested |
|  | ListAutoLaunchChangeHistories | Obtain the historical change records of the startup item. | To be tested |
|  | RunHostAssetManualCollect | Collection of the asset fingerprint of a single host | To be tested |
|  | ListWebFrameworkStatistics | Asset Management-Asset Fingerprint-Web Framework navigation tree on the left | To be tested |
|  | ShowCommonPort | Displays the details about a port, for example, local port: 80Type: TCPSeverity: NormalPort Description: Commonly used in SSH (SecureShell)-remote login protocol, used for secure login file transfer (SCP, SFTP) and port redirection. | To be tested |
|  | ListKernelModuleHostInfo | Asset Management-Asset Fingerprint-Kernel Module Server List | To be tested |
|  | ListWebAppAndServiceStatistics | Asset Management > Asset Fingerprint > WebAppAndService name tree information on the left | To be tested |
|  | ListWebFrameworkHostInfo | Asset Management-Asset Fingerprint-Web Framework Server List | To be tested |
|  | CreateGlobalAssetScanTask | Create a global asset scanning task | To be tested |
|  | ListUserStatistics | Query the account information list. The number of servers can be queried by entering the account name parameter. | To be tested |
|  | ListWebSiteHostInfo | Asset Management-Asset Fingerprint-Website Server List | To be tested |
|  | ListKernelModuleStatistics | Asset Management-Asset Fingerprint-Kernel Module Tree on the Left | To be tested |
|  | ListPortStatistics | Query the list of open ports. The number of servers can be queried by input port or protocol type. | To be tested |
|  | ListJarPackageStatistics | Query the middleware list. The server tree can be queried by middleware name. | To be tested |
| Baseline Management | ShowBaselineScanStatus | Query the manual baseline scanning result | To be tested |
|  | ChangePasswordComplexityStatus | Ignore or cancel ignoring hosts that fail the password complexity check. | To be tested |
|  | ListRiskConfigs | Query the server security configuration detection result list of a tenant | To be tested |
|  | ListPasswordComplexity | Query the password complexity policy detection report | To be tested |
|  | ListRiskConfigCheckRules | Query the check item list of a specified security configuration item | To be tested |
|  | ShowRiskConfigDetail | Query the check result of a specified security configuration item | To be tested |
|  | ListWeakPasswordUsers | Query the list of weak password detection results | To be tested |
|  | ChangeCheckRuleAction | Ignore, cancel, repair, and verify configuration items that fail the check. | To be tested |
|  | ListRiskConfigHosts | Query the list of affected servers of a specified security configuration item | To be tested |
|  | ShowCheckRuleDetail | Query the configuration check report | To be tested |
| Cluster management | ListCceClusterDetectRisk | Obtain the risk information of container clusters in batches | To be tested |
|  | ShowClusterAssetStatistics | Query the number of cluster assets | To be tested |
|  | AddCceIntegrationProtection | Create CCE integrated protection configuration | To be tested |
|  | ListCommonTips | Obtain some prompt information | To be tested |
|  | ListCceClusterConfig | Obtain the cluster configuration | To be tested |
|  | SyncClusterProtectionEvent | Synchronizing cluster protection events | To be tested |
|  | ListClusterAuditLogs | Query the audit log list of the Kubernetes cluster | To be tested |
|  | ShowClusterProtectPolicyTemplate | Query the cluster protection policy template | To be tested |
|  | ListClusterEventLogs | Query the K8S cluster event list | To be tested |
|  | ListClusterProtectPolicyTemplates | Query the cluster protection policy template list | To be tested |
| Cluster protection | DeleteClusterProtectionPolicy | Delete a cluster protection policy | To be tested |
|  | CreateClusterProtectionPolicy | Create a cluster protection policy | To be tested |
|  | ChangeClusterEvents | Modifying the alarm status | To be tested |
|  | ListClusterProtectionItem | Obtain all protection items of a cluster | To be tested |
|  | ListClusterProtectOverview | Cluster Protection Overview | To be tested |
|  | ListClusterProtectionInfo | Query cluster protection information | To be tested |
|  | ChangeClusterProtectionPolicy | Modifying a cluster protection policy | To be tested |
|  | ListClusterProtectionDefaultPolicy | Obtain the default cluster protection policy list | To be tested |
|  | ListClusterProtectionPolicy | Obtain the cluster protection policy list | To be tested |
|  | SwitchClusterProtectionMode | Operation cluster protection mode | To be tested |
|  | ListClusterEvents | Obtain alarm events in all clusters | To be tested |
|  | ListClusterProtectionPolicyDetail | View details about a specified policy | To be tested |
| Container Asset | ListK8sCronJobs | Query the basic cronjobs information list | To be tested |
|  | ListK8sDeployments | Query the basic deployment information list | To be tested |
|  | ListK8sJobs | Query the basic job information list | To be tested |
|  | ListK8sDaemonSets | Query the basic information list of daemonsets | To be tested |
|  | ListK8sStatefulSets | Query the statefulset basic information list | To be tested |
| Container installation and configuration | BatchUpgradeAgentDaemonset | Upgrading Cluster daemonset in Batches | To be tested |
|  | ShowMultiCloudClusterProxyScript | Obtain the agent installation script of the multi-cloud cluster | To be tested |
|  | UpdateAgentDaemonset | Update the cluster daemonset | To be tested |
|  | SyncMultiCloudClusterStatus | Synchronizing the access status of a multi-cloud cluster | To be tested |
|  | ShowAgentDaemonsetDetailInfo | Obtain the cluster daemonset information | To be tested |
|  | RemoveMultiCloudClusters | Delete a multi-cloud cluster | To be tested |
|  | ShowMultiCloudClusterImageCommand | Obtain the command for uploading an image of a multi-cloud cluster | To be tested |
|  | BatchDeleteAgentDaemonset | Uninstalling the cluster daemonset in batches | To be tested |
|  | CreateAgentDaemonset | Create a cluster daemonset | To be tested |
|  | UpdateMultiCloudClusters | Update multi-cloud cluster | To be tested |
|  | ParseMultiCloudClusterConfig | Resolve the configuration file of the multi-cloud cluster | To be tested |
|  | DeleteAgentDaemonset | Delete a cluster daemonset | To be tested |
|  | CreateMultiCloudClusters | Creating a multi-cloud cluster | To be tested |
|  | ShowAgentDaemonsetDeployTemplate | Obtain the deployment template, which is provided during Daemonset installation. | To be tested |
|  | ListMultiCloudClusters | Querying a multi-cloud cluster | To be tested |
| Container management | ShowContainerNodeStatistics | Query the protection overview data of a container node | To be tested |
|  | CreateClustersInfo | Synchronizing cluster information | To be tested |
|  | SwitchContainerProtectStatus | Switch the protection status | To be tested |
|  | ListContainers | Query the container basic information list | To be tested |
|  | ShowKubernetesEndpointInfo | Query details about a container Kubernetes endpoint | To be tested |
|  | ShowKubernetesServiceInfo | Querying details about the container Kubernetes service | To be tested |
|  | ListContainerCmdLogs | Query the list of commands running in a container | To be tested |
|  | ListK8sPods | Query the basic pod information list | To be tested |
|  | ShowK8sPodDetail | Query pod details | To be tested |
|  | ListKubernetesServiceDetails | Query the Kubernetes service list of a container | To be tested |
|  | ExportContainerList | Create a container export task | To be tested |
|  | ShowK8sContainerDetail | Query container details | To be tested |
|  | ListContainerLogs | Query the container log list | To be tested |
|  | ListKubernetesEndpointDetails | Query the Kubernetes endpoint list of a container | To be tested |
|  | ListKubernetesClusterDetails | Query the container Kubernetes cluster list | To be tested |
|  | ListContainerNodes | Query the container node list | To be tested |
| Container network isolation information | SyncClusterList | Synchronizing the latest data of the container cluster | To be tested |
|  | SyncContainerNetworkPolicyList | Synchronize the latest container network policy data in the cluster | To be tested |
|  | SyncContainerNetworkNode | Synchronize the latest container network policy data in the cluster | To be tested |
|  | CreateContainerNetworkPolicy | Configuration policy for adding a container cluster network | To be tested |
|  | ListContainerNetworkClusters | Query the cluster information about container protection | To be tested |
|  | ShowContainerNetworkInfo | Query the network information of the container cluster network | To be tested |
|  | ListWorkLoads | Query the workload in a namespace in a cluster | To be tested |
|  | SyncSecurityGroupPolicies | Synchronize the latest security group policy data in the cluster | To be tested |
|  | ListContainerNetworkPolicy | Query the policy list of the container cluster network | To be tested |
|  | UpdateSecurityGroupPolicy | Update security group policies (cloud-native network model) | To be tested |
|  | CreateSecurityGroupPolicy | Create a security group policy (cloud-native network model) | To be tested |
|  | ListContainerNetworkNodeList | Query the policy list of the container cluster network | To be tested |
|  | ListSecurityGroupPolicies | Query the security group policies configured for the cluster in cloud native network mode 2.0 | To be tested |
|  | DeleteSecurityGroupPolicy | Delete a security group policy (cloud-native network model) | To be tested |
|  | UpdateContainerNetworkPolicy | Container cluster network update configuration policy | To be tested |
|  | DeleteContainerNetworkPolicy | Configuration policy for deleting a container cluster network | To be tested |
|  | ShowNetworkStatistics | Cluster network policy overview | To be tested |
| Dynamic Port Honeypot | CreateDecoyPortPolicy | Adding a dynamic port honeypot policy | To be tested |
|  | ShowDecoyPortPolicyDetails | View details about a dynamic port honeypot policy | To be tested |
|  | SwitchDecoyPortHostPolicy | Switch the dynamic port honeypot policy of the host | To be tested |
|  | ListDecoyPortPolicy | View the dynamic port honeypot policy | To be tested |
|  | DeleteDecoyPortHostPolicy | Disable the dynamic port honeypot policy of the host | To be tested |
|  | ModifyDecoyPortPolicy | Editing a dynamic port honeypot policy | To be tested |
|  | DeleteDecoyPortPolicy | Delete a dynamic port honeypot policy | To be tested |
| Event Management | ChangeIsolatedFile | Restoring quarantined files | To be tested |
|  | ListQueryExportTask | Query export task information | To be tested |
|  | ListBlockedIp | Query the list of blocked IP addresses | To be tested |
|  | ChangeBlockedIp | Unblocked IP Address | To be tested |
|  | ListIsolatedFile | Query the list of isolated files | To be tested |
|  | ListDownloadExportedFile | Download the exported file | To be tested |
|  | DeleteIsolatedFile | Delete quarantined files | To be tested |
|  | ShowLatestExportTaskByType | Query export task information | To be tested |
| Host Installation and Configuration | ListLoginWhiteIp | Query the SSH login IP address whitelist | To be tested |
|  | ListLoginCommonLocation | Query common login location information | To be tested |
|  | SetTwoFactorLoginConfig | Set the two-factor login configuration | To be tested |
|  | ListTwoFactorLoginHost | Query the two-factor host list | To be tested |
|  | ListLoginCommonIp | Query common login IP addresses | To be tested |
| Host management | ListHostStatus | Query the ECS list | To be tested |
|  | ListPolicies | Query the host policy list | To be tested |
|  | DeleteHostsGroup | Delete a server group | To be tested |
|  | ListHostGroups | Query the server group list | To be tested |
|  | AddHostsGroup | Create a server group | To be tested |
|  | ChangeHostsGroup | Editing a server group | To be tested |
|  | SwitchHostsProtectStatus | Switch the protection status | To be tested |
| Installation and Configuration | ListOrganizationTree | Query an account organization | To be tested |
|  | ListAgentInstallScript | Query the agent installation script | To be tested |
|  | ListAccounts | Query the multi-account list | To be tested |
|  | DeleteAccount | Delete an account | To be tested |
|  | BatchAddAccounts | Adding Accounts in Batches | To be tested |
| Intrusion detection | ListSecurityEvents | Querying the intrusion event list | To be tested |
|  | ChangeEvent | Handling alarm events | To be tested |
| Organization Management | ListNamespaces | Query the organization list | To be tested |
| Policy Management | ListPolicyGroup | Query the policy group list | To be tested |
|  | AssociatePolicyGroup | Deployment Policy Group | To be tested |
| Port | ListPorts | Query all ports of the tenant that submits the request. A maximum of 2000 records can be returned at a time. | To be tested |
| Protection Policy Management | UpdatePolicy | Update the protection policy. The request body can contain only the part to be updated. | To be tested |
|  | DeletePolicy | To delete a protection policy, if the policy is in use, you need to unbind the domain name from the policy before deleting the policy. | To be tested |
| Quota Management | CreateQuotasOrder | The subscription quota for creating an order for the HSS service. Only the yearly/monthly billing mode is supported. | To be tested |
|  | ShowProductdataOfferingInfos | Query product and offering information | To be tested |
|  | ShowResourceQuotas | Query quota information | To be tested |
|  | ListQuotasDetail | Query quota details | To be tested |
| Ransom Protection | StopProtection | Disable ransomware protection | To be tested |
|  | UpdateBackupPolicyInfo | Modifying the backup policy bound to the repository | To be tested |
|  | ListRansomwareProtectionNodes | Query the list of ransomware servers. This interface is used together with the cloud backup service. Therefore, ensure that the cloud backup service is available at the site before using ransomware-related interfaces. | To be tested |
|  | ListProtectionServer | Query the list of ransomware servers. This interface is used together with the cloud backup service. Therefore, ensure that the cloud backup service is available at the site before using ransomware-related interfaces. | To be tested |
|  | ListBackupVaults | Query the backup repository list | To be tested |
|  | ShowBackupPolicyInfo | Query the backup policy bound to the HSS repository and ensure that the ransomware repository has been purchased. You can verify the purchase on the CBR cloud backup service and ensure that the repository named HSS_projectid has been purchased. | To be tested |
|  | ShowSingleBackupPolicyInfo | Query information about a single backup policy | To be tested |
|  | UpdateProtectionPolicy | Modifying a ransomware policy | To be tested |
|  | AddProtectionPolicy | Adding a Protection Policy | To be tested |
|  | ListOperationLogsByVaultName | Query the backup and restoration task list | To be tested |
|  | ListProtectionPolicy | Query the ransomware protection policy list | To be tested |
|  | BatchStartProtection | Enable ransomware protection in batches. If backup protection is enabled, ensure that the CBR cloud backup service is available in the region. | To be tested |
|  | DeleteProtectionPolicy | Delete a protection policy | To be tested |
|  | StartProtection | To enable ransomware protection, ensure that the CBR cloud backup service is available in the region and the ransomware is associated with the cloud backup service. | To be tested |
| Retainer image | ShowImageCheckRuleDetail | Query the mirroring configuration check report | To be tested |
|  | ListImageVulnerabilities | Query image vulnerability information | To be tested |
|  | ListSwrImageRepository | Query the image list in the SWR image repository. If the latest image needs to be synchronized from the SWR, call the API for synchronizing images from the SWR. | To be tested |
|  | ListContainerImageLogs | Query operation logs of a container image | To be tested |
|  | BatchScanSwrImage | Scan images in the image repository in batches | To be tested |
|  | RunImageSynchronize | Synchronizing the image list from the SWR service | To be tested |
|  | ListVulnerabilityCve | CVE information corresponding to the vulnerability | To be tested |
|  | ListImageRiskConfigRules | Query the list of check items for the specified security configuration items of an image | To be tested |
|  | ListImageLocal | Querying the local image list | To be tested |
|  | ListImageRiskConfigs | Query the image security configuration check result list. Currently, system configuration items and SSH application configuration items of CentOS 7, Debian 10, EulerOS, and Ubuntu 16 images can be checked. | To be tested |
|  | ListContainerImages | Query the container image list | To be tested |
| Security group | ListSecurityGroups | Query the security group list of a tenant. | To be tested |
| Security operation | ListAntivirusHandleHistory | Query the list of historical processing records of virus scanning | To be tested |
|  | ListEventHandleHistory | Query the historical handling records of alarms and events | To be tested |
|  | ListVulHandleHistory | Query the historical vulnerability handling record list | To be tested |
| Tag Management | DeleteResourceInstanceTag | Delete a tag under a single resource | To be tested |
|  | BatchCreateTags | Create tags in batches | To be tested |
| Tags | ListProjectTags | Query all tags of a specified resource type in a specified project | To be tested |
| Virus detection and killing | ShowAntivirusPayPerScanStatus | Query the status of the function of charging by times for virus scanning and killing | To be tested |
|  | ChangeAntivirusPolicy | Editing a customized antivirus policy | To be tested |
|  | ListAntiVirusTask | Viewing the virus scanning task list | To be tested |
|  | DeleteAntivirusPolicy | Delete a user-defined antivirus policy. | To be tested |
|  | ExportAntiVirusResult | Export the virus scanning result list | To be tested |
|  | HandleAntiVirusResult | Dispose of virus scanning results | To be tested |
|  | ListAntiVirusResult | Query the virus scanning result list | To be tested |
|  | CreateAntiVirusTask | Create a virus scanning task | To be tested |
|  | ShowAntivirusStatistic | Query virus scanning and removal statistics | To be tested |
|  | ListAntiVirusPolicy | Query the user-defined antivirus policy list | To be tested |
|  | CreateAntiVirusPolicy | Create a customized antivirus policy | To be tested |
|  | ListAntiVirusHost | Query the list of available antivirus servers | To be tested |
| Vulnerability Management | ShowVulScanPolicy | Query a vulnerability scanning policy | To be tested |
|  | ChangeVulScanPolicy | Modifying a Vulnerability Scan Policy | To be tested |
|  | ListVulScanTask | Query the list of vulnerability scanning tasks | To be tested |
|  | ListVulScanTaskHost | Query the host list corresponding to the vulnerability scanning task | To be tested |
|  | ListHostVuls | Query vulnerability information about a single server | To be tested |
|  | ShowVulStatics | Query the vulnerability management statistics | To be tested |
|  | ChangeVulStatus | Modifying the status of a vulnerability | To be tested |
|  | ListVulnerabilities | Query the vulnerability list | To be tested |
|  | CreateVulnerabilityScanTask | Create a vulnerability scanning task | To be tested |
|  | ExportVuls | Exporting information about vulnerabilities and affected hosts | To be tested |
|  | ListVulHosts | Query information about the ECSs affected by a single vulnerability | To be tested |
| Web Tamper Protection | SetRaspSwitch | Enabling or disabling dynamic web tamper protection, delivering or clearing dynamic web tamper protection policies | To be tested |
|  | ListWtpProtectHost | Querying the protection list: Query the protection status list of WTP hosts | To be tested |
|  | ListHostProtectHistoryInfo | Query the static WTP protection status of a host, including the server name, server IP address, protection policy, detection time, protection file, and event description. | To be tested |
|  | ListHostRaspProtectHistoryInfo | Query dynamic WTP protection information of a host, including the alarm severity, server IP address, server name, threat type, alarm time, attack source IP address, and attack source URL. | To be tested |
|  | SetWtpProtectionStatusInfo | Enable or disable WTP and deliver or clear WTP policies. | To be tested |
| Whitelist management | AddLoginWhiteList | Add the login whitelist | To be tested |
|  | RemoveAlarmWhiteList | Delete alarm whitelist | To be tested |
|  | RemoveLoginWhiteList | Delete the login whitelist | To be tested |
|  | UpdateSystemUserWhiteList | Modifying the system user whitelist | To be tested |
|  | ListSystemUserWhiteList | Query the system user whitelist | To be tested |
|  | RemoveSystemUserWhiteList | Delete the system user whitelist | To be tested |
|  | ListLoginWhiteList | Query the login whitelist | To be tested |
|  | AddSystemUserWhiteList | Adding a system user whitelist | To be tested |
|  | ListAlarmWhiteList | Query the alarm whitelist | To be tested |

