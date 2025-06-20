# VIAS MCP Server 

## 版本信息
v0.1.0

## 产品描述

VIAS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务VIAS交互的能力。可以基于自然语言对VIAS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| IAlgorithmController | ShowServiceDetail | 获取服务详情 | To be tested |
|  | StopDeployAlgorithm | 停止算法部署 | To be tested |
|  | ListUserServices | 我的算法服务列表 | To be tested |
|  | DeployAlgorithm | 部署算法 | To be tested |
| IBatchTaskController | CreateBatchTask | 新增批量任务 | To be tested |
|  | DeleteBatchTask | 删除批量配置 | To be tested |
|  | ListBatchTasks | 获取批量配置任务列表 | To be tested |
|  | BatchStartStopTask | 启动/停止批量配置任务 | To be tested |
|  | UpdateBatchTask | 修改批量配置任务 | To be tested |
| IEdgePoolController | CreateEdgePool | 创建边缘资源池 | To be tested |
|  | ShowEdgePoolInfo | 查询边缘资源池详情 | To be tested |
|  | DeleteEdgePool | 删除边缘资源池 | To be tested |
|  | ListEdgePools | 查询边缘资源池列表 | To be tested |
| ITaskController | ShowTaskInfo | 用于获取视频智能分析任务详情 | To be tested |
|  | DeleteTask | 删除单个任务 | To be tested |
|  | UpdateTask | 任务修改接口,用于修改任务配置 | To be tested |
|  | CreateTask | 该接口用于创建任务 | To be tested |
|  | StartStopTask | 该接口用于启动或停止任务 | To be tested |
|  | ListTasks | 获取任务列表 | To be tested |
| IVideoGroupController | ShowVideoGroupDetail | 获取视频源分组详情 | To be tested |
|  | UpdateVideoGroup | 更新视频源分组 | To be tested |
|  | DeleteVideoGroup | 删除视频源分组 | To be tested |
|  | ListVideoGroups | 获取视频源分组列表 | To be tested |
|  | CreateVideoGroup | 创建视频源分组 | To be tested |
| IVideoSourceController | CreateVideoSource | 创建视频源 | To be tested |
|  | ListVideoSources | 获取视频源列表 | To be tested |
|  | DeleteVideoSource | 删除视频源 | To be tested |
|  | ShowVideoSourceDetail | 视频源详情展示 | To be tested |
|  | UpdateVideoSource | 修改视频源 | To be tested |
