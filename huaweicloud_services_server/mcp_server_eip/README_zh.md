# EIP MCP Server 

## 版本信息
v0.1.0

## 产品描述

EIP MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务EIP交互的能力。可以基于自然语言对EIP资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| GEIP与实例的绑定关系 | ListProjectGeipBindings | 查询GEIP与实例绑定关系的租户列表 | To be tested |
| OpenStack - 浮动IP | NeutronUpdateFloatingIp | 更新浮动IP。 | To be tested |
|  | NeutronShowFloatingIp | 查询浮动IP详情,包括浮动IP状态,浮动IP所属路由器ID,浮动IP的外部网络ID等等。 | To be tested |
|  | NeutronDeleteFloatingIp | 删除指定的浮动IP。 | To be tested |
|  | NeutronListFloatingIps | 查询提交请求的租户有权限操作的所有浮动IP地址。 | To be tested |
|  | NeutronCreateFloatingIp | 创建浮动IP的外部网络UUID,请使用GET /v2.0/networks?router:external=True或neutron net-external-list方式获取。 | To be tested |
| 公共池 | ListPublicipPool | 全量查询公网IP池列表 | To be tested |
|  | ListCommonPools | 查询公共池列表 | To be tested |
|  | ShowPublicipPool | 查询公网IP池详情 | To be tested |
| 共享带宽类型 | ListShareBandwidthTypes | 查询指定租户下的共享带宽类型列表 | To be tested |
| 带宽 | AddPublicipsIntoSharedBandwidth | 共享带宽插入弹性公网IP。 | To be tested |
|  | UpdatePrePaidBandwidth | 更新带宽。 | To be tested |
|  | UpdateBandwidth | 更新带宽。 | To be tested |
|  | ListBandwidths | 查询带宽列表。 | To be tested |
|  | ChangeBandwidthToPeriod | 租户按需转包接口。 | To be tested |
|  | DeleteSharedBandwidth | 删除共享带宽。 | To be tested |
|  | RemovePublicipsFromSharedBandwidth | 共享带宽移除弹性公网IP。 | To be tested |
|  | ListEipBandwidths | 查询带宽列表 | To be tested |
|  | ShowBandwidth | 查询带宽 | To be tested |
|  | CreateSharedBandwidth | 创建共享带宽。 | To be tested |
|  | BatchModifyBandwidth | 批量更新带宽,共享带宽和包周期带宽该接口不适用。 | To be tested |
|  | BatchCreateSharedBandwidths | 批量创建共享带宽。 | To be tested |
|  | ListBandwidth | 查询带宽列表 | To be tested |
|  | ListBandwidthsLimit | 获取EIP带宽限制列表 | To be tested |
| 带宽加油包 | ListBandwidthPkg | 查询带宽加油包列表信息 | To be tested |
| 弹性公网IP | DeletePublicip | 删除弹性公网IP,绑定状态eip不允许直接删除。 | To be tested |
|  | ListPublicips | 查询弹性公网IP列表信息 | To be tested |
|  | DisableNat64 | 弹性公网IP关闭NAT64 | To be tested |
|  | ChangePublicipToPeriod | 租户按需转包接口。 | To be tested |
|  | AttachBatchPublicIp | 共享带宽批量加入弹性公网IP | To be tested |
|  | ShowPublicip | 查询弹性公网IP详情 | To be tested |
|  | CountEipAvailableResources | IP池用于查询公网可用ip个数 | To be tested |
|  | DisassociatePublicips | 解绑弹性公网IP | To be tested |
|  | EnableNat64 | 弹性公网IP开启NAT64 | To be tested |
|  | AssociatePublicips | 绑定弹性公网IP | To be tested |
|  | DetachShareBandwidth | 共享带宽移出弹性公网IP | To be tested |
|  | CreatePublicip | 申请弹性公网IP,支持IPv4和IPv6。 | To be tested |
|  | CreatePrePaidPublicip | 申请包年包月的弹性公网IP。 | To be tested |
|  | UpdatePublicip | 更新弹性公网IP | To be tested |
|  | AttachShareBandwidth | 共享带宽加入弹性公网IP | To be tested |
|  | DetachBatchPublicIp | 共享带宽批量移出弹性公网IP | To be tested |
| 弹性公网IP标签管理 | ShowPublicipTags | 查询指定弹性IP实例的标签信息。 | To be tested |
|  | BatchDeletePublicipTags | 为指定的弹性公网IP资源实例批量删除标签。 | To be tested |
|  | CreatePublicipTag | 给指定弹性IP资源实例增加标签信息。 | To be tested |
|  | BatchCreatePublicipTags | 为指定的弹性公网IP资源实例批量添加标签。 | To be tested |
|  | ListPublicipsByTags | 使用标签过滤弹性公网IP。 | To be tested |
|  | DeletePublicipTag | 删除指定弹性公网IP的标签信息。其中project_id是项目ID,publicip_id 是要操作的弹性公网IP的id。key是要删除标签的键。 | To be tested |
|  | ListPublicipTags | 查询租户在指定区域和实例类型的所有标签集合。 | To be tested |
| 弹性公网IP辅助接口 | ShowPublicIpType | 查询PublicIp类型 | To be tested |
|  | CountPublicIp | 查询PublicIp数量 | To be tested |
|  | CountPublicIpInstance | 查询PublicIp实例数 | To be tested |
| 批量操作弹性公网IP | BatchDisassociatePublicips | 批量解绑弹性公网IP | To be tested |
|  | BatchDeletePublicIp | 批量删除弹性公网IP | To be tested |
|  | BatchCreatePublicips | 批量创建弹性公网IP | To be tested |
| 查询Job状态 | ShowResourcesJobDetail | 查询Job状态接口 | To be tested |
| 虚拟igw | ListTenantVpcIgws | 查询指定租户下的虚拟igw列表 | To be tested |
|  | DeleteTenantVpcIgw | 删除虚拟igw | To be tested |
|  | CreateTenantVpcIgw | 创建虚拟igw | To be tested |
|  | UpdateTenantVpcIgw | 修改虚拟igw | To be tested |
|  | ShowInternalVpcIgw | 查询虚拟igw详情 | To be tested |
| 配额 | ListQuotas | 查询配额 | To be tested |
