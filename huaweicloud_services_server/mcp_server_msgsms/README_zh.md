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
                    <td>该接口用于用户查询已创建的应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApp</td>
                    <td>该接口用于用户创建应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApp</td>
                    <td>该接口用于用户查询应用详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppCount</td>
                    <td>该接口用于用户查询应用使用的数量信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApp</td>
                    <td>该接口用于用户修改应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">SignatureManagement</td>
                    <td>ShowSignature</td>
                    <td>该接口用于用户查询签名详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSignatureFile</td>
                    <td>该接口用于用户查询上传的文件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSignature</td>
                    <td>该接口用于用户更新签名信息,目前仅支持审核不通过的短信签名重新修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadSignatureFile</td>
                    <td>该接口用于用户上传文件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSignature</td>
                    <td>该接口用于用户删除已创建的签名信息息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableSignature</td>
                    <td>该接口用于用户申请激活签名信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSignature</td>
                    <td>该接口用于用户创建签名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSignatureDetails</td>
                    <td>该接口用于用户查询已创建的短信签名信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">TemplateManagement</td>
                    <td>UpdateTemplate</td>
                    <td>该接口用于用户修改模板信息,目前仅支持审核不通过的短信模板重新修改</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTemplate</td>
                    <td>该接口用于用户删除已创建的模板信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSendCountryDetails</td>
                    <td>该接口用于用户查询短信发送的国家信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTemplate</td>
                    <td>该接口用于用户查询已创建的模板详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplateDetails</td>
                    <td>该接口用于用户查询已创建的模板信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplateVarilableDetails</td>
                    <td>该接口用于用户查询模板参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemplate</td>
                    <td>该接口用于用户创建模板。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
