# Moderation MCP Server 

## 版本信息
v0.1.0

## 产品描述

Moderation MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务Moderation交互的能力。可以基于自然语言对Moderation资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 图像内容审核 | CheckImageModeration | 分析并识别用户上传的图像内容是否有敏感内容(如涉及暴恐元素、涉黄内容等),并将识别结果返回给用户。 | To be tested |
| 图像审核批量同步接口 | BatchCheckImageSync | 图像审核批量同步接口 | To be tested |
| 文本内容审核 | RunTextModeration | 分析并识别用户上传的文本内容是否有敏感内容(如色情、政治等),并将识别结果返回给用户 | To be tested |
| 视频内容审核 | RunCreateVideoModerationJob | 创建视频内容审核作业,创建成功会将作业ID返回给用户 | To be tested |
|  | RunQueryVideoModerationJob | 查询视频审核作业处理状态与结果,并将识别结果返回给用户 | To be tested |
| 音频内容审核 | RunQueryAudioModerationJob |  | To be tested |
|  | RunCreateAudioModerationJob | 分析并识别用户上传的音频内容是否有敏感内容(如色情、政治等),并将识别结果返回给用户 | To be tested |
| 音频流内容审核 | RunCloseAudioStreamModerationJob | 关闭音频流内容审核作业 | To be tested |
|  | RunCreateAudioStreamModerationJob | 创建音频流内容审核作业,创建成功会将作业ID返回给用户 | To be tested |
