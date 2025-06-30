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
                    <td>Query the status of a motion picture task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAnimatedGraphicsTask</td>
                    <td>Create an animation task to convert a complete video file or part of a video file into a dynamic image file. Currently, only GIF files are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAnimatedGraphicsTask</td>
                    <td>Cancels delivered animation generation tasks. Only tasks in the queue can be canceled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">AuthorizationAndConfiguration</td>
                    <td>NotifySmnTopicConfig</td>
                    <td>Configure the transcoding server event notification.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgenciesTask</td>
                    <td>Enable or disable delegated authorization". After the permission is enabled, MPS has the read and write permissions on all your buckets. Member accounts do not support delegated authorization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllBuckets</td>
                    <td>This API is used to query the bucket list created by the user in a specified region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllObsObjList</td>
                    <td>Query objects in a bucket.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotifyEvent</td>
                    <td>Query all subscription events of an SMN topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotifySmnTopicConfig</td>
                    <td>Query the status of subscription events and messages of the SMN topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgenciesTask</td>
                    <td>Query the status of creating an entrusted task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">EncryptManager</td>
                    <td>DeleteEncryptTask</td>
                    <td>Cancel the independent encryption task. This API is deprecated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEncryptTask</td>
                    <td>Query the status of an independent encryption task. Return the task execution result or current status. This API is deprecated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEncryptTask</td>
                    <td>Independent encryption is supported, including creating, querying, and deleting independent encryption tasks. This API is deprecated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ExtractTaskManager</td>
                    <td>ListExtractTask</td>
                    <td>Query the status and result of a parsing task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateExtractTask</td>
                    <td>Create a video parsing task to parse video metadata.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteExtractTask</td>
                    <td>Cancels delivered video parsing tasks. Only the tasks in the queue can be canceled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">RemuxTaskManager</td>
                    <td>CreateRemuxTask</td>
                    <td>Create an encapsulation task to convert the formats of audio and video files without changing the resolution and bit rate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRetryRemuxTask</td>
                    <td>Retry the failed repackaging task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRemuxTask</td>
                    <td>Query the repackaging task status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelRemuxTask</td>
                    <td>Cancel delivered repackaging tasks. Only the tasks in the queue can be canceled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRemuxTask</td>
                    <td>Delete repackaging task records. Only the records in the Canceled, Transcoding succeeded, or Transcoding failed states can be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TemplateManagement</td>
                    <td>DeleteTemplate</td>
                    <td>This API is used to delete a created template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">TenantAccess</td>
                    <td>UpdateTenantAccessInfo</td>
                    <td>The tenant enables the media transcoding service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTenantAccessInfo</td>
                    <td>Query the status of the media transcoding service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ThumbnailsTask</td>
                    <td>CreateThumbnailsTask</td>
                    <td>Create a snapshot task. The first frame is taken, the last frame is taken at the specified interval, and the last frame is taken.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteThumbnailsTask</td>
                    <td>Cancel the delivered snapshot task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListThumbnailsTask</td>
                    <td>Query the status of a screenshot task. Return the task execution result, including the status, input, and output.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">TranscodeTask</td>
                    <td>CreateTranscodingTask</td>
                    <td>You can create a transcoding task to transcode videos and suppress watermarks and screenshots during the transcoding. Before video transcoding, you need to configure a transcoding template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTranscodingTask</td>
                    <td>Query the status of the transcoding task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTranscodingTaskByConsole</td>
                    <td>Delete transcoding task records. Only the records in the Cancelled, Transcoding succeeded, or Transcoding failed states can be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTranscodingTask</td>
                    <td>Cancel the delivered transcoding task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStatSummary</td>
                    <td>Query the Transcoding Duration and Transcoding API Call Times in the last week, month, or customized period.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">TranscodeTemplate</td>
                    <td>ListTemplate</td>
                    <td>Query the user-defined transcoding configuration template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTransTemplate</td>
                    <td>Update the transcoding template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTransTemplate</td>
                    <td>Create a transcoding template and use the customized template for transcoding.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Transcoding template group management</td>
                    <td>ListTemplateGroup</td>
                    <td>Query the transcoding template group list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTemplateGroup</td>
                    <td>Delete the customized transcoding template group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTemplateGroup</td>
                    <td>Modify the customized transcoding template group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemplateGroup</td>
                    <td>Create a customized transcoding template group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Upload media asset</td>
                    <td>UpdateBucketAuthorized</td>
                    <td>You can call this API to authorize or cancel the authorization of an OBS bucket to the VOD service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Watermark Template Management</td>
                    <td>ListWatermarkTemplate</td>
                    <td>Query the watermark template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWatermarkTemplate</td>
                    <td>Delete a watermark template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWatermarkTemplate</td>
                    <td>Modifying a watermark template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWatermarkTemplate</td>
                    <td>Create a watermark template.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
