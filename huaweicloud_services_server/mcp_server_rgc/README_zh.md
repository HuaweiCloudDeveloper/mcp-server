# RGC MCP Server 

## 版本信息
v0.1.0

## 产品描述

RGC MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务RGC交互的能力。可以基于自然语言对RGC资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Governance | DisableControl | 关闭组织下的某个单元的某个控制策略。 | To be tested |
|  | ListControlsForOrganizationalUnit | 列出组织里某个注册OU开启的所有控制策略信息。 | To be tested |
|  | ShowControlOperate | 根据操作ID查询返回指定ID的操作状态。 | To be tested |
|  | EnableControl | 给组织下的某个单元开启某个控制策略。 | To be tested |
|  | ListEnabledControls | 列出组织里开启的所有控制策略信息。 | To be tested |
| ManagedOrganization | RegisterOrganizationalUnit | 将组织里的某个OU注册到RGC服务。 | To be tested |
|  | ShowOperation | 查询在RGC服务里注册/取消注册的过程信息。 | To be tested |
|  | ShowManagedAccount | 查询组织里某个纳管账号信息。 | To be tested |
|  | CreateAccount | 在组织里的某个注册OU下创建账号。 | To be tested |
