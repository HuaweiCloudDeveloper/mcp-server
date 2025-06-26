# EPS MCP Server 


## Version
v0.1.0

## Overview

EPS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EPS. Full-chain management of EPS resources can be carried out based on natural language.

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
                    <td rowspan="9">企业项目管理操作</td>
                    <td>ShowEnterpriseProjectQuota</td>
                    <td>查询企业项目的配额信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableEnterpriseProject</td>
                    <td>启用企业项目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnterpriseProject</td>
                    <td>查询企业项目详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnterpriseProject</td>
                    <td>修改企业项目。当前仅支持修改名称和描述。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateResource</td>
                    <td>迁移资源到目标企业项目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnterpriseProject</td>
                    <td>创建企业项目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableEnterpriseProject</td>
                    <td>停用企业项目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceBindEnterpriseProject</td>
                    <td>查询企业项目下绑定的资源详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnterpriseProject</td>
                    <td>查询当前用户已授权的企业项目列表,用户可以使用企业项目绑定资源。</td>
                    <td>To be tested</td>
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
            </tbody>
        </table>
    </body>
</html>
