# GEIP MCP Server 

## 版本信息
v0.1.0

## 产品描述

GEIP MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务GEIP交互的能力。可以基于自然语言对GEIP资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Job相关接口 | ShowJobs | 查询Job详情 | To be tested |
|  | ListJobs | 查询Job列表 | To be tested |
| Region限制 | ListSupportRegions | 全域弹性公网IP支持绑定的Region限制 | To be tested |
|  | ListTenantGeipSupportInstances | console通过此接口获取指定pop点的全域弹性公网IP允许绑定的region实例信息 | To be tested |
| 免责条款签署 | CreateUserDisclaimer | 创建租户签署免责条款 | To be tested |
|  | ShowUserDisclaimer | 查询租户签署免责条款详情 | To be tested |
|  | DeleteUserDisclaimer | 删除租户撤销免责条款 | To be tested |
| 全域公网带宽 | CountInternetBandwidth | 查询全域公网带宽个数 | To be tested |
|  | ShowInternetBandwidth | 查询全域公网带宽详情 | To be tested |
|  | CreateInternetBandwidth | 创建全域公网带宽 | To be tested |
|  | DeleteInternetBandwidth | 删除全域公网带宽 | To be tested |
|  | BatchCreateInternetBandwidth | 批量创建全域公网带宽 | To be tested |
|  | UpdateInternetBandwidth | 更新全域公网带宽 | To be tested |
|  | ListInternetBandwidths | 查询全域公网带宽列表 | To be tested |
| 全域公网带宽标签 | ListInternetBandwidthCountFilterTags | 查询资源实例列表数目 | To be tested |
|  | ShowInternetBandwidthTags | 查询全域公网带宽标签 | To be tested |
|  | AddInternetBandwidthTags | 添加全域公网带宽标签 | To be tested |
|  | BatchDeleteInternetBandwidthTags | 批量删除全域公网带宽标签 | To be tested |
|  | DeleteInternetBandwidthTag | 删除全域公网带宽标签 | To be tested |
|  | ListInternetBandwidthDomainTags | 查询全域公网带宽项目标签 | To be tested |
|  | BatchCreateInternetBandwidthTags | 批量添加全域公网带宽标签 | To be tested |
|  | ListInternetBandwidthFilterTags | 查询资源实例列表 | To be tested |
| 全域公网带宽限制 | ListInternetBandwidthLimits | 查询全域公网带宽限制列表 | To be tested |
| 全域弹性公网IP | CreateGlobalEip | 创建全域弹性公网IP | To be tested |
|  | CountGlobalEips | 查询全域弹性公网IP个数 | To be tested |
|  | AssociateInstance | 绑定后端实例 | To be tested |
|  | DetachInternetBandwidth | 解绑全域公网带宽 | To be tested |
|  | BatchAttachInternetBandwidth | 批量绑定全域公网带宽 | To be tested |
|  | DeleteGlobalEip | 删除全域弹性公网IP | To be tested |
|  | AttachInternetBandwidth | 绑定全域公网带宽 | To be tested |
|  | ListGlobalEips | 查询全域弹性公网IP列表 | To be tested |
|  | BatchCreateGlobalEip | 批量创建全域弹性公网IP | To be tested |
|  | ShowGlobalEip | 查询全域弹性公网IP详情 | To be tested |
|  | BatchDetachInternetBandwidth | 批量解绑全域公网带宽 | To be tested |
|  | UpdateGlobalEip | 更新全域弹性公网IP信息 | To be tested |
|  | DisassociateInstance | 解绑后端实例 | To be tested |
| 全域弹性公网IP标签 | ListGlobalEipDomainTags | 查询全域弹性公网IP的项目标签 | To be tested |
|  | BatchDeleteGlobalEipTags | 批量删除全域弹性公网IP的标签 | To be tested |
|  | AddGlobalEipTags | 添加全域弹性公网IP的标签 | To be tested |
|  | ListGlobalEipCountFilterTags | 查询资源实例列表数目 | To be tested |
|  | DeleteGlobalEipTag | 删除全域弹性公网IP的标签 | To be tested |
|  | ShowGlobalEipTags | 查询全域弹性公网IP的标签 | To be tested |
|  | ListGlobalEipFilterTags | 查询资源实例列表 | To be tested |
|  | BatchCreateGlobalEipTags | 批量添加全域弹性公网IP的标签 | To be tested |
| 全域弹性公网IP段 | CreateGlobalEipSegment | 创建全域弹性公网IP段 | To be tested |
|  | DisassociateGeipSegmentInstance | 全域弹性公网IP段解绑后端实例 | To be tested |
|  | CountGlobalEipSegment | 查询全域弹性公网IP段个数 | To be tested |
|  | ListGlobalEipSegments | 查询全域弹性公网IP段列表 | To be tested |
|  | DeleteGlobalEipSegment | 删除全域弹性公网IP段 | To be tested |
|  | BatchDetachGeipSegmentInternetBandwidth | 全域弹性公网IP段批量解绑全域公网带宽 | To be tested |
|  | UpdateGlobalEipSegment | 更新全域弹性公网IP段 | To be tested |
|  | AssociateGeipSegmentInstance | 全域弹性公网IP段绑定后端实例 | To be tested |
|  | ShowGlobalEipSegment | 查询全域弹性公网IP段详情 | To be tested |
|  | BatchAttachGeipSegmentInternetBandwidth | 全域弹性公网IP段批量绑定全域公网带宽 | To be tested |
| 全域弹性公网IP段标签 | BatchDeleteGeipSegmentTags | 批量删除全域弹性公网IP段的标签 | To be tested |
|  | AddGeipSegmentTags | 添加全域弹性公网IP段的标签 | To be tested |
|  | ListGeipSegmentCountFilterTags | 查询资源实例列表的数目 | To be tested |
|  | ListGeipSegmentDomainTags | 查询全域弹性公网IP段的项目标签 | To be tested |
|  | DeleteGeipSegmentTag | 删除全域弹性公网IP段的标签 | To be tested |
|  | ListGeipSegmentFilterTags | 查询资源实例的列表 | To be tested |
|  | ShowGeipSegmentTags | 查询全域弹性公网IP段的标签 | To be tested |
|  | BatchCreateGeipSegmentTags | 批量添加全域弹性公网IP段的标签 | To be tested |
| 全域弹性公网IP池 | ListGeipPools | 查询全域弹性公网IP池列表 | To be tested |
| 接入点 | ListAccessSites | 查询接入点列表 | To be tested |
| 掩码限制 | ListSupportMasks | 查询全域弹性公网IP段支持的掩码列表 | To be tested |
| 配额 | ListGeipResourceQuotas | 查询租户全域弹性公网IP配额 | To be tested |
