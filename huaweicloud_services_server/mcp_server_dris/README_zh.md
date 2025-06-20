# DRIS MCP Server 

## 版本信息
v0.1.0

## 产品描述

DRIS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DRIS交互的能力。可以基于自然语言对DRIS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| APIG-SN-DATACHANNEL | CreateDataChannel | 创建业务通道,用于创建Edge消息上报的数据通道。 | To be tested |
|  | UpdateDataChannel | 修改业务通道 | To be tested |
|  | ShowDataChannel | 查询业务通道 | To be tested |
|  | DeleteDataChannel | 删除业务通道 | To be tested |
| APIG-SN-EDGE | ShowDeploymentCode | 生成部署应用安装命令,然后在ITS800或者ATLAS500上通过Shell执行 | To be tested |
|  | DeleteV2XEdgeByV2xEdgeId | 删除Edge之前需要删除Edge下的业务通道和关联设备。 | To be tested |
|  | ShowV2xEdgeDetail | 查询Edge | To be tested |
|  | UpdateV2xEdge | 修改Edge | To be tested |
|  | CreateV2xEdge | 创建Edge | To be tested |
|  | ListV2xEdges | 查询Edge列表 | To be tested |
| APIG-SN-ForwardingConfigResources | ShowForwardingConfigs | 查询数据转发配置列表 | To be tested |
|  | DeleteForwardingConfig | 根据转发配置的唯一ID(forwarding_config_id)删除数据转发配置,删除后配置中订阅的topic消息将不会被转发至brokers。 | To be tested |
|  | AddForwardingConfigs | 创建数据转发配置。当前仅支持数据转发至kafka,数据转发配置成功添加后配置中的Topic消息将会转发至指定的brokers。 | To be tested |
|  | UpdateForwardingConfig | 根据转发配置的唯一ID(forwarding_config_id)修改数据转发配置,当前支持更新的字段有topicPrefix、userTopics、brokers,需要把该字段新的对应值全量写入。 | To be tested |
|  | ShowForwardingConfig | 根据转发配置的唯一ID(forwarding_config_id)查询数据转发配置 | To be tested |
| APIG-SN-HistoryTrafficEvents | ShowHistoryTrafficEvents | 查询历史交通事件列表 | To be tested |
|  | ListEdgeFlows | 查询历史交通统计信息列表 | To be tested |
| APIG-SN-IPC | ShowIpc | 查询IPC | To be tested |
|  | BatchShowIpcs | 获取多个IPC资源 | To be tested |
| APIG-SN-RADAR | BatchShowRadars | 查询雷达列表 | To be tested |
| APIG-SN-RSU | UpdateRsu | 修改RSU | To be tested |
|  | DeleteRsu | 删除RSU | To be tested |
|  | CreateRsu | 创建RSU | To be tested |
|  | BatchShowRsus | 查询RSU列表 | To be tested |
| APIG-SN-SendImmediateEvent | SendImmediateEvent | 创建即时交通事件,平台分发即时交通事件给目标设备的接口。事件一旦创建便会立即下发且只会下发一次。 | To be tested |
| APIG-SN-TRAFFIC-CONTROLLER | DeleteTrafficController | 删除信号机 | To be tested |
|  | CreateTrafficController | 创建信号机 | To be tested |
|  | BatchShowTrafficControllers | 查询信号机列表 | To be tested |
|  | UpdateTrafficController | 修改信号机 | To be tested |
| APIG-SN-TRAFFICEVENT | BatchShowTrafficEvents | 条件查询交通事件 | To be tested |
|  | ShowTrafficEvent | 查询长期交通事件 | To be tested |
|  | CreateTrafficEvent | 创建长期交通事件时,平台根据事件的起始时间和结束时间确定当前长期交通事件的状态。对于活跃状态的交通事件会立即下发给在事件影响范围内的RSU,对于未来事件则是在事件开始时间点下发到在事件影响范围内的RSU,过期事件不会下发。 | To be tested |
|  | UpdateTrafficEvent | 修改长期交通事件 | To be tested |
|  | DeleteTrafficEvent | 刪除长期交通事件 | To be tested |
| APIG-SN-V2XEDGE-APP | UpdateV2xEdgeApp | **升级边缘应用前需确保**: | To be tested |
|  | ShowV2XEdgeAppDetailByEdgeAppId | 查询边缘应用 | To be tested |
|  | CreateV2xEdgeApp | **部署边缘应用前需确保**: | To be tested |
|  | ListV2xEdgeApp | 查询边缘应用列表 | To be tested |
|  | DeleteV2XEdgeAppByEdgeAppId | 删除系统应用($edgetepa)前应先删除业务通道。如删除边缘应用接口调用成功,稍后边缘设备将会自动删除应用无需手动操作。 | To be tested |
| APIG-SN-VEHICLE | CreateVehicle | 创建车辆 | To be tested |
|  | BatchShowVehicles | 查询车辆列表 | To be tested |
|  | DeleteVehicle | 删除车辆 | To be tested |
|  | UpdateVehicle | 修改车辆 | To be tested |
| EdgeAppManagement | BatchShowEdgeApps | 查询应用列表 | To be tested |
|  | DeleteEdgeApp | 删除应用 | To be tested |
|  | CreateEdgeApp | 创建应用 | To be tested |
|  | UpdateEdgeApp | 修改应用 | To be tested |
| EdgeAppVersionManagement | ShowEdgeApplicationVersion | 查询应用版本 | To be tested |
|  | UpdateEdgeApplicationVersion | 修改应用版本 | To be tested |
|  | CreateEdgeApplicationVersion | 创建应用版本 | To be tested |
|  | BatchShowEdgeAppVersions | 查询应用版本列表 | To be tested |
|  | UpdateEdgeApplicationVersionState | 更新应用版本状态。 | To be tested |
|  | DeleteEdgeApplicationVersion | 删除应用版本 | To be tested |
| RsuModelManagement | UpdateRsuModel | 可调用此接口修改已创建的RSU型号。 | To be tested |
|  | DeleteRsuModel | 可调用此接口删除已创建的RSU型号。 | To be tested |
|  | CreateRsuModel | 调用此接口可创建RSU型号。 | To be tested |
|  | ListRsuModels | 可调用此接口查询已创建RSU型号列表。 | To be tested |
|  | ShowRsuModel | 可调用此接口查询已创建的RSU型号。 | To be tested |
