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
                    <td>创建业务通道,用于创建Edge消息上报的数据通道。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataChannel</td>
                    <td>修改业务通道</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataChannel</td>
                    <td>查询业务通道</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDataChannel</td>
                    <td>删除业务通道</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">APIG-SN-EDGE</td>
                    <td>ShowDeploymentCode</td>
                    <td>生成部署应用安装命令,然后在ITS800或者ATLAS500上通过Shell执行</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteV2XEdgeByV2xEdgeId</td>
                    <td>删除Edge之前需要删除Edge下的业务通道和关联设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowV2xEdgeDetail</td>
                    <td>查询Edge</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateV2xEdge</td>
                    <td>修改Edge</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateV2xEdge</td>
                    <td>创建Edge</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListV2xEdges</td>
                    <td>查询Edge列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">APIG-SN-ForwardingConfigResources</td>
                    <td>ShowForwardingConfigs</td>
                    <td>查询数据转发配置列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteForwardingConfig</td>
                    <td>根据转发配置的唯一ID(forwarding_config_id)删除数据转发配置,删除后配置中订阅的topic消息将不会被转发至brokers。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddForwardingConfigs</td>
                    <td>创建数据转发配置。当前仅支持数据转发至kafka,数据转发配置成功添加后配置中的Topic消息将会转发至指定的brokers。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateForwardingConfig</td>
                    <td>根据转发配置的唯一ID(forwarding_config_id)修改数据转发配置,当前支持更新的字段有topicPrefix、userTopics、brokers,需要把该字段新的对应值全量写入。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowForwardingConfig</td>
                    <td>根据转发配置的唯一ID(forwarding_config_id)查询数据转发配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">APIG-SN-HistoryTrafficEvents</td>
                    <td>ShowHistoryTrafficEvents</td>
                    <td>查询历史交通事件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeFlows</td>
                    <td>查询历史交通统计信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">APIG-SN-IPC</td>
                    <td>ShowIpc</td>
                    <td>查询IPC</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowIpcs</td>
                    <td>获取多个IPC资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">APIG-SN-RADAR</td>
                    <td>BatchShowRadars</td>
                    <td>查询雷达列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">APIG-SN-RSU</td>
                    <td>UpdateRsu</td>
                    <td>修改RSU</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRsu</td>
                    <td>删除RSU</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRsu</td>
                    <td>创建RSU</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowRsus</td>
                    <td>查询RSU列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">APIG-SN-SendImmediateEvent</td>
                    <td>SendImmediateEvent</td>
                    <td>创建即时交通事件,平台分发即时交通事件给目标设备的接口。事件一旦创建便会立即下发且只会下发一次。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">APIG-SN-TRAFFIC-CONTROLLER</td>
                    <td>DeleteTrafficController</td>
                    <td>删除信号机</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrafficController</td>
                    <td>创建信号机</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowTrafficControllers</td>
                    <td>查询信号机列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTrafficController</td>
                    <td>修改信号机</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">APIG-SN-TRAFFICEVENT</td>
                    <td>BatchShowTrafficEvents</td>
                    <td>条件查询交通事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrafficEvent</td>
                    <td>查询长期交通事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrafficEvent</td>
                    <td>创建长期交通事件时,平台根据事件的起始时间和结束时间确定当前长期交通事件的状态。对于活跃状态的交通事件会立即下发给在事件影响范围内的RSU,对于未来事件则是在事件开始时间点下发到在事件影响范围内的RSU,过期事件不会下发。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTrafficEvent</td>
                    <td>修改长期交通事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrafficEvent</td>
                    <td>刪除长期交通事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">APIG-SN-V2XEDGE-APP</td>
                    <td>UpdateV2xEdgeApp</td>
                    <td>**升级边缘应用前需确保**:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowV2XEdgeAppDetailByEdgeAppId</td>
                    <td>查询边缘应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateV2xEdgeApp</td>
                    <td>**部署边缘应用前需确保**:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListV2xEdgeApp</td>
                    <td>查询边缘应用列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteV2XEdgeAppByEdgeAppId</td>
                    <td>删除系统应用($edgetepa)前应先删除业务通道。如删除边缘应用接口调用成功,稍后边缘设备将会自动删除应用无需手动操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">APIG-SN-VEHICLE</td>
                    <td>CreateVehicle</td>
                    <td>创建车辆</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowVehicles</td>
                    <td>查询车辆列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVehicle</td>
                    <td>删除车辆</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVehicle</td>
                    <td>修改车辆</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">EdgeAppManagement</td>
                    <td>BatchShowEdgeApps</td>
                    <td>查询应用列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeApp</td>
                    <td>删除应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeApp</td>
                    <td>创建应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeApp</td>
                    <td>修改应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">EdgeAppVersionManagement</td>
                    <td>ShowEdgeApplicationVersion</td>
                    <td>查询应用版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeApplicationVersion</td>
                    <td>修改应用版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeApplicationVersion</td>
                    <td>创建应用版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowEdgeAppVersions</td>
                    <td>查询应用版本列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeApplicationVersionState</td>
                    <td>更新应用版本状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeApplicationVersion</td>
                    <td>删除应用版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">RsuModelManagement</td>
                    <td>UpdateRsuModel</td>
                    <td>可调用此接口修改已创建的RSU型号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRsuModel</td>
                    <td>可调用此接口删除已创建的RSU型号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRsuModel</td>
                    <td>调用此接口可创建RSU型号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRsuModels</td>
                    <td>可调用此接口查询已创建RSU型号列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRsuModel</td>
                    <td>可调用此接口查询已创建的RSU型号。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
