# DDM MCP Server 

## 版本信息
v0.1.0

## 产品描述

DDM MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DDM交互的能力。可以基于自然语言对DDM资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| DDM会话管理 | ExecuteKillPhysicalProcesses | kill物理会话 | To be tested |
|  | ShowProcessesAuditLog | 查询kill会话审计日志 | To be tested |
|  | ShowLogicalProcesses | 查询逻辑会话列表 | To be tested |
|  | ShowPhysicalProcesses | 查询物理会话列表 | To be tested |
|  | ExecuteKillLogicalProcesses | kill逻辑会话 | To be tested |
| DDM实例管理 | ShrinkInstanceNodes | 对指定的DDM实例的节点个数进行缩容。 | To be tested |
|  | CreateInstance | 创建一个DDM实例。 | To be tested |
|  | UpdateReadAndWriteStrategy | 修改DDM已关联的数据库实例的读策略。 | To be tested |
|  | RestartInstance | 重启指定的DDM实例。 | To be tested |
|  | ExpandDdmInstanceNodes | 对指定的DDM实例的节点个数进行扩容,支持按需实例与包周期实例。 | To be tested |
|  | ListInstances | 查询DDM实例列表。 | To be tested |
|  | ShowInstanceParam | 查询DDM指定实例的参数详情。 | To be tested |
|  | ListDdmEngines | 查询DDM引擎信息 | To be tested |
|  | ListNodes | 查询DDM实例节点列表。 | To be tested |
|  | UpdateDatabaseInfo | 同步当前DDM实例已关联的所有DN实例配置信息。 | To be tested |
|  | SwitchSsl | 为实例设置SSL数据加密。 | To be tested |
|  | ShowInstance | 查询指定DDM实例的详细信息。 | To be tested |
|  | ShowNode | 查询DDM实例节点详情。 | To be tested |
|  | CreateGroup | 创建组 | To be tested |
|  | UpdateInstanceParam | 修改DDM实例参数。 | To be tested |
|  | UpdateInstanceSecurityGroup | 修改DDM实例安全组。 | To be tested |
|  | ShowDdmJobResult | 获取指定ID的任务信息 | To be tested |
|  | ListGroup | 获取实例组信息列表 | To be tested |
|  | DeleteInstance | 删除指定的DDM实例,释放该实例的所有资源。 | To be tested |
|  | ResizeFlavor | 变更DDM实例规格。 | To be tested |
|  | ListDdmFlavors | 查询DDM可用区规格信息 | To be tested |
|  | ListFlavors | 查询DDM可用区规格信息详情。 | To be tested |
|  | ListEngines | 查询DDM引擎信息详情。 | To be tested |
|  | DeleteDdmInstance | 删除指定的DDM实例,释放该实例的所有资源。 | To be tested |
|  | RebuildConfig | DDM实例跨region容灾场景下,针对目标DDM实例实现表数据reload,使数据同步。 | To be tested |
|  | ExpandInstanceNodes | 对指定的DDM实例的节点个数进行扩容,支持按需实例与包周期实例。 | To be tested |
|  | UpdateInstanceName | 修改DDM实例名称。 | To be tested |
| DDM帐号管理 | ResetAdministrator | 首次调用时新建DDM管理员帐号并设置密码。后续调用时仅更新管理员密码。 | To be tested |
|  | ResetUserPassword | 重置现有DDM帐号的密码。 | To be tested |
|  | CreateUsers | DDM帐号用于连接和管理逻辑库。一个DDM实例最多能创建100个DDM帐号,一个DDM帐号可以关联多个逻辑库。 | To be tested |
|  | UpdateUser | 修改现有DDM帐号的权限或者与逻辑库的管理关系。 | To be tested |
|  | ValidateWeakPassword | 弱密码校验 | To be tested |
|  | ListUsers | 查询DDM帐号列表。 | To be tested |
|  | DeleteUser | 删除指定的DDM实例帐号,如果帐号关联了逻辑库,则对应的关联关系也会删除。 | To be tested |
| DDM监控管理 | ListSlowLog | 查询指定时间段内在DDM实例上执行过的慢sql相关信息。 | To be tested |
|  | ListReadWriteRatio | 查询指定时间段内在DDM实例的读写次数。 | To be tested |
|  | ListSlowLogs | 查询指定时间段内在DDM实例上执行过的慢sql相关信息。 | To be tested |
| DDM逻辑库管理 | DeleteDatabase | 删除指定的逻辑库,释放该逻辑库的所有资源。 | To be tested |
|  | ListDatabases | 查询DDM逻辑库列表。 | To be tested |
|  | ShowDatabase | 查询指定逻辑库的详细信息。 | To be tested |
|  | CreateDdmDatabase | 创建DDM逻辑库。 | To be tested |
|  | ListAvailableRdsList | 查询创建逻辑库可选取的数据库实例列表。 | To be tested |
|  | CreateDatabase | 创建DDM逻辑库。 | To be tested |
|  | DeleteDdmDatabase | 删除指定的逻辑库。 | To be tested |
| 参数配置 | ListDdmConfigurations | 获取参数模板列表,包括所有DDM的默认参数模板和用户创建的参数模板。 | To be tested |
|  | ShowConfiguration | 获取指定参数模板的参数 | To be tested |
| 查询API版本 | ListApiVersion | 查询API版本列表。 | To be tested |
| 版本管理 | ChangeDatabaseVersion | 变更内核版本 | To be tested |
|  | ShowRiskInfo | 内核版本风险提醒 | To be tested |
|  | ListDatabaseAvailableVersions | 查询可变更内核版本 | To be tested |
|  | RollBackDatabaseVersion | 回滚内核版本 | To be tested |
