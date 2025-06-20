# DNS MCP Server 

## 版本信息
v0.1.0

## 产品描述

DNS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DNS交互的能力。可以基于自然语言对DNS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| DNSSEC | EnableDnssecConfig | 开启公网域名的DNSSEC。 | To be tested |
|  | ShowDnssecConfig | 查询公网域名的DNSSEC。 | To be tested |
|  | DisableDnssecConfig | 关闭公网域名的DNSSEC。 | To be tested |
| 公网域名管理 | ShowPublicZoneNameServer | 查询公网域名的名称服务器。 | To be tested |
|  | UpdatePublicZoneStatus | 设置公网域名状态,支持暂停、启用域名。 | To be tested |
|  | ListPublicZones | 查询公网域名列表。 | To be tested |
|  | CreatePublicZone | 创建公网域名。 | To be tested |
|  | UpdatePublicZone | 修改公网域名。 | To be tested |
|  | ShowPublicZone | 查询公网域名。 | To be tested |
|  | DeletePublicZone | 删除公网域名。 | To be tested |
| 内网域名管理 | DeletePrivateZone | 删除内网域名。 | To be tested |
|  | SetPrivateZoneProxyPattern | 设置内网域名的子域名递归解析代理。 | To be tested |
|  | ShowPrivateZone | 查询内网域名。 | To be tested |
|  | ListPrivateZones | 查询内网域名列表。 | To be tested |
|  | ShowPrivateZoneNameServer | 查询内网域名的名称服务器。 | To be tested |
|  | UpdatePrivateZoneStatus | 设置内网域名状态,支持暂停、启用域名。 | To be tested |
|  | AssociateRouter | 在内网域名上关联VPC。 | To be tested |
|  | CreatePrivateZone | 创建内网域名。 | To be tested |
|  | DisassociateRouter | 在内网域名上解关联VPC。 | To be tested |
|  | UpdatePrivateZone | 修改内网域名。 | To be tested |
| 反向解析管理(待废弃) | UpdatePtrRecord | 修改弹性公网IP的反向解析记录。 | To be tested |
|  | ListPtrRecords | 查询弹性公网IP的反向解析记录列表。 | To be tested |
|  | RestorePtrRecord | 将弹性公网IP的反向解析记录恢复为默认值。 | To be tested |
|  | ShowPtrRecordSet | 查询弹性公网IP的反向解析记录。 | To be tested |
|  | CreateEipRecordSet | 设置弹性公网IP的反向解析记录。 | To be tested |
| 反向解析管理(新版本) | ListPtrs | 查询弹性公网IP的反向解析记录列表。 | To be tested |
|  | DeletePtr | 将弹性公网IP的反向解析记录恢复为默认值。 | To be tested |
|  | UpdatePtr | 修改弹性公网IP的反向解析记录。 | To be tested |
|  | CreatePtr | 创建弹性公网IP的反向解析记录。 | To be tested |
|  | ShowPtr | 查询弹性公网IP的反向解析记录。 | To be tested |
| 名称服务器管理 | ListNameServers | 查询名称服务器列表 | To be tested |
| 批量接口管理 | BatchDeleteRecordSetWithLine | 批量删除域名下的记录集,当删除的资源不存在时,则默认删除成功。 | To be tested |
|  | BatchSetRecordSetsStatus | 批量设置记录集状态。 | To be tested |
|  | CreateRecordSetWithBatchLines | 批量线路创建记录集。属于原子性操作,如果存在一个参数校验不通过,则创建失败。仅公网域名支持。 | To be tested |
|  | BatchDeleteZones | 批量删除域名。 | To be tested |
|  | BatchDeletePtrRecords | 批量删除反向解析。本接口为原子操作,所有记录应全部删除成功或全部失败。 | To be tested |
|  | BatchSetZonesStatus | 批量设置域名状态。 | To be tested |
|  | BatchDeleteRecordSets | 批量删除记录集。 | To be tested |
|  | BatchUpdateRecordSetWithLine | 批量修改记录集。属于原子性操作,请求记录集将全部完成修改,或不做任何修改。 | To be tested |
| 标签管理 | ListTag | 使用标签查询资源实例 | To be tested |
|  | ShowResourceTag | 查询指定实例的标签信息 | To be tested |
|  | CreateTag | 为指定实例添加标签 | To be tested |
|  | DeleteTag | 删除资源标签 | To be tested |
|  | BatchCreateTag | 为指定实例批量添加或删除标签 | To be tested |
|  | ListTags | 查询指定实例类型的所有标签集合 | To be tested |
| 版本管理 | ShowApiInfo | 查询指定的云解析服务API版本号。 | To be tested |
|  | ListApiVersions | 查询所有的云解析服务API版本号列表。 | To be tested |
| 线路分组管理 | ShowLineGroup | 查询线路分组。该接口部分区域未上线,如需使用请提交工单申请开通。 | To be tested |
|  | UpdateLineGroups | 更新线路分组。该接口部分区域未上线,如需使用请提交工单申请开通。 | To be tested |
|  | DeleteLineGroup | 删除线路分组。该接口部分区域未上线,如需使用请提交工单申请开通。 | To be tested |
|  | CreateLineGroup | 创建线路分组。该接口部分区域未上线,如需使用请提交工单申请开通。 | To be tested |
|  | ListLineGroups | 查询线路分组列表。该接口部分区域未上线,如需使用请提交工单申请开通。 | To be tested |
| 终端节点管理 | DisassociateEndpointIpaddress | 终端节点解绑IP地址。 | To be tested |
|  | DeleteEndpoint | 删除终端节点。 | To be tested |
|  | ShowEndpoint | 查询终端节点。 | To be tested |
|  | ListEndpointVpcs | 查询终端节点VPC列表。 | To be tested |
|  | AssociateEndpointIpaddress | 终端节点绑定IP地址。 | To be tested |
|  | ListEndpointIpaddresses | 查询终端节点下的IP地址列表。 | To be tested |
|  | UpdateEndpoint | 修改终端节点 | To be tested |
|  | CreateEndpoint | 创建终端节点。 | To be tested |
|  | ListEndpoints | 查询终端节点列表。 | To be tested |
| 自定义线路管理 | ListCustomLine | 查询自定义线路。 | To be tested |
|  | CreateCustomLine | 创建自定义线路。 | To be tested |
|  | UpdateCustomLine | 更新自定义线路。 | To be tested |
|  | DeleteCustomLine | 删除自定义线路。 | To be tested |
| 记录集管理(待废弃) | ListRecordSets | 查询租户记录集列表。 | To be tested |
|  | ShowRecordSet | 查询记录集。 | To be tested |
|  | DeleteRecordSet | 删除记录集。删除有添加智能解析的记录集时,需要用记录集管理(新版本)模块中删除接口进行删除。 | To be tested |
|  | UpdateRecordSet | 修改记录集。 | To be tested |
|  | ListRecordSetsByZone | 查询域名下的记录集列表。 | To be tested |
|  | CreateRecordSet | 创建记录集。 | To be tested |
| 记录集管理(新版本) | SetRecordSetsStatus | 设置记录集状态。 | To be tested |
|  | DeleteRecordSets | 删除记录集。 | To be tested |
|  | ListRecordSetsWithLine | 查询租户记录集列表。 | To be tested |
|  | ShowRecordSetByZone | 查询域名下的记录集列表。 | To be tested |
|  | ShowRecordSetWithLine | 查询记录集。 | To be tested |
|  | UpdateRecordSets | 修改记录集。 | To be tested |
|  | ListPublicZoneLines | 查询公网域名的线路列表。 | To be tested |
|  | CreateRecordSetWithLine | 创建记录集。 | To be tested |
| 转发规则管理 | AssociateResolverRuleRouter | 解析器转发规则关联VPC。 | To be tested |
|  | ListResolverRules | 查询解析器转发规则列表。 | To be tested |
|  | DeleteResolverRule | 删除解析器转发规则。 | To be tested |
|  | ShowResolverRule | 查询解析器转发规则。 | To be tested |
|  | CreateResolverRule | 创建解析器转发规则。 | To be tested |
|  | UpdateResolverRule | 修改解析器转发规则。 | To be tested |
|  | DisassociateResolverRuleRouter | 解析器转发规则解关联VPC。 | To be tested |
| 配额管理 | ShowDomainQuota | 查询租户在DNS服务下的资源配额,包括公网域名配额、内网域名配额、记录集配额、反向解析配额、自定义线路配额、线路分组配额、入站终端节点配额、出站终端节点配额、转发规则配额等。 | To be tested |
