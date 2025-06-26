# Kafka MCP Server 


## Version
v0.1.0

## Overview

Kafka MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service Kafka. Full-chain management of Kafka resources can be carried out based on natural language.

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
                    <td rowspan="1">App Permission Management</td>
                    <td>UpdateTopicAccessPolicy</td>
                    <td>Update the topic permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Background Task Management</td>
                    <td>ShowBackgroundTask</td>
                    <td>Query the specified record in the background task management.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackgroundTasks</td>
                    <td>Query the background task list of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackgroundTask</td>
                    <td>Delete a specified record in background task management.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">Consumer group management</td>
                    <td>DeleteInstanceConsumerGroup</td>
                    <td>Delete a consumer group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetMessageOffsetWithEngine</td>
                    <td>The consumption progress cannot be reset online. The reset consumer group client must be stopped before the reset consumption progress can be performed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConsumerGroupOffsets</td>
                    <td>Delete the consumption location of the consumer group in the specified topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKafkaConsumerGroup</td>
                    <td>Creating a consumer group for an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConsumerGroupMessageOffset</td>
                    <td>Query the message location of a consumer group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConsumerGroups</td>
                    <td>Query the consumer group list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConsumerGroup</td>
                    <td>Modifies a specified consumer group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteGroup</td>
                    <td>This API is used to delete consumer groups from a Kafka instance in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConsumerGroupTopics</td>
                    <td>Query topics of a specified consumer group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGroups</td>
                    <td>Query consumer group information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceGroup</td>
                    <td>Modify all consumer groups.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConsumerGroup</td>
                    <td>Query the specified consumer group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConsumerGroupMembers</td>
                    <td>Query the consumption members of a specified consumer group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Diagnosis Management</td>
                    <td>ShowDiagnosisPreCheck</td>
                    <td>Message stacking diagnosis pre-check</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMessageDiagnosisReport</td>
                    <td>Query diagnosis report details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMessageDiagnosisTask</td>
                    <td>Create a message stack diagnosis task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMessageDiagnosisReports</td>
                    <td>Query the message backlog diagnosis report list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteMessageDiagnosisReports</td>
                    <td>Deletion of messages stacked in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Exclusive Instance Management</td>
                    <td>ShowInstance</td>
                    <td>Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">Instance Management</td>
                    <td>ShowCoordinators</td>
                    <td>Query the coordinator information of the Kafka instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKafkaPortProtocol</td>
                    <td>Change the internal or public network access mode of the Kafka.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKafkaReassignmentTask</td>
                    <td>This API is used to submit a partition balancing task to the Kafka instance. If the task is submitted successfully, the job ID of the partition balancing task is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaTopicPartitionDiskusage</td>
                    <td>Query the disk usage of a topic on the broker.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateReassignmentTask</td>
                    <td>This API is used to submit a partition balancing task to a Kafka instance or calculate the estimated partition balancing time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetManagerPassword</td>
                    <td>Reset the Manager password.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPassword</td>
                    <td>Reset the password (only for instances with SSL enabled).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKafkaUserClientQuotaTask</td>
                    <td>This interface is used to submit a user- and client-level flow control task to the Kafka instance. If the task is successfully deleted, the job_id of the flow control task is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartManager</td>
                    <td>Restart Manager.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKafkaUserClientQuotaTask</td>
                    <td>This API is used to submit a user- and client-level flow control task to the Kafka instance. If the task is successfully created, the job_id of the flow control task is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceAutoCreateTopic</td>
                    <td>Enables or disables the function of automatically creating topics for an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCluster</td>
                    <td>Query Kafka cluster metadata.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CloseKafkaManager</td>
                    <td>After Kafka Manager is disabled, the original management interfaces are unavailable.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceCrossVpcIp</td>
                    <td>Change the internal IP address for cross-VPC access of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTopicReplica</td>
                    <td>Modifies the copy of the topic partition of the Kafka instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKafkaUserClientQuotaTask</td>
                    <td>This API is used to submit a user- and client-level flow control task to a Kafka instance. If the task is successfully submitted, the job_id of the flow control task is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaUserClientQuota</td>
                    <td>This interface is used to query the flow control configuration from the Kafka instance. If the query is successful, the flow control configuration list is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Lifecycle Management</td>
                    <td>ShowInstanceConfigs</td>
                    <td>Obtains the instance configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRestartOrDeleteInstances</td>
                    <td>Restart or delete instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableDns</td>
                    <td>Enable the RocketMQ instance domain name access capability.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstance</td>
                    <td>Modifies the name and description of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceByEngine</td>
                    <td>This API is used to create an instance in pay-per-use or yearly/monthly mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyInstanceConfigs</td>
                    <td>Modify the instance configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostPaidKafkaInstance</td>
                    <td>Create an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeInstance</td>
                    <td>Upgrading the Instance Kernel</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>Query the instance list of a tenant. Query by condition is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Message management</td>
                    <td>ShowPartitionEndMessage</td>
                    <td>Query the location of the latest messages in the partition.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceMessages</td>
                    <td>Query the offset and content of a message.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMessages</td>
                    <td>Query the messages generated in a specified period of time in a partition.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPartitionBeginningMessage</td>
                    <td>Query the location of the earliest message in the partition.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPartitionMessage</td>
                    <td>Query the message of the specified offset of the partition.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKafkaMessage</td>
                    <td>Kafka deletes a message.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Other interfaces</td>
                    <td>ListAvailableZones</td>
                    <td>When creating an instance, you need to configure the ID of the AZ where the instance is located. You can use this API to query the ID of the AZ.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaProductCores</td>
                    <td>Query the number of cores of the Kafka product specification.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCesHierarchy</td>
                    <td>Query the monitoring hierarchy of instances in CES.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEngineProducts</td>
                    <td>Query the product specification list of the corresponding engine.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMaintainWindows</td>
                    <td>Query the start time and end time of the maintenance time window.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Smart Connect</td>
                    <td>PauseConnectorTask</td>
                    <td>Suspend the Smart Connect task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartConnectorTask</td>
                    <td>Starts Smart Connect tasks that are not started and restarts suspended or running Smart Connect tasks. Note that restarting the Smart Connect task resets the synchronization progress and restarts the synchronization task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConnectorTask</td>
                    <td>Query Smart Connector task details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnector</td>
                    <td>This section describes how to disable Smart Connect for a pay-per-use instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConnectorTasks</td>
                    <td>Query the Smart Connect task list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnectorTask</td>
                    <td>Delete the Smart Connector task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResumeConnectorTask</td>
                    <td>Start the suspended Smart Connect task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnector</td>
                    <td>Enable Smart Connect and submit the task for creating Smart Connect nodes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnectorTask</td>
                    <td>Create a Smart Connect task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Specification Change Management</td>
                    <td>ShowEngineInstanceExtendProductInfo</td>
                    <td>Query the scaled-up specifications of a DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaInstanceExtendProductInfo</td>
                    <td>Query the scale-up specifications of a DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeKafkaInstance</td>
                    <td>This API is used to change the instance specification. Currently, only on-demand instances can be scaled up by calling APIs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeEngineInstance</td>
                    <td>This API is used to change the instance specification. Currently, only on-demand instances can be scaled up by calling APIs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Subject Management</td>
                    <td>DeleteKafkaTopicQuota</td>
                    <td>This API is used to submit a topic-level flow control task to the Kafka instance. If the task is successfully deleted, the job ID of the flow control task is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopicPartitions</td>
                    <td>Query the partition list of a topic</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceTopicDetail</td>
                    <td>Query details about a Kafka instance topic. (A single instance cannot be invoked every 1s.)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceTopic</td>
                    <td>This API is used to create a topic for a Kafka instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKafkaTopicQuota</td>
                    <td>This API is used to submit a topic-level flow control task to the Kafka instance. If the creation is successful, the job_id of the flow control task is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaTopicQuota</td>
                    <td>This interface is used to query topic-level flow control tasks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopicProducers</td>
                    <td>Query the producer list of a topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendKafkaMessage</td>
                    <td>Send a specified message to the Kafka instance on the console.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceTopics</td>
                    <td>This API is used to query topic details of a specified Kafka instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceTopic</td>
                    <td>Modifying a Kafka Instance Topic</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyKafkaTopicQuota</td>
                    <td>This API is used to submit a topic-level flow control task to the Kafka instance. If the task is successfully submitted, the job_id of the flow control task is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteInstanceTopic</td>
                    <td>This API is used to delete topics from Kafka instances in batches. When multiple topics are deleted in batches, some topics are successfully deleted and some topics fail to be deleted. In this case, the interface returns a message indicating that the deletion is successful and the information about the topics that fail to be deleted is displayed in the message.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Tag Management</td>
                    <td>BatchCreateOrDeleteKafkaTag</td>
                    <td>Add or delete instance tags in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaProjectTags</td>
                    <td>Query project tags.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaTags</td>
                    <td>Query the instance tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">User management</td>
                    <td>CreateInstanceUser</td>
                    <td>User for creating Kafka instances. You can connect to Kafka instances with SASL enabled. For Kafka instances created before July 15, 2023, a maximum of 20 users can be created for each instance. For Kafka instances created on July 15, 2023 or later, a maximum of 500 users can be created for each instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTopicAccessPolicy</td>
                    <td>Query user permissions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceUser</td>
                    <td>Modifying user parameters</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteInstanceUsers</td>
                    <td>User for deleting Kafka instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceUsers</td>
                    <td>Query the user list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetUserPasswrod</td>
                    <td>Resetting the user password</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
