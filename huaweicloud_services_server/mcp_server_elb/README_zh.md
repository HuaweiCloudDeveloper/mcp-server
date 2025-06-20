# ELB MCP Server 

## 版本信息
v0.1.0

## 产品描述

ELB MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务ELB交互的能力。可以基于自然语言对ELB资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| API版本信息 | ListApiVersions | 返回ELB当前所有可用的API版本。 | To be tested |
| IP地址组 | UpdateIpGroup | 更新IP地址组,只支持全量更新IP。即IP地址组中的ip_list将被全量覆盖,不在请求参数中的IP地址将被移除。 | To be tested |
|  | ShowIpGroupRelatedListeners | 查询IP地址组关联的监听器列表。 | To be tested |
|  | BatchDeleteIpList | 批量删除IP地址组的IP列表信息。 | To be tested |
|  | CreateIpGroup | 创建IP地址组。输入的ip可为ip地址、CIDR子网或者ip地址段,格式为ip-ip,例如10.12.3.1-10.12.3.10,支持IPV4和IPV6。 | To be tested |
|  | ListIpGroups | 查询IP地址组列表。 | To be tested |
|  | ShowIpGroup | 获取IP地址组详情。 | To be tested |
|  | UpdateIpList | 添加新的IP地址到IP地址组的IP列表信息,或更新已有IP地址的描述。 | To be tested |
|  | DeleteIpGroup | 删除ip地址组。 | To be tested |
| 主备后端服务器组 | ShowMasterSlavePool | 主备后端服务器组详情。 | To be tested |
|  | ListMasterSlavePools | 主备后端服务器组列表。 | To be tested |
|  | CreateMasterSlavePool | 创建主备后端服务器组。 | To be tested |
|  | DeleteMasterSlavePool | 删除主备后端服务器组。 | To be tested |
| 云日志 | ShowLogtank | 云日志详情。 | To be tested |
|  | DeleteLogtank | 删除云日志。 | To be tested |
|  | CreateLogtank | 创建云日志。 | To be tested |
|  | ListLogtanks | 查询云日志列表。 | To be tested |
|  | UpdateLogtank | 更新云日志。 | To be tested |
| 健康检查 | CreateHealthMonitor | 创建健康检查。 | To be tested |
|  | ShowHealthmonitors | 根据指定ID查询健康检查详情。 | To be tested |
|  | DeleteHealthMonitor | 删除健康检查。 | To be tested |
|  | ShowHealthMonitor | 查询健康检查详情。 | To be tested |
|  | ListHealthmonitors | 查询健康检查列表 | To be tested |
|  | UpdateHealthMonitor | 更新健康检查。 | To be tested |
| 可用区 | ListAvailabilityZones | 返回租户创建LB时可使用的可用区集合列表情况。 | To be tested |
| 后端云服务器 | UpdateMember | 更新后端云服务器 | To be tested |
|  | ListMembers | 查询属于某个后端云服务器组的后端云服务器。 | To be tested |
|  | DeleteMember | 删除后端云服务器 | To be tested |
|  | ShowMember | 根据指定ID查询后端云服务器详情。 | To be tested |
| 后端云服务器组 | UpdatePool | 更新后端云服务器组。 | To be tested |
|  | ShowPool | 根据指定ID查询后端云服务器组详情。 | To be tested |
|  | ListPools | 查询后端云服务器组列表。 | To be tested |
|  | CreatePool | 创建后端云服务器组。将多个后端云服务器添加到后端云服务器组中后,请求会在后端云服务器间按后端云服务器组的负载均衡算法和后端云服务器的权重来做请求分发。 | To be tested |
|  | DeletePool | 删除后端云服务器组。 | To be tested |
| 后端服务器 | CreateMemberHealthCheckJob | 创建后端服务器检测任务。包括后端服务器的配置、ACL规则和安全组规则检查。 | To be tested |
|  | ListAllMembers | 查询当前项目下的后端服务器列表。 | To be tested |
|  | CreateMember | 创建后端服务器。 | To be tested |
|  | BatchCreateMembers | 在指定pool下批量创建后端服务器。一次最多创建200个。 | To be tested |
|  | BatchUpdateMembers | 在指定pool下批量更新后端服务器。一次最多添加200个。 | To be tested |
|  | ShowMemberHealthCheckJob | 查询后端服务器检测任务的结果。 | To be tested |
|  | BatchDeleteMembers | 在指定pool下批量删除后端服务器。一次最多添加200个。 | To be tested |
| 后端服务器组 | DeletePoolCascade | 级联删除后端服务器组,包含在此后端服务器组下的所有后端服务器和健康检查也将被删除。 | To be tested |
| 回收站 | UpdateRecycleBinEnable | 开启或关闭回收站功能。开启后删除的LB可以进入回收站,否则将不进入回收站而是直接被删除无法恢复。关闭回收站前需要先将回收站中的实例还原或销毁。 | To be tested |
|  | ListRecycleBinLoadBalancers | 查询回收站负载均衡器列表。 | To be tested |
|  | DeleteRecycleLoadBalancer | 销毁回收站负载均衡器。销毁后无法再还原。 | To be tested |
|  | UpdateRecycleBinPolicy | 更新回收站的配置。若回收站未开启,则更新会报错。 | To be tested |
|  | RestoreLoadbalancer | 从回收站中还原负载均衡器 | To be tested |
|  | ShowRecycleBin | 查询回收站的配置 | To be tested |
| 安全策略 | ShowSecurityPolicy | 查询自定义安全策略详情。 | To be tested |
|  | ListSecurityPolicies | 查询自定义安全策略列表。 | To be tested |
|  | DeleteSecurityPolicy | 删除自定义安全策略。 | To be tested |
|  | UpdateSecurityPolicy | 更新自定义安全策略。 | To be tested |
|  | ListSystemSecurityPolicies | 查询系统安全策略列表。 | To be tested |
|  | CreateSecurityPolicy | 创建自定义安全策略。用于在创建HTTPS监听器时,请求参数中指定security_policy_id来设置监听器的自定义安全策略。 | To be tested |
| 异步任务 | ListJobs | 用于查询实例导出、实例复制、实例升级等异步接口任务的状态。 | To be tested |
|  | ShowJob | 用于查询模板导入、实例复制、实例升级等异步接口任务的状态 | To be tested |
| 标签管理 | BatchDeleteListenerTags | 批量删除监听器标签。 | To be tested |
|  | ShowListenerTags | 查询指定监听器的所有标签信息。 | To be tested |
|  | BatchDeleteLoadbalancerTags | 批量删除负载均衡器标签。 | To be tested |
|  | ListListenerTags | 查询指定项目下所有监听器的标签列表 | To be tested |
|  | CreateListenerTags | 给指定监听器添加标签。 | To be tested |
|  | BatchCreateListenerTags | 批量添加监听器标签。 | To be tested |
|  | DeleteLoadbalancerTags | 删除负载均衡器的某个key对应的标签。 | To be tested |
|  | ListLoadbalancerTags | 查询指定项目下所有负载均衡器的标签列表 | To be tested |
|  | DeleteListenerTags | 删除监听器的某个key对应的标签。 | To be tested |
|  | ListLoadbalancersByTags | 根据标签过滤查询负载均衡实例。 | To be tested |
|  | ShowLoadbalancerTags | 查询指定负载均衡器的所有标签信息 | To be tested |
|  | ListListenersByTags | 根据标签过滤查询监听器实例。 | To be tested |
|  | BatchCreateLoadbalancerTags | 批量添加负载均衡器标签。 | To be tested |
|  | CreateLoadbalancerTags | 给指定负载均衡器添加标签。 | To be tested |
| 特性配置 | ListLoadbalancerFeature | 查询指定ELB实例的特性配置情况。 | To be tested |
|  | ListFeatureConfigs | 查询当前租户ELB服务的特性配置。 | To be tested |
| 白名单 | UpdateWhitelist | 更新白名单。可以打开或关闭白名单,或更新访问控制的IP。 | To be tested |
|  | ShowWhitelist | 根据指定ID查询白名单详情。 | To be tested |
|  | ListWhitelists | 查询白名单,支持过滤查询和分页查询。 | To be tested |
|  | DeleteWhitelist | 删除白名单 | To be tested |
|  | CreateWhitelist | 创建白名单,控制监听器的访问权限。若开启了白名单功能,只有白名单中放通的IP可以访问该监听器的后端服务。 | To be tested |
| 监听器 | DeleteListenerForce | 删除监听器且级联删除其下子资源(删除监听器、转发策略等,解绑后端服务器组)。 | To be tested |
|  | ListListeners | 查询监听器列表。支持过滤查询和分页查询。可以通过监听器ID、协议类型、监听端口号、关联的后端云服务器的IP等查询监听器。 | To be tested |
|  | UpdateListener | 更新监听器。 | To be tested |
|  | CreateListener | 创建与负载均衡器绑定的监听器。 | To be tested |
|  | DeleteListener | 删除监听器。 | To be tested |
|  | ShowListener | 根据指定ID查询监听器详情。 | To be tested |
| 规格 | ShowFlavor | 查询规格的详情。 | To be tested |
|  | ListFlavors | 查询当前region下可用的负载均衡规格列表。 | To be tested |
| 证书 | ShowCertificatePrivateKeyEcho | 查询证书私钥回显开关当前的状态,开启或关闭。 | To be tested |
|  | CreateCertificatePrivateKeyEcho | 开启或关闭证书私钥字段回显开关。 | To be tested |
|  | ListCertificates | 查询证书列表。 | To be tested |
|  | DeleteCertificate | 删除证书。 | To be tested |
|  | UpdateCertificate | 更新证书。 | To be tested |
|  | CreateCertificate | 创建证书。用于HTTPS协议监听器。 | To be tested |
|  | ShowCertificate | 查询证书详情。 | To be tested |
| 负载均衡器 | BatchAddAvailableZones | 给负载均衡器新增可用区。 | To be tested |
|  | ListLoadbalancers | 查询负载均衡器列表。 | To be tested |
|  | CreateLoadbalancer | 创建私网类型的增强型负载均衡器。创建成功后,该接口会返回创建的增强型负载均衡器的ID、所属子网ID、负载均衡器IP等详细信息。若要创建公网类型的增强型负载均衡器,还需调用创建浮动IP的接口,将浮动IP与私网负载均衡器的vip_port_id绑定。 | To be tested |
|  | ShowLoadbalancersStatus | 查询负载均衡器状态树。可通过该接口查询负载均衡器关联的监听器、后端云服务器组、后端云服务器、健康检查、转发策略、转发规则的主要信息,了解负载均衡器下资源的拓扑情况。 | To be tested |
|  | UpdateLoadbalancer | 更新负载均衡器。 | To be tested |
|  | CloneLoadbalancer | 复制已有的负载均衡器实例。 | To be tested |
|  | BatchRemoveAvailableZones | 移除负载均衡器的可用区。 | To be tested |
|  | DeleteLoadBalancerCascade | 删除负载均衡器且级联删除其下子资源(删除负载均衡器及其绑定的监听器、后端服务器等一系列资源)。以及根据需要删除或解绑后端服务器组和LB关联的EIP。 | To be tested |
|  | UpgradeLoadbalancer | 升级负载均衡器类型。支持将共享型ELB升级为独享型ELB,但不支持独享型降级为共享型。 | To be tested |
|  | DeleteLoadBalancer | 删除负载均衡器。 | To be tested |
|  | BatchCreateLoadBalancers | 批量创建独享型或者共享型负载均衡器,包括按需及包周期计费负载均衡器。 | To be tested |
|  | ShowLoadBalancerStatus | 查询负载均衡器状态树,包括负载均衡器及其关联的子资源的状态信息。 | To be tested |
|  | DeleteLoadBalancerForce | 删除负载均衡器且级联删除其下子资源(删除负载均衡器及其绑定的监听器、后端服务器组、后端服务器等一系列资源)。 | To be tested |
|  | ShowLoadBalancer | 查询负载均衡器详情。 | To be tested |
|  | ChangeLoadbalancerChargeMode | 负载均衡器计费模式变更,当前支持的计费模式变更为: | To be tested |
| 转发策略 | CreateL7policy | 创建listener关联的转发策略 | To be tested |
|  | BatchUpdatePoliciesPriority | 批量更新转发策略的优先级。 | To be tested |
|  | ShowL7Policy | 查询七层转发策略详情。 | To be tested |
|  | DeleteL7policy | 删除转发策略 | To be tested |
|  | ListL7Policies | 查询七层转发策略列表。 | To be tested |
|  | UpdateL7Policy | 更新七层转发策略。 | To be tested |
|  | UpdateL7policies | 更新转发策略 | To be tested |
| 转发规则 | ListL7rules | 查询指定转发策略下关联的转发规则列表 | To be tested |
|  | UpdateL7Rule | 更新七层转发规则。 | To be tested |
|  | CreateL7Rule | 创建七层转发规则。 | To be tested |
|  | ShowL7rule | 根据指定ID查询某转发策略下关联的转发规则详情。 | To be tested |
|  | DeleteL7rule | 删除转发规则 | To be tested |
| 配额 | ShowQuota | 查询指定项目中负载均衡相关的各类资源的当前配额。 | To be tested |
|  | ListQuotaDetails | 查询指定项目中负载均衡相关的各类资源的当前配额和已使用配额信息。 | To be tested |
| 预占IP | CountPreoccupyIpNum | 计算以下几种场景的预占用IP数量: | To be tested |
