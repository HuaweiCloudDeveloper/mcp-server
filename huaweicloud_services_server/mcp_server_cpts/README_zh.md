# CPTS MCP Server 

## 版本信息
v0.1.0

## 产品描述

CPTS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CPTS交互的能力。可以基于自然语言对CPTS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| PerfTest工程管理 | DeleteProject | 删除工程 | To be tested |
|  | CreateProject | 创建工程 | To be tested |
|  | ShowProcess | 查询导入进度 | To be tested |
|  | ListProjectSets | 查询工程集 | To be tested |
|  | UpdateProject | 修改工程 | To be tested |
|  | ShowProject | 查询工程 | To be tested |
| 事务管理 | CreateTemp | 创建事务 | To be tested |
|  | ShowTemp | 查询事务 | To be tested |
|  | ShowTempSet | 查询事务集 | To be tested |
|  | DeleteTemp | 删除事务 | To be tested |
|  | UpdateTemp | 修改事务 | To be tested |
| 任务管理 | CreateNewTask | 创建任务 | To be tested |
|  | ShowTask | 查询任务(旧版) | To be tested |
|  | DeleteTask | 删除任务(旧版) | To be tested |
|  | CreateTask | 创建任务(旧版) | To be tested |
|  | ListTaskCases | 获取任务关联的用例列表 | To be tested |
|  | UpdateTaskStatus | 更新任务状态 | To be tested |
|  | UpdateTask | 修改任务(旧版) | To be tested |
|  | ShowTaskSet | 查询任务集 | To be tested |
|  | DeleteNewTask | 删除任务 | To be tested |
|  | UpdateTaskRelatedTestCase | 修改任务关联用例 | To be tested |
|  | BatchUpdateTaskStatus | 批量启停任务 | To be tested |
| 全局变量管理 | DeleteVariable | 删除全局变量 | To be tested |
|  | UpdateVariable | 修改变量 | To be tested |
|  | CreateVariable | 创建变量 | To be tested |
|  | ListVariables | 查询全局变量 | To be tested |
| 全链路压测管理 | ShowAgentConfig | 全链路压测探针获取配置信息 | To be tested |
|  | UpdateAgentHealthStatus | 全链路压测探针上报健康状态 | To be tested |
| 报告管理 | ShowReport | 查询报告 | To be tested |
|  | ShowMergeTaskCase | 查询任务报告的用例列表 | To be tested |
|  | ShowMergeCaseDetail | 查询用例报告详情 | To be tested |
|  | ShowHistoryRunInfo | 查询PerfTest任务离线报告列表 | To be tested |
|  | ShowTaskCaseAwChart | 查询用例的AW曲线图 | To be tested |
| 用例管理 | CreateCase | 创建用例(旧版) | To be tested |
|  | CreateNewCase | 创建用例 | To be tested |
|  | DebugCase | 调试用例 | To be tested |
|  | DeleteNewCase | 删除用例 | To be tested |
|  | UpdateCase | 修改用例(旧版) | To be tested |
|  | DeleteCase | 删除用例(旧版) | To be tested |
|  | ShowCase | 查询用例 | To be tested |
|  | UpdateNewCase | 修改用例 | To be tested |
| 目录管理 | UpdateDirectory | 修改目录 | To be tested |
|  | DeleteDirectory | 删除目录 | To be tested |
|  | CreateDirectory | 创建目录 | To be tested |
|  | ListProjectTestCase | 查询用例树 | To be tested |
