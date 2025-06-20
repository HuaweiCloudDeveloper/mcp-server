# RES MCP Server 

## 版本信息
v0.1.0

## 产品描述

RES MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务RES交互的能力。可以基于自然语言对RES资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 在线服务 | UpdateResOnlineInstance | 修改指定在线服务的元数据内容。 | To be tested |
|  | ListResOnlineServiceDetails | 根据给定的workspace_id和resource_id及category查询在线服务。 | To be tested |
|  | CreateResOnlineInstance | 新建在线服务元数据,新建成功之后可手动发布此服务。 | To be tested |
|  | DeleteResOnlineInstance | 删除在线服务实例。 | To be tested |
| 场景 | CreateResIntelligentScene | 在指定工作空间下面创建智能场景。 | To be tested |
|  | DeleteResScene | 该接口用于删除场景,删除之后不能恢复,请您谨慎操作。 | To be tested |
|  | ListResScenes | 查询当前工作空间下的场景列表。 | To be tested |
|  | ShowResScene | 查询指定场景的详情。 | To be tested |
|  | CreateResScene | 在指定工作空间下面创建自定义场景。 | To be tested |
|  | UpdateResIntelligentScene | 更新智能场景的内容信息。 | To be tested |
|  | UpdateResScene | 更新自定义场景的内容信息。 | To be tested |
| 工作空间 | ShowResWrokspace | 查询指定工作空间的具体信息。 | To be tested |
|  | CreateResWorkspace | 用于在推荐系统下面创建独立的工作空间,用于资源的隔离,用户可以在工作空间下面继续创建数据源、场景以及推荐任务等。是否有工作空间的操作权限取决于用户是否属于当前工作空间绑定的企业项目。 | To be tested |
|  | ListResEnterprises | 查询用户在当前项目id下的企业项目列表。在创建工作空间时需要提供企业项目id。 | To be tested |
|  | DeleteResWorkspace | 删除指定工作空间。 | To be tested |
|  | UpdateResWorkspace | 更新工作空间信息, 只允许更新描述信息。 | To be tested |
|  | ListResWorkspaces | 用于查询当前用户具有操作权限的工作空间列表。 | To be tested |
| 数据源 | UpdateResDatasource | 修改指定数据源的配置内容。 | To be tested |
|  | CreateResDatasource | 在指定的工作空间下面创建一个新的数据源。 | To be tested |
|  | ShowResDatasourceWorkDetail | 查询指定数据源下离线任务的结果。其中包括数据格式,数据检测、数据探索及效果评估的内容。 | To be tested |
|  | ListResDatasources | 查询当前工作空间下的数据源列表。 | To be tested |
|  | ShowResDatasource | 查询指定数据源的详情信息。 | To be tested |
|  | DeleteResDatasource | 删除数据源。 | To be tested |
|  | UpdateResDatastruct | 修改数据源中的特征。 | To be tested |
| 查询规格 | ListResResourceSpec | 查询当前推荐系统所提供的离线计算规格,实时计算规格和排序模型训练规格。在创建数据源和场景时,需要提供此信息。 | To be tested |
| 训练作业 | ShowResJob | 查询resource_id(数据源id或场景id)下的指定类型的作业。 | To be tested |
|  | CreateResJob | 新建训练作业元数据,新建成功之后可手动执行此任务。 | To be tested |
|  | CreateResJobs | 批量新建作业。 | To be tested |
|  | ShowResRecallSet | 查询给定workspaces_id和指定resource_id下的候选集。 | To be tested |
|  | DeleteResJob | 删除指定作业。 | To be tested |
|  | UpdateResJob | 修改指定作业的元数据信息。 | To be tested |
| 调度 | StartResJob | 执行独立的作业。 | To be tested |
|  | StartResSceneJobs | 执行场景下面的所有作业和服务。 | To be tested |
