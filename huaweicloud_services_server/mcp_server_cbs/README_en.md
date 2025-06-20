# CBS MCP Server 


## Version
v0.1.0

## Overview

CBS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CBS. Full-chain management of CBS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Connection management | DeleteSession | Terminates the instance node session. | To be tested |
| Image management | ExecuteGetCharacters | TODO: | To be tested |
|  | ExecuteGetCharacterInfoById |  | To be tested |
| Material Management | ExecuteUploadImage | Upload an image and generate an image link. The image size must be less than 10 m. | To be tested |
|  | ExecuteDeleteimageById |  | To be tested |
|  | ExecuteGetFramsListByImagesId | Obtain the list of available playboxes for a specified image. | To be tested |
|  | ExecuteUploadPpt | Currently, only PDF files can be uploaded. If there is a PPT file, convert it into PDF files and upload it. The file size must be less than 10 MB. | To be tested |
|  | ExecutePostCreateImages |  | To be tested |
|  | ExecuteGetImagesList |  | To be tested |
|  | ExecuteUpdateImageName |  | To be tested |
| Other Q&A | ListSuggestions | Obtain the list of prompt questions entered by a user. | To be tested |
|  | TagLabor | Indicates whether to transfer the call to the manual service after the intelligent Q&A result is returned. | To be tested |
|  | TagSatisfaction | Whether the user is satisfied with the result returned by the intelligent Q&A after asking a question. | To be tested |
| Other Q&A API | PostRequests | The input of the Q&A service is user questions, and the output is top N (by default, top 5) knowledge points that match the input. The knowledge points are sorted by score in descending order. | To be tested |
| Question & Answer Bot | ExecuteQaChat | A user invokes this interface to chat with a bot. | To be tested |
| Question & Answer Session | CreateSession | The Q&A session API consists of three APIs: starting, processing, and closing a session. This API is invoked to create a session. This API can be invoked only by old users. For new users, use the Q&A Bot API first. | To be tested |
|  | ExecuteSession | The Q&A session API consists of three APIs: starting, processing, and closing a session. Users can call this API to have a session with the robot. This API is about to go offline. Use the Q&A Bot API first to call this API. | To be tested |
| Question and Answer Statistics | CollectReplyRates | Query the response rate of a specified domain within a specified time range. Statistics can be collected by period. | To be tested |
|  | CollectHotQuestions | Obtains the list of hot criteria that are completely matched. | To be tested |
|  | CollectSessionStats | Obtains user session statistics. | To be tested |
|  | CollectKeyWords | User-asked keyword statistics. | To be tested |
| Video management | ExecuteComposeVideoOndemand |  | To be tested |
|  | ExecuteUpdateVideoById |  | To be tested |
|  | ExecuteCreateVideo |  | To be tested |
|  | ExecuteDeleteVideoById |  | To be tested |
|  | ExecuteGetVideoInfoById |  | To be tested |
|  | ExecuteUpdateVideoInfoById | This interface is used to configure videos. | To be tested |
|  | ExecuteGetVideosList | This interface is used to obtain the video list. | To be tested |
|  | ExecuteComposeVideo |  | To be tested |

