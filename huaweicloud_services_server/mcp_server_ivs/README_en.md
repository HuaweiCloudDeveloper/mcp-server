# IVS MCP Server 


## Version
v0.1.0

## Overview

IVS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IVS. Full-chain management of IVS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Standard Edition of Witness Verification (Three Elements) | DetectStandardByNameAndId | Use the name, ID number, and face image to perform identity verification. | To be tested |
|  | DetectStandardByIdCardImage | Use the front and back images of the ID card to extract the name and ID card number, and perform three-element identity verification with the face image. | To be tested |
|  | DetectStandardByVideoAndIdCardImage | Extract the name and ID card number from the front and back images of the ID card, perform liveness detection on the video, and extract the face image for identity verification. | To be tested |
|  | DetectStandardByVideoAndNameAndId | Use the name and ID card number text, perform liveness detection on the video, and extract face images for identity verification. | To be tested |
| Verified Certificate of Witness (Two Elements) | DetectExtentionByNameAndId | Use the name and ID card number for identity verification. During identity authentication, the input data is ID card information. When extracting ID card information, you can use the front and back pictures of ID card, or directly enter the name and ID card number text. | To be tested |
|  | DetectExtentionByIdCardImage | Use the name and ID card number for identity verification. During identity authentication, the input data is ID card information. When extracting ID card information, you can use the front and back pictures of ID card, or directly enter the name and ID card number text. | To be tested |

