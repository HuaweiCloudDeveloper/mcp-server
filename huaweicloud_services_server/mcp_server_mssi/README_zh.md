# MSSI MCP Server 

## 版本信息
v0.1.0

## 产品描述

MSSI MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务MSSI交互的能力。可以基于自然语言对MSSI资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 流 | ShowAllFlows | 查询所有Flow | To be tested |
|  | SearchFlowById | 查询特定flow | To be tested |
|  | CreateFlow | 创建flow | To be tested |
|  | DeleteFlow | 删除Flow | To be tested |
|  | UpdateFlow | 更新flow | To be tested |
| 流模板 | CreateFlowTemplateFromFlow |  | To be tested |
| 连接 | UpdateConnectionInfo |  | To be tested |
|  | ShowSingleConnection | 查询单个连接 | To be tested |
|  | ShowAllConnections | 查询所有连接 | To be tested |
|  | CreateConnectionInfo | 新建连接 | To be tested |
|  | DeleteConnectionInfo | 删除Connection | To be tested |
| 连接器 | DeleteCustomConnector | 删除自定义连接器 | To be tested |
|  | ShowCustomConnectors | 查询CustomConnector列表 | To be tested |
|  | ShowCustomConnector | 发布连接器 | To be tested |
|  | ShowConnectors | 查询Connector列表 | To be tested |
|  | CreateCustomConnectorFromOpenapi | 新建自定义连接器(导入swagger方式) | To be tested |
