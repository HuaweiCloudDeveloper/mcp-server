# NAT MCP Server 

## 版本信息
v0.1.0

## 产品描述

NAT MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务NAT交互的能力。可以基于自然语言对NAT资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 中转IP标签管理 | CreateTransitIpTag | - 一个中转IP上最多有10个标签。 | To be tested |
|  | ListTransitIpsByTags | - 使用标签过滤中转IP实例。 | To be tested |
|  | ShowTransitIpTags | - 查询指定中转IP实例的标签信息。 | To be tested |
|  | DeleteTransitIpTag | - 幂等接口: | To be tested |
|  | BatchCreateDeleteTransitIpTags | - 为指定中转IP实例批量添加或删除标签 | To be tested |
|  | ListTransitIpTags | - 查询租户在指定Project和实例类型的所有中转IP标签集合。 | To be tested |
| 公网DNAT规则 | BatchCreateNatGatewayDnatRules | 批量创建DNAT规则。 | To be tested |
|  | UpdateNatGatewayDnatRule | 更新指定的DNAT规则。 | To be tested |
|  | ListNatGatewayDnatRules | 查询DNAT规则列表。 | To be tested |
|  | ShowNatGatewayDnatRule | 查询指定的DNAT规则详情。 | To be tested |
|  | CreateNatGatewayDnatRule | 创建DNAT规则。 | To be tested |
|  | DeleteNatGatewayDnatRule | 删除指定的DNAT规则。 | To be tested |
| 公网NAT网关 | ShowNatGateway | 查询指定的公网NAT网关实例详情。 | To be tested |
|  | UpdateNatGateway | 更新公网NAT网关实例。 | To be tested |
|  | CreateNatGateway | 创建公网NAT网关实例。 | To be tested |
|  | DeleteNatGateway | 删除公网NAT网关实例。 | To be tested |
|  | ListNatGateways | 查询公网NAT网关实例列表。 | To be tested |
| 公网NAT网关标签 | ListNatGatewayByTag | - 使用标签过滤公网NAT网关资源实例。 | To be tested |
|  | BatchCreateDeleteNatGatewayTag | - 为指定公网NAT网关实例批量添加或删除标签。  | To be tested |
|  | CreateNatGatewayTag | - 添加公网NAT网关资源标签。一个资源上最多有10个标签。 | To be tested |
|  | ListNatGatewayTag | - 查询租户在指定项目和公网NAT网关实例类型的所有标签集合。 | To be tested |
|  | DeleteNatGatewayTag | - 删除指定公网NAT网关资源实例的标签信息。 | To be tested |
|  | ShowNatGatewayTag | - 查询指定公网NAT网关实例的标签信息。 | To be tested |
| 公网SNAT规则 | DeleteNatGatewaySnatRule | 删除指定的SNAT规则。 | To be tested |
|  | UpdateNatGatewaySnatRule | 更新指定的SNAT规则。 | To be tested |
|  | CreateNatGatewaySnatRule | 创建SNAT规则。 | To be tested |
|  | ListNatGatewaySnatRules | 查询SNAT规则列表。 | To be tested |
|  | ShowNatGatewaySnatRule | 查询指定的SNAT规则详情。 | To be tested |
| 私网DNAT规则 | DeletePrivateDnat | 删除指定的DNAT规则。 | To be tested |
|  | ListPrivateDnats | 查询DNAT规则列表。 | To be tested |
|  | CreatePrivateDnat | 创建DNAT规则。 | To be tested |
|  | UpdatePrivateDnat | 更新指定的DNAT规则。 | To be tested |
|  | ShowPrivateDnat | 查询指定的DNAT规则详情。 | To be tested |
| 私网NAT中转IP | CreateTransitIp | 创建中转IP。 | To be tested |
|  | DeleteTransitIp | 删除中转IP。 | To be tested |
|  | ListTransitIps | 查询中转IP列表。 | To be tested |
|  | ShowTransitIp | 查询中转IP详情。 | To be tested |
| 私网NAT网关 | CreatePrivateNat | 创建私网NAT网关实例。 | To be tested |
|  | DeletePrivateNat | 删除私网NAT网关实例。 | To be tested |
|  | UpdatePrivateNat | 更新私网NAT网关实例。 | To be tested |
|  | ShowPrivateNat | 查询指定的私网NAT网关实例详情。 | To be tested |
|  | ListPrivateNats | 查询私网NAT网关实例列表。 | To be tested |
| 私网NAT网关标签管理 | CreatePrivateNatTag | - 一个私网NAT网关上最多有10个标签。 | To be tested |
|  | DeletePrivateNatTag | - 幂等接口: | To be tested |
|  | ShowPrivateNatTags | - 查询指定私网NAT网关实例的标签信息。 | To be tested |
|  | ListPrivateNatTags | - 查询租户在指定Project和实例类型的所有私网NAT网关标签集合。 | To be tested |
|  | ListPrivateNatsByTags | - 使用标签过滤私网NAT网关实例。 | To be tested |
|  | BatchCreateDeletePrivateNatTags | - 为指定私网NAT网关实例批量添加或删除标签 | To be tested |
| 私网SNAT规则 | CreatePrivateSnat | 创建SNAT规则。 | To be tested |
|  | ListPrivateSnats | 查询SNAT规则列表。 | To be tested |
|  | DeletePrivateSnat | 删除指定的SNAT规则。 | To be tested |
|  | UpdatePrivateSnat | 更新指定的SNAT规则。 | To be tested |
|  | ShowPrivateSnat | 查询指定的SNAT规则详情。 | To be tested |
