# EG MCP Server 

## 版本信息
v0.1.0

## 产品描述

EG MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务EG交互的能力。可以基于自然语言对EG资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| API版本管理 | ListApiVersions | 获取服务支持的API版本列表。 | To be tested |
| obs桶管理 | ListObsBuckets | 获取obs桶列表。 | To be tested |
|  | Refurbishobs | 翻新obs fg触发器,创建为EG订阅 | To be tested |
| 事件模型管理 | ListEventSchema | 查询事件模型列表,包括系统事件模型和自定义事件模型 | To be tested |
|  | UpdateEventSchema | 更新自定义事件模型定义 | To be tested |
|  | CreateEventSchema | 创建自定义事件模型 | To be tested |
|  | DiscoverEventSchemaFromData | 事件模型自动发现 | To be tested |
|  | ListEventSchemaVersions | 查询事件模型版本列表 | To be tested |
|  | CreateEventSchemaVersion | 创建自定义事件模型版本,版本号后台自动生成 | To be tested |
|  | DeleteEventSchema | 删除事件模型 | To be tested |
|  | DeleteEventSchemaVersion | 删除事件模型指定版本 | To be tested |
|  | ShowDetailOfEventSchema | 查询事件模型详情 | To be tested |
|  | ShowDetailOfEventSchemaVersion | 查询事件模型指定版本详情 | To be tested |
| 事件流管理 | DeleteEventStreaming | 删除事件流。 | To be tested |
|  | UpdateEventStreaming | 更新事件流。 | To be tested |
|  | CreateEventStreaming | 创建事件流。 | To be tested |
|  | ShowEventStreaming | 查询事件流详情。 | To be tested |
|  | ListEventStreaming | 查询事件流列表。 | To be tested |
|  | ResumeEventStreaming | 操作事件流。 | To be tested |
| 事件源管理 | ShowDetailOfEventSource | 查询事件源详情信息。 | To be tested |
|  | CreateEventSource | 创建用户自定义类型的事件源,只能指定自定义通道,不能指定系统通道。 | To be tested |
|  | ListEventSources | 支持条件查询,如可以指定事件通道ID来查询某个事件通道下的所有事件源。 | To be tested |
|  | DeleteEventSource | 删除指定的自定义事件源。 | To be tested |
|  | UpdateEventSource | 更新自定义事件源定义。 | To be tested |
| 事件目标分类管理 | ListEventTarget | 查询预置的事件目标分类,获取每个事件目标分类的字段定义。 | To be tested |
| 事件示例管理 | ShowListOfEventSample | 查询事件示例列表 | To be tested |
| 事件管理 | PutOfficialEvents | 发布官方事件到事件通道。 | To be tested |
|  | ListTracedEvents | 查询事件追踪列表。 | To be tested |
|  | CheckPutEvents | 发布事件到事件源成功需要有订阅等条件,预先校验。 | To be tested |
|  | ShowDetailOfEvent | 根据事件ID查询事件详情。 | To be tested |
|  | PutEvents | 发布事件到事件通道,仅供调试使用。 | To be tested |
|  | ShowDetailOfEventTrace | 事件轨迹详情,展示事件源到投递目标的投递情况。 | To be tested |
| 事件订阅管理 | ShowDetailOfSubscriptionTarget | 查询事件订阅目标详情。 | To be tested |
|  | ExecuteSubscriptionOperation | 操作事件订阅,支持启用、禁用。 | To be tested |
|  | UpdateSubscriptionSource | 更新事件订阅源定义。 | To be tested |
|  | CreateSubscriptionTarget | 创建单个事件订阅目标。 | To be tested |
|  | ListSubscriptions | 查询事件订阅列表,支持指定事件通道。 | To be tested |
|  | UpdateSubscriptionTarget | 更新事件订阅目标定义。 | To be tested |
|  | CreateSubscription | 创建事件订阅。 | To be tested |
|  | DeleteSubscriptionTarget | 删除事件订阅目标。 | To be tested |
|  | DeleteSubscription | 删除事件订阅。 | To be tested |
|  | UpdateSubscription | 更新事件订阅定义。 | To be tested |
|  | ShowDetailOfSubscription | 查询事件订阅详情。 | To be tested |
| 事件通道管理 | UpdateChannel | 更新自定义事件通道定义。 | To be tested |
|  | CreateChannel | 创建自定义事件通道。 | To be tested |
|  | ListChannels | 查询事件通道列表,包括系统通道和自定义通道。 | To be tested |
|  | ShowDetailOfChannel | 查询指定事件通道详情。 | To be tested |
|  | DeleteChannel | 删除指定自定义事件通道。 | To be tested |
| 服务委托管理 | ListAgencies | 查询服务委托。 | To be tested |
|  | CreateAgencies | 按照业务场景,一键创建服务委托授权。 | To be tested |
| 特性管理 | QuerySupportFeature | 查询当前用户项目支持特性。 | To be tested |
| 监控指标管理 | ListSubMetrics | 查询事件订阅监控指标数据。 | To be tested |
|  | ListPubMetrics | 查询事件通道监控指标数据。 | To be tested |
| 目标连接管理 | ShowDetailOfConnection | 查询目标连接详情。 | To be tested |
|  | UpdateConnection | 更新目标连接。 | To be tested |
|  | CreateConnection | 创建目标连接。 | To be tested |
|  | ListConnections | 查询目标连接列表。 | To be tested |
|  | DeleteConnection | 删除目标连接。 | To be tested |
| 触发器管理 | ListWorkflowTriggers | 查询触发器,支持指定函数流id,一个以函数流id为目标的订阅为一个触发器。 | To be tested |
|  | ListTriggers | 查询触发器,支持指定函数urn,一个以函数urn为目标的订阅为一个触发器。 | To be tested |
| 访问端点管理 | UpdateEndpoint | 更新访问端点。 | To be tested |
|  | ListEndpoints | 查询访问端点。 | To be tested |
|  | CreateEndpoint | 创建访问端点。 | To be tested |
|  | DeleteEndpoint | 删除访问端点。 | To be tested |
| 配额管理 | ListQuotas | 查询当前租户的配额,未特殊配置过的会返回默认配额。 | To be tested |
