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
                    <td rowspan="4">Predefined label operation</td>
                    <td>CreatePredefineTags</td>
                    <td>Creates a predefined tag. After creating predefined tags, you can use the predefined tags to create tags for resources. This interface supports idempotent features and bulk data processing.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePredefineTags</td>
                    <td>This command is used to delete a predetermined tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePredefineTags</td>
                    <td>Modify the predefined tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPredefineTags</td>
                    <td>Query the list of predefined tags.</td>
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
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowTagQuota</td>
                    <td>Query the quota information about a tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Resource Tag</td>
                    <td>DeleteResourceTag</td>
                    <td>This API is used to remove tags of multiple cloud service resources in batches. A maximum of 10 tags can be removed for each resource. A maximum of 20 tags can be removed at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResource</td>
                    <td>Filter resources by tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceTag</td>
                    <td>Query the tags of a single resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagValues</td>
                    <td>Query all tag values under a tag key in a specified region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagKeys</td>
                    <td>Query all tag keys in a specified region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResourceTag</td>
                    <td>Add tags to multiple cloud service resources. A maximum of 10 tags can be added to each resource. A maximum of 20 tags can be operated at a time.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
