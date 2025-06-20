# STS MCP Server 

## 版本信息
v0.1.0

## 产品描述

STS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务STS交互的能力。可以基于自然语言对STS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AuthorizationResult | DecodeAuthorizationMessage | 解密鉴权失败的原因。 | To be tested |
| Caller | GetCallerIdentity | 获取调用者(华为云用户,代理等)身份信息。 | To be tested |
