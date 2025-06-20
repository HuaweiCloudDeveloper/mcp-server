# RocketMQ MCP Server 


## Version
v0.1.0

## Overview

RocketMQ MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RocketMQ. Full-chain management of RocketMQ resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Consumer group management | UpdateConsumerGroup | Modifies the parameters of a specified consumer group. | To be tested |
|  | ShowConsumerListOrDetails | Query the consumption list or details. | To be tested |
|  | ListInstanceConsumerGroups | Query the consumer group list. | To be tested |
|  | ShowConsumerConnections | Query the consumer list in a consumer group | To be tested |
|  | DeleteConsumerGroup | Delete a consumer group. | To be tested |
|  | CreateConsumerGroupOrBatchDeleteConsumerGroup | Create a consumer group or delete consumer groups in batches. | To be tested |
|  | ResetConsumeOffset | Reset the consumption progress. | To be tested |
|  | BatchUpdateConsumerGroup | Modify consumer groups in batches. | To be tested |
|  | ShowGroup | Query the details of a specified consumer group. | To be tested |
| Exclusive Instance Management | DeleteInstance | Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
|  | ShowInstance | Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
| Instance Management | ShowInstanceNodes | Query the instance node information. | To be tested |
|  | RestartInstance | Restarts a specified instance. | To be tested |
| Lifecycle Management | ListBrokers | Query the proxy list. | To be tested |
|  | EnableDns | Enable the RocketMQ instance domain name access capability. | To be tested |
|  | UpdateInstance | Modifies the name and description of an instance. | To be tested |
|  | CreateInstanceByEngine | This API is used to create an instance in pay-per-use or yearly/monthly mode. | To be tested |
|  | BatchDeleteInstances | Delete instances in batches. After the instance is deleted, the original data in the instance will be deleted and no backup will be performed. Exercise caution when performing this operation. | To be tested |
|  | ListInstances | Query the instance list of a tenant. Query by condition is supported. | To be tested |
| Message management | ExportDlqMessage | Export dead letter messages. | To be tested |
|  | ListMessages | Query messages. | To be tested |
|  | SendDlqMessage | Resend a dead letter message. | To be tested |
|  | ListMessageTrace | Query the message track. | To be tested |
|  | ValidateConsumedMessage | Consumption verification. | To be tested |
| Metadata Migration | ListRocketMqMigrationTask | 1. Query all migration tasks in an instance. | To be tested |
|  | CreateRocketMqMigrationTask | Create a metadata migration task. | To be tested |
|  | DeleteRocketMqMigrationTask | Delete a metadata migration task. | To be tested |
| Other interfaces | ListEngineProducts | Query the product specification list of the corresponding engine. | To be tested |
|  | ListAvailableZones | When creating an instance, you need to configure the ID of the AZ where the instance is located. You can use this API to query the ID of the AZ. | To be tested |
|  | ShowRocketMQProductCores | Query the number of RocketMQ cores. | To be tested |
| Parameter Management | UpdateRocketMqConfigs | This interface is used to modify RocketMQ configurations. | To be tested |
|  | ShowRocketMqConfigs | This interface is used to query the RocketMQ configuration. If the query is successful, the configuration information is returned. | To be tested |
| Specification Change Management | ResizeInstance | The instance specification is changed. | To be tested |
|  | ShowEngineInstanceExtendProductInfo | Query the scaled-up specifications of a DB instance. | To be tested |
| Tag Management | ShowRocketmqProjectTags | Query project tags. | To be tested |
|  | BatchCreateOrDeleteRocketmqTag | Add or delete instance tags in batches. | To be tested |
|  | ShowRocketmqTags | Query the instance label. | To be tested |
| Topic management | ListConsumerGroupOfTopic | Query the consumer group list of the theme. | To be tested |
|  | ShowTopicStatus | Query the number of messages in the topic. | To be tested |
|  | CreateTopicOrBatchDeleteTopic | Create a topic or delete topics in batches. | To be tested |
|  | ShowOneTopic | Query a single topic. | To be tested |
|  | ListRocketInstanceTopics | This API is used to query the topic list of a specified RocketMQ instance. | To be tested |
| Topic operation | UpdateTopic | Update the display name. | To be tested |
|  | DeleteTopic | Delete a topic. | To be tested |
| User management | ListUser | Query the user list. | To be tested |
|  | UpdateUser | Modify user parameters. | To be tested |
|  | ShowUser | Query user details. | To be tested |
|  | ListTopicAccessPolicy | Query the list of authorized users of a topic. | To be tested |
|  | CreateUser | Create a user. | To be tested |
|  | ListConsumeGroupAccessPolicy | Query the authorized users of the consumer group. | To be tested |
|  | DeleteUser | Delete a user. | To be tested |

