# ER MCP Server 


## Version
v0.1.0

## Overview

ER MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ER. Full-chain management of ER resources can be carried out based on natural language.

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
                    <td rowspan="1">Association</td>
                    <td>ListAssociations</td>
                    <td>查询路由关联列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Attachments</td>
                    <td>ListAttachments</td>
                    <td>查询企业路由器实例下的连接列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAttachment</td>
                    <td>查询连接详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAttachment</td>
                    <td>修改连接基本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RejectAttachment</td>
                    <td>拒绝共享连接创建</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AcceptAttachment</td>
                    <td>接受共享连接创建</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">AvailableZone</td>
                    <td>ListAvailabilityZone</td>
                    <td>查询支持创建企业路由器实例的可用区列表,当可用区状态为available时,表示可以创建企业路由器实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">EnterpriseRouterInstance</td>
                    <td>ChangeAvailabilityZone</td>
                    <td>更新企业路由器的可用区信息,企业路由器实例状态为available的时候才能更新。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnterpriseRouters</td>
                    <td>查询企业路由器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnterpriseRouter</td>
                    <td>创建企业路由器实例,如果使能默认关联路由表或使能默认传递路由表,那么系统会默认创建一张路由表,作为默认关联路由表或默认传递路由表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnterpriseRouter</td>
                    <td>更新企业路由器基本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnterpriseRouter</td>
                    <td>查询企业路由器详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnterpriseRouter</td>
                    <td>删除企业路由器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">FlowLog</td>
                    <td>EnableFlowLog</td>
                    <td>开启流日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableFlowLog</td>
                    <td>关闭流日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Propagation</td>
                    <td>ListPropagations</td>
                    <td>查询路由传播列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisablePropagation</td>
                    <td>解绑连接和路由表的传播关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnablePropagation</td>
                    <td>每个连接可以和多个路由表建立传播关系,从该连接学习到的路由会应用到具有传播关系的路由表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Route</td>
                    <td>ListStaticRoutes</td>
                    <td>查询静态路由列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEffectiveRoutes</td>
                    <td>查询有效的路由列表,支持分页查询能力</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStaticRoute</td>
                    <td>创建静态路由</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStaticRoute</td>
                    <td>更新静态路由</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStaticRoute</td>
                    <td>查询静态路由详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStaticRoute</td>
                    <td>删除静态路由</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tags</td>
                    <td>ListProjectTags</td>
                    <td>查询租户在指定项目中指定资源类型下的所有标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateResourceTags</td>
                    <td>为指定实例批量添加标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">VPCAttachment</td>
                    <td>ListVpcAttachments</td>
                    <td>查询企业路由器实例下的VPC连接列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpcAttachment</td>
                    <td>查询VPC连接详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpcAttachment</td>
                    <td>修改VPC连接基本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpcAttachment</td>
                    <td>给ER实例创建VPC连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpcAttachment</td>
                    <td>删除VPC连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">流日志</td>
                    <td>ShowFlowLog</td>
                    <td>查询流日志详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlowLog</td>
                    <td>更新流日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFlowLog</td>
                    <td>删除流日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlowLogs</td>
                    <td>查询提交请求的租户的所有流日志列表,并根据过滤条件进行过滤</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFlowLog</td>
                    <td>创建流日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">资源标签</td>
                    <td>ShowResourceTag</td>
                    <td>查询单个资源上的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResourceTag</td>
                    <td>用于给云服务的多个资源添加标签,每个资源最多可添加10个标签,每次最多支持批量操作20个资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResourceTag</td>
                    <td>用于批量移除云服务多个资源的标签,每个资源最多支持移除10个标签,每次最多支持批量操作20个资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">路由表</td>
                    <td>ListRouteTables</td>
                    <td>查询提交请求的帐户的所有路由表列表,并根据过滤条件进行过滤</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateRouteTable</td>
                    <td>子网解关联路由表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRouteTable</td>
                    <td>创建路由表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRouteTable</td>
                    <td>删除路由表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRouteTable</td>
                    <td>路由表关联子网。子网关联路由表A后,再关联B,不需要先跟路由表A解关联再关联路由表B</td>
                    <td>To be tested</td>
                </tr>
                <tr>
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
                    <td rowspan="1">配额</td>
                    <td>ShowQuotas</td>
                    <td>查询当前项目下资源配额情况。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
