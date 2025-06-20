# DLI MCP Server 

## 版本信息
v0.1.0

## 产品描述

DLI MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DLI交互的能力。可以基于自然语言对DLI资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Flink作业-作业相关API | ShowFlinkJobExecutionGraph | 查询Flink作业执行计划。 | To be tested |
|  | ListFlinkJobs | 查询当前用户的作业列表,可以根据作业ID作为ID,查询大于ID或小于ID的限定条数的作业,默认查询全部状态的作业,也可以设定运行中或其他状态条件。 | To be tested |
|  | BatchRunFlinkJobs | 触发批量运行Flink作业。 | To be tested |
|  | CreateFlinkJarJob | 用户自定义作业目前支持jar格式,运行在独享集群中。 | To be tested |
|  | BatchDeleteFlinkJobs | 批量删除任何状态的作业。 | To be tested |
|  | BatchStopFlinkJobs | 批量停止正在运行的Flink作业。 | To be tested |
|  | CreateFlinkSqlJobGraph | 生成flink SQL作业的静态流图 | To be tested |
|  | UpdateFlinkSqlJob | Stream SQL的语法扩展了Apache Flink SQL。 | To be tested |
|  | ShowFlinkJob | 查看一个Flink作业的详情信息。 | To be tested |
|  | ImportFlinkJobs | 通过POST方式,导入flink作业,请求体为JSON格式。 | To be tested |
|  | CreateFlinkSqlJob | 通过POST方式,提交流式SQL作业,请求体为JSON格式。 | To be tested |
|  | UpdateFlinkJarJob | 更新用户自定义作业,目前支持jar格式,运行在独享集群中。 | To be tested |
|  | ExportFlinkJobs | 通过POST方式,导出flink作业,请求体为JSON格式。 | To be tested |
|  | DeleteFlinkJob | 删除任何状态的作业。 | To be tested |
| Flink作业-模板相关API | CreateFlinkSqlJobTemplate | 在DLI服务中新建一个Flink作业模板,最多100个。 | To be tested |
|  | ListFlinkSqlJobTemplates | 查询Flink作业模板列表。当前只支持查询用户自定义模板。 | To be tested |
|  | UpdateFlinkSqlJobTemplate | 对DLI服务中已有的Flink作业模板进行更新。 | To be tested |
|  | DeleteFlinkSqlJobTemplate | 删除一个Flink作业模板,即使当前模板正在被作业使用,也允许删除。 | To be tested |
| Flink作业-管理相关API | ImportFlinkJobSavepoint | 导入Flink作业保存点。 | To be tested |
|  | ExecuteFlinkJobSavepoint | 触发Flink作业保存点。 | To be tested |
| SQL作业-作业相关API | CancelSqlJob | 该API用于取消已经提交的作业,若作业已经执行结束或失败则无法取消。 | To be tested |
|  | ExportSqlJobResult | 该API用于将SQL语句的查询结果导出到OBS对象存储中,只支持导出“QUERY”类型作业的查询结果。 | To be tested |
|  | ShowSqlJobProgress | 该API用于获取作业执行进度信息,如果作业正在执行,可以获取到子作业的信息,如果作业刚开始或者已经结束,不可以获取到子作业信息。 | To be tested |
|  | CheckSql | 该API用于检查SQL语法。 | To be tested |
|  | ShowSqlJobDetail | 该API用于查询作业的详细信息,如作业的databasename、tablename、file size和export mode等信息。 | To be tested |
|  | ShowSqlJobStatus | 该API用于在作业提交后查询作业状态。 | To be tested |
|  | PreviewSqlJobResult | 该API用于在执行SQL查询语句的作业完成后,查看该作业执行的结果。目前仅支持查看“QUERY”类型作业的执行结果。 | To be tested |
|  | ListSqlJobs | 该API用于查询当前工程下面的所有作业的信息。 | To be tested |
|  | CreateSqlJob | 该API用于通过执行SQL语句的方式向队列提交作业。 | To be tested |
| SQL作业-拦截规则相关API | UpdateSqlJobDefendRule | 该API用于更新SQL拦截规则,拦截匹配规则的SQL。 | To be tested |
|  | CreateSqlJobDefendRule | 该API用于创建SQL拦截规则,拦截匹配规则的SQL。 | To be tested |
|  | ShowSqlJobSystemDefendRule | 该API用于获取系统预制SQL拦截规则。 | To be tested |
|  | DeleteSqlJobDefendRule | 该API用于删除SQL拦截规则。 | To be tested |
|  | ListSqlJobSystemDefendRules | 该API用于获取系统预制SQL拦截规则。 | To be tested |
|  | ShowSqlJobDefendRule | 该API用于获取单个SQL拦截规则。 | To be tested |
|  | ListSqlJobDefendRules | 该API用于批量获取SQL拦截规则。 | To be tested |
| SQL作业-模板相关API | BatchDeleteSqlJobTemplates | 该API用于批量删除SQL模板。 | To be tested |
|  | UpdateSqlJobTemplate | 该API用于更新SQL模板。 | To be tested |
|  | CreateSqlJobTemplate | 该API用于存储指定的SQL语句,后续可以重复使用。 | To be tested |
|  | ListSqlJobTemplates | 该API用查看用户保存的所有SQL模板。 | To be tested |
| Spark作业-作业相关API | ShowSparkJob | 该API用于根据批处理作业的id查询作业详情。 | To be tested |
|  | CancelSparkJob | 该API用于取消批处理作业。 | To be tested |
|  | ListSparkJobs | 该API用于查询Project下某队列批处理作业的列表。 | To be tested |
|  | CreateSparkJob | 该API用于在某个队列上创建作业。 | To be tested |
|  | ShowSparkJobStatus | 该API用于查询批处理作业的状态。 | To be tested |
| Spark作业-模板相关API | ShowSparkJobTemplate | 该API用于获取作业模板。 | To be tested |
|  | UpdateSparkJobTemplate | 该API用于修改作业模板。 | To be tested |
|  | ListSparkJobTemplates | 该API用于查询作业模板列表。 | To be tested |
|  | CreateSparkJobTemplate | 该API用于创建作业模板。 | To be tested |
| 全局变量相关API | UpdateGlobalVariable | 修改全局变量。 | To be tested |
|  | DeleteGlobalVariable | 删除全局变量。 | To be tested |
|  | ListGlobalVariables | 查询全局变量列表。 | To be tested |
|  | CreateGlobalVariable | 创建全局变量。全局变量用于替换SQL作业中的敏感数据。 | To be tested |
| 动态脱敏策略相关API | ShowDataMaskStrategy | 该API用于获取单个动态脱敏策略。 | To be tested |
|  | DeleteDataMaskStrategy | 该API用于删除动态脱敏策略。 | To be tested |
|  | CreateDataMaskStrategyUserAuth | 该API用于动态脱敏策略授权。 | To be tested |
|  | ListDataMaskStrategies | 该API用于批量获取动态脱敏策略。 | To be tested |
|  | CreateDataMaskStrategy | 该API用于动态脱敏策略,SQL执行的结果脱敏展示。 | To be tested |
|  | ShowDataMaskStrategyUserAuth | 该API用于获取脱敏策略权限。 | To be tested |
|  | UpdateDataMaskStrategy | 该API用于更新动态脱敏策略,SQL执行的结果脱敏展示。 | To be tested |
| 增强型跨源连接相关API | ListJobAuthInfos | 该API用于查询跨源认证信息。 | To be tested |
|  | CreateJobAuthInfo | 该API用于创建跨源认证。 | To be tested |
|  | ShowEnhancedConnectionPrivilege | 该API用于查询增强型跨源连接授权的信息。 | To be tested |
|  | ShowEnhancedConnection | 该API用于查询该用户指定的已创建的增强型跨源连接。 | To be tested |
|  | CreateRouteToEnhancedConnection | 该API用于创建跨源需要的路由。 | To be tested |
|  | DeleteJobAuthInfo | 该API用于删除跨源认证信息。 | To be tested |
|  | DeleteRouteFromEnhancedConnection | 该API用于删除跨源需要的路由。 | To be tested |
|  | UpdateJobAuthInfo | 该API用于更新跨源认证信息。 | To be tested |
|  | DeleteEnhancedConnection | 该API用于删除已创建的增强型跨源连接。 | To be tested |
|  | UpdateEnhancedConnection | 该API用于在跨源中修改数据源主机信息,仅支持全量覆盖。 | To be tested |
|  | ListEnhancedConnections | 该API用于查询该用户已创建的增强型跨源连接列表。 | To be tested |
|  | DisassociateQueueFromEnhancedConnection | 该API用于在增强型跨源中解绑已绑定的队列。 | To be tested |
|  | CreateEnhancedConnection | 该API用于创建与其他服务的增强型跨源连接。 | To be tested |
|  | AssociateQueueToEnhancedConnection | 该API用于在已创建的增强型跨源中绑定队列。 | To be tested |
| 已弃用-Flink作业-作业相关API | RegisterBucket | 用户主动授权OBS桶的操作权限给DLI服务, 用于保存用户作业的checkpoint、作业的运行日志等。 | To be tested |
|  | ShowFlinkMetric | 查询Flink作业监控信息, 支持同时查询多个Flink作业的监控信息。 | To be tested |
|  | CreateIefSystemEvents | 该API用于处理IEF系统事件上报 | To be tested |
|  | UpdateFlinkJobStatusReport | 该API用于处理边缘Flink作业状态上报信息 | To be tested |
|  | RunIefJobActionCallBack | 该API用于处理IEF Flink作业action回调信息 | To be tested |
|  | CreateIefMessageChannel | 该API用于创建IEF消息通道 | To be tested |
| 已弃用-SQL作业相关API | ListTables | 该API用于查询指定数据库下符合过滤条件的或所有的表信息。 | To be tested |
|  | ListPartitions |  | To be tested |
|  | ListSqlSampleTemplates | 该API用于查询所有SQL样例模板。 | To be tested |
|  | DeleteDatabase | 该API用于删除空数据库,若待删除的数据库中存在表,则需先删除其中的所有表。 | To be tested |
|  | UpdateDatabaseOwner | 用于修改数据库的owner。 | To be tested |
|  | DeleteTable | 该API用于删除指定的表。 | To be tested |
|  | CreateDatabase | 该API用于新增数据库。 | To be tested |
|  | PreviewTable | 该API用于用于预览表中前10行的内容。 | To be tested |
|  | ImportTable | 该API用于将数据从文件导入DLI或OBS表,目前仅支持将OBS上的数据导入DLI或OBS中。 | To be tested |
|  | ExportTable | 该API用于将SQL语句的查询结果导出到OBS对象存储中,只支持导出“QUERY”类型作业的查询结果。 | To be tested |
|  | ListDatabases | 该API用于查询出所有的数据库信息。 | To be tested |
|  | UpdateTableOwner | 用于修改表的owner。 | To be tested |
|  | ShowTable | 该API用于描述指定表的元数据信息。 | To be tested |
|  | CreateTable | 该API用于创建新的表。 | To be tested |
| 已弃用-Spark作业-作业相关API | ShowSparkJobLog | 该API用于查询批处理作业的后台日志。 | To be tested |
| 已弃用-分组资源相关API | UploadPythonFileJobResources | 该API用于在project下的上传pyfile类型模块。 | To be tested |
|  | UploadFileJobResources | 该API用于在project下上传file类型模块。 | To be tested |
|  | UploadJobResources | 该API用于上传分组资源到某个project下。 | To be tested |
|  | UpdateJobResourceOwner | 用于修改程序包的owner。 | To be tested |
|  | UploadJarJobResources | 该API用于在project下上传jar类型分组资源。 | To be tested |
|  | ShowJobResource | 该API用于查看某个project某个分组下的具体资源信息。 | To be tested |
|  | ListJobResources | 该API用于查看某个project下的所有资源,其中包含Group。 | To be tested |
|  | DeleteJobResource | 该API用于删除某个project某个分组下的资源包 | To be tested |
| 已弃用-委托与权限相关API | ListQueueUsers | 该API用于查询可以使用的指定队列的所有用户名称。 | To be tested |
|  | ListDatabaseUsers | 该API用于查询可以使用的指定队列的所有用户名称。 | To be tested |
|  | RunDataAuthorizationAction | 该API用于将数据库或数据表的数据权限赋给指定的其他用户。 | To be tested |
|  | ListTablePrivileges | 该API用于查询指定用户在表上的权限。 | To be tested |
|  | ListTableUsers | 该API用于查看有权访问指定表或表的列的所有用户。 | To be tested |
|  | CreateDliAgency | 创建DLI委托 | To be tested |
|  | RegisterAuthorizedQueue | 该API用于与其他用户共享指定的队列,可以给用户赋使用指定的队列的权限或者收回使用权限。 | To be tested |
|  | ShowDliAgency | 获取dli委托信息 | To be tested |
| 已弃用-跨源连接相关API | ShowDatasourceConnection | 该API用于查询该用户指定的已创建的经典型跨源连接。 | To be tested |
|  | UpdateAuthInfo | 该API用于更新跨源认证信息。 | To be tested |
|  | ListAuthInfo | 该API用于查询跨源认证信息。 | To be tested |
|  | ListDatasourceConnections | 该API用于查询该用户已创建的经典型跨源连接列表。 | To be tested |
|  | CreateEnhancedConnectionRoutes | 该API用于创建跨源需要的路由。 | To be tested |
|  | DeleteAuthInfo | 该API用于删除跨源认证信息。 | To be tested |
|  | CreateDatasourceConnection | 该API用于创建与其他服务的经典型跨源连接。 | To be tested |
|  | DeleteEnhancedConnectionRoutes | 该API用于删除跨源需要的路由。 | To be tested |
|  | CreateAuthInfo | 该API用于创建跨源认证。 | To be tested |
|  | DeleteDatasourceConnection | 该API用于删除已创建的经典型跨源连接。 | To be tested |
| 已弃用-队列相关API | BatchDeleteQueuePlans | 该API用于批量删除队列定时扩缩容计划。 | To be tested |
|  | ListQueuePlans | 查看队列定时扩缩容计划接口,列出指定队列定时规格变更计划。 | To be tested |
|  | UpdateQueueCidr | 该功能用于修改包年包月队列网段。 | To be tested |
|  | DeleteQueuePlan | 该API用于删除指定ID的队列定时扩缩容计划。 | To be tested |
|  | UpdateQueuePlan | 该API用于修改指定ID的队列定时扩缩容计划。 | To be tested |
|  | CreateQueuePlan | 创建队列定时扩缩容计划接口,对指定的队列创建定时规格变更计划。 | To be tested |
| 弹性资源池相关API | CreatePeriodElasticResourcePoolSpecChangeOrder | 包周期弹性资源池规格变更下单接口 | To be tested |
|  | ListElasticResourcePoolScaleRecords | 查询当前弹性资源池扩缩容历史记录 | To be tested |
|  | ListElasticResourcePools | 查询所有弹性资源池 | To be tested |
|  | AssociateQueueToElasticResourcePool | 关联队列到弹性资源池 | To be tested |
|  | DeleteElasticResourcePool | 删除弹性资源池 | To be tested |
|  | UpdateElasticResourcePoolQueue | 设置弹性资源池指定队列的扩缩容策略信息。 | To be tested |
|  | CreatePeriodElasticResourcePoolOrder | 创建包周期弹性资源池 | To be tested |
|  | CreateElasticResourcePool | 创建弹性资源池 | To be tested |
|  | UpdateElasticResourcePool | 修改弹性资源池信息 | To be tested |
|  | ListElasticResourcePoolQueues | 查询弹性资源池所属队列 | To be tested |
| 数据目录相关API | ShowCatalog | 该API用于描述DLI catalog详情 | To be tested |
|  | ListCatalogs | 该API获取指定项目下所有catalog信息 | To be tested |
|  | RunCatalogAction | 该API创建DLI绑定/解绑到lakeformation等服务的元数据目录(CATALOG)相关信息。 | To be tested |
| 权限相关API | RunAuthorizationAction | 该API用于将DLI资源权限赋给、回收、更新指定的其他用户或项目。 | To be tested |
|  | ListAuthorizationPrivileges | 获取对象赋权用户的权限信息 | To be tested |
| 资源标签相关API | ListResourcesTags | 查询指定资源类型的标签信息。 | To be tested |
|  | BatchCreateResourceTags | 批量添加资源标签。 | To be tested |
|  | CountResourcesByTags | 查询资源实例数量。 | To be tested |
|  | ListResourcesByTags | 查询资源实例列表。 | To be tested |
|  | BatchDeleteResourceTags | 批量删除资源标签。 | To be tested |
|  | ShowResourceTags | 查询指定资源实例的标签信息。 | To be tested |
| 配额相关API | ShowQuota | 该API用于获取用户配额信息列表。 | To be tested |
| 队列相关API | CreateQueueProperty | 该接口用于增加队列属性, 一次可增加多个属性。 | To be tested |
|  | ShowConnectivityTask | 该API用于在连通性测试提交后查询连通性结果。 | To be tested |
|  | DeleteQueue | 该API用于删除指定队列。 | To be tested |
|  | ListQueues | 该API用于列出该project下所有的队列。 | To be tested |
|  | UpdateQueueProperty | 更新队列属性 | To be tested |
|  | CreateQueue | 该API用于创建队列,该队列将会绑定用户指定的计算资源。 | To be tested |
|  | ShowQueue | 该API用于列出该project下指定的队列详情。 | To be tested |
|  | ListQueueProperties | 获取队列配置的属性 | To be tested |
|  | RunQueueAction | 该功能用于重新启动队列、扩容队列、缩容队列。 | To be tested |
|  | CreateConnectivityTask | 创建地址连通性请求API接口,往指定集群发送地址连通性测试请求,并将测试地址插入表内 | To be tested |
|  | DeleteQueueProperty | 该接口用于删除队列的属性,一次可删除多个属性值。 | To be tested |
