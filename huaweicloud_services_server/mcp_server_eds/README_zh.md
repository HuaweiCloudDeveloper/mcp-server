# EDS MCP Server 

## 版本信息
v0.1.0

## 产品描述

EDS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务EDS交互的能力。可以基于自然语言对EDS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| offer | ListOffers | 查询指定连接器下的offer列表 | To be tested |
|  | ShowOffer | 查询指定offer详情 | To be tested |
| user | AddConnectorUser | 分配子账号 | To be tested |
|  | DeleteConnectorUser | 账号回收 | To be tested |
| 合约 | CommitContract | 提交合约 | To be tested |
|  | CancelContract | 终止合约 | To be tested |
|  | ShowContract | 查询合约 | To be tested |
| 审计日志 | ShowAuditLog | 查询数据资产的审计日志 | To be tested |
| 连接器 | ShowConnector | 查询指定租户的连接器详情 | To be tested |
|  | ListConnectorsByInstanceUser | 按空间用户查询连接器列表 | To be tested |
|  | ListConnectorsByInstanceManger | 按空间管理员查询连接器列表 | To be tested |
