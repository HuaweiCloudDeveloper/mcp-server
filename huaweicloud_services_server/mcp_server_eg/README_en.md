# EG MCP Server 


## Version
v0.1.0

## Overview

EG MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EG. Full-chain management of EG resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Access Endpoint Management | UpdateEndpoint | Update the access endpoint. | To be tested |
| Destination Connection Management | ShowDetailOfConnection | Query the details about the target connection. | To be tested |
|  | UpdateConnection | Update the target connection. | To be tested |
|  | CreateConnection | Create the target connection. | To be tested |
|  | ListConnections | Query the list of target connections. | To be tested |
|  | DeleteConnection | Delete the target connection. | To be tested |
| Entrusted management | ListAgencies | This interface is used by the (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the agency list based on the specified conditions. | To be tested |
| Event Channel Management | UpdateChannel | Updates the definition of a customized event channel. | To be tested |
|  | CreateChannel | Create a custom event channel. | To be tested |
|  | ListChannels | Query the event channel list, including system channels and user-defined channels. | To be tested |
|  | ShowDetailOfChannel | Query details about a specified event channel. | To be tested |
|  | DeleteChannel | Delete a specified customized event channel. | To be tested |
| Event Example Management | ShowListOfEventSample | Query the sample event list | To be tested |
| Event Flow Management | DeleteEventStreaming | Delete an event flow. | To be tested |
|  | UpdateEventStreaming | Update the event flow. | To be tested |
|  | CreateEventStreaming | Create an event flow. | To be tested |
|  | ShowEventStreaming | Query event flow details. | To be tested |
|  | ListEventStreaming | Query the event flow list. | To be tested |
|  | ResumeEventStreaming | Operation event flow. | To be tested |
| Event Model Management | ListEventSchema | Query the event model list, including the system event model and user-defined event model | To be tested |
|  | UpdateEventSchema | Updating the definition of a custom event model | To be tested |
|  | CreateEventSchema | Create a custom event model | To be tested |
|  | DiscoverEventSchemaFromData | Automatic discovery of event models | To be tested |
|  | ListEventSchemaVersions | Query the event model version list | To be tested |
|  | CreateEventSchemaVersion | Create a customized event model version. The version number is automatically generated in the background. | To be tested |
|  | DeleteEventSchema | Delete an event model | To be tested |
|  | DeleteEventSchemaVersion | Delete a specified version of an event model | To be tested |
|  | ShowDetailOfEventSchema | Query event model details | To be tested |
|  | ShowDetailOfEventSchemaVersion | Query details about a specified version of an event model | To be tested |
| Event Source Management | ShowDetailOfEventSource | Query details about an event source. | To be tested |
|  | CreateEventSource | To create a user-defined event source, you can specify only a user-defined channel, but not a system channel. | To be tested |
|  | ListEventSources | Query by condition is supported. For example, you can specify an event channel ID to query all event sources in an event channel. | To be tested |
|  | DeleteEventSource | Delete a specified user-defined event source. | To be tested |
|  | UpdateEventSource | Updates the definition of a user-defined event source. | To be tested |
| Event Subscription Management | ShowDetailOfSubscriptionTarget | Query details about an event subscription target. | To be tested |
|  | ExecuteSubscriptionOperation | Operation event subscription, which can be enabled or disabled. | To be tested |
|  | UpdateSubscriptionSource | Updates the definition of an event feed. | To be tested |
|  | CreateSubscriptionTarget | Create a single event subscription target. | To be tested |
|  | UpdateSubscriptionTarget | Updates the definition of an event subscription target. | To be tested |
|  | DeleteSubscriptionTarget | Delete an event subscription target. | To be tested |
|  | DeleteSubscription | Delete an event subscription. | To be tested |
|  | ShowDetailOfSubscription | Query event subscription details. | To be tested |
| Event Target Category Management | ListEventTarget | Query the preconfigured target event categories and obtain the field definition of each target event category. | To be tested |
| Event management | PutOfficialEvents | Release an official event to the event channel. | To be tested |
|  | ListTracedEvents | Query the event tracing list. | To be tested |
|  | CheckPutEvents | Release events to the event source requires the subscription conditions and pre-verification. | To be tested |
|  | ShowDetailOfEvent | Query event details based on the event ID. | To be tested |
|  | PutEvents | Release events to the event channel for debugging only. | To be tested |
|  | ShowDetailOfEventTrace | Event track details, which displays the delivery status from the event source to the delivery target. | To be tested |
| Feature Management | QuerySupportFeature | Query the features supported by the current user's project. | To be tested |
| Monitoring Metric Management | ListSubMetrics | Query the monitoring indicator data of event subscription. | To be tested |
|  | ListPubMetrics | Query the monitoring metrics of an event channel. | To be tested |
| OBS bucket management | ListObsBuckets | Obtain the OBS bucket list. | To be tested |
|  | Refurbishobs | Renovate the OBS fg trigger and create it as an EG subscription. | To be tested |
| Query version operation | ListApiVersions | Query the TMS API version list. | To be tested |
| Quota Management | ListQuotas | Obtain quota information | To be tested |
| Service Entrusted Management | CreateAgencies | Create a service agency based on the service scenario by one click. | To be tested |
| Service provisioning management | ListSubscriptions | This interface is used to obtain service provisioning information. | To be tested |
|  | CreateSubscription | This interface is used by a user to apply for the video access service. | To be tested |
| Subscription operation | UpdateSubscription | Update the subscriber remarks. | To be tested |
| Trigger Management | ListWorkflowTriggers | Query trigger. You can specify the function stream ID. A subscription whose target is the function stream ID is a trigger. | To be tested |
|  | ListTriggers | Query trigger. You can specify the URN of the function. A subscription with the URN as the target is a trigger. | To be tested |
| VPC Endpoint Function | ListEndpoints | Query the list of VPC endpoints of the current user. | To be tested |
|  | CreateEndpoint | Create a VPC endpoint so that it can access the VPC endpoint service. | To be tested |
|  | DeleteEndpoint | Delete the VPC endpoint. | To be tested |

