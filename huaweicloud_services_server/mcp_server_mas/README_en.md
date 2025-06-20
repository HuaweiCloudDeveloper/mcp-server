# MAS MCP Server 


## Version
v0.1.0

## Overview

MAS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service MAS. Full-chain management of MAS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| App Management | DeleteApplications |  | To be tested |
| Application operation | CreateApplication | Create a platform application. | To be tested |
|  | ListApplications | Query the application platform list. | To be tested |
| Data Source Management | DeleteDataSource |  | To be tested |
|  | ShowDataSources |  | To be tested |
|  | UpdateDataSource |  | To be tested |
|  | CreateDataSource |  | To be tested |
| Data synchronization task management | CreateDataSyncTask |  | To be tested |
|  | SwitchoverDataSyncTask |  | To be tested |
|  | ShowDataSyncTask |  | To be tested |
|  | ShowDataSyncTasks |  | To be tested |
|  | DeleteDataSyncTask |  | To be tested |
|  | ShowDataSource |  | To be tested |
| Database connection pool management | UpdateDbConnectionPool |  | To be tested |
|  | ShowDbConnectionPool |  | To be tested |
|  | CreateDbConnectionPool |  | To be tested |
| ETCD Certificate | DownloadEtcdCert |  | To be tested |
| Equipment Room Monitor | ShowDcMonitor |  | To be tested |
|  | ResetDcMonitor |  | To be tested |
| Exclusive Instance Management | CreateInstance | Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore | To be tested |
|  | DeleteInstance | Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
|  | ShowInstance | Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
| Global Configuration | ShowGlobalConf |  | To be tested |
|  | UpdateGlobalConf |  | To be tested |
|  | DeleteGlobalConf |  | To be tested |
|  | SetGlobalConf |  | To be tested |
| Instance Management | DeployInstance |  | To be tested |
|  | ShowStatisticalData |  | To be tested |
| Key Management | ShowSecret |  | To be tested |
|  | SetSecret |  | To be tested |
|  | DeleteSecret |  | To be tested |
| Lifecycle Management | UpdateInstance | Modifies the name and description of an instance. | To be tested |
|  | ListInstances | Query the instance list of a tenant. Query by condition is supported. | To be tested |
| Module Management | EnableActivateModule |  | To be tested |
|  | ShowModule |  | To be tested |
|  | DeleteModule |  | To be tested |
|  | UpdateModule |  | To be tested |
| Monitoring management | SetMonitorGlobalConfig |  | To be tested |
|  | UpdateMonitor |  | To be tested |
|  | SwitchMonitor |  | To be tested |
|  | ShowMonitorGlobalConfig |  | To be tested |
|  | ListMonitors |  | To be tested |
|  | ShowMonitor |  | To be tested |
|  | ShowOverallMonitors |  | To be tested |
|  | CreateMonitor |  | To be tested |
| Namespace management | ShowNamespacesById |  | To be tested |
|  | UpdateNameSpace |  | To be tested |
|  | ShowNameSpaceList |  | To be tested |
| One-click application switchover | BatchSwitchMonitor |  | To be tested |
|  | ListSwitchJobs |  | To be tested |
|  | ListBatchSwitchDetail |  | To be tested |
|  | DeleteAppSwitchJopNote |  | To be tested |
| Organization Management | CreateNamespace | Create an organization | To be tested |

