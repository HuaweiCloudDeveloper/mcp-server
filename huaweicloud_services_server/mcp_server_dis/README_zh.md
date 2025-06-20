# DIS MCP Server 

## 版本信息
v0.1.0

## 产品描述

DIS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DIS交互的能力。可以基于自然语言对DIS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| App管理 | ListApp | 本接口用于查询APP列表。 | To be tested |
|  | ShowApp | 本接口用于查询APP详情。 | To be tested |
|  | CreateApp | 本接口用于创建消费APP。 | To be tested |
|  | DeleteApp | 本接口用于删除App。 | To be tested |
|  | ShowConsumerState | 本接口用于查询APP消费状态。 | To be tested |
| Checkpoint管理 | CommitCheckpoint | 本接口用于提交Checkpoint。 | To be tested |
|  | DeleteCheckpoint | 本接口用于删除Checkpoint。 | To be tested |
|  | ShowCheckpoint | 本接口用于查询Checkpoint详情。 | To be tested |
| 数据管理 | SendRecords | 本接口用于上传数据到DIS通道中。 | To be tested |
|  | ConsumeRecords | 本接口用于从DIS通道中下载数据。 | To be tested |
|  | ShowCursor | 本接口用于获取数据游标。 | To be tested |
| 标签管理 | BatchDeleteTags | 该接口用于批量删除资源(通道等)标签。此接口为幂等接口:删除时,如果删除的标签不存在,默认处理成功;删除时不对标签字符集范围做校验。删除时tags结构体不能缺失,key不能为空,或者空字符串。 | To be tested |
|  | ShowStreamTags | 该接口用于查询指定通道的标签信息。 | To be tested |
|  | CreateTag | 本接口用于给指定通道添加标签。 | To be tested |
|  | DeleteTag | 该接口用于删除指定通道的标签。 | To be tested |
|  | ListResourcesByTags | 该接口用于使用标签过滤资源(通道等)。 | To be tested |
|  | ListTags | 该接口用于查询指定区域所有标签集合。 | To be tested |
|  | BatchCreateTags | 该接口用于批量添加资源(通道等)标签。此接口为幂等接口:创建时如果请求体中存在重复key则报错。创建时,不允许设置重复key数据,如果数据库已存在该key,就覆盖value的值。 | To be tested |
| 监控管理 | ShowPartitionMetrics | 本接口用于查询通道指定分区的监控数据。 | To be tested |
|  | ShowStreamMetrics | 本接口用于查询指定通道的监控数据。 | To be tested |
| 转储任务管理 | BatchStartTransferTask | 此接口用于批量启动转储任务。 | To be tested |
|  | DeleteTransferTask | 该接口用于删除转储任务。 | To be tested |
|  | ShowTransferTask | 查询转储任务详情。 | To be tested |
|  | BatchStopTransferTask | 此接口用于批量暂停转储任务。 | To be tested |
|  | CreateDliTransferTask | 本接口用于添加DLI转储任务。 | To be tested |
|  | CreateObsTransferTask | 本接口用于添加OBS转储任务。 | To be tested |
|  | ListTransferTasks | 本接口用于查询转储任务列表。 | To be tested |
|  | CreateMrsTransferTask | 本接口用于添加MRS转储任务。 | To be tested |
|  | CreateCloudTableTransferTask | 本接口用于添加CloudTable转储任务。 | To be tested |
|  | CreateDwsTransferTask | 本接口用于添加DWS转储任务。 | To be tested |
| 通道管理 | CreatePolicies | 本接口用于给指定通道添加权限策略。 | To be tested |
|  | ShowStream | 本接口用于查询指定通道的详情。 | To be tested |
|  | ListStreams | 本接口用户查询当前租户创建的所有通道。 | To be tested |
|  | UpdatePartitionCount | 本接口用于变更指定通道中的分区数量。 | To be tested |
|  | ListPolicies | 本接口用于查询指定通道的权限策略列表。 | To be tested |
|  | CreateStream | 本接口用于创建通道。 | To be tested |
|  | DeleteStream | 本接口用于删除指定通道。 | To be tested |
|  | UpdateStream | 本接口用于更新指定通道的通道信息。 | To be tested |
