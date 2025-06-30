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
                    <td rowspan="1">Access Endpoint Management</td>
                    <td>UpdateEndpoint</td>
                    <td>Update the access endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Destination Connection Management</td>
                    <td>ShowDetailOfConnection</td>
                    <td>Query the details about the target connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConnection</td>
                    <td>Update the target connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnection</td>
                    <td>Create the target connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConnections</td>
                    <td>Query the list of target connections.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnection</td>
                    <td>Delete the target connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Entrusted management</td>
                    <td>ListAgencies</td>
                    <td>This interface is used by the (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the agency list based on the specified conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Event Channel Management</td>
                    <td>UpdateChannel</td>
                    <td>Updates the definition of a customized event channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateChannel</td>
                    <td>Create a custom event channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListChannels</td>
                    <td>Query the event channel list, including system channels and user-defined channels.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailOfChannel</td>
                    <td>Query details about a specified event channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteChannel</td>
                    <td>Delete a specified customized event channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Event Example Management</td>
                    <td>ShowListOfEventSample</td>
                    <td>Query the sample event list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Event Flow Management</td>
                    <td>DeleteEventStreaming</td>
                    <td>Delete an event flow.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEventStreaming</td>
                    <td>Update the event flow.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEventStreaming</td>
                    <td>Create an event flow.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEventStreaming</td>
                    <td>Query event flow details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventStreaming</td>
                    <td>Query the event flow list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResumeEventStreaming</td>
                    <td>Operation event flow.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Event Model Management</td>
                    <td>ListEventSchema</td>
                    <td>Query the event model list, including the system event model and user-defined event model</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEventSchema</td>
                    <td>Updating the definition of a custom event model</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEventSchema</td>
                    <td>Create a custom event model</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DiscoverEventSchemaFromData</td>
                    <td>Automatic discovery of event models</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventSchemaVersions</td>
                    <td>Query the event model version list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEventSchemaVersion</td>
                    <td>Create a customized event model version. The version number is automatically generated in the background.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEventSchema</td>
                    <td>Delete an event model</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEventSchemaVersion</td>
                    <td>Delete a specified version of an event model</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailOfEventSchema</td>
                    <td>Query event model details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailOfEventSchemaVersion</td>
                    <td>Query details about a specified version of an event model</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Event Source Management</td>
                    <td>ShowDetailOfEventSource</td>
                    <td>Query details about an event source.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEventSource</td>
                    <td>To create a user-defined event source, you can specify only a user-defined channel, but not a system channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEventSources</td>
                    <td>Query by condition is supported. For example, you can specify an event channel ID to query all event sources in an event channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEventSource</td>
                    <td>Delete a specified user-defined event source.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEventSource</td>
                    <td>Updates the definition of a user-defined event source.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Event Subscription Management</td>
                    <td>ShowDetailOfSubscriptionTarget</td>
                    <td>Query details about an event subscription target.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteSubscriptionOperation</td>
                    <td>Operation event subscription, which can be enabled or disabled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubscriptionSource</td>
                    <td>Updates the definition of an event feed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubscriptionTarget</td>
                    <td>Create a single event subscription target.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubscriptionTarget</td>
                    <td>Updates the definition of an event subscription target.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubscriptionTarget</td>
                    <td>Delete an event subscription target.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubscription</td>
                    <td>Delete an event subscription.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailOfSubscription</td>
                    <td>Query event subscription details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Event Target Category Management</td>
                    <td>ListEventTarget</td>
                    <td>Query the preconfigured target event categories and obtain the field definition of each target event category.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Event management</td>
                    <td>PutOfficialEvents</td>
                    <td>Release an official event to the event channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTracedEvents</td>
                    <td>Query the event tracing list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckPutEvents</td>
                    <td>Release events to the event source requires the subscription conditions and pre-verification.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailOfEvent</td>
                    <td>Query event details based on the event ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PutEvents</td>
                    <td>Release events to the event channel for debugging only.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailOfEventTrace</td>
                    <td>Event track details, which displays the delivery status from the event source to the delivery target.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Feature Management</td>
                    <td>QuerySupportFeature</td>
                    <td>Query the features supported by the current user's project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Monitoring Metric Management</td>
                    <td>ListSubMetrics</td>
                    <td>Query the monitoring indicator data of event subscription.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPubMetrics</td>
                    <td>Query the monitoring metrics of an event channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">OBS bucket management</td>
                    <td>ListObsBuckets</td>
                    <td>Obtain the OBS bucket list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Refurbishobs</td>
                    <td>Renovate the OBS fg trigger and create it as an EG subscription.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query version operation</td>
                    <td>ListApiVersions</td>
                    <td>Query the TMS API version list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota Management</td>
                    <td>ListQuotas</td>
                    <td>Obtain quota information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Service Entrusted Management</td>
                    <td>CreateAgencies</td>
                    <td>Create a service agency based on the service scenario by one click.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Service provisioning management</td>
                    <td>ListSubscriptions</td>
                    <td>This interface is used to obtain service provisioning information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubscription</td>
                    <td>This interface is used by a user to apply for the video access service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Subscription operation</td>
                    <td>UpdateSubscription</td>
                    <td>Update the subscriber remarks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Trigger Management</td>
                    <td>ListWorkflowTriggers</td>
                    <td>Query trigger. You can specify the function stream ID. A subscription whose target is the function stream ID is a trigger.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTriggers</td>
                    <td>Query trigger. You can specify the URN of the function. A subscription with the URN as the target is a trigger.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">VPC Endpoint Function</td>
                    <td>ListEndpoints</td>
                    <td>Query the list of VPC endpoints of the current user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEndpoint</td>
                    <td>Create a VPC endpoint so that it can access the VPC endpoint service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEndpoint</td>
                    <td>Delete the VPC endpoint.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
