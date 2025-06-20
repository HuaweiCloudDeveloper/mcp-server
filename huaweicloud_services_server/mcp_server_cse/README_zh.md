# CSE MCP Server 

## 版本信息
v0.1.0

## 产品描述

CSE MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CSE交互的能力。可以基于自然语言对CSE资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| gateway | ModifyHttp2Rpc | 修改http转rpc方法。 | To be tested |
|  | ShowPlugins | 查询插件列表。 | To be tested |
|  | ModifyPlugin | 修改插件。 | To be tested |
|  | CreateHttp2Rpc | 创建http转rpc方法。 | To be tested |
|  | DeletePlugin | 删除插件。 | To be tested |
|  | CreatePlugin | 创建插件。 | To be tested |
|  | DeleteHttp2Rpc | 删除http转rpc方法。 | To be tested |
|  | ShowHttp2Rpcs | 查询http转rpc资源列表。 | To be tested |
|  | ShowSinglePlugin | 查询单个插件。 | To be tested |
| nacos | ListNacosNamespaces | 查询nacos命名空间。 | To be tested |
|  | DeleteNacosNamespaces | 删除nacos命名空间。 | To be tested |
|  | UpdateNacosNamespaces | 更新nacos命名空间。 | To be tested |
|  | CreateNacosNamespaces | 创建nacos命名空间。 | To be tested |
| 引擎管理 | ShowEngine | 查询微服务引擎详情 | To be tested |
|  | DeleteEngine | 删除微服务引擎。 | To be tested |
|  | ListFlavors | 查询微服务引擎的规格列表。 | To be tested |
|  | UpgradeEngine | 升级微服务引擎 | To be tested |
|  | RetryEngine | 对微服务引擎进行重试,当前支持ServiceComb专享版引擎 | To be tested |
|  | ShowEngineQuotas | 查询微服务引擎配额。 | To be tested |
|  | ListEngines | 查询微服务引擎列表。 | To be tested |
|  | ResizeEngine | 变更微服务引擎规格。 | To be tested |
|  | UpgradeEngineConfig | 更新微服务引擎配置,更新ServiceComb专享版引擎与注册配置中心引擎的配置 | To be tested |
|  | CreateEngine | 创建微服务引擎,支持创建ServiceComb引擎专享版、注册配置中心、应用网关(公测)。 | To be tested |
|  | ShowEngineJob | 查询微服务引擎任务详情。 | To be tested |
| 治理 | ListGovernancePolicyByPolicyId | 查询治理策略详情。 | To be tested |
|  | CreateGovernancePolicy | 创建治理策略。 | To be tested |
|  | UpdateGovernancePolicy | 修改治理策略。 | To be tested |
|  | CreateMicroserviceRouteRule | 创建灰度发布策略。 | To be tested |
|  | DeleteGovernancePolicy | 删除治理策略。 | To be tested |
|  | DeleteMicroserviceRouteRule | 删除灰度发布策略。 | To be tested |
|  | ListGovernancePolicys | 查询治理策略列表。 | To be tested |
|  | ListGovernancePolicy | 查询指定类型治理策略列表。 | To be tested |
|  | ListMicroserviceRouteRule | 查询微服务的灰度发布规则。 | To be tested |
| 配置管理 | UploadKie | 导入kie配置 | To be tested |
|  | DownloadKie | 导出kie配置 | To be tested |
