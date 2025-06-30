# RGC MCP Server 


## Version
v0.1.0

## Overview

RGC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RGC. Full-chain management of RGC resources can be carried out based on natural language.

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
                    <td rowspan="5">Governance</td>
                    <td>DisableControl</td>
                    <td>关闭组织下的某个单元的某个控制策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListControlsForOrganizationalUnit</td>
                    <td>列出组织里某个注册OU开启的所有控制策略信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowControlOperate</td>
                    <td>根据操作ID查询返回指定ID的操作状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableControl</td>
                    <td>给组织下的某个单元开启某个控制策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnabledControls</td>
                    <td>列出组织里开启的所有控制策略信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">ManagedOrganization</td>
                    <td>RegisterOrganizationalUnit</td>
                    <td>将组织里的某个OU注册到RGC服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOperation</td>
                    <td>查询在RGC服务里注册/取消注册的过程信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowManagedAccount</td>
                    <td>查询组织里某个纳管账号信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAccount</td>
                    <td>在组织里的某个注册OU下创建账号。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
