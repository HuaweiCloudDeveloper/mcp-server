# IEC MCP Server 

## 版本信息
v0.1.0

## 产品描述

IEC MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IEC交互的能力。可以基于自然语言对IEC资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| port | AttachVipBandwidth | IPv6虚拟IP或者IPv6私网IP绑定带宽,支持公网访问。 | To be tested |
|  | DetachVipBandwidth | IPv6虚拟IP或者IPv6私网IP解绑带宽。 | To be tested |
| subnet | CreateSubnet | 根据用户的请求内容,创建子网。 | To be tested |
| 子网 | UpdateSubnet | 更新子网的基本信息。 | To be tested |
|  | DeleteSubnet | 根据子网的ID,删除子网。 | To be tested |
|  | ListRelatedRoutetables | 查询子网关联的路由表。 | To be tested |
|  | ListSubnets | 根据查询条件获取子网的列表信息。 | To be tested |
|  | ShowSubnet | 根据子网的ID,获取子网的详细信息。 | To be tested |
| 安全组 | ListSecurityGroups | 根据特定查询条件,获取安全组的列表信息。 | To be tested |
|  | ShowSecurityGroup | 根据安全组的ID,获取特定安全组的详细信息。 | To be tested |
|  | DeleteSecurityGroupRule | 根据安全组的ID,删除对应的安全组。 | To be tested |
|  | CreateSecurityGroup | 根据用户的请求内容,创建对应的安全组。 | To be tested |
|  | CreateSecurityGroupRule | 根据用户的请求内容,创建安全组规则。 | To be tested |
|  | DeleteSecurityGroup | 根据安全组的ID,删除对应的安全组。 | To be tested |
|  | ListSecurityGroupRules | 根据用户的查询条件,获取安全组规则的列表信息。 | To be tested |
|  | ShowSecurityGroupRule | 根据安全组规则的ID,获取安全组规则的详细信息。 | To be tested |
| 密钥对 | ListKeypairs | 查询密钥信息列表。 | To be tested |
|  | DeleteKeypair | 删除密钥。 | To be tested |
|  | ShowKeypair | 查询密钥信息列表。 | To be tested |
|  | CreateKeypair | 创建SSH密钥,或把公钥导入系统,生成密钥对。 | To be tested |
| 带宽 | ListBandwidths | 查询带宽列表。 | To be tested |
|  | ListBandwidthTypes | 查询共享带宽类型列表。 | To be tested |
|  | DeleteBandwidth | 删除带宽。 | To be tested |
|  | ShowBandwidth | 查询带宽详情。 | To be tested |
|  | UpdateBandwidth | 更新带宽。 | To be tested |
| 弹性公网IP | ListPublicIps | 获取弹性公网IP列表信息。 | To be tested |
|  | CreatePublicIp | 根据用户的请求内容,创建弹性公网IP | To be tested |
|  | DeletePublicIp | 根据弹性公网IP的ID,删除对应的弹性公网IP。 | To be tested |
|  | UpdatePublicIp | 更新弹性公网IP的信息,主要用于解绑和绑定EIP和VIP之间的关系。 | To be tested |
|  | ShowPublicIp | 获取弹性公网IP的详情信息。 | To be tested |
| 端口 | UpdatePort | 更新端口。 | To be tested |
|  | ShowPort | 根据端口的ID,获取端口的详细信息。 | To be tested |
|  | ListPorts | 查询端口的列表信息 | To be tested |
|  | CreatePort | 创建端口。 | To be tested |
|  | DeletePort | 删除端口。 | To be tested |
| 网络ACL | ShowFirewall | 查询网络ACL详情。 | To be tested |
|  | CreateFirewall | 创建网络ACL。 | To be tested |
|  | DeleteFirewall | 删除网络ACL。 | To be tested |
|  | ListFirewalls | 查询网络ACL列表。 | To be tested |
|  | UpdateFirewall | 更新网络ACL。 | To be tested |
|  | UpdateFirewallRule | 更新网络ACL规则。 | To be tested |
| 虚拟私有云 | DeleteVpc | 根据虚拟机私有云的ID,删除对应的虚拟私有云。 | To be tested |
|  | UpdateVpc | 更新虚拟私有云的信息 | To be tested |
|  | CreateVpc | 根据用户的请求内容,创建虚拟私有云。 | To be tested |
|  | ListVpcs | 获取虚拟私有云的列表。 | To be tested |
|  | ShowVpc | 根据虚拟私有云ID,获取虚拟私有云的详情。 | To be tested |
| 路由表 | DisassociateSubnet | 路由表解关联子网 | To be tested |
|  | AssociateSubnet | 路由表关联子网 | To be tested |
|  | DeleteRoutes | 删除路由 | To be tested |
|  | UpdateRoutes | 更新路由信息 | To be tested |
|  | ListRoutes | 查询路由列表 | To be tested |
|  | ListRoutetables | 查询路由列表 | To be tested |
|  | CreateRoutes | 创建路由 | To be tested |
|  | UpdateRoutetable | 更新路由表基本信息 | To be tested |
|  | ShowRoutetable | 查询路由表详情 | To be tested |
|  | DeleteRoutetable | 删除路由表 | To be tested |
|  | CreateRoutetable | 创建路由表 | To be tested |
| 边缘业务 | CreateDeployment | 为方便您的统一管理,以及跨边缘站点管理资源,IEC基于业务场景角度,定义了边缘业务。 | To be tested |
|  | ListDeployments | 查询部署计划列表。 | To be tested |
|  | DeleteDeployment | 删除部署计划。 | To be tested |
|  | ShowEdgeCloud | 查询边缘业务详情。 | To be tested |
|  | ExecuteDeployment | 执行部署计划,创建一个边缘业务。单租户默认可创建10个边缘业务。 | To be tested |
|  | DeleteEdgeCloud | 删除边缘业务。 | To be tested |
|  | ExpandEdgecloud | 执行部署计划,对边缘业务进行扩容操作。 | To be tested |
|  | ListEdgeCloud | 查询边缘业务列表。 | To be tested |
| 边缘实例 | CreateInstance | 创建边缘实例。单租户默认可创建50个边缘实例。 | To be tested |
|  | DeleteNics | 删除网卡。 | To be tested |
|  | ShowInstance | 查询边缘实例详情。 | To be tested |
|  | ListInstances | 查询边缘实例列表。 | To be tested |
|  | UpdateInstance | 修改边缘实例。 | To be tested |
|  | AddNics | 添加网卡。 | To be tested |
|  | ChangeOs | 切换边缘实例操作系统,支持边缘实例创建成功后,保持ip、数据盘不变的情况下重装操作系统。 | To be tested |
|  | BatchStartInstance | 批量操作启动边缘实例。 | To be tested |
|  | DeleteInstances | 批量删除边缘实例。 | To be tested |
|  | BatchRebootInstance | 批量重启边缘实例。 | To be tested |
|  | BatchStopInstance | 批量关闭边缘实例。 | To be tested |
| 边缘硬盘 | ListVolume | 查询硬盘列表。 | To be tested |
|  | ShowVolumeTypes | 查询硬盘类型列表。 | To be tested |
|  | ShowVolume | 查询硬盘详情。 | To be tested |
| 边缘站点 | ListSites | 查询边缘站点列表。 | To be tested |
| 边缘规格 | ListFlavors | 查询边缘规格列表。 | To be tested |
| 边缘镜像 | ListImages | 根据不同条件查询镜像列表,例: | To be tested |
|  | DeleteImage | 将指定ID的边缘私有镜像删除 | To be tested |
|  | ListCloudImages | 查询租户在某个云Region的可见镜像列表。 | To be tested |
|  | ShowImage | 查询镜像详情。 | To be tested |
|  | CreateImage | 使用指定边缘实例的系统盘创建边缘私有镜像。 | To be tested |
|  | RebuildImage | 重试边缘镜像任务。 | To be tested |
|  | RegisterImage | 将指定Region和ID的IMS镜像注册到边缘IEC-IMS;  | To be tested |
| 配额 | ListQuota | 查询租户资源配额。 | To be tested |
