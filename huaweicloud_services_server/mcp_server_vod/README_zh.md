# VOD MCP Server 


## Version
v0.1.0

## Overview

VOD MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VOD. Full-chain management of VOD resources can be carried out based on natural language.

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
                    <td rowspan="3">OBS托管管理</td>
                    <td>ListTakeOverTask</td>
                    <td>查询OBS存量托管任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTakeOverTaskDetails</td>
                    <td>查询OBS存量托管任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTakeOverAssetDetails</td>
                    <td>查询OBS托管媒资的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">媒资上传</td>
                    <td>PublishAssetFromObs</td>
                    <td>若您在使用点播服务前,已经在OBS桶中存储了音视频文件,您可以使用该接口将存储在OBS桶中的音视频文件转存到点播服务中,使用点播服务的音视频管理功能。调用该接口前,您需要调用[桶授权](https://support.huaweicloud.com/api-vod/vod_04_0199.html)接口,将存储音视频文件的OBS桶授权给点播服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadMetaDataByUrl</td>
                    <td>基于音视频源文件URL,将音视频文件离线拉取上传到点播服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckMd5Duplication</td>
                    <td>校验媒资文件是否已存储于视频点播服务中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBucketAuthorized</td>
                    <td>用户可以通过该接口将OBS桶授权给点播服务或取消点播服务的授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTakeOverTask</td>
                    <td>通过存量托管的方式,将已存储在OBS桶中的音视频文件同步到点播服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAssetTempAuthority</td>
                    <td>客户端请求创建媒资时,如果媒资文件超过20MB,需采用分段的方式向OBS上传,在每次与OBS交互前,客户端需通过此接口获取到授权方可与OBS交互。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAssetByFileUpload</td>
                    <td>调用该接口创建媒资时,需要将对应的媒资文件上传到点播服务的OBS桶中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConfirmAssetUpload</td>
                    <td>媒资分段上传完成后,需要调用此接口通知点播服务媒资上传的状态,表示媒资上传创建完成。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">媒资分类</td>
                    <td>ListAssetCategory</td>
                    <td>查询指定分类信息,及其子分类(即下一级分类)的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAssetCategory</td>
                    <td>修改媒资分类。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAssetCategory</td>
                    <td>删除媒资分类。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAssetCategory</td>
                    <td>创建媒资分类。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">媒资刷新</td>
                    <td>ShowRefreshResult</td>
                    <td>查询刷新结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RefreshAsset</td>
                    <td>媒资状态为完成态、删除态、发布态,可通过指定媒资ID或URL向CDN进行刷新。将CDN节点缓存的资源强制过期,用户下次访问时CDN将回源获取最新的资源返回给用户,同时将新的资源缓存到CDN节点。单租户每天最多刷新1000个。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">媒资处理</td>
                    <td>CancelExtractAudioTask</td>
                    <td>取消提取音频任务,只有排队中的提取音频任务才可以取消。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAssetReviewTask</td>
                    <td>对上传的媒资进行审核。审核后,可以调用[查询媒资详细信息](https://support.huaweicloud.com/api-vod/vod_04_0202.html)接口查看审核结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAssetProcessTask</td>
                    <td>实现视频转码、截图、加密等处理。既可以同时启动多种操作,也可以只启动一种操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAsset</td>
                    <td>媒资创建后,单独上传封面、更新视频文件或更新已有封面。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCoverByThumbnail</td>
                    <td>将视频截图生成的某张图片设置成封面。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelAssetTranscodeTask</td>
                    <td>取消媒资转码任务,只能取消排队中的转码任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateExtractAudioTask</td>
                    <td>本接口为异步接口,创建音频提取任务下发成功后会返回asset_id和提取的audio_asset_id,但此时音频提取任务并没有立即完成,可通过消息订阅界面配置的音频提取完成事件来获取音频提取任务完成与否。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">媒资存储模式管理</td>
                    <td>ShowVodRetrieval</td>
                    <td>## 典型场景 ##</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStorageModeType</td>
                    <td>修改媒资降冷粒度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStorageModeType</td>
                    <td>查询媒资降冷配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStorageMode</td>
                    <td>## 接口功能 ##</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">媒资管理</td>
                    <td>ShowAssetDetail</td>
                    <td>查询指定媒资的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAssetMeta</td>
                    <td>修改媒资属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAssetList</td>
                    <td>查询媒资列表,列表中的每一条记录包含媒资的概要信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAssetMeta</td>
                    <td>查询媒资信息,支持指定媒资ID、分类、状态、起止时间查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishAssets</td>
                    <td>将媒资设置为发布状态。支持批量发布。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAssets</td>
                    <td>删除媒资。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnpublishAssets</td>
                    <td>将媒资设置为未发布状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">媒资预热</td>
                    <td>ShowPreheatingAsset</td>
                    <td>查询预热结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePreheatingAsset</td>
                    <td>媒资发布后,可通过指定媒资ID或URL向CDN预热。用户初次请求时,将由CDN节点提供请求媒资,加快用户下载缓存时间,提高用户体验。单租户每天最多预热1000个。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">字幕管理</td>
                    <td>ModifySubtitle</td>
                    <td>多字幕封装,仅支持 HLS VTT格式和HLS SRT格式</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">密钥查询</td>
                    <td>ShowAssetCipher</td>
                    <td>终端播放HLS加密视频时,向租户管理系统请求密钥,租户管理系统先查询其本地有没有已缓存的密钥,没有时则调用此接口向VOD查询。该接口的具体使用场景请参见[通过HLS加密防止视频泄露](https://support.huaweicloud.com/bestpractice-vod/vod_10_0004.html)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">水印模板管理</td>
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
                    <td>DeleteWatermarkTemplate</td>
                    <td>删除水印模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWatermarkTemplate</td>
                    <td>查询水印模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConfirmImageUpload</td>
                    <td>确认水印图片上传状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">统计分析</td>
                    <td>ShowVodStatistics</td>
                    <td>查询点播源站的统计数据,包括存储空间、转码时长。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainLogs</td>
                    <td>查询指定点播域名某段时间内在CDN的相关日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAssetDailySummaryLog</td>
                    <td>查询媒资日播放统计数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopStatistics</td>
                    <td>查询指定域名在指定日期播放次数排名Top 100的媒资统计数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCdnStatistics</td>
                    <td>查询CDN的统计数据,包括流量、峰值带宽、请求总数、请求命中率、流量命中率。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">转码产物管理</td>
                    <td>DeleteTranscodeProduct</td>
                    <td>删除转码产物。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">转码模板管理</td>
                    <td>DeleteTranscodeTemplate</td>
                    <td>删除自定义模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTranscodeTemplate</td>
                    <td>创建自定义转码模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTranscodeTemplate</td>
                    <td>修改转码模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTranscodeTemplate</td>
                    <td>查询转码模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">转码模板组管理</td>
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
                <tr>
                    <td>ListTemplateGroup</td>
                    <td>查询转码模板组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">转码模板集合管理</td>
                    <td>DeleteTemplateGroupCollection</td>
                    <td>删除转码模板组集合</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTemplateGroupCollection</td>
                    <td>修改转码模板组结合</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemplateGroupCollection</td>
                    <td>创建转码模板组集合</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplateGroupCollection</td>
                    <td>查询转码模板组集合</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
