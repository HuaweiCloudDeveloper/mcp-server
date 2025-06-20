# MPC MCP Server 

## 版本信息
v0.1.0

## 产品描述

MPC MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务MPC交互的能力。可以基于自然语言对MPC资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AnimatedGraphicsTaskManager | ListAnimatedGraphicsTask | 查询动图任务的状态。 | To be tested |
|  | CreateAnimatedGraphicsTask | 创建动图任务,用于将完整的视频文件或视频文件中的一部分转换为动态图文件,暂只支持输出GIF文件。 | To be tested |
|  | DeleteAnimatedGraphicsTask | 取消已下发的生成动图任务,仅支持取消正在排队中的任务。 | To be tested |
| AuthorizationAndConfiguration | NotifySmnTopicConfig | 配置转码服务端事件通知。 | To be tested |
|  | CreateAgenciesTask | 开启或关闭"委托授权", 开启后,媒体处理服务将拥有您所有桶的读写权限,子账号不支持委托授权。 | To be tested |
|  | ListAllBuckets | 请求查询自己创建的指定的桶区域位置的桶列表。 | To be tested |
|  | ListAllObsObjList | 查询桶里的object。 | To be tested |
|  | ListNotifyEvent | 查询消息订阅功能板块, SMN主题的所有订阅事件。 | To be tested |
|  | ListNotifySmnTopicConfig | 查询消息订阅功能板块, SMN主题的订阅事件的启用状态和订阅消息的启用状态。 | To be tested |
|  | UpdateBucketAuthorized | 对OBS桶进行授权或取消授权,媒体处理服务仅拥有已授权桶的读写权限。(暂不支持KMS加密桶的授权) | To be tested |
|  | ShowAgenciesTask | 查询创建委托任务状态。 | To be tested |
| EncryptManager | DeleteEncryptTask | 取消独立加密任务。该API已废弃。 | To be tested |
|  | ListEncryptTask | 查询独立加密任务状态。返回任务执行结果或当前状态。该API已废弃。 | To be tested |
|  | CreateEncryptTask | 支持独立加密,包括创建、查询、删除独立加密任务。该API已废弃。 | To be tested |
| ExtractTaskManager | ListExtractTask | 查询解析任务的状态和结果。 | To be tested |
|  | CreateExtractTask | 创建视频解析任务,解析视频元数据。 | To be tested |
|  | DeleteExtractTask | 取消已下发的视频解析任务,仅支持取消正在排队中的任务。 | To be tested |
| RemuxTaskManager | CreateRemuxTask | 创建转封装任务,转换音视频文件的格式,但不改变其分辨率和码率。 | To be tested |
|  | CreateRetryRemuxTask | 对失败的转封装任务进行重试。 | To be tested |
|  | ListRemuxTask | 查询转封装任务状态。 | To be tested |
|  | CancelRemuxTask | 取消已下发的转封装任务,仅支持取消正在排队中的任务。。 | To be tested |
|  | DeleteRemuxTask | 删除转封装任务记录,只能删除状态为“已取消”,“转码成功”,“转码失败”的任务记录。 | To be tested |
| TemplateGroup | ListTemplateGroup | 查询转码模板组列表。 | To be tested |
|  | DeleteTemplateGroup | 删除转码模板组。 | To be tested |
|  | UpdateTemplateGroup | 修改模板组接口。 | To be tested |
|  | CreateTemplateGroup | 新建转码模板组,最多支持一进六出。 | To be tested |
| TenantAccess | UpdateTenantAccessInfo | 租户开通媒体转码服务。 | To be tested |
|  | ShowTenantAccessInfo | 租户查询媒体转码服务开通状态信息。 | To be tested |
| ThumbnailsTask | CreateThumbnailsTask | 新建截图任务,视频截图将从首帧开始,按设置的时间间隔截图,最后截取末帧。 | To be tested |
|  | DeleteThumbnailsTask | 取消已下发截图任务。 | To be tested |
|  | ListThumbnailsTask | 查询截图任务状态。返回任务执行结果,包括状态、输入、输出等信息。 | To be tested |
| TranscodeTask | CreateTranscodingTask | 新建转码任务可以将视频进行转码,并在转码过程中压制水印、视频截图等。视频转码前需要配置转码模板。 | To be tested |
|  | ListTranscodingTask | 查询转码任务状态。 | To be tested |
|  | DeleteTranscodingTaskByConsole | 删除转码任务记录,只能删除状态为“已取消”,“转码成功”,“转码失败”的转码任务记录。 | To be tested |
|  | DeleteTranscodingTask | 取消已下发转码任务。 | To be tested |
|  | ListStatSummary | 查询最近一周,最近一月或者自定义时间段的“转码时长”,“调用转码API次数”。 | To be tested |
| TranscodeTemplate | ListTemplate | 查询用户自定义转码配置模板。 | To be tested |
|  | UpdateTransTemplate | 更新转码模板。 | To be tested |
|  | DeleteTemplate | 删除转码模板。 | To be tested |
|  | CreateTransTemplate | 新建转码模板,采用自定义的模板转码。 | To be tested |
| WatermarkTemplateManager | ListWatermarkTemplate | 查询自定义水印模板。支持指定模板ID查询,或分页全量查询。 | To be tested |
|  | DeleteWatermarkTemplate | 删除自定义水印模板。 | To be tested |
|  | UpdateWatermarkTemplate | 更新自定义水印模板。 | To be tested |
|  | CreateWatermarkTemplate | 自定义水印模板。 | To be tested |
