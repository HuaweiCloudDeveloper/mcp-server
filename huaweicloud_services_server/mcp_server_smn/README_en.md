# SMN MCP Server 


## Version
v0.1.0

## Overview

SMN MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SMN. Full-chain management of SMN resources can be carried out based on natural language.

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
                    <td rowspan="1">Application Direct Message Operation</td>
                    <td>PublishAppMessage</td>
                    <td>Send the message to the endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Application endpoint operation</td>
                    <td>CreateApplicationEndpoint</td>
                    <td>Create the endpoint of the application platform.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplicationEndpoints</td>
                    <td>Query the endpoint list of the platform.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApplicationEndpoint</td>
                    <td>Deletes a device.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApplicationEndpoint</td>
                    <td>Updates device attributes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplicationEndpointAttributes</td>
                    <td>Obtains the endpoint attributes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Application operation</td>
                    <td>CreateApplication</td>
                    <td>Create a platform application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApplication</td>
                    <td>Update the application platform.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplications</td>
                    <td>Query the application platform list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplicationAttributes</td>
                    <td>Obtain the application platform attributes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApplication</td>
                    <td>Delete a platform application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Log operation</td>
                    <td>CreateLogtank</td>
                    <td>Bind a cloud log to a specified topic to record the message sending status of the topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogtank</td>
                    <td>This API is used to update the cloud logs bound to a specified topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogtank</td>
                    <td>Unbind the cloud logs from a specified topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogtank</td>
                    <td>Query the cloud logs bound to a specified topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Notification Policy</td>
                    <td>ShowNotifyPolicy</td>
                    <td>Query notification policies</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNotifyPolicy</td>
                    <td>Create a notification policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNotifyPolicy</td>
                    <td>Modifies a notification policy. This API supports only full modification.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNotifyPolicy</td>
                    <td>Delete a notification policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Publish Message Operation</td>
                    <td>ShowHttpDetectResult</td>
                    <td>Query the detection result based on the task_id returned by the HTTP detection message.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishMessage</td>
                    <td>Send the message to all the subscription endpoints of the topic. When the message ID is returned, the message has been saved and attempts to push it to the subscribers of the topic have begun. To ensure that your messages can be successfully sent to all subscribers, ensure that your messages comply with local laws and regulations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishHttpDetect</td>
                    <td>Send an HTTP/HTTPS detection message based on the theme to check whether the current HTTP/HTTPS device is available and whether the device can access the SMN egress.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Query version operation</td>
                    <td>ListVersion</td>
                    <td>Query the SMN API V2 version information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVersions</td>
                    <td>Query the version number supported by SMN open APIs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Resource Tag</td>
                    <td>CreateResourceTag</td>
                    <td>Add tags to multiple cloud service resources. A maximum of 10 tags can be added to each resource. A maximum of 20 tags can be operated at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResourceTag</td>
                    <td>This API is used to remove tags of multiple cloud service resources in batches. A maximum of 10 tags can be removed for each resource. A maximum of 20 tags can be removed at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Service provisioning management</td>
                    <td>ListSubscriptions</td>
                    <td>This interface is used to obtain service provisioning information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Subscribe to filtering policy operation</td>
                    <td>BatchCreateSubscriptionsFilterPolices</td>
                    <td>Create a message filtering policy for the subscriber.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateSubscriptionsFilterPolices</td>
                    <td>Update the message filtering policy of the subscriber.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteSubscriptionsFilterPolices</td>
                    <td>Delete the message filtering policy of the subscriber.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Subscription operation</td>
                    <td>AddSubscriptionFromSubscriptionUser</td>
                    <td>Add a subscriber to a specified topic. The subscriber information source is the subscriber list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubscriptionsByTopic</td>
                    <td>Obtain the subscription list of specific topics in pagination mode. The subscription list is sorted in ascending order by subscription creation time. You can specify the offset and limit for pagination query. If the specified topic does not have subscribers, an empty list is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelSubscription</td>
                    <td>Delete the specified subscriber.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddSubscription</td>
                    <td>Adds a subscriber to a specified topic. If the status of the subscriber is unacknowledged, a confirmation message is sent to the subscriber. After the subscriber confirms the subscription, the subscriber can receive the message published by the topic. By default, a maximum of 10000 subscribers can be added to a topic. In the high-concurrency scenario, the number of subscribers may exceed 10000. This is normal. The interface is idempotent. If an existing subscriber is added, a success message is returned and the status code is 200. Otherwise, the status code is 201.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubscription</td>
                    <td>Update the subscriber remarks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TAG Function</td>
                    <td>ListResourceInstances</td>
                    <td>Query resource instances of a tenant by tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>Query all tags of a specified resource type in a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Template operation</td>
                    <td>ListMessageTemplateDetails</td>
                    <td>Query the template details, including the template content.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMessageTemplate</td>
                    <td>Create a template. Users can send messages based on the template to reduce the requested data volume.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMessageTemplate</td>
                    <td>Modify the content of the message template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMessageTemplates</td>
                    <td>Query the template list by page. The template list is sorted by creation time in ascending order. You can specify the offset and limit for pagination query. If no template exists, an empty list is returned. Additional query parameters are message_template_name and protocol, respectively.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMessageTemplate</td>
                    <td>Delete a message template. Message requests sent by the template before the template is deleted can be sent by the template. After the template is deleted, the template cannot be used to send messages.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Topic operation</td>
                    <td>DeleteTopic</td>
                    <td>Delete a topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopicDetails</td>
                    <td>Query the details about a topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTopicAttribute</td>
                    <td>Updates the policy information about a topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopics</td>
                    <td>Query the topic list by page. Topics are sorted in descending order by topic creation time. You can specify the offset and limit for pagination query. If no topic exists, an empty list is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTopicAttributeByName</td>
                    <td>Delete the specified topic policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTopicAttributes</td>
                    <td>Delete all topic policies.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTopic</td>
                    <td>Update the display name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopicAttributes</td>
                    <td>Query policy information about a topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTopic</td>
                    <td>Create a topic. The default quota of a single user is 3000. In the high-concurrency scenario, the number of topics may exceed 3000, which is normal.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Use TMS</td>
                    <td>BatchCreateOrDeleteResourceTags</td>
                    <td>This API is used to add or delete tags for specified DB instances in batches. A maximum of 10 labels can be placed on a resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceTags</td>
                    <td>Query the label information of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
