# CFW MCP Server 

## 版本信息
v0.1.0

## 产品描述

CFW MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CFW交互的能力。可以基于自然语言对CFW资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| ACL规则管理 | UpdateAclRuleOrder | ACL防护规则优先级设置 | To be tested |
|  | ListAclRuleHitCount | 获取规则击中次数 | To be tested |
|  | ListRuleAclTags | 查询规则标签 | To be tested |
|  | BatchDeleteAclRules | 批量删除Acl规则 | To be tested |
|  | UpdateAclRule | 更新ACL规则 | To be tested |
|  | ListAclRules | 查询防护规则 | To be tested |
|  | ListRegions | 查看region列表 | To be tested |
|  | DeleteAclRuleHitCount | 清除规则击中次数 | To be tested |
|  | ShowImportStatus | 查看导入状态接口 | To be tested |
|  | BatchUpdateAclRuleActions | 批量更新规则动作 | To be tested |
|  | DeleteAclRule | 删除ACL规则组 | To be tested |
|  | AddAclRule | 创建ACL规则 | To be tested |
| EIP管理 | ChangeEipStatus | 开启关闭EIP,客户购买EIP后首次开启EIP防护前需使用ListEips同步EIP资产,sync字段设置为1。 | To be tested |
|  | ListEipCount | 查询Eip个数 | To be tested |
|  | ListEips | 弹性IP列表查询 | To be tested |
|  | ShowAutoProtectStatus | 获取eip自动防护状态信息 | To be tested |
|  | SwitchAutoProtectStatus | 修改eip自动防护开关 | To be tested |
|  | ListAlarmWhitelist | 查看eip告警白名单 | To be tested |
| IPS管理 | ListIpsSwitchStatus | 查询IPS特性开关状态 | To be tested |
|  | ListIpsProtectMode | 查询防护模式 | To be tested |
|  | ListIpsRules | 查询频率ips规则信息 | To be tested |
|  | ChangeIpsProtectMode | 切换防护模式 | To be tested |
|  | ShowIpsUpdateTime | 获取ips规则细节 | To be tested |
|  | ChangeIpsRuleMode | 改变ips规则模式 | To be tested |
|  | ChangeIpsSwitchStatus | 切换开关状态 | To be tested |
|  | ListCustomerIps | 获取自定义ips规则 | To be tested |
|  | UpdateAdvancedIpsRule | 创建频率ips规则 | To be tested |
|  | ListIpsRules1 | 获取ips规则列表 | To be tested |
| 反病毒管理 | ShowAntiVirusRule | 获取防火墙反病毒规则信息 | To be tested |
|  | UpdateAntiVirusSwitch | 修改反病毒开关 | To be tested |
|  | UpdateAntiVirusRule | 修改反病毒规则 | To be tested |
|  | ShowAntiVirusSwitch | 查看反病毒开关 | To be tested |
| 告警配置管理 | UpdateAlarmConfig | 修改告警配置接口 | To be tested |
|  | ShowAlarmConfig | 获取告警配置信息 | To be tested |
| 地址组管理 | AddAddressSet | 添加地址组 | To be tested |
|  | UpdateAddressSet | 更新地址组信息 | To be tested |
|  | DeleteAddressSet | 删除地址组 | To be tested |
|  | ListAddressItems | 查询地址组成员 | To be tested |
|  | DeleteAddressItem | 删除地址组成员 | To be tested |
|  | AddAddressItem | 添加地址组成员 | To be tested |
|  | UpdateObjectConfigDesc | 编辑对象组内成员的描述信息 | To be tested |
|  | ListAddressSets | 查询地址组列表 | To be tested |
|  | ListAddressSetDetail | 查询地址组详细 | To be tested |
|  | BatchDeleteAddressItems | 批量删除地址组成员 | To be tested |
| 域名解析及域名组管理 | ShowDomainSetDetail | 查看域名组详情 | To be tested |
|  | DeleteDomains | 删除域名列表 | To be tested |
|  | UpdateDnsServers | 更新dns服务器列表 | To be tested |
|  | BatchDeleteDomainSet | 批量删除域名组 | To be tested |
|  | ListDomainSets | 查询域名组列表 | To be tested |
|  | AddDomains | 添加域名列表 | To be tested |
|  | AddDomainSet | 添加域名组 | To be tested |
|  | UpdateDomainSet | 更新域名组 | To be tested |
|  | ListDomains | 获取域名组下域名列表 | To be tested |
|  | ListDnsServers | 查询dns服务器列表 | To be tested |
|  | ListDomainParseDetail | 测试域名有效性 | To be tested |
|  | ListDomainParseIp | 获取域名地址解析结果 | To be tested |
|  | DeleteDomainSet | 删除域名组 | To be tested |
| 抓包管理 | CancelCaptureTask | 取消抓包任务 | To be tested |
|  | ListCaptureTask | 查询抓包任务 | To be tested |
|  | CreateCaptureTask | 创建抓包任务,每个任务只能执行一次。 | To be tested |
|  | ListCaptureResult | 获取抓包任务结果 | To be tested |
|  | DeleteCaptureTask | 批量删除抓包任务 | To be tested |
| 日志管理 | ListFlowLogs | 查询流日志 | To be tested |
|  | ListLogConfig | 获取日志配置 | To be tested |
|  | UpdateLogConfig | 更新日志配置 | To be tested |
|  | AddLogConfig | 创建日志配置 | To be tested |
|  | ListAttackLogs | 查询攻击日志 | To be tested |
|  | ListAccessControlLogs | 查询访问控制日志 | To be tested |
| 服务组管理 | DeleteServiceSet | 删除服务组 | To be tested |
|  | AddServiceSet | 创建服务组 | To be tested |
|  | ListServiceItems | 查询服务组成员列表 | To be tested |
|  | UpdateServiceSet | 更新服务组 | To be tested |
|  | ListServiceSets | 获取服务组列表 | To be tested |
|  | AddServiceItems | 批量添加服务组成员 | To be tested |
|  | BatchDeleteServiceItems | 批量删除服务组成员信息 | To be tested |
|  | DeleteServiceItem | 删除服务组成员 | To be tested |
|  | ListServiceSetDetail | 查询服务组细节 | To be tested |
| 标签管理 | SaveTags | 保存资源标签接口 | To be tested |
|  | ListProjectTags | 查询标签信息 | To be tested |
|  | ListResourceTags | 查询资源标签信息 | To be tested |
| 防火墙管理 | ListJob | 获取CFW任务执行状态 | To be tested |
|  | DeleteTag | 删除标签 | To be tested |
|  | CreateTag | 创建标签 | To be tested |
|  | CreateEastWestFirewall | 创建东西向防火墙 | To be tested |
|  | ListFirewallList | 查询防火墙列表 | To be tested |
|  | CreateFirewall | 创建防火墙 | To be tested |
|  | DeleteFirewall | 删除防火墙,仅按需生效 | To be tested |
|  | ListProtectedVpcs | 查询防护vpc信息 | To be tested |
|  | ChangeEastWestFirewallStatus | 东西向防护开启/关闭 | To be tested |
|  | ListEastWestFirewall | 获取东西向防火墙信息 | To be tested |
|  | ListFirewallDetail | 查询防火墙实例 | To be tested |
| 黑白名单管理 | DeleteBlackWhiteList | 删除黑白名单规则 | To be tested |
|  | UpdateBlackWhiteList | 更新黑白名单列表 | To be tested |
|  | ListBlackWhiteLists | 查询黑白名单列表 | To be tested |
|  | AddBlackWhiteList | 创建黑白名单规则 | To be tested |
