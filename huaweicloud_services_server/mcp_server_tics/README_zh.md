# TICS MCP Server 


## Version
v0.1.0

## Overview

TICS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service TICS. Full-chain management of TICS resources can be carried out based on natural language.

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
                    <td rowspan="3">作业实例管理</td>
                    <td>ShowJobInstanceDag</td>
                    <td>获取实例执行图</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceHistory</td>
                    <td>查询作业的历史实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceReport</td>
                    <td>查询实例执行报告</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">可信节点管理</td>
                    <td>ShowAgentDetail</td>
                    <td>功能描述:用户可以使用该接口获取单个可信计算节点详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgents</td>
                    <td>功能描述:用户可以使用该接口获取可信节点信息列表。支持节点名称与联盟名称的模糊查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">审计日志管理</td>
                    <td>ListAuditInfo</td>
                    <td>查询审计日志信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">数据集管理</td>
                    <td>ListLeagueDatasets</td>
                    <td>功能描述:用户可以使用该接口查询联盟已注册数据集列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">统计信息管理</td>
                    <td>ShowOverview</td>
                    <td>查询当前租户的联盟及代理统计数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPartnerStatistics</td>
                    <td>功能描述:用户可以使用该接口进行联盟合作方统计。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobStatistics</td>
                    <td>功能描述:用户可以使用该接口进行联盟作业统计。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatasetStatistics</td>
                    <td>用户可以使用该接口进行联盟数据集统计。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">联盟管理</td>
                    <td>ListNotices</td>
                    <td>功能描述:用户可以使用该接口查询通知管理列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLeague</td>
                    <td>功能描述:用户可以使用接口更新联盟信息(包含联盟描述,联盟版本,隐私保护等级,查分隐私开关)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPartners</td>
                    <td>功能描述:用户可以使用该接口获取联盟组员信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodes</td>
                    <td>功能描述:用户可以使用该接口查询联盟可信节点(包含聚合节点和计算节点)列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLeagues</td>
                    <td>功能描述:用户可以使用该接口获取联盟列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLeague</td>
                    <td>功能描述:用户可以使用该接口获取联盟详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">联邦分析作业管理</td>
                    <td>ListSqlJob</td>
                    <td>查询联邦分析作业列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">联邦学习作业管理</td>
                    <td>ListFlJob</td>
                    <td>查询联邦学习作业列表</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
