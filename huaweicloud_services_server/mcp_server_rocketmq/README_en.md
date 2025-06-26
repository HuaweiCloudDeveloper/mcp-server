# RocketMQ MCP Server 


## Version
v0.1.0

## Overview

RocketMQ MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RocketMQ. Full-chain management of RocketMQ resources can be carried out based on natural language.

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
                    <td rowspan="9">Consumer group management</td>
                    <td>UpdateConsumerGroup</td>
                    <td>Modifies the parameters of a specified consumer group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConsumerListOrDetails</td>
                    <td>Query the consumption list or details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConsumerGroups</td>
                    <td>Query the consumer group list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConsumerConnections</td>
                    <td>Query the consumer list in a consumer group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConsumerGroup</td>
                    <td>Delete a consumer group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConsumerGroupOrBatchDeleteConsumerGroup</td>
                    <td>Create a consumer group or delete consumer groups in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetConsumeOffset</td>
                    <td>Reset the consumption progress.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateConsumerGroup</td>
                    <td>Modify consumer groups in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGroup</td>
                    <td>Query the details of a specified consumer group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Exclusive Instance Management</td>
                    <td>DeleteInstance</td>
                    <td>Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Instance Management</td>
                    <td>ShowInstanceNodes</td>
                    <td>Query the instance node information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartInstance</td>
                    <td>Restarts a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Lifecycle Management</td>
                    <td>ListBrokers</td>
                    <td>Query the proxy list.</td>
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
                    <td>BatchDeleteInstances</td>
                    <td>Delete instances in batches. After the instance is deleted, the original data in the instance will be deleted and no backup will be performed. Exercise caution when performing this operation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>Query the instance list of a tenant. Query by condition is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Message management</td>
                    <td>ExportDlqMessage</td>
                    <td>Export dead letter messages.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMessages</td>
                    <td>Query messages.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendDlqMessage</td>
                    <td>Resend a dead letter message.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMessageTrace</td>
                    <td>Query the message track.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateConsumedMessage</td>
                    <td>Consumption verification.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Metadata Migration</td>
                    <td>ListRocketMqMigrationTask</td>
                    <td>1. Query all migration tasks in an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRocketMqMigrationTask</td>
                    <td>Create a metadata migration task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRocketMqMigrationTask</td>
                    <td>Delete a metadata migration task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Other interfaces</td>
                    <td>ListEngineProducts</td>
                    <td>Query the product specification list of the corresponding engine.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableZones</td>
                    <td>When creating an instance, you need to configure the ID of the AZ where the instance is located. You can use this API to query the ID of the AZ.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRocketMQProductCores</td>
                    <td>Query the number of RocketMQ cores.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Parameter Management</td>
                    <td>UpdateRocketMqConfigs</td>
                    <td>This interface is used to modify RocketMQ configurations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRocketMqConfigs</td>
                    <td>This interface is used to query the RocketMQ configuration. If the query is successful, the configuration information is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Specification Change Management</td>
                    <td>ResizeInstance</td>
                    <td>The instance specification is changed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEngineInstanceExtendProductInfo</td>
                    <td>Query the scaled-up specifications of a DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Tag Management</td>
                    <td>ShowRocketmqProjectTags</td>
                    <td>Query project tags.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateOrDeleteRocketmqTag</td>
                    <td>Add or delete instance tags in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRocketmqTags</td>
                    <td>Query the instance label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Topic management</td>
                    <td>ListConsumerGroupOfTopic</td>
                    <td>Query the consumer group list of the theme.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTopicStatus</td>
                    <td>Query the number of messages in the topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTopicOrBatchDeleteTopic</td>
                    <td>Create a topic or delete topics in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOneTopic</td>
                    <td>Query a single topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRocketInstanceTopics</td>
                    <td>This API is used to query the topic list of a specified RocketMQ instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Topic operation</td>
                    <td>UpdateTopic</td>
                    <td>Update the display name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTopic</td>
                    <td>Delete a topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">User management</td>
                    <td>ListUser</td>
                    <td>Query the user list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUser</td>
                    <td>Modify user parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUser</td>
                    <td>Query user details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopicAccessPolicy</td>
                    <td>Query the list of authorized users of a topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUser</td>
                    <td>Create a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConsumeGroupAccessPolicy</td>
                    <td>Query the authorized users of the consumer group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUser</td>
                    <td>Delete a user.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
