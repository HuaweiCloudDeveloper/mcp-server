# AAD MCP Server 

## 版本信息
v0.1.0

## 产品描述

AAD MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务AAD交互的能力。可以基于自然语言对AAD资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| DDoS原生高级防护-告警配置管理 | UpdateAlarmConfig | 设置告警配置 | To be tested |
|  | DeleteAlarmConfig | 删除告警配置 | To be tested |
|  | ShowAlarmConfig | 查询告警配置 | To be tested |
| DDoS原生高级防护-实例管理 | UpdatePackageName | 更新实例名字 | To be tested |
|  | ListUnboundProtectedIp | 查询可绑定的防护对象列表 | To be tested |
|  | ListPackage | 查询实例列表 | To be tested |
|  | UpdatePackageIp | 更新实例绑定的全量防护对象 | To be tested |
| DDoS原生高级防护-策略管理 | DeletePolicy | 删除策略 | To be tested |
|  | DisassociateIpFromPolicyAndPackage | 策略和实例解绑防护对象 | To be tested |
|  | ShowPolicy | 查询策略详情 | To be tested |
|  | AssociateIpToPolicyAndPackage | 策略和实例绑定防护对象 | To be tested |
|  | AssociateIpToPolicy | 策略绑定防护对象 | To be tested |
|  | ListPolicy | 查询策略列表 | To be tested |
|  | UpdatePolicy | 更新策略 | To be tested |
|  | AddPolicyBlackAndWhiteIpList | 策略添加黑白名单 | To be tested |
|  | DeletePolicyBlackAndWhiteIpList | 策略删除黑白名单 | To be tested |
|  | CreatePolicy | 创建策略 | To be tested |
|  | DisassociateIpFromPolicy | 策略解绑防护对象 | To be tested |
| DDoS原生高级防护-防护对象管理 | ListProtectedIp | 查询防护对象列表 | To be tested |
|  | UpdateTagForProtectedIp | 防护对象设置标签 | To be tested |
| DDoS高防-域名管理 | CreateDomain | 创建防护域名 | To be tested |
|  | ModifyDomainWebSwitch | 修改域名WEB基础防护开关/CC防护开关 | To be tested |
|  | ListDomain | 查询域名列表 | To be tested |
|  | DeleteDomain | 删除防护域名 | To be tested |
|  | ShowDomainCertificate | 查询域名关联的证书信息 | To be tested |
|  | ListInstanceId | 查询域名关联的实例ID | To be tested |
|  | SetCertForDomain | 上传/修改域名对应证书 | To be tested |
|  | CreateAadDomain | 创建防护域名 | To be tested |
|  | UpdateDomain | 更新域名源站配置信息 | To be tested |
|  | ListSourceIps | 查询高防回源IP段列表 | To be tested |
| DDoS高防-实例列表 | ListInstance | 查询高防实例列表 | To be tested |
|  | ListInstanceDomains | 查询实例关联的域名信息 | To be tested |
|  | UpgradeInstanceSpec | 修改实例规格 | To be tested |
| DDoS高防-概览 | ListPeak | 查询流量峰值、攻击计数 | To be tested |
|  | ListDDoSAttackEvent | 查询DDoS攻击事件列表 | To be tested |
|  | ListWafAttackEvent | 查询攻击事件列表 | To be tested |
|  | ListDDoSFlow | 查询DDoS攻击防护BPS/PPS流量 | To be tested |
|  | ShowWafQps | 查询CC攻击防护请求QPS | To be tested |
|  | ListWafBandwidth | 带宽曲线 | To be tested |
|  | ListWafQps | 查询请求QPS | To be tested |
|  | ListDDoSConnectionNumber | 查询新建连接数和并发连接数 | To be tested |
| DDoS高防-转发规则管理 | BatchDeleteInstanceIpRule | 批量删除高防实例IP的转发规则 | To be tested |
|  | BatchCreateInstanceIpRule | 批量创建高防实例IP的转发规则 | To be tested |
|  | UpdateInstanceIpRule | 修改高防实例转发配置的源站IP | To be tested |
|  | ListInstanceIpRule | 查询高防实例IP的转发规则列表 | To be tested |
| DDoS高防-防护策略 | AddBlackWhiteIpList | 高防实例添加黑白名单 | To be tested |
|  | ListFrequencyControlRule | 查询频率控制规则列表 | To be tested |
|  | DeleteWafWhiteIpRule | 防护策略web-cc黑白名单-删除黑白名单规则 | To be tested |
|  | ShowWafPolicy | 查询WEB防护策略配置 | To be tested |
|  | ShowFlowBlock | 查询流量封禁信息 | To be tested |
|  | ListWhiteBlackIpRule | 查询DDoS攻击防护的黑白名单列表 | To be tested |
|  | AddWafWhiteIpRule | 防护策略web-cc黑白名单-创建黑白名单规则 | To be tested |
|  | DeleteBlackWhiteIpList | 高防实例删除黑白名单 | To be tested |
|  | ListWafGeoIpRule | 查询区域封禁规则 | To be tested |
|  | ListWafCustomRule | 查询精准防护规则 | To be tested |
|  | ListWafWhiteIpRule | 防护策略web-cc黑白名单-查询黑白名单规则 | To be tested |
| 解封中心-解封管理 | ShowBlockStatistics | 查询封堵统计数据 | To be tested |
|  | ListBlockIps | 查询租户封堵列表 | To be tested |
|  | ListUnblockQuotaStatistics | 查询解封配额 | To be tested |
|  | ShowUnblockRecord | 查询租户解封记录 | To be tested |
|  | ExecuteUnblockIp | 解封IP | To be tested |
