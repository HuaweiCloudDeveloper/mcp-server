# WAF MCP Server 

## 版本信息
v0.1.0

## 产品描述

WAF MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务WAF交互的能力。可以基于自然语言对WAF资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 云模式防护网站管理 | ListHost | 查询云模式防护域名列表 | To be tested |
|  | ShowHost | 根据防护域名Id查询云模式防护域名详细信息 | To be tested |
|  | UpdateHostProtectStatus | 修改域名防护状态 | To be tested |
|  | UpdateHost | 更新云模式防护域名配置,在没有填入源站信息server的原始数据的情况下,则新的源站信息server会覆盖源站信息,而不是新增源站。此外,请求体可只传需要更新的部分。 | To be tested |
|  | ListHostRoute | 返回路由信息 | To be tested |
|  | CreateHost | 创建云模式防护域名 | To be tested |
|  | DeleteHost | 删除云模式防护域名 | To be tested |
| 告警管理 | ListNoticeConfigs | 查询告警通知配置 | To be tested |
|  | UpdateAlertNoticeConfig | 更新告警通知配置 | To be tested |
| 地址组管理 | ShowIpGroup | 查询ip地址组明细 | To be tested |
|  | CreateIpGroup | 创建ip地址组 | To be tested |
|  | ListIpGroup | 查询地址组列表 | To be tested |
|  | UpdateIpGroup | 修改ip地址组 | To be tested |
|  | DeleteIpGroup | 删除ip地址组 | To be tested |
| 安全总览 | ListRequestTimeline | 查询安全总览中请求次数时间线统计数据。 | To be tested |
|  | ListQpsTimeline | 查询安全统计qps次数。 | To be tested |
|  | ListTopAbnormal | 查询业务异常TOP统计信息。 | To be tested |
|  | ListBandwidthTimeline | 查询安全统计带宽数据,统计的带宽数据为平均值,单位为bit/s。 | To be tested |
|  | ListStatistics | 查询安全总览请求与攻击数量。 | To be tested |
|  | ListOverviewsClassification | 查询安全总览分类统计TOP信息,包含受攻击域名 、攻击源ip、受攻击URL、攻击来源区域、攻击事件分布。 | To be tested |
| 局点支持特性查询 | ShowConsoleConfig | 局点支持特性查询 | To be tested |
| 日志配置管理 | UpdateLtsInfoConfig | 配置全量日志lts,该接口可用来开启与关闭waf全量日志以及配置日志组和日志流。日志组id和日志流id可前往云日志服务获取。配置的日志流id要属于所配置的日志组。 | To be tested |
|  | ShowLtsInfoConfig | 查询lts配置信息 | To be tested |
| 独享实例管理 | RenameInstance | 重命名WAF独享引擎。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳  、中国-香港、亚太-曼谷、 亚太-新加坡。 | To be tested |
|  | CreateInstance | 创建WAF独享引擎实例。独享模式支持的局点包括:华东-青岛、中东-利雅得、华北-北京一、华北-北京四、华北-乌兰察布一、华东-上海一、华东-上海二、华南-广州、华南-深圳、中国-香港、西南-贵阳一、亚太-曼谷、 亚太-新加坡、非洲约翰内斯堡、土耳其-伊斯坦布尔;普通租户类独享支持的局点:华北-北京四、华东-上海一、华南-广州、中国-香港、亚太-曼谷、 亚太-新加坡。 | To be tested |
|  | ListInstance | 查询WAF独享引擎列表。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳  、中国-香港、亚太-曼谷、 亚太-新加坡。 | To be tested |
|  | ShowInstance | 查询WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳  、中国-香港、亚太-曼谷、 亚太-新加坡。 | To be tested |
|  | DeleteInstance | 删除WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳  、中国-香港、亚太-曼谷、 亚太-新加坡。 | To be tested |
| 独享模式防护网站管理 | DeletePremiumHost | 删除独享模式域名 | To be tested |
|  | ListPremiumHost | 独享模式域名列表 | To be tested |
|  | UpdatePremiumHostProtectStatus | 修改独享模式域名防护状态 | To be tested |
|  | ShowPremiumHost | 查看独享模式域名配置 | To be tested |
|  | CreatePremiumHost | 创建独享模式域名 | To be tested |
|  | UpdatePremiumHost | 修改独享模式域名配置,在没有填入源站信息server的原始数据的情况下,则新的源站信息server会覆盖源站信息,而不是新增源站。此外,请求体可只传需要更新的部分。 | To be tested |
| 租户域名查询 | ListCompositeHosts | 查询全部防护域名列表,包括云模式和独享模式 | To be tested |
|  | ShowCompositeHost | 根据Id查询防护域名 | To be tested |
| 租户订购管理 | CreatePrepaidCloudWaf | 购买包周期云模式waf。 | To be tested |
|  | ShowSubscriptionInfo | 查询租户订购信息,包括云模式包周期、按需计费、独享模式 | To be tested |
|  | ChangePrepaidCloudWaf | 变更包周期云模式waf规格。注: | To be tested |
| 租户防护域名管理 | MigrateCompositeHosts | 按企业项目迁移防护域名,仅专业版与独享版支持该功能 | To be tested |
| 策略规则管理 | ListCcRules | 查询cc规则列表 | To be tested |
|  | DeleteCustomRule | 删除精准防护规则 | To be tested |
|  | DeleteAntitamperRule | 删除防篡改防护规则 | To be tested |
|  | ShowCustomRule | 根据Id查询精准防护规则 | To be tested |
|  | ShowAntileakageRule | 根据Id查询防敏感信息泄露防护规则 | To be tested |
|  | ListAntileakageRules | 查询防敏感信息泄露规则列表 | To be tested |
|  | ShowCcRule | 根据Id查询cc防护规则 | To be tested |
|  | UpdateGeoipRule | 更新地理位置控制防护规则 | To be tested |
|  | CreateValueList | 创建引用表,引用表能够被CC攻击防护规则和精准访问防护中的规则所引用。 | To be tested |
|  | ListPrivacyRule | 查询隐私屏蔽防护规则列表 | To be tested |
|  | UpdateAnticrawlerRuleType | 更新JS脚本反爬虫规则防护模式,在创建JS脚本反爬虫规则前,需要调用该接口指定JS脚本反爬虫规则防护模式。 | To be tested |
|  | DeletePrivacyRule | 删除隐私屏蔽防护规则 | To be tested |
|  | UpdatePunishmentRule | 更新攻击惩罚规则 | To be tested |
|  | UpdateWhiteblackipRule | 更新黑白名单防护规则,可以更新ip/ip段以及防护动作等信息 | To be tested |
|  | CreateWhiteblackipRule | 创建黑白名单规则 | To be tested |
|  | DeleteValueList | 删除引用表 | To be tested |
|  | CreatePunishmentRule | 创建攻击惩罚规则 | To be tested |
|  | UpdateIgnoreRule | 更新全局白名单(原误报屏蔽)防护规则 | To be tested |
|  | DeleteCcRule | 删除cc防护规则 | To be tested |
|  | UpdateAntileakageRule | 更新防敏感信息泄露防护规则 | To be tested |
|  | DeleteIgnoreRule | 删除全局白名单(原误报屏蔽)防护规则 | To be tested |
|  | CreateAntileakageRule | 创建防敏感信息泄露规则 | To be tested |
|  | ListWhiteblackipRule | 查询黑白名单规则列表 | To be tested |
|  | ShowPrivacyRule | 查询隐私屏蔽防护规则 | To be tested |
|  | ListCustomRules | 查询精准防护规则列表 | To be tested |
|  | ShowWhiteBlackIpRule | 查询黑白名单防护规则 | To be tested |
|  | UpdatePolicyRuleStatus | 修改单条规则的状态,用于开启或者关闭单条规则,比如关闭精准防护中某一条规则 | To be tested |
|  | UpdateAnticrawlerRule | 更新JS脚本反爬虫防护规则 | To be tested |
|  | UpdateAntiTamperRuleRefresh | 网页防篡改规则更新缓存 | To be tested |
|  | ShowPunishmentRule | 根据Id查询攻击惩罚防护规则 | To be tested |
|  | UpdateCustomRule | 更新精准防护规则 | To be tested |
|  | CreateGeoipRule | 创建地理位置控制规则 | To be tested |
|  | UpdateCcRule | 更新cc防护规则 | To be tested |
|  | CreateAnticrawlerRule | 创建JS脚本反爬虫规则,在调用此接口创建防护规则前,需要调用更新JS脚本反爬虫规则防护模式(UpdateAnticrawlerRuleType)接口指定防护模式 | To be tested |
|  | DeleteGeoipRule | 删除地理位置控制防护规则 | To be tested |
|  | CreateAntiTamperRule | 创建防篡改规则 | To be tested |
|  | ShowGeoipRule | 删除地理位置控制防护规则 | To be tested |
|  | DeleteAnticrawlerRule | 删除JS脚本反爬虫防护规则 | To be tested |
|  | CreateIgnoreRule | 创建全局白名单(原误报屏蔽)规则 | To be tested |
|  | ListIgnoreRule | 查询全局白名单(原误报屏蔽)规则列表 | To be tested |
|  | ListGeoipRule | 查询地理位置访问控制规则列表 | To be tested |
|  | DeleteWhiteBlackIpRule | 删除黑白名单防护规则 | To be tested |
|  | ShowValueList | 查询引用表 | To be tested |
|  | DeletePunishmentRule | 删除攻击惩罚规则 | To be tested |
|  | ShowAntitamperRule | 查询防篡改防护规则 | To be tested |
|  | DeleteAntileakageRule | 删除防敏感信息泄露防护规则 | To be tested |
|  | ListPunishmentRules | 查询攻击惩罚规则列表 | To be tested |
|  | UpdatePrivacyRule | 更新隐私屏蔽防护规则 | To be tested |
|  | CreatePrivacyRule | 创建隐私屏蔽防护规则 | To be tested |
|  | ShowAnticrawlerRule | 根据Id查询JS脚本反爬虫防护规则 | To be tested |
|  | ListValueList | 查询引用表列表 | To be tested |
|  | ShowIgnoreRule | 查询全局白名单(原误报屏蔽)防护规则 | To be tested |
|  | UpdateValueList | 修改引用表 | To be tested |
|  | ListAnticrawlerRules | 查询JS脚本反爬虫规则列表 | To be tested |
|  | CreateCustomRule | 创建精准防护规则 | To be tested |
|  | CreateCcRule | 创建cc规则 | To be tested |
|  | ListAntitamperRule | 查询防篡改规则列表 | To be tested |
| 系统管理 | ShowSourceIp | 查询WAF回源Ip信息 | To be tested |
| 证书管理 | UpdateCertificate | 修改证书 | To be tested |
|  | ApplyCertificateToHost | 绑定证书到域名 | To be tested |
|  | DeleteCertificate | 删除证书 | To be tested |
|  | ShowCertificate | 查询证书 | To be tested |
|  | CreateCertificate | 创建证书 | To be tested |
|  | ListCertificates | 查询证书列表 | To be tested |
| 防护事件管理 | ListEvent | 查询攻击事件列表,该API暂时不支持查询全部防护事件,pagesize参数不可设为-1,由于性能原因,数据量越大消耗的内存越大,后端最多限制查询10000条数据,例如:自定义时间段内的数据超过了10000条,就无法查出page为101,pagesize为100之后的数据,需要调整时间区间,再进行查询 | To be tested |
|  | ShowEvent | 查询指定事件id的防护事件详情 | To be tested |
| 防护策略管理 | DeletePolicy | 删除防护策略,若策略正在使用,则需要先接解除域名与策略的绑定关系才能删除策略。 | To be tested |
|  | UpdatePolicyProtectHost | 更新防护策略的防护域名 | To be tested |
|  | ListPolicy | 查询防护策略列表 | To be tested |
|  | ShowPolicy | 根据Id查询防护策略 | To be tested |
|  | CreatePolicy | 创建防护策略,系统会在生成策略时配置一些默认的配置项,如果需要修改策略的默认配置项需要通过调用更新防护策略接口实现 | To be tested |
|  | UpdatePolicy | 更新防护策略,请求体可只传需要更新的部分 | To be tested |
