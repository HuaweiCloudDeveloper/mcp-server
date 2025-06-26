# VPN MCP Server 


## Version
v0.1.0

## Overview

VPN MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VPN. Full-chain management of VPN resources can be carried out based on natural language.

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
                    <td rowspan="5">ClientCaCertificate</td>
                    <td>CheckClientCaCertificate</td>
                    <td>创建服务端时,可以先调用客户端CA的预校验API,检查CA的合法性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClientCa</td>
                    <td>修改客户端CA证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportClientCa</td>
                    <td>导入客户端 CA 证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClientCa</td>
                    <td>删除客户端CA证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClientCa</td>
                    <td>查询客户端CA证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">ConnectionMonitor</td>
                    <td>ListConnectionMonitors</td>
                    <td>查询VPN连接监控列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConnectionMonitor</td>
                    <td>根据VPN连接监控的ID,查询指定的VPN连接监控</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnectionMonitor</td>
                    <td>根据VPN连接监控的ID,删除指定的VPN连接监控</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnectionMonitor</td>
                    <td>创建VPN连接监控</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">CustomerGateway</td>
                    <td>ShowCgw</td>
                    <td>根据对端网关ID,查询指定的对端网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCgw</td>
                    <td>根据对端网关ID,删除指定的对端网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCgw</td>
                    <td>创建租户用于与VPN网关相连的对端网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCgw</td>
                    <td>根据对端网关ID,更新指定的对端网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCgws</td>
                    <td>查询对端网关列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">P2cVpnGateway</td>
                    <td>DeleteP2cVgwConnection</td>
                    <td>断开P2C VPN网关连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListP2cVgwAvailabilityZones</td>
                    <td>查询P2C VPN网关可用区</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListP2cVgwConnections</td>
                    <td>List p2c vpn gateway connections</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListP2cVgws</td>
                    <td>查询P2C VPN网关列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowP2cVgw</td>
                    <td>根据P2C VPN网关ID,查询指定的VPN网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateP2cVgw</td>
                    <td>根据P2C VPN网关ID,更新指定的P2C VPN网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Tags</td>
                    <td>ShowResourceTags</td>
                    <td>查询指定实例的标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateResourceTags</td>
                    <td>为指定实例批量添加标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourcesByTags</td>
                    <td>根据标签查询资源实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectTags</td>
                    <td>查询租户在指定项目中指定资源类型下的所有标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteResourceTags</td>
                    <td>为指定实例批量删除标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountResourcesByTags</td>
                    <td>根据标签查询资源实例数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">VpnAccessPolicy</td>
                    <td>UpdateVpnAccessPolicy</td>
                    <td>修改VPN访问策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpnAccessPolicy</td>
                    <td>删除VPN访问策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpnAccessPolicies</td>
                    <td>查询VPN访问策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpnAccessPolicy</td>
                    <td>创建VPN访问策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpnAccessPolicy</td>
                    <td>查询VPN访问策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">VpnConnection</td>
                    <td>ShowVpnConnection</td>
                    <td>根据连接ID,查询指定的VPN连接的参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpnConnection</td>
                    <td>根据连接ID,更新指定的VPN连接的参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetVpnConnection</td>
                    <td>根据连接ID,重置指定VPN连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpnConnection</td>
                    <td>创建VPN连接,连接VPN网关与对端网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpnConnectionLog</td>
                    <td>根据连接ID,查询指定的VPN连接日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpnConnections</td>
                    <td>查询VPN连接列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpnConnection</td>
                    <td>根据连接ID,删除指定的VPN连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">VpnConnectionsLogConfig</td>
                    <td>ShowVpnConnectionsLogConfig</td>
                    <td>查询VPN连接日志配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpnConnectionsLogConfig</td>
                    <td>删除VPN连接日志配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpnConnectionsLogConfig</td>
                    <td>更新VPN连接日志配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">VpnGateway</td>
                    <td>ShowVgw</td>
                    <td>根据VPN网关ID,查询指定的VPN网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListExtendedAvailabilityZones</td>
                    <td>查询VPN网关可用区</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpnGatewayRoutingTable</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePostpaidVgwSpecification</td>
                    <td>对单个网关规格进行修改,可以升配或降配</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailabilityZones</td>
                    <td>查询VPN网关可用区</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVgw</td>
                    <td>创建一个VPN网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVgw</td>
                    <td>根据VPN网关ID,更新指定的VPN网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVgws</td>
                    <td>查询VPN网关列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVgw</td>
                    <td>根据VPN网关ID,删除指定的VPN网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">VpnGatewayCertificate</td>
                    <td>ShowVpnGatewayCertificate</td>
                    <td>根据VPN网关ID,查询所指定的VPN网关证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVgwCertificate</td>
                    <td>更新租户VPN网关所使用的证书,包括签名证书、签名私钥、加密证书、加密私钥和CA证书链。当前只支持国密证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVgwCertificate</td>
                    <td>导入租户VPN网关所使用的证书,包括签名证书、签名私钥、加密证书、加密私钥和CA证书链。当前只支持国密证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">VpnQuota</td>
                    <td>ShowQuotasInfo</td>
                    <td>查询指定租户的配额</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">VpnServer</td>
                    <td>ListVpnServersByVgw</td>
                    <td>查询一个网关下的服务端信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpnServer</td>
                    <td>更新指定VPN 服务端</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportClientConfig</td>
                    <td>导出客户端配置信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpnServer</td>
                    <td>创建一个VPN 服务端</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpnServersByProject</td>
                    <td>查询租户下的所有服务端信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">VpnUser</td>
                    <td>ListVpnUsers</td>
                    <td>查询VPN用户列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpnUser</td>
                    <td>修改VPN用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpnUser</td>
                    <td>创建VPN用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateVpnUsers</td>
                    <td>批量创建P2C VPN用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpnUserPassword</td>
                    <td>修改VPN用户密码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpnUser</td>
                    <td>查询VPN用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpnUser</td>
                    <td>删除VPN用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetVpnUserPassword</td>
                    <td>重置VPN用户密码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteVpnUsers</td>
                    <td>批量删除P2C VPN用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">VpnUserGroup</td>
                    <td>AddVpnUsersToGroup</td>
                    <td>添加VPN用户到组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpnUserGroup</td>
                    <td>创建VPN用户组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpnUserGroups</td>
                    <td>查询VPN用户组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpnUserGroup</td>
                    <td>删除VPN用户组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpnUserGroup</td>
                    <td>修改VPN用户组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpnUsersInGroup</td>
                    <td>查询组内VPN用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveVpnUsersFromGroup</td>
                    <td>删除组内VPN用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpnUserGroup</td>
                    <td>查询VPN用户组</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
