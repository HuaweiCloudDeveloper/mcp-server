# DNS MCP Server 


## Version
v0.1.0

## Overview

DNS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DNS. Full-chain management of DNS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

<html>
    <head></head>
    <body>
        <table border="1" cellspacing="0" cellpadding="5">
            <tbody>
                <tr>
                    <th>类别</th>
                    <th>工具名称</th>
                    <th>功能描述</th>
                    <th>状态</th>
                </tr>
                <tr>
                    <td rowspan="3">DNSSEC</td>
                    <td>EnableDnssecConfig</td>
                    <td>开启公网域名的DNSSEC。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDnssecConfig</td>
                    <td>查询公网域名的DNSSEC。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableDnssecConfig</td>
                    <td>关闭公网域名的DNSSEC。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">公网域名管理</td>
                    <td>ShowPublicZoneNameServer</td>
                    <td>查询公网域名的名称服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublicZoneStatus</td>
                    <td>设置公网域名状态,支持暂停、启用域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublicZones</td>
                    <td>查询公网域名列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePublicZone</td>
                    <td>创建公网域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublicZone</td>
                    <td>修改公网域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPublicZone</td>
                    <td>查询公网域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePublicZone</td>
                    <td>删除公网域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">内网域名管理</td>
                    <td>DeletePrivateZone</td>
                    <td>删除内网域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetPrivateZoneProxyPattern</td>
                    <td>设置内网域名的子域名递归解析代理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateZone</td>
                    <td>查询内网域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateZones</td>
                    <td>查询内网域名列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateZoneNameServer</td>
                    <td>查询内网域名的名称服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrivateZoneStatus</td>
                    <td>设置内网域名状态,支持暂停、启用域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRouter</td>
                    <td>在内网域名上关联VPC。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePrivateZone</td>
                    <td>创建内网域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateRouter</td>
                    <td>在内网域名上解关联VPC。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrivateZone</td>
                    <td>修改内网域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">反向解析管理(待废弃)</td>
                    <td>UpdatePtrRecord</td>
                    <td>修改弹性公网IP的反向解析记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPtrRecords</td>
                    <td>查询弹性公网IP的反向解析记录列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestorePtrRecord</td>
                    <td>将弹性公网IP的反向解析记录恢复为默认值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPtrRecordSet</td>
                    <td>查询弹性公网IP的反向解析记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEipRecordSet</td>
                    <td>设置弹性公网IP的反向解析记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">反向解析管理(新版本)</td>
                    <td>ListPtrs</td>
                    <td>查询弹性公网IP的反向解析记录列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePtr</td>
                    <td>将弹性公网IP的反向解析记录恢复为默认值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePtr</td>
                    <td>修改弹性公网IP的反向解析记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePtr</td>
                    <td>创建弹性公网IP的反向解析记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPtr</td>
                    <td>查询弹性公网IP的反向解析记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">名称服务器管理</td>
                    <td>ListNameServers</td>
                    <td>查询名称服务器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">密钥标签管理</td>
                    <td>DeleteTag</td>
                    <td>- 功能介绍:删除密钥标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">批量接口管理</td>
                    <td>BatchDeleteRecordSetWithLine</td>
                    <td>批量删除域名下的记录集,当删除的资源不存在时,则默认删除成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetRecordSetsStatus</td>
                    <td>批量设置记录集状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRecordSetWithBatchLines</td>
                    <td>批量线路创建记录集。属于原子性操作,如果存在一个参数校验不通过,则创建失败。仅公网域名支持。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteZones</td>
                    <td>批量删除域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePtrRecords</td>
                    <td>批量删除反向解析。本接口为原子操作,所有记录应全部删除成功或全部失败。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetZonesStatus</td>
                    <td>批量设置域名状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteRecordSets</td>
                    <td>批量删除记录集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateRecordSetWithLine</td>
                    <td>批量修改记录集。属于原子性操作,请求记录集将全部完成修改,或不做任何修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询API版本信息</td>
                    <td>ShowApiInfo</td>
                    <td>查询对象存储迁移服务指定API版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询版本操作</td>
                    <td>ListApiVersions</td>
                    <td>查询标签管理服务的API版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">标签</td>
                    <td>ListTag</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">标签管理</td>
                    <td>CreateTag</td>
                    <td>为资源添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateTag</td>
                    <td>为指定实例批量添加或删除标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">线路分组管理</td>
                    <td>ShowLineGroup</td>
                    <td>查询线路分组。该接口部分区域未上线,如需使用请提交工单申请开通。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLineGroups</td>
                    <td>更新线路分组。该接口部分区域未上线,如需使用请提交工单申请开通。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLineGroup</td>
                    <td>删除线路分组。该接口部分区域未上线,如需使用请提交工单申请开通。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLineGroup</td>
                    <td>创建线路分组。该接口部分区域未上线,如需使用请提交工单申请开通。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLineGroups</td>
                    <td>查询线路分组列表。该接口部分区域未上线,如需使用请提交工单申请开通。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">终端节点功能</td>
                    <td>DeleteEndpoint</td>
                    <td>删除终端节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEndpoint</td>
                    <td>创建终端节点,以便访问终端节点服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpoints</td>
                    <td>查询当前用户下的终端节点的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">终端节点管理</td>
                    <td>DisassociateEndpointIpaddress</td>
                    <td>终端节点解绑IP地址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEndpoint</td>
                    <td>查询终端节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpointVpcs</td>
                    <td>查询终端节点VPC列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateEndpointIpaddress</td>
                    <td>终端节点绑定IP地址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpointIpaddresses</td>
                    <td>查询终端节点下的IP地址列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">自定义线路管理</td>
                    <td>ListCustomLine</td>
                    <td>查询自定义线路。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCustomLine</td>
                    <td>创建自定义线路。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCustomLine</td>
                    <td>更新自定义线路。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomLine</td>
                    <td>删除自定义线路。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">记录集管理(待废弃)</td>
                    <td>ListRecordSets</td>
                    <td>查询租户记录集列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordSet</td>
                    <td>查询记录集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRecordSet</td>
                    <td>删除记录集。删除有添加智能解析的记录集时,需要用记录集管理(新版本)模块中删除接口进行删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRecordSet</td>
                    <td>修改记录集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecordSetsByZone</td>
                    <td>查询域名下的记录集列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRecordSet</td>
                    <td>创建记录集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">记录集管理(新版本)</td>
                    <td>SetRecordSetsStatus</td>
                    <td>设置记录集状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRecordSets</td>
                    <td>删除记录集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecordSetsWithLine</td>
                    <td>查询租户记录集列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordSetByZone</td>
                    <td>查询域名下的记录集列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordSetWithLine</td>
                    <td>查询记录集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRecordSets</td>
                    <td>修改记录集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublicZoneLines</td>
                    <td>查询公网域名的线路列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRecordSetWithLine</td>
                    <td>创建记录集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">访问端点管理</td>
                    <td>UpdateEndpoint</td>
                    <td>更新访问端点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">账号管理</td>
                    <td>ShowDomainQuota</td>
                    <td>该接口可以用于查询账号配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资源标签</td>
                    <td>ShowResourceTag</td>
                    <td>查询单个资源上的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">转发规则管理</td>
                    <td>AssociateResolverRuleRouter</td>
                    <td>解析器转发规则关联VPC。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResolverRules</td>
                    <td>查询解析器转发规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResolverRule</td>
                    <td>删除解析器转发规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResolverRule</td>
                    <td>查询解析器转发规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResolverRule</td>
                    <td>创建解析器转发规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResolverRule</td>
                    <td>修改解析器转发规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateResolverRuleRouter</td>
                    <td>解析器转发规则解关联VPC。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像标签</td>
                    <td>ListTags</td>
                    <td>根据不同条件查询镜像标签列表信息。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
