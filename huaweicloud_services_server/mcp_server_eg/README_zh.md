# EG MCP Server 


## Version
v0.1.0

## Overview

EG MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EG. Full-chain management of EG resources can be carried out based on natural language.

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
                    <td rowspan="2">obs桶管理</td>
                    <td>ListObsBuckets</td>
                    <td>获取obs桶列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Refurbishobs</td>
                    <td>翻新obs fg触发器,创建为EG订阅</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">事件模型管理</td>
                    <td>ListEventSchema</td>
                    <td>查询事件模型列表,包括系统事件模型和自定义事件模型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEventSchema</td>
                    <td>更新自定义事件模型定义</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEventSchema</td>
                    <td>创建自定义事件模型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DiscoverEventSchemaFromData</td>
                    <td>事件模型自动发现</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventSchemaVersions</td>
                    <td>查询事件模型版本列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEventSchemaVersion</td>
                    <td>创建自定义事件模型版本,版本号后台自动生成</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEventSchema</td>
                    <td>删除事件模型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEventSchemaVersion</td>
                    <td>删除事件模型指定版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailOfEventSchema</td>
                    <td>查询事件模型详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailOfEventSchemaVersion</td>
                    <td>查询事件模型指定版本详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">事件流管理</td>
                    <td>DeleteEventStreaming</td>
                    <td>删除事件流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEventStreaming</td>
                    <td>更新事件流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEventStreaming</td>
                    <td>创建事件流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEventStreaming</td>
                    <td>查询事件流详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventStreaming</td>
                    <td>查询事件流列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResumeEventStreaming</td>
                    <td>操作事件流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">事件源管理</td>
                    <td>ShowDetailOfEventSource</td>
                    <td>查询事件源详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEventSource</td>
                    <td>创建用户自定义类型的事件源,只能指定自定义通道,不能指定系统通道。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventSources</td>
                    <td>支持条件查询,如可以指定事件通道ID来查询某个事件通道下的所有事件源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEventSource</td>
                    <td>删除指定的自定义事件源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEventSource</td>
                    <td>更新自定义事件源定义。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">事件目标分类管理</td>
                    <td>ListEventTarget</td>
                    <td>查询预置的事件目标分类,获取每个事件目标分类的字段定义。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">事件示例管理</td>
                    <td>ShowListOfEventSample</td>
                    <td>查询事件示例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">事件管理</td>
                    <td>PutOfficialEvents</td>
                    <td>发布官方事件到事件通道。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTracedEvents</td>
                    <td>查询事件追踪列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckPutEvents</td>
                    <td>发布事件到事件源成功需要有订阅等条件,预先校验。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailOfEvent</td>
                    <td>根据事件ID查询事件详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PutEvents</td>
                    <td>发布事件到事件通道,仅供调试使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailOfEventTrace</td>
                    <td>事件轨迹详情,展示事件源到投递目标的投递情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">事件订阅管理</td>
                    <td>ShowDetailOfSubscriptionTarget</td>
                    <td>查询事件订阅目标详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteSubscriptionOperation</td>
                    <td>操作事件订阅,支持启用、禁用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubscriptionSource</td>
                    <td>更新事件订阅源定义。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubscriptionTarget</td>
                    <td>创建单个事件订阅目标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubscriptionTarget</td>
                    <td>更新事件订阅目标定义。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubscriptionTarget</td>
                    <td>删除事件订阅目标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubscription</td>
                    <td>删除事件订阅。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailOfSubscription</td>
                    <td>查询事件订阅详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">事件通道管理</td>
                    <td>UpdateChannel</td>
                    <td>更新自定义事件通道定义。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateChannel</td>
                    <td>创建自定义事件通道。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListChannels</td>
                    <td>查询事件通道列表,包括系统通道和自定义通道。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailOfChannel</td>
                    <td>查询指定事件通道详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteChannel</td>
                    <td>删除指定自定义事件通道。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">委托管理</td>
                    <td>ListAgencies</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定条件下的委托列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">服务委托管理</td>
                    <td>CreateAgencies</td>
                    <td>按照业务场景,一键创建服务委托授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">服务开通管理</td>
                    <td>ListSubscriptions</td>
                    <td>该接口用于获取服务开通信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubscription</td>
                    <td>此接口用于用户申请开通视频接入服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询版本操作</td>
                    <td>ListApiVersions</td>
                    <td>查询标签管理服务的API版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">特性管理</td>
                    <td>QuerySupportFeature</td>
                    <td>查询当前用户项目支持特性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">监控指标管理</td>
                    <td>ListSubMetrics</td>
                    <td>查询事件订阅监控指标数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPubMetrics</td>
                    <td>查询事件通道监控指标数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">目标连接管理</td>
                    <td>ShowDetailOfConnection</td>
                    <td>查询目标连接详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConnection</td>
                    <td>更新目标连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnection</td>
                    <td>创建目标连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConnections</td>
                    <td>查询目标连接列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnection</td>
                    <td>删除目标连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">终端节点功能</td>
                    <td>ListEndpoints</td>
                    <td>查询当前用户下的终端节点的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEndpoint</td>
                    <td>创建终端节点,以便访问终端节点服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEndpoint</td>
                    <td>删除终端节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">触发器管理</td>
                    <td>ListWorkflowTriggers</td>
                    <td>查询触发器,支持指定函数流id,一个以函数流id为目标的订阅为一个触发器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTriggers</td>
                    <td>查询触发器,支持指定函数urn,一个以函数urn为目标的订阅为一个触发器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">订阅操作</td>
                    <td>UpdateSubscription</td>
                    <td>更新订阅者备注。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">访问端点管理</td>
                    <td>UpdateEndpoint</td>
                    <td>更新访问端点。</td>
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
