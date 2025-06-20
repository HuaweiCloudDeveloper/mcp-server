# KVS MCP Server 

## 版本信息
v0.1.0

## 产品描述

KVS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务KVS交互的能力。可以基于自然语言对KVS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| KV接口 | DeleteKv | 指定表,指定主键,删除该文档;允许指定条件执行。 | To be tested |
|  | PutKv | 指定表,新建kv或覆盖已有kv,且满足表的key schema描述;允许指定条件执行。 | To be tested |
|  | BatchGetKv | 批量读请求,其中可以携带一或多个表的不同kv的查询操作。 | To be tested |
|  | GetKv | 下载一个kv文档的全部内容,或者部分字段的内容。 | To be tested |
|  | BatchWriteKv | 批量写请求,其中可以携带一或多个表的不同kv的写操作,上传kv/删除kv。 | To be tested |
|  | ScanSkeyKv | 指定表及分区键,携带条件查询kv;允许指定过滤条件。 | To be tested |
|  | UpdateKv | 指定表,指定主键,指定更新文档的部分内容,如果是自描述文档,指定字段名;如果是二进制文档,指定偏移位置和长度;允许指定条件执行。 | To be tested |
|  | ScanKv | 指定表,扫描表下所有kv;允许指定过滤条件。 | To be tested |
| 仓接口 | ListStore | 一个账户下可以创建最多25个仓,每个仓可以创建最多100个store,响应中一次性返回所有仓名称。 | To be tested |
|  | CreateTable | 在指定仓内创建表,表名在仓内唯一;创建表时,指定主键模板及本地二级索引模板及全局二级索引模板。创建表时,如果仓不存在,将会自动创建仓。 | To be tested |
|  | ListTable | 指定仓列举创建的所有表。 | To be tested |
| 表接口 | DeleteTable | 删除指定表及所有kv文档,表标记为删除后,空间不会立刻释放,并发的读写访问仍需继续完成。 | To be tested |
|  | DescribeTable | 指定仓查询表属性,如容量,规模,配额。 | To be tested |
