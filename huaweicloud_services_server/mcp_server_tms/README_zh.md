# TMS MCP Server 


## Version
v0.1.0

## Overview

TMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service TMS. Full-chain management of TMS resources can be carried out based on natural language.

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
                    <td rowspan="1">查询标签管理支持的服务</td>
                    <td>ListProviders</td>
                    <td>查询标签管理支持的服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">查询版本操作</td>
                    <td>ShowApiVersion</td>
                    <td>查询指定的标签管理服务API版本号详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersions</td>
                    <td>查询标签管理服务的API版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">资源标签</td>
                    <td>DeleteResourceTag</td>
                    <td>用于批量移除云服务多个资源的标签,每个资源最多支持移除10个标签,每次最多支持批量操作20个资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResource</td>
                    <td>根据标签过滤资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceTag</td>
                    <td>查询单个资源上的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagValues</td>
                    <td>查询指定区域的标签键下的所有标签值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagKeys</td>
                    <td>查询指定区域的所有标签键.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResourceTag</td>
                    <td>用于给云服务的多个资源添加标签,每个资源最多可添加10个标签,每次最多支持批量操作20个资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowTagQuota</td>
                    <td>查询标签的配额信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">预定义标签操作</td>
                    <td>CreatePredefineTags</td>
                    <td>用于创建预定标签。用户创建预定义标签后,可以使用预定义标签来给资源创建标签。该接口支持幂等特性和处理批量数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePredefineTags</td>
                    <td>用于删除预定标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePredefineTags</td>
                    <td>修改预定义标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPredefineTags</td>
                    <td>用于查询预定义标签列表。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
