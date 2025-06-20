# KVS MCP Server 


## Version
v0.1.0

## Overview

KVS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service KVS. Full-chain management of KVS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| KV interface | DeleteKv | Delete the document by specifying the table and primary key. Allows the specified conditions to be executed. | To be tested |
|  | PutKv | Specify a table. Create a new KV or overwrite an existing KV, and ensure that the table meets the key schema description. Allows the specified conditions to be executed. | To be tested |
|  | BatchGetKv | Batch read request, which can carry different KV query operations of one or more tables. | To be tested |
|  | GetKv | Downloads all or some fields in a KV file. | To be tested |
|  | BatchWriteKv | Batch write request, which can carry different KV write operations of one or more tables, such as uploading KV and deleting KV. | To be tested |
|  | ScanSkeyKv | Specify the table and partition key, and query the KV by conditions. Allows you to specify filter criteria. | To be tested |
|  | UpdateKv | Specify a table, specify a primary key, and specify a part of the document to be updated. For a self-description document, specify a field name. For a binary document, specify the offset position and length. Allows the specified conditions to be executed. | To be tested |
|  | ScanKv | Specify a table and scan all KVs in the table. Allows you to specify filter criteria. | To be tested |
| Table interface | DeleteTable | This API is used to delete a specified table and all KV documents. After the table is marked as deleted, the space is not released immediately. Concurrent read and write operations still need to be completed. | To be tested |
|  | DescribeTable | Query table attributes, such as the capacity, scale, and quota, in the specified warehouse. | To be tested |
| Warehouse interface | ListStore | A maximum of 25 warehouses can be created under an account, and a maximum of 100 stores can be created for each warehouse. All warehouse names are returned in the response. | To be tested |
|  | CreateTable | Create a table in the specified repository. The table name is unique in the repository. When creating a table, you need to specify the primary key profile, local secondary index profile, and global secondary index profile. When you create a table, if the warehouse does not exist, the warehouse will be created automatically. | To be tested |
|  | ListTable | Specify the repository to list all created tables. | To be tested |

