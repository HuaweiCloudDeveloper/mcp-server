# BCS MCP Server 


## Version
v0.1.0

## Overview

BCS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service BCS. Full-chain management of BCS resources can be carried out based on natural language.

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
                    <td rowspan="5">BCS监控</td>
                    <td>ListBcsMetric</td>
                    <td>该接口用于查询BCS服务的监控数据,可以指定相应的指标名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceMetric</td>
                    <td>该接口用于BCS组织实例监控数据详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBcsEventsStatistic</td>
                    <td>该接口用于查询BCS服务的分段事件、告警统计数据,可以指定查询时的过滤条件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEntityMetric</td>
                    <td>该接口用于查询BCS组织的监控数据列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBcsEvents</td>
                    <td>该接口用于查询BCS服务的事件、告警数据,可以指定查询时的过滤条件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="18">BCS管理</td>
                    <td>ShowBlockchainDetail</td>
                    <td>查询指定服务实例详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBlockchainCertByUserName</td>
                    <td>通过用户名生成指定服务实例组织用户证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBlockchainNodes</td>
                    <td>查询指定服务实例节点信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnfreezeCert</td>
                    <td>解冻指定服务实例组织用户证书,解冻后需等待半分钟到一分钟左右生效</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBlockchainFlavors</td>
                    <td>查询服务联盟链规格信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBlockchainStatus</td>
                    <td>查询指定服务实例创建状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRemoveOrgsFromChannel</td>
                    <td>该接口用于BCS组织退出某通道。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOpRecord</td>
                    <td>查询异步操作结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadBlockchainCert</td>
                    <td>下载指定服务实例相关证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBlockchain</td>
                    <td>删除bcs实例。包周期实例不支持</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNewBlockchain</td>
                    <td>创建BCS服务实例,只支持按需创建</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadBlockchainSdkConfig</td>
                    <td>下载指定服务实例SDK配置文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>FreezeCert</td>
                    <td>冻结指定服务实例组织用户证书,冻结后需等待半分钟到一分钟左右生效</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRemovePeersFromChannel</td>
                    <td>该接口用于BCS某个组织中的节点退出某通道。当节点为通道中最后一个节点时,需要使用组织退通道的接口来将通道中的最后一个节点退出。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateChannels</td>
                    <td>创建通道</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBlockchainChannels</td>
                    <td>查询指定服务实例通道信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddPeersToChannel</td>
                    <td>peer节点加入通道,目前仅支持往一个通道中加入peer</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBlockchains</td>
                    <td>查询当前项目下所有服务实例的简要信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">BCS联盟</td>
                    <td>HandleUnionMemberQuitList</td>
                    <td>被邀请方退出联盟</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>HandleNotification</td>
                    <td>处理联盟邀请</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchInviteMembersToChannel</td>
                    <td>批量邀请联盟成员加入通道,此操作会向被邀请方发出邀请通知</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMemberInvite</td>
                    <td>可通过此接口批量取消邀请或删除对已退出或拒绝加入或解散的成员邀请信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">事件通道管理</td>
                    <td>DeleteChannel</td>
                    <td>删除指定自定义事件通道。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">关键操作通知管理</td>
                    <td>ListNotifications</td>
                    <td>查询创建的关键操作通知规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">后端云服务器</td>
                    <td>ListMembers</td>
                    <td>查询属于某个后端云服务器组的后端云服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">生命周期管理</td>
                    <td>UpdateInstance</td>
                    <td>修改实例的名称和描述信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额管理</td>
                    <td>ListQuotas</td>
                    <td>获取配额信息</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
