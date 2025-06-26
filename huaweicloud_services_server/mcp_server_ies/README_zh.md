# IES MCP Server 


## Version
v0.1.0

## Overview

IES MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IES. Full-chain management of IES resources can be carried out based on natural language.

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
                    <td rowspan="5">edge-site</td>
                    <td>ListEdgeSites</td>
                    <td>查询边缘小站列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeSite</td>
                    <td>查询边缘小站详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeSite</td>
                    <td>更新边缘小站。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeSite</td>
                    <td>创建边缘小站。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeSite</td>
                    <td>删除指定的边缘小站。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">monitor</td>
                    <td>ListEdgeSiteMetrics</td>
                    <td>查看站点容量信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">rack</td>
                    <td>ShowRack</td>
                    <td>查询机柜详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRacks</td>
                    <td>查询机柜列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">region</td>
                    <td>ListSupportedRegions</td>
                    <td>查询支持智能边缘小站接入的华为云区域(region)列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">storage-pool</td>
                    <td>ShowStoragePool</td>
                    <td>查询存储池详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStoragePools</td>
                    <td>查询存储池列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额管理</td>
                    <td>ListQuotas</td>
                    <td>获取配额信息</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
