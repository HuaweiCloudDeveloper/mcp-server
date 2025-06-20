# SMN MCP Server 


## Version
v0.1.0

## Overview

SMN MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SMN. Full-chain management of SMN resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Application Direct Message Operation | PublishAppMessage | Send the message to the endpoint. | To be tested |
| Application endpoint operation | CreateApplicationEndpoint | Create the endpoint of the application platform. | To be tested |
|  | ListApplicationEndpoints | Query the endpoint list of the platform. | To be tested |
|  | DeleteApplicationEndpoint | Deletes a device. | To be tested |
|  | UpdateApplicationEndpoint | Updates device attributes. | To be tested |
|  | ListApplicationEndpointAttributes | Obtains the endpoint attributes. | To be tested |
| Application operation | CreateApplication | Create a platform application. | To be tested |
|  | UpdateApplication | Update the application platform. | To be tested |
|  | ListApplications | Query the application platform list. | To be tested |
|  | ListApplicationAttributes | Obtain the application platform attributes. | To be tested |
|  | DeleteApplication | Delete a platform application. | To be tested |
| Log operation | CreateLogtank | Bind a cloud log to a specified topic to record the message sending status of the topic. | To be tested |
|  | UpdateLogtank | This API is used to update the cloud logs bound to a specified topic. | To be tested |
|  | DeleteLogtank | Unbind the cloud logs from a specified topic. | To be tested |
|  | ListLogtank | Query the cloud logs bound to a specified topic. | To be tested |
| Notification Policy | ShowNotifyPolicy | Query notification policies | To be tested |
|  | CreateNotifyPolicy | Create a notification policy | To be tested |
|  | UpdateNotifyPolicy | Modifies a notification policy. This API supports only full modification.  | To be tested |
|  | DeleteNotifyPolicy | Delete a notification policy | To be tested |
| Publish Message Operation | ShowHttpDetectResult | Query the detection result based on the task_id returned by the HTTP detection message. | To be tested |
|  | PublishMessage | Send the message to all the subscription endpoints of the topic. When the message ID is returned, the message has been saved and attempts to push it to the subscribers of the topic have begun. To ensure that your messages can be successfully sent to all subscribers, ensure that your messages comply with local laws and regulations. | To be tested |
|  | PublishHttpDetect | Send an HTTP/HTTPS detection message based on the theme to check whether the current HTTP/HTTPS device is available and whether the device can access the SMN egress. | To be tested |
| Query version operation | ListVersion | Query the SMN API V2 version information. | To be tested |
|  | ListVersions | Query the version number supported by SMN open APIs. | To be tested |
| Resource Tag | CreateResourceTag | Add tags to multiple cloud service resources. A maximum of 10 tags can be added to each resource. A maximum of 20 tags can be operated at a time. | To be tested |
|  | DeleteResourceTag | This API is used to remove tags of multiple cloud service resources in batches. A maximum of 10 tags can be removed for each resource. A maximum of 20 tags can be removed at a time. | To be tested |
| Service provisioning management | ListSubscriptions | This interface is used to obtain service provisioning information. | To be tested |
| Subscribe to filtering policy operation | BatchCreateSubscriptionsFilterPolices | Create a message filtering policy for the subscriber. | To be tested |
|  | BatchUpdateSubscriptionsFilterPolices | Update the message filtering policy of the subscriber. | To be tested |
|  | BatchDeleteSubscriptionsFilterPolices | Delete the message filtering policy of the subscriber. | To be tested |
| Subscription operation | AddSubscriptionFromSubscriptionUser | Add a subscriber to a specified topic. The subscriber information source is the subscriber list. | To be tested |
|  | ListSubscriptionsByTopic | Obtain the subscription list of specific topics in pagination mode. The subscription list is sorted in ascending order by subscription creation time. You can specify the offset and limit for pagination query. If the specified topic does not have subscribers, an empty list is returned. | To be tested |
|  | CancelSubscription | Delete the specified subscriber. | To be tested |
|  | AddSubscription | Adds a subscriber to a specified topic. If the status of the subscriber is unacknowledged, a confirmation message is sent to the subscriber. After the subscriber confirms the subscription, the subscriber can receive the message published by the topic. By default, a maximum of 10000 subscribers can be added to a topic. In the high-concurrency scenario, the number of subscribers may exceed 10000. This is normal. The interface is idempotent. If an existing subscriber is added, a success message is returned and the status code is 200. Otherwise, the status code is 201. | To be tested |
|  | UpdateSubscription | Update the subscriber remarks. | To be tested |
| TAG Function | ListResourceInstances | Query resource instances of a tenant by tag. | To be tested |
| Tags | ListProjectTags | Query all tags of a specified resource type in a specified project | To be tested |
| Template operation | ListMessageTemplateDetails | Query the template details, including the template content. | To be tested |
|  | CreateMessageTemplate | Create a template. Users can send messages based on the template to reduce the requested data volume. | To be tested |
|  | UpdateMessageTemplate | Modify the content of the message template. | To be tested |
|  | ListMessageTemplates | Query the template list by page. The template list is sorted by creation time in ascending order. You can specify the offset and limit for pagination query. If no template exists, an empty list is returned. Additional query parameters are message_template_name and protocol, respectively. | To be tested |
|  | DeleteMessageTemplate | Delete a message template. Message requests sent by the template before the template is deleted can be sent by the template. After the template is deleted, the template cannot be used to send messages. | To be tested |
| Topic operation | DeleteTopic | Delete a topic. | To be tested |
|  | ListTopicDetails | Query the details about a topic. | To be tested |
|  | UpdateTopicAttribute | Updates the policy information about a topic. | To be tested |
|  | ListTopics | Query the topic list by page. Topics are sorted in descending order by topic creation time. You can specify the offset and limit for pagination query. If no topic exists, an empty list is returned. | To be tested |
|  | DeleteTopicAttributeByName | Delete the specified topic policy. | To be tested |
|  | DeleteTopicAttributes | Delete all topic policies. | To be tested |
|  | UpdateTopic | Update the display name. | To be tested |
|  | ListTopicAttributes | Query policy information about a topic. | To be tested |
|  | CreateTopic | Create a topic. The default quota of a single user is 3000. In the high-concurrency scenario, the number of topics may exceed 3000, which is normal. | To be tested |
| Use TMS | BatchCreateOrDeleteResourceTags | This API is used to add or delete tags for specified DB instances in batches. A maximum of 10 labels can be placed on a resource. | To be tested |
|  | ListResourceTags | Query the label information of a specified DB instance. | To be tested |

