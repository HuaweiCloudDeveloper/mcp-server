# VPC MCP Server 


## Version
v0.1.0

## Overview

VPC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VPC. Full-chain management of VPC resources can be carried out based on natural language.

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
                    <td rowspan="6">IP地址组</td>
                    <td>ShowAddressGroup</td>
                    <td>查询地址组详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAddressGroup</td>
                    <td>创建地址组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAddressGroup</td>
                    <td>查询地址组列表,根据过滤条件进行过滤。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIpAddressGroupForce</td>
                    <td>强制删除地址组,删除的地址组与安全组规则关联时,会删除地址组与关联的安全组规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAddressGroup</td>
                    <td>删除地址组,非强制删除,删除前请确保未被其他资源引用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAddressGroup</td>
                    <td>更新地址组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">OpenStack - API版本信息</td>
                    <td>ListApiVersion</td>
                    <td>返回当前API所有可用的版本(仅针对OpenStack原生接口)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">OpenStack - 子网</td>
                    <td>NeutronShowSubnet</td>
                    <td>查询子网详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateSubnet</td>
                    <td>创建子网。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateSubnet</td>
                    <td>更新子网</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListSubnets</td>
                    <td>查询提交请求租户的所有子网,单次查询最多返回2000条数据,超过2000后会返回分页标记。分页查询请参考分页查询 。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteSubnet</td>
                    <td>删除子网</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">OpenStack - 安全组</td>
                    <td>NeutronCreateSecurityGroupRule</td>
                    <td>创建安全组规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowSecurityGroup</td>
                    <td>查询安全组详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateSecurityGroup</td>
                    <td>创建安全组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowSecurityGroupRule</td>
                    <td>查询安全组规则详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListSecurityGroupRules</td>
                    <td>查询提交请求的租户有权限查看的所有安全组规则。单次查询最多返回2000条数据,超过2000后会返回分页标记。分页查询请参考分页查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateSecurityGroup</td>
                    <td>更新安全组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListSecurityGroups</td>
                    <td>查询提交请求租户的所有安全组,单次查询最多返回2000条数据,超过2000后会返回分页标记。分页查询请参考分页查询 。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteSecurityGroup</td>
                    <td>删除安全组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteSecurityGroupRule</td>
                    <td>删除安全组规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">OpenStack - 端口</td>
                    <td>NeutronDeletePort</td>
                    <td>删除端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdatePort</td>
                    <td>更新端口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowPort</td>
                    <td>查询端口详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListPorts</td>
                    <td>查询提交请求的租户的所有端口,单次查询最多返回2000条数据,超过2000后会返回分页标记。分页查询请参考分页查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreatePort</td>
                    <td>创建端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">OpenStack - 网络</td>
                    <td>NeutronShowNetwork</td>
                    <td>查询指定的网络详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteNetwork</td>
                    <td>删除网络</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateNetwork</td>
                    <td>创建网络</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListNetworks</td>
                    <td>查询提交请求的租户的所有网络,单次查询最多返回2000条数据,超过2000后会返回分页标记。分页查询请参考分页查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateNetwork</td>
                    <td>更新网络</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">OpenStack - 网络ACL</td>
                    <td>NeutronListFirewallRules</td>
                    <td>查询提交请求的租户有权限操作的所有网络ACL规则信息。单次查询最多返回2000条数据,超过2000后会返回分页标记。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowFirewallPolicy</td>
                    <td>查询特定网络ACL策略详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteFirewallPolicy</td>
                    <td>删除网络ACL策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateFirewallGroup</td>
                    <td>更新网络ACL组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteFirewallRule</td>
                    <td>删除网络ACL规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowFirewallGroup</td>
                    <td>查询特定网络ACL组详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateFirewallGroup</td>
                    <td>创建网络ACL组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronRemoveFirewallRule</td>
                    <td>从某一网络ACL策略中移除一条网络ACL规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronAddFirewallRule</td>
                    <td>插入一条网络ACL规则到某一网络ACL策略中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateFirewallPolicy</td>
                    <td>更新网络ACL策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListFirewallGroups</td>
                    <td>查询提交请求的租户有权限操作的所有网络ACL组信息。单次查询最多返回2000条数据,超过2000后会返回分页标记。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateFirewallRule</td>
                    <td>创建网络ACL规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateFirewallPolicy</td>
                    <td>创建网络ACL策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListFirewallPolicies</td>
                    <td>查询提交请求的租户有权限操作的所有网络ACL策略信息。单次查询最多返回2000条数据,超过2000后会返回分页标记。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateFirewallRule</td>
                    <td>更新网络ACL规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteFirewallGroup</td>
                    <td>删除网络ACL组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowFirewallRule</td>
                    <td>查询特定网络ACL规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">OpenStack - 路由器</td>
                    <td>NeutronRemoveRouterInterface</td>
                    <td>删除路由器接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateRouter</td>
                    <td>创建路由器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowRouter</td>
                    <td>查询路由器详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronUpdateRouter</td>
                    <td>更新路由器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListRouters</td>
                    <td>查询提交请求的租户有权限操作的所有路由器信息,单次查询最多返回2000条数据,超过2000后会返回分页标记。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronAddRouterInterface</td>
                    <td>添加路由器接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteRouter</td>
                    <td>删除路由器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">VPC</td>
                    <td>DeleteVpc</td>
                    <td>删除虚拟私有云。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpc</td>
                    <td>更新虚拟私有云。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpc</td>
                    <td>创建虚拟私有云。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcs</td>
                    <td>查询vpc列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpc</td>
                    <td>查询vpc详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddVpcExtendCidr</td>
                    <td>添加VPC的扩展网段</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveVpcExtendCidr</td>
                    <td>移除VPC扩展网段</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">VPC资源标签管理</td>
                    <td>BatchDeleteVpcTags</td>
                    <td>为指定的VPC资源实例批量删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcsByTags</td>
                    <td>使用标签过滤实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcTags</td>
                    <td>查询租户在指定区域和实例类型的所有标签集合</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateVpcTags</td>
                    <td>为指定的VPC资源实例批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpcResourceTag</td>
                    <td>给指定VPC资源实例增加标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpcTag</td>
                    <td>删除指定VPC资源实例的标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpcTags</td>
                    <td>查询指定VPC实例的标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">VPC路由</td>
                    <td>DeleteVpcRoute</td>
                    <td>删除路由</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpcRoute</td>
                    <td>查询路由详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcRoutes</td>
                    <td>查询提交请求的租户的所有路由列表,并根据过滤条件进行过滤。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpcRoute</td>
                    <td>创建路由</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">子网</td>
                    <td>ShowSubnet</td>
                    <td>查询子网详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubnet</td>
                    <td>更新子网。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubnet</td>
                    <td>创建子网。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubnet</td>
                    <td>删除子网</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubnets</td>
                    <td>查询子网列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">子网资源标签管理</td>
                    <td>BatchDeleteSubnetTags</td>
                    <td>为指定的子网资源实例批量删除标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubnetTags</td>
                    <td>查询指定子网实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubnetTags</td>
                    <td>查询租户在指定区域和实例类型的所有标签集合</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubnetsByTags</td>
                    <td>使用标签过滤实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubnetTag</td>
                    <td>删除指定子网资源实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateSubnetTags</td>
                    <td>为指定的子网资源实例批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubnetTag</td>
                    <td>给指定子网资源实例增加标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">安全组</td>
                    <td>ListSecurityGroups</td>
                    <td>查询某租户下的安全组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityGroup</td>
                    <td>创建安全组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityGroup</td>
                    <td>删除安全组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityGroup</td>
                    <td>查询单个安全组详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityGroup</td>
                    <td>更新安全组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">安全组规则</td>
                    <td>ListSecurityGroupRules</td>
                    <td>查询安全组规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityGroupRule</td>
                    <td>删除安全组规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityGroupRule</td>
                    <td>查询单个安全组规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateSecurityGroupRules</td>
                    <td>在特定安全组下批量创建安全组规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityGroupRule</td>
                    <td>创建安全组规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">安全组资源标签管理</td>
                    <td>ListSecurityGroupTags</td>
                    <td>查询租户在指定区域和实例类型的所有标签集合</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityGroupTag</td>
                    <td>删除指定安全组资源实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateSecurityGroupTags</td>
                    <td>为指定的安全组资源实例批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityGroupTag</td>
                    <td>给指定安全组资源实例增加标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityGroupTags</td>
                    <td>查询指定安全组实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityGroupsByTags</td>
                    <td>使用标签过滤实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteSecurityGroupTags</td>
                    <td>为指定的安全组资源实例批量删除标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">对等连接</td>
                    <td>ShowVpcPeering</td>
                    <td>查询对等连接详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpcPeering</td>
                    <td>删除对等连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AcceptVpcPeering</td>
                    <td>租户A名下的VPC申请和租户B的VPC建立对等连接,需要等待租户B接受该请求。此接口用于租户接受其他租户发起的对等连接请求。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcPeerings</td>
                    <td>查询提交请求的租户的所有对等连接。根据过滤条件进行过滤。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpcPeering</td>
                    <td>创建对等连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpcPeering</td>
                    <td>更新对等连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RejectVpcPeering</td>
                    <td>租户A名下的VPC申请和租户B的VPC建立对等连接,需要等待租户B接受该请求。此接口用于租户拒绝其他租户发起的对等连接请求。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询网络IP使用情况</td>
                    <td>ShowNetworkIpAvailabilities</td>
                    <td>显示一个指定网络中的IPv4地址使用情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">流日志</td>
                    <td>UpdateFlowLog</td>
                    <td>更新流日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFlowLog</td>
                    <td>创建流日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlowLog</td>
                    <td>查询流日志详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlowLogs</td>
                    <td>查询提交请求的租户的所有流日志列表,并根据过滤条件进行过滤</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFlowLog</td>
                    <td>删除流日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">流量镜像会话</td>
                    <td>AddSourcesToTrafficMirrorSession</td>
                    <td>流量镜像会话添加镜像源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrafficMirrorSession</td>
                    <td>创建流量镜像会话</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrafficMirrorSession</td>
                    <td>查询流量镜像会话详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTrafficMirrorSession</td>
                    <td>更新流量镜像会话</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrafficMirrorSession</td>
                    <td>删除流量镜像会话</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveSourcesFromTrafficMirrorSession</td>
                    <td>流量镜像会话移除镜像源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTrafficMirrorSessions</td>
                    <td>查询流量镜像会话列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">流量镜像筛选条件</td>
                    <td>ListTrafficMirrorFilters</td>
                    <td>查询流量镜像筛选条件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTrafficMirrorFilter</td>
                    <td>更新流量镜像筛选条件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrafficMirrorFilter</td>
                    <td>创建流量镜像筛选条件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrafficMirrorFilter</td>
                    <td>查询流量镜像筛选条件详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrafficMirrorFilter</td>
                    <td>删除流量镜像筛选条件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">流量镜像筛选规则</td>
                    <td>UpdateTrafficMirrorFilterRule</td>
                    <td>更新流量镜像筛选规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrafficMirrorFilterRule</td>
                    <td>查询流量镜像筛选规则详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrafficMirrorFilterRule</td>
                    <td>创建流量镜像筛选规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrafficMirrorFilterRule</td>
                    <td>删除流量镜像筛选规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTrafficMirrorFilterRules</td>
                    <td>查询流量镜像筛选规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">私有IP</td>
                    <td>DeletePrivateip</td>
                    <td>删除私有IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePrivateip</td>
                    <td>申请私有IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateips</td>
                    <td>查询指定子网下的私有IP列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateip</td>
                    <td>指定ID查询私有IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">端口</td>
                    <td>UpdatePort</td>
                    <td>更新端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePort</td>
                    <td>创建端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPort</td>
                    <td>查询单个端口详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddSecurityGroups</td>
                    <td>端口插入安全组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePort</td>
                    <td>删除端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveSecurityGroups</td>
                    <td>端口移除安全组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPorts</td>
                    <td>查询提交请求的租户的所有端口,单次查询最多返回2000条数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">端口资源标签管理</td>
                    <td>CountPortsByTags</td>
                    <td>使用标签过滤查询端口实例数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreatePortTags</td>
                    <td>为指定的端口批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPortsByTags</td>
                    <td>使用标签过滤查询端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePortTag</td>
                    <td>删除指定端口的标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePortTag</td>
                    <td>给指定端口资源实例增加标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPortTags</td>
                    <td>查询租户在指定Project中实例类型的所有资源标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePortTags</td>
                    <td>为指定的端口资源实例批量删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPortTags</td>
                    <td>查询指定端口的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">网络ACL</td>
                    <td>ShowFirewall</td>
                    <td>查询网络ACL详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFirewall</td>
                    <td>删除网络ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFirewallRules</td>
                    <td>网络ACL更新规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateSubnetFirewall</td>
                    <td>网络ACL绑定子网</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFirewall</td>
                    <td>创建网络ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddFirewallRules</td>
                    <td>网络ACL插入规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFirewall</td>
                    <td>更新网络ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateSubnetFirewall</td>
                    <td>网络ACL解绑子网</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveFirewallRules</td>
                    <td>网络ACL移除规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFirewall</td>
                    <td>查询网络ACL列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">网络ACL资源标签管理</td>
                    <td>BatchCreateFirewallTags</td>
                    <td>为指定的网络ACL资源实例批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFirewallTag</td>
                    <td>删除指定IP地址组资源实例的标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFirewallTag</td>
                    <td>给指定IP地址组资源实例增加标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFirewallTags</td>
                    <td>查询租户在指定Project中实例类型的所有资源标签集合</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountFirewallsByTags</td>
                    <td>使用标签过滤查询ACL实例数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFirewallTags</td>
                    <td>查询指定ACL实例的标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFirewallsByTags</td>
                    <td>使用标签过滤查询ACL实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteFirewallTags</td>
                    <td>为指定的网络ACL资源实例批量删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">路由表</td>
                    <td>ShowRouteTable</td>
                    <td>查询路由表详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRouteTable</td>
                    <td>更新路由表,包括可以更新路由表的名称,描述,以及新增、更新、删除路由条目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRouteTables</td>
                    <td>查询提交请求的帐户的所有路由表列表,并根据过滤条件进行过滤</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRouteTable</td>
                    <td>路由表关联子网。子网关联路由表A后,再关联B,不需要先跟路由表A解关联再关联路由表B</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRouteTable</td>
                    <td>创建路由表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateRouteTable</td>
                    <td>子网解关联路由表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRouteTable</td>
                    <td>删除路由表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">辅助弹性网卡</td>
                    <td>DeleteSubNetworkInterface</td>
                    <td>删除辅助弹性网卡</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubNetworkInterfaces</td>
                    <td>查询辅助弹性网卡列表,单次查询最多返回2000条数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubNetworkInterface</td>
                    <td>创建辅助弹性网卡</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubNetworkInterfacesQuantity</td>
                    <td>查询辅助弹性网卡数目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateSubNetworkInterface</td>
                    <td>批量创建辅助弹性网卡</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubNetworkInterface</td>
                    <td>查询辅助弹性网卡详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubNetworkInterface</td>
                    <td>更新辅助弹性网卡</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowQuota</td>
                    <td>查询单租户在VPC服务下的网络资源配额,包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额,vpn配额等。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
