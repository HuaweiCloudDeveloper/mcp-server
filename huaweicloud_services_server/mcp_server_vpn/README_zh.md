# VPN MCP Server 

## 版本信息
v0.1.0

## 产品描述

VPN MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务VPN交互的能力。可以基于自然语言对VPN资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| ClientCaCertificate | CheckClientCaCertificate | 创建服务端时,可以先调用客户端CA的预校验API,检查CA的合法性 | To be tested |
|  | UpdateClientCa | 修改客户端CA证书 | To be tested |
|  | ImportClientCa | 导入客户端 CA 证书 | To be tested |
|  | DeleteClientCa | 删除客户端CA证书 | To be tested |
|  | ShowClientCa | 查询客户端CA证书 | To be tested |
| ConnectionMonitor | ListConnectionMonitors | 查询VPN连接监控列表 | To be tested |
|  | ShowConnectionMonitor | 根据VPN连接监控的ID,查询指定的VPN连接监控 | To be tested |
|  | DeleteConnectionMonitor | 根据VPN连接监控的ID,删除指定的VPN连接监控 | To be tested |
|  | CreateConnectionMonitor | 创建VPN连接监控 | To be tested |
| CustomerGateway | ShowCgw | 根据对端网关ID,查询指定的对端网关 | To be tested |
|  | DeleteCgw | 根据对端网关ID,删除指定的对端网关 | To be tested |
|  | CreateCgw | 创建租户用于与VPN网关相连的对端网关 | To be tested |
|  | UpdateCgw | 根据对端网关ID,更新指定的对端网关 | To be tested |
|  | ListCgws | 查询对端网关列表 | To be tested |
| P2cVpnGateway | DeleteP2cVgwConnection | 断开P2C VPN网关连接 | To be tested |
|  | ListP2cVgwAvailabilityZones | 查询P2C VPN网关可用区 | To be tested |
|  | ListP2cVgwConnections | List p2c vpn gateway connections | To be tested |
|  | ListP2cVgws | 查询P2C VPN网关列表 | To be tested |
|  | ShowP2cVgw | 根据P2C VPN网关ID,查询指定的VPN网关 | To be tested |
|  | UpdateP2cVgw | 根据P2C VPN网关ID,更新指定的P2C VPN网关 | To be tested |
| Tags | ShowResourceTags | 查询指定实例的标签信息 | To be tested |
|  | BatchCreateResourceTags | 为指定实例批量添加标签 | To be tested |
|  | ListResourcesByTags | 根据标签查询资源实例列表 | To be tested |
|  | ListProjectTags | 查询租户在指定项目中指定资源类型下的所有标签 | To be tested |
|  | BatchDeleteResourceTags | 为指定实例批量删除标签 | To be tested |
|  | CountResourcesByTags | 根据标签查询资源实例数量 | To be tested |
| VpnAccessPolicy | UpdateVpnAccessPolicy | 修改VPN访问策略 | To be tested |
|  | DeleteVpnAccessPolicy | 删除VPN访问策略 | To be tested |
|  | ListVpnAccessPolicies | 查询VPN访问策略列表 | To be tested |
|  | CreateVpnAccessPolicy | 创建VPN访问策略 | To be tested |
|  | ShowVpnAccessPolicy | 查询VPN访问策略 | To be tested |
| VpnConnection | ShowVpnConnection | 根据连接ID,查询指定的VPN连接的参数 | To be tested |
|  | UpdateVpnConnection | 根据连接ID,更新指定的VPN连接的参数 | To be tested |
|  | ResetVpnConnection | 根据连接ID,重置指定VPN连接 | To be tested |
|  | CreateVpnConnection | 创建VPN连接,连接VPN网关与对端网关 | To be tested |
|  | ShowVpnConnectionLog | 根据连接ID,查询指定的VPN连接日志 | To be tested |
|  | ListVpnConnections | 查询VPN连接列表 | To be tested |
|  | DeleteVpnConnection | 根据连接ID,删除指定的VPN连接 | To be tested |
| VpnConnectionsLogConfig | ShowVpnConnectionsLogConfig | 查询VPN连接日志配置 | To be tested |
|  | DeleteVpnConnectionsLogConfig | 删除VPN连接日志配置 | To be tested |
|  | UpdateVpnConnectionsLogConfig | 更新VPN连接日志配置 | To be tested |
| VpnGateway | ShowVgw | 根据VPN网关ID,查询指定的VPN网关 | To be tested |
|  | ListExtendedAvailabilityZones | 查询VPN网关可用区 | To be tested |
|  | ShowVpnGatewayRoutingTable |  | To be tested |
|  | UpdatePostpaidVgwSpecification | 对单个网关规格进行修改,可以升配或降配 | To be tested |
|  | ListAvailabilityZones | 查询VPN网关可用区 | To be tested |
|  | CreateVgw | 创建一个VPN网关 | To be tested |
|  | UpdateVgw | 根据VPN网关ID,更新指定的VPN网关 | To be tested |
|  | ListVgws | 查询VPN网关列表 | To be tested |
|  | DeleteVgw | 根据VPN网关ID,删除指定的VPN网关 | To be tested |
| VpnGatewayCertificate | ShowVpnGatewayCertificate | 根据VPN网关ID,查询所指定的VPN网关证书 | To be tested |
|  | UpdateVgwCertificate | 更新租户VPN网关所使用的证书,包括签名证书、签名私钥、加密证书、加密私钥和CA证书链。当前只支持国密证书 | To be tested |
|  | CreateVgwCertificate | 导入租户VPN网关所使用的证书,包括签名证书、签名私钥、加密证书、加密私钥和CA证书链。当前只支持国密证书 | To be tested |
| VpnQuota | ShowQuotasInfo | 查询指定租户的配额 | To be tested |
| VpnServer | ListVpnServersByVgw | 查询一个网关下的服务端信息 | To be tested |
|  | UpdateVpnServer | 更新指定VPN 服务端 | To be tested |
|  | ExportClientConfig | 导出客户端配置信息 | To be tested |
|  | CreateVpnServer | 创建一个VPN 服务端 | To be tested |
|  | ListVpnServersByProject | 查询租户下的所有服务端信息 | To be tested |
| VpnUser | ListVpnUsers | 查询VPN用户列表 | To be tested |
|  | UpdateVpnUser | 修改VPN用户 | To be tested |
|  | CreateVpnUser | 创建VPN用户 | To be tested |
|  | BatchCreateVpnUsers | 批量创建P2C VPN用户 | To be tested |
|  | UpdateVpnUserPassword | 修改VPN用户密码 | To be tested |
|  | ShowVpnUser | 查询VPN用户 | To be tested |
|  | DeleteVpnUser | 删除VPN用户 | To be tested |
|  | ResetVpnUserPassword | 重置VPN用户密码 | To be tested |
|  | BatchDeleteVpnUsers | 批量删除P2C VPN用户 | To be tested |
| VpnUserGroup | AddVpnUsersToGroup | 添加VPN用户到组 | To be tested |
|  | CreateVpnUserGroup | 创建VPN用户组 | To be tested |
|  | ListVpnUserGroups | 查询VPN用户组列表 | To be tested |
|  | DeleteVpnUserGroup | 删除VPN用户组 | To be tested |
|  | UpdateVpnUserGroup | 修改VPN用户组 | To be tested |
|  | ListVpnUsersInGroup | 查询组内VPN用户 | To be tested |
|  | RemoveVpnUsersFromGroup | 删除组内VPN用户 | To be tested |
|  | ShowVpnUserGroup | 查询VPN用户组 | To be tested |
