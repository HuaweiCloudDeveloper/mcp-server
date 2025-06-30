# CBS MCP Server 


## Version
v0.1.0

## Overview

CBS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CBS. Full-chain management of CBS resources can be carried out based on natural language.

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
                    <td rowspan="1">Connection management</td>
                    <td>DeleteSession</td>
                    <td>Terminates the instance node session.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Image management</td>
                    <td>ExecuteGetCharacters</td>
                    <td>TODO:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteGetCharacterInfoById</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Material Management</td>
                    <td>ExecuteUploadImage</td>
                    <td>Upload an image and generate an image link. The image size must be less than 10 m.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteDeleteimageById</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteGetFramsListByImagesId</td>
                    <td>Obtain the list of available playboxes for a specified image.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteUploadPpt</td>
                    <td>Currently, only PDF files can be uploaded. If there is a PPT file, convert it into PDF files and upload it. The file size must be less than 10 MB.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecutePostCreateImages</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteGetImagesList</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteUpdateImageName</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Other Q&amp;A</td>
                    <td>ListSuggestions</td>
                    <td>Obtain the list of prompt questions entered by a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>TagLabor</td>
                    <td>Indicates whether to transfer the call to the manual service after the intelligent Q&amp;A result is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>TagSatisfaction</td>
                    <td>Whether the user is satisfied with the result returned by the intelligent Q&amp;A after asking a question.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Other Q&amp;A API</td>
                    <td>PostRequests</td>
                    <td>The input of the Q&amp;A service is user questions, and the output is top N (by default, top 5) knowledge points that match the input. The knowledge points are sorted by score in descending order.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Question &amp; Answer Bot</td>
                    <td>ExecuteQaChat</td>
                    <td>A user invokes this interface to chat with a bot.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Question &amp; Answer Session</td>
                    <td>CreateSession</td>
                    <td>The Q&amp;A session API consists of three APIs: starting, processing, and closing a session. This API is invoked to create a session. This API can be invoked only by old users. For new users, use the Q&amp;A Bot API first.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteSession</td>
                    <td>The Q&amp;A session API consists of three APIs: starting, processing, and closing a session. Users can call this API to have a session with the robot. This API is about to go offline. Use the Q&amp;A Bot API first to call this API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Question and Answer Statistics</td>
                    <td>CollectReplyRates</td>
                    <td>Query the response rate of a specified domain within a specified time range. Statistics can be collected by period.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectHotQuestions</td>
                    <td>Obtains the list of hot criteria that are completely matched.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectSessionStats</td>
                    <td>Obtains user session statistics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectKeyWords</td>
                    <td>User-asked keyword statistics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Video management</td>
                    <td>ExecuteComposeVideoOndemand</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteUpdateVideoById</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteCreateVideo</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteDeleteVideoById</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteGetVideoInfoById</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteUpdateVideoInfoById</td>
                    <td>This interface is used to configure videos.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteGetVideosList</td>
                    <td>This interface is used to obtain the video list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteComposeVideo</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
