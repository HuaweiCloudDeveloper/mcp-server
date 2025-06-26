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
                    <td rowspan="3">其他问答</td>
                    <td>ListSuggestions</td>
                    <td>获取用户输入问题的提示问题列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>TagLabor</td>
                    <td>智能问答返回的结果后,用户是否转人工。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>TagSatisfaction</td>
                    <td>用户提出问题后,对智能问答返回的结果是否满意。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">其他问答API</td>
                    <td>PostRequests</td>
                    <td>问答服务的输入为用户提问,输出是与输入最匹配的Top N(默认为top5)个知识点,知识点按得分从高到低排序。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">形象管理</td>
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
                    <td rowspan="7">素材管理</td>
                    <td>ExecuteUploadImage</td>
                    <td>上传图片并生成图片链接,图片需小于10m;</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteDeleteimageById</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteGetFramsListByImagesId</td>
                    <td>获取指定图片可用的播报框列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteUploadPpt</td>
                    <td>当前仅支持上传PDF,如有PPT请将PPT转化为PDF再进行上传,文件需小于10m;</td>
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
                    <td rowspan="8">视频管理</td>
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
                    <td>通过该接口配置视频</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteGetVideosList</td>
                    <td>该接口用于获取视频列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteComposeVideo</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">连接管理</td>
                    <td>DeleteSession</td>
                    <td>终结实例节点会话。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">问答会话</td>
                    <td>CreateSession</td>
                    <td>问答会话API由开启会话、处理会话、关闭会话三个接口组成。用户可通过调用该接口创建会话。该接口仅支持老用户,新用户请优先使用问答机器人API接口进行调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteSession</td>
                    <td>问答会话API由开启会话、处理会话、关闭会话三个接口组成。用户可通过调用该接口与机器人进行会话。该接口即将下线,请优先使用问答机器人API接口进行调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">问答机器人</td>
                    <td>ExecuteQaChat</td>
                    <td>用户调用该接口和机器人进行聊天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">问答统计</td>
                    <td>CollectReplyRates</td>
                    <td>指定领域获取指定时间范围内的问题答复率,支持按周期统计。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectHotQuestions</td>
                    <td>获取完全匹配的热点标准问题列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectSessionStats</td>
                    <td>获取用户会话统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectKeyWords</td>
                    <td>用户问关键词统计。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
