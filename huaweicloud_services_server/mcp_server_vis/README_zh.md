# VIS MCP Server 

## 版本信息
v0.1.0

## 产品描述

VIS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务VIS交互的能力。可以基于自然语言对VIS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| obs桶策略管理 | UpdateAuthority | 此接口用于用户更新桶授权:授权和取消授权。授权时,operation设置为"ON",取消授权时,operation设置为"OFF"。 | To be tested |
|  | ListBucket | 此接口用于用户获取桶信息列表,桶信息中包含两个字段,分别是桶名称和桶授权信息。 | To be tested |
| 凭证管理 | CreateDeviceCertificate | 该接口用于创建GB/T28181凭证,该凭证用于GB/T28181设备注册时使用。 | To be tested |
|  | ListAkskCertificates | 该接口用于获取所有AK/SK凭证。 | To be tested |
|  | ListDevicesCertificates | 该接口用于获取所有GB/T28181凭证。 | To be tested |
|  | UpdateAksk | 该接口用于更新AK/SK凭证,AK/SK用于RTMP推流的鉴权 | To be tested |
|  | DeleteDeviceCertificate | 该接口用于删除GB/T28181用户的凭证。 | To be tested |
|  | UpdateDeviceCertificate | 该接口用于更新GB/T28181用户名密码凭证。 | To be tested |
|  | DeleteAkskCertificate | 该接口用于删除AKSK凭证。 | To be tested |
|  | CreateAkskCertificate | 该接口用于创建AK/SK凭证,AK/SK用于RTMP视频流推流时的鉴权。 | To be tested |
| 服务开通管理 | CreateSubscription | 此接口用于用户申请开通视频接入服务 | To be tested |
|  | ListSubscriptions | 该接口用于获取服务开通信息 | To be tested |
| 视频流管理 | ListStreamInfos | 此接口用于获取指定视频流的详细信息。 | To be tested |
|  | CreateStream | 该接口用于创建视频流。包括RTMP以及HTTP-FLV类型视频流。 | To be tested |
|  | ListStreams | 此接口用于获取所有视频流的详细信息。 | To be tested |
|  | UpdateRetention | 此接口用于更新视频转储信息。创建的视频流默认没有转储信息,即视频数据不会保存。更新转储信息后可以将视频流保存到指定的存储媒介,如OBS。后续用户可以从OBS上获取到转储的视频。 | To be tested |
|  | UpdateStream | 该接口用于更新视频流的详情,包括RTMP以及HTTP-FLV类型视频流。 | To be tested |
|  | ListStreamsAddresses | 此接口用于获取指定视频流的地址。该地址用于进行视频流推流或者拉流。 | To be tested |
|  | DeleteStream | 此接口用于删除指定视频流。 | To be tested |
| 设备指标统计 | ListLongTermOfflineDevices | 获取当前project下,长期不在线的GB/T28181设备列表。 | To be tested |
|  | ListTodayNewOnlineDevices | 获取当前project下,最新上线(即之前没有上线记录)的GB/T28181设备列表。 | To be tested |
|  | ListNotSendDataDevices | 获取当前project下,从来没有视频数据发送的设备列表。 | To be tested |
|  | ListPastOnlineDevices | 获取当前project下,获取曾经上线的GB/T28181设备列表,即只要上线过的设备信息都会显示。 | To be tested |
|  | ListTodayDroppedDevices | 获取当前project下,最新掉线的GB/T28181设备列表。 | To be tested |
|  | ListTodayPacketReceivedRateDevices | 获取当天有视频接入的GB/T28181设备的平均视频包接受率的列表。 | To be tested |
|  | ListShortTermOfflineDevices | 获取当前project下,最近三天新掉线的设备列表。 | To be tested |
| 设备管理 | UpdateNvrDeviceChannel | 该接口用于更新NVR设备的通道列表。 | To be tested |
|  | UpdateDeviceChannelStrategy | 该接口用于设置GB/T28181设备的视频接入策略。用户可以通过设置接入策略定时自动进行设备的接入。 | To be tested |
|  | DeleteDevice | 此接口用于删除指定设备。 | To be tested |
|  | ListDevices | 此接口用于获取已经注册成功的GB/T28181设备列表。 | To be tested |
|  | CreateDeviceChannel | 此接口用于创建GB/T28181设备(摄像头、网络硬盘录像机等)通道。创建成功之后,自动为GB/T28181设备生成设备ID,以及选择关联的GB/T28181凭证。用户在设备注册时使用该设备ID与凭证,作为设备的用户名以及认证ID址。 | To be tested |
|  | UpdateDeviceChannel | 该接口用于GB/T28181设备进行“视频邀约”和“取消邀约”,配置优先使用TCP传输的配置。 | To be tested |
|  | ListNvrChannels | 此接口用于获取已经注册成功的NVR设备通道列表。 | To be tested |
