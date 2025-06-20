# CDM MCP Server 

## 版本信息
v0.1.0

## 产品描述

CDM MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CDM交互的能力。可以基于自然语言对CDM资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 作业管理 | ShowJobStatus | 查询作业状态接口。 | To be tested |
|  | ShowSubmissions | 查询作业执行历史接口。 | To be tested |
|  | UpdateJob | 修改作业接口。 | To be tested |
|  | CreateJob | 指定集群创建作业接口。 | To be tested |
|  | ShowJobs | 查询作业接口。 | To be tested |
|  | DeleteJob | 删除作业接口。 | To be tested |
|  | StartJob | 启动作业接口。 | To be tested |
|  | StopJob | 停止作业接口。 | To be tested |
|  | CreateAndStartRandomClusterJob | 随机集群创建作业并执行接口。 | To be tested |
| 连接管理 | UpdateLink | 修改连接接口。 | To be tested |
|  | DeleteLink | 删除连接接口。 | To be tested |
|  | CreateLink | 创建连接接口。 | To be tested |
|  | ShowLink | 查询连接接口。 | To be tested |
| 集群管理 | DeleteCluster | 删除集群接口。 | To be tested |
|  | CreateCluster | 创建集群接口。 | To be tested |
|  | StartCluster | 启动集群接口。 | To be tested |
|  | ShowDatastores | 查询CDM集群支持的版本。 | To be tested |
|  | ShowFlavorDetail | 查询指定规格ID的规格详请。 | To be tested |
|  | ModifyCluster | 修改CDM集群配置。 | To be tested |
|  | ShowClusterEnterpriseProjects | 查询指定集群的企业项目ID。 | To be tested |
|  | ShowClusterDetail | 查询集群详情接口。 | To be tested |
|  | ShowEnterpriseProjects | 查询当前项目下的所有集群的企业项目ID。 | To be tested |
|  | ListClusters | 查询集群列表接口。 | To be tested |
|  | RestartCluster | 重启集群接口。 | To be tested |
|  | ShowAvailabilityZones | 查询CDM集群的所有可用区。 | To be tested |
|  | ShowFlavors | 按版本ID查询所有兼容规格。 | To be tested |
|  | ShowInstanceDetail | 查询集群实例信息。 | To be tested |
