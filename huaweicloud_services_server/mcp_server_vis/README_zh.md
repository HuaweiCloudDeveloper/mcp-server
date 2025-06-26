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
                    <td rowspan="2">obs桶策略管理</td>
                    <td>UpdateAuthority</td>
                    <td>此接口用于用户更新桶授权:授权和取消授权。授权时,operation设置为"ON",取消授权时,operation设置为"OFF"。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBucket</td>
                    <td>此接口用于用户获取桶信息列表,桶信息中包含两个字段,分别是桶名称和桶授权信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">凭证管理</td>
                    <td>CreateDeviceCertificate</td>
                    <td>该接口用于创建GB/T28181凭证,该凭证用于GB/T28181设备注册时使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAkskCertificates</td>
                    <td>该接口用于获取所有AK/SK凭证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevicesCertificates</td>
                    <td>该接口用于获取所有GB/T28181凭证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAksk</td>
                    <td>该接口用于更新AK/SK凭证,AK/SK用于RTMP推流的鉴权</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceCertificate</td>
                    <td>该接口用于删除GB/T28181用户的凭证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceCertificate</td>
                    <td>该接口用于更新GB/T28181用户名密码凭证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAkskCertificate</td>
                    <td>该接口用于删除AKSK凭证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAkskCertificate</td>
                    <td>该接口用于创建AK/SK凭证,AK/SK用于RTMP视频流推流时的鉴权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">服务开通管理</td>
                    <td>CreateSubscription</td>
                    <td>此接口用于用户申请开通视频接入服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubscriptions</td>
                    <td>该接口用于获取服务开通信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">视频流管理</td>
                    <td>ListStreamInfos</td>
                    <td>此接口用于获取指定视频流的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStream</td>
                    <td>该接口用于创建视频流。包括RTMP以及HTTP-FLV类型视频流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStreams</td>
                    <td>此接口用于获取所有视频流的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRetention</td>
                    <td>此接口用于更新视频转储信息。创建的视频流默认没有转储信息,即视频数据不会保存。更新转储信息后可以将视频流保存到指定的存储媒介,如OBS。后续用户可以从OBS上获取到转储的视频。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStream</td>
                    <td>该接口用于更新视频流的详情,包括RTMP以及HTTP-FLV类型视频流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStreamsAddresses</td>
                    <td>此接口用于获取指定视频流的地址。该地址用于进行视频流推流或者拉流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStream</td>
                    <td>此接口用于删除指定视频流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">设备指标统计</td>
                    <td>ListLongTermOfflineDevices</td>
                    <td>获取当前project下,长期不在线的GB/T28181设备列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTodayNewOnlineDevices</td>
                    <td>获取当前project下,最新上线(即之前没有上线记录)的GB/T28181设备列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotSendDataDevices</td>
                    <td>获取当前project下,从来没有视频数据发送的设备列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPastOnlineDevices</td>
                    <td>获取当前project下,获取曾经上线的GB/T28181设备列表,即只要上线过的设备信息都会显示。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTodayDroppedDevices</td>
                    <td>获取当前project下,最新掉线的GB/T28181设备列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTodayPacketReceivedRateDevices</td>
                    <td>获取当天有视频接入的GB/T28181设备的平均视频包接受率的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListShortTermOfflineDevices</td>
                    <td>获取当前project下,最近三天新掉线的设备列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">设备管理</td>
                    <td>UpdateNvrDeviceChannel</td>
                    <td>该接口用于更新NVR设备的通道列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceChannelStrategy</td>
                    <td>该接口用于设置GB/T28181设备的视频接入策略。用户可以通过设置接入策略定时自动进行设备的接入。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDevice</td>
                    <td>此接口用于删除指定设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevices</td>
                    <td>此接口用于获取已经注册成功的GB/T28181设备列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeviceChannel</td>
                    <td>此接口用于创建GB/T28181设备(摄像头、网络硬盘录像机等)通道。创建成功之后,自动为GB/T28181设备生成设备ID,以及选择关联的GB/T28181凭证。用户在设备注册时使用该设备ID与凭证,作为设备的用户名以及认证ID址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceChannel</td>
                    <td>该接口用于GB/T28181设备进行“视频邀约”和“取消邀约”,配置优先使用TCP传输的配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNvrChannels</td>
                    <td>此接口用于获取已经注册成功的NVR设备通道列表。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
