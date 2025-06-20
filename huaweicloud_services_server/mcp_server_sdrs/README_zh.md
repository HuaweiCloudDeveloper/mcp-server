# SDRS MCP Server 

## 版本信息
v0.1.0

## 产品描述

SDRS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务SDRS交互的能力。可以基于自然语言对SDRS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| API版本信息 | ListApiVersions | 查询存储容灾当前所有可用的版本信息列表。 | To be tested |
|  | ShowSpecifiedApiVersion | 查询存储容灾指定API版本信息。 | To be tested |
| Job管理 | ShowJobStatus | 查询job的执行状态。 | To be tested |
| 任务中心 | DeleteServerGroupFailureJobs | 删除指定保护组内的所有失败任务,创建保护实例失败、创建复制对失败、删除保护实例失败、删除复制对失败等。 | To be tested |
|  | DeleteAllServerGroupFailureJobs | 删除所有保护组层级的失败任务,创建、删除保护组失败等。 | To be tested |
|  | DeleteFailureJob | 删除单个失败任务。 | To be tested |
|  | ListFailureJobs | 查询所有保护组失败任务列表或者指定保护组下的所有失败任务列表。 | To be tested |
| 保护实例 | DeleteProtectedInstance | 删除指定的保护实例。 | To be tested |
|  | ShowProtectedInstance | 查询单个保护实例的详细信息,如名称、ID等。 | To be tested |
|  | BatchCreateProtectedInstances | 典型场景:没有特殊操作场景 | To be tested |
|  | AttachProtectedInstanceReplication | 将指定的复制对挂载到指定的保护实例上。 | To be tested |
|  | AddProtectedInstanceNic | 给指定的保护实例添加网卡。 | To be tested |
|  | ListProtectedInstances | 查询当前租户下的所有保护实例列表。 | To be tested |
|  | DetachProtectedInstanceReplication | 将指定的复制对从指定的保护实例上卸载。 | To be tested |
|  | DeleteProtectedInstanceNic | 删除指定保护实例的指定网卡。 | To be tested |
|  | UpdateProtectedInstanceName | 更新某一个保护实例的名称。 | To be tested |
|  | BatchDeleteProtectedInstances | 典型场景:没有特殊操作场景 | To be tested |
|  | CreateProtectedInstance | 创建保护实例。保护实例创建完成后,系统默认容灾站点云服务器名称与生产站点云服务器名称相同,但ID不同。如果需要修改云服务器名称,请在保护实例详情页面单击云服务器名称,进入云服务器详情页面进行修改 | To be tested |
|  | ResizeProtectedInstance | 变更指定保护实例中弹性云服务器的规格,包括:同时变更生产站点云服务器和容灾站点云服务器的规格。 | To be tested |
| 保护组 | StopProtectionGroup | 对某一个保护组的停止保护操作。 | To be tested |
|  | StartReverseProtectionGroup | 对保护组进行切换操作,可以将保护组的当前生产站点,从创建保护组时指定的生产站点切换到创建保护组时指定的容灾站点,也可以从创建保护组时指定的容灾站点切换到创建保护组时指定的生产站点。切换后,生产站点和容灾站点的数据仍然处于被保护状态,只是复制方向与操作之前相反。 | To be tested |
|  | StartFailoverProtectionGroup | 当保护组的生产站点发生故障时,将保护组的生产站点切到当前的容灾站点,即另一端AZ,启用当前容灾站点的云硬盘以及云服务器等资源。 | To be tested |
|  | ShowProtectionGroup | 查询单个保护组的详细信息,如ID、名称等。 | To be tested |
|  | DeleteProtectionGroup | 删除指定的保护组。 | To be tested |
|  | UpdateProtectionGroupName | 更新某一个保护组的名称。 | To be tested |
|  | ListProtectionGroups | 查询当前租户所有的保护组列表。 | To be tested |
|  | StartProtectionGroup | 对某一个保护组的“开启保护”或“重保护”操作。 | To be tested |
|  | CreateProtectionGroup | 创建保护组。 | To be tested |
| 复制对 | ListReplications | 查询指定保护组下的所有复制对列表,如果不给定指定保护组则查询当前租户下的所有复制对列表。 | To be tested |
|  | DeleteReplication | 删除指定的复制对。 | To be tested |
|  | CreateReplication | 创建复制对,并将其添加到指定的保护组中。 | To be tested |
|  | ShowReplication | 查询单个复制对的详细信息。 | To be tested |
|  | UpdateReplicationName | 更新复制对名称。 | To be tested |
|  | ExpandReplication | 对复制对包含的两个磁盘进行扩容操作。 | To be tested |
| 大屏管理 | ListRpoStatistics | 查询当前租户大屏显示中,资源的RPO超标趋势记录列表。 | To be tested |
| 容灾演练 | ShowDisasterRecoveryDrill | 查询单个容灾演练的详细信息。 | To be tested |
|  | ListDisasterRecoveryDrills | 查询指定保护组下的所有容灾演练列表,当未指定保护组时查询当前租户下的所有容灾演练列表。 | To be tested |
|  | CreateDisasterRecoveryDrill | 创建容灾演练。 | To be tested |
|  | DeleteDisasterRecoveryDrill | 删除指定的容灾演练。删除后: | To be tested |
|  | UpdateDisasterRecoveryDrillName | 更新容灾演练的名称。 | To be tested |
| 查询双活域 | ListActiveActiveDomains | 查询双活域。双活域由本端存储设备、远端存储设备组成,通过双活域,应用服务器可以实现跨站点的数据访问。 | To be tested |
| 标签管理 | AddProtectedInstanceTags | 一个保护实例上最多有10个标签。此接口为幂等接口:创建时,如果创建的标签已经存在(key相同),则覆盖。 | To be tested |
|  | ListProtectedInstancesByTags | 使用标签过滤保护实例 | To be tested |
|  | ListProtectedInstancesProjectTags | 查询租户在指定Project中保护实例的所有资源标签集合。 | To be tested |
|  | ListProtectedInstanceTags | 查询指定保护实例的标签信息。 | To be tested |
|  | DeleteProtectedInstanceTag | 幂等接口:删除时,不对标签字符集做校验,调用接口前必须要做encodeURI,服务端需要对接口URI做decodeURI。 | To be tested |
|  | BatchAddTags | 为指定保护实例批量添加或删除标签。一个资源上最多有10个标签。 | To be tested |
|  | BatchDeleteTags | 为指定保护实例批量删除标签。一个资源上最多有10个标签。 | To be tested |
| 租户配额管理 | ShowQuota | 查询资源的配额相关信息。 | To be tested |
