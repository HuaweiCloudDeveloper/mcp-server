# AOM MCP Server 


## Version
v0.1.0

## Overview

AOM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service AOM. Full-chain management of AOM resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

<html>
    <head></head>
    <body>
        <table border="1" cellspacing="0" cellpadding="5">
            <tbody>
                <tr>
                    <th>类别</th>
                    <th>工具名称</th>
                    <th>功能描述</th>
                    <th>状态</th>
                </tr>
                <tr>
                    <td rowspan="3">AppManagement</td>
                    <td>CreateApp</td>
                    <td>该接口用于用户创建应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApp</td>
                    <td>该接口用于用户修改应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApp</td>
                    <td>该接口用于用户查询应用详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Component</td>
                    <td>CreateComponent</td>
                    <td>创建组件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowComponent</td>
                    <td>获取组件详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateComponent</td>
                    <td>更新组件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteComponent</td>
                    <td>删除组件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Permission</td>
                    <td>ListPermissions</td>
                    <td>检索指定资源类型的共享资源权限列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Prometheus实例</td>
                    <td>DeletePromInstance</td>
                    <td>该接口用于卸载托管Prometheus实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRecordingRule</td>
                    <td>该接口用于给Prometheus实例创建预聚合规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePromInstance</td>
                    <td>该接口用于新增Prometheus实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccessCode</td>
                    <td>该接口用于获取Prometheus实例调用凭证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPromInstance</td>
                    <td>该接口用于查询Prometheus实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">UniAgent管理</td>
                    <td>BatchImportAgent</td>
                    <td>该接口用于下发批量安装UniAgent任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgentInfos</td>
                    <td>该接口用于查询执行过安装UniAgent任务的主机列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateAgent</td>
                    <td>该接口用于下发批量升级UniAgent任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">prometheus监控</td>
                    <td>ListRangeQueryAomPromPost</td>
                    <td>该接口使用POST方法查询PromQL(Prometheus Query Language)在一段时间返回内的计算结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstantQueryAomPromPost</td>
                    <td>该接口使用POST方法查询PromQL(Prometheus Query Language) 在特定时间点下的计算结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetadataAomPromGet</td>
                    <td>该接口用于查询序列及序列标签的元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLabelsAomPromGet</td>
                    <td>该接口使用GET方法获取标签名列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstantQueryAomPromGet</td>
                    <td>该接口使用GET方法查询PromQL(Prometheus Query Language)在特定时间点下的计算结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLabelsAomPromPost</td>
                    <td>该接口使用POST方法获取标签名列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRangeQueryAomPromGet</td>
                    <td>该接口使用GET方法查询PromQL(Prometheus Query Language)在一段时间返回内的计算结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLabelValuesAomPromGet</td>
                    <td>该接口用于查询带有指定标签的时间序列列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">函数流</td>
                    <td>ListWorkflowExecutions</td>
                    <td>获取指定函数流执行实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflow</td>
                    <td>创建函数流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkflow</td>
                    <td>查询函数流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">函数测试事件</td>
                    <td>ListEvents</td>
                    <td>获取指定函数的测试事件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">可信节点管理</td>
                    <td>ListAgents</td>
                    <td>功能描述:用户可以使用该接口获取可信节点信息列表。支持节点名称与联盟名称的模糊查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="19">告警</td>
                    <td>PushEvents</td>
                    <td>该接口用于上报对应用户的事件、告警。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotifiedHistories</td>
                    <td>获取告警发送结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEventRule</td>
                    <td>更新事件类告警规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetricOrEventAlarmRule</td>
                    <td>查询AOM2.0指标类或者事件类告警规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEvent2alarmRule</td>
                    <td>删除一条事件类告警规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEvent2alarmRule</td>
                    <td>查询事件类告警规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddEvent2alarmRule</td>
                    <td>新增一条事件类告警规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMetricOrEventAlarmRule</td>
                    <td>删除AOM2.0指标类或事件类告警规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListActionRule</td>
                    <td>获取告警行动规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMuteRules</td>
                    <td>删除静默规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddMuteRules</td>
                    <td>新增静默规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateActionRule</td>
                    <td>修改告警行动规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddActionRule</td>
                    <td>新增告警行动规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteActionRule</td>
                    <td>删除告警行动规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMuteRule</td>
                    <td>获取静默规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowActionRule</td>
                    <td>通过规则名称获取告警行动规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMuteRule</td>
                    <td>修改静默规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountEvents</td>
                    <td>该接口用于分段统计指定条件下的事件、告警。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddOrUpdateMetricOrEventAlarmRule</td>
                    <td>添加或修改AOM2.0指标类或事件类告警规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">应用模板管理</td>
                    <td>DeleteApp</td>
                    <td>删除应用模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">应用资源管理(aom2.0接口)</td>
                    <td>ListResourceUnderNode</td>
                    <td>该接口用于查询绑定在节点上的资源列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnv</td>
                    <td>该接口用于删除环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnvByName</td>
                    <td>该接口用于查询环境详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnv</td>
                    <td>该接口用于创建环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnv</td>
                    <td>该接口用于修改环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppByName</td>
                    <td>该接口用于查询应用详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubApp</td>
                    <td>该接口用于修改子应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubApp</td>
                    <td>该接口用于新增子应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubApp</td>
                    <td>该接口用于删除子应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowComponentByName</td>
                    <td>该接口用于查询组件详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnv</td>
                    <td>该接口用于查询环境详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">日志</td>
                    <td>ListLogItems</td>
                    <td>该接口用于查询不同维度(例如集群、IP、应用等)下的日志内容,支持分页查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">监控</td>
                    <td>DeleteserviceDiscoveryRules</td>
                    <td>该接口用于删除服务发现规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlarmRule</td>
                    <td>该接口用于查询单条阈值规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceDiscoveryRules</td>
                    <td>该接口用于查询系统当前已存在的服务发现规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddMetricData</td>
                    <td>该接口用于向服务端添加一条或多条监控数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlarmRule</td>
                    <td>该接口用于删除阈值规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmRule</td>
                    <td>该接口用于查询阈值规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddOrUpdateServiceDiscoveryRules</td>
                    <td>该接口用于添加或修改一条或多条服务发现规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSeries</td>
                    <td>该接口用于查询系统当前可监控的时间序列列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlarmRules</td>
                    <td>该接口用于批量删除阈值规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetricItems</td>
                    <td>该接口用于查询系统当前可监控的指标列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetricsData</td>
                    <td>该接口用于查询指定时间范围内指标的监控数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlarmRule</td>
                    <td>该接口用于修改一条阈值规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAlarmRule</td>
                    <td>该接口用于添加一条阈值规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSample</td>
                    <td>该接口用于查询指定时间范围内的监控时序数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">自动化运维</td>
                    <td>SearchTemplateById</td>
                    <td>该接口可根据执行方案id查询执行方案详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplateByJobId</td>
                    <td>该接口可根据作业ID查询执行方案,分页返回执行方案列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartPausingWorkflowExecutions</td>
                    <td>该接口可对任务进行失败重试、失败跳过、暂停继续操作,返回操作结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFastExecuteScript</td>
                    <td>该接口用于创建快速执行脚本的任务,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteWorkflow</td>
                    <td>该接口可下发执行指定的任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllJobByName</td>
                    <td>该接口可查询已创建的作业,可指定作业名称和作业创建人去精确查询,返回作业列表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllVersionByVersionId</td>
                    <td>该接口可查询指定脚本ID下的所有版本,返回该名称的脚本版本列表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkflowTriggerStatus</td>
                    <td>更新定时任务的启停状态,可启动定时任务或停止定时任务,返回操作任务结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchWorkflowExecutionDetail</td>
                    <td>该接口可获取任务的执行详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllScriptByName</td>
                    <td>该接口是脚本主页查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopExecution</td>
                    <td>该接口可终止正在执行的任务</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
