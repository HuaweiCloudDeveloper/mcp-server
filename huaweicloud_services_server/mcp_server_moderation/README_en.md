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
                    <td rowspan="1">API for synchronizing image review in batches</td>
                    <td>BatchCheckImageSync</td>
                    <td>API for synchronizing image review in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Audio Stream Content Moderation</td>
                    <td>RunCloseAudioStreamModerationJob</td>
                    <td>Disable the ACM job</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunCreateAudioStreamModerationJob</td>
                    <td>Create an ACM job. If the job is created successfully, the job ID will be returned to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Audio content moderation</td>
                    <td>RunQueryAudioModerationJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunCreateAudioModerationJob</td>
                    <td>Analyzes and identifies whether the audio content uploaded by the user contains sensitive content (such as pornographic and political content), and returns the identification result to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Image Moderation</td>
                    <td>CheckImageModeration</td>
                    <td>Analyze and identify whether the image content uploaded by the user contains sensitive content. (e.g. violent terrorist elements, pornographic content, etc.) and return the recognition result to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Text Moderation</td>
                    <td>RunTextModeration</td>
                    <td>Analyzes and identifies whether the uploaded text content contains sensitive content (such as pornographic and political content), and returns the identification result to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Video Moderation</td>
                    <td>RunCreateVideoModerationJob</td>
                    <td>Create a Video Content Moderation job. If the job is successfully created, the job ID will be returned to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunQueryVideoModerationJob</td>
                    <td>Query the processing status and result of the video moderation job and return the recognition result to the user</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
