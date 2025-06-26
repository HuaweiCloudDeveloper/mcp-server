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
                    <td>Disable a control policy for a unit in an organization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListControlsForOrganizationalUnit</td>
                    <td>Lists all control policies enabled by a registered OU in the organization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowControlOperate</td>
                    <td>Query the operation status based on the operation ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableControl</td>
                    <td>Enable a control policy for a unit in an organization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnabledControls</td>
                    <td>Lists all enabled control policies in the organization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">ManagedOrganization</td>
                    <td>RegisterOrganizationalUnit</td>
                    <td>Register an OU in the organization with the RGC service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOperation</td>
                    <td>Query the registration and deregistration process information in the RGC service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowManagedAccount</td>
                    <td>Query information about a management account in an organization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAccount</td>
                    <td>Create an account under a registered OU in the organization.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
