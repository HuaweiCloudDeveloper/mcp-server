# SIS MCP Server 


## Version
v0.1.0

## Overview

SIS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SIS. Full-chain management of SIS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Hot word management interface | DeleteVocabulary | Delete a hot word table based on the hot word table ID. | To be tested |
|  | UpdateVocabulary | Update a hot word table. If the update is successful, the ID is returned. | To be tested |
|  | ShowVocabulary | Query information and content in a hot word table based on the hot word table ID. | To be tested |
|  | CreateVocabulary | Create a hot word table. If the table is created successfully, the ID is returned. A maximum of 10 hot word lists can be created per user. | To be tested |
|  | ShowVocabularies | Query all hot word lists of a user. | To be tested |
| Speech Recognition Interface | RecognizeShortAudio | One-sentence recognition interface, which is used for synchronous recognition of short voice. Upload the entire audio at a time, and the recognition result is returned in the response. | To be tested |
|  | CollectTranscriberJob | This interface is used to obtain the recording recognition result and recognition status. | To be tested |
|  | PushTranscriberJobs | **Recording file recognition* * | To be tested |
|  | RecognizeFlashAsr | Extreme ASR (Restful API, applicable to audio (file size <= 100 MB, voice duration <= 30 minutes)) Synchronous identification of the file. | To be tested |
| TTS Interface | RunTts | TTS is a service that converts text into vivid voice. Users can access and invoke APIs in real time to obtain the speech synthesis result and synthesize the text entered by users into audio. Personalized pronunciation services for enterprises and individuals through timbre selection, custom volume, and speed of speech | To be tested |

