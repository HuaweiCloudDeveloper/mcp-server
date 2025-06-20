# SMNGLOBAL MCP Server 

## 版本信息
v0.1.0

## 产品描述

SMNGLOBAL MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务SMNGLOBAL交互的能力。可以基于自然语言对SMNGLOBAL资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 订阅用户 | UpdateSubscriptionUser | 更新订阅用户。 | To be tested |
|  | CreateSubscriptionUser | 添加订阅用户。如果订阅用户的状态为未确认,则会向订阅用户发送一条确认订阅消息。订阅用户点击订阅链接确认订阅后,则订阅用户的状态变更为已确认,同时会向订阅用户发送一条取消订阅消息,便于订阅用户随时可以取消订阅。订阅用户点击取消订阅链接后,则订阅用户的状态变更为已取消,同时会向订阅用户发送一条重新订阅消息,便于订阅用户可以重新订阅。 | To be tested |
|  | ListSubscriptionUser | 查询订阅用户列表。 | To be tested |
|  | DeleteSubscriptionUser | 删除订阅用户。 | To be tested |
