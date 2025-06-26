# IVS MCP Server 


## Version
v0.1.0

## Overview

IVS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IVS. Full-chain management of IVS resources can be carried out based on natural language.

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
                    <td rowspan="4">Standard Edition of Witness Verification (Three Elements)</td>
                    <td>DetectStandardByNameAndId</td>
                    <td>Use the name, ID number, and face image to perform identity verification.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectStandardByIdCardImage</td>
                    <td>Use the front and back images of the ID card to extract the name and ID card number, and perform three-element identity verification with the face image.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectStandardByVideoAndIdCardImage</td>
                    <td>Extract the name and ID card number from the front and back images of the ID card, perform liveness detection on the video, and extract the face image for identity verification.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectStandardByVideoAndNameAndId</td>
                    <td>Use the name and ID card number text, perform liveness detection on the video, and extract face images for identity verification.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Verified Certificate of Witness (Two Elements)</td>
                    <td>DetectExtentionByNameAndId</td>
                    <td>Use the name and ID card number for identity verification. During identity authentication, the input data is ID card information. When extracting ID card information, you can use the front and back pictures of ID card, or directly enter the name and ID card number text.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectExtentionByIdCardImage</td>
                    <td>Use the name and ID card number for identity verification. During identity authentication, the input data is ID card information. When extracting ID card information, you can use the front and back pictures of ID card, or directly enter the name and ID card number text.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
