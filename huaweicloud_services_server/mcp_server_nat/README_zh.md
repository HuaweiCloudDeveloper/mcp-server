# NAT MCP Server 


## Version
v0.1.0

## Overview

NAT MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service NAT. Full-chain management of NAT resources can be carried out based on natural language.

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
                    <td rowspan="6">中转IP标签管理</td>
                    <td>CreateTransitIpTag</td>
                    <td>- 一个中转IP上最多有10个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTransitIpsByTags</td>
                    <td>- 使用标签过滤中转IP实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTransitIpTags</td>
                    <td>- 查询指定中转IP实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTransitIpTag</td>
                    <td>- 幂等接口:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateDeleteTransitIpTags</td>
                    <td>- 为指定中转IP实例批量添加或删除标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTransitIpTags</td>
                    <td>- 查询租户在指定Project和实例类型的所有中转IP标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">公网DNAT规则</td>
                    <td>BatchCreateNatGatewayDnatRules</td>
                    <td>批量创建DNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNatGatewayDnatRule</td>
                    <td>更新指定的DNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNatGatewayDnatRules</td>
                    <td>查询DNAT规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNatGatewayDnatRule</td>
                    <td>查询指定的DNAT规则详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNatGatewayDnatRule</td>
                    <td>创建DNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNatGatewayDnatRule</td>
                    <td>删除指定的DNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">公网NAT网关</td>
                    <td>ShowNatGateway</td>
                    <td>查询指定的公网NAT网关实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNatGateway</td>
                    <td>更新公网NAT网关实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNatGateway</td>
                    <td>创建公网NAT网关实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNatGateway</td>
                    <td>删除公网NAT网关实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNatGateways</td>
                    <td>查询公网NAT网关实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">公网NAT网关标签</td>
                    <td>ListNatGatewayByTag</td>
                    <td>- 使用标签过滤公网NAT网关资源实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateDeleteNatGatewayTag</td>
                    <td>- 为指定公网NAT网关实例批量添加或删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNatGatewayTag</td>
                    <td>- 添加公网NAT网关资源标签。一个资源上最多有10个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNatGatewayTag</td>
                    <td>- 查询租户在指定项目和公网NAT网关实例类型的所有标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNatGatewayTag</td>
                    <td>- 删除指定公网NAT网关资源实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNatGatewayTag</td>
                    <td>- 查询指定公网NAT网关实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">公网SNAT规则</td>
                    <td>DeleteNatGatewaySnatRule</td>
                    <td>删除指定的SNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNatGatewaySnatRule</td>
                    <td>更新指定的SNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNatGatewaySnatRule</td>
                    <td>创建SNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNatGatewaySnatRules</td>
                    <td>查询SNAT规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNatGatewaySnatRule</td>
                    <td>查询指定的SNAT规则详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">私网DNAT规则</td>
                    <td>DeletePrivateDnat</td>
                    <td>删除指定的DNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateDnats</td>
                    <td>查询DNAT规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePrivateDnat</td>
                    <td>创建DNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrivateDnat</td>
                    <td>更新指定的DNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateDnat</td>
                    <td>查询指定的DNAT规则详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">私网NAT中转IP</td>
                    <td>CreateTransitIp</td>
                    <td>创建中转IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTransitIp</td>
                    <td>删除中转IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTransitIps</td>
                    <td>查询中转IP列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTransitIp</td>
                    <td>查询中转IP详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">私网NAT网关</td>
                    <td>CreatePrivateNat</td>
                    <td>创建私网NAT网关实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePrivateNat</td>
                    <td>删除私网NAT网关实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrivateNat</td>
                    <td>更新私网NAT网关实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateNat</td>
                    <td>查询指定的私网NAT网关实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateNats</td>
                    <td>查询私网NAT网关实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">私网NAT网关标签管理</td>
                    <td>CreatePrivateNatTag</td>
                    <td>- 一个私网NAT网关上最多有10个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePrivateNatTag</td>
                    <td>- 幂等接口:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateNatTags</td>
                    <td>- 查询指定私网NAT网关实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateNatTags</td>
                    <td>- 查询租户在指定Project和实例类型的所有私网NAT网关标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateNatsByTags</td>
                    <td>- 使用标签过滤私网NAT网关实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateDeletePrivateNatTags</td>
                    <td>- 为指定私网NAT网关实例批量添加或删除标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">私网SNAT规则</td>
                    <td>CreatePrivateSnat</td>
                    <td>创建SNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateSnats</td>
                    <td>查询SNAT规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePrivateSnat</td>
                    <td>删除指定的SNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrivateSnat</td>
                    <td>更新指定的SNAT规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateSnat</td>
                    <td>查询指定的SNAT规则详情。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
