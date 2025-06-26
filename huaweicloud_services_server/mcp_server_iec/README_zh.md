# IEC MCP Server 


## Version
v0.1.0

## Overview

IEC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IEC. Full-chain management of IEC resources can be carried out based on natural language.

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
                    <td rowspan="1">Misc</td>
                    <td>ListQuota</td>
                    <td>查询当前账号的资源共享配额信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">VPC</td>
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
                    <td rowspan="2">port</td>
                    <td>AttachVipBandwidth</td>
                    <td>IPv6虚拟IP或者IPv6私网IP绑定带宽,支持公网访问。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachVipBandwidth</td>
                    <td>IPv6虚拟IP或者IPv6私网IP解绑带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">子网</td>
                    <td>UpdateSubnet</td>
                    <td>更新子网。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubnet</td>
                    <td>删除子网</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRelatedRoutetables</td>
                    <td>查询子网关联的路由表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubnets</td>
                    <td>查询子网列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubnet</td>
                    <td>创建子网。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubnet</td>
                    <td>查询子网详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">安全组</td>
                    <td>ListSecurityGroups</td>
                    <td>查询某租户下的安全组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityGroup</td>
                    <td>查询单个安全组详情</td>
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
                    <td rowspan="4">安全组规则</td>
                    <td>DeleteSecurityGroupRule</td>
                    <td>删除安全组规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityGroupRule</td>
                    <td>创建安全组规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityGroupRules</td>
                    <td>查询安全组规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityGroupRule</td>
                    <td>查询单个安全组规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">实例管理</td>
                    <td>BatchStopInstance</td>
                    <td>批量停止实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">密钥对</td>
                    <td>ShowKeypair</td>
                    <td>查询密钥信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">密钥对管理</td>
                    <td>ListKeypairs</td>
                    <td>查询SSH密钥对列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKeypair</td>
                    <td>删除SSH密钥对。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKeypair</td>
                    <td>创建和导入SSH密钥对</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">带宽</td>
                    <td>ListBandwidths</td>
                    <td>查询带宽列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidthTypes</td>
                    <td>查询共享带宽类型列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBandwidth</td>
                    <td>删除带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBandwidth</td>
                    <td>查询带宽详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBandwidth</td>
                    <td>更新带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">引擎版本和规格</td>
                    <td>ListFlavors</td>
                    <td>查询数据库规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">弹性公网IP</td>
                    <td>ListPublicIps</td>
                    <td>获取弹性公网IP列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePublicIp</td>
                    <td>根据用户的请求内容,创建弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePublicIp</td>
                    <td>根据弹性公网IP的ID,删除对应的弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublicIp</td>
                    <td>更新弹性公网IP的信息,主要用于解绑和绑定EIP和VIP之间的关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPublicIp</td>
                    <td>获取弹性公网IP的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">独享实例管理</td>
                    <td>CreateInstance</td>
                    <td>创建WAF独享引擎实例。独享模式支持的局点包括:华东-青岛、中东-利雅得、华北-北京一、华北-北京四、华北-乌兰察布一、华东-上海一、华东-上海二、华南-广州、华南-深圳、中国-香港、西南-贵阳一、亚太-曼谷、 亚太-新加坡、非洲约翰内斯堡、土耳其-伊斯坦布尔;普通租户类独享支持的局点:华北-北京四、华东-上海一、华南-广州、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>查询WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">生命周期管理</td>
                    <td>ListInstances</td>
                    <td>查询租户的实例列表,支持按照条件查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstance</td>
                    <td>修改实例的名称和描述信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">端口</td>
                    <td>UpdatePort</td>
                    <td>更新端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPort</td>
                    <td>查询单个端口详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPorts</td>
                    <td>查询提交请求的租户的所有端口,单次查询最多返回2000条数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePort</td>
                    <td>创建端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePort</td>
                    <td>删除端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">网络ACL</td>
                    <td>ShowFirewall</td>
                    <td>查询网络ACL详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFirewall</td>
                    <td>创建网络ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFirewall</td>
                    <td>删除网络ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFirewalls</td>
                    <td>查询网络ACL列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFirewall</td>
                    <td>更新网络ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFirewallRule</td>
                    <td>更新网络ACL规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">路由表</td>
                    <td>DisassociateSubnet</td>
                    <td>路由表解关联子网</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateSubnet</td>
                    <td>路由表关联子网</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRoutes</td>
                    <td>删除路由</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRoutes</td>
                    <td>更新路由信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRoutes</td>
                    <td>查询路由列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRoutetables</td>
                    <td>查询路由列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRoutes</td>
                    <td>创建路由</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRoutetable</td>
                    <td>更新路由表基本信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRoutetable</td>
                    <td>查询路由表详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRoutetable</td>
                    <td>删除路由表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRoutetable</td>
                    <td>创建路由表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">边缘业务</td>
                    <td>CreateDeployment</td>
                    <td>为方便您的统一管理,以及跨边缘站点管理资源,IEC基于业务场景角度,定义了边缘业务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeCloud</td>
                    <td>查询边缘业务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteDeployment</td>
                    <td>执行部署计划,创建一个边缘业务。单租户默认可创建10个边缘业务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeCloud</td>
                    <td>删除边缘业务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandEdgecloud</td>
                    <td>执行部署计划,对边缘业务进行扩容操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeCloud</td>
                    <td>查询边缘业务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">边缘实例</td>
                    <td>DeleteNics</td>
                    <td>删除网卡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddNics</td>
                    <td>添加网卡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeOs</td>
                    <td>切换边缘实例操作系统,支持边缘实例创建成功后,保持ip、数据盘不变的情况下重装操作系统。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartInstance</td>
                    <td>批量操作启动边缘实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstances</td>
                    <td>批量删除边缘实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRebootInstance</td>
                    <td>批量重启边缘实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">边缘硬盘</td>
                    <td>ListVolume</td>
                    <td>查询硬盘列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVolumeTypes</td>
                    <td>查询硬盘类型列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVolume</td>
                    <td>查询硬盘详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">边缘站点</td>
                    <td>ListSites</td>
                    <td>查询边缘站点列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">边缘镜像</td>
                    <td>DeleteImage</td>
                    <td>将指定ID的边缘私有镜像删除</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudImages</td>
                    <td>查询租户在某个云Region的可见镜像列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImage</td>
                    <td>查询镜像详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebuildImage</td>
                    <td>重试边缘镜像任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">部署管理</td>
                    <td>ListDeployments</td>
                    <td>查询部署列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeployment</td>
                    <td>删除应用部署</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">镜像</td>
                    <td>ListImages</td>
                    <td>根据不同条件查询镜像列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateImage</td>
                    <td>本接口用于制作私有镜像,支持:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterImage</td>
                    <td>该接口用于将镜像文件注册为云平台未初始化的私有镜像。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
