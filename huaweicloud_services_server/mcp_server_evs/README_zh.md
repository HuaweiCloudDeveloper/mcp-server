# EVS MCP Server 


## Version
v0.1.0

## Overview

EVS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EVS. Full-chain management of EVS resources can be carried out based on natural language.

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
                    <td rowspan="11">云硬盘</td>
                    <td>RetypeVolume</td>
                    <td>对按需或者包周期云硬盘进行磁盘类型变更。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVolumes</td>
                    <td>查询所有云硬盘的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderListAvailabilityZones</td>
                    <td>查询所有的可用分区信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeVolume</td>
                    <td>对按需或者包周期云硬盘进行扩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVolume</td>
                    <td>删除一个云硬盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVolume</td>
                    <td>更新一个云硬盘的名称和描述。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnsubscribePostpaidVolume</td>
                    <td>退订包周期计费模式的云硬盘,有如下约束:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyVolumeQoS</td>
                    <td>调整云硬盘的iops或者吞吐量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVolume</td>
                    <td>创建按需或包周期云硬盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderListQuotas</td>
                    <td>查询租户的详细配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderListVolumeTypes</td>
                    <td>查询云硬盘类型列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">云硬盘快照</td>
                    <td>RollbackSnapshot</td>
                    <td>将快照数据回滚到云硬盘。支持企业项目授权功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshots</td>
                    <td>查询云硬盘快照详细列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSnapshot</td>
                    <td>删除云硬盘快照。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSnapshot</td>
                    <td>创建云硬盘快照。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSnapshot</td>
                    <td>查询单个云硬盘快照信息。支持企业项目授权功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSnapshot</td>
                    <td>更新云硬盘快照。支持企业项目授权功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">云硬盘标签</td>
                    <td>ShowVolumeTags</td>
                    <td>查询指定云硬盘的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVolumeTags</td>
                    <td>获取某个租户的所有云硬盘资源的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVolumesByTags</td>
                    <td>通过标签查询云硬盘资源实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateVolumeTags</td>
                    <td>为指定云硬盘批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteVolumeTags</td>
                    <td>为指定云硬盘批量删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">云硬盘过户</td>
                    <td>CinderDeleteVolumeTransfer</td>
                    <td>当云硬盘过户未被接受时,您可以删除云硬盘过户记录,接受后则无法执行删除操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderListVolumeTransfers</td>
                    <td>查询当前租户下所有云硬盘的过户记录列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderCreateVolumeTransfer</td>
                    <td>指定云硬盘来创建云硬盘过户记录,创建成功后,会返回过户记录ID以及身份认证密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderShowVolumeTransfer</td>
                    <td>查询单个云硬盘的过户记录详情,比如过户记录创建时间、ID以及名称等信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderAcceptVolumeTransfer</td>
                    <td>通过云硬盘过户记录ID以及身份认证密钥来接受云硬盘过户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询密钥API版本信息</td>
                    <td>ShowVersion</td>
                    <td>- 功能介绍:查指定API版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询版本操作</td>
                    <td>ListVersions</td>
                    <td>查询SMN开放API支持的版本号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">边缘硬盘</td>
                    <td>ShowVolume</td>
                    <td>查询硬盘详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像任务</td>
                    <td>ShowJob</td>
                    <td>该接口为扩展接口,主要用于查询异步接口执行情况,比如查询导出镜像任务的执行状态。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
