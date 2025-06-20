# Kafka MCP Server 


## Version
v0.1.0

## Overview

Kafka MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service Kafka. Full-chain management of Kafka resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| App Permission Management | UpdateTopicAccessPolicy | Update the topic permission. | To be tested |
| Background Task Management | ShowBackgroundTask | Query the specified record in the background task management. | To be tested |
|  | ListBackgroundTasks | Query the background task list of an instance. | To be tested |
|  | DeleteBackgroundTask | Delete a specified record in background task management. | To be tested |
| Consumer group management | DeleteInstanceConsumerGroup | Delete a consumer group. | To be tested |
|  | ResetMessageOffsetWithEngine | The consumption progress cannot be reset online. The reset consumer group client must be stopped before the reset consumption progress can be performed. | To be tested |
|  | DeleteConsumerGroupOffsets | Delete the consumption location of the consumer group in the specified topic. | To be tested |
|  | CreateKafkaConsumerGroup | Creating a consumer group for an instance | To be tested |
|  | ListInstanceConsumerGroupMessageOffset | Query the message location of a consumer group. | To be tested |
|  | ListInstanceConsumerGroups | Query the consumer group list. | To be tested |
|  | UpdateInstanceConsumerGroup | Modifies a specified consumer group. | To be tested |
|  | BatchDeleteGroup | This API is used to delete consumer groups from a Kafka instance in batches. | To be tested |
|  | ListInstanceConsumerGroupTopics | Query topics of a specified consumer group. | To be tested |
|  | ShowGroups | Query consumer group information. | To be tested |
|  | UpdateInstanceGroup | Modify all consumer groups. | To be tested |
|  | ListInstanceConsumerGroup | Query the specified consumer group. | To be tested |
|  | ListInstanceConsumerGroupMembers | Query the consumption members of a specified consumer group. | To be tested |
| Diagnosis Management | ShowDiagnosisPreCheck | Message stacking diagnosis pre-check | To be tested |
|  | ShowMessageDiagnosisReport | Query diagnosis report details | To be tested |
|  | CreateMessageDiagnosisTask | Create a message stack diagnosis task. | To be tested |
|  | ListMessageDiagnosisReports | Query the message backlog diagnosis report list | To be tested |
|  | BatchDeleteMessageDiagnosisReports | Deletion of messages stacked in batches | To be tested |
| Exclusive Instance Management | ShowInstance | Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
|  | DeleteInstance | Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
| Instance Management | ShowCoordinators | Query the coordinator information of the Kafka instance. | To be tested |
|  | UpdateKafkaPortProtocol | Change the internal or public network access mode of the Kafka. | To be tested |
|  | CreateKafkaReassignmentTask | This API is used to submit a partition balancing task to the Kafka instance. If the task is submitted successfully, the job ID of the partition balancing task is returned. | To be tested |
|  | ShowKafkaTopicPartitionDiskusage | Query the disk usage of a topic on the broker. | To be tested |
|  | CreateReassignmentTask | This API is used to submit a partition balancing task to a Kafka instance or calculate the estimated partition balancing time. | To be tested |
|  | ResetManagerPassword | Reset the Manager password. | To be tested |
|  | ResetPassword | Reset the password (only for instances with SSL enabled). | To be tested |
|  | DeleteKafkaUserClientQuotaTask | This interface is used to submit a user- and client-level flow control task to the Kafka instance. If the task is successfully deleted, the job_id of the flow control task is returned. | To be tested |
|  | RestartManager | Restart Manager. | To be tested |
|  | CreateKafkaUserClientQuotaTask | This API is used to submit a user- and client-level flow control task to the Kafka instance. If the task is successfully created, the job_id of the flow control task is returned. | To be tested |
|  | UpdateInstanceAutoCreateTopic | Enables or disables the function of automatically creating topics for an instance. | To be tested |
|  | ShowCluster | Query Kafka cluster metadata. | To be tested |
|  | CloseKafkaManager | After Kafka Manager is disabled, the original management interfaces are unavailable. | To be tested |
|  | UpdateInstanceCrossVpcIp | Change the internal IP address for cross-VPC access of an instance. | To be tested |
|  | UpdateTopicReplica | Modifies the copy of the topic partition of the Kafka instance. | To be tested |
|  | UpdateKafkaUserClientQuotaTask | This API is used to submit a user- and client-level flow control task to a Kafka instance. If the task is successfully submitted, the job_id of the flow control task is returned. | To be tested |
|  | ShowKafkaUserClientQuota | This interface is used to query the flow control configuration from the Kafka instance. If the query is successful, the flow control configuration list is returned. | To be tested |
| Lifecycle Management | ShowInstanceConfigs | Obtains the instance configuration. | To be tested |
|  | BatchRestartOrDeleteInstances | Restart or delete instances in batches. | To be tested |
|  | EnableDns | Enable the RocketMQ instance domain name access capability. | To be tested |
|  | UpdateInstance | Modifies the name and description of an instance. | To be tested |
|  | CreateInstanceByEngine | This API is used to create an instance in pay-per-use or yearly/monthly mode. | To be tested |
|  | ModifyInstanceConfigs | Modify the instance configuration. | To be tested |
|  | CreatePostPaidKafkaInstance | Create an instance. | To be tested |
|  | UpgradeInstance | Upgrading the Instance Kernel | To be tested |
|  | ListInstances | Query the instance list of a tenant. Query by condition is supported. | To be tested |
| Message management | ShowPartitionEndMessage | Query the location of the latest messages in the partition. | To be tested |
|  | ShowInstanceMessages | Query the offset and content of a message. | To be tested |
|  | ShowMessages | Query the messages generated in a specified period of time in a partition. | To be tested |
|  | ShowPartitionBeginningMessage | Query the location of the earliest message in the partition. | To be tested |
|  | ShowPartitionMessage | Query the message of the specified offset of the partition. | To be tested |
|  | DeleteKafkaMessage | Kafka deletes a message. | To be tested |
| Other interfaces | ListAvailableZones | When creating an instance, you need to configure the ID of the AZ where the instance is located. You can use this API to query the ID of the AZ. | To be tested |
|  | ShowKafkaProductCores | Query the number of cores of the Kafka product specification. | To be tested |
|  | ShowCesHierarchy | Query the monitoring hierarchy of instances in CES. | To be tested |
|  | ListEngineProducts | Query the product specification list of the corresponding engine. | To be tested |
|  | ShowMaintainWindows | Query the start time and end time of the maintenance time window. | To be tested |
| Smart Connect | PauseConnectorTask | Suspend the Smart Connect task. | To be tested |
|  | RestartConnectorTask | Starts Smart Connect tasks that are not started and restarts suspended or running Smart Connect tasks. Note that restarting the Smart Connect task resets the synchronization progress and restarts the synchronization task. | To be tested |
|  | ShowConnectorTask | Query Smart Connector task details. | To be tested |
|  | DeleteConnector | This section describes how to disable Smart Connect for a pay-per-use instance. | To be tested |
|  | ListConnectorTasks | Query the Smart Connect task list. | To be tested |
|  | DeleteConnectorTask | Delete the Smart Connector task. | To be tested |
|  | ResumeConnectorTask | Start the suspended Smart Connect task. | To be tested |
|  | CreateConnector | Enable Smart Connect and submit the task for creating Smart Connect nodes. | To be tested |
|  | CreateConnectorTask | Create a Smart Connect task. | To be tested |
| Specification Change Management | ShowEngineInstanceExtendProductInfo | Query the scaled-up specifications of a DB instance. | To be tested |
|  | ShowKafkaInstanceExtendProductInfo | Query the scale-up specifications of a DB instance. | To be tested |
|  | ResizeKafkaInstance | This API is used to change the instance specification. Currently, only on-demand instances can be scaled up by calling APIs. | To be tested |
|  | ResizeEngineInstance | This API is used to change the instance specification. Currently, only on-demand instances can be scaled up by calling APIs. | To be tested |
| Subject Management | DeleteKafkaTopicQuota | This API is used to submit a topic-level flow control task to the Kafka instance. If the task is successfully deleted, the job ID of the flow control task is returned. | To be tested |
|  | ListTopicPartitions | Query the partition list of a topic | To be tested |
|  | ShowInstanceTopicDetail | Query details about a Kafka instance topic. (A single instance cannot be invoked every 1s.) | To be tested |
|  | CreateInstanceTopic | This API is used to create a topic for a Kafka instance. | To be tested |
|  | CreateKafkaTopicQuota | This API is used to submit a topic-level flow control task to the Kafka instance. If the creation is successful, the job_id of the flow control task is returned. | To be tested |
|  | ShowKafkaTopicQuota | This interface is used to query topic-level flow control tasks. | To be tested |
|  | ListTopicProducers | Query the producer list of a topic. | To be tested |
|  | SendKafkaMessage | Send a specified message to the Kafka instance on the console. | To be tested |
|  | ListInstanceTopics | This API is used to query topic details of a specified Kafka instance. | To be tested |
|  | UpdateInstanceTopic | Modifying a Kafka Instance Topic | To be tested |
|  | ModifyKafkaTopicQuota | This API is used to submit a topic-level flow control task to the Kafka instance. If the task is successfully submitted, the job_id of the flow control task is returned. | To be tested |
|  | BatchDeleteInstanceTopic | This API is used to delete topics from Kafka instances in batches. When multiple topics are deleted in batches, some topics are successfully deleted and some topics fail to be deleted. In this case, the interface returns a message indicating that the deletion is successful and the information about the topics that fail to be deleted is displayed in the message. | To be tested |
| Tag Management | BatchCreateOrDeleteKafkaTag | Add or delete instance tags in batches. | To be tested |
|  | ShowKafkaProjectTags | Query project tags. | To be tested |
|  | ShowKafkaTags | Query the instance tag. | To be tested |
| User management | CreateInstanceUser | User for creating Kafka instances. You can connect to Kafka instances with SASL enabled. For Kafka instances created before July 15, 2023, a maximum of 20 users can be created for each instance. For Kafka instances created on July 15, 2023 or later, a maximum of 500 users can be created for each instance. | To be tested |
|  | ShowTopicAccessPolicy | Query user permissions. | To be tested |
|  | UpdateInstanceUser | Modifying user parameters | To be tested |
|  | BatchDeleteInstanceUsers | User for deleting Kafka instances in batches. | To be tested |
|  | ShowInstanceUsers | Query the user list. | To be tested |
|  | ResetUserPasswrod | Resetting the user password | To be tested |

