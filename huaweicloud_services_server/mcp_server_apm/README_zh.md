# APM MCP Server 

## 版本信息
v0.1.0

## 产品描述

APM MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务APM交互的能力。可以基于自然语言对APM资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AKSK | ShowAkSks | 查询租户的aksk。 | To be tested |
|  | CreateAkSk | 创建aksk。 | To be tested |
|  | DeleteAkSk | 删除aksk。 | To be tested |
| ALARM | ListAlarmNotify | 查询单个告警的触发详情与历史。 | To be tested |
|  | ListAlarmData | 查询系统中存在的告警。 | To be tested |
| APM | ChangeAgentStatus | 改变指定实例的采集状态:开启和关闭。 | To be tested |
|  | ShowMasterAddress | 根据region名称获取该region下的master服务podlb地址信息。 | To be tested |
|  | DeleteAgent | 删除agent | To be tested |
|  | SaveMonitorItemConfig | 保存监控项。 | To be tested |
|  | ListEnvMonitorItem | 查询监控项列表。 | To be tested |
|  | ListAkSk | 获取该用户创建的ak/sk列表。 | To be tested |
|  | ListBusiness | 该接口用于查询对应用户下的应用。 | To be tested |
|  | SearchAgent | 该接口用于搜索应用下所有探针情况。 | To be tested |
|  | SearchApplication | 对指定区域下的组件和环境及其探针情况进行搜索。 | To be tested |
| CMDB | ShowSubBusinessDetail | 查询单个子应用详情。 | To be tested |
|  | ListApps | 获取组件列表。 | To be tested |
|  | ListAppEnvs | 获取组件下的环境列表。 | To be tested |
|  | ListEnvTags | 查询环境标签接口。 | To be tested |
|  | DeleteApp | 该接口用于删除指定的组件。 | To be tested |
|  | ShowBusinessDetail | 查询单个应用的详情。 | To be tested |
|  | ShowTopologyTree | 获取应用树。 | To be tested |
| Profiling | ShowFlameLineTree |  | To be tested |
| REGION | ListOpenRegion | 该接口用于查询用户开通的region信息。 | To be tested |
|  | ListSupportedRegion | 查询所有的支持的region信息。 | To be tested |
| TOPOLOGY | SearchEnvTopology | 查询组件环境级别全局拓扑图信息。 | To be tested |
|  | SearchBusinessTopology | 查询应用级别全局拓扑图信息。 | To be tested |
| TRACING | ShowToken | 获取链路追踪应用的token | To be tested |
|  | CreateBusiness | 创建链路追踪应用 | To be tested |
|  | ShowAccessPoint | 获取链路追踪应用接入地址 | To be tested |
| TRANSACTION | SearchTransactionConfig | 查询已配置好的URL跟踪配置列表。 | To be tested |
|  | ListBusinessEnv | 查询所选Region下设置了URL跟踪的环境列表。 | To be tested |
|  | SearchTransaction | 查询当前被调用的URL跟踪视图列表。 | To be tested |
|  | ShowTransactionDetail | 查询某条URL跟踪视图详情。 | To be tested |
| VIEW | ShowEnvMonitorItems | 获取监控项信息。 | To be tested |
|  | ShowRawTable | 获取原始数据表格。 | To be tested |
|  | ShowMonitorItemDetail | 获取一个监控项的详情。 | To be tested |
|  | ShowMonitorItemViewConfig | 查询监控项配置信息。 | To be tested |
|  | ShowSpanSearch | span数据查询接口。 | To be tested |
|  | ShowTopology | 调用链拓扑图。 | To be tested |
|  | ShowClobDetail | 获取原始数据详情。 | To be tested |
|  | ListEnvInstances | 获取实例信息列表。 | To be tested |
|  | ShowTrend | 获取趋势图。 | To be tested |
|  | ShowSumTable | 获取汇总表格数据。 | To be tested |
|  | ShowTraceEvents | 获取一个trace的所有调用链数据。 | To be tested |
|  | ShowEventDetail | 获取event的详情。 | To be tested |
