# WAF MCP Server 


## Version
v0.1.0

## Overview

WAF MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service WAF. Full-chain management of WAF resources can be carried out based on natural language.

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
                    <td rowspan="7">云模式防护网站管理</td>
                    <td>ListHost</td>
                    <td>查询云模式防护域名列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHost</td>
                    <td>根据防护域名Id查询云模式防护域名详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHostProtectStatus</td>
                    <td>修改域名防护状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHost</td>
                    <td>更新云模式防护域名配置,在没有填入源站信息server的原始数据的情况下,则新的源站信息server会覆盖源站信息,而不是新增源站。此外,请求体可只传需要更新的部分。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostRoute</td>
                    <td>返回路由信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHost</td>
                    <td>创建云模式防护域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHost</td>
                    <td>删除云模式防护域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">告警管理</td>
                    <td>ListNoticeConfigs</td>
                    <td>查询告警通知配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlertNoticeConfig</td>
                    <td>更新告警通知配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">地址组管理</td>
                    <td>ShowIpGroup</td>
                    <td>查询ip地址组明细</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIpGroup</td>
                    <td>创建ip地址组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIpGroup</td>
                    <td>查询地址组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIpGroup</td>
                    <td>修改ip地址组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIpGroup</td>
                    <td>删除ip地址组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">安全总览</td>
                    <td>ListRequestTimeline</td>
                    <td>查询安全总览中请求次数时间线统计数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQpsTimeline</td>
                    <td>查询安全统计qps次数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopAbnormal</td>
                    <td>查询业务异常TOP统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidthTimeline</td>
                    <td>查询安全统计带宽数据,统计的带宽数据为平均值,单位为bit/s。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStatistics</td>
                    <td>查询安全总览请求与攻击数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOverviewsClassification</td>
                    <td>查询安全总览分类统计TOP信息,包含受攻击域名 、攻击源ip、受攻击URL、攻击来源区域、攻击事件分布。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">局点支持特性查询</td>
                    <td>ShowConsoleConfig</td>
                    <td>局点支持特性查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">日志配置管理</td>
                    <td>UpdateLtsInfoConfig</td>
                    <td>配置全量日志lts,该接口可用来开启与关闭waf全量日志以及配置日志组和日志流。日志组id和日志流id可前往云日志服务获取。配置的日志流id要属于所配置的日志组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLtsInfoConfig</td>
                    <td>查询lts配置信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">独享实例管理</td>
                    <td>RenameInstance</td>
                    <td>重命名WAF独享引擎。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstance</td>
                    <td>创建WAF独享引擎实例。独享模式支持的局点包括:华东-青岛、中东-利雅得、华北-北京一、华北-北京四、华北-乌兰察布一、华东-上海一、华东-上海二、华南-广州、华南-深圳、中国-香港、西南-贵阳一、亚太-曼谷、 亚太-新加坡、非洲约翰内斯堡、土耳其-伊斯坦布尔;普通租户类独享支持的局点:华北-北京四、华东-上海一、华南-广州、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstance</td>
                    <td>查询WAF独享引擎列表。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>查询WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>删除WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">独享模式防护网站管理</td>
                    <td>DeletePremiumHost</td>
                    <td>删除独享模式域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPremiumHost</td>
                    <td>独享模式域名列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePremiumHostProtectStatus</td>
                    <td>修改独享模式域名防护状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPremiumHost</td>
                    <td>查看独享模式域名配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePremiumHost</td>
                    <td>创建独享模式域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePremiumHost</td>
                    <td>修改独享模式域名配置,在没有填入源站信息server的原始数据的情况下,则新的源站信息server会覆盖源站信息,而不是新增源站。此外,请求体可只传需要更新的部分。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">租户域名查询</td>
                    <td>ListCompositeHosts</td>
                    <td>查询全部防护域名列表,包括云模式和独享模式</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCompositeHost</td>
                    <td>根据Id查询防护域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">租户订购管理</td>
                    <td>CreatePrepaidCloudWaf</td>
                    <td>购买包周期云模式waf。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubscriptionInfo</td>
                    <td>查询租户订购信息,包括云模式包周期、按需计费、独享模式</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangePrepaidCloudWaf</td>
                    <td>变更包周期云模式waf规格。注:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">租户防护域名管理</td>
                    <td>MigrateCompositeHosts</td>
                    <td>按企业项目迁移防护域名,仅专业版与独享版支持该功能</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="57">策略规则管理</td>
                    <td>ListCcRules</td>
                    <td>查询cc规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomRule</td>
                    <td>删除精准防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAntitamperRule</td>
                    <td>删除防篡改防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCustomRule</td>
                    <td>根据Id查询精准防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAntileakageRule</td>
                    <td>根据Id查询防敏感信息泄露防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAntileakageRules</td>
                    <td>查询防敏感信息泄露规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCcRule</td>
                    <td>根据Id查询cc防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGeoipRule</td>
                    <td>更新地理位置控制防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateValueList</td>
                    <td>创建引用表,引用表能够被CC攻击防护规则和精准访问防护中的规则所引用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivacyRule</td>
                    <td>查询隐私屏蔽防护规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAnticrawlerRuleType</td>
                    <td>更新JS脚本反爬虫规则防护模式,在创建JS脚本反爬虫规则前,需要调用该接口指定JS脚本反爬虫规则防护模式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePrivacyRule</td>
                    <td>删除隐私屏蔽防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePunishmentRule</td>
                    <td>更新攻击惩罚规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWhiteblackipRule</td>
                    <td>更新黑白名单防护规则,可以更新ip/ip段以及防护动作等信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWhiteblackipRule</td>
                    <td>创建黑白名单规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteValueList</td>
                    <td>删除引用表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePunishmentRule</td>
                    <td>创建攻击惩罚规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIgnoreRule</td>
                    <td>更新全局白名单(原误报屏蔽)防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCcRule</td>
                    <td>删除cc防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAntileakageRule</td>
                    <td>更新防敏感信息泄露防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIgnoreRule</td>
                    <td>删除全局白名单(原误报屏蔽)防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAntileakageRule</td>
                    <td>创建防敏感信息泄露规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWhiteblackipRule</td>
                    <td>查询黑白名单规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivacyRule</td>
                    <td>查询隐私屏蔽防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCustomRules</td>
                    <td>查询精准防护规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWhiteBlackIpRule</td>
                    <td>查询黑白名单防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicyRuleStatus</td>
                    <td>修改单条规则的状态,用于开启或者关闭单条规则,比如关闭精准防护中某一条规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAnticrawlerRule</td>
                    <td>更新JS脚本反爬虫防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAntiTamperRuleRefresh</td>
                    <td>网页防篡改规则更新缓存</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPunishmentRule</td>
                    <td>根据Id查询攻击惩罚防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCustomRule</td>
                    <td>更新精准防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGeoipRule</td>
                    <td>创建地理位置控制规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCcRule</td>
                    <td>更新cc防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAnticrawlerRule</td>
                    <td>创建JS脚本反爬虫规则,在调用此接口创建防护规则前,需要调用更新JS脚本反爬虫规则防护模式(UpdateAnticrawlerRuleType)接口指定防护模式</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGeoipRule</td>
                    <td>删除地理位置控制防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAntiTamperRule</td>
                    <td>创建防篡改规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGeoipRule</td>
                    <td>删除地理位置控制防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAnticrawlerRule</td>
                    <td>删除JS脚本反爬虫防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIgnoreRule</td>
                    <td>创建全局白名单(原误报屏蔽)规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIgnoreRule</td>
                    <td>查询全局白名单(原误报屏蔽)规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGeoipRule</td>
                    <td>查询地理位置访问控制规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWhiteBlackIpRule</td>
                    <td>删除黑白名单防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowValueList</td>
                    <td>查询引用表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePunishmentRule</td>
                    <td>删除攻击惩罚规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAntitamperRule</td>
                    <td>查询防篡改防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAntileakageRule</td>
                    <td>删除防敏感信息泄露防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPunishmentRules</td>
                    <td>查询攻击惩罚规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrivacyRule</td>
                    <td>更新隐私屏蔽防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePrivacyRule</td>
                    <td>创建隐私屏蔽防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAnticrawlerRule</td>
                    <td>根据Id查询JS脚本反爬虫防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListValueList</td>
                    <td>查询引用表列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIgnoreRule</td>
                    <td>查询全局白名单(原误报屏蔽)防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateValueList</td>
                    <td>修改引用表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAnticrawlerRules</td>
                    <td>查询JS脚本反爬虫规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCustomRule</td>
                    <td>创建精准防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCcRule</td>
                    <td>创建cc规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAntitamperRule</td>
                    <td>查询防篡改规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">系统管理</td>
                    <td>ShowSourceIp</td>
                    <td>查询WAF回源Ip信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">证书管理</td>
                    <td>UpdateCertificate</td>
                    <td>修改证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplyCertificateToHost</td>
                    <td>绑定证书到域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCertificate</td>
                    <td>删除证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificate</td>
                    <td>查询证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificate</td>
                    <td>创建证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificates</td>
                    <td>查询证书列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">防护事件管理</td>
                    <td>ListEvent</td>
                    <td>查询攻击事件列表,该API暂时不支持查询全部防护事件,pagesize参数不可设为-1,由于性能原因,数据量越大消耗的内存越大,后端最多限制查询10000条数据,例如:自定义时间段内的数据超过了10000条,就无法查出page为101,pagesize为100之后的数据,需要调整时间区间,再进行查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEvent</td>
                    <td>查询指定事件id的防护事件详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">防护策略管理</td>
                    <td>DeletePolicy</td>
                    <td>删除防护策略,若策略正在使用,则需要先接解除域名与策略的绑定关系才能删除策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicyProtectHost</td>
                    <td>更新防护策略的防护域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicy</td>
                    <td>查询防护策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPolicy</td>
                    <td>根据Id查询防护策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePolicy</td>
                    <td>创建防护策略,系统会在生成策略时配置一些默认的配置项,如果需要修改策略的默认配置项需要通过调用更新防护策略接口实现</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicy</td>
                    <td>更新防护策略,请求体可只传需要更新的部分</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
