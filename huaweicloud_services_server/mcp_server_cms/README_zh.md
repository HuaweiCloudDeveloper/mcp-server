# CMS MCP Server 


## Version
v0.1.0

## Overview

CMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CMS. Full-chain management of CMS resources can be carried out based on natural language.

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
                    <td rowspan="5">智能购买组管理</td>
                    <td>CreateAutoLaunchGroup</td>
                    <td>创建智能购买组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoLaunchGroup</td>
                    <td>查询指定智能购买组的详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAutoLaunchGroup</td>
                    <td>删除指定的智能购买组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutoLaunchGroups</td>
                    <td>获取租户创建的所有的智能购买组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutoLaunchGroup</td>
                    <td>更新指定智能购买组信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">生命周期管理</td>
                    <td>ListInstances</td>
                    <td>查询租户的实例列表,支持按照条件查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">规格推荐管理</td>
                    <td>ListSupplyRecommendation</td>
                    <td>对ECS的资源供给的地域和规格进行推荐,推荐结果以打分的形式呈现,分数越高推荐程度越高</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
