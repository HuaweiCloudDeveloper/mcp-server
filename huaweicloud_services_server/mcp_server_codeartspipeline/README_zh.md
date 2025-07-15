# CodeArtsPipeline MCP Server 

## 版本信息
v0.1.0

## 产品描述

CodeArtsPipeline MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CodeArtsPipeline交互的能力。可以基于自然语言对CodeArtsPipeline资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 扩展插件管理 | CreatePublisher | 创建发布商 | To be tested |
|  | UploadBasicPlugin | 上传基础插件 | To be tested |
|  | ShowPluginVersion | 查询插件版本详情 | To be tested |
|  | DeletePublisher | 删除发布商 | To be tested |
|  | CreatePluginVersion | 创建插件版本 | To be tested |
|  | ListBasePluginsNewPost | 分页查询可选插件列表 | To be tested |
|  | DeleteBasicPlugin | 删除基础插件 | To be tested |
|  | ShowBasicPlugin | 查询基础插件详情 | To be tested |
|  | ListAvailablePublisher | 查询可用发布商 | To be tested |
|  | ShowPublisher | 查询发布商详情 | To be tested |
|  | UpdatePluginBaseInfo | 更新插件基本信息 | To be tested |
|  | ListPLuginVersion | 查询插件所有版本信息 | To be tested |
|  | UploadPluginIcon | 更新插件图标 | To be tested |
|  | ListPlugins | 查询插件列表 | To be tested |
|  | UploadPublisherIcon | 更新发布商图标 | To be tested |
|  | CreatePluginDraft | 创建插件草稿版本 | To be tested |
|  | UpdatePluginDraft | 更新插件草稿 | To be tested |
|  | ListStagePlugins | 查询可选插件列表 | To be tested |
|  | ShowPluginOutputs | 查询插件输出配置 | To be tested |
|  | ListPublisher | 查询发布商列表 | To be tested |
|  | DeletePluginDraft | 删除插件草稿 | To be tested |
|  | PublishPluginDraft | 发布插件草稿 | To be tested |
|  | ShowPluginInputs | 查询插件输入配置 | To be tested |
|  | PublishPlugin | 发布插件 | To be tested |
|  | PublishPluginBind | 插件绑定发布商 | To be tested |
|  | UpdateBasicPlugin | 更新基础插件 | To be tested |
|  | ListPluginVersionNumber | 查询插件版本号 | To be tested |
|  | ShowPluginMetrics | 查询插件指标配置 | To be tested |
|  | CreateBasicPlugin | 创建基础插件 | To be tested |
|  | ListBasePlugins | 查询基础插件列表 | To be tested |
| 模板管理 | ListTemplates | 查询模板列表,支持分页查询,支持模板名字模糊查询 | To be tested |
|  | ShowTemplateDetail | 查询模板详情 | To be tested |
| 流水线分组管理 | UpdatePipelineGroup | 更新流水线分组 | To be tested |
|  | ShowPipelineGroupTree | 查询流水线分组树 | To be tested |
|  | CreatePipelineGroup | 新建流水线分组 | To be tested |
|  | BatchMovePipelineToGroup | 批量把流水线移动到分组下 | To be tested |
|  | DeletePipelineGroup | 删除流水线分组 | To be tested |
| 流水线模板管理--新 | DeletePipelineTemplate | 删除流水线模板 | To be tested |
|  | ShowPipelineTemplateDetail | 查询模板详情 | To be tested |
|  | UpdatePipelineTemplate | 更新流水线模板 | To be tested |
|  | ListPipelineTemplates | 查询流水线模板列表 | To be tested |
|  | CreatePipelineTemplate | 创建流水线模板 | To be tested |
| 流水线管理 | ShowPipelineDetail | 查询流水线详情 | To be tested |
|  | UpdatePipelineInfo | 修改流水线信息 | To be tested |
|  | ListPipleineBuildResult | 获取项目下流水线执行状况 | To be tested |
|  | ListPipelineSimpleInfo | 获取流水线列表接口 | To be tested |
|  | StartNewPipeline | 启动流水线 | To be tested |
|  | RemovePipeline | 根据id删除流水线 | To be tested |
|  | ShowPipleineStatus | 获取流水线状态,阶段及任务信息 | To be tested |
|  | CreatePipelineByTemplate | 基于模板快速创建流水线及流水线内任务 | To be tested |
|  | BatchShowPipelinesStatus | 批量获取流水线状态和阶段信息 | To be tested |
|  | StopPipelineNew | 停止流水线 | To be tested |
|  | ShowInstanceStatus | 检查流水线创建状态 | To be tested |
| 流水线管理--新 | CreatePipelineNew | 创建流水线 | To be tested |
|  | RetryPipelineRun | 重试运行流水线 | To be tested |
|  | ShowPipelineLog | 查询流水线日志 | To be tested |
|  | StopPipelineRun | 停止流水线 | To be tested |
|  | DeletePipeline | 删除流水线 | To be tested |
|  | BatchShowPipelinesLatestStatus | 批量获取流水线状态 | To be tested |
|  | RejectManualReview | 驳回人工审核 | To be tested |
|  | AcceptManualReview | 通过人工审核 | To be tested |
|  | RunPipeline | 启动流水线 | To be tested |
|  | ListPipelineRuns | 获取流水线执行记录 | To be tested |
|  | ShowStepOutputs | 获取流水线步骤执行输出 | To be tested |
|  | CreatePipelineByTemplateId | 基于模板创建流水线 | To be tested |
|  | ShowPipelineArtifacts | 查询流水线上的构建产物 | To be tested |
|  | ListPipelines | 获取流水线列表/获取项目下流水线执行状况 | To be tested |
|  | ShowPipelineRunDetail | 获取流水线状态/获取流水线执行详情 | To be tested |
| 租户级策略管理 | DeleteStrategy | 删除策略 | To be tested |
|  | ListStrategy | 获取策略列表 | To be tested |
|  | SwitchStrategy | 修改策略状态 | To be tested |
|  | CreateStrategy | 创建策略 | To be tested |
|  | UpdateStrategy | 修改策略 | To be tested |
|  | ShowStrategy | 获取策略详情 | To be tested |
| 规则管理 | ShowRule | 获取单条规则详情 | To be tested |
|  | DeleteRule | 删除规则 | To be tested |
|  | CreateRule | 创建规则 | To be tested |
|  | UpdateRule | 更新规则 | To be tested |
|  | ListRule | 分页获取规则列表 | To be tested |
| 项目级策略管理 | ListProjectStrategy | 获取策略列表 | To be tested |
|  | ShowProjectStrategy | 查询项目级策略详情 | To be tested |
