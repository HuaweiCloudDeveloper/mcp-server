# KVS MCP Server 


## Version
v0.1.0

## Overview

KVS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service KVS. Full-chain management of KVS resources can be carried out based on natural language.

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
                    <td rowspan="8">KV interface</td>
                    <td>DeleteKv</td>
                    <td>Delete the document by specifying the table and primary key. Allows the specified conditions to be executed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PutKv</td>
                    <td>Specify a table. Create a new KV or overwrite an existing KV, and ensure that the table meets the key schema description. Allows the specified conditions to be executed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchGetKv</td>
                    <td>Batch read request, which can carry different KV query operations of one or more tables.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetKv</td>
                    <td>Downloads all or some fields in a KV file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchWriteKv</td>
                    <td>Batch write request, which can carry different KV write operations of one or more tables, such as uploading KV and deleting KV.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ScanSkeyKv</td>
                    <td>Specify the table and partition key, and query the KV by conditions. Allows you to specify filter criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKv</td>
                    <td>Specify a table, specify a primary key, and specify a part of the document to be updated. For a self-description document, specify a field name. For a binary document, specify the offset position and length. Allows the specified conditions to be executed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ScanKv</td>
                    <td>Specify a table and scan all KVs in the table. Allows you to specify filter criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Table interface</td>
                    <td>DeleteTable</td>
                    <td>This API is used to delete a specified table and all KV documents. After the table is marked as deleted, the space is not released immediately. Concurrent read and write operations still need to be completed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DescribeTable</td>
                    <td>Query table attributes, such as the capacity, scale, and quota, in the specified warehouse.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Warehouse interface</td>
                    <td>ListStore</td>
                    <td>A maximum of 25 warehouses can be created under an account, and a maximum of 100 stores can be created for each warehouse. All warehouse names are returned in the response.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTable</td>
                    <td>Create a table in the specified repository. The table name is unique in the repository. When creating a table, you need to specify the primary key profile, local secondary index profile, and global secondary index profile. When you create a table, if the warehouse does not exist, the warehouse will be created automatically.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTable</td>
                    <td>Specify the repository to list all created tables.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
