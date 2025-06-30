# SDRS MCP Server 


## Version
v0.1.0

## Overview

SDRS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SDRS. Full-chain management of SDRS resources can be carried out based on natural language.

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
                    <td rowspan="1">API版本信息</td>
                    <td>ShowSpecifiedApiVersion</td>
                    <td>查询存储容灾指定API版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job管理</td>
                    <td>ShowJobStatus</td>
                    <td>查询job的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">任务中心</td>
                    <td>DeleteServerGroupFailureJobs</td>
                    <td>删除指定保护组内的所有失败任务,创建保护实例失败、创建复制对失败、删除保护实例失败、删除复制对失败等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAllServerGroupFailureJobs</td>
                    <td>删除所有保护组层级的失败任务,创建、删除保护组失败等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFailureJob</td>
                    <td>删除单个失败任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFailureJobs</td>
                    <td>查询所有保护组失败任务列表或者指定保护组下的所有失败任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">保护实例</td>
                    <td>DeleteProtectedInstance</td>
                    <td>删除指定的保护实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProtectedInstance</td>
                    <td>查询单个保护实例的详细信息,如名称、ID等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateProtectedInstances</td>
                    <td>典型场景:没有特殊操作场景</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachProtectedInstanceReplication</td>
                    <td>将指定的复制对挂载到指定的保护实例上。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddProtectedInstanceNic</td>
                    <td>给指定的保护实例添加网卡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectedInstances</td>
                    <td>查询当前租户下的所有保护实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachProtectedInstanceReplication</td>
                    <td>将指定的复制对从指定的保护实例上卸载。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProtectedInstanceNic</td>
                    <td>删除指定保护实例的指定网卡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProtectedInstanceName</td>
                    <td>更新某一个保护实例的名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteProtectedInstances</td>
                    <td>典型场景:没有特殊操作场景</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProtectedInstance</td>
                    <td>创建保护实例。保护实例创建完成后,系统默认容灾站点云服务器名称与生产站点云服务器名称相同,但ID不同。如果需要修改云服务器名称,请在保护实例详情页面单击云服务器名称,进入云服务器详情页面进行修改</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeProtectedInstance</td>
                    <td>变更指定保护实例中弹性云服务器的规格,包括:同时变更生产站点云服务器和容灾站点云服务器的规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">保护组</td>
                    <td>StopProtectionGroup</td>
                    <td>对某一个保护组的停止保护操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartReverseProtectionGroup</td>
                    <td>对保护组进行切换操作,可以将保护组的当前生产站点,从创建保护组时指定的生产站点切换到创建保护组时指定的容灾站点,也可以从创建保护组时指定的容灾站点切换到创建保护组时指定的生产站点。切换后,生产站点和容灾站点的数据仍然处于被保护状态,只是复制方向与操作之前相反。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartFailoverProtectionGroup</td>
                    <td>当保护组的生产站点发生故障时,将保护组的生产站点切到当前的容灾站点,即另一端AZ,启用当前容灾站点的云硬盘以及云服务器等资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProtectionGroup</td>
                    <td>查询单个保护组的详细信息,如ID、名称等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProtectionGroup</td>
                    <td>删除指定的保护组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProtectionGroupName</td>
                    <td>更新某一个保护组的名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectionGroups</td>
                    <td>查询当前租户所有的保护组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartProtectionGroup</td>
                    <td>对某一个保护组的“开启保护”或“重保护”操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProtectionGroup</td>
                    <td>创建保护组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">复制对</td>
                    <td>ListReplications</td>
                    <td>查询指定保护组下的所有复制对列表,如果不给定指定保护组则查询当前租户下的所有复制对列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteReplication</td>
                    <td>删除指定的复制对。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateReplication</td>
                    <td>创建复制对,并将其添加到指定的保护组中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReplication</td>
                    <td>查询单个复制对的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateReplicationName</td>
                    <td>更新复制对名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandReplication</td>
                    <td>对复制对包含的两个磁盘进行扩容操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">大屏管理</td>
                    <td>ListRpoStatistics</td>
                    <td>查询当前租户大屏显示中,资源的RPO超标趋势记录列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">容灾演练</td>
                    <td>ShowDisasterRecoveryDrill</td>
                    <td>查询单个容灾演练的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDisasterRecoveryDrills</td>
                    <td>查询指定保护组下的所有容灾演练列表,当未指定保护组时查询当前租户下的所有容灾演练列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDisasterRecoveryDrill</td>
                    <td>创建容灾演练。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDisasterRecoveryDrill</td>
                    <td>删除指定的容灾演练。删除后:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDisasterRecoveryDrillName</td>
                    <td>更新容灾演练的名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询双活域</td>
                    <td>ListActiveActiveDomains</td>
                    <td>查询双活域。双活域由本端存储设备、远端存储设备组成,通过双活域,应用服务器可以实现跨站点的数据访问。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询版本操作</td>
                    <td>ListApiVersions</td>
                    <td>查询标签管理服务的API版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">标签管理</td>
                    <td>AddProtectedInstanceTags</td>
                    <td>一个保护实例上最多有10个标签。此接口为幂等接口:创建时,如果创建的标签已经存在(key相同),则覆盖。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectedInstancesByTags</td>
                    <td>使用标签过滤保护实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectedInstancesProjectTags</td>
                    <td>查询租户在指定Project中保护实例的所有资源标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectedInstanceTags</td>
                    <td>查询指定保护实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProtectedInstanceTag</td>
                    <td>幂等接口:删除时,不对标签字符集做校验,调用接口前必须要做encodeURI,服务端需要对接口URI做decodeURI。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddTags</td>
                    <td>为指定保护实例批量添加或删除标签。一个资源上最多有10个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTags</td>
                    <td>为指定保护实例批量删除标签。一个资源上最多有10个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowQuota</td>
                    <td>查询单租户在VPC服务下的网络资源配额,包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额,vpn配额等。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
