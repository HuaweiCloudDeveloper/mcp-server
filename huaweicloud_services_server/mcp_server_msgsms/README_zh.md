# MSGSMS MCP Server 

## 版本信息
v0.1.0

## 产品描述

MSGSMS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务MSGSMS交互的能力。可以基于自然语言对MSGSMS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AppManagement | ListAppDetails | 该接口用于用户查询已创建的应用信息。 | To be tested |
|  | CreateApp | 该接口用于用户创建应用信息。 | To be tested |
|  | ShowApp | 该接口用于用户查询应用详情信息。 | To be tested |
|  | ShowAppCount | 该接口用于用户查询应用使用的数量信息。 | To be tested |
|  | UpdateApp | 该接口用于用户修改应用信息。 | To be tested |
| SignatureManagement | ShowSignature | 该接口用于用户查询签名详情信息。 | To be tested |
|  | ShowSignatureFile | 该接口用于用户查询上传的文件信息。 | To be tested |
|  | UpdateSignature | 该接口用于用户更新签名信息,目前仅支持审核不通过的短信签名重新修改。 | To be tested |
|  | UploadSignatureFile | 该接口用于用户上传文件信息。 | To be tested |
|  | DeleteSignature | 该接口用于用户删除已创建的签名信息息。 | To be tested |
|  | EnableSignature | 该接口用于用户申请激活签名信息。 | To be tested |
|  | CreateSignature | 该接口用于用户创建签名。 | To be tested |
|  | ListSignatureDetails | 该接口用于用户查询已创建的短信签名信息。 | To be tested |
| TemplateManagement | UpdateTemplate | 该接口用于用户修改模板信息,目前仅支持审核不通过的短信模板重新修改 | To be tested |
|  | DeleteTemplate | 该接口用于用户删除已创建的模板信息。 | To be tested |
|  | ListSendCountryDetails | 该接口用于用户查询短信发送的国家信息 | To be tested |
|  | ShowTemplate | 该接口用于用户查询已创建的模板详情。 | To be tested |
|  | ListTemplateDetails | 该接口用于用户查询已创建的模板信息。 | To be tested |
|  | ListTemplateVarilableDetails | 该接口用于用户查询模板参数。 | To be tested |
|  | CreateTemplate | 该接口用于用户创建模板。 | To be tested |
