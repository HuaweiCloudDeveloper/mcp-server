# Moderation MCP Server 


## Version
v0.1.0

## Overview

Moderation MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service Moderation. Full-chain management of Moderation resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| API for synchronizing image review in batches | BatchCheckImageSync | API for synchronizing image review in batches | To be tested |
| Audio Stream Content Moderation | RunCloseAudioStreamModerationJob | Disable the ACM job | To be tested |
|  | RunCreateAudioStreamModerationJob | Create an ACM job. If the job is created successfully, the job ID will be returned to the user. | To be tested |
| Audio content moderation | RunQueryAudioModerationJob |  | To be tested |
|  | RunCreateAudioModerationJob | Analyzes and identifies whether the audio content uploaded by the user contains sensitive content (such as pornographic and political content), and returns the identification result to the user. | To be tested |
| Image Moderation | CheckImageModeration | Analyze and identify whether the image content uploaded by the user contains sensitive content. (e.g. violent terrorist elements, pornographic content, etc.) and return the recognition result to the user. | To be tested |
| Text Moderation | RunTextModeration | Analyzes and identifies whether the uploaded text content contains sensitive content (such as pornographic and political content), and returns the identification result to the user. | To be tested |
| Video Moderation | RunCreateVideoModerationJob | Create a Video Content Moderation job. If the job is successfully created, the job ID will be returned to the user. | To be tested |
|  | RunQueryVideoModerationJob | Query the processing status and result of the video moderation job and return the recognition result to the user | To be tested |

