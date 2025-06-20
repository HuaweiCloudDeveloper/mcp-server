# VPCEP MCP Server 

## 版本信息
v0.1.0

## 产品描述

VPCEP MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务VPCEP交互的能力。可以基于自然语言对VPCEP资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| TAG功能 | BatchAddOrRemoveResourceInstance | 为指定Endpoint Service或Endpoint批量添加或删除标签。 | To be tested |
|  | ListQueryProjectResourceTags | 根据租户ID和资源类型,获取租户下资源的标签。 | To be tested |
|  | ListResourceInstances | 使用标签过滤查询租户下资源的实例。 | To be tested |
| 版本管理 | ListVersionDetails | 查询VPC终端节点接口版本列表。 | To be tested |
|  | ListSpecifiedVersionDetails | 查询指定VPC终端节点接口版本信息。 | To be tested |
| 终端节点功能 | UpdateEndpointPolicy | 修改终端节点策略。 | To be tested |
|  | DeleteEndpoint | 删除终端节点。 | To be tested |
|  | DeleteEndpointPolicy | 删除网关型终端节点策略,该接口待下线,不建议使用。 | To be tested |
|  | UpdateEndpointWhite | 更新或删除允许访问终端节点的白名单。 | To be tested |
|  | UpdateEndpointRoutetable | 修改终端节点的路由表。 | To be tested |
|  | ListEndpointInfoDetails | 查询终端节点的详细信息。 | To be tested |
|  | ListEndpoints | 查询当前用户下的终端节点的列表。 | To be tested |
|  | CreateEndpoint | 创建终端节点,以便访问终端节点服务。 | To be tested |
| 终端节点服务功能 | DeleteEndpointService | 删除终端节点服务。 | To be tested |
|  | ListServiceConnections | 查询连接当前用户下的某一个终端节点服务的连接列表。marker_id是连接的唯一标识。 | To be tested |
|  | UpgradeEndpointService | 升级终端节点服务,使终端节点服务支持创建专业型终端节点实例 | To be tested |
|  | AddOrRemoveServicePermissions | 批量添加或移除当前用户下终端节点服务的白名单。 | To be tested |
|  | ListServicePublicDetails | 查询公共终端节点服务的列表,公共终端节点服务是所有用户可见且可连接的终端节点服务, | To be tested |
|  | BatchRemoveEndpointServicePermissions | 批量删除当前用户下终端节点服务的白名单 | To be tested |
|  | UpdateEndpointService | 修改终端节点服务。 | To be tested |
|  | CreateEndpointService | 创建终端节点服务,允许其他用户创建终端节点连接您创建的终端节点服务, | To be tested |
|  | ListServicePermissionsDetails | 查询当前用户下终端节点服务的白名单列表。 | To be tested |
|  | BatchAddEndpointServicePermissions | 批量添加当前用户下终端节点服务的白名单,支持添加描述信息。 | To be tested |
|  | ListEndpointService | 查询当前用户下的终端节点服务的列表。 | To be tested |
|  | UpdateEndpointServicePermissionDesc | 更新当前用户下终端节点服务白名单的描述信息 | To be tested |
|  | ListServiceDescribeDetails | 查询终端节点服务的概要信息, 此接口是供创建终端节点的用户来查询需要连接的终端节点服务信息。 此接口既可以方便其他用户查询到您的终端节点服务概要信息, 又可以避免您的终端节点服务的细节信息暴露给其他用户。 | To be tested |
|  | UpdateEndpointConnectionsDesc | 更新终端节点服务连接的终端节点的描述。 | To be tested |
|  | AcceptOrRejectEndpoint | 接受或者拒绝终端节点连接到当前的终端节点服务。 | To be tested |
|  | ListServiceDetails | 查询终端节点服务的详细信息。 | To be tested |
|  | UpdateEndpointServiceName | 修改终端节点服务名称 | To be tested |
| 资源配额功能 | ListQuotaDetails | 查询用户的资源配额,包括终端节点服务和终端节点。 | To be tested |
