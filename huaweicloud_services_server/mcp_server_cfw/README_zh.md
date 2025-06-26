# CFW MCP Server 


## Version
v0.1.0

## Overview

CFW MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CFW. Full-chain management of CFW resources can be carried out based on natural language.

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
                    <td rowspan="11">ACL规则管理</td>
                    <td>UpdateAclRuleOrder</td>
                    <td>ACL防护规则优先级设置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAclRuleHitCount</td>
                    <td>获取规则击中次数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRuleAclTags</td>
                    <td>查询规则标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAclRules</td>
                    <td>批量删除Acl规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAclRule</td>
                    <td>更新ACL规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAclRules</td>
                    <td>查询防护规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAclRuleHitCount</td>
                    <td>清除规则击中次数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImportStatus</td>
                    <td>查看导入状态接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateAclRuleActions</td>
                    <td>批量更新规则动作</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAclRule</td>
                    <td>删除ACL规则组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAclRule</td>
                    <td>创建ACL规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">EIP管理</td>
                    <td>ChangeEipStatus</td>
                    <td>开启关闭EIP,客户购买EIP后首次开启EIP防护前需使用ListEips同步EIP资产,sync字段设置为1。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEipCount</td>
                    <td>查询Eip个数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEips</td>
                    <td>弹性IP列表查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoProtectStatus</td>
                    <td>获取eip自动防护状态信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchAutoProtectStatus</td>
                    <td>修改eip自动防护开关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmWhitelist</td>
                    <td>查看eip告警白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">IPS管理</td>
                    <td>ListIpsSwitchStatus</td>
                    <td>查询IPS特性开关状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIpsProtectMode</td>
                    <td>查询防护模式</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIpsRules</td>
                    <td>查询频率ips规则信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeIpsProtectMode</td>
                    <td>切换防护模式</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIpsUpdateTime</td>
                    <td>获取ips规则细节</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeIpsRuleMode</td>
                    <td>改变ips规则模式</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeIpsSwitchStatus</td>
                    <td>切换开关状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCustomerIps</td>
                    <td>获取自定义ips规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAdvancedIpsRule</td>
                    <td>创建频率ips规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIpsRules1</td>
                    <td>获取ips规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Region</td>
                    <td>ListRegions</td>
                    <td>查询用户可见的区域</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>查询租户在指定项目中指定资源类型下的所有标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">websites</td>
                    <td>DeleteDomains</td>
                    <td>删除租户的网站资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomains</td>
                    <td>获取租户的所有网站资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">使用标签管理服务</td>
                    <td>ListResourceTags</td>
                    <td>查询指定实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">反病毒管理</td>
                    <td>ShowAntiVirusRule</td>
                    <td>获取防火墙反病毒规则信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAntiVirusSwitch</td>
                    <td>修改反病毒开关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAntiVirusRule</td>
                    <td>修改反病毒规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAntiVirusSwitch</td>
                    <td>查看反病毒开关</td>
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
                    <td rowspan="10">地址组管理</td>
                    <td>AddAddressSet</td>
                    <td>添加地址组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAddressSet</td>
                    <td>更新地址组信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAddressSet</td>
                    <td>删除地址组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAddressItems</td>
                    <td>查询地址组成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAddressItem</td>
                    <td>删除地址组成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAddressItem</td>
                    <td>添加地址组成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateObjectConfigDesc</td>
                    <td>编辑对象组内成员的描述信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAddressSets</td>
                    <td>查询地址组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAddressSetDetail</td>
                    <td>查询地址组详细</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAddressItems</td>
                    <td>批量删除地址组成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">域名解析及域名组管理</td>
                    <td>ShowDomainSetDetail</td>
                    <td>查看域名组详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDnsServers</td>
                    <td>更新dns服务器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteDomainSet</td>
                    <td>批量删除域名组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainSets</td>
                    <td>查询域名组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDomains</td>
                    <td>添加域名列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDomainSet</td>
                    <td>添加域名组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainSet</td>
                    <td>更新域名组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDnsServers</td>
                    <td>查询dns服务器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainParseDetail</td>
                    <td>测试域名有效性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainParseIp</td>
                    <td>获取域名地址解析结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDomainSet</td>
                    <td>删除域名组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">密钥标签管理</td>
                    <td>DeleteTag</td>
                    <td>- 功能介绍:删除密钥标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">抓包管理</td>
                    <td>CancelCaptureTask</td>
                    <td>取消抓包任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCaptureTask</td>
                    <td>查询抓包任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCaptureTask</td>
                    <td>创建抓包任务,每个任务只能执行一次。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCaptureResult</td>
                    <td>获取抓包任务结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCaptureTask</td>
                    <td>批量删除抓包任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">日志管理</td>
                    <td>ListLogConfig</td>
                    <td>获取日志配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogConfig</td>
                    <td>更新日志配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddLogConfig</td>
                    <td>创建日志配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAttackLogs</td>
                    <td>查询攻击日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccessControlLogs</td>
                    <td>查询访问控制日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">服务组管理</td>
                    <td>DeleteServiceSet</td>
                    <td>删除服务组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddServiceSet</td>
                    <td>创建服务组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceItems</td>
                    <td>查询服务组成员列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServiceSet</td>
                    <td>更新服务组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceSets</td>
                    <td>获取服务组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddServiceItems</td>
                    <td>批量添加服务组成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteServiceItems</td>
                    <td>批量删除服务组成员信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServiceItem</td>
                    <td>删除服务组成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceSetDetail</td>
                    <td>查询服务组细节</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">标签管理</td>
                    <td>CreateTag</td>
                    <td>为资源添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveTags</td>
                    <td>保存资源标签接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">流日志</td>
                    <td>ListFlowLogs</td>
                    <td>查询提交请求的租户的所有流日志列表,并根据过滤条件进行过滤</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">网络ACL</td>
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
                    <td rowspan="7">防火墙管理</td>
                    <td>ListJob</td>
                    <td>获取CFW任务执行状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEastWestFirewall</td>
                    <td>创建东西向防火墙</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFirewallList</td>
                    <td>查询防火墙列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectedVpcs</td>
                    <td>查询防护vpc信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeEastWestFirewallStatus</td>
                    <td>东西向防护开启/关闭</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEastWestFirewall</td>
                    <td>获取东西向防火墙信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFirewallDetail</td>
                    <td>查询防火墙实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">黑白名单管理</td>
                    <td>DeleteBlackWhiteList</td>
                    <td>删除黑白名单规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBlackWhiteList</td>
                    <td>更新黑白名单列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBlackWhiteLists</td>
                    <td>查询黑白名单列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddBlackWhiteList</td>
                    <td>创建黑白名单规则</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
