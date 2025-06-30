# SIS MCP Server 


## Version
v0.1.0

## Overview

SIS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SIS. Full-chain management of SIS resources can be carried out based on natural language.

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
                    <td rowspan="5">Hot word management interface</td>
                    <td>DeleteVocabulary</td>
                    <td>Delete a hot word table based on the hot word table ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVocabulary</td>
                    <td>Update a hot word table. If the update is successful, the ID is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVocabulary</td>
                    <td>Query information and content in a hot word table based on the hot word table ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVocabulary</td>
                    <td>Create a hot word table. If the table is created successfully, the ID is returned. A maximum of 10 hot word lists can be created per user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVocabularies</td>
                    <td>Query all hot word lists of a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Speech Recognition Interface</td>
                    <td>RecognizeShortAudio</td>
                    <td>One-sentence recognition interface, which is used for synchronous recognition of short voice. Upload the entire audio at a time, and the recognition result is returned in the response.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectTranscriberJob</td>
                    <td>This interface is used to obtain the recording recognition result and recognition status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PushTranscriberJobs</td>
                    <td>**Recording file recognition* *</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RecognizeFlashAsr</td>
                    <td>Extreme ASR (Restful API, applicable to audio (file size &lt;= 100 MB, voice duration &lt;= 30 minutes)) Synchronous identification of the file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TTS Interface</td>
                    <td>RunTts</td>
                    <td>TTS is a service that converts text into vivid voice. Users can access and invoke APIs in real time to obtain the speech synthesis result and synthesize the text entered by users into audio. Personalized pronunciation services for enterprises and individuals through timbre selection, custom volume, and speed of speech</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
