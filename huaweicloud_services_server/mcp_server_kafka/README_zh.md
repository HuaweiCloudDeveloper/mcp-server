# Kafka MCP Server 

## 版本信息
v0.1.0

## 产品描述

Kafka MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务Kafka交互的能力。可以基于自然语言对Kafka资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Smart Connect | PauseConnectorTask | 暂停Smart Connect任务。 | To be tested |
|  | RestartConnectorTask | 用于**启动未启动的Smart Connect任务**以及**重启已暂停或者运行中的Smart Connect任务**。注意,重启Smart Connect任务将重置同步进度,并重新开始同步任务。 | To be tested |
|  | ShowConnectorTask | 查询Smart Connector任务详情。 | To be tested |
|  | DeleteConnector | 介绍按需实例如何关闭Smart Connect。 | To be tested |
|  | ListConnectorTasks | 查询Smart Connect任务列表。 | To be tested |
|  | DeleteConnectorTask | 删除Smart Connector任务。 | To be tested |
|  | ResumeConnectorTask | 启动已暂停的Smart Connect任务。 | To be tested |
|  | CreateConnector | 开启Smart Connect,提交创建Smart Connect节点任务。 | To be tested |
|  | CreateConnectorTask | 创建Smart Connect任务。 | To be tested |
| 主题管理 | DeleteKafkaTopicQuota | 该接口用于向Kafka实例提交删除topic级别的流控任务,若成功则返回流控任务的job_id。 | To be tested |
|  | ListTopicPartitions | 查询Topic的分区列表 | To be tested |
|  | ShowInstanceTopicDetail | 查询Kafka实例Topic详细信息。(单个实例调用不要超过1s一次) | To be tested |
|  | CreateInstanceTopic | 该接口用于向Kafka实例创建Topic。 | To be tested |
|  | CreateKafkaTopicQuota | 该接口用于向Kafka实例提交创建topic级别的流控任务,若成功则返回流控任务的job_id。 | To be tested |
|  | ShowKafkaTopicQuota | 该接口用于查询topic级别的流控任务。 | To be tested |
|  | ListTopicProducers | 查询Topic的当前生产者列表。 | To be tested |
|  | SendKafkaMessage | 在控制台发送指定消息到Kafka实例 | To be tested |
|  | ListInstanceTopics | 该接口用于查询指定Kafka实例的Topic详情。 | To be tested |
|  | UpdateInstanceTopic | 修改Kafka实例Topic | To be tested |
|  | ModifyKafkaTopicQuota | 该接口用于向Kafka实例提交修改topic级别的流控任务,若成功则返回流控任务的job_id。 | To be tested |
|  | BatchDeleteInstanceTopic | 该接口用于向Kafka实例批量删除Topic。批量删除多个Topic时,部分删除成功,部分失败,此时接口返回删除成功,并在返回中显示删除失败的Topic信息。 | To be tested |
| 其他接口 | ListAvailableZones | 在创建实例时,需要配置实例所在的可用区ID,可通过该接口查询可用区的ID。 | To be tested |
|  | ShowKafkaProductCores | 查询Kafka产品规格核数。 | To be tested |
|  | ShowCesHierarchy | 查询实例在CES的监控层级关系。 | To be tested |
|  | ListEngineProducts | 查询产品规格列表。 | To be tested |
|  | ShowMaintainWindows | 查询维护时间窗开始时间和结束时间。 | To be tested |
| 后台任务管理 | ShowBackgroundTask | 查询后台任务管理中的指定记录。 | To be tested |
|  | ListBackgroundTasks | 查询实例的后台任务列表。 | To be tested |
|  | DeleteBackgroundTask | 删除后台任务管理中的指定记录。 | To be tested |
| 实例管理 | ShowCoordinators | 查询Kafka实例的协调器信息。 | To be tested |
|  | UpdateKafkaPortProtocol | 修改Kafka的内网或者公网接入方式。 | To be tested |
|  | CreateKafkaReassignmentTask | 该接口用于向Kafka实例提交分区平衡任务,若成功则返回分区平衡任务的job id。 | To be tested |
|  | ShowKafkaTopicPartitionDiskusage | 查询topic在Broker上磁盘占用情况。 | To be tested |
|  | CreateReassignmentTask | 该接口用于向Kafka实例提交分区平衡任务或计算分区平衡预估时间。 | To be tested |
|  | ResetManagerPassword | 重置Manager密码。 | To be tested |
|  | ResetPassword | 重置密码(只针对开通SSL的实例)。 | To be tested |
|  | DeleteKafkaUserClientQuotaTask | 该接口用于向Kafka实例提交删除用户、客户端级别的流控任务,若成功则返回流控任务的job_id。 | To be tested |
|  | RestartManager | 重启Manager。 | To be tested |
|  | CreateKafkaUserClientQuotaTask | 该接口用于向Kafka实例提交创建用户、客户端级别的流控任务,若成功则返回流控任务的job_id。 | To be tested |
|  | UpdateInstanceAutoCreateTopic | 开启或关闭实例自动创建topic功能。 | To be tested |
|  | ShowCluster | 查询Kafka集群元数据信息。 | To be tested |
|  | CloseKafkaManager | 关闭Kafka Manager,相应的原来开放出的management相关接口也将不可用。 | To be tested |
|  | UpdateInstanceCrossVpcIp | 修改实例跨VPC访问的内网IP。 | To be tested |
|  | UpdateTopicReplica | 修改Kafka实例Topic分区的副本。 | To be tested |
|  | UpdateKafkaUserClientQuotaTask | 该接口用于向Kafka实例提交修改用户、客户端级别的流控任务,若成功则返回流控任务的job_id。 | To be tested |
|  | ShowKafkaUserClientQuota | 该接口用于向Kafka实例查询流控的配置,若成功则返回流控配置的列表。 | To be tested |
| 标签管理 | BatchCreateOrDeleteKafkaTag | 批量添加或删除实例标签。 | To be tested |
|  | ShowKafkaProjectTags | 查询项目标签。 | To be tested |
|  | ShowKafkaTags | 查询实例标签。 | To be tested |
| 消息管理 | ShowPartitionEndMessage | 查询分区最新消息的位置。 | To be tested |
|  | ShowInstanceMessages | 查询消息的偏移量和消息内容。 | To be tested |
|  | ShowMessages | 查询分区指定时间段的消息。 | To be tested |
|  | ShowPartitionBeginningMessage | 查询分区最早消息的位置。 | To be tested |
|  | ShowPartitionMessage | 查询分区指定偏移量的消息。 | To be tested |
|  | DeleteKafkaMessage | Kafka删除消息。 | To be tested |
| 消费组管理 | DeleteInstanceConsumerGroup | 删除指定消费组。 | To be tested |
|  | ResetMessageOffsetWithEngine | Kafka实例不支持在线重置消费进度。在执行重置消费进度之前,必须停止被重置消费组客户端。 | To be tested |
|  | DeleteConsumerGroupOffsets | 删除消费组在指定Topic的消费位点。 | To be tested |
|  | CreateKafkaConsumerGroup | 实例创建消费组 | To be tested |
|  | ListInstanceConsumerGroupMessageOffset | 查询消费组消息位点。 | To be tested |
|  | ListInstanceConsumerGroups | 查询所有消费组。 | To be tested |
|  | UpdateInstanceConsumerGroup | 修改指定消费组。 | To be tested |
|  | BatchDeleteGroup | 该接口用于向Kafka实例批量删除消费组。 | To be tested |
|  | ListInstanceConsumerGroupTopics | 查询指定消费组的Topic。 | To be tested |
|  | ShowGroups | 查询消费组信息。 | To be tested |
|  | UpdateInstanceGroup | 修改所有消费组。 | To be tested |
|  | ListInstanceConsumerGroup | 查询指定消费组。 | To be tested |
|  | ListInstanceConsumerGroupMembers | 查询指定消费组的消费成员。 | To be tested |
| 生命周期管理 | ShowInstanceConfigs | 获取实例配置。 | To be tested |
|  | BatchRestartOrDeleteInstances | 批量重启或删除实例。 | To be tested |
|  | EnableDns | 开启Kafka实例域名访问后,客户端可以通过域名连接Kafka实例。 | To be tested |
|  | ShowInstance | 查询指定实例的详细信息。 | To be tested |
|  | UpdateInstance | 修改实例信息。 | To be tested |
|  | CreateInstanceByEngine | 创建实例。 | To be tested |
|  | ModifyInstanceConfigs | 修改实例配置。 | To be tested |
|  | DeleteInstance | 删除指定的实例,释放该实例的所有资源。 | To be tested |
|  | CreatePostPaidKafkaInstance | 创建实例。 | To be tested |
|  | UpgradeInstance | 实例内核升级 | To be tested |
|  | ListInstances | 查询租户的实例列表,支持按照条件查询。 | To be tested |
| 用户管理 | CreateInstanceUser | 创建Kafka实例的用户,用户可连接开启SASL的Kafka实例。  2023年7月15日前创建的Kafka实例,一个实例最多创建20个用户。2023年7月15日及以后创建的Kafka实例,一个实例最多创建500个用户。 | To be tested |
|  | UpdateTopicAccessPolicy | 设置用户权限。 | To be tested |
|  | ShowTopicAccessPolicy | 查询用户权限。 | To be tested |
|  | UpdateInstanceUser | 修改用户参数 | To be tested |
|  | BatchDeleteInstanceUsers | 批量删除Kafka实例的用户。 | To be tested |
|  | ShowInstanceUsers | 查询用户列表。 | To be tested |
|  | ResetUserPasswrod | 重置用户密码 | To be tested |
| 规格变更管理 | ShowEngineInstanceExtendProductInfo | 查询实例的扩容规格列表。 | To be tested |
|  | ShowKafkaInstanceExtendProductInfo | 查询实例的扩容规格列表。 | To be tested |
|  | ResizeKafkaInstance | 实例规格变更。当前通过调用API,只支持按需实例进行实例扩容。 | To be tested |
|  | ResizeEngineInstance | 实例规格变更。当前通过调用API,只支持按需实例进行实例扩容。 | To be tested |
| 诊断管理 | ShowDiagnosisPreCheck | 消息积压诊断预检查 | To be tested |
|  | ShowMessageDiagnosisReport | 查询诊断报告详情 | To be tested |
|  | CreateMessageDiagnosisTask | 创建消息积压诊断任务 | To be tested |
|  | ListMessageDiagnosisReports | 查询消息积压诊断报告列表 | To be tested |
|  | BatchDeleteMessageDiagnosisReports | 批量删除消息积压诊断报告 | To be tested |
