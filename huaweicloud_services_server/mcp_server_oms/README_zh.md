# OMS MCP Server 

## 版本信息
v0.1.0

## 产品描述

OMS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务OMS交互的能力。可以基于自然语言对OMS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 云服务 | ShowCloudType | 查询所有支持的云厂商 | To be tested |
| 区域 | ShowRegionInfo | 查询云厂商支持的reigon | To be tested |
| 同步任务 | DeleteSyncTask | 调用该接口删除同步任务。 | To be tested |
|  | ListSyncTaskStatistic | 查询指定ID同步任务的接收同步请求对象数、同步成功对象数、同步失败对象数、同步跳过对象数、同步成功对象容量统计数据(目前只支持华北-北京四、华东-上海一地区)。 | To be tested |
|  | CreateSyncTask | 创建同步任务,创建成功后,任务会被自动启动,不需要额外调用启动任务命令。 | To be tested |
|  | CreateSyncEvents | 源端有对象需要进行同步时,调用该接口创建一个同步事件,系统将根据同步事件中包含的对象名称进行同步(目前只支持华北-北京四、华东-上海一地区)。 | To be tested |
|  | StopSyncTask | 当同步任务处于同步中时,调用该接口停止任务(目前只支持华北-北京四、华东-上海一地区)。 | To be tested |
|  | ListSyncTasks | 查询用户名下所有同步任务信息 | To be tested |
|  | StartSyncTask | 同步任务停止后,调用该接口以启动同步任务(目前只支持华北-北京四、华东-上海一地区)。 | To be tested |
|  | ShowSyncTask | 查询指定ID的同步任务详情。 | To be tested |
| 查询API版本信息 | ShowApiInfo | 查询对象存储迁移服务指定API版本信息。 | To be tested |
|  | ListApiVersions | 查询对象存储迁移服务的API版本信息。 | To be tested |
| 桶操作 | ShowBucketRegion | 查询桶对应的region | To be tested |
|  | ShowBucketObjects | 查询桶对象列表 | To be tested |
|  | ShowBucketList | 查询桶列表 | To be tested |
|  | CheckPrefix | 检查前缀是否在源端桶中存在 | To be tested |
|  | ShowCdnInfo | 查桶对应的CDN信息 | To be tested |
| 迁移任务管理 | DeleteTask | 调用该接口删除迁移任务。 | To be tested |
|  | CreateTask | 创建迁移任务,创建成功后,任务会被自动启动,不需要额外调用启动任务命令。 | To be tested |
|  | ListTasks | 查询用户账户下的所有任务信息。 | To be tested |
|  | BatchUpdateTasks | 批量更新迁移任务,可指定单个迁移任务组下所有的迁移任务或通过迁移任务ID来执行。 | To be tested |
|  | StopTask | 当迁移任务处于迁移中时,调用该接口停止任务。 | To be tested |
|  | ShowTask | 查询指定ID的任务详情。 | To be tested |
|  | UpdateBandwidthPolicy | 当迁移任务未执行完成时,修改迁移任务的流量控制策略。 | To be tested |
|  | StartTask | 迁移任务暂停或失败后,调用该接口以启动任务。 | To be tested |
| 迁移任务组管理 | StopTaskGroup | 当迁移任务组处于创建任务中或监控中时,调用该接口暂停指定迁移任务组。 | To be tested |
|  | DeleteTaskGroup | 删除指定的迁移任务组. | To be tested |
|  | UpdateTaskGroup | 当迁移任务组未执行完成时,修改迁移任务组的流量控制策略。 | To be tested |
|  | ShowTaskGroup | 获取指定id的taskgroup信息 | To be tested |
|  | RetryTaskGroup | 当迁移任务组处于迁移失败状态时,调用该接口重启指定id的迁移任务组。 | To be tested |
|  | StartTaskGroup | 当迁移任务组处于暂停状态时,调用该接口启动指定id的迁移任务组。 | To be tested |
|  | CreateTaskGroup | 创建迁移任务组,创建成功后,迁移任务组会自动创建迁移任务,不需要额外调用启动任务命令。 | To be tested |
|  | ListTaskGroup | 查询用户账户下的任务组信息 | To be tested |
