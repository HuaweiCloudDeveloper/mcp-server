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
                    <td rowspan="2">Application操作</td>
                    <td>CreateApplication</td>
                    <td>创建平台应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplications</td>
                    <td>查询应用平台列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ETCD证书</td>
                    <td>DownloadEtcdCert</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">全局配置</td>
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
                    <td rowspan="3">命名空间管理</td>
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
                    <td rowspan="2">实例管理</td>
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
                    <td rowspan="3">密钥管理</td>
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
                    <td rowspan="4">应用一键切换</td>
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
                    <td rowspan="1">应用管理</td>
                    <td>DeleteApplications</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">数据同步任务管理</td>
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
                    <td rowspan="3">数据库连接池管理</td>
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
                    <td rowspan="4">数据源管理</td>
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
                    <td rowspan="2">机房级监控器</td>
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
                    <td rowspan="4">模块管理</td>
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
                    <td rowspan="3">独享实例管理</td>
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
                    <td>ShowInstance</td>
                    <td>查询WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">生命周期管理</td>
                    <td>UpdateInstance</td>
                    <td>修改实例的名称和描述信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>查询租户的实例列表,支持按照条件查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">监控管理</td>
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
                    <td rowspan="1">组织管理</td>
                    <td>CreateNamespace</td>
                    <td>创建组织</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
