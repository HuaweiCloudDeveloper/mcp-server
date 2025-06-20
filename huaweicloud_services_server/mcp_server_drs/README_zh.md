# DRS MCP Server 

## 版本信息
v0.1.0

## 产品描述

DRS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DRS交互的能力。可以基于自然语言对DRS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 企业项目管理 | ShowEnterpriseProject | 查询企业项目列表。 | To be tested |
| 公共接口管理 | ListDataCompareDetail | 查询行数对比详情。 | To be tested |
|  | BatchShowParams | 在进行数据库迁移时,为了确保迁移成功后业务应用的使用不受影响,数据复制服务提供了参数对比功能帮助您进行源库和目标库参数一致性对比,此接口可以获取源库和目标库的数据库参数。 | To be tested |
|  | ListContentCompareDifference | 查询内容对比差异。 | To be tested |
|  | BatchUpdateJob | 批量修改任务名称或描述,设置异常通知信息。 | To be tested |
|  | BatchSetSpeed | 批量设置任务限速,任务创建成功后默认不限速。 | To be tested |
|  | BatchSetObjects | 迁移之前,选择需要迁移的数据库或者表。 | To be tested |
|  | BatchListJobDetails | 根据任务ID批量查询任务详情。 | To be tested |
|  | BatchStopJobs | 批量暂停任务。 | To be tested |
|  | StartPromptlyDataLevelTableCompareJob | 立即启动数据级表对比任务。 | To be tested |
|  | CreateDataLevelTableCompareJob | 创建数据级表对比任务。 | To be tested |
|  | BatchSetDefiner | 批量设置Definer迁移是否迁移到到该用户下。 | To be tested |
|  | ListObejectLevelCompareDetail | 查询对象对比任务详情。 | To be tested |
|  | CreateCompareResultFile | 导出对比任务结果文件。 | To be tested |
|  | ListAvailableZone | 查询规格未售罄的可用区 | To be tested |
|  | DownloadCompareResultFile | 下载对比任务结果文件。 | To be tested |
|  | BatchCheckJobs | 批量预检查,校验是否可进行迁移。 | To be tested |
|  | ListDataLevelTableCompareJobs | 查询数据级表对比任务列表。 | To be tested |
|  | BatchDeleteJobs | 批量结束任务或删除实时迁移、实时同步、实时灾备任务。 | To be tested |
|  | ListDataCompareOverview | 查询行数对比总览。 | To be tested |
|  | ListCompareResult | 查询对比结果。 | To be tested |
|  | ListAvailableNodeTypes | 查询可用的Node规格。 | To be tested |
|  | BatchValidateClustersConnections | - 批量测试连接(集群模式)。 | To be tested |
|  | ShowJobList | 查询租户任务列表,可以根据引擎类型,网络类型,任务状态,任务名称,任务ID进行查询。 | To be tested |
|  | BatchListProgresses | 根据任务ID批量查询全量进度、增量时延信息。 | To be tested |
|  | BatchValidateConnections | 批量测试连接。 | To be tested |
|  | BatchCreateJobs | 根据请求参数不同,可以批量创建实时迁移、实时同步、实时灾备任务。 | To be tested |
|  | UpdateParams | 修改数据库参数。 | To be tested |
|  | ListObejectLevelCompareOverview | 查询对象对比任务概览。 | To be tested |
|  | ListContentCompareOverview | 查询内容对比总览。 | To be tested |
|  | BatchListJobStatus | 根据任务ID批量查询任务状态。 | To be tested |
|  | BatchSetSmn | 批量设置异常通知,已结束的任务不支持设置。 | To be tested |
|  | CreateObjectLevelCompareJob | 创建对象级对比任务。 | To be tested |
|  | BatchStartJobs | 批量启动实时迁移、同步、灾备任务。 | To be tested |
|  | DeleteCompareJob | 取消对比任务。 | To be tested |
|  | CreateCompareTask | 创建对比任务。 | To be tested |
|  | BatchRestoreTask | 在迁移过程中由于不确定因素导致迁移任务失败,可通过重试功能,重新提交迁移任务。 | To be tested |
|  | BatchCheckResults | 批量查询任务的预检查结果。 | To be tested |
|  | ListContentCompareDetail | 查询内容对比详情 | To be tested |
|  | BatchResetPassword | 任务启动之后需要修改源库/目标库密码时调用此接口。 | To be tested |
| 参数管理 | ListJobParameters | 查询任务的参数配置列表信息 | To be tested |
|  | UpdateJobConfigurations | 更新任务的参数信息。 | To be tested |
|  | ListJobHistoryParameters | 查询任务的参数配置修改历史 | To be tested |
| 备份迁移 | CreateReplicationJob | 该接口主要用于三种常见场景下备份迁移任务的配置。 | To be tested |
|  | UpdateReplicationJob | 修改指定备份迁移任务信息,任务名与任务描述。 | To be tested |
|  | ListReplicationJobs | 获取当前备份迁移任务列表,不包含已删除的任务。 | To be tested |
|  | ShowReplicationJob | 获取指定备份迁移任务详细信息。 | To be tested |
|  | DeleteReplicationJob | 对于已经完成的备份迁移任务,可以选择删除迁移任务。 | To be tested |
| 实例操作 | BatchStopJobsAction | 批量结束租户指定ID任务。 | To be tested |
|  | DeleteUserJdbcDriver | 删除驱动文件。 | To be tested |
|  | ShowPositionResult | 获取查询数据库位点的结果 | To be tested |
|  | ValidateJobName | 创建任务时对任务名称进行校验。 | To be tested |
|  | ExecuteJobAction | 操作租户指定ID任务。 | To be tested |
|  | BatchExecuteJobActions | 批量操作租户指定ID任务。 | To be tested |
|  | UploadJdbcDriver | 上传驱动文件。 | To be tested |
|  | StopJobAction | 结束租户指定ID任务。 | To be tested |
|  | ListJdbcDrivers | 查询驱动文件列表。 | To be tested |
|  | DeleteJdbcDriver | 删除驱动文件。 | To be tested |
|  | CollectPositionAsync | 采集数据库位点信息。 | To be tested |
|  | ShowActions | 获取指定任务允许、不允许、当前操作信息。 | To be tested |
|  | UploadUserJdbcDriver | 上传驱动文件。 | To be tested |
|  | UpdateStartPosition | 更新增量任务的启动位点。 | To be tested |
|  | ListUserJdbcDrivers | 查询驱动文件列表。 | To be tested |
|  | SyncJdbcDriver | 同步驱动文件。 | To be tested |
|  | SyncUserJdbcDriver | 同步驱动文件。 | To be tested |
| 实例数据库对象配置 | CollectDbObjectsInfo | 提交查询数据库对象信息。例如: | To be tested |
|  | ListDbObjects | 查询数据库对象信息。 | To be tested |
|  | ShowDbObjectTemplateProgress | 对象选择(文件导入 - 进度查询)。 | To be tested |
|  | CollectDbObjectsAsync | 提交查询数据库对象信息。例如: | To be tested |
|  | ShowObjectMapping | 查询实时同步映射关系包括对象选择时的库映射、schema映射、表映射和数据加工时的列映射。 | To be tested |
|  | ShowDbObjectTemplateResult | 对象选择(文件导入 - 获取导入结果)。 | To be tested |
|  | ShowDbObjectCollectionStatus | 获取提交查询数据库对象信息的结果。 | To be tested |
|  | ShowUpdateObjectSavingStatus | 获取对象保存进度。 | To be tested |
|  | ShowDbObjectsList | 查询数据库对象信息。 | To be tested |
|  | UploadDbObjectTemplate | 对象选择(文件导入 - 模板上传)。 | To be tested |
|  | ShowSupportObjectType | 查询任务支持的对象选择类型、列映射、支持搜索的对象类型等信息。 | To be tested |
|  | DownloadDbObjectTemplate | 对象选择(文件导入 - 模板下载)。 | To be tested |
| 实例管理 | CreateJob | 创建单个任务,根据请求参数不同,可以创建单个实时迁移、实时同步、实时灾备等任务。 | To be tested |
|  | ChangeToPeriod | DRS同步和灾备任务按需计费转包周期计费。 | To be tested |
|  | UpdateJob | 更新租户指定ID任务详情。 | To be tested |
|  | CopyJob | DRS支持通过克隆功能,快速复制现有同步任务的配置。 | To be tested |
|  | ListJobs | 查询租户任务列表,可以根据企业项目,引擎类型,网络类型,任务状态,任务名称,任务ID进行查询。 | To be tested |
|  | BatchDeleteJobsById | 批量删除租户指定ID任务。 | To be tested |
|  | DeleteJob | 删除租户指定ID任务。 | To be tested |
| 实例详情 | ShowIncrementComponentsDetail | 查询任务同步的增量组件的详细信息,实时同步任务,任务模式为增量或者全量+增量才支持。具体介绍可以参考:[查询同步进度](https://support.huaweicloud.com/realtimesyn-drs/drs_10_0007.html) | To be tested |
|  | ShowMonitorData | 获取任务监控数据。 | To be tested |
|  | ShowJobDetail | 查询任务详情。 | To be tested |
|  | ShowDirtyData | 查询异常数据列表。 | To be tested |
|  | ShowMetering | 获取询价接口的参数。 | To be tested |
|  | ShowTimeline | 指定不同的任务ID可以展示当前任务创建时间、启动时间、重试、重置等操作的时间轴信息。 | To be tested |
|  | ExportOperationInfo | 导出指定任务操作统计信息。 | To be tested |
| 实时同步管理 | BatchSetPolicy | - 批量设置同步策略,包括冲突策略、过滤DROP Datase、对象同步范围。 | To be tested |
|  | UpdateTuningParams | 修改调优参数的值。 | To be tested |
|  | BatchChangeData | 数据复制服务支持对同步的对象进行加工,即可以为选择的对象添加规则。 | To be tested |
| 实时灾备管理 | BatchListStructProcess | 根据任务ID批量查询灾备初始化进度,虚拟id不支持查询。 | To be tested |
|  | BatchListRposAndRtos | 批量查询RPO和RTO。 | To be tested |
|  | ShowMonitoringData | 根据任务ID查询容灾监控数据。 | To be tested |
|  | BatchListStructDetail | 根据任务ID批量查询灾备初始化对象详情。 | To be tested |
|  | BatchSwitchover | 批量主备倒换。 | To be tested |
| 实时迁移管理 | ListUsers | 数据库的迁移过程中,迁移用户需要进行单独处理,该接口可以查询源库的用户信息。 | To be tested |
|  | BatchUpdateUser | 数据库的迁移过程中,迁移用户需要进行单独处理,该接口可以批量设置需要迁移的用户和角色。 | To be tested |
| 对比管理 | ShowComparePolicy | 查询对比策略。 | To be tested |
|  | ShowHealthCompareJobDetail | 查询健康对比任务详情。 | To be tested |
|  | UpdateComparePolicy | 修改周期性对比的对比策略,目前仅MySQL->MySQL、MySQL->GaussDB(for MySQL)、MySQL->GaussDB(DWS)、GaussDB(for MySQL)->MySQL同步任务,MySQL->MySQL、MySQL->GaussDB(for MySQL)迁移任务,MySQL->MySQL、MySQL->GaussDB(for MySQL)、GaussDB(for MySQL)->GaussDB(for MySQL)、DDM->DDM、DDS-DDS灾备任务支持对比策略设置。 | To be tested |
|  | ShowProgressData | 查询不同迁移对象类型的迁移进度。 | To be tested |
|  | ShowHealthObjectCompareJobOverview | 获取健康对比对象级对比概览。 | To be tested |
|  | ShowHealthCompareJobList | 查询健康对比列表。 | To be tested |
| 录制回放 | ShowReplayResults | 获取录制回放结果数据,包括:回放基于时间维度统计信息,异常SQL及统计结果、慢SQL及统计结果 | To be tested |
| 批量异步实例管理 | ImportBatchCreateJobs | 批量导入任务 | To be tested |
|  | CommitAsyncJob | 提交批量创建异步任务,当批量异步任务创建或更新参数后,系统会自动开始进行参数校验,待所有任务成功完成参数校验后并且无报错时,可调用此接口开始创建DRS任务实例。 | To be tested |
|  | UpdateBatchAsyncJobs | 更新租户指定ID批量异步任务详情。 | To be tested |
|  | BatchCreateJobsAsync | 批量异步创建任务,根据请求参数不同,可以批量异步创建实时迁移、实时同步、实时灾备等任务。 | To be tested |
|  | ListAsyncJobs | 查询租户批量异步创建的任务列表。 | To be tested |
|  | DownloadBatchCreateTemplate | 下载批量导入任务模板 | To be tested |
|  | ListAsyncJobDetail | 查询租户指定ID批量异步任务详情,默认为任务的“create_time”降序排序获取结果,支持分页查询。 | To be tested |
| 数据加工 | ShowDataFilteringResult | 获取数据过滤校验结果 | To be tested |
|  | CollectColumns | 采集指定数据库表的列信息 | To be tested |
|  | ShowDataProcessingRulesResult | 获取指定任务数据加工规则更新结果 | To be tested |
|  | ShowColumnInfoResult | 获取指定数据库表列信息 | To be tested |
|  | CheckDataFilter | 数据过滤规则校验 | To be tested |
|  | UpdateDataProgress | 更新指定任务数据加工规则 | To be tested |
|  | ShowDataProgress | 查询数据加工规则:包含数据库表的映射信息、列信息、数据过滤信息、附加列信息、DDL以及DML信息 | To be tested |
| 权限管理 | UpdateAgencyPolicy | 更新委托权限策略 | To be tested |
|  | ShowAgencyInfo | 查询委托权限详情 | To be tested |
|  | ListsAgencyPermissions | 根据源库类型,目标库类型,是否自建,获取委托所需要的权限 | To be tested |
| 标签管理 | ListProjectTags | 查询指定project ID下不同任务类型的所有标签集合。 | To be tested |
|  | BatchCreateTags | 批量添加资源标签。 | To be tested |
|  | ListTags | 查询租户在指定Project中实例类型的所有资源标签集合。 | To be tested |
|  | CountInstanceByTags | 查询资源实例数量。 | To be tested |
|  | ShowInstanceTags | 查询指定实例的标签信息。 | To be tested |
|  | BatchDeleteTags | 为指定实例批量删除标签。 | To be tested |
|  | ListInstanceTags | 查询指定实例的标签信息。 | To be tested |
|  | ListInstanceByTags | 查询资源实例列表。 | To be tested |
|  | BatchTagAction | 批量添加删除资源标签。 | To be tested |
| 资源管理 | ListLinks | 根据参数不同,可查询实时迁移、实时同步、实时灾备等可用链路信息。 | To be tested |
|  | ListFeatures | 根据参数不同,可查询所有特性开关的状态。 | To be tested |
| 连接管理 | ModifyConnection | 修改创建的连接信息。 | To be tested |
|  | ListConnections | 查询连接列表,可根据连接类型进行查询。 | To be tested |
|  | CreateConnection | 创建单个连接,该连接可以为线下自建库或云上RDS等,目前支持的数据库引擎包括MySQL、PostgreSQL、Oracle和MongoDB。 | To be tested |
|  | DeleteConnection | 删除租户指定的连接。 | To be tested |
| 配置管理 | ListJobDdls | 查询增量DDL列表,可根据status查询 | To be tested |
|  | CleanAlarms | 清除DDL告警 | To be tested |
| 配额 | ShowQuotas | 查询单租户在某一项目下DRS服务下的配额信息。 | To be tested |
