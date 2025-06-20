# RocketMQ MCP Server 

## 版本信息
v0.1.0

## 产品描述

RocketMQ MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务RocketMQ交互的能力。可以基于自然语言对RocketMQ资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Topic管理 | UpdateTopic | 修改主题。 | To be tested |
|  | ListConsumerGroupOfTopic | 查询主题消费组列表。 | To be tested |
|  | DeleteTopic | 删除指定主题。 | To be tested |
|  | ShowTopicStatus | 查询主题的消息数。 | To be tested |
|  | CreateTopicOrBatchDeleteTopic | 创建主题或批量删除主题。 | To be tested |
|  | ShowOneTopic | 查询单个主题。 | To be tested |
|  | ListRocketInstanceTopics | 该接口用于查询指定RocketMQ实例的Topic列表。 | To be tested |
| 元数据迁移 | ListRocketMqMigrationTask | 1. 查询实例下所有迁移任务 | To be tested |
|  | CreateRocketMqMigrationTask | 新建元数据迁移任务。 | To be tested |
|  | DeleteRocketMqMigrationTask | 删除元数据迁移任务。 | To be tested |
| 其他接口 | ListEngineProducts | 查询相应引擎的产品规格列表。 | To be tested |
|  | ListAvailableZones | 在创建实例时,需要配置实例所在的可用区ID,可通过该接口查询可用区的ID。 | To be tested |
|  | ShowRocketMQProductCores | 查询RocketMQ产品规格核数。 | To be tested |
| 参数管理 | UpdateRocketMqConfigs | 该接口用于修改RocketMQ配置。 | To be tested |
|  | ShowRocketMqConfigs | 该接口用于查询RocketMQ配置,若成功则返回配置的相关信息。 | To be tested |
| 实例管理 | ShowInstanceNodes | 查询实例节点信息。 | To be tested |
|  | RestartInstance | 重启指定实例。 | To be tested |
| 标签管理 | ShowRocketmqProjectTags | 查询项目标签。 | To be tested |
|  | BatchCreateOrDeleteRocketmqTag | 批量添加或删除实例标签。 | To be tested |
|  | ShowRocketmqTags | 查询实例标签。 | To be tested |
| 消息管理 | ExportDlqMessage | 导出死信消息。 | To be tested |
|  | ListMessages | 查询消息。 | To be tested |
|  | SendDlqMessage | 重发死信消息。 | To be tested |
|  | ListMessageTrace | 查询消息轨迹。 | To be tested |
|  | ValidateConsumedMessage | 消费验证。 | To be tested |
| 消费组管理 | UpdateConsumerGroup | 修改指定消费组参数。 | To be tested |
|  | ShowConsumerListOrDetails | 查询消费列表或详情。 | To be tested |
|  | ListInstanceConsumerGroups | 查询消费组列表。 | To be tested |
|  | ShowConsumerConnections | 查询消费组内消费者列表 | To be tested |
|  | DeleteConsumerGroup | 删除指定消费组。 | To be tested |
|  | CreateConsumerGroupOrBatchDeleteConsumerGroup | 创建消费组或批量删除消费组。 | To be tested |
|  | ResetConsumeOffset | 重置消费进度。 | To be tested |
|  | BatchUpdateConsumerGroup | 批量修改消费组。 | To be tested |
|  | ShowGroup | 查询指定消费组详情。 | To be tested |
| 生命周期管理 | ListBrokers | 查询代理列表。 | To be tested |
|  | EnableDns | 开启RocketMQ实例域名访问能力。 | To be tested |
|  | DeleteInstance | 删除指定的实例,释放该实例的所有资源。 | To be tested |
|  | UpdateInstance | 修改实例的名称和描述信息。 | To be tested |
|  | CreateInstanceByEngine | 创建实例,该接口支持创建按需和包周期两种计费方式的实例。 | To be tested |
|  | BatchDeleteInstances | 批量删除实例。**实例删除后,实例中原有的数据将被删除,且没有备份,请谨慎操作。** | To be tested |
|  | ShowInstance | 查询指定实例的详细信息。 | To be tested |
|  | ListInstances | 查询租户的实例列表,支持按照条件查询。 | To be tested |
| 用户管理 | ListUser | 查询用户列表。 | To be tested |
|  | UpdateUser | 修改用户参数。 | To be tested |
|  | ShowUser | 查询用户详情。 | To be tested |
|  | ListTopicAccessPolicy | 查询主题的授权用户列表。 | To be tested |
|  | CreateUser | 创建用户。 | To be tested |
|  | ListConsumeGroupAccessPolicy | 查询消费组的授权用户列表。 | To be tested |
|  | DeleteUser | 删除用户。 | To be tested |
| 规格变更管理 | ResizeInstance | 实例规格变更。 | To be tested |
|  | ShowEngineInstanceExtendProductInfo | 查询实例的扩容规格列表。 | To be tested |
