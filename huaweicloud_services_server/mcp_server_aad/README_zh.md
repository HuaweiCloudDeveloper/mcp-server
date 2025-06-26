# AAD MCP Server 


## Version
v0.1.0

## Overview

AAD MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service AAD. Full-chain management of AAD resources can be carried out based on natural language.

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
                    <td rowspan="1">DDoS原生高级防护-告警配置管理</td>
                    <td>DeleteAlarmConfig</td>
                    <td>删除告警配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">DDoS原生高级防护-实例管理</td>
                    <td>UpdatePackageName</td>
                    <td>更新实例名字</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUnboundProtectedIp</td>
                    <td>查询可绑定的防护对象列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPackage</td>
                    <td>查询实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePackageIp</td>
                    <td>更新实例绑定的全量防护对象</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">DDoS原生高级防护-策略管理</td>
                    <td>DisassociateIpFromPolicyAndPackage</td>
                    <td>策略和实例解绑防护对象</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateIpToPolicyAndPackage</td>
                    <td>策略和实例绑定防护对象</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateIpToPolicy</td>
                    <td>策略绑定防护对象</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddPolicyBlackAndWhiteIpList</td>
                    <td>策略添加黑白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePolicyBlackAndWhiteIpList</td>
                    <td>策略删除黑白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateIpFromPolicy</td>
                    <td>策略解绑防护对象</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">DDoS原生高级防护-防护对象管理</td>
                    <td>ListProtectedIp</td>
                    <td>查询防护对象列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTagForProtectedIp</td>
                    <td>防护对象设置标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">DDoS高防-域名管理</td>
                    <td>ModifyDomainWebSwitch</td>
                    <td>修改域名WEB基础防护开关/CC防护开关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomain</td>
                    <td>查询域名列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainCertificate</td>
                    <td>查询域名关联的证书信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceId</td>
                    <td>查询域名关联的实例ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetCertForDomain</td>
                    <td>上传/修改域名对应证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAadDomain</td>
                    <td>创建防护域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomain</td>
                    <td>更新域名源站配置信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSourceIps</td>
                    <td>查询高防回源IP段列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">DDoS高防-实例列表</td>
                    <td>ListInstanceDomains</td>
                    <td>查询实例关联的域名信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeInstanceSpec</td>
                    <td>修改实例规格</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">DDoS高防-概览</td>
                    <td>ListPeak</td>
                    <td>查询流量峰值、攻击计数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDDoSAttackEvent</td>
                    <td>查询DDoS攻击事件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWafAttackEvent</td>
                    <td>查询攻击事件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDDoSFlow</td>
                    <td>查询DDoS攻击防护BPS/PPS流量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWafQps</td>
                    <td>查询CC攻击防护请求QPS</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWafBandwidth</td>
                    <td>带宽曲线</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWafQps</td>
                    <td>查询请求QPS</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDDoSConnectionNumber</td>
                    <td>查询新建连接数和并发连接数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">DDoS高防-转发规则管理</td>
                    <td>BatchDeleteInstanceIpRule</td>
                    <td>批量删除高防实例IP的转发规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateInstanceIpRule</td>
                    <td>批量创建高防实例IP的转发规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceIpRule</td>
                    <td>修改高防实例转发配置的源站IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceIpRule</td>
                    <td>查询高防实例IP的转发规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">DDoS高防-防护策略</td>
                    <td>AddBlackWhiteIpList</td>
                    <td>高防实例添加黑白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFrequencyControlRule</td>
                    <td>查询频率控制规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWafWhiteIpRule</td>
                    <td>防护策略web-cc黑白名单-删除黑白名单规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWafPolicy</td>
                    <td>查询WEB防护策略配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlowBlock</td>
                    <td>查询流量封禁信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWhiteBlackIpRule</td>
                    <td>查询DDoS攻击防护的黑白名单列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddWafWhiteIpRule</td>
                    <td>防护策略web-cc黑白名单-创建黑白名单规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBlackWhiteIpList</td>
                    <td>高防实例删除黑白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWafGeoIpRule</td>
                    <td>查询区域封禁规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWafCustomRule</td>
                    <td>查询精准防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWafWhiteIpRule</td>
                    <td>防护策略web-cc黑白名单-查询黑白名单规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Domain</td>
                    <td>CreateDomain</td>
                    <td>创建域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDomain</td>
                    <td>删除域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">告警配置管理</td>
                    <td>UpdateAlarmConfig</td>
                    <td>修改告警配置接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlarmConfig</td>
                    <td>获取告警配置信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">独享实例管理</td>
                    <td>ListInstance</td>
                    <td>查询WAF独享引擎列表。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">解封中心-解封管理</td>
                    <td>ShowBlockStatistics</td>
                    <td>查询封堵统计数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBlockIps</td>
                    <td>查询租户封堵列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUnblockQuotaStatistics</td>
                    <td>查询解封配额</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUnblockRecord</td>
                    <td>查询租户解封记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteUnblockIp</td>
                    <td>解封IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">防护策略管理</td>
                    <td>DeletePolicy</td>
                    <td>删除防护策略,若策略正在使用,则需要先接解除域名与策略的绑定关系才能删除策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPolicy</td>
                    <td>根据Id查询防护策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicy</td>
                    <td>查询防护策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicy</td>
                    <td>更新防护策略,请求体可只传需要更新的部分</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePolicy</td>
                    <td>创建防护策略,系统会在生成策略时配置一些默认的配置项,如果需要修改策略的默认配置项需要通过调用更新防护策略接口实现</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
