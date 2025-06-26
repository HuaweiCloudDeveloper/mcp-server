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
                    <td rowspan="1">Lifecycle Management</td>
                    <td>ListInstances</td>
                    <td>Query the instance list of a tenant. Query by condition is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Smart Buying Group Management</td>
                    <td>CreateAutoLaunchGroup</td>
                    <td>Create Smart Buying Group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoLaunchGroup</td>
                    <td>Query the details about a specified smart purchase group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAutoLaunchGroup</td>
                    <td>Delete a specified smart buying group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutoLaunchGroups</td>
                    <td>Obtain all smart purchase groups created by the tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutoLaunchGroup</td>
                    <td>Update the information about a specified smart purchase group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Specification Recommendation Management</td>
                    <td>ListSupplyRecommendation</td>
                    <td>Recommend the region and specifications of ECS resources. The recommendation result is displayed in the form of scores. A higher score indicates a higher recommendation degree.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
