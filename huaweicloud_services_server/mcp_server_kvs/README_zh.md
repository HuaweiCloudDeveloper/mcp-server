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
                    <td rowspan="8">KV接口</td>
                    <td>DeleteKv</td>
                    <td>指定表,指定主键,删除该文档;允许指定条件执行。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PutKv</td>
                    <td>指定表,新建kv或覆盖已有kv,且满足表的key schema描述;允许指定条件执行。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchGetKv</td>
                    <td>批量读请求,其中可以携带一或多个表的不同kv的查询操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetKv</td>
                    <td>下载一个kv文档的全部内容,或者部分字段的内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchWriteKv</td>
                    <td>批量写请求,其中可以携带一或多个表的不同kv的写操作,上传kv/删除kv。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ScanSkeyKv</td>
                    <td>指定表及分区键,携带条件查询kv;允许指定过滤条件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKv</td>
                    <td>指定表,指定主键,指定更新文档的部分内容,如果是自描述文档,指定字段名;如果是二进制文档,指定偏移位置和长度;允许指定条件执行。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ScanKv</td>
                    <td>指定表,扫描表下所有kv;允许指定过滤条件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">仓接口</td>
                    <td>ListStore</td>
                    <td>一个账户下可以创建最多25个仓,每个仓可以创建最多100个store,响应中一次性返回所有仓名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTable</td>
                    <td>在指定仓内创建表,表名在仓内唯一;创建表时,指定主键模板及本地二级索引模板及全局二级索引模板。创建表时,如果仓不存在,将会自动创建仓。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTable</td>
                    <td>指定仓列举创建的所有表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">表接口</td>
                    <td>DeleteTable</td>
                    <td>删除指定表及所有kv文档,表标记为删除后,空间不会立刻释放,并发的读写访问仍需继续完成。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DescribeTable</td>
                    <td>指定仓查询表属性,如容量,规模,配额。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
