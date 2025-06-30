# MSGSMS MCP Server 


## Version
v0.1.0

## Overview

MSGSMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service MSGSMS. Full-chain management of MSGSMS resources can be carried out based on natural language.

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
                    <td rowspan="5">AppManagement</td>
                    <td>ListAppDetails</td>
                    <td>This interface is used to query information about created applications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApp</td>
                    <td>This interface is used by users to create application information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApp</td>
                    <td>This interface is used by users to query application details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppCount</td>
                    <td>This interface is used to query the number of applications used by a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApp</td>
                    <td>This interface is used by users to modify application information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">SignatureManagement</td>
                    <td>ShowSignature</td>
                    <td>This interface is used to query signature details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSignatureFile</td>
                    <td>This interface is used by users to query information about uploaded files.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSignature</td>
                    <td>This interface is used by users to update signature information. Currently, only the signatures of rejected SMS messages can be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadSignatureFile</td>
                    <td>This interface is used by users to upload file information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSignature</td>
                    <td>This API is used to delete a created signature.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableSignature</td>
                    <td>This interface is used by a user to apply for signature activation information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSignature</td>
                    <td>This interface is used by users to create signatures.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSignatureDetails</td>
                    <td>This interface is used to query created SMS signatures.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">TemplateManagement</td>
                    <td>UpdateTemplate</td>
                    <td>This interface is used by users to modify template information. Currently, only the SMS templates that are rejected can be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTemplate</td>
                    <td>This API is used to delete a created template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSendCountryDetails</td>
                    <td>This interface is used by users to query the country to which SMS messages are sent.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTemplate</td>
                    <td>This API is used to query the details of a created template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplateDetails</td>
                    <td>This interface is used to query information about created templates.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplateVarilableDetails</td>
                    <td>This interface is used to query template parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemplate</td>
                    <td>This interface is used by users to create templates.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
