# VIS MCP Server 


## Version
v0.1.0

## Overview

VIS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VIS. Full-chain management of VIS resources can be carried out based on natural language.

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
                    <td rowspan="8">Certificate Management</td>
                    <td>CreateDeviceCertificate</td>
                    <td>This API is used to create a GB/T 28181 certificate for device registration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAkskCertificates</td>
                    <td>This API is used to obtain all AK/SK credentials.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevicesCertificates</td>
                    <td>This interface is used to obtain all GB/T 28181 credentials.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAksk</td>
                    <td>This API is used to update the AK/SK. The AK/SK is used for RTMP streaming authentication.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceCertificate</td>
                    <td>This interface is used to delete the credentials of GB/T 28181 users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceCertificate</td>
                    <td>This interface is used to update the GB/T 28181 user name and password credential.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAkskCertificate</td>
                    <td>This API is used to delete an AK/SK credential.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAkskCertificate</td>
                    <td>This API is used to create an AK/SK. The AK/SK is used for authentication during RTMP video stream pushing.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Device Indicator Statistics</td>
                    <td>ListLongTermOfflineDevices</td>
                    <td>Obtain the list of GB/T 28181 devices that have been offline for a long time in the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTodayNewOnlineDevices</td>
                    <td>Obtain the list of GB/T 28181 devices that are newly brought online (no previous online records) in the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotSendDataDevices</td>
                    <td>Obtain the list of devices that have never sent video data in the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPastOnlineDevices</td>
                    <td>Obtain the list of GB/T 28181 devices that have been online in the current project. That is, all devices that have been online will be displayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTodayDroppedDevices</td>
                    <td>Obtains the latest offline GB/T 28181 devices in the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTodayPacketReceivedRateDevices</td>
                    <td>Obtain the list of the average video packet receiving rates of GB/T 28181 devices that have video access on the current day.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListShortTermOfflineDevices</td>
                    <td>Obtain the list of devices that are disconnected in the last three days in the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Device management</td>
                    <td>UpdateNvrDeviceChannel</td>
                    <td>This interface is used to update the NVR channel list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceChannelStrategy</td>
                    <td>This interface is used to set video access policies for GB/T 28181 devices. Users can set access policies to automatically access devices at a scheduled time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDevice</td>
                    <td>This API is used to delete a specified device.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevices</td>
                    <td>This interface is used to obtain the list of registered GB/T 28181 devices.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeviceChannel</td>
                    <td>This interface is used to create a channel for a GB/T 28181 device, such as a camera or a network video recorder. After the device is created successfully, the system automatically generates a device ID for the GB/T 28181 device and selects the associated GB/T 28181 certificate. The user uses the device ID and credential as the user name and authentication ID address during device registration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceChannel</td>
                    <td>This interface is used by GB/T 28181 devices to initiate video invitations and cancel invitations. The configuration that TCP transmission is preferentially used is configured.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNvrChannels</td>
                    <td>This interface is used to obtain the channel list of registered NVRs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">OBS Bucket Policy Management</td>
                    <td>UpdateAuthority</td>
                    <td>This API is used to update bucket authorization, including authorization and cancellation. Set operation to "ON" for authorization and "OFF" for authorization cancellation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBucket</td>
                    <td>This API is used to obtain the bucket list. The bucket list contains two fields: bucket name and bucket authorization information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Service provisioning management</td>
                    <td>CreateSubscription</td>
                    <td>This interface is used by a user to apply for the video access service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubscriptions</td>
                    <td>This interface is used to obtain service provisioning information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Video Stream Management</td>
                    <td>ListStreamInfos</td>
                    <td>This interface is used to obtain details about a specified video stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStream</td>
                    <td>This interface is used to create video streams. include RTMP and HTTP-FLV type video stream.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStreams</td>
                    <td>This interface is used to obtain details about all video streams.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRetention</td>
                    <td>This interface is used to update video dump information. By default, the created video stream does not contain dump information. That is, the video data is not saved. After the dumping information is updated, video streams can be saved to a specified storage medium, such as OBS. You can obtain dumped videos from OBS later.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStream</td>
                    <td>This interface is used to update details about video streams, including RTMP and HTTP-FLV video streams.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStreamsAddresses</td>
                    <td>This interface is used to obtain the address of a specified video stream. This address is used to push or pull video streams.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStream</td>
                    <td>This interface is used to delete a specified video stream.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
