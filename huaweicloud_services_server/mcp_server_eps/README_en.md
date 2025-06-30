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
                    <td rowspan="9">Enterprise Project Management Operation</td>
                    <td>ShowEnterpriseProjectQuota</td>
                    <td>Query the quota information of an enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableEnterpriseProject</td>
                    <td>Enable an enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnterpriseProject</td>
                    <td>Query enterprise project details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnterpriseProject</td>
                    <td>Modify an enterprise project. Currently, only the name and description can be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateResource</td>
                    <td>Migrate resources to the target enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnterpriseProject</td>
                    <td>Create an enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableEnterpriseProject</td>
                    <td>Disable an enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceBindEnterpriseProject</td>
                    <td>Query details about resources bound to an enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnterpriseProject</td>
                    <td>Query the list of authorized enterprise projects of the current user. The user can bind resources to the enterprise projects.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query services supported by tag management</td>
                    <td>ListProviders</td>
                    <td>Query the services supported by tag management.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Query version operation</td>
                    <td>ShowApiVersion</td>
                    <td>Query the details about a specified TMS API version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersions</td>
                    <td>Query the TMS API version list.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
