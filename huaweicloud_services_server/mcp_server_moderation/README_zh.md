# Moderation MCP Server 


## Version
v0.1.0

## Overview

Moderation MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service Moderation. Full-chain management of Moderation resources can be carried out based on natural language.

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
                    <td rowspan="1">图像内容审核</td>
                    <td>CheckImageModeration</td>
                    <td>分析并识别用户上传的图像内容是否有敏感内容(如涉及暴恐元素、涉黄内容等),并将识别结果返回给用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">图像审核批量同步接口</td>
                    <td>BatchCheckImageSync</td>
                    <td>图像审核批量同步接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">文本内容审核</td>
                    <td>RunTextModeration</td>
                    <td>分析并识别用户上传的文本内容是否有敏感内容(如色情、政治等),并将识别结果返回给用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">视频内容审核</td>
                    <td>RunCreateVideoModerationJob</td>
                    <td>创建视频内容审核作业,创建成功会将作业ID返回给用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunQueryVideoModerationJob</td>
                    <td>查询视频审核作业处理状态与结果,并将识别结果返回给用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">音频内容审核</td>
                    <td>RunQueryAudioModerationJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunCreateAudioModerationJob</td>
                    <td>分析并识别用户上传的音频内容是否有敏感内容(如色情、政治等),并将识别结果返回给用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">音频流内容审核</td>
                    <td>RunCloseAudioStreamModerationJob</td>
                    <td>关闭音频流内容审核作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunCreateAudioStreamModerationJob</td>
                    <td>创建音频流内容审核作业,创建成功会将作业ID返回给用户</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
