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
                    <td rowspan="1">App Template Management</td>
                    <td>ListApps</td>
                    <td>Query the application template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Application protection</td>
                    <td>ListProtectionServers</td>
                    <td>Querying the protection server list: Query the protection server data, including the server name, IP address, OS, server group name, protection policy, protection status, microservice protection status, RASP protection status, and number of RASP attacks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRaspProtectStatistics</td>
                    <td>Protection data statistics: collects the number of added protection servers and the number of microservice RASP attacks in the last seven days.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppRaspSwitchStatus</td>
                    <td>Querying the status of the application protection function: Query the status of the application protection function on a single server</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRaspEvents</td>
                    <td>Querying the application protection event list: Displays the event information, including the alarm severity, server name, alarm name, alarm time, attack source IP address, and attack source URL.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddPolicy</td>
                    <td>Adding a protection policy: Create a protection policy, including the policy name, rule enabling status, protection action, and detection rule configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRaspPolicies</td>
                    <td>Querying the protection policy list: Query the information about the created protection policy, including the policy name, detection rule, and number of associated servers.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCheckFeatureRule</td>
                    <td>Querying the detection rule list: Query the information about the default detection rule, including 14 types of detection rules, which are disabled by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRaspPolicyDetail</td>
                    <td>Querying the details of a protection policy: Query the detection rule information about the protection policy, including 14 types of detection rules.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRaspServerDetail</td>
                    <td>Querying Java Application Details of the Protection Server: Querying the Java Application Status List of the Protection Server</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchRasp</td>
                    <td>To enable or disable application protection, select the protection policy to be enabled, select the server to be protected, and deliver the protection policy. You can import the port number to update the protection port. If the protection policy is disabled, the policy is cleared.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="28">Asset Management</td>
                    <td>ListAutoLaunchs</td>
                    <td>Query the service list of the self-startup item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWebSiteStatistics</td>
                    <td>Asset Management-Asset Fingerprint-Website navigation tree on the left</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppChangeHistories</td>
                    <td>Obtain historical change records of software information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProcessesHost</td>
                    <td>Information about the host or container that has the process</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWebAppAndServices</td>
                    <td>Asset Management &gt; Asset Fingerprint &gt; WebAppAndService Asset Information on the Right</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJarPackageHostInfo</td>
                    <td>Query the server list of a specified middleware. The middleware name parameter is transferred and the corresponding middleware server list is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppStatistics</td>
                    <td>Query the software list. The number of servers can be queried by software name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAssetStatistic</td>
                    <td>Asset statistics, including accounts, ports, and processes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHostAssetManualCollectStatus</td>
                    <td>Query the asset fingerprint collection status of a single host</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPortHost</td>
                    <td>Information about the host or container that has the port</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsers</td>
                    <td>Query the server list of the account</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProcessStatistics</td>
                    <td>Query the process list. Query the number of servers based on the input process path parameter.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutoLaunchStatistics</td>
                    <td>Query the auto-startup information. The startup type and number of servers can be queried based on the auto-startup name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserChangeHistories</td>
                    <td>Obtain historical account change records</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalAssetScanTask</td>
                    <td>Query the status of global asset scanning tasks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutoLaunchChangeHistories</td>
                    <td>Obtain the historical change records of the startup item.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunHostAssetManualCollect</td>
                    <td>Collection of the asset fingerprint of a single host</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWebFrameworkStatistics</td>
                    <td>Asset Management-Asset Fingerprint-Web Framework navigation tree on the left</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCommonPort</td>
                    <td>Displays the details about a port, for example, local port: 80Type: TCPSeverity: NormalPort Description: Commonly used in SSH (SecureShell)-remote login protocol, used for secure login file transfer (SCP, SFTP) and port redirection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKernelModuleHostInfo</td>
                    <td>Asset Management-Asset Fingerprint-Kernel Module Server List</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWebAppAndServiceStatistics</td>
                    <td>Asset Management &gt; Asset Fingerprint &gt; WebAppAndService name tree information on the left</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWebFrameworkHostInfo</td>
                    <td>Asset Management-Asset Fingerprint-Web Framework Server List</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGlobalAssetScanTask</td>
                    <td>Create a global asset scanning task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserStatistics</td>
                    <td>Query the account information list. The number of servers can be queried by entering the account name parameter.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWebSiteHostInfo</td>
                    <td>Asset Management-Asset Fingerprint-Website Server List</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKernelModuleStatistics</td>
                    <td>Asset Management-Asset Fingerprint-Kernel Module Tree on the Left</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPortStatistics</td>
                    <td>Query the list of open ports. The number of servers can be queried by input port or protocol type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJarPackageStatistics</td>
                    <td>Query the middleware list. The server tree can be queried by middleware name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Baseline Management</td>
                    <td>ShowBaselineScanStatus</td>
                    <td>Query the manual baseline scanning result</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangePasswordComplexityStatus</td>
                    <td>Ignore or cancel ignoring hosts that fail the password complexity check.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRiskConfigs</td>
                    <td>Query the server security configuration detection result list of a tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPasswordComplexity</td>
                    <td>Query the password complexity policy detection report</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRiskConfigCheckRules</td>
                    <td>Query the check item list of a specified security configuration item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRiskConfigDetail</td>
                    <td>Query the check result of a specified security configuration item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWeakPasswordUsers</td>
                    <td>Query the list of weak password detection results</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeCheckRuleAction</td>
                    <td>Ignore, cancel, repair, and verify configuration items that fail the check.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRiskConfigHosts</td>
                    <td>Query the list of affected servers of a specified security configuration item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCheckRuleDetail</td>
                    <td>Query the configuration check report</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Cluster management</td>
                    <td>ListCceClusterDetectRisk</td>
                    <td>Obtain the risk information of container clusters in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterAssetStatistics</td>
                    <td>Query the number of cluster assets</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddCceIntegrationProtection</td>
                    <td>Create CCE integrated protection configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCommonTips</td>
                    <td>Obtain some prompt information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCceClusterConfig</td>
                    <td>Obtain the cluster configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncClusterProtectionEvent</td>
                    <td>Synchronizing cluster protection events</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterAuditLogs</td>
                    <td>Query the audit log list of the Kubernetes cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterProtectPolicyTemplate</td>
                    <td>Query the cluster protection policy template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterEventLogs</td>
                    <td>Query the K8S cluster event list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectPolicyTemplates</td>
                    <td>Query the cluster protection policy template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Cluster protection</td>
                    <td>DeleteClusterProtectionPolicy</td>
                    <td>Delete a cluster protection policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClusterProtectionPolicy</td>
                    <td>Create a cluster protection policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeClusterEvents</td>
                    <td>Modifying the alarm status</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectionItem</td>
                    <td>Obtain all protection items of a cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectOverview</td>
                    <td>Cluster Protection Overview</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectionInfo</td>
                    <td>Query cluster protection information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeClusterProtectionPolicy</td>
                    <td>Modifying a cluster protection policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectionDefaultPolicy</td>
                    <td>Obtain the default cluster protection policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectionPolicy</td>
                    <td>Obtain the cluster protection policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchClusterProtectionMode</td>
                    <td>Operation cluster protection mode</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterEvents</td>
                    <td>Obtain alarm events in all clusters</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterProtectionPolicyDetail</td>
                    <td>View details about a specified policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Container Asset</td>
                    <td>ListK8sCronJobs</td>
                    <td>Query the basic cronjobs information list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListK8sDeployments</td>
                    <td>Query the basic deployment information list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListK8sJobs</td>
                    <td>Query the basic job information list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListK8sDaemonSets</td>
                    <td>Query the basic information list of daemonsets</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListK8sStatefulSets</td>
                    <td>Query the statefulset basic information list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">Container installation and configuration</td>
                    <td>BatchUpgradeAgentDaemonset</td>
                    <td>Upgrading Cluster daemonset in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMultiCloudClusterProxyScript</td>
                    <td>Obtain the agent installation script of the multi-cloud cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAgentDaemonset</td>
                    <td>Update the cluster daemonset</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncMultiCloudClusterStatus</td>
                    <td>Synchronizing the access status of a multi-cloud cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgentDaemonsetDetailInfo</td>
                    <td>Obtain the cluster daemonset information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveMultiCloudClusters</td>
                    <td>Delete a multi-cloud cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMultiCloudClusterImageCommand</td>
                    <td>Obtain the command for uploading an image of a multi-cloud cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAgentDaemonset</td>
                    <td>Uninstalling the cluster daemonset in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgentDaemonset</td>
                    <td>Create a cluster daemonset</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMultiCloudClusters</td>
                    <td>Update multi-cloud cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ParseMultiCloudClusterConfig</td>
                    <td>Resolve the configuration file of the multi-cloud cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAgentDaemonset</td>
                    <td>Delete a cluster daemonset</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMultiCloudClusters</td>
                    <td>Creating a multi-cloud cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgentDaemonsetDeployTemplate</td>
                    <td>Obtain the deployment template, which is provided during Daemonset installation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMultiCloudClusters</td>
                    <td>Querying a multi-cloud cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">Container management</td>
                    <td>ShowContainerNodeStatistics</td>
                    <td>Query the protection overview data of a container node</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClustersInfo</td>
                    <td>Synchronizing cluster information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchContainerProtectStatus</td>
                    <td>Switch the protection status</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainers</td>
                    <td>Query the container basic information list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKubernetesEndpointInfo</td>
                    <td>Query details about a container Kubernetes endpoint</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKubernetesServiceInfo</td>
                    <td>Querying details about the container Kubernetes service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerCmdLogs</td>
                    <td>Query the list of commands running in a container</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListK8sPods</td>
                    <td>Query the basic pod information list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowK8sPodDetail</td>
                    <td>Query pod details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKubernetesServiceDetails</td>
                    <td>Query the Kubernetes service list of a container</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportContainerList</td>
                    <td>Create a container export task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowK8sContainerDetail</td>
                    <td>Query container details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerLogs</td>
                    <td>Query the container log list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKubernetesEndpointDetails</td>
                    <td>Query the Kubernetes endpoint list of a container</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKubernetesClusterDetails</td>
                    <td>Query the container Kubernetes cluster list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerNodes</td>
                    <td>Query the container node list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">Container network isolation information</td>
                    <td>SyncClusterList</td>
                    <td>Synchronizing the latest data of the container cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncContainerNetworkPolicyList</td>
                    <td>Synchronize the latest container network policy data in the cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncContainerNetworkNode</td>
                    <td>Synchronize the latest container network policy data in the cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateContainerNetworkPolicy</td>
                    <td>Configuration policy for adding a container cluster network</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerNetworkClusters</td>
                    <td>Query the cluster information about container protection</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowContainerNetworkInfo</td>
                    <td>Query the network information of the container cluster network</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkLoads</td>
                    <td>Query the workload in a namespace in a cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncSecurityGroupPolicies</td>
                    <td>Synchronize the latest security group policy data in the cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerNetworkPolicy</td>
                    <td>Query the policy list of the container cluster network</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityGroupPolicy</td>
                    <td>Update security group policies (cloud-native network model)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityGroupPolicy</td>
                    <td>Create a security group policy (cloud-native network model)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerNetworkNodeList</td>
                    <td>Query the policy list of the container cluster network</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityGroupPolicies</td>
                    <td>Query the security group policies configured for the cluster in cloud native network mode 2.0</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityGroupPolicy</td>
                    <td>Delete a security group policy (cloud-native network model)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateContainerNetworkPolicy</td>
                    <td>Container cluster network update configuration policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteContainerNetworkPolicy</td>
                    <td>Configuration policy for deleting a container cluster network</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNetworkStatistics</td>
                    <td>Cluster network policy overview</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Dynamic Port Honeypot</td>
                    <td>CreateDecoyPortPolicy</td>
                    <td>Adding a dynamic port honeypot policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDecoyPortPolicyDetails</td>
                    <td>View details about a dynamic port honeypot policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchDecoyPortHostPolicy</td>
                    <td>Switch the dynamic port honeypot policy of the host</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDecoyPortPolicy</td>
                    <td>View the dynamic port honeypot policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDecoyPortHostPolicy</td>
                    <td>Disable the dynamic port honeypot policy of the host</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyDecoyPortPolicy</td>
                    <td>Editing a dynamic port honeypot policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDecoyPortPolicy</td>
                    <td>Delete a dynamic port honeypot policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Event Management</td>
                    <td>ChangeIsolatedFile</td>
                    <td>Restoring quarantined files</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryExportTask</td>
                    <td>Query export task information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBlockedIp</td>
                    <td>Query the list of blocked IP addresses</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeBlockedIp</td>
                    <td>Unblocked IP Address</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIsolatedFile</td>
                    <td>Query the list of isolated files</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDownloadExportedFile</td>
                    <td>Download the exported file</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIsolatedFile</td>
                    <td>Delete quarantined files</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLatestExportTaskByType</td>
                    <td>Query export task information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Host Installation and Configuration</td>
                    <td>ListLoginWhiteIp</td>
                    <td>Query the SSH login IP address whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoginCommonLocation</td>
                    <td>Query common login location information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetTwoFactorLoginConfig</td>
                    <td>Set the two-factor login configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTwoFactorLoginHost</td>
                    <td>Query the two-factor host list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoginCommonIp</td>
                    <td>Query common login IP addresses</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Host management</td>
                    <td>ListHostStatus</td>
                    <td>Query the ECS list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicies</td>
                    <td>Query the host policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHostsGroup</td>
                    <td>Delete a server group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostGroups</td>
                    <td>Query the server group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddHostsGroup</td>
                    <td>Create a server group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeHostsGroup</td>
                    <td>Editing a server group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchHostsProtectStatus</td>
                    <td>Switch the protection status</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Installation and Configuration</td>
                    <td>ListOrganizationTree</td>
                    <td>Query an account organization</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgentInstallScript</td>
                    <td>Query the agent installation script</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccounts</td>
                    <td>Query the multi-account list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAccount</td>
                    <td>Delete an account</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddAccounts</td>
                    <td>Adding Accounts in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Intrusion detection</td>
                    <td>ListSecurityEvents</td>
                    <td>Querying the intrusion event list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeEvent</td>
                    <td>Handling alarm events</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Organization Management</td>
                    <td>ListNamespaces</td>
                    <td>Query the organization list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Policy Management</td>
                    <td>ListPolicyGroup</td>
                    <td>Query the policy group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociatePolicyGroup</td>
                    <td>Deployment Policy Group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Port</td>
                    <td>ListPorts</td>
                    <td>Query all ports of the tenant that submits the request. A maximum of 2000 records can be returned at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Protection Policy Management</td>
                    <td>UpdatePolicy</td>
                    <td>Update the protection policy. The request body can contain only the part to be updated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePolicy</td>
                    <td>To delete a protection policy, if the policy is in use, you need to unbind the domain name from the policy before deleting the policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Quota Management</td>
                    <td>CreateQuotasOrder</td>
                    <td>The subscription quota for creating an order for the HSS service. Only the yearly/monthly billing mode is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProductdataOfferingInfos</td>
                    <td>Query product and offering information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceQuotas</td>
                    <td>Query quota information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQuotasDetail</td>
                    <td>Query quota details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Ransom Protection</td>
                    <td>StopProtection</td>
                    <td>Disable ransomware protection</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBackupPolicyInfo</td>
                    <td>Modifying the backup policy bound to the repository</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRansomwareProtectionNodes</td>
                    <td>Query the list of ransomware servers. This interface is used together with the cloud backup service. Therefore, ensure that the cloud backup service is available at the site before using ransomware-related interfaces.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectionServer</td>
                    <td>Query the list of ransomware servers. This interface is used together with the cloud backup service. Therefore, ensure that the cloud backup service is available at the site before using ransomware-related interfaces.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackupVaults</td>
                    <td>Query the backup repository list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupPolicyInfo</td>
                    <td>Query the backup policy bound to the HSS repository and ensure that the ransomware repository has been purchased. You can verify the purchase on the CBR cloud backup service and ensure that the repository named HSS_projectid has been purchased.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSingleBackupPolicyInfo</td>
                    <td>Query information about a single backup policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProtectionPolicy</td>
                    <td>Modifying a ransomware policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddProtectionPolicy</td>
                    <td>Adding a Protection Policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOperationLogsByVaultName</td>
                    <td>Query the backup and restoration task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectionPolicy</td>
                    <td>Query the ransomware protection policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartProtection</td>
                    <td>Enable ransomware protection in batches. If backup protection is enabled, ensure that the CBR cloud backup service is available in the region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProtectionPolicy</td>
                    <td>Delete a protection policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartProtection</td>
                    <td>To enable ransomware protection, ensure that the CBR cloud backup service is available in the region and the ransomware is associated with the cloud backup service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Retainer image</td>
                    <td>ShowImageCheckRuleDetail</td>
                    <td>Query the mirroring configuration check report</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageVulnerabilities</td>
                    <td>Query image vulnerability information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSwrImageRepository</td>
                    <td>Query the image list in the SWR image repository. If the latest image needs to be synchronized from the SWR, call the API for synchronizing images from the SWR.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerImageLogs</td>
                    <td>Query operation logs of a container image</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchScanSwrImage</td>
                    <td>Scan images in the image repository in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunImageSynchronize</td>
                    <td>Synchronizing the image list from the SWR service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVulnerabilityCve</td>
                    <td>CVE information corresponding to the vulnerability</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageRiskConfigRules</td>
                    <td>Query the list of check items for the specified security configuration items of an image</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageLocal</td>
                    <td>Querying the local image list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageRiskConfigs</td>
                    <td>Query the image security configuration check result list. Currently, system configuration items and SSH application configuration items of CentOS 7, Debian 10, EulerOS, and Ubuntu 16 images can be checked.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContainerImages</td>
                    <td>Query the container image list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Security group</td>
                    <td>ListSecurityGroups</td>
                    <td>Query the security group list of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Security operation</td>
                    <td>ListAntivirusHandleHistory</td>
                    <td>Query the list of historical processing records of virus scanning</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventHandleHistory</td>
                    <td>Query the historical handling records of alarms and events</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVulHandleHistory</td>
                    <td>Query the historical vulnerability handling record list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tag Management</td>
                    <td>DeleteResourceInstanceTag</td>
                    <td>Delete a tag under a single resource</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateTags</td>
                    <td>Create tags in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>Query all tags of a specified resource type in a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Virus detection and killing</td>
                    <td>ShowAntivirusPayPerScanStatus</td>
                    <td>Query the status of the function of charging by times for virus scanning and killing</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeAntivirusPolicy</td>
                    <td>Editing a customized antivirus policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAntiVirusTask</td>
                    <td>Viewing the virus scanning task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAntivirusPolicy</td>
                    <td>Delete a user-defined antivirus policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportAntiVirusResult</td>
                    <td>Export the virus scanning result list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>HandleAntiVirusResult</td>
                    <td>Dispose of virus scanning results</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAntiVirusResult</td>
                    <td>Query the virus scanning result list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAntiVirusTask</td>
                    <td>Create a virus scanning task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAntivirusStatistic</td>
                    <td>Query virus scanning and removal statistics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAntiVirusPolicy</td>
                    <td>Query the user-defined antivirus policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAntiVirusPolicy</td>
                    <td>Create a customized antivirus policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAntiVirusHost</td>
                    <td>Query the list of available antivirus servers</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Vulnerability Management</td>
                    <td>ShowVulScanPolicy</td>
                    <td>Query a vulnerability scanning policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeVulScanPolicy</td>
                    <td>Modifying a Vulnerability Scan Policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVulScanTask</td>
                    <td>Query the list of vulnerability scanning tasks</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVulScanTaskHost</td>
                    <td>Query the host list corresponding to the vulnerability scanning task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostVuls</td>
                    <td>Query vulnerability information about a single server</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVulStatics</td>
                    <td>Query the vulnerability management statistics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeVulStatus</td>
                    <td>Modifying the status of a vulnerability</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVulnerabilities</td>
                    <td>Query the vulnerability list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVulnerabilityScanTask</td>
                    <td>Create a vulnerability scanning task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportVuls</td>
                    <td>Exporting information about vulnerabilities and affected hosts</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVulHosts</td>
                    <td>Query information about the ECSs affected by a single vulnerability</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Web Tamper Protection</td>
                    <td>SetRaspSwitch</td>
                    <td>Enabling or disabling dynamic web tamper protection, delivering or clearing dynamic web tamper protection policies</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWtpProtectHost</td>
                    <td>Querying the protection list: Query the protection status list of WTP hosts</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostProtectHistoryInfo</td>
                    <td>Query the static WTP protection status of a host, including the server name, server IP address, protection policy, detection time, protection file, and event description.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostRaspProtectHistoryInfo</td>
                    <td>Query dynamic WTP protection information of a host, including the alarm severity, server IP address, server name, threat type, alarm time, attack source IP address, and attack source URL.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetWtpProtectionStatusInfo</td>
                    <td>Enable or disable WTP and deliver or clear WTP policies.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Whitelist management</td>
                    <td>AddLoginWhiteList</td>
                    <td>Add the login whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveAlarmWhiteList</td>
                    <td>Delete alarm whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveLoginWhiteList</td>
                    <td>Delete the login whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSystemUserWhiteList</td>
                    <td>Modifying the system user whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSystemUserWhiteList</td>
                    <td>Query the system user whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveSystemUserWhiteList</td>
                    <td>Delete the system user whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoginWhiteList</td>
                    <td>Query the login whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddSystemUserWhiteList</td>
                    <td>Adding a system user whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmWhiteList</td>
                    <td>Query the alarm whitelist</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
