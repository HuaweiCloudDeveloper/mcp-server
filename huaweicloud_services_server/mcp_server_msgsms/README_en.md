# MSGSMS MCP Server 


## Version
v0.1.0

## Overview

MSGSMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service MSGSMS. Full-chain management of MSGSMS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AppManagement | ListAppDetails | This interface is used to query information about created applications. | To be tested |
|  | CreateApp | This interface is used by users to create application information. | To be tested |
|  | ShowApp | This interface is used by users to query application details. | To be tested |
|  | ShowAppCount | This interface is used to query the number of applications used by a user. | To be tested |
|  | UpdateApp | This interface is used by users to modify application information. | To be tested |
| SignatureManagement | ShowSignature | This interface is used to query signature details. | To be tested |
|  | ShowSignatureFile | This interface is used by users to query information about uploaded files. | To be tested |
|  | UpdateSignature | This interface is used by users to update signature information. Currently, only the signatures of rejected SMS messages can be modified. | To be tested |
|  | UploadSignatureFile | This interface is used by users to upload file information. | To be tested |
|  | DeleteSignature | This API is used to delete a created signature. | To be tested |
|  | EnableSignature | This interface is used by a user to apply for signature activation information. | To be tested |
|  | CreateSignature | This interface is used by users to create signatures. | To be tested |
|  | ListSignatureDetails | This interface is used to query created SMS signatures. | To be tested |
| TemplateManagement | UpdateTemplate | This interface is used by users to modify template information. Currently, only the SMS templates that are rejected can be modified. | To be tested |
|  | DeleteTemplate | This API is used to delete a created template. | To be tested |
|  | ListSendCountryDetails | This interface is used by users to query the country to which SMS messages are sent. | To be tested |
|  | ShowTemplate | This API is used to query the details of a created template. | To be tested |
|  | ListTemplateDetails | This interface is used to query information about created templates. | To be tested |
|  | ListTemplateVarilableDetails | This interface is used to query template parameters. | To be tested |
|  | CreateTemplate | This interface is used by users to create templates. | To be tested |

