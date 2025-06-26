# DRS MCP Server 


## Version
v0.1.0

## Overview

DRS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DRS. Full-chain management of DRS resources can be carried out based on natural language.

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
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>查询租户在指定项目中指定资源类型下的所有标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">任务中心API</td>
                    <td>ListJobs</td>
                    <td>查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务,该API用于查询这些任务的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">任务管理</td>
                    <td>ShowJobDetail</td>
                    <td>查询job的执行状态。 可用于查询SFS Turbo异步API的执行状态。例如:可使用调用创建并绑定ldap配置接口时返回的jobId,通过该接口查询job的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">企业项目管理操作</td>
                    <td>ShowEnterpriseProject</td>
                    <td>查询企业项目详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">作业管理接口</td>
                    <td>BatchDeleteJobs</td>
                    <td>在MRS集群中批量删除作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="38">公共接口管理</td>
                    <td>ListDataCompareDetail</td>
                    <td>查询行数对比详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowParams</td>
                    <td>在进行数据库迁移时,为了确保迁移成功后业务应用的使用不受影响,数据复制服务提供了参数对比功能帮助您进行源库和目标库参数一致性对比,此接口可以获取源库和目标库的数据库参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContentCompareDifference</td>
                    <td>查询内容对比差异。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateJob</td>
                    <td>批量修改任务名称或描述,设置异常通知信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetSpeed</td>
                    <td>批量设置任务限速,任务创建成功后默认不限速。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetObjects</td>
                    <td>迁移之前,选择需要迁移的数据库或者表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListJobDetails</td>
                    <td>根据任务ID批量查询任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopJobs</td>
                    <td>批量暂停任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartPromptlyDataLevelTableCompareJob</td>
                    <td>立即启动数据级表对比任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataLevelTableCompareJob</td>
                    <td>创建数据级表对比任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetDefiner</td>
                    <td>批量设置Definer迁移是否迁移到到该用户下。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListObejectLevelCompareDetail</td>
                    <td>查询对象对比任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCompareResultFile</td>
                    <td>导出对比任务结果文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableZone</td>
                    <td>查询规格未售罄的可用区</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadCompareResultFile</td>
                    <td>下载对比任务结果文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCheckJobs</td>
                    <td>批量预检查,校验是否可进行迁移。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataLevelTableCompareJobs</td>
                    <td>查询数据级表对比任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataCompareOverview</td>
                    <td>查询行数对比总览。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCompareResult</td>
                    <td>查询对比结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableNodeTypes</td>
                    <td>查询可用的Node规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchValidateClustersConnections</td>
                    <td>- 批量测试连接(集群模式)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobList</td>
                    <td>查询租户任务列表,可以根据引擎类型,网络类型,任务状态,任务名称,任务ID进行查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListProgresses</td>
                    <td>根据任务ID批量查询全量进度、增量时延信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchValidateConnections</td>
                    <td>批量测试连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateJobs</td>
                    <td>根据请求参数不同,可以批量创建实时迁移、实时同步、实时灾备任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateParams</td>
                    <td>修改数据库参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListObejectLevelCompareOverview</td>
                    <td>查询对象对比任务概览。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContentCompareOverview</td>
                    <td>查询内容对比总览。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListJobStatus</td>
                    <td>根据任务ID批量查询任务状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetSmn</td>
                    <td>批量设置异常通知,已结束的任务不支持设置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateObjectLevelCompareJob</td>
                    <td>创建对象级对比任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartJobs</td>
                    <td>批量启动实时迁移、同步、灾备任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCompareJob</td>
                    <td>取消对比任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCompareTask</td>
                    <td>创建对比任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRestoreTask</td>
                    <td>在迁移过程中由于不确定因素导致迁移任务失败,可通过重试功能,重新提交迁移任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCheckResults</td>
                    <td>批量查询任务的预检查结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListContentCompareDetail</td>
                    <td>查询内容对比详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchResetPassword</td>
                    <td>任务启动之后需要修改源库/目标库密码时调用此接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">参数管理</td>
                    <td>ListJobParameters</td>
                    <td>查询任务的参数配置列表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateJobConfigurations</td>
                    <td>更新任务的参数信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobHistoryParameters</td>
                    <td>查询任务的参数配置修改历史</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">备份迁移</td>
                    <td>CreateReplicationJob</td>
                    <td>该接口主要用于三种常见场景下备份迁移任务的配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateReplicationJob</td>
                    <td>修改指定备份迁移任务信息,任务名与任务描述。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReplicationJobs</td>
                    <td>获取当前备份迁移任务列表,不包含已删除的任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReplicationJob</td>
                    <td>获取指定备份迁移任务详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteReplicationJob</td>
                    <td>对于已经完成的备份迁移任务,可以选择删除迁移任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">实例操作</td>
                    <td>BatchStopJobsAction</td>
                    <td>批量结束租户指定ID任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUserJdbcDriver</td>
                    <td>删除驱动文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPositionResult</td>
                    <td>获取查询数据库位点的结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateJobName</td>
                    <td>创建任务时对任务名称进行校验。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteJobAction</td>
                    <td>操作租户指定ID任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchExecuteJobActions</td>
                    <td>批量操作租户指定ID任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadJdbcDriver</td>
                    <td>上传驱动文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopJobAction</td>
                    <td>结束租户指定ID任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJdbcDrivers</td>
                    <td>查询驱动文件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteJdbcDriver</td>
                    <td>删除驱动文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectPositionAsync</td>
                    <td>采集数据库位点信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowActions</td>
                    <td>获取指定任务允许、不允许、当前操作信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadUserJdbcDriver</td>
                    <td>上传驱动文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStartPosition</td>
                    <td>更新增量任务的启动位点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserJdbcDrivers</td>
                    <td>查询驱动文件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncJdbcDriver</td>
                    <td>同步驱动文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncUserJdbcDriver</td>
                    <td>同步驱动文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">实例数据库对象配置</td>
                    <td>CollectDbObjectsInfo</td>
                    <td>提交查询数据库对象信息。例如:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbObjects</td>
                    <td>查询数据库对象信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDbObjectTemplateProgress</td>
                    <td>对象选择(文件导入 - 进度查询)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectDbObjectsAsync</td>
                    <td>提交查询数据库对象信息。例如:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowObjectMapping</td>
                    <td>查询实时同步映射关系包括对象选择时的库映射、schema映射、表映射和数据加工时的列映射。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDbObjectTemplateResult</td>
                    <td>对象选择(文件导入 - 获取导入结果)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDbObjectCollectionStatus</td>
                    <td>获取提交查询数据库对象信息的结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpdateObjectSavingStatus</td>
                    <td>获取对象保存进度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDbObjectsList</td>
                    <td>查询数据库对象信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadDbObjectTemplate</td>
                    <td>对象选择(文件导入 - 模板上传)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSupportObjectType</td>
                    <td>查询任务支持的对象选择类型、列映射、支持搜索的对象类型等信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadDbObjectTemplate</td>
                    <td>对象选择(文件导入 - 模板下载)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">实例管理</td>
                    <td>CreateJob</td>
                    <td>创建单个任务,根据请求参数不同,可以创建单个实时迁移、实时同步、实时灾备等任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeToPeriod</td>
                    <td>DRS同步和灾备任务按需计费转包周期计费。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateJob</td>
                    <td>更新租户指定ID任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyJob</td>
                    <td>DRS支持通过克隆功能,快速复制现有同步任务的配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFeatures</td>
                    <td>查询当前实例高级特性列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteJobsById</td>
                    <td>批量删除租户指定ID任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">实例详情</td>
                    <td>ShowIncrementComponentsDetail</td>
                    <td>查询任务同步的增量组件的详细信息,实时同步任务,任务模式为增量或者全量+增量才支持。具体介绍可以参考:[查询同步进度](https://support.huaweicloud.com/realtimesyn-drs/drs_10_0007.html)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonitorData</td>
                    <td>获取任务监控数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDirtyData</td>
                    <td>查询异常数据列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetering</td>
                    <td>获取询价接口的参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTimeline</td>
                    <td>指定不同的任务ID可以展示当前任务创建时间、启动时间、重试、重置等操作的时间轴信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportOperationInfo</td>
                    <td>导出指定任务操作统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">实时同步管理</td>
                    <td>BatchSetPolicy</td>
                    <td>- 批量设置同步策略,包括冲突策略、过滤DROP Datase、对象同步范围。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTuningParams</td>
                    <td>修改调优参数的值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchChangeData</td>
                    <td>数据复制服务支持对同步的对象进行加工,即可以为选择的对象添加规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">实时灾备管理</td>
                    <td>BatchListStructProcess</td>
                    <td>根据任务ID批量查询灾备初始化进度,虚拟id不支持查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListRposAndRtos</td>
                    <td>批量查询RPO和RTO。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonitoringData</td>
                    <td>根据任务ID查询容灾监控数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListStructDetail</td>
                    <td>根据任务ID批量查询灾备初始化对象详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSwitchover</td>
                    <td>批量主备倒换。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">实时迁移管理</td>
                    <td>BatchUpdateUser</td>
                    <td>数据库的迁移过程中,迁移用户需要进行单独处理,该接口可以批量设置需要迁移的用户和角色。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">对比管理</td>
                    <td>ShowComparePolicy</td>
                    <td>查询对比策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHealthCompareJobDetail</td>
                    <td>查询健康对比任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateComparePolicy</td>
                    <td>修改周期性对比的对比策略,目前仅MySQL-&gt;MySQL、MySQL-&gt;GaussDB(for MySQL)、MySQL-&gt;GaussDB(DWS)、GaussDB(for MySQL)-&gt;MySQL同步任务,MySQL-&gt;MySQL、MySQL-&gt;GaussDB(for MySQL)迁移任务,MySQL-&gt;MySQL、MySQL-&gt;GaussDB(for MySQL)、GaussDB(for MySQL)-&gt;GaussDB(for MySQL)、DDM-&gt;DDM、DDS-DDS灾备任务支持对比策略设置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProgressData</td>
                    <td>查询不同迁移对象类型的迁移进度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHealthObjectCompareJobOverview</td>
                    <td>获取健康对比对象级对比概览。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHealthCompareJobList</td>
                    <td>查询健康对比列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">录制回放</td>
                    <td>ShowReplayResults</td>
                    <td>获取录制回放结果数据,包括:回放基于时间维度统计信息,异常SQL及统计结果、慢SQL及统计结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">批量异步实例管理</td>
                    <td>ImportBatchCreateJobs</td>
                    <td>批量导入任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CommitAsyncJob</td>
                    <td>提交批量创建异步任务,当批量异步任务创建或更新参数后,系统会自动开始进行参数校验,待所有任务成功完成参数校验后并且无报错时,可调用此接口开始创建DRS任务实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBatchAsyncJobs</td>
                    <td>更新租户指定ID批量异步任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateJobsAsync</td>
                    <td>批量异步创建任务,根据请求参数不同,可以批量异步创建实时迁移、实时同步、实时灾备等任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAsyncJobs</td>
                    <td>查询租户批量异步创建的任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadBatchCreateTemplate</td>
                    <td>下载批量导入任务模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAsyncJobDetail</td>
                    <td>查询租户指定ID批量异步任务详情,默认为任务的“create_time”降序排序获取结果,支持分页查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">数据加工</td>
                    <td>ShowDataFilteringResult</td>
                    <td>获取数据过滤校验结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectColumns</td>
                    <td>采集指定数据库表的列信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataProcessingRulesResult</td>
                    <td>获取指定任务数据加工规则更新结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowColumnInfoResult</td>
                    <td>获取指定数据库表列信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckDataFilter</td>
                    <td>数据过滤规则校验</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataProgress</td>
                    <td>更新指定任务数据加工规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataProgress</td>
                    <td>查询数据加工规则:包含数据库表的映射信息、列信息、数据过滤信息、附加列信息、DDL以及DML信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">权限管理</td>
                    <td>UpdateAgencyPolicy</td>
                    <td>更新委托权限策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgencyInfo</td>
                    <td>查询委托权限详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListsAgencyPermissions</td>
                    <td>根据源库类型,目标库类型,是否自建,获取委托所需要的权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">标签管理</td>
                    <td>BatchCreateTags</td>
                    <td>批量创建标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountInstanceByTags</td>
                    <td>查询资源实例数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceTags</td>
                    <td>查询指定实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTags</td>
                    <td>为指定保护实例批量删除标签。一个资源上最多有10个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceTags</td>
                    <td>查询实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceByTags</td>
                    <td>查询资源实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchTagAction</td>
                    <td>批量添加删除资源标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">目标连接管理</td>
                    <td>ListConnections</td>
                    <td>查询目标连接列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnection</td>
                    <td>创建目标连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnection</td>
                    <td>删除目标连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资产管理</td>
                    <td>ListUsers</td>
                    <td>查询账号的服务器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资源管理</td>
                    <td>ListLinks</td>
                    <td>根据参数不同,可查询实时迁移、实时同步、实时灾备等可用链路信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">连接管理</td>
                    <td>ModifyConnection</td>
                    <td>修改创建的连接信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">配置管理</td>
                    <td>ListJobDdls</td>
                    <td>查询增量DDL列表,可根据status查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CleanAlarms</td>
                    <td>清除DDL告警</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowQuotas</td>
                    <td>查询当前项目下资源配额情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像标签</td>
                    <td>ListTags</td>
                    <td>根据不同条件查询镜像标签列表信息。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
