# MPC MCP Server 


## Version
v0.1.0

## Overview

MPC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service MPC. Full-chain management of MPC resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AnimatedGraphicsTaskManager | ListAnimatedGraphicsTask | Query the status of a motion picture task. | To be tested |
|  | CreateAnimatedGraphicsTask | Create an animation task to convert a complete video file or part of a video file into a dynamic image file. Currently, only GIF files are supported. | To be tested |
|  | DeleteAnimatedGraphicsTask | Cancels delivered animation generation tasks. Only tasks in the queue can be canceled. | To be tested |
| AuthorizationAndConfiguration | NotifySmnTopicConfig | Configure the transcoding server event notification. | To be tested |
|  | CreateAgenciesTask | Enable or disable delegated authorization". After the permission is enabled, MPS has the read and write permissions on all your buckets. Member accounts do not support delegated authorization. | To be tested |
|  | ListAllBuckets | This API is used to query the bucket list created by the user in a specified region. | To be tested |
|  | ListAllObsObjList | Query objects in a bucket. | To be tested |
|  | ListNotifyEvent | Query all subscription events of an SMN topic. | To be tested |
|  | ListNotifySmnTopicConfig | Query the status of subscription events and messages of the SMN topic. | To be tested |
|  | ShowAgenciesTask | Query the status of creating an entrusted task. | To be tested |
| EncryptManager | DeleteEncryptTask | Cancel the independent encryption task. This API is deprecated. | To be tested |
|  | ListEncryptTask | Query the status of an independent encryption task. Return the task execution result or current status. This API is deprecated. | To be tested |
|  | CreateEncryptTask | Independent encryption is supported, including creating, querying, and deleting independent encryption tasks. This API is deprecated. | To be tested |
| ExtractTaskManager | ListExtractTask | Query the status and result of a parsing task. | To be tested |
|  | CreateExtractTask | Create a video parsing task to parse video metadata. | To be tested |
|  | DeleteExtractTask | Cancels delivered video parsing tasks. Only the tasks in the queue can be canceled. | To be tested |
| RemuxTaskManager | CreateRemuxTask | Create an encapsulation task to convert the formats of audio and video files without changing the resolution and bit rate. | To be tested |
|  | CreateRetryRemuxTask | Retry the failed repackaging task. | To be tested |
|  | ListRemuxTask | Query the repackaging task status. | To be tested |
|  | CancelRemuxTask | Cancel delivered repackaging tasks. Only the tasks in the queue can be canceled. | To be tested |
|  | DeleteRemuxTask | Delete repackaging task records. Only the records in the Canceled, Transcoding succeeded, or Transcoding failed states can be deleted. | To be tested |
| TemplateManagement | DeleteTemplate | This API is used to delete a created template. | To be tested |
| TenantAccess | UpdateTenantAccessInfo | The tenant enables the media transcoding service. | To be tested |
|  | ShowTenantAccessInfo | Query the status of the media transcoding service. | To be tested |
| ThumbnailsTask | CreateThumbnailsTask | Create a snapshot task. The first frame is taken, the last frame is taken at the specified interval, and the last frame is taken. | To be tested |
|  | DeleteThumbnailsTask | Cancel the delivered snapshot task. | To be tested |
|  | ListThumbnailsTask | Query the status of a screenshot task. Return the task execution result, including the status, input, and output. | To be tested |
| TranscodeTask | CreateTranscodingTask | You can create a transcoding task to transcode videos and suppress watermarks and screenshots during the transcoding. Before video transcoding, you need to configure a transcoding template. | To be tested |
|  | ListTranscodingTask | Query the status of the transcoding task. | To be tested |
|  | DeleteTranscodingTaskByConsole | Delete transcoding task records. Only the records in the Cancelled, Transcoding succeeded, or Transcoding failed states can be deleted. | To be tested |
|  | DeleteTranscodingTask | Cancel the delivered transcoding task. | To be tested |
|  | ListStatSummary | Query the Transcoding Duration and Transcoding API Call Times in the last week, month, or customized period. | To be tested |
| TranscodeTemplate | ListTemplate | Query the user-defined transcoding configuration template. | To be tested |
|  | UpdateTransTemplate | Update the transcoding template. | To be tested |
|  | CreateTransTemplate | Create a transcoding template and use the customized template for transcoding. | To be tested |
| Transcoding template group management | ListTemplateGroup | Query the transcoding template group list. | To be tested |
|  | DeleteTemplateGroup | Delete the customized transcoding template group. | To be tested |
|  | UpdateTemplateGroup | Modify the customized transcoding template group. | To be tested |
|  | CreateTemplateGroup | Create a customized transcoding template group. | To be tested |
| Upload media asset | UpdateBucketAuthorized | You can call this API to authorize or cancel the authorization of an OBS bucket to the VOD service. | To be tested |
| Watermark Template Management | ListWatermarkTemplate | Query the watermark template | To be tested |
|  | DeleteWatermarkTemplate | Delete a watermark template | To be tested |
|  | UpdateWatermarkTemplate | Modifying a watermark template | To be tested |
|  | CreateWatermarkTemplate | Create a watermark template. | To be tested |

