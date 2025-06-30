# ELB MCP Server 


## Version
v0.1.0

## Overview

ELB MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ELB. Full-chain management of ELB resources can be carried out based on natural language.

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
                    <td rowspan="4">IP地址组</td>
                    <td>ShowIpGroupRelatedListeners</td>
                    <td>查询IP地址组关联的监听器列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteIpList</td>
                    <td>批量删除IP地址组的IP列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIpGroups</td>
                    <td>查询IP地址组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIpList</td>
                    <td>添加新的IP地址到IP地址组的IP列表信息,或更新已有IP地址的描述。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">VpnGateway</td>
                    <td>ListAvailabilityZones</td>
                    <td>查询VPN网关可用区</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">主备后端服务器组</td>
                    <td>ShowMasterSlavePool</td>
                    <td>主备后端服务器组详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMasterSlavePools</td>
                    <td>主备后端服务器组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMasterSlavePool</td>
                    <td>创建主备后端服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMasterSlavePool</td>
                    <td>删除主备后端服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">云日志</td>
                    <td>ShowLogtank</td>
                    <td>云日志详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogtanks</td>
                    <td>查询云日志列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">云日志操作</td>
                    <td>DeleteLogtank</td>
                    <td>解绑指定Topic绑定的云日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogtank</td>
                    <td>为指定Topic绑定一个云日志,用于记录主题消息发送状态等信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogtank</td>
                    <td>更新指定Topic绑定的云日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">任务中心API</td>
                    <td>ListJobs</td>
                    <td>查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务,该API用于查询这些任务的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">健康检查</td>
                    <td>CreateHealthMonitor</td>
                    <td>创建健康检查。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHealthmonitors</td>
                    <td>根据指定ID查询健康检查详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHealthMonitor</td>
                    <td>删除健康检查。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHealthMonitor</td>
                    <td>查询健康检查详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHealthmonitors</td>
                    <td>查询健康检查列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHealthMonitor</td>
                    <td>更新健康检查。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">后端云服务器</td>
                    <td>UpdateMember</td>
                    <td>更新后端云服务器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMembers</td>
                    <td>查询属于某个后端云服务器组的后端云服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMember</td>
                    <td>删除后端云服务器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMember</td>
                    <td>根据指定ID查询后端云服务器详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">后端云服务器组</td>
                    <td>UpdatePool</td>
                    <td>更新后端云服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPool</td>
                    <td>根据指定ID查询后端云服务器组详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPools</td>
                    <td>查询后端云服务器组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePool</td>
                    <td>创建后端云服务器组。将多个后端云服务器添加到后端云服务器组中后,请求会在后端云服务器间按后端云服务器组的负载均衡算法和后端云服务器的权重来做请求分发。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePool</td>
                    <td>删除后端云服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">后端服务器</td>
                    <td>CreateMemberHealthCheckJob</td>
                    <td>创建后端服务器检测任务。包括后端服务器的配置、ACL规则和安全组规则检查。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllMembers</td>
                    <td>查询当前项目下的后端服务器列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMember</td>
                    <td>创建后端服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateMembers</td>
                    <td>在指定pool下批量创建后端服务器。一次最多创建200个。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMemberHealthCheckJob</td>
                    <td>查询后端服务器检测任务的结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">后端服务器组</td>
                    <td>DeletePoolCascade</td>
                    <td>级联删除后端服务器组,包含在此后端服务器组下的所有后端服务器和健康检查也将被删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">回收站</td>
                    <td>UpdateRecycleBinEnable</td>
                    <td>开启或关闭回收站功能。开启后删除的LB可以进入回收站,否则将不进入回收站而是直接被删除无法恢复。关闭回收站前需要先将回收站中的实例还原或销毁。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecycleBinLoadBalancers</td>
                    <td>查询回收站负载均衡器列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRecycleLoadBalancer</td>
                    <td>销毁回收站负载均衡器。销毁后无法再还原。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRecycleBinPolicy</td>
                    <td>更新回收站的配置。若回收站未开启,则更新会报错。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreLoadbalancer</td>
                    <td>从回收站中还原负载均衡器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecycleBin</td>
                    <td>查询回收站的配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">地址组管理</td>
                    <td>UpdateIpGroup</td>
                    <td>修改ip地址组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIpGroup</td>
                    <td>创建ip地址组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIpGroup</td>
                    <td>查询ip地址组明细</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIpGroup</td>
                    <td>删除ip地址组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">安全策略</td>
                    <td>ShowSecurityPolicy</td>
                    <td>查询自定义安全策略详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityPolicies</td>
                    <td>查询自定义安全策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityPolicy</td>
                    <td>删除自定义安全策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityPolicy</td>
                    <td>更新自定义安全策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSystemSecurityPolicies</td>
                    <td>查询系统安全策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityPolicy</td>
                    <td>创建自定义安全策略。用于在创建HTTPS监听器时,请求参数中指定security_policy_id来设置监听器的自定义安全策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">引擎版本和规格</td>
                    <td>ListFlavors</td>
                    <td>查询数据库规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询版本操作</td>
                    <td>ListApiVersions</td>
                    <td>查询标签管理服务的API版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">标签管理</td>
                    <td>BatchDeleteListenerTags</td>
                    <td>批量删除监听器标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowListenerTags</td>
                    <td>查询指定监听器的所有标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteLoadbalancerTags</td>
                    <td>批量删除负载均衡器标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListListenerTags</td>
                    <td>查询指定项目下所有监听器的标签列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateListenerTags</td>
                    <td>给指定监听器添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateListenerTags</td>
                    <td>批量添加监听器标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLoadbalancerTags</td>
                    <td>删除负载均衡器的某个key对应的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoadbalancerTags</td>
                    <td>查询指定项目下所有负载均衡器的标签列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteListenerTags</td>
                    <td>删除监听器的某个key对应的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoadbalancersByTags</td>
                    <td>根据标签过滤查询负载均衡实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLoadbalancerTags</td>
                    <td>查询指定负载均衡器的所有标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListListenersByTags</td>
                    <td>根据标签过滤查询监听器实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateLoadbalancerTags</td>
                    <td>批量添加负载均衡器标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLoadbalancerTags</td>
                    <td>给指定负载均衡器添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">特性配置</td>
                    <td>ListLoadbalancerFeature</td>
                    <td>查询指定ELB实例的特性配置情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFeatureConfigs</td>
                    <td>查询当前租户ELB服务的特性配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">白名单</td>
                    <td>UpdateWhitelist</td>
                    <td>更新白名单。可以打开或关闭白名单,或更新访问控制的IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWhitelist</td>
                    <td>根据指定ID查询白名单详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWhitelists</td>
                    <td>查询白名单,支持过滤查询和分页查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWhitelist</td>
                    <td>删除白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWhitelist</td>
                    <td>创建白名单,控制监听器的访问权限。若开启了白名单功能,只有白名单中放通的IP可以访问该监听器的后端服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">监听器</td>
                    <td>DeleteListenerForce</td>
                    <td>删除监听器且级联删除其下子资源(删除监听器、转发策略等,解绑后端服务器组)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListListeners</td>
                    <td>查询监听器列表。支持过滤查询和分页查询。可以通过监听器ID、协议类型、监听端口号、关联的后端云服务器的IP等查询监听器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateListener</td>
                    <td>更新监听器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateListener</td>
                    <td>创建与负载均衡器绑定的监听器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteListener</td>
                    <td>删除监听器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowListener</td>
                    <td>根据指定ID查询监听器详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">规格</td>
                    <td>ShowFlavor</td>
                    <td>查询规格的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">证书</td>
                    <td>ShowCertificatePrivateKeyEcho</td>
                    <td>查询证书私钥回显开关当前的状态,开启或关闭。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificatePrivateKeyEcho</td>
                    <td>开启或关闭证书私钥字段回显开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">证书管理</td>
                    <td>ListCertificates</td>
                    <td>查询证书列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCertificate</td>
                    <td>删除证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCertificate</td>
                    <td>修改证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificate</td>
                    <td>创建证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificate</td>
                    <td>查询证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">负载均衡器</td>
                    <td>BatchAddAvailableZones</td>
                    <td>给负载均衡器新增可用区。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoadbalancers</td>
                    <td>查询负载均衡器列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLoadbalancer</td>
                    <td>创建私网类型的增强型负载均衡器。创建成功后,该接口会返回创建的增强型负载均衡器的ID、所属子网ID、负载均衡器IP等详细信息。若要创建公网类型的增强型负载均衡器,还需调用创建浮动IP的接口,将浮动IP与私网负载均衡器的vip_port_id绑定。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLoadbalancersStatus</td>
                    <td>查询负载均衡器状态树。可通过该接口查询负载均衡器关联的监听器、后端云服务器组、后端云服务器、健康检查、转发策略、转发规则的主要信息,了解负载均衡器下资源的拓扑情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLoadbalancer</td>
                    <td>更新负载均衡器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CloneLoadbalancer</td>
                    <td>复制已有的负载均衡器实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRemoveAvailableZones</td>
                    <td>移除负载均衡器的可用区。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLoadBalancerCascade</td>
                    <td>删除负载均衡器且级联删除其下子资源(删除负载均衡器及其绑定的监听器、后端服务器等一系列资源)。以及根据需要删除或解绑后端服务器组和LB关联的EIP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeLoadbalancer</td>
                    <td>升级负载均衡器类型。支持将共享型ELB升级为独享型ELB,但不支持独享型降级为共享型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLoadBalancer</td>
                    <td>删除负载均衡器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateLoadBalancers</td>
                    <td>批量创建独享型或者共享型负载均衡器,包括按需及包周期计费负载均衡器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLoadBalancerStatus</td>
                    <td>查询负载均衡器状态树,包括负载均衡器及其关联的子资源的状态信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLoadBalancerForce</td>
                    <td>删除负载均衡器且级联删除其下子资源(删除负载均衡器及其绑定的监听器、后端服务器组、后端服务器等一系列资源)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLoadBalancer</td>
                    <td>查询负载均衡器详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeLoadbalancerChargeMode</td>
                    <td>负载均衡器计费模式变更,当前支持的计费模式变更为:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资源配额功能</td>
                    <td>ListQuotaDetails</td>
                    <td>查询用户的资源配额,包括终端节点服务和终端节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">转发策略</td>
                    <td>CreateL7policy</td>
                    <td>创建listener关联的转发策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdatePoliciesPriority</td>
                    <td>批量更新转发策略的优先级。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowL7Policy</td>
                    <td>查询七层转发策略详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteL7policy</td>
                    <td>删除转发策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListL7Policies</td>
                    <td>查询七层转发策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateL7Policy</td>
                    <td>更新七层转发策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateL7policies</td>
                    <td>更新转发策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">转发规则</td>
                    <td>ListL7rules</td>
                    <td>查询指定转发策略下关联的转发规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateL7Rule</td>
                    <td>更新七层转发规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateL7Rule</td>
                    <td>创建七层转发规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowL7rule</td>
                    <td>根据指定ID查询某转发策略下关联的转发规则详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteL7rule</td>
                    <td>删除转发规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowQuota</td>
                    <td>查询单租户在VPC服务下的网络资源配额,包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额,vpn配额等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像任务</td>
                    <td>ShowJob</td>
                    <td>该接口为扩展接口,主要用于查询异步接口执行情况,比如查询导出镜像任务的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">镜像共享</td>
                    <td>BatchUpdateMembers</td>
                    <td>该接口为扩展接口,主要用于用户接受或者拒绝多个共享镜像时批量更新镜像成员的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteMembers</td>
                    <td>该接口为扩展接口,主要用于取消镜像共享。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">预占IP</td>
                    <td>CountPreoccupyIpNum</td>
                    <td>计算以下几种场景的预占用IP数量:</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
