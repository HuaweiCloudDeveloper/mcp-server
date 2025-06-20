# VIS MCP Server 


## Version
v0.1.0

## Overview

VIS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VIS. Full-chain management of VIS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Certificate Management | CreateDeviceCertificate | This API is used to create a GB/T 28181 certificate for device registration. | To be tested |
|  | ListAkskCertificates | This API is used to obtain all AK/SK credentials. | To be tested |
|  | ListDevicesCertificates | This interface is used to obtain all GB/T 28181 credentials. | To be tested |
|  | UpdateAksk | This API is used to update the AK/SK. The AK/SK is used for RTMP streaming authentication. | To be tested |
|  | DeleteDeviceCertificate | This interface is used to delete the credentials of GB/T 28181 users. | To be tested |
|  | UpdateDeviceCertificate | This interface is used to update the GB/T 28181 user name and password credential. | To be tested |
|  | DeleteAkskCertificate | This API is used to delete an AK/SK credential. | To be tested |
|  | CreateAkskCertificate | This API is used to create an AK/SK. The AK/SK is used for authentication during RTMP video stream pushing. | To be tested |
| Device Indicator Statistics | ListLongTermOfflineDevices | Obtain the list of GB/T 28181 devices that have been offline for a long time in the current project. | To be tested |
|  | ListTodayNewOnlineDevices | Obtain the list of GB/T 28181 devices that are newly brought online (no previous online records) in the current project. | To be tested |
|  | ListNotSendDataDevices | Obtain the list of devices that have never sent video data in the current project. | To be tested |
|  | ListPastOnlineDevices | Obtain the list of GB/T 28181 devices that have been online in the current project. That is, all devices that have been online will be displayed. | To be tested |
|  | ListTodayDroppedDevices | Obtains the latest offline GB/T 28181 devices in the current project. | To be tested |
|  | ListTodayPacketReceivedRateDevices | Obtain the list of the average video packet receiving rates of GB/T 28181 devices that have video access on the current day. | To be tested |
|  | ListShortTermOfflineDevices | Obtain the list of devices that are disconnected in the last three days in the current project. | To be tested |
| Device management | UpdateNvrDeviceChannel | This interface is used to update the NVR channel list. | To be tested |
|  | UpdateDeviceChannelStrategy | This interface is used to set video access policies for GB/T 28181 devices. Users can set access policies to automatically access devices at a scheduled time. | To be tested |
|  | DeleteDevice | This API is used to delete a specified device. | To be tested |
|  | ListDevices | This interface is used to obtain the list of registered GB/T 28181 devices. | To be tested |
|  | CreateDeviceChannel | This interface is used to create a channel for a GB/T 28181 device, such as a camera or a network video recorder. After the device is created successfully, the system automatically generates a device ID for the GB/T 28181 device and selects the associated GB/T 28181 certificate. The user uses the device ID and credential as the user name and authentication ID address during device registration. | To be tested |
|  | UpdateDeviceChannel | This interface is used by GB/T 28181 devices to initiate video invitations and cancel invitations. The configuration that TCP transmission is preferentially used is configured. | To be tested |
|  | ListNvrChannels | This interface is used to obtain the channel list of registered NVRs. | To be tested |
| OBS Bucket Policy Management | UpdateAuthority | This API is used to update bucket authorization, including authorization and cancellation. Set operation to "ON" for authorization and "OFF" for authorization cancellation. | To be tested |
|  | ListBucket | This API is used to obtain the bucket list. The bucket list contains two fields: bucket name and bucket authorization information. | To be tested |
| Service provisioning management | CreateSubscription | This interface is used by a user to apply for the video access service. | To be tested |
|  | ListSubscriptions | This interface is used to obtain service provisioning information. | To be tested |
| Video Stream Management | ListStreamInfos | This interface is used to obtain details about a specified video stream. | To be tested |
|  | CreateStream | This interface is used to create video streams. include RTMP and HTTP-FLV type video stream. | To be tested |
|  | ListStreams | This interface is used to obtain details about all video streams. | To be tested |
|  | UpdateRetention | This interface is used to update video dump information. By default, the created video stream does not contain dump information. That is, the video data is not saved. After the dumping information is updated, video streams can be saved to a specified storage medium, such as OBS. You can obtain dumped videos from OBS later. | To be tested |
|  | UpdateStream | This interface is used to update details about video streams, including RTMP and HTTP-FLV video streams. | To be tested |
|  | ListStreamsAddresses | This interface is used to obtain the address of a specified video stream. This address is used to push or pull video streams. | To be tested |
|  | DeleteStream | This interface is used to delete a specified video stream. | To be tested |

