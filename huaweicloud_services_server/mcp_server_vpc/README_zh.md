# VPC MCP Server 

## 版本信息
v0.1.0

## 产品描述

VPC MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务VPC交互的能力。可以基于自然语言对VPC资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| IP地址组 | ShowAddressGroup | 查询地址组详情。 | To be tested |
|  | CreateAddressGroup | 创建地址组 | To be tested |
|  | ListAddressGroup | 查询地址组列表,根据过滤条件进行过滤。 | To be tested |
|  | DeleteIpAddressGroupForce | 强制删除地址组,删除的地址组与安全组规则关联时,会删除地址组与关联的安全组规则。 | To be tested |
|  | DeleteAddressGroup | 删除地址组,非强制删除,删除前请确保未被其他资源引用 | To be tested |
|  | UpdateAddressGroup | 更新地址组。 | To be tested |
| OpenStack - API版本信息 | ListApiVersion | 返回当前API所有可用的版本(仅针对OpenStack原生接口)。 | To be tested |
| OpenStack - 子网 | NeutronShowSubnet | 查询子网详情 | To be tested |
|  | NeutronCreateSubnet | 创建子网。 | To be tested |
|  | NeutronUpdateSubnet | 更新子网 | To be tested |
|  | NeutronListSubnets | 查询提交请求租户的所有子网,单次查询最多返回2000条数据,超过2000后会返回分页标记。分页查询请参考分页查询 。 | To be tested |
|  | NeutronDeleteSubnet | 删除子网 | To be tested |
| OpenStack - 安全组 | NeutronCreateSecurityGroupRule | 创建安全组规则 | To be tested |
|  | NeutronShowSecurityGroup | 查询安全组详情 | To be tested |
|  | NeutronCreateSecurityGroup | 创建安全组 | To be tested |
|  | NeutronShowSecurityGroupRule | 查询安全组规则详情。 | To be tested |
|  | NeutronListSecurityGroupRules | 查询提交请求的租户有权限查看的所有安全组规则。单次查询最多返回2000条数据,超过2000后会返回分页标记。分页查询请参考分页查询 | To be tested |
|  | NeutronUpdateSecurityGroup | 更新安全组 | To be tested |
|  | NeutronListSecurityGroups | 查询提交请求租户的所有安全组,单次查询最多返回2000条数据,超过2000后会返回分页标记。分页查询请参考分页查询 。 | To be tested |
|  | NeutronDeleteSecurityGroup | 删除安全组 | To be tested |
|  | NeutronDeleteSecurityGroupRule | 删除安全组规则 | To be tested |
| OpenStack - 端口 | NeutronDeletePort | 删除端口。 | To be tested |
|  | NeutronUpdatePort | 更新端口 | To be tested |
|  | NeutronShowPort | 查询端口详情。 | To be tested |
|  | NeutronListPorts | 查询提交请求的租户的所有端口,单次查询最多返回2000条数据,超过2000后会返回分页标记。分页查询请参考分页查询。 | To be tested |
|  | NeutronCreatePort | 创建端口。 | To be tested |
| OpenStack - 网络 | NeutronShowNetwork | 查询指定的网络详情 | To be tested |
|  | NeutronDeleteNetwork | 删除网络 | To be tested |
|  | NeutronCreateNetwork | 创建网络 | To be tested |
|  | NeutronListNetworks | 查询提交请求的租户的所有网络,单次查询最多返回2000条数据,超过2000后会返回分页标记。分页查询请参考分页查询。 | To be tested |
|  | NeutronUpdateNetwork | 更新网络 | To be tested |
| OpenStack - 网络ACL | NeutronListFirewallRules | 查询提交请求的租户有权限操作的所有网络ACL规则信息。单次查询最多返回2000条数据,超过2000后会返回分页标记。 | To be tested |
|  | NeutronShowFirewallPolicy | 查询特定网络ACL策略详情。 | To be tested |
|  | NeutronDeleteFirewallPolicy | 删除网络ACL策略。 | To be tested |
|  | NeutronUpdateFirewallGroup | 更新网络ACL组。 | To be tested |
|  | NeutronDeleteFirewallRule | 删除网络ACL规则。 | To be tested |
|  | NeutronShowFirewallGroup | 查询特定网络ACL组详情。 | To be tested |
|  | NeutronCreateFirewallGroup | 创建网络ACL组 | To be tested |
|  | NeutronRemoveFirewallRule | 从某一网络ACL策略中移除一条网络ACL规则。 | To be tested |
|  | NeutronAddFirewallRule | 插入一条网络ACL规则到某一网络ACL策略中。 | To be tested |
|  | NeutronUpdateFirewallPolicy | 更新网络ACL策略。 | To be tested |
|  | NeutronListFirewallGroups | 查询提交请求的租户有权限操作的所有网络ACL组信息。单次查询最多返回2000条数据,超过2000后会返回分页标记。 | To be tested |
|  | NeutronCreateFirewallRule | 创建网络ACL规则。 | To be tested |
|  | NeutronCreateFirewallPolicy | 创建网络ACL策略。 | To be tested |
|  | NeutronListFirewallPolicies | 查询提交请求的租户有权限操作的所有网络ACL策略信息。单次查询最多返回2000条数据,超过2000后会返回分页标记。 | To be tested |
|  | NeutronUpdateFirewallRule | 更新网络ACL规则。 | To be tested |
|  | NeutronDeleteFirewallGroup | 删除网络ACL组 | To be tested |
|  | NeutronShowFirewallRule | 查询特定网络ACL规则。 | To be tested |
| OpenStack - 路由器 | NeutronRemoveRouterInterface | 删除路由器接口。 | To be tested |
|  | NeutronCreateRouter | 创建路由器。 | To be tested |
|  | NeutronShowRouter | 查询路由器详情。 | To be tested |
|  | NeutronUpdateRouter | 更新路由器。 | To be tested |
|  | NeutronListRouters | 查询提交请求的租户有权限操作的所有路由器信息,单次查询最多返回2000条数据,超过2000后会返回分页标记。 | To be tested |
|  | NeutronAddRouterInterface | 添加路由器接口。 | To be tested |
|  | NeutronDeleteRouter | 删除路由器 | To be tested |
| VPC | DeleteVpc | 删除虚拟私有云。 | To be tested |
|  | UpdateVpc | 更新虚拟私有云。 | To be tested |
|  | CreateVpc | 创建虚拟私有云。 | To be tested |
|  | ListVpcs | 查询vpc列表 | To be tested |
|  | ShowVpc | 查询vpc详情 | To be tested |
|  | AddVpcExtendCidr | 添加VPC的扩展网段 | To be tested |
|  | RemoveVpcExtendCidr | 移除VPC扩展网段 | To be tested |
| VPC资源标签管理 | BatchDeleteVpcTags | 为指定的VPC资源实例批量删除标签。 | To be tested |
|  | ListVpcsByTags | 使用标签过滤实例。 | To be tested |
|  | ListVpcTags | 查询租户在指定区域和实例类型的所有标签集合 | To be tested |
|  | BatchCreateVpcTags | 为指定的VPC资源实例批量添加标签。 | To be tested |
|  | CreateVpcResourceTag | 给指定VPC资源实例增加标签信息 | To be tested |
|  | DeleteVpcTag | 删除指定VPC资源实例的标签信息 | To be tested |
|  | ShowVpcTags | 查询指定VPC实例的标签信息 | To be tested |
| VPC路由 | DeleteVpcRoute | 删除路由 | To be tested |
|  | ShowVpcRoute | 查询路由详情 | To be tested |
|  | ListVpcRoutes | 查询提交请求的租户的所有路由列表,并根据过滤条件进行过滤。 | To be tested |
|  | CreateVpcRoute | 创建路由 | To be tested |
| 子网 | ShowSubnet | 查询子网详情。 | To be tested |
|  | UpdateSubnet | 更新子网。 | To be tested |
|  | CreateSubnet | 创建子网。 | To be tested |
|  | DeleteSubnet | 删除子网 | To be tested |
|  | ListSubnets | 查询子网列表 | To be tested |
| 子网资源标签管理 | BatchDeleteSubnetTags | 为指定的子网资源实例批量删除标签 | To be tested |
|  | ShowSubnetTags | 查询指定子网实例的标签信息。 | To be tested |
|  | ListSubnetTags | 查询租户在指定区域和实例类型的所有标签集合 | To be tested |
|  | ListSubnetsByTags | 使用标签过滤实例 | To be tested |
|  | DeleteSubnetTag | 删除指定子网资源实例的标签信息。 | To be tested |
|  | BatchCreateSubnetTags | 为指定的子网资源实例批量添加标签。 | To be tested |
|  | CreateSubnetTag | 给指定子网资源实例增加标签信息。 | To be tested |
| 安全组 | ListSecurityGroups | 查询某租户下的安全组列表 | To be tested |
|  | CreateSecurityGroup | 创建安全组 | To be tested |
|  | DeleteSecurityGroup | 删除安全组 | To be tested |
|  | ShowSecurityGroup | 查询单个安全组详情 | To be tested |
|  | UpdateSecurityGroup | 更新安全组 | To be tested |
| 安全组规则 | ListSecurityGroupRules | 查询安全组规则列表 | To be tested |
|  | DeleteSecurityGroupRule | 删除安全组规则 | To be tested |
|  | ShowSecurityGroupRule | 查询单个安全组规则 | To be tested |
|  | BatchCreateSecurityGroupRules | 在特定安全组下批量创建安全组规则 | To be tested |
|  | CreateSecurityGroupRule | 创建安全组规则 | To be tested |
| 安全组资源标签管理 | ListSecurityGroupTags | 查询租户在指定区域和实例类型的所有标签集合 | To be tested |
|  | DeleteSecurityGroupTag | 删除指定安全组资源实例的标签信息。 | To be tested |
|  | BatchCreateSecurityGroupTags | 为指定的安全组资源实例批量添加标签。 | To be tested |
|  | CreateSecurityGroupTag | 给指定安全组资源实例增加标签信息。 | To be tested |
|  | ShowSecurityGroupTags | 查询指定安全组实例的标签信息。 | To be tested |
|  | ListSecurityGroupsByTags | 使用标签过滤实例 | To be tested |
|  | BatchDeleteSecurityGroupTags | 为指定的安全组资源实例批量删除标签 | To be tested |
| 对等连接 | ShowVpcPeering | 查询对等连接详情。 | To be tested |
|  | DeleteVpcPeering | 删除对等连接。 | To be tested |
|  | AcceptVpcPeering | 租户A名下的VPC申请和租户B的VPC建立对等连接,需要等待租户B接受该请求。此接口用于租户接受其他租户发起的对等连接请求。 | To be tested |
|  | ListVpcPeerings | 查询提交请求的租户的所有对等连接。根据过滤条件进行过滤。 | To be tested |
|  | CreateVpcPeering | 创建对等连接。 | To be tested |
|  | UpdateVpcPeering | 更新对等连接。 | To be tested |
|  | RejectVpcPeering | 租户A名下的VPC申请和租户B的VPC建立对等连接,需要等待租户B接受该请求。此接口用于租户拒绝其他租户发起的对等连接请求。 | To be tested |
| 查询网络IP使用情况 | ShowNetworkIpAvailabilities | 显示一个指定网络中的IPv4地址使用情况。 | To be tested |
| 流日志 | UpdateFlowLog | 更新流日志 | To be tested |
|  | CreateFlowLog | 创建流日志。 | To be tested |
|  | ShowFlowLog | 查询流日志详情 | To be tested |
|  | ListFlowLogs | 查询提交请求的租户的所有流日志列表,并根据过滤条件进行过滤 | To be tested |
|  | DeleteFlowLog | 删除流日志 | To be tested |
| 流量镜像会话 | AddSourcesToTrafficMirrorSession | 流量镜像会话添加镜像源 | To be tested |
|  | CreateTrafficMirrorSession | 创建流量镜像会话 | To be tested |
|  | ShowTrafficMirrorSession | 查询流量镜像会话详情 | To be tested |
|  | UpdateTrafficMirrorSession | 更新流量镜像会话 | To be tested |
|  | DeleteTrafficMirrorSession | 删除流量镜像会话 | To be tested |
|  | RemoveSourcesFromTrafficMirrorSession | 流量镜像会话移除镜像源 | To be tested |
|  | ListTrafficMirrorSessions | 查询流量镜像会话列表 | To be tested |
| 流量镜像筛选条件 | ListTrafficMirrorFilters | 查询流量镜像筛选条件列表 | To be tested |
|  | UpdateTrafficMirrorFilter | 更新流量镜像筛选条件 | To be tested |
|  | CreateTrafficMirrorFilter | 创建流量镜像筛选条件 | To be tested |
|  | ShowTrafficMirrorFilter | 查询流量镜像筛选条件详情 | To be tested |
|  | DeleteTrafficMirrorFilter | 删除流量镜像筛选条件 | To be tested |
| 流量镜像筛选规则 | UpdateTrafficMirrorFilterRule | 更新流量镜像筛选规则 | To be tested |
|  | ShowTrafficMirrorFilterRule | 查询流量镜像筛选规则详情 | To be tested |
|  | CreateTrafficMirrorFilterRule | 创建流量镜像筛选规则 | To be tested |
|  | DeleteTrafficMirrorFilterRule | 删除流量镜像筛选规则 | To be tested |
|  | ListTrafficMirrorFilterRules | 查询流量镜像筛选规则列表 | To be tested |
| 私有IP | DeletePrivateip | 删除私有IP。 | To be tested |
|  | CreatePrivateip | 申请私有IP。 | To be tested |
|  | ListPrivateips | 查询指定子网下的私有IP列表。 | To be tested |
|  | ShowPrivateip | 指定ID查询私有IP。 | To be tested |
| 端口 | UpdatePort | 更新端口。 | To be tested |
|  | CreatePort | 创建端口。 | To be tested |
|  | ShowPort | 查询单个端口详情。 | To be tested |
|  | AddSecurityGroups | 端口插入安全组 | To be tested |
|  | DeletePort | 删除端口。 | To be tested |
|  | RemoveSecurityGroups | 端口移除安全组 | To be tested |
|  | ListPorts | 查询提交请求的租户的所有端口,单次查询最多返回2000条数据。 | To be tested |
| 端口资源标签管理 | CountPortsByTags | 使用标签过滤查询端口实例数量。 | To be tested |
|  | BatchCreatePortTags | 为指定的端口批量添加标签。 | To be tested |
|  | ListPortsByTags | 使用标签过滤查询端口。 | To be tested |
|  | DeletePortTag | 删除指定端口的标签信息 | To be tested |
|  | CreatePortTag | 给指定端口资源实例增加标签信息 | To be tested |
|  | ListPortTags | 查询租户在指定Project中实例类型的所有资源标签集合。 | To be tested |
|  | BatchDeletePortTags | 为指定的端口资源实例批量删除标签。 | To be tested |
|  | ShowPortTags | 查询指定端口的标签信息。 | To be tested |
| 网络ACL | ShowFirewall | 查询网络ACL详情 | To be tested |
|  | DeleteFirewall | 删除网络ACL | To be tested |
|  | UpdateFirewallRules | 网络ACL更新规则 | To be tested |
|  | AssociateSubnetFirewall | 网络ACL绑定子网 | To be tested |
|  | CreateFirewall | 创建网络ACL | To be tested |
|  | AddFirewallRules | 网络ACL插入规则 | To be tested |
|  | UpdateFirewall | 更新网络ACL | To be tested |
|  | DisassociateSubnetFirewall | 网络ACL解绑子网 | To be tested |
|  | RemoveFirewallRules | 网络ACL移除规则 | To be tested |
|  | ListFirewall | 查询网络ACL列表 | To be tested |
| 网络ACL资源标签管理 | BatchCreateFirewallTags | 为指定的网络ACL资源实例批量添加标签。 | To be tested |
|  | DeleteFirewallTag | 删除指定IP地址组资源实例的标签信息 | To be tested |
|  | CreateFirewallTag | 给指定IP地址组资源实例增加标签信息 | To be tested |
|  | ListFirewallTags | 查询租户在指定Project中实例类型的所有资源标签集合 | To be tested |
|  | CountFirewallsByTags | 使用标签过滤查询ACL实例数量。 | To be tested |
|  | ShowFirewallTags | 查询指定ACL实例的标签信息 | To be tested |
|  | ListFirewallsByTags | 使用标签过滤查询ACL实例。 | To be tested |
|  | BatchDeleteFirewallTags | 为指定的网络ACL资源实例批量删除标签。 | To be tested |
| 路由表 | ShowRouteTable | 查询路由表详情 | To be tested |
|  | UpdateRouteTable | 更新路由表,包括可以更新路由表的名称,描述,以及新增、更新、删除路由条目 | To be tested |
|  | ListRouteTables | 查询提交请求的帐户的所有路由表列表,并根据过滤条件进行过滤 | To be tested |
|  | AssociateRouteTable | 路由表关联子网。子网关联路由表A后,再关联B,不需要先跟路由表A解关联再关联路由表B | To be tested |
|  | CreateRouteTable | 创建路由表 | To be tested |
|  | DisassociateRouteTable | 子网解关联路由表 | To be tested |
|  | DeleteRouteTable | 删除路由表 | To be tested |
| 辅助弹性网卡 | DeleteSubNetworkInterface | 删除辅助弹性网卡 | To be tested |
|  | ListSubNetworkInterfaces | 查询辅助弹性网卡列表,单次查询最多返回2000条数据 | To be tested |
|  | CreateSubNetworkInterface | 创建辅助弹性网卡 | To be tested |
|  | ShowSubNetworkInterfacesQuantity | 查询辅助弹性网卡数目 | To be tested |
|  | BatchCreateSubNetworkInterface | 批量创建辅助弹性网卡 | To be tested |
|  | ShowSubNetworkInterface | 查询辅助弹性网卡详情 | To be tested |
|  | UpdateSubNetworkInterface | 更新辅助弹性网卡 | To be tested |
| 配额 | ShowQuota | 查询单租户在VPC服务下的网络资源配额,包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额,vpn配额等。 | To be tested |
