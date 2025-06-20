# VOD MCP Server 

## 版本信息
v0.1.0

## 产品描述

VOD MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务VOD交互的能力。可以基于自然语言对VOD资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| OBS托管管理 | ListTakeOverTask | 查询OBS存量托管任务列表。 | To be tested |
|  | ShowTakeOverTaskDetails | 查询OBS存量托管任务详情。 | To be tested |
|  | ShowTakeOverAssetDetails | 查询OBS托管媒资的详细信息。 | To be tested |
| 媒资上传 | PublishAssetFromObs | 若您在使用点播服务前,已经在OBS桶中存储了音视频文件,您可以使用该接口将存储在OBS桶中的音视频文件转存到点播服务中,使用点播服务的音视频管理功能。调用该接口前,您需要调用[桶授权](https://support.huaweicloud.com/api-vod/vod_04_0199.html)接口,将存储音视频文件的OBS桶授权给点播服务。 | To be tested |
|  | UploadMetaDataByUrl | 基于音视频源文件URL,将音视频文件离线拉取上传到点播服务。 | To be tested |
|  | CheckMd5Duplication | 校验媒资文件是否已存储于视频点播服务中。 | To be tested |
|  | UpdateBucketAuthorized | 用户可以通过该接口将OBS桶授权给点播服务或取消点播服务的授权。 | To be tested |
|  | CreateTakeOverTask | 通过存量托管的方式,将已存储在OBS桶中的音视频文件同步到点播服务。 | To be tested |
|  | ShowAssetTempAuthority | 客户端请求创建媒资时,如果媒资文件超过20MB,需采用分段的方式向OBS上传,在每次与OBS交互前,客户端需通过此接口获取到授权方可与OBS交互。 | To be tested |
|  | CreateAssetByFileUpload | 调用该接口创建媒资时,需要将对应的媒资文件上传到点播服务的OBS桶中。 | To be tested |
|  | ConfirmAssetUpload | 媒资分段上传完成后,需要调用此接口通知点播服务媒资上传的状态,表示媒资上传创建完成。 | To be tested |
| 媒资分类 | ListAssetCategory | 查询指定分类信息,及其子分类(即下一级分类)的列表。 | To be tested |
|  | UpdateAssetCategory | 修改媒资分类。 | To be tested |
|  | DeleteAssetCategory | 删除媒资分类。 | To be tested |
|  | CreateAssetCategory | 创建媒资分类。 | To be tested |
| 媒资刷新 | ShowRefreshResult | 查询刷新结果。 | To be tested |
|  | RefreshAsset | 媒资状态为完成态、删除态、发布态,可通过指定媒资ID或URL向CDN进行刷新。将CDN节点缓存的资源强制过期,用户下次访问时CDN将回源获取最新的资源返回给用户,同时将新的资源缓存到CDN节点。单租户每天最多刷新1000个。 | To be tested |
| 媒资处理 | CancelExtractAudioTask | 取消提取音频任务,只有排队中的提取音频任务才可以取消。 | To be tested |
|  | CreateAssetReviewTask | 对上传的媒资进行审核。审核后,可以调用[查询媒资详细信息](https://support.huaweicloud.com/api-vod/vod_04_0202.html)接口查看审核结果。 | To be tested |
|  | CreateAssetProcessTask | 实现视频转码、截图、加密等处理。既可以同时启动多种操作,也可以只启动一种操作。 | To be tested |
|  | UpdateAsset | 媒资创建后,单独上传封面、更新视频文件或更新已有封面。 | To be tested |
|  | UpdateCoverByThumbnail | 将视频截图生成的某张图片设置成封面。 | To be tested |
|  | CancelAssetTranscodeTask | 取消媒资转码任务,只能取消排队中的转码任务。 | To be tested |
|  | CreateExtractAudioTask | 本接口为异步接口,创建音频提取任务下发成功后会返回asset_id和提取的audio_asset_id,但此时音频提取任务并没有立即完成,可通过消息订阅界面配置的音频提取完成事件来获取音频提取任务完成与否。 | To be tested |
| 媒资存储模式管理 | ShowVodRetrieval | ## 典型场景 ## | To be tested |
|  | UpdateStorageModeType | 修改媒资降冷粒度。 | To be tested |
|  | ShowStorageModeType | 查询媒资降冷配置。 | To be tested |
|  | UpdateStorageMode | ## 接口功能 ## | To be tested |
| 媒资管理 | ShowAssetDetail | 查询指定媒资的详细信息。 | To be tested |
|  | UpdateAssetMeta | 修改媒资属性。 | To be tested |
|  | ListAssetList | 查询媒资列表,列表中的每一条记录包含媒资的概要信息。 | To be tested |
|  | ShowAssetMeta | 查询媒资信息,支持指定媒资ID、分类、状态、起止时间查询。 | To be tested |
|  | PublishAssets | 将媒资设置为发布状态。支持批量发布。 | To be tested |
|  | DeleteAssets | 删除媒资。 | To be tested |
|  | UnpublishAssets | 将媒资设置为未发布状态。 | To be tested |
| 媒资预热 | ShowPreheatingAsset | 查询预热结果。 | To be tested |
|  | CreatePreheatingAsset | 媒资发布后,可通过指定媒资ID或URL向CDN预热。用户初次请求时,将由CDN节点提供请求媒资,加快用户下载缓存时间,提高用户体验。单租户每天最多预热1000个。 | To be tested |
| 字幕管理 | ModifySubtitle | 多字幕封装,仅支持 HLS VTT格式和HLS SRT格式 | To be tested |
| 密钥查询 | ShowAssetCipher | 终端播放HLS加密视频时,向租户管理系统请求密钥,租户管理系统先查询其本地有没有已缓存的密钥,没有时则调用此接口向VOD查询。该接口的具体使用场景请参见[通过HLS加密防止视频泄露](https://support.huaweicloud.com/bestpractice-vod/vod_10_0004.html)。 | To be tested |
| 水印模板管理 | UpdateWatermarkTemplate | 修改水印模板 | To be tested |
|  | CreateWatermarkTemplate | 创建水印模板。 | To be tested |
|  | DeleteWatermarkTemplate | 删除水印模板 | To be tested |
|  | ListWatermarkTemplate | 查询水印模板 | To be tested |
|  | ConfirmImageUpload | 确认水印图片上传状态。 | To be tested |
| 统计分析 | ShowVodStatistics | 查询点播源站的统计数据,包括存储空间、转码时长。 | To be tested |
|  | ListDomainLogs | 查询指定点播域名某段时间内在CDN的相关日志。 | To be tested |
|  | ListAssetDailySummaryLog | 查询媒资日播放统计数据。 | To be tested |
|  | ListTopStatistics | 查询指定域名在指定日期播放次数排名Top 100的媒资统计数据。 | To be tested |
|  | ShowCdnStatistics | 查询CDN的统计数据,包括流量、峰值带宽、请求总数、请求命中率、流量命中率。 | To be tested |
| 转码产物管理 | DeleteTranscodeProduct | 删除转码产物。 | To be tested |
| 转码模板管理 | DeleteTranscodeTemplate | 删除自定义模板 | To be tested |
|  | CreateTranscodeTemplate | 创建自定义转码模板。 | To be tested |
|  | UpdateTranscodeTemplate | 修改转码模板 | To be tested |
|  | ListTranscodeTemplate | 查询转码模板列表 | To be tested |
| 转码模板组管理 | DeleteTemplateGroup | 删除自定义转码模板组。 | To be tested |
|  | UpdateTemplateGroup | 修改自定义转码模板组。 | To be tested |
|  | CreateTemplateGroup | 创建自定义转码模板组。 | To be tested |
|  | ListTemplateGroup | 查询转码模板组列表。 | To be tested |
| 转码模板集合管理 | DeleteTemplateGroupCollection | 删除转码模板组集合 | To be tested |
|  | UpdateTemplateGroupCollection | 修改转码模板组结合 | To be tested |
|  | CreateTemplateGroupCollection | 创建转码模板组集合 | To be tested |
|  | ListTemplateGroupCollection | 查询转码模板组集合 | To be tested |
