# VPCEP MCP Server 


## Version
v0.1.0

## Overview

VPCEP MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VPCEP. Full-chain management of VPCEP resources can be carried out based on natural language.

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
                    <td rowspan="3">TAG功能</td>
                    <td>BatchAddOrRemoveResourceInstance</td>
                    <td>为指定Endpoint Service或Endpoint批量添加或删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryProjectResourceTags</td>
                    <td>根据租户ID和资源类型,获取租户下资源的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceInstances</td>
                    <td>使用标签过滤查询租户下资源的实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">版本管理</td>
                    <td>ListVersionDetails</td>
                    <td>查询VPC终端节点接口版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSpecifiedVersionDetails</td>
                    <td>查询指定VPC终端节点接口版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">终端节点功能</td>
                    <td>UpdateEndpointPolicy</td>
                    <td>修改终端节点策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEndpoint</td>
                    <td>删除终端节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEndpointPolicy</td>
                    <td>删除网关型终端节点策略,该接口待下线,不建议使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpointWhite</td>
                    <td>更新或删除允许访问终端节点的白名单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpointRoutetable</td>
                    <td>修改终端节点的路由表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpointInfoDetails</td>
                    <td>查询终端节点的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpoints</td>
                    <td>查询当前用户下的终端节点的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEndpoint</td>
                    <td>创建终端节点,以便访问终端节点服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">终端节点服务功能</td>
                    <td>DeleteEndpointService</td>
                    <td>删除终端节点服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceConnections</td>
                    <td>查询连接当前用户下的某一个终端节点服务的连接列表。marker_id是连接的唯一标识。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeEndpointService</td>
                    <td>升级终端节点服务,使终端节点服务支持创建专业型终端节点实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddOrRemoveServicePermissions</td>
                    <td>批量添加或移除当前用户下终端节点服务的白名单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServicePublicDetails</td>
                    <td>查询公共终端节点服务的列表,公共终端节点服务是所有用户可见且可连接的终端节点服务,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRemoveEndpointServicePermissions</td>
                    <td>批量删除当前用户下终端节点服务的白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpointService</td>
                    <td>修改终端节点服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEndpointService</td>
                    <td>创建终端节点服务,允许其他用户创建终端节点连接您创建的终端节点服务,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServicePermissionsDetails</td>
                    <td>查询当前用户下终端节点服务的白名单列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddEndpointServicePermissions</td>
                    <td>批量添加当前用户下终端节点服务的白名单,支持添加描述信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpointService</td>
                    <td>查询当前用户下的终端节点服务的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpointServicePermissionDesc</td>
                    <td>更新当前用户下终端节点服务白名单的描述信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceDescribeDetails</td>
                    <td>查询终端节点服务的概要信息, 此接口是供创建终端节点的用户来查询需要连接的终端节点服务信息。 此接口既可以方便其他用户查询到您的终端节点服务概要信息, 又可以避免您的终端节点服务的细节信息暴露给其他用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpointConnectionsDesc</td>
                    <td>更新终端节点服务连接的终端节点的描述。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AcceptOrRejectEndpoint</td>
                    <td>接受或者拒绝终端节点连接到当前的终端节点服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceDetails</td>
                    <td>查询终端节点服务的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpointServiceName</td>
                    <td>修改终端节点服务名称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资源配额功能</td>
                    <td>ListQuotaDetails</td>
                    <td>查询用户的资源配额,包括终端节点服务和终端节点。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
