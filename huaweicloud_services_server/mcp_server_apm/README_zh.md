# APM MCP Server 


## Version
v0.1.0

## Overview

APM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service APM. Full-chain management of APM resources can be carried out based on natural language.

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
                    <td rowspan="3">AKSK</td>
                    <td>ShowAkSks</td>
                    <td>查询租户的aksk。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAkSk</td>
                    <td>创建aksk。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAkSk</td>
                    <td>删除aksk。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ALARM</td>
                    <td>ListAlarmNotify</td>
                    <td>查询单个告警的触发详情与历史。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmData</td>
                    <td>查询系统中存在的告警。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">APM</td>
                    <td>ChangeAgentStatus</td>
                    <td>改变指定实例的采集状态:开启和关闭。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMasterAddress</td>
                    <td>根据region名称获取该region下的master服务podlb地址信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAgent</td>
                    <td>删除agent</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveMonitorItemConfig</td>
                    <td>保存监控项。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvMonitorItem</td>
                    <td>查询监控项列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAkSk</td>
                    <td>获取该用户创建的ak/sk列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBusiness</td>
                    <td>该接口用于查询对应用户下的应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchAgent</td>
                    <td>该接口用于搜索应用下所有探针情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchApplication</td>
                    <td>对指定区域下的组件和环境及其探针情况进行搜索。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">CMDB</td>
                    <td>ShowSubBusinessDetail</td>
                    <td>查询单个子应用详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppEnvs</td>
                    <td>获取组件下的环境列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvTags</td>
                    <td>查询环境标签接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBusinessDetail</td>
                    <td>查询单个应用的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTopologyTree</td>
                    <td>获取应用树。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Profiling</td>
                    <td>ShowFlameLineTree</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">REGION</td>
                    <td>ListOpenRegion</td>
                    <td>该接口用于查询用户开通的region信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSupportedRegion</td>
                    <td>查询所有的支持的region信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">TOPOLOGY</td>
                    <td>SearchEnvTopology</td>
                    <td>查询组件环境级别全局拓扑图信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchBusinessTopology</td>
                    <td>查询应用级别全局拓扑图信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">TRACING</td>
                    <td>ShowToken</td>
                    <td>获取链路追踪应用的token</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBusiness</td>
                    <td>创建链路追踪应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAccessPoint</td>
                    <td>获取链路追踪应用接入地址</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">TRANSACTION</td>
                    <td>SearchTransactionConfig</td>
                    <td>查询已配置好的URL跟踪配置列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBusinessEnv</td>
                    <td>查询所选Region下设置了URL跟踪的环境列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchTransaction</td>
                    <td>查询当前被调用的URL跟踪视图列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTransactionDetail</td>
                    <td>查询某条URL跟踪视图详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">VIEW</td>
                    <td>ShowEnvMonitorItems</td>
                    <td>获取监控项信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRawTable</td>
                    <td>获取原始数据表格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonitorItemDetail</td>
                    <td>获取一个监控项的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonitorItemViewConfig</td>
                    <td>查询监控项配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSpanSearch</td>
                    <td>span数据查询接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTopology</td>
                    <td>调用链拓扑图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClobDetail</td>
                    <td>获取原始数据详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvInstances</td>
                    <td>获取实例信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrend</td>
                    <td>获取趋势图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSumTable</td>
                    <td>获取汇总表格数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTraceEvents</td>
                    <td>获取一个trace的所有调用链数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEventDetail</td>
                    <td>获取event的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">应用模板管理</td>
                    <td>ListApps</td>
                    <td>查询应用模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApp</td>
                    <td>删除应用模板</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
