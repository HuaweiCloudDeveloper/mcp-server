# AOM MCP Server 

## 版本信息
v0.1.0

## 产品描述

AOM MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务AOM交互的能力。可以基于自然语言对AOM资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Prometheus实例 | DeletePromInstance | 该接口用于卸载托管Prometheus实例。 | To be tested |
|  | CreateRecordingRule | 该接口用于给Prometheus实例创建预聚合规则。 | To be tested |
|  | CreatePromInstance | 该接口用于新增Prometheus实例。 | To be tested |
|  | ListAccessCode | 该接口用于获取Prometheus实例调用凭证。 | To be tested |
|  | ListPromInstance | 该接口用于查询Prometheus实例。 | To be tested |
| UniAgent管理 | BatchImportAgent | 该接口用于下发批量安装UniAgent任务。 | To be tested |
|  | ShowAgentInfos | 该接口用于查询执行过安装UniAgent任务的主机列表信息。 | To be tested |
|  | BatchUpdateAgent | 该接口用于下发批量升级UniAgent任务。 | To be tested |
| prometheus监控 | ListRangeQueryAomPromPost | 该接口使用POST方法查询PromQL(Prometheus Query Language)在一段时间返回内的计算结果。 | To be tested |
|  | ListInstantQueryAomPromPost | 该接口使用POST方法查询PromQL(Prometheus Query Language) 在特定时间点下的计算结果。 | To be tested |
|  | ListMetadataAomPromGet | 该接口用于查询序列及序列标签的元数据。 | To be tested |
|  | ListLabelsAomPromGet | 该接口使用GET方法获取标签名列表。 | To be tested |
|  | ListInstantQueryAomPromGet | 该接口使用GET方法查询PromQL(Prometheus Query Language)在特定时间点下的计算结果。 | To be tested |
|  | ListLabelsAomPromPost | 该接口使用POST方法获取标签名列表。 | To be tested |
|  | ListRangeQueryAomPromGet | 该接口使用GET方法查询PromQL(Prometheus Query Language)在一段时间返回内的计算结果。 | To be tested |
|  | ListLabelValuesAomPromGet | 该接口用于查询带有指定标签的时间序列列表。 | To be tested |
| 告警 | PushEvents | 该接口用于上报对应用户的事件、告警。 | To be tested |
|  | ListNotifiedHistories | 获取告警发送结果。 | To be tested |
|  | UpdateEventRule | 更新事件类告警规则。 | To be tested |
|  | ListMetricOrEventAlarmRule | 查询AOM2.0指标类或者事件类告警规则列表。(注:接口目前开放的region为:华东-上海一) | To be tested |
|  | DeleteEvent2alarmRule | 删除一条事件类告警规则。 | To be tested |
|  | ListEvent2alarmRule | 查询事件类告警规则列表。 | To be tested |
|  | AddEvent2alarmRule | 新增一条事件类告警规则。 | To be tested |
|  | DeleteMetricOrEventAlarmRule | 删除AOM2.0指标类或事件类告警规则。(注:接口目前开放的region为:华东-上海一) | To be tested |
|  | ListEvents | 该接口用于查询对应用户的事件、告警。 | To be tested |
|  | ListActionRule | 获取告警行动规则列表。 | To be tested |
|  | DeleteMuteRules | 删除静默规则。 | To be tested |
|  | AddMuteRules | 新增静默规则。 | To be tested |
|  | UpdateActionRule | 修改告警行动规则。 | To be tested |
|  | AddActionRule | 新增告警行动规则。 | To be tested |
|  | DeleteActionRule | 删除告警行动规则。 | To be tested |
|  | ListMuteRule | 获取静默规则列表。 | To be tested |
|  | ShowActionRule | 通过规则名称获取告警行动规则。 | To be tested |
|  | UpdateMuteRule | 修改静默规则。 | To be tested |
|  | CountEvents | 该接口用于分段统计指定条件下的事件、告警。 | To be tested |
|  | AddOrUpdateMetricOrEventAlarmRule | 添加或修改AOM2.0指标类或事件类告警规则。(注:接口目前开放的region为:华东-上海一) | To be tested |
| 应用资源管理(aom2.0接口) | ListResourceUnderNode | 该接口用于查询绑定在节点上的资源列表。 | To be tested |
|  | CreateApp | 该接口用于新增应用。 | To be tested |
|  | DeleteEnv | 该接口用于删除环境。 | To be tested |
|  | ShowEnvByName | 该接口用于查询环境详情。 | To be tested |
|  | CreateEnv | 该接口用于创建环境。 | To be tested |
|  | UpdateEnv | 该接口用于修改环境。 | To be tested |
|  | DeleteApp | 该接口用于删除应用。 | To be tested |
|  | CreateComponent | 该接口用于新增组件。 | To be tested |
|  | UpdateApp | 该接口用于修改应用。 | To be tested |
|  | ShowComponent | 该接口用于查询组件详情。 | To be tested |
|  | ShowAppByName | 该接口用于查询应用详情。 | To be tested |
|  | UpdateSubApp | 该接口用于修改子应用。 | To be tested |
|  | CreateSubApp | 该接口用于新增子应用。 | To be tested |
|  | UpdateComponent | 该接口用于修改组件。 | To be tested |
|  | DeleteSubApp | 该接口用于删除子应用。 | To be tested |
|  | DeleteComponent | 该接口用于删除组件。 | To be tested |
|  | ShowComponentByName | 该接口用于查询组件详情。 | To be tested |
|  | ShowApp | 该接口用于查询应用详情。 | To be tested |
|  | ShowEnv | 该接口用于查询环境详情。 | To be tested |
| 日志 | ListLogItems | 该接口用于查询不同维度(例如集群、IP、应用等)下的日志内容,支持分页查询。 | To be tested |
| 监控 | DeleteserviceDiscoveryRules | 该接口用于删除服务发现规则。 | To be tested |
|  | ShowAlarmRule | 该接口用于查询单条阈值规则。 | To be tested |
|  | ListServiceDiscoveryRules | 该接口用于查询系统当前已存在的服务发现规则。 | To be tested |
|  | AddMetricData | 该接口用于向服务端添加一条或多条监控数据。 | To be tested |
|  | DeleteAlarmRule | 该接口用于删除阈值规则。 | To be tested |
|  | ListAlarmRule | 该接口用于查询阈值规则列表。 | To be tested |
|  | AddOrUpdateServiceDiscoveryRules | 该接口用于添加或修改一条或多条服务发现规则。同一projectid下可添加的规则上限为100条。 | To be tested |
|  | ListSeries | 该接口用于查询系统当前可监控的时间序列列表,可以指定时间序列命名空间、名称、维度、所属资源的编号(格式为:resType_resId),分页查询的起始位置和返回的最大记录条数。 | To be tested |
|  | DeleteAlarmRules | 该接口用于批量删除阈值规则 | To be tested |
|  | ListMetricItems | 该接口用于查询系统当前可监控的指标列表,可以指定指标命名空间、指标名称、维度、所属资源的编号(格式为:resType_resId),分页查询的起始位置和返回的最大记录条数。 | To be tested |
|  | ShowMetricsData | 该接口用于查询指定时间范围内指标的监控数据,可以通过参数指定需要查询的数据维度,数据周期等。 | To be tested |
|  | UpdateAlarmRule | 该接口用于修改一条阈值规则。 | To be tested |
|  | AddAlarmRule | 该接口用于添加一条阈值规则。 | To be tested |
|  | ListSample | 该接口用于查询指定时间范围内的监控时序数据,可以通过参数指定需要查询的数据维度,数据周期等。 | To be tested |
| 自动化运维 | SearchTemplateById | 该接口可根据执行方案id查询执行方案详情。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
|  | ListTemplateByJobId | 该接口可根据作业ID查询执行方案,分页返回执行方案列表。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
|  | StartPausingWorkflowExecutions | 该接口可对任务进行失败重试、失败跳过、暂停继续操作,返回操作结果。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
|  | CreateFastExecuteScript | 该接口用于创建快速执行脚本的任务,可以指定脚本类型,执行用户,脚本参数,执行机器,脚本内容,在用户指定的机器上执行脚本。(注:接口目前开放的region为:华东-苏州二零一)。 | To be tested |
|  | ListWorkflowExecutions | 该接口可获取执行任务的执行历史。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
|  | ExecuteWorkflow | 该接口可下发执行指定的任务。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
|  | ListAllJobByName | 该接口可查询已创建的作业,可指定作业名称和作业创建人去精确查询,返回作业列表信息。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
|  | CreateWorkflow | 该接口用于创建工作流(任务),返回工作流详情。任务类型取决于模板名称和'input'参数。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
|  | ListAllVersionByVersionId | 该接口可查询指定脚本ID下的所有版本,返回该名称的脚本版本列表信息。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
|  | UpdateWorkflowTriggerStatus | 更新定时任务的启停状态,可启动定时任务或停止定时任务,返回操作任务结果。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
|  | ListWorkflow | 该接口可返回已经创建的任务列表,可按任务名称,任务状态,任务类型,执行人,更新时间为查询条件分页查询任务。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
|  | SearchWorkflowExecutionDetail | 该接口可获取任务的执行详情,可指定工作流ID和执行ID去查询对应的任务,返回任务执行详情。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
|  | ListAllScriptByName | 该接口是脚本主页查询,可指定脚本名称和脚本创建人进行精确查询,返回包含脚本基本信息的列表数据。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
|  | StopExecution | 该接口可终止正在执行的任务,指定工作流ID和执行ID去终止对应的任务,返回终止操作状态。(注:接口目前开放的region为:华北-北京四,华东-上海一,华东-上海二,华南-广州)。 | To be tested |
| 配置管理 | ListPermissions | 该接口用于查询aom2.0相关云服务授权信息。 | To be tested |
|  | ListAgents | 该接口用于查询集群主机或用户自定义主机安装的ICAgent信息。 | To be tested |
