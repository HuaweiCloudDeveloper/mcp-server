# CodeArtsInspector MCP Server 


## Version
v0.1.0

## Overview

CodeArtsInspector MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeArtsInspector. Full-chain management of CodeArtsInspector resources can be carried out based on natural language.

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
                    <td rowspan="1">Group</td>
                    <td>DeleteGroup</td>
                    <td>删除代码组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">host_groups</td>
                    <td>ListGroups</td>
                    <td>获取主机组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddGroup</td>
                    <td>批量创建主机组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">host_results</td>
                    <td>ListHostResults</td>
                    <td>获取主机漏洞扫描结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">host_tasks</td>
                    <td>BatchStartHostTasks</td>
                    <td>批量启动或取消主机漏洞扫描任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">hosts</td>
                    <td>BatchCreateHosts</td>
                    <td>批量创建租户的主机资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">purchase</td>
                    <td>CreatePurchaseOrder</td>
                    <td>订购下单接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubscription</td>
                    <td>资源版本查询接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePurchaseOrder</td>
                    <td>变更下单接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">web_results</td>
                    <td>ShowReportStatus</td>
                    <td>获取网站扫描PDF报告生成状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadTaskReport</td>
                    <td>下载网站扫描任务PDF报告</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFalsePositive</td>
                    <td>更新网站扫描漏洞的误报状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteGenerateReport</td>
                    <td>生成网站扫描PDF报告</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPortResults</td>
                    <td>获取网站端口扫描结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBusinessRisks</td>
                    <td>获取网站业务风险扫描结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResults</td>
                    <td>获取网站漏洞扫描结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">web_tasks</td>
                    <td>CancelTasks</td>
                    <td>取消或重启网站漏洞扫描任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTasks</td>
                    <td>获取网站漏洞扫描任务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskHistories</td>
                    <td>获取网站漏洞扫描的历史扫描任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">websites</td>
                    <td>DeleteDomains</td>
                    <td>删除租户的网站资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AuthorizeDomains</td>
                    <td>认证租户的网站资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainSettings</td>
                    <td>更新网站登录配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDomains</td>
                    <td>创建租户的网站资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomains</td>
                    <td>获取租户的所有网站资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainSettings</td>
                    <td>获取网站登录配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">云模式防护网站管理</td>
                    <td>DeleteHost</td>
                    <td>删除云模式防护域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">服务作业管理</td>
                    <td>CreateTasks</td>
                    <td>该接口用于创建服务作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">集群管理接口</td>
                    <td>ListHosts</td>
                    <td>该接口用于查询输入集群的主机列表详情。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
