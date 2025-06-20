# CloudPipeline MCP Server 

## 版本信息
v0.1.0

## 产品描述

CloudPipeline MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CloudPipeline交互的能力。可以基于自然语言对CloudPipeline资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 模板管理 | ListTemplates | 查询模板列表,支持分页查询,支持模板名字模糊查询 | To be tested |
|  | ShowTemplateDetail | 查询模板详情 | To be tested |
| 流水线模板管理--新 | ListPipelineTemplates | 查询流水线模板列表 | To be tested |
|  | ShowPipelineTemplateDetail | 查询模板详情 | To be tested |
| 流水线管理 | CreatePipelineByTemplate | 基于模板快速创建流水线及流水线内任务 | To be tested |
|  | ListPipleineBuildResult | 获取项目下流水线执行状况 | To be tested |
|  | StartNewPipeline | 启动流水线 | To be tested |
|  | ShowPipleineStatus | 获取流水线状态,阶段及任务信息 | To be tested |
|  | RemovePipeline | 根据id删除流水线 | To be tested |
|  | StopPipelineNew | 停止流水线 | To be tested |
|  | ShowInstanceStatus | 检查流水线创建状态 | To be tested |
|  | BatchShowPipelinesStatus | 批量获取流水线状态和阶段信息 | To be tested |
|  | ListPipelineSimpleInfo | 获取流水线列表接口 | To be tested |
| 流水线管理--新 | CreatePipelineByTemplateId | 基于模板创建流水线 | To be tested |
|  | StopPipelineRun | 停止流水线 | To be tested |
|  | ListPipelines | 获取流水线列表/获取项目下流水线执行状况 | To be tested |
|  | BatchShowPipelinesLatestStatus | 批量获取流水线状态 | To be tested |
|  | ListPipelineRuns | 获取流水线执行记录 | To be tested |
|  | DeletePipeline | 删除流水线 | To be tested |
|  | ShowPipelineRunDetail | 获取流水线状态/获取流水线执行详情 | To be tested |
|  | RunPipeline | 启动流水线 | To be tested |
