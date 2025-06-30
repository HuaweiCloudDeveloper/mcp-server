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
                    <td rowspan="5">热词管理接口</td>
                    <td>DeleteVocabulary</td>
                    <td>通过热词表id删除热词表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVocabulary</td>
                    <td>更新一个热词表,更新成功返回id。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVocabulary</td>
                    <td>通过热词表id查询热词表的信息和内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVocabulary</td>
                    <td>新建一个热词表,创建成功返回id。每个用户限制创建10个热词表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVocabularies</td>
                    <td>查询用户所有热词表列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">语音合成接口</td>
                    <td>RunTts</td>
                    <td>语音合成,是一种将文本转换成逼真语音的服务。用户通过实时访问和调用API获取语音合成结果,将用户输入的文字合成为音频。通过音色选择、自定义音量、语速,为企业和个人提供个性化的发音服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">语音识别接口</td>
                    <td>RecognizeShortAudio</td>
                    <td>一句话识别接口,用于短语音的同步识别。一次性上传整个音频,响应中即返回识别结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectTranscriberJob</td>
                    <td>该接口用于获取录音文件识别结果及识别状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PushTranscriberJobs</td>
                    <td>**录音文件识别**</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RecognizeFlashAsr</td>
                    <td>极速版ASR(Restful API 接口, 适用于音频(文件大小&lt;=100M,语音时长&lt;=30分钟)文件的同步识别。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
