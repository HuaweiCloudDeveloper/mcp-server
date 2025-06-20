# IVS MCP Server 

## 版本信息
v0.1.0

## 产品描述

IVS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IVS交互的能力。可以基于自然语言对IVS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 人证核身标准版(三要素) | DetectStandardByNameAndId | 使用姓名、身份证号文本和人脸图片进行三要素身份审核。 | To be tested |
|  | DetectStandardByIdCardImage | 使用身份证正反面图片提取姓名和身份证号码,与人脸图片进行三要素身份审核。 | To be tested |
|  | DetectStandardByVideoAndIdCardImage | 从身份证正反面图片中提取姓名和身份证号码,并对视频做活体检测后提取人脸图片,以此进行三要素身份审核。 | To be tested |
|  | DetectStandardByVideoAndNameAndId | 使用姓名、身份证号文本,并对视频做活体检测后提取人脸图片,以此进行三要素身份审核。 | To be tested |
| 人证核身证件版(二要素) | DetectExtentionByNameAndId | 使用姓名、身份证号码二要素进行身份审核。身份验证时,传入的数据为身份证信息。提取身份证信息时,可以使用身份证正反面图片,也可以直接输入姓名、身份证号文本。 | To be tested |
|  | DetectExtentionByIdCardImage | 使用姓名、身份证号码二要素进行身份审核。身份验证时,传入的数据为身份证信息。提取身份证信息时,可以使用身份证正反面图片,也可以直接输入姓名、身份证号文本。 | To be tested |
