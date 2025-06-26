# DRIS MCP Server 


## Version
v0.1.0

## Overview

DRIS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DRIS. Full-chain management of DRIS resources can be carried out based on natural language.

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
                    <td rowspan="4">APIG-SN-DATACHANNEL</td>
                    <td>CreateDataChannel</td>
                    <td>Create a service channel, which is used to create a data channel for reporting Edge messages.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataChannel</td>
                    <td>Modifying a service channel</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataChannel</td>
                    <td>Query a service channel</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDataChannel</td>
                    <td>Delete a service channel</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">APIG-SN-EDGE</td>
                    <td>ShowDeploymentCode</td>
                    <td>Generate the application installation command and run it on the ITS800 or ATLAS500 through the shell.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteV2XEdgeByV2xEdgeId</td>
                    <td>Before deleting an edge, you need to delete the service channels and associated devices under the edge.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowV2xEdgeDetail</td>
                    <td>Query Edge</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateV2xEdge</td>
                    <td>Modifying Edge</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateV2xEdge</td>
                    <td>Create Edge</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListV2xEdges</td>
                    <td>Query the edge list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">APIG-SN-ForwardingConfigResources</td>
                    <td>ShowForwardingConfigs</td>
                    <td>Query the data forwarding configuration list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteForwardingConfig</td>
                    <td>Delete the data forwarding configuration based on the unique ID (forwarding_config_id) of the forwarding configuration. After the deletion, the subscribed topic messages will not be forwarded to brokers.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddForwardingConfigs</td>
                    <td>Create a data forwarding configuration. Currently, only data can be forwarded to Kafka. After the data forwarding configuration is added, topic messages in the configuration will be forwarded to the specified brokers.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateForwardingConfig</td>
                    <td>Modify the data forwarding configuration based on the unique ID (forwarding_config_id) of the forwarding configuration. Currently, the topicPrefix, userTopics, and brokers fields can be updated. You need to write all the new values of the fields.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowForwardingConfig</td>
                    <td>Query the data forwarding configuration based on the unique ID (forwarding_config_id) of the forwarding configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">APIG-SN-HistoryTrafficEvents</td>
                    <td>ShowHistoryTrafficEvents</td>
                    <td>Query the historical traffic event list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeFlows</td>
                    <td>Query the historical traffic statistics list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">APIG-SN-IPC</td>
                    <td>ShowIpc</td>
                    <td>Querying IPCs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowIpcs</td>
                    <td>Obtaining multiple IPC resources</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">APIG-SN-RADAR</td>
                    <td>BatchShowRadars</td>
                    <td>Query the radar list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">APIG-SN-RSU</td>
                    <td>UpdateRsu</td>
                    <td>Modifying an RSU</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRsu</td>
                    <td>Delete RSU</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRsu</td>
                    <td>Create RSU</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowRsus</td>
                    <td>Query the RSU list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">APIG-SN-SendImmediateEvent</td>
                    <td>SendImmediateEvent</td>
                    <td>Interface for creating an instant traffic event. The IoT platform distributes the instant traffic event to the target device. Once an event is created, it will be delivered immediately and only once.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">APIG-SN-TRAFFIC-CONTROLLER</td>
                    <td>DeleteTrafficController</td>
                    <td>Delete signal controller</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrafficController</td>
                    <td>Create signal controller</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowTrafficControllers</td>
                    <td>Query the signal controller list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTrafficController</td>
                    <td>Modifying the signal controller</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">APIG-SN-TRAFFICEVENT</td>
                    <td>BatchShowTrafficEvents</td>
                    <td>Query traffic events by conditions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrafficEvent</td>
                    <td>Query long-term traffic events</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrafficEvent</td>
                    <td>When a long-term traffic event is created, the IoT platform determines the status of the long-term traffic event based on the start time and end time of the event. For active traffic events, the system immediately delivers RSUs within the impact scope of the event. For future events, the system delivers RSUs within the impact scope at the start time of the event. Expired events will not be delivered.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTrafficEvent</td>
                    <td>Modifying a long-term traffic event</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrafficEvent</td>
                    <td>Delete long-term traffic events</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">APIG-SN-V2XEDGE-APP</td>
                    <td>UpdateV2xEdgeApp</td>
                    <td>**Before upgrading an edge application, ensure that * *:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowV2XEdgeAppDetailByEdgeAppId</td>
                    <td>Query edge applications</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateV2xEdgeApp</td>
                    <td>**Before deploying an edge application, ensure that * *:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListV2xEdgeApp</td>
                    <td>Query the edge application list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteV2XEdgeAppByEdgeAppId</td>
                    <td>Before deleting the system application ($edgetepa), delete the service channel. If the API for deleting an edge application is invoked successfully, the edge device automatically deletes the application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">APIG-SN-VEHICLE</td>
                    <td>CreateVehicle</td>
                    <td>Create a vehicle</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowVehicles</td>
                    <td>Query the vehicle list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVehicle</td>
                    <td>Deleting a vehicle</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVehicle</td>
                    <td>Modifying a vehicle</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">EdgeAppManagement</td>
                    <td>BatchShowEdgeApps</td>
                    <td>Query the application list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeApp</td>
                    <td>Delete an application</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeApp</td>
                    <td>Create an application</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeApp</td>
                    <td>Modifying an application</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">EdgeAppVersionManagement</td>
                    <td>ShowEdgeApplicationVersion</td>
                    <td>Query the application version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeApplicationVersion</td>
                    <td>Modifying the application version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeApplicationVersion</td>
                    <td>Create an application version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowEdgeAppVersions</td>
                    <td>Query the application version list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeApplicationVersionState</td>
                    <td>Update the application version status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeApplicationVersion</td>
                    <td>Delete an application version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">RsuModelManagement</td>
                    <td>UpdateRsuModel</td>
                    <td>You can invoke this interface to modify the model of an existing RSU.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRsuModel</td>
                    <td>You can invoke this interface to delete a created RSU model.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRsuModel</td>
                    <td>This interface is used to create an RSU model.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRsuModels</td>
                    <td>This interface can be invoked to query the created RSU model list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRsuModel</td>
                    <td>This interface can be invoked to query created RSU models.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
