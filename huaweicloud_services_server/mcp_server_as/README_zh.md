# AS MCP Server 

## 版本信息
v0.1.0

## 产品描述

AS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务AS交互的能力。可以基于自然语言对AS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 伸缩活动日志管理 | ListScalingActivityLogs | 根据输入条件过滤查询伸缩活动日志。查询结果分页显示。可根据起始时间,截止时间,起始行号,记录数进行条件过滤查询。若不加过滤条件默认查询最多20条伸缩活动日志信息。 | To be tested |
|  | ListScalingActivityV2Logs | 根据输入条件过滤查询伸缩活动日志,支持查询实例伸缩、ELB迁移、实例备用等类型活动。查询结果分页显示。查询伸缩活动日志V2版本与V1版本区别在于,V2版本展示了更详细的实例伸缩日志,如ELB迁移日志,实例备用日志信息。可根据起始时间,截止时间,起始行号,记录数,伸缩活动类型等作为条件过滤查询。若不加过滤条件默认查询最多20条伸缩活动日志信息。 | To be tested |
| 伸缩策略日志管理 | ListScalingPolicyExecuteLogs | 根据输入条件过滤查询策略执行的历史记录。查询结果分页显示。可根据日志ID,伸缩资源类型,伸缩资源ID,策略执行类型,查询额起始,查询截止时间,查询起始行号,查询记录数进行条件过滤查询。若不加过滤条件默认查询最多20条策略执行日志信息。 | To be tested |
| 弹性伸缩API管理 | ShowApiVersion | 根据租户id和资源id查询指定资源类型的标签列表 | To be tested |
|  | ListApiVersions | 查询弹性伸缩API所有版本信息 | To be tested |
| 弹性伸缩实例管理 | ListScalingInstances | 根据输入条件过滤查询弹性伸缩组中实例信息。查询结果分页显示。可根据实例在伸缩组中的生命周期状态,实例健康状态,实例保护状态,起始行号,记录条数进行条件过滤查询。若不加过滤条件默认查询组内最多20条实例信息 | To be tested |
|  | BatchUnsetScalingInstancesStantby | 批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。 | To be tested |
|  | BatchUnprotectScalingInstances | 批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。 | To be tested |
|  | BatchSetScalingInstancesStandby | 批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。 | To be tested |
|  | DeleteScalingInstance | 从弹性伸缩组中移出一个指定实例。实例处于INSERVICE且移出后实例数不能小于伸缩组的最小实例数时才可以移出。当伸缩组没有伸缩活动时,才能移出实例。 | To be tested |
|  | BatchRemoveScalingInstances | 批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。 | To be tested |
|  | BatchProtectScalingInstances | 批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。 | To be tested |
|  | BatchAddScalingInstances | 批量移出伸缩组中的实例或批量添加伸缩组外的实例。批量对伸缩组中的实例设置或取消其实例保护属性。批量将伸缩组中的实例转入或移出备用状态。说明:- 单次最多批量操作实例个数为10。批量添加后实例数不能大于伸缩组的最大实例数,批量移出后实例数不能小于伸缩组的最小实例数。- 当伸缩组处于INSERVICE状态且没有伸缩活动时,才能添加实例。- 当伸缩组没有伸缩活动时,才能移出实例。- 向伸缩组中添加实例时,必须保证实例所在的可用区包含于伸缩组的可用区内。- 实例处于INSERVICE状态时才可以进行移出、设置或取消实例保护属性等操作。- 当伸缩组发生自动缩容活动时,设置了实例保护的实例不会被移出伸缩组。- 批量移出弹性伸缩组中的实例时,若该实例加入伸缩组时绑定的监听器和伸缩组本身的监听器相同,会解绑定实例和监听器。若该实例加入伸缩组时绑定的监听器和伸缩组本身的监听器不同,会保留实例和监听器的绑定关系。 | To be tested |
| 弹性伸缩策略管理 | UpdateScalingPolicy | 修改指定弹性伸缩策略。 | To be tested |
|  | ResumeScalingPolicy | 立即执行或启用或停止一个指定弹性伸缩策略。当伸缩组、伸缩策略状态处于INSERVICE时,伸缩策略才能被正确执行,否则会执行失败。 | To be tested |
|  | ExecuteScalingPolicy | 立即执行或启用或停止一个指定弹性伸缩策略。当伸缩组、伸缩策略状态处于INSERVICE时,伸缩策略才能被正确执行,否则会执行失败。 | To be tested |
|  | BatchPauseScalingPolicies | 批量启用、停用或者删除弹性伸缩策略。单次最多批量操作伸缩策略个数为20。 | To be tested |
|  | DeleteScalingPolicy | 删除一个指定弹性伸缩策略。 | To be tested |
|  | ShowScalingPolicy | 查询指定弹性伸缩策略信息。 | To be tested |
|  | BatchResumeScalingPolicies | 批量启用、停用或者删除弹性伸缩策略。单次最多批量操作伸缩策略个数为20。 | To be tested |
|  | CreateScalingPolicy | 创建弹性伸缩策略。伸缩策略定义了伸缩组内实例的扩张和收缩操作。如果执行伸缩策略造成伸缩组期望实例数与伸缩组内实例数不符,弹性伸缩会自动调整实例资源,以匹配期望实例数。当前伸缩策略支持告警触发策略,周期触发策略,定时触发策略。在策略执行具体动作中,可设置实例变化的个数,或根据当前实例的百分比数进行伸缩。 | To be tested |
|  | ListScalingPolicies | 根据输入条件过滤查询弹性伸缩策略。查询结果分页显示。可根据伸缩策略名称,策略类型,伸缩策略ID,起始行号,记录数进行条件过滤查询。若不加过滤条件默认查询租户下指定伸缩组内最多20条伸缩策略信息。 | To be tested |
|  | PauseScalingPolicy | 立即执行或启用或停止一个指定弹性伸缩策略。当伸缩组、伸缩策略状态处于INSERVICE时,伸缩策略才能被正确执行,否则会执行失败。 | To be tested |
|  | BatchDeleteScalingPolicies | 批量启用、停用或者删除弹性伸缩策略。单次最多批量操作伸缩策略个数为20。 | To be tested |
| 弹性伸缩策略管理V2 | ListAllScalingV2Policies | 根据输入条件过滤查询弹性伸缩策略,支持查询当前租户下全量伸缩策略。查询结果分页显示。可根据伸缩资源ID,伸缩资源类型,伸缩策略名称,伸缩策略ID,告警ID,企业项目ID,起始行号,记录数,排序方式等条件进行过滤查询。若不加过滤添加默认查询该租户下最多20条伸缩策略信息。 | To be tested |
|  | UpdateScalingV2Policy | 修改指定弹性伸缩策略。修改弹性伸缩策略V2版本与V1版本的区别在于,V2版本支持修改伸缩资源类型。 | To be tested |
|  | CreateScalingV2Policy | 可针对不同类型资源如伸缩组或带宽,创建弹性伸缩策略。创建弹性伸缩策略V2版本与V1版本的区别在于,V2版本支持创建对带宽资源进行调整的策略,通过伸缩资源类型区分伸缩资源。 | To be tested |
|  | ShowScalingV2Policy | 查询指定弹性伸缩策略信息。 | To be tested |
|  | ListScalingV2Policies | 根据输入条件过滤查询弹性伸缩策略。查询结果分页显示。查询弹性伸缩策略V2版本与V1版本的区别在于,V2版本响应含伸缩资源类型。可根据伸缩策略名称,策略类型,伸缩策略ID,起始行号,记录数进行条件过滤查询。若不加过滤条件默认查询该租户下指定资源下最多20条伸缩策略信息。 | To be tested |
| 弹性伸缩组管理 | PauseScalingGroup | 启用或停止一个指定弹性伸缩组。已停用状态的伸缩组,不会自动触发任何伸缩活动。当伸缩组正在进行伸缩活动,即使停用,正在进行的伸缩活动也不会立即停止。 | To be tested |
|  | ShowScalingGroup | 查询一个指定弹性伸缩组详情。 | To be tested |
|  | CreateScalingGroup | 伸缩组是具有相同应用场景的实例的集合,是启停伸缩策略和进行伸缩活动的基本单位。伸缩组内定义了最大实例数、期望实例数、最小实例数、虚拟私有云、子网、负载均衡等信息。默认最多可以创建10个伸缩组。如果伸缩组配置了负载均衡,在添加或移除实例时,会自动为实例绑定或解绑负载均衡监听器。如果伸缩组使用负载均衡健康检查方式,伸缩组中的实例需要启用负载均衡器的监听端口才能通过健康检查。端口启用可在安全组中进行配置,可参考添加安全组规则进行操作。 | To be tested |
|  | ListScalingGroups | 根据输入条件过滤查询弹性伸缩组列表。查询结果分页显示。可根据伸缩组名称,伸缩配置ID,伸缩组状态,企业项目ID,起始行号,记录条数进行条件过滤查询。若不加过滤条件默认最多查询租户下20条伸缩组信息。 | To be tested |
|  | ResumeScalingGroup | 启用或停止一个指定弹性伸缩组。已停用状态的伸缩组,不会自动触发任何伸缩活动。当伸缩组正在进行伸缩活动,即使停用,正在进行的伸缩活动也不会立即停止。 | To be tested |
|  | UpdateScalingGroup | 修改一个指定弹性伸缩组中的信息。更换伸缩组的伸缩配置,伸缩组中已经存在的使用之前伸缩配置创建的云服务器云主机不受影响。伸缩组为没有正在进行的伸缩活动时,可以修改伸缩组的子网、可用区和负载均衡配置。当伸缩组的期望实例数改变时,会触发伸缩活动加入或移出实例。期望实例数必须大于或等于最小实例数,必须小于或等于最大实例数。 | To be tested |
|  | DeleteScalingGroup | 删除一个指定弹性伸缩组。force_delete属性表示如果伸缩组存在ECS实例或正在进行伸缩活动,是否强制删除伸缩组并移出和释放ECS实例。默认值为no,表示不强制删除伸缩组。如果force_delete的值为no,必须满足以下两个条件,才能删除伸缩组:条件一:伸缩组没有正在进行的伸缩活动。条件二:伸缩组当前的ECS实例数量(current_instance_number)为0。如果force_delete的值为yes,伸缩组会被置于DELETING状态,拒绝接收新的伸缩活动请求,然后等待已有的伸缩活动完成,最后将伸缩组内所有ECS实例移出伸缩组(用户手动添加的ECS实例会被移出伸缩组,弹性伸缩自动创建的ECS实例会被自动删除)并删除伸缩组。 | To be tested |
| 弹性伸缩配置 | BatchDeleteScalingConfigs | 批量删除指定弹性伸缩配置。被伸缩组使用的伸缩配置不能被删除。单次最多删除伸缩配置个数为50。 | To be tested |
|  | DeleteScalingConfig | 删除一个指定弹性伸缩配置。 | To be tested |
|  | ListScalingConfigs | 根据输入条件过滤查询弹性伸缩配置。查询结果分页显示。可以根据伸缩配置名称,镜像ID,起始行号,记录条数进行条件过滤查询。若不加过滤条件默认最多查询租户下20条伸缩配置信息。 | To be tested |
|  | ShowScalingConfig | 根据伸缩配置ID查询一个弹性伸缩配置的详细信息。 | To be tested |
|  | CreateScalingConfig | 创建弹性伸缩配置。伸缩配置是伸缩组内实例(弹性云服务器云主机)的模板,定义了伸缩组内待添加的实例的规格数据。伸缩配置与伸缩组是解耦的,同一伸缩配置可以被多个伸缩组使用。默认最多可以创建100个伸缩配置。 | To be tested |
| 标签管理 | ListScalingTagInfosByResourceId | 根据项目ID和资源ID查询指定资源类型的资源标签列表。 | To be tested |
|  | DeleteScalingTagInfo | 创建或删除指定资源的标签。每个伸缩组最多添加10个标签。 | To be tested |
|  | CreateScalingTagInfo | 创建或删除指定资源的标签。每个伸缩组最多添加10个标签。 | To be tested |
|  | ListScalingTagInfosByTenantId | 根据项目ID查询指定资源类型的标签列表。 | To be tested |
|  | ListResourceInstances | 根据项目ID查询指定资源类型的资源实例。资源、资源tag默认按照创建时间倒序。 | To be tested |
| 生命周期挂钩管理 | AttachCallbackInstanceLifeCycleHook | 通过生命周期操作令牌或者通过实例ID和生命周期挂钩名称对伸缩实例指定的挂钩进行回调操作。如果在超时时间结束前已完成自定义操作,选择终止或继续完成生命周期操作。如果需要更多时间完成自定义操作,选择延长超时时间,实例保持等待状态的时间将增加1小时。只有实例的生命周期挂钩状态为 HANGING 时才可以进行回调操作。 | To be tested |
|  | ListLifeCycleHooks | 根据伸缩组ID查询生命周期挂钩列表。 | To be tested |
|  | CreateLifyCycleHook | 创建生命周期挂钩,可为伸缩组添加一个或多个生命周期挂钩,最多添加5个。添加生命周期挂钩后,当伸缩组进行伸缩活动时,实例将被生命周期挂钩挂起并置于等待状态(正在加入伸缩组或正在移出伸缩组),实例将保持此状态直至超时时间结束或者用户手动回调。用户能够在实例保持等待状态的时间段内执行自定义操作,例如,用户可以在新启动的实例上安装或配置软件,也可以在实例终止前从实例中下载日志文件。 | To be tested |
|  | DeleteLifecycleHook | 删除一个指定生命周期挂钩。伸缩组进行伸缩活动时,不允许删除该伸缩组内的生命周期挂钩。 | To be tested |
|  | UpdateLifeCycleHook | 修改一个指定生命周期挂钩中的信息。 | To be tested |
|  | ListHookInstances | 添加生命周期挂钩后,当伸缩组进行伸缩活动时,实例将被挂钩挂起并置于等待状态,根据输入条件过滤查询弹性伸缩组中伸缩实例的挂起信息。可根据实例ID进行条件过滤查询。若不加过滤条件默认查询指定伸缩组内所有实例挂起信息。 | To be tested |
|  | ShowLifeCycleHook | 根据伸缩组ID及生命周期挂钩名称查询指定的生命周期挂钩详情。 | To be tested |
| 计划任务 | DeleteGroupScheduledTask | 删除计划任务 | To be tested |
|  | UpdateGroupScheduledTask | 更新计划任务 | To be tested |
|  | CreateGroupScheduledTask | 创建计划任务 | To be tested |
|  | ListGroupScheduledTasks | 查询计划任务列表 | To be tested |
| 通知管理 | DeleteScalingNotification | 删除指定的弹性伸缩组中指定的通知。 | To be tested |
|  | ListScalingNotifications | 根据伸缩组ID查询指定弹性伸缩组的通知列表。 | To be tested |
|  | CreateScalingNotification | 给弹性伸缩组配置通知功能。每调用一次该接口,伸缩组即配置一个通知主题及其通知场景,每个伸缩组最多可以增加5个主题。通知主题由用户事先在SMN创建并进行订阅,当通知主题对应的通知场景出现时,伸缩组会向用户的订阅终端发送通知。 | To be tested |
| 配额管理 | ShowResourceQuota | 查询指定租户下的弹性伸缩组、伸缩配置、伸缩带宽策略、伸缩策略和伸缩实例的配额总数及已使用配额数。 | To be tested |
|  | ShowPolicyAndInstanceQuota | 根据伸缩组ID查询指定弹性伸缩组下的伸缩策略和伸缩实例的配额总数及已使用配额数。 | To be tested |
