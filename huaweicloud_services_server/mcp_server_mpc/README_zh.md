# MPC MCP Server 


## Version
v0.1.0

## Overview

MPC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service MPC. Full-chain management of MPC resources can be carried out based on natural language.

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
                    <td rowspan="3">AnimatedGraphicsTaskManager</td>
                    <td>ListAnimatedGraphicsTask</td>
                    <td>查询动图任务的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAnimatedGraphicsTask</td>
                    <td>创建动图任务,用于将完整的视频文件或视频文件中的一部分转换为动态图文件,暂只支持输出GIF文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAnimatedGraphicsTask</td>
                    <td>取消已下发的生成动图任务,仅支持取消正在排队中的任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">AuthorizationAndConfiguration</td>
                    <td>NotifySmnTopicConfig</td>
                    <td>配置转码服务端事件通知。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgenciesTask</td>
                    <td>开启或关闭"委托授权", 开启后,媒体处理服务将拥有您所有桶的读写权限,子账号不支持委托授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllBuckets</td>
                    <td>请求查询自己创建的指定的桶区域位置的桶列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllObsObjList</td>
                    <td>查询桶里的object。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotifyEvent</td>
                    <td>查询消息订阅功能板块, SMN主题的所有订阅事件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotifySmnTopicConfig</td>
                    <td>查询消息订阅功能板块, SMN主题的订阅事件的启用状态和订阅消息的启用状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgenciesTask</td>
                    <td>查询创建委托任务状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">EncryptManager</td>
                    <td>DeleteEncryptTask</td>
                    <td>取消独立加密任务。该API已废弃。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEncryptTask</td>
                    <td>查询独立加密任务状态。返回任务执行结果或当前状态。该API已废弃。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEncryptTask</td>
                    <td>支持独立加密,包括创建、查询、删除独立加密任务。该API已废弃。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ExtractTaskManager</td>
                    <td>ListExtractTask</td>
                    <td>查询解析任务的状态和结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateExtractTask</td>
                    <td>创建视频解析任务,解析视频元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteExtractTask</td>
                    <td>取消已下发的视频解析任务,仅支持取消正在排队中的任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">RemuxTaskManager</td>
                    <td>CreateRemuxTask</td>
                    <td>创建转封装任务,转换音视频文件的格式,但不改变其分辨率和码率。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRetryRemuxTask</td>
                    <td>对失败的转封装任务进行重试。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRemuxTask</td>
                    <td>查询转封装任务状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelRemuxTask</td>
                    <td>取消已下发的转封装任务,仅支持取消正在排队中的任务。。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRemuxTask</td>
                    <td>删除转封装任务记录,只能删除状态为“已取消”,“转码成功”,“转码失败”的任务记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TemplateManagement</td>
                    <td>DeleteTemplate</td>
                    <td>该接口用于用户删除已创建的模板信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">TenantAccess</td>
                    <td>UpdateTenantAccessInfo</td>
                    <td>租户开通媒体转码服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTenantAccessInfo</td>
                    <td>租户查询媒体转码服务开通状态信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ThumbnailsTask</td>
                    <td>CreateThumbnailsTask</td>
                    <td>新建截图任务,视频截图将从首帧开始,按设置的时间间隔截图,最后截取末帧。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteThumbnailsTask</td>
                    <td>取消已下发截图任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListThumbnailsTask</td>
                    <td>查询截图任务状态。返回任务执行结果,包括状态、输入、输出等信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">TranscodeTask</td>
                    <td>CreateTranscodingTask</td>
                    <td>新建转码任务可以将视频进行转码,并在转码过程中压制水印、视频截图等。视频转码前需要配置转码模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTranscodingTask</td>
                    <td>查询转码任务状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTranscodingTaskByConsole</td>
                    <td>删除转码任务记录,只能删除状态为“已取消”,“转码成功”,“转码失败”的转码任务记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTranscodingTask</td>
                    <td>取消已下发转码任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStatSummary</td>
                    <td>查询最近一周,最近一月或者自定义时间段的“转码时长”,“调用转码API次数”。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">TranscodeTemplate</td>
                    <td>ListTemplate</td>
                    <td>查询用户自定义转码配置模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTransTemplate</td>
                    <td>更新转码模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTransTemplate</td>
                    <td>新建转码模板,采用自定义的模板转码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">媒资上传</td>
                    <td>UpdateBucketAuthorized</td>
                    <td>用户可以通过该接口将OBS桶授权给点播服务或取消点播服务的授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">水印模板管理</td>
                    <td>ListWatermarkTemplate</td>
                    <td>查询水印模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWatermarkTemplate</td>
                    <td>删除水印模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWatermarkTemplate</td>
                    <td>修改水印模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWatermarkTemplate</td>
                    <td>创建水印模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">转码模板组管理</td>
                    <td>ListTemplateGroup</td>
                    <td>查询转码模板组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTemplateGroup</td>
                    <td>删除自定义转码模板组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTemplateGroup</td>
                    <td>修改自定义转码模板组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemplateGroup</td>
                    <td>创建自定义转码模板组。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
