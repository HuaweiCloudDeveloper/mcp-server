# CBS MCP Server 

## 版本信息
v0.1.0

## 产品描述

CBS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CBS交互的能力。可以基于自然语言对CBS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 其他问答 | ListSuggestions | 获取用户输入问题的提示问题列表。 | To be tested |
|  | TagLabor | 智能问答返回的结果后,用户是否转人工。 | To be tested |
|  | TagSatisfaction | 用户提出问题后,对智能问答返回的结果是否满意。 | To be tested |
| 其他问答API | PostRequests | 问答服务的输入为用户提问,输出是与输入最匹配的Top N(默认为top5)个知识点,知识点按得分从高到低排序。 | To be tested |
| 形象管理 | ExecuteGetCharacters | TODO: | To be tested |
|  | ExecuteGetCharacterInfoById |  | To be tested |
| 素材管理 | ExecuteUploadImage | 上传图片并生成图片链接,图片需小于10m; | To be tested |
|  | ExecuteDeleteimageById |  | To be tested |
|  | ExecuteGetFramsListByImagesId | 获取指定图片可用的播报框列表 | To be tested |
|  | ExecuteUploadPpt | 当前仅支持上传PDF,如有PPT请将PPT转化为PDF再进行上传,文件需小于10m; | To be tested |
|  | ExecutePostCreateImages |  | To be tested |
|  | ExecuteGetImagesList |  | To be tested |
|  | ExecuteUpdateImageName |  | To be tested |
| 视频管理 | ExecuteComposeVideoOndemand |  | To be tested |
|  | ExecuteUpdateVideoById |  | To be tested |
|  | ExecuteCreateVideo |  | To be tested |
|  | ExecuteDeleteVideoById |  | To be tested |
|  | ExecuteGetVideoInfoById |  | To be tested |
|  | ExecuteUpdateVideoInfoById | 通过该接口配置视频 | To be tested |
|  | ExecuteGetVideosList | 该接口用于获取视频列表。 | To be tested |
|  | ExecuteComposeVideo |  | To be tested |
| 问答会话 | CreateSession | 问答会话API由开启会话、处理会话、关闭会话三个接口组成。用户可通过调用该接口创建会话。该接口仅支持老用户,新用户请优先使用问答机器人API接口进行调用。 | To be tested |
|  | DeleteSession | 问答会话API由开启会话、处理会话、关闭会话三个接口组成。用户可通过调用该接口关闭会话。该接口即将下线,请优先使用问答机器人API接口进行调用。 | To be tested |
|  | ExecuteSession | 问答会话API由开启会话、处理会话、关闭会话三个接口组成。用户可通过调用该接口与机器人进行会话。该接口即将下线,请优先使用问答机器人API接口进行调用。 | To be tested |
| 问答机器人 | ExecuteQaChat | 用户调用该接口和机器人进行聊天。 | To be tested |
| 问答统计 | CollectReplyRates | 指定领域获取指定时间范围内的问题答复率,支持按周期统计。 | To be tested |
|  | CollectHotQuestions | 获取完全匹配的热点标准问题列表。 | To be tested |
|  | CollectSessionStats | 获取用户会话统计信息。 | To be tested |
|  | CollectKeyWords | 用户问关键词统计。 | To be tested |
