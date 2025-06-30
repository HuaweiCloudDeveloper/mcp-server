# MAS MCP Server 


## Version
v0.1.0

## Overview

MAS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service MAS. Full-chain management of MAS resources can be carried out based on natural language.

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
                    <td rowspan="1">App Management</td>
                    <td>DeleteApplications</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Application operation</td>
                    <td>CreateApplication</td>
                    <td>Create a platform application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplications</td>
                    <td>Query the application platform list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Data Source Management</td>
                    <td>DeleteDataSource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataSources</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataSource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataSource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Data synchronization task management</td>
                    <td>CreateDataSyncTask</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchoverDataSyncTask</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataSyncTask</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataSyncTasks</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDataSyncTask</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataSource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Database connection pool management</td>
                    <td>UpdateDbConnectionPool</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDbConnectionPool</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDbConnectionPool</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ETCD Certificate</td>
                    <td>DownloadEtcdCert</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Equipment Room Monitor</td>
                    <td>ShowDcMonitor</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetDcMonitor</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Exclusive Instance Management</td>
                    <td>CreateInstance</td>
                    <td>Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Global Configuration</td>
                    <td>ShowGlobalConf</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGlobalConf</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGlobalConf</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetGlobalConf</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Instance Management</td>
                    <td>DeployInstance</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStatisticalData</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Key Management</td>
                    <td>ShowSecret</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetSecret</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecret</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Lifecycle Management</td>
                    <td>UpdateInstance</td>
                    <td>Modifies the name and description of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>Query the instance list of a tenant. Query by condition is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Module Management</td>
                    <td>EnableActivateModule</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowModule</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteModule</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateModule</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Monitoring management</td>
                    <td>SetMonitorGlobalConfig</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMonitor</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchMonitor</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonitorGlobalConfig</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMonitors</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonitor</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOverallMonitors</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMonitor</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Namespace management</td>
                    <td>ShowNamespacesById</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNameSpace</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNameSpaceList</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">One-click application switchover</td>
                    <td>BatchSwitchMonitor</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSwitchJobs</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBatchSwitchDetail</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppSwitchJopNote</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Organization Management</td>
                    <td>CreateNamespace</td>
                    <td>Create an organization</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
