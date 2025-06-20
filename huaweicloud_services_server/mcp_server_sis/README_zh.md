# SIS MCP Server 

## 版本信息
v0.1.0

## 产品描述

SIS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务SIS交互的能力。可以基于自然语言对SIS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 热词管理接口 | DeleteVocabulary | 通过热词表id删除热词表。 | To be tested |
|  | UpdateVocabulary | 更新一个热词表,更新成功返回id。 | To be tested |
|  | ShowVocabulary | 通过热词表id查询热词表的信息和内容。 | To be tested |
|  | CreateVocabulary | 新建一个热词表,创建成功返回id。每个用户限制创建10个热词表。 | To be tested |
|  | ShowVocabularies | 查询用户所有热词表列表。 | To be tested |
| 语音合成接口 | RunTts | 语音合成,是一种将文本转换成逼真语音的服务。用户通过实时访问和调用API获取语音合成结果,将用户输入的文字合成为音频。通过音色选择、自定义音量、语速,为企业和个人提供个性化的发音服务 | To be tested |
| 语音识别接口 | RecognizeShortAudio | 一句话识别接口,用于短语音的同步识别。一次性上传整个音频,响应中即返回识别结果。 | To be tested |
|  | CollectTranscriberJob | 该接口用于获取录音文件识别结果及识别状态。 | To be tested |
|  | PushTranscriberJobs | **录音文件识别** | To be tested |
|  | RecognizeFlashAsr | 极速版ASR(Restful API 接口, 适用于音频(文件大小<=100M,语音时长<=30分钟)文件的同步识别。 | To be tested |
