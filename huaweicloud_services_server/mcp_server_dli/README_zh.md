# DLI MCP Server 


## Version
v0.1.0

## Overview

DLI MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DLI. Full-chain management of DLI resources can be carried out based on natural language.

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
                    <td rowspan="14">Flink作业-作业相关API</td>
                    <td>ShowFlinkJobExecutionGraph</td>
                    <td>查询Flink作业执行计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlinkJobs</td>
                    <td>查询当前用户的作业列表,可以根据作业ID作为ID,查询大于ID或小于ID的限定条数的作业,默认查询全部状态的作业,也可以设定运行中或其他状态条件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRunFlinkJobs</td>
                    <td>触发批量运行Flink作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFlinkJarJob</td>
                    <td>用户自定义作业目前支持jar格式,运行在独享集群中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteFlinkJobs</td>
                    <td>批量删除任何状态的作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopFlinkJobs</td>
                    <td>批量停止正在运行的Flink作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFlinkSqlJobGraph</td>
                    <td>生成flink SQL作业的静态流图</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlinkSqlJob</td>
                    <td>Stream SQL的语法扩展了Apache Flink SQL。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlinkJob</td>
                    <td>查看一个Flink作业的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportFlinkJobs</td>
                    <td>通过POST方式,导入flink作业,请求体为JSON格式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFlinkSqlJob</td>
                    <td>通过POST方式,提交流式SQL作业,请求体为JSON格式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlinkJarJob</td>
                    <td>更新用户自定义作业,目前支持jar格式,运行在独享集群中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportFlinkJobs</td>
                    <td>通过POST方式,导出flink作业,请求体为JSON格式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFlinkJob</td>
                    <td>删除任何状态的作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Flink作业-模板相关API</td>
                    <td>CreateFlinkSqlJobTemplate</td>
                    <td>在DLI服务中新建一个Flink作业模板,最多100个。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlinkSqlJobTemplates</td>
                    <td>查询Flink作业模板列表。当前只支持查询用户自定义模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlinkSqlJobTemplate</td>
                    <td>对DLI服务中已有的Flink作业模板进行更新。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFlinkSqlJobTemplate</td>
                    <td>删除一个Flink作业模板,即使当前模板正在被作业使用,也允许删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Flink作业-管理相关API</td>
                    <td>ImportFlinkJobSavepoint</td>
                    <td>导入Flink作业保存点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteFlinkJobSavepoint</td>
                    <td>触发Flink作业保存点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">SQL作业-作业相关API</td>
                    <td>CancelSqlJob</td>
                    <td>该API用于取消已经提交的作业,若作业已经执行结束或失败则无法取消。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportSqlJobResult</td>
                    <td>该API用于将SQL语句的查询结果导出到OBS对象存储中,只支持导出“QUERY”类型作业的查询结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlJobProgress</td>
                    <td>该API用于获取作业执行进度信息,如果作业正在执行,可以获取到子作业的信息,如果作业刚开始或者已经结束,不可以获取到子作业信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckSql</td>
                    <td>该API用于检查SQL语法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlJobDetail</td>
                    <td>该API用于查询作业的详细信息,如作业的databasename、tablename、file size和export mode等信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlJobStatus</td>
                    <td>该API用于在作业提交后查询作业状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PreviewSqlJobResult</td>
                    <td>该API用于在执行SQL查询语句的作业完成后,查看该作业执行的结果。目前仅支持查看“QUERY”类型作业的执行结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlJobs</td>
                    <td>该API用于查询当前工程下面的所有作业的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlJob</td>
                    <td>该API用于通过执行SQL语句的方式向队列提交作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">SQL作业-拦截规则相关API</td>
                    <td>UpdateSqlJobDefendRule</td>
                    <td>该API用于更新SQL拦截规则,拦截匹配规则的SQL。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlJobDefendRule</td>
                    <td>该API用于创建SQL拦截规则,拦截匹配规则的SQL。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlJobSystemDefendRule</td>
                    <td>该API用于获取系统预制SQL拦截规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlJobDefendRule</td>
                    <td>该API用于删除SQL拦截规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlJobSystemDefendRules</td>
                    <td>该API用于获取系统预制SQL拦截规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlJobDefendRule</td>
                    <td>该API用于获取单个SQL拦截规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlJobDefendRules</td>
                    <td>该API用于批量获取SQL拦截规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">SQL作业-模板相关API</td>
                    <td>BatchDeleteSqlJobTemplates</td>
                    <td>该API用于批量删除SQL模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSqlJobTemplate</td>
                    <td>该API用于更新SQL模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlJobTemplate</td>
                    <td>该API用于存储指定的SQL语句,后续可以重复使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlJobTemplates</td>
                    <td>该API用查看用户保存的所有SQL模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Spark作业-作业相关API</td>
                    <td>ShowSparkJob</td>
                    <td>该API用于根据批处理作业的id查询作业详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelSparkJob</td>
                    <td>该API用于取消批处理作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSparkJobs</td>
                    <td>该API用于查询Project下某队列批处理作业的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSparkJob</td>
                    <td>该API用于在某个队列上创建作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSparkJobStatus</td>
                    <td>该API用于查询批处理作业的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Spark作业-模板相关API</td>
                    <td>ShowSparkJobTemplate</td>
                    <td>该API用于获取作业模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSparkJobTemplate</td>
                    <td>该API用于修改作业模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSparkJobTemplates</td>
                    <td>该API用于查询作业模板列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSparkJobTemplate</td>
                    <td>该API用于创建作业模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Tags</td>
                    <td>BatchCreateResourceTags</td>
                    <td>为指定实例批量添加标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountResourcesByTags</td>
                    <td>根据标签查询资源实例数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourcesByTags</td>
                    <td>根据标签查询资源实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteResourceTags</td>
                    <td>为指定实例批量删除标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceTags</td>
                    <td>查询指定实例的标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">仓接口</td>
                    <td>CreateTable</td>
                    <td>在指定仓内创建表,表名在仓内唯一;创建表时,指定主键模板及本地二级索引模板及全局二级索引模板。创建表时,如果仓不存在,将会自动创建仓。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">全局变量相关API</td>
                    <td>UpdateGlobalVariable</td>
                    <td>修改全局变量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGlobalVariable</td>
                    <td>删除全局变量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalVariables</td>
                    <td>查询全局变量列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGlobalVariable</td>
                    <td>创建全局变量。全局变量用于替换SQL作业中的敏感数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">动态脱敏策略相关API</td>
                    <td>ShowDataMaskStrategy</td>
                    <td>该API用于获取单个动态脱敏策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDataMaskStrategy</td>
                    <td>该API用于删除动态脱敏策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataMaskStrategyUserAuth</td>
                    <td>该API用于动态脱敏策略授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataMaskStrategies</td>
                    <td>该API用于批量获取动态脱敏策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataMaskStrategy</td>
                    <td>该API用于动态脱敏策略,SQL执行的结果脱敏展示。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataMaskStrategyUserAuth</td>
                    <td>该API用于获取脱敏策略权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataMaskStrategy</td>
                    <td>该API用于更新动态脱敏策略,SQL执行的结果脱敏展示。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">增强型跨源连接相关API</td>
                    <td>ListJobAuthInfos</td>
                    <td>该API用于查询跨源认证信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateJobAuthInfo</td>
                    <td>该API用于创建跨源认证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnhancedConnectionPrivilege</td>
                    <td>该API用于查询增强型跨源连接授权的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnhancedConnection</td>
                    <td>该API用于查询该用户指定的已创建的增强型跨源连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRouteToEnhancedConnection</td>
                    <td>该API用于创建跨源需要的路由。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteJobAuthInfo</td>
                    <td>该API用于删除跨源认证信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRouteFromEnhancedConnection</td>
                    <td>该API用于删除跨源需要的路由。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateJobAuthInfo</td>
                    <td>该API用于更新跨源认证信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnhancedConnection</td>
                    <td>该API用于删除已创建的增强型跨源连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnhancedConnection</td>
                    <td>该API用于在跨源中修改数据源主机信息,仅支持全量覆盖。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnhancedConnections</td>
                    <td>该API用于查询该用户已创建的增强型跨源连接列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateQueueFromEnhancedConnection</td>
                    <td>该API用于在增强型跨源中解绑已绑定的队列。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnhancedConnection</td>
                    <td>该API用于创建与其他服务的增强型跨源连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateQueueToEnhancedConnection</td>
                    <td>该API用于在已创建的增强型跨源中绑定队列。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">已弃用-Flink作业-作业相关API</td>
                    <td>RegisterBucket</td>
                    <td>用户主动授权OBS桶的操作权限给DLI服务, 用于保存用户作业的checkpoint、作业的运行日志等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlinkMetric</td>
                    <td>查询Flink作业监控信息, 支持同时查询多个Flink作业的监控信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIefSystemEvents</td>
                    <td>该API用于处理IEF系统事件上报</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlinkJobStatusReport</td>
                    <td>该API用于处理边缘Flink作业状态上报信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunIefJobActionCallBack</td>
                    <td>该API用于处理IEF Flink作业action回调信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIefMessageChannel</td>
                    <td>该API用于创建IEF消息通道</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">已弃用-SQL作业相关API</td>
                    <td>ListTables</td>
                    <td>该API用于查询指定数据库下符合过滤条件的或所有的表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPartitions</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlSampleTemplates</td>
                    <td>该API用于查询所有SQL样例模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PreviewTable</td>
                    <td>该API用于用于预览表中前10行的内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportTable</td>
                    <td>该API用于将数据从文件导入DLI或OBS表,目前仅支持将OBS上的数据导入DLI或OBS中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportTable</td>
                    <td>该API用于将SQL语句的查询结果导出到OBS对象存储中,只支持导出“QUERY”类型作业的查询结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTableOwner</td>
                    <td>用于修改表的owner。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTable</td>
                    <td>该API用于描述指定表的元数据信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">已弃用-Spark作业-作业相关API</td>
                    <td>ShowSparkJobLog</td>
                    <td>该API用于查询批处理作业的后台日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">已弃用-分组资源相关API</td>
                    <td>UploadPythonFileJobResources</td>
                    <td>该API用于在project下的上传pyfile类型模块。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadFileJobResources</td>
                    <td>该API用于在project下上传file类型模块。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadJobResources</td>
                    <td>该API用于上传分组资源到某个project下。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateJobResourceOwner</td>
                    <td>用于修改程序包的owner。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadJarJobResources</td>
                    <td>该API用于在project下上传jar类型分组资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobResource</td>
                    <td>该API用于查看某个project某个分组下的具体资源信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobResources</td>
                    <td>该API用于查看某个project下的所有资源,其中包含Group。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteJobResource</td>
                    <td>该API用于删除某个project某个分组下的资源包</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">已弃用-委托与权限相关API</td>
                    <td>ListQueueUsers</td>
                    <td>该API用于查询可以使用的指定队列的所有用户名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunDataAuthorizationAction</td>
                    <td>该API用于将数据库或数据表的数据权限赋给指定的其他用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTablePrivileges</td>
                    <td>该API用于查询指定用户在表上的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTableUsers</td>
                    <td>该API用于查看有权访问指定表或表的列的所有用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDliAgency</td>
                    <td>创建DLI委托</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterAuthorizedQueue</td>
                    <td>该API用于与其他用户共享指定的队列,可以给用户赋使用指定的队列的权限或者收回使用权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDliAgency</td>
                    <td>获取dli委托信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">已弃用-跨源连接相关API</td>
                    <td>ShowDatasourceConnection</td>
                    <td>该API用于查询该用户指定的已创建的经典型跨源连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAuthInfo</td>
                    <td>该API用于更新跨源认证信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuthInfo</td>
                    <td>该API用于查询跨源认证信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatasourceConnections</td>
                    <td>该API用于查询该用户已创建的经典型跨源连接列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnhancedConnectionRoutes</td>
                    <td>该API用于创建跨源需要的路由。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAuthInfo</td>
                    <td>该API用于删除跨源认证信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatasourceConnection</td>
                    <td>该API用于创建与其他服务的经典型跨源连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnhancedConnectionRoutes</td>
                    <td>该API用于删除跨源需要的路由。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAuthInfo</td>
                    <td>该API用于创建跨源认证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatasourceConnection</td>
                    <td>该API用于删除已创建的经典型跨源连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">已弃用-队列相关API</td>
                    <td>BatchDeleteQueuePlans</td>
                    <td>该API用于批量删除队列定时扩缩容计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueuePlans</td>
                    <td>查看队列定时扩缩容计划接口,列出指定队列定时规格变更计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateQueueCidr</td>
                    <td>该功能用于修改包年包月队列网段。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteQueuePlan</td>
                    <td>该API用于删除指定ID的队列定时扩缩容计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateQueuePlan</td>
                    <td>该API用于修改指定ID的队列定时扩缩容计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateQueuePlan</td>
                    <td>创建队列定时扩缩容计划接口,对指定的队列创建定时规格变更计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">弹性资源池相关API</td>
                    <td>CreatePeriodElasticResourcePoolSpecChangeOrder</td>
                    <td>包周期弹性资源池规格变更下单接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListElasticResourcePoolScaleRecords</td>
                    <td>查询当前弹性资源池扩缩容历史记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListElasticResourcePools</td>
                    <td>查询所有弹性资源池</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateQueueToElasticResourcePool</td>
                    <td>关联队列到弹性资源池</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteElasticResourcePool</td>
                    <td>删除弹性资源池</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateElasticResourcePoolQueue</td>
                    <td>设置弹性资源池指定队列的扩缩容策略信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePeriodElasticResourcePoolOrder</td>
                    <td>创建包周期弹性资源池</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateElasticResourcePool</td>
                    <td>创建弹性资源池</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateElasticResourcePool</td>
                    <td>修改弹性资源池信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListElasticResourcePoolQueues</td>
                    <td>查询弹性资源池所属队列</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">数据库权限管理</td>
                    <td>ListDatabaseUsers</td>
                    <td>查询所有数据库用户/角色。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">数据目录相关API</td>
                    <td>ShowCatalog</td>
                    <td>该API用于描述DLI catalog详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCatalogs</td>
                    <td>该API获取指定项目下所有catalog信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunCatalogAction</td>
                    <td>该API创建DLI绑定/解绑到lakeformation等服务的元数据目录(CATALOG)相关信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">权限相关API</td>
                    <td>RunAuthorizationAction</td>
                    <td>该API用于将DLI资源权限赋给、回收、更新指定的其他用户或项目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuthorizationPrivileges</td>
                    <td>获取对象赋权用户的权限信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">管理数据库和用户(MySQL)</td>
                    <td>DeleteDatabase</td>
                    <td>删除数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabase</td>
                    <td>创建数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabases</td>
                    <td>查询数据库列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">管理数据库和用户(PostgreSQL)</td>
                    <td>UpdateDatabaseOwner</td>
                    <td>修改数据库owner</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">表接口</td>
                    <td>DeleteTable</td>
                    <td>删除指定表及所有kv文档,表标记为删除后,空间不会立刻释放,并发的读写访问仍需继续完成。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资源标签相关API</td>
                    <td>ListResourcesTags</td>
                    <td>查询指定资源类型的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowQuota</td>
                    <td>查询单租户在VPC服务下的网络资源配额,包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额,vpn配额等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">队列相关API</td>
                    <td>CreateQueueProperty</td>
                    <td>该接口用于增加队列属性, 一次可增加多个属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConnectivityTask</td>
                    <td>该API用于在连通性测试提交后查询连通性结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteQueue</td>
                    <td>该API用于删除指定队列。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueues</td>
                    <td>该API用于列出该project下所有的队列。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateQueueProperty</td>
                    <td>更新队列属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateQueue</td>
                    <td>该API用于创建队列,该队列将会绑定用户指定的计算资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowQueue</td>
                    <td>该API用于列出该project下指定的队列详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueueProperties</td>
                    <td>获取队列配置的属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunQueueAction</td>
                    <td>该功能用于重新启动队列、扩容队列、缩容队列。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnectivityTask</td>
                    <td>创建地址连通性请求API接口,往指定集群发送地址连通性测试请求,并将测试地址插入表内</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteQueueProperty</td>
                    <td>该接口用于删除队列的属性,一次可删除多个属性值。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
