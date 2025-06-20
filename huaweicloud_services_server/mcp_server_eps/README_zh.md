# EPS MCP Server 

## 版本信息
v0.1.0

## 产品描述

EPS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务EPS交互的能力。可以基于自然语言对EPS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 企业项目管理操作 | ShowEnterpriseProjectQuota | 查询企业项目的配额信息。 | To be tested |
|  | EnableEnterpriseProject | 启用企业项目。 | To be tested |
|  | ShowEnterpriseProject | 查询企业项目详情。 | To be tested |
|  | UpdateEnterpriseProject | 修改企业项目。当前仅支持修改名称和描述。 | To be tested |
|  | MigrateResource | 迁移资源到目标企业项目。 | To be tested |
|  | CreateEnterpriseProject | 创建企业项目。 | To be tested |
|  | DisableEnterpriseProject | 停用企业项目。 | To be tested |
|  | ShowResourceBindEnterpriseProject | 查询企业项目下绑定的资源详情。 | To be tested |
|  | ListEnterpriseProject | 查询当前用户已授权的企业项目列表,用户可以使用企业项目绑定资源。 | To be tested |
| 查询企业项目支持的服务 | ListProviders | 查询企业项目支持的服务 | To be tested |
| 查询版本操作 | ShowApiVersion | 查询指定的企业项目API版本号详情 | To be tested |
|  | ListApiVersions | 查询企业项目的API版本列表。 | To be tested |
