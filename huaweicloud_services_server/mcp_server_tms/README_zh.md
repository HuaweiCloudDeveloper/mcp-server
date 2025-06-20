# TMS MCP Server 

## 版本信息
v0.1.0

## 产品描述

TMS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务TMS交互的能力。可以基于自然语言对TMS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 查询标签管理支持的服务 | ListProviders | 查询标签管理支持的服务。 | To be tested |
| 查询版本操作 | ShowApiVersion | 查询指定的标签管理服务API版本号详情。 | To be tested |
|  | ListApiVersions | 查询标签管理服务的API版本列表。 | To be tested |
| 资源标签 | DeleteResourceTag | 用于批量移除云服务多个资源的标签,每个资源最多支持移除10个标签,每次最多支持批量操作20个资源。 | To be tested |
|  | ListResource | 根据标签过滤资源。 | To be tested |
|  | ShowResourceTag | 查询单个资源上的标签。 | To be tested |
|  | ListTagValues | 查询指定区域的标签键下的所有标签值。 | To be tested |
|  | ListTagKeys | 查询指定区域的所有标签键. | To be tested |
|  | CreateResourceTag | 用于给云服务的多个资源添加标签,每个资源最多可添加10个标签,每次最多支持批量操作20个资源。 | To be tested |
| 配额 | ShowTagQuota | 查询标签的配额信息。 | To be tested |
| 预定义标签操作 | CreatePredefineTags | 用于创建预定标签。用户创建预定义标签后,可以使用预定义标签来给资源创建标签。该接口支持幂等特性和处理批量数据。 | To be tested |
|  | DeletePredefineTags | 用于删除预定标签。 | To be tested |
|  | UpdatePredefineTags | 修改预定义标签。 | To be tested |
|  | ListPredefineTags | 用于查询预定义标签列表。 | To be tested |
