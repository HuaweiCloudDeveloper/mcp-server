# DRIS MCP Server 


## Version
v0.1.0

## Overview

DRIS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DRIS. Full-chain management of DRIS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| APIG-SN-DATACHANNEL | CreateDataChannel | Create a service channel, which is used to create a data channel for reporting Edge messages. | To be tested |
|  | UpdateDataChannel | Modifying a service channel | To be tested |
|  | ShowDataChannel | Query a service channel | To be tested |
|  | DeleteDataChannel | Delete a service channel | To be tested |
| APIG-SN-EDGE | ShowDeploymentCode | Generate the application installation command and run it on the ITS800 or ATLAS500 through the shell. | To be tested |
|  | DeleteV2XEdgeByV2xEdgeId | Before deleting an edge, you need to delete the service channels and associated devices under the edge. | To be tested |
|  | ShowV2xEdgeDetail | Query Edge | To be tested |
|  | UpdateV2xEdge | Modifying Edge | To be tested |
|  | CreateV2xEdge | Create Edge | To be tested |
|  | ListV2xEdges | Query the edge list | To be tested |
| APIG-SN-ForwardingConfigResources | ShowForwardingConfigs | Query the data forwarding configuration list | To be tested |
|  | DeleteForwardingConfig | Delete the data forwarding configuration based on the unique ID (forwarding_config_id) of the forwarding configuration. After the deletion, the subscribed topic messages will not be forwarded to brokers. | To be tested |
|  | AddForwardingConfigs | Create a data forwarding configuration. Currently, only data can be forwarded to Kafka. After the data forwarding configuration is added, topic messages in the configuration will be forwarded to the specified brokers. | To be tested |
|  | UpdateForwardingConfig | Modify the data forwarding configuration based on the unique ID (forwarding_config_id) of the forwarding configuration. Currently, the topicPrefix, userTopics, and brokers fields can be updated. You need to write all the new values of the fields. | To be tested |
|  | ShowForwardingConfig | Query the data forwarding configuration based on the unique ID (forwarding_config_id) of the forwarding configuration | To be tested |
| APIG-SN-HistoryTrafficEvents | ShowHistoryTrafficEvents | Query the historical traffic event list | To be tested |
|  | ListEdgeFlows | Query the historical traffic statistics list | To be tested |
| APIG-SN-IPC | ShowIpc | Querying IPCs | To be tested |
|  | BatchShowIpcs | Obtaining multiple IPC resources | To be tested |
| APIG-SN-RADAR | BatchShowRadars | Query the radar list | To be tested |
| APIG-SN-RSU | UpdateRsu | Modifying an RSU | To be tested |
|  | DeleteRsu | Delete RSU | To be tested |
|  | CreateRsu | Create RSU | To be tested |
|  | BatchShowRsus | Query the RSU list | To be tested |
| APIG-SN-SendImmediateEvent | SendImmediateEvent | Interface for creating an instant traffic event. The IoT platform distributes the instant traffic event to the target device. Once an event is created, it will be delivered immediately and only once. | To be tested |
| APIG-SN-TRAFFIC-CONTROLLER | DeleteTrafficController | Delete signal controller | To be tested |
|  | CreateTrafficController | Create signal controller | To be tested |
|  | BatchShowTrafficControllers | Query the signal controller list | To be tested |
|  | UpdateTrafficController | Modifying the signal controller | To be tested |
| APIG-SN-TRAFFICEVENT | BatchShowTrafficEvents | Query traffic events by conditions | To be tested |
|  | ShowTrafficEvent | Query long-term traffic events | To be tested |
|  | CreateTrafficEvent | When a long-term traffic event is created, the IoT platform determines the status of the long-term traffic event based on the start time and end time of the event. For active traffic events, the system immediately delivers RSUs within the impact scope of the event. For future events, the system delivers RSUs within the impact scope at the start time of the event. Expired events will not be delivered. | To be tested |
|  | UpdateTrafficEvent | Modifying a long-term traffic event | To be tested |
|  | DeleteTrafficEvent | Delete long-term traffic events | To be tested |
| APIG-SN-V2XEDGE-APP | UpdateV2xEdgeApp | **Before upgrading an edge application, ensure that * *: | To be tested |
|  | ShowV2XEdgeAppDetailByEdgeAppId | Query edge applications | To be tested |
|  | CreateV2xEdgeApp | **Before deploying an edge application, ensure that * *: | To be tested |
|  | ListV2xEdgeApp | Query the edge application list | To be tested |
|  | DeleteV2XEdgeAppByEdgeAppId | Before deleting the system application ($edgetepa), delete the service channel. If the API for deleting an edge application is invoked successfully, the edge device automatically deletes the application. | To be tested |
| APIG-SN-VEHICLE | CreateVehicle | Create a vehicle | To be tested |
|  | BatchShowVehicles | Query the vehicle list | To be tested |
|  | DeleteVehicle | Deleting a vehicle | To be tested |
|  | UpdateVehicle | Modifying a vehicle | To be tested |
| EdgeAppManagement | BatchShowEdgeApps | Query the application list | To be tested |
|  | DeleteEdgeApp | Delete an application | To be tested |
|  | CreateEdgeApp | Create an application | To be tested |
|  | UpdateEdgeApp | Modifying an application | To be tested |
| EdgeAppVersionManagement | ShowEdgeApplicationVersion | Query the application version | To be tested |
|  | UpdateEdgeApplicationVersion | Modifying the application version | To be tested |
|  | CreateEdgeApplicationVersion | Create an application version | To be tested |
|  | BatchShowEdgeAppVersions | Query the application version list | To be tested |
|  | UpdateEdgeApplicationVersionState | Update the application version status. | To be tested |
|  | DeleteEdgeApplicationVersion | Delete an application version | To be tested |
| RsuModelManagement | UpdateRsuModel | You can invoke this interface to modify the model of an existing RSU. | To be tested |
|  | DeleteRsuModel | You can invoke this interface to delete a created RSU model. | To be tested |
|  | CreateRsuModel | This interface is used to create an RSU model. | To be tested |
|  | ListRsuModels | This interface can be invoked to query the created RSU model list. | To be tested |
|  | ShowRsuModel | This interface can be invoked to query created RSU models. | To be tested |

