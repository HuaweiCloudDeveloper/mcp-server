# GSL MCP Server 


## Version
v0.1.0

## Overview

GSL MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GSL. Full-chain management of GSL resources can be carried out based on natural language.

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
                    <td rowspan="6">Attribute</td>
                    <td>CreateAttribute</td>
                    <td>用户新增自定义属性接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableAttribute</td>
                    <td>启用自定义属性接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableAttribute</td>
                    <td>停用自定义属性接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAttributes</td>
                    <td>查询自定义属性列表接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAttribute</td>
                    <td>修改自定义属性接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetAttributes</td>
                    <td>批量设置自定义属性接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">BackPool</td>
                    <td>ListBackPools</td>
                    <td>查询后向流量池列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackPoolMembers</td>
                    <td>查询后向流量池成员列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">NetworkSwitchPolicies</td>
                    <td>ListNetworkSwitchPolicies</td>
                    <td>查询策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddNetworkSwitchPolicy</td>
                    <td>新增网络切换策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">PricePlans</td>
                    <td>ListProPricePlans</td>
                    <td>查询套餐列表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">SimCards</td>
                    <td>ListSimCards</td>
                    <td>查询SIM卡列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartStopNet</td>
                    <td>SIM卡申请断网/恢复在用,接口仅支持中国电信卡调用。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetSpeedValue</td>
                    <td>实体卡限速接口,接口仅支持中国电信和中国联通实体卡调用。中国联通卡需要个人实名认证后才能使用限速功能。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonthUsages</td>
                    <td>设备月用量统计</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRealName</td>
                    <td>清除实名认证信息,接口仅支持中国电信卡调用。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSimCard</td>
                    <td>查询SIM卡详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopSimCard</td>
                    <td>创建停机申请,返回业务受理单号。1~2个工作日完成停机操作。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableSimCard</td>
                    <td>创建激活实体卡申请,返回业务受理单号。1~2个工作日完成激活操作。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSimCardFlowPerDay</td>
                    <td>批量查询SIM卡日用量接口,支持按天或按月查询。SIM卡标识和容器ID只能选一个参数,天和月也只能选一个参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRealNamed</td>
                    <td>实时查询SIM卡实名认证信息,接口仅支持查询中国大陆运营商卡片的实名认证信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterImei</td>
                    <td>支持固定机卡重绑(需要上传IMEI,将SIM卡绑定到指定IMEI的设备)和普通机卡重绑(会清除之前绑定的设备,将SIM卡绑定到正在使用的设备),接口仅支持中国电信卡,中国移动卡调用。中国电信卡单卡每月只允许重绑2次,中国移动卡仅支持普通机卡重绑。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetExceedCutNet</td>
                    <td>SIM卡达量断网/取消达量断网,接口仅支持中国电信的卡以及中国联通、中国移动的组池卡调用。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetSimCard</td>
                    <td>创建复机申请,返回业务受理单号。1~2个工作日完成复机操作。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">SimDeviceMultiply</td>
                    <td>SwitchNetwork</td>
                    <td>切换网络</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSimDeviceMultiply</td>
                    <td>通过cid或全量查询三网卡列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetNetworkSwitchPolicy</td>
                    <td>SIM卡设置网络切换策略,接口仅支持三网卡调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">SimPool</td>
                    <td>ListSimPools</td>
                    <td>查询流量池列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSimPoolMembers</td>
                    <td>查询流量池成员列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">SimPricePlans</td>
                    <td>ListSimPricePlans</td>
                    <td>SIM卡套餐列表查询,实体卡只会有一个套餐,eSIM/vSIM可能会有多个套餐</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlowBySimCards</td>
                    <td>批量查询实体卡流量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Sms</td>
                    <td>SendSms</td>
                    <td>发送短信,接口仅支持开通短信套餐的中国移动与中国电信卡调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSmsDetails</td>
                    <td>短信发送详情,接口仅支持开通短信套餐的中国移动与中国电信卡调用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tag</td>
                    <td>BatchSetTags</td>
                    <td>批量设置/取消设置标签接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">WorkOrder</td>
                    <td>ListWorkOrders</td>
                    <td>分页查询业务受理单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkOrderDetails</td>
                    <td>分页查询业务受理明细</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">密钥标签管理</td>
                    <td>DeleteTag</td>
                    <td>- 功能介绍:删除密钥标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">标签管理</td>
                    <td>CreateTag</td>
                    <td>为资源添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像标签</td>
                    <td>ListTags</td>
                    <td>根据不同条件查询镜像标签列表信息。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
