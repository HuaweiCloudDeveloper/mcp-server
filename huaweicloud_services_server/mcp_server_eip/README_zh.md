# EIP MCP Server 


## Version
v0.1.0

## Overview

EIP MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EIP. Full-chain management of EIP resources can be carried out based on natural language.

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
                    <td rowspan="1">GEIP与实例的绑定关系</td>
                    <td>ListProjectGeipBindings</td>
                    <td>查询GEIP与实例绑定关系的租户列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">OpenStack - 浮动IP</td>
                    <td>NeutronUpdateFloatingIp</td>
                    <td>更新浮动IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronShowFloatingIp</td>
                    <td>查询浮动IP详情,包括浮动IP状态,浮动IP所属路由器ID,浮动IP的外部网络ID等等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronDeleteFloatingIp</td>
                    <td>删除指定的浮动IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronListFloatingIps</td>
                    <td>查询提交请求的租户有权限操作的所有浮动IP地址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NeutronCreateFloatingIp</td>
                    <td>创建浮动IP的外部网络UUID,请使用GET /v2.0/networks?router:external=True或neutron net-external-list方式获取。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">公共池</td>
                    <td>ListPublicipPool</td>
                    <td>全量查询公网IP池列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCommonPools</td>
                    <td>查询公共池列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPublicipPool</td>
                    <td>查询公网IP池详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">共享带宽类型</td>
                    <td>ListShareBandwidthTypes</td>
                    <td>查询指定租户下的共享带宽类型列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">带宽</td>
                    <td>AddPublicipsIntoSharedBandwidth</td>
                    <td>共享带宽插入弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrePaidBandwidth</td>
                    <td>更新带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBandwidth</td>
                    <td>更新带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidths</td>
                    <td>查询带宽列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeBandwidthToPeriod</td>
                    <td>租户按需转包接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSharedBandwidth</td>
                    <td>删除共享带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemovePublicipsFromSharedBandwidth</td>
                    <td>共享带宽移除弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEipBandwidths</td>
                    <td>查询带宽列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBandwidth</td>
                    <td>查询带宽详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSharedBandwidth</td>
                    <td>创建共享带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchModifyBandwidth</td>
                    <td>批量更新带宽,共享带宽和包周期带宽该接口不适用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateSharedBandwidths</td>
                    <td>批量创建共享带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidth</td>
                    <td>查询带宽列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidthsLimit</td>
                    <td>获取EIP带宽限制列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">带宽加油包</td>
                    <td>ListBandwidthPkg</td>
                    <td>查询带宽加油包列表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">弹性公网IP</td>
                    <td>DeletePublicip</td>
                    <td>删除弹性公网IP,绑定状态eip不允许直接删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublicips</td>
                    <td>查询弹性公网IP列表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableNat64</td>
                    <td>弹性公网IP关闭NAT64</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangePublicipToPeriod</td>
                    <td>租户按需转包接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachBatchPublicIp</td>
                    <td>共享带宽批量加入弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPublicip</td>
                    <td>查询弹性公网IP详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountEipAvailableResources</td>
                    <td>IP池用于查询公网可用ip个数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociatePublicips</td>
                    <td>解绑弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableNat64</td>
                    <td>弹性公网IP开启NAT64</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociatePublicips</td>
                    <td>绑定弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachShareBandwidth</td>
                    <td>共享带宽移出弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePublicip</td>
                    <td>申请弹性公网IP,支持IPv4和IPv6。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePrePaidPublicip</td>
                    <td>申请包年包月的弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublicip</td>
                    <td>更新弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachShareBandwidth</td>
                    <td>共享带宽加入弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachBatchPublicIp</td>
                    <td>共享带宽批量移出弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">弹性公网IP标签管理</td>
                    <td>ShowPublicipTags</td>
                    <td>查询指定弹性IP实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePublicipTags</td>
                    <td>为指定的弹性公网IP资源实例批量删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePublicipTag</td>
                    <td>给指定弹性IP资源实例增加标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreatePublicipTags</td>
                    <td>为指定的弹性公网IP资源实例批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublicipsByTags</td>
                    <td>使用标签过滤弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePublicipTag</td>
                    <td>删除指定弹性公网IP的标签信息。其中project_id是项目ID,publicip_id 是要操作的弹性公网IP的id。key是要删除标签的键。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublicipTags</td>
                    <td>查询租户在指定区域和实例类型的所有标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">弹性公网IP辅助接口</td>
                    <td>ShowPublicIpType</td>
                    <td>查询PublicIp类型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountPublicIp</td>
                    <td>查询PublicIp数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountPublicIpInstance</td>
                    <td>查询PublicIp实例数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">批量操作弹性公网IP</td>
                    <td>BatchDisassociatePublicips</td>
                    <td>批量解绑弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePublicIp</td>
                    <td>批量删除弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreatePublicips</td>
                    <td>批量创建弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询Job状态</td>
                    <td>ShowResourcesJobDetail</td>
                    <td>查询Job状态接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">虚拟igw</td>
                    <td>ListTenantVpcIgws</td>
                    <td>查询指定租户下的虚拟igw列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTenantVpcIgw</td>
                    <td>删除虚拟igw</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTenantVpcIgw</td>
                    <td>创建虚拟igw</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTenantVpcIgw</td>
                    <td>修改虚拟igw</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInternalVpcIgw</td>
                    <td>查询虚拟igw详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额管理</td>
                    <td>ListQuotas</td>
                    <td>获取配额信息</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
