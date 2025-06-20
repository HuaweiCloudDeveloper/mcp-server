# CodeArtsBuild MCP Server 

## 版本信息
v0.1.0

## 产品描述

CodeArtsBuild MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CodeArtsBuild交互的能力。可以基于自然语言对CodeArtsBuild资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| CodeArtsBuild | ListOfficialTemplate | 查询官方模版 | To be tested |
|  | ShowJobListByProjectId | 查看项目下用户的构建任务列表 | To be tested |
|  | DownloadBuildLog | 下载全量构建日志 | To be tested |
|  | ShowKeystorePermission | 文件管理查询权限 | To be tested |
|  | ShowBuildRecord | 查询指定构建记录详情 | To be tested |
|  | CreateBuildJob | 创建构建任务 | To be tested |
|  | ShowJobConfig | 获取构建任务详情 | To be tested |
|  | ShowBuildParamsList | 编辑页获取参数类型的接口 | To be tested |
|  | EnableBuildJob | 恢复构建任务 | To be tested |
|  | ShowListHistory | 查看构建任务的构建历史列表 | To be tested |
|  | StopBuildJob | 停止构建任务 | To be tested |
|  | ListProjectJobs | 查询项目任务列表 | To be tested |
|  | ShowJobConfigDiff | 获取构建任务配置的对比差异 | To be tested |
|  | ShowJobInfo | 查看构建任务构建信息 | To be tested |
|  | UpdateBuildJob | 更新构建任务 | To be tested |
|  | ShowDefaultBuildParameters | 获取编译构建默认参数 | To be tested |
|  | ListNotice | 查询通知 | To be tested |
|  | CreateTemplates | 创建构建模板 | To be tested |
|  | ShowImageTemplateList | 获取镜像模板列表 | To be tested |
|  | ShowListPeriodHistory | 根据开始时间和结束时间查看构建任务的构建历史列表 | To be tested |
|  | ListRecyclingJob | 查看回收站中删除的构建任务列表 | To be tested |
|  | ListJobConfig | 获取构建任务详情 | To be tested |
|  | ListRelatedProjectInfo | 获取项目列表 | To be tested |
|  | DownloadTaskLog | 下载构建步骤日志 | To be tested |
|  | ShowDockerfileTemplate | 获取dockerfileTemplate | To be tested |
|  | ListBuildInfoRecordByJobId | 获取任务构建记录列表v1 | To be tested |
|  | ShowProjectPermission | 获取用户权限 | To be tested |
|  | ShowJobStatus | 查看任务运行状态 | To be tested |
|  | ListBuildInfoRecord | 获取任务构建记录列表 | To be tested |
|  | ShowJobBuildSuccessRatio | 查询构建成功率 | To be tested |
|  | DownloadRealTimeLog | 下载构建实时日志 | To be tested |
|  | ShowJobSystemParameters | 查看系统预定义参数 | To be tested |
|  | CheckJobNameIsExists | 查看项目下任务名是否存在 | To be tested |
|  | DownloadKeystoreByName | 文件管理文件下载 | To be tested |
|  | ShowBuildRecordBuildScript | 获取构建记录的构建脚本 | To be tested |
|  | DisableBuildJob | 禁用构建任务 | To be tested |
|  | ShowRunningStatus | 查看任务是否在构建 | To be tested |
|  | ShowJobSuccessRatio | 根据开始时间和结束时间查看构建任务的构建成功率 | To be tested |
|  | ShowLastHistory | 查询指定代码仓库最近一次成功的构建历史 | To be tested |
|  | RunJob | 执行构建任务,可传自定义参数 | To be tested |
|  | ShowRecordDetail | 获取构建记录信息 | To be tested |
|  | DeleteTemplates | 删除构建模板 | To be tested |
|  | ShowJobBuildTime | 洞察构建时长 | To be tested |
|  | DeleteBuildJob | 删除构建任务 | To be tested |
|  | ListRecords | 获取指定工程的构建记录列表 | To be tested |
|  | ShowReportSummary | 获取覆盖率接口 | To be tested |
|  | ListKeystore | 查询用户可使用文件 | To be tested |
|  | ShowBuildRecordFullStages | 获取任务各阶段信息 | To be tested |
|  | ShowRelatedProject | 获取当前用户的项目信息列表 | To be tested |
|  | ShowOutputInfo | 获取构建产物详情信息 | To be tested |
|  | ShowYamlTemplate | 获取代码化构建默认模板 | To be tested |
|  | DisableNotice | 取消通知 | To be tested |
|  | ShowHistoryDetails | 获取构建历史详情信息接口 | To be tested |
|  | ShowJobNoticeConfigInfo | 获取通知信息 | To be tested |
|  | DownloadKeystore | 下载指定租户下的KeyStore文件 | To be tested |
|  | ShowBuildInfoRecord | 获取任务构建记录列表 | To be tested |
|  | ShowJobRolePermission | 获取构建任务的角色权限矩阵信息 | To be tested |
|  | ListTemplates | 查询构建模板 | To be tested |
|  | UpdateNotice | 更新通知 | To be tested |
| Offline | ShowRecordInfo | 获取构建记录信息(待下线) | To be tested |
|  | DownloadLogByRecordId | 下载构建日志(待下线) | To be tested |
|  | ShowFlowGraph | 获取构建记录的有向无环图(待下线) | To be tested |
|  | StopJob | 停止构建任务(待下线) | To be tested |
