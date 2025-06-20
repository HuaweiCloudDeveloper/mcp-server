# CodeArtsCheck MCP Server 

## 版本信息
v0.1.0

## 产品描述

CodeArtsCheck MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CodeArtsCheck交互的能力。可以基于自然语言对CodeArtsCheck资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 任务管理 | ShowTasksRulesets | 查询任务的已选规则集列表。 | To be tested |
|  | ShowTaskListByProjectId | 根据DEVCLOUD_PROJECT_UUID查询该项目下的任务列表。 | To be tested |
|  | CheckRecord | 提供每次扫描的问题数量统计 | To be tested |
|  | ListTaskRuleset | 查询任务的已选规则集列表。 | To be tested |
|  | ShowTaskSettings | 查询任务的高级选项 | To be tested |
|  | ShowTaskPathTree | 获取任务的目录树 | To be tested |
|  | ShowTasklog | 查询任务检查失败日志,不传execute_id则查询最近一次的检查日志 | To be tested |
|  | UpdateTaskSettings | 任务配置高级选项,如自定义镜像 | To be tested |
|  | ShowProgressDetail | 根据任务ID查询任务执行状态。任务状态:0表示检查中,1表示检查失败,2表示检查成功,3表示任务中止。只有正在检查中才有进度的详细信息。 | To be tested |
|  | CheckRulesetParameters | 查询任务规则集的检查参数 | To be tested |
|  | StopTaskById | 根据任务ID终止检查任务。 | To be tested |
|  | ListTaskParameter | 任务配置检查参数 | To be tested |
|  | UpdateTaskRuleset | 修改任务规则集。 | To be tested |
|  | RunTask | 执行检查任务。 | To be tested |
|  | CheckParameters | 查询任务规则集的检查参数 | To be tested |
|  | CreateTask | 新建检查任务但是不执行。 | To be tested |
|  | UpdateIgnorePath | 任务配置屏蔽目录 | To be tested |
|  | DeleteTask | 删除检查任务,执行中的任务删除无法再查看 | To be tested |
| 缺陷管理 | ShowTaskCmetrics | 根据检查任务ID查询cmertrics缺陷概要。 | To be tested |
|  | ShowTaskDefects | 根据检查任务ID分页查询缺陷结果详情。 | To be tested |
|  | UpdateDefectStatus | 修改检查出的缺陷的状态为已解决、已忽略 | To be tested |
|  | ShowTaskDefectsStatistic | 根据检查任务ID查询缺陷详情的统计 | To be tested |
|  | ShowTaskDetail | 根据检查任务ID查询缺陷结果的概要。包括问题概述、问题状态、圈复杂度、代码重复率等。 | To be tested |
| 规则管理 | SetDefaulTemplate | 设置每个项目对应语言的默认规则集配置。 | To be tested |
|  | ListRules | 根据语言、问题级别等条件查询规则列表。 | To be tested |
|  | ListTemplateRules | 根据项目ID、规则集ID等条件查询规则列表。 | To be tested |
|  | DeleteRuleset | 删除自定义规则集,正在使用中的或默认规则集不能删除 | To be tested |
|  | CreateRuleset | 可根据需求灵活的组合规则。 | To be tested |
|  | ListRulesets | 根据项目ID、语言等条件查询规则集列表。 | To be tested |
