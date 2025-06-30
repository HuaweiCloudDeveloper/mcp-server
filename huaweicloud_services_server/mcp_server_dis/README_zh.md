# DIS MCP Server 


## Version
v0.1.0

## Overview

DIS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DIS. Full-chain management of DIS resources can be carried out based on natural language.

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
                    <td rowspan="2">AppManagement</td>
                    <td>ShowApp</td>
                    <td>该接口用于用户查询应用详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApp</td>
                    <td>该接口用于用户创建应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">App管理</td>
                    <td>ListApp</td>
                    <td>本接口用于查询APP列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConsumerState</td>
                    <td>本接口用于查询APP消费状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Checkpoint管理</td>
                    <td>CommitCheckpoint</td>
                    <td>本接口用于提交Checkpoint。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCheckpoint</td>
                    <td>本接口用于删除Checkpoint。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCheckpoint</td>
                    <td>本接口用于查询Checkpoint详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListResourcesByTags</td>
                    <td>根据标签查询资源实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">主机管理</td>
                    <td>ListPolicies</td>
                    <td>查询主机策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">密钥标签管理</td>
                    <td>DeleteTag</td>
                    <td>- 功能介绍:删除密钥标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">应用模板管理</td>
                    <td>DeleteApp</td>
                    <td>删除应用模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">数据管理</td>
                    <td>SendRecords</td>
                    <td>本接口用于上传数据到DIS通道中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConsumeRecords</td>
                    <td>本接口用于从DIS通道中下载数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCursor</td>
                    <td>本接口用于获取数据游标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">标签管理</td>
                    <td>BatchDeleteTags</td>
                    <td>为指定保护实例批量删除标签。一个资源上最多有10个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStreamTags</td>
                    <td>该接口用于查询指定通道的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTag</td>
                    <td>为资源添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateTags</td>
                    <td>批量创建标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">监控管理</td>
                    <td>ShowPartitionMetrics</td>
                    <td>本接口用于查询通道指定分区的监控数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStreamMetrics</td>
                    <td>本接口用于查询指定通道的监控数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">视频流管理</td>
                    <td>ListStreams</td>
                    <td>此接口用于获取所有视频流的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStream</td>
                    <td>该接口用于创建视频流。包括RTMP以及HTTP-FLV类型视频流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStream</td>
                    <td>此接口用于删除指定视频流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStream</td>
                    <td>该接口用于更新视频流的详情,包括RTMP以及HTTP-FLV类型视频流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">转储任务管理</td>
                    <td>BatchStartTransferTask</td>
                    <td>此接口用于批量启动转储任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTransferTask</td>
                    <td>该接口用于删除转储任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTransferTask</td>
                    <td>查询转储任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopTransferTask</td>
                    <td>此接口用于批量暂停转储任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDliTransferTask</td>
                    <td>本接口用于添加DLI转储任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateObsTransferTask</td>
                    <td>本接口用于添加OBS转储任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTransferTasks</td>
                    <td>本接口用于查询转储任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMrsTransferTask</td>
                    <td>本接口用于添加MRS转储任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCloudTableTransferTask</td>
                    <td>本接口用于添加CloudTable转储任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDwsTransferTask</td>
                    <td>本接口用于添加DWS转储任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">通道管理</td>
                    <td>CreatePolicies</td>
                    <td>本接口用于给指定通道添加权限策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStream</td>
                    <td>本接口用于查询指定通道的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePartitionCount</td>
                    <td>本接口用于变更指定通道中的分区数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像标签</td>
                    <td>ListTags</td>
                    <td>根据不同条件查询镜像标签列表信息。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
