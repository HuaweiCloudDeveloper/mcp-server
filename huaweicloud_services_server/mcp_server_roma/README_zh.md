# ROMA MCP Server 

## 版本信息
v0.1.0

## 产品描述

ROMA MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务ROMA交互的能力。可以基于自然语言对ROMA资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| ACL策略管理 | UpdateAclStrategyV2 | 修改指定的ACL策略,其中可修改的属性为:acl_name、acl_type、acl_value,其它属性不可修改。 | To be tested |
|  | DeleteAclV2 | 删除指定的ACL策略, 如果存在api与该ACL策略的绑定关系,则无法删除 | To be tested |
|  | CreateAclStrategyV2 | 增加一个ACL策略,策略类型通过字段acl_type来确定(permit或者deny),限制的对象的类型可以为IP或者DOMAIN,这里的DOMAIN对应的acl_value的值为租户名称,而非“www.exampleDomain.com"之类的网络域名。 | To be tested |
|  | BatchDeleteAclV2 | 批量删除指定的多个ACL策略。 | To be tested |
|  | ShowDetailsOfAclPolicyV2 | 查询指定ACL策略的详情。 | To be tested |
|  | ListAclStrategiesV2 | 查询所有的ACL策略列表。 | To be tested |
| API分组管理 | ShowDetailsOfApiGroupV2 | 查询指定分组的详细信息。 | To be tested |
|  | DeleteApiGroupV2 | 删除指定的API分组。 | To be tested |
|  | CheckApiGroupsV2 | 校验API分组名称是否存在。 | To be tested |
|  | UpdateApiGroupV2 | 修改API分组属性。其中name和remark可修改,其他属性不可修改。 | To be tested |
|  | CreateApiGroupV2 | API分组是API的管理单元,一个API分组等同于一个服务入口,创建API分组时,返回一个子域名作为访问入口。建议一个API分组下的API具有一定的相关性。 | To be tested |
|  | ListApiGroupsV2 | 查询API分组列表。 | To be tested |
| API管理 | DeleteApiV2 | 删除指定的API。 | To be tested |
|  | ListApisV2 | 查看API列表,返回API详细信息、发布信息等,但不能查看到后端服务信息。 | To be tested |
|  | CreateOrDeletePublishRecordForApiV2 | 对API进行发布或下线。 | To be tested |
|  | ListApiVersionDetailV2 | 查询某个指定的版本详情。 | To be tested |
|  | ChangeApiVersionV2 | API每次发布时,会基于当前的API定义生成一个版本。版本记录了API发布时的各种定义及状态。 | To be tested |
|  | ListApiVersionsV2 | 查询某个API的历史版本。每个API在一个环境上最多存在10个历史版本。 | To be tested |
|  | DebugApiV2 | 调试一个API在指定运行环境下的定义,接口调用者需要具有操作该API的权限。 | To be tested |
|  | BatchPublishOrOfflineApiV2 | 将多个API发布到一个指定的环境,或将多个API从指定的环境下线。 | To be tested |
|  | ShowDetailsOfApiV2 | 查看指定的API的详细信息。 | To be tested |
|  | ListApiRuntimeDefinitionV2 | 查看指定的API在指定的环境上的运行时定义,默认查询RELEASE环境上的运行时定义。 | To be tested |
|  | UpdateApiV2 | 修改指定API的信息,包括后端服务信息。 | To be tested |
|  | CheckApisV2 | 校验API定义。校验API的路径或名称是否已存在 | To be tested |
|  | CreateApiV2 | 添加一个API,API即一个服务接口,具体的服务能力。 | To be tested |
|  | DeleteApiByVersionIdV2 | 对某个生效中的API版本进行下线操作,下线后,API在该版本生效的环境中将不再能够被调用。 | To be tested |
| API绑定ACL策略 | CreateApiAclBindingV2 | 将API与ACL策略进行绑定。 | To be tested |
|  | DeleteApiAclBindingV2 | 解除某条API与ACL策略的绑定关系 | To be tested |
|  | BatchDeleteApiAclBindingV2 | 批量解除API与ACL策略的绑定 | To be tested |
|  | ListApisUnbindedToAclPolicyV2 | 查看ACL策略未绑定的API列表,需要API已发布 | To be tested |
|  | ListApisBindedToAclPolicyV2 | 查看ACL策略绑定的API列表 | To be tested |
|  | ListAclPolicyBindedToApiV2 | 查看API绑定的ACL策略列表 | To be tested |
| API绑定流控策略 | DisassociateRequestThrottlingPolicyV2 | 解除API与流控策略的绑定关系。 | To be tested |
|  | ListRequestThrottlingPoliciesBindedToApiV2 | 查询某个API绑定的流控策略列表。每个环境上应该最多只有一个流控策略。 | To be tested |
|  | AssociateRequestThrottlingPolicyV2 | 将流控策略应用于API,则所有对该API的访问将会受到该流控策略的限制。 | To be tested |
|  | ListApisUnbindedToRequestThrottlingPolicyV2 | 查询所有未绑定到该流控策略上的自有API列表。需要API已经发布,未发布的API不予展示。 | To be tested |
|  | BatchDisassociateThrottlingPolicyV2 | 批量解除API与流控策略的绑定关系 | To be tested |
|  | ListApisBindedToRequestThrottlingPolicyV2 | 查询某个流控策略上已经绑定的API列表。 | To be tested |
| APPLICATION_MANAGEMENT | CheckRomaAppDetails | 查询应用详情 | To be tested |
|  | AddUserToApp | - 设置应用的用户成员,为空数组时会清空已有应用成员列表 | To be tested |
|  | ListRomaApp | 查询应用列表,支持条件查询,所有条件是并且的关系 | To be tested |
|  | ResetRomaAppSecret | 重置应用密钥 | To be tested |
|  | DeleteRomaApp | 删除单个应用 | To be tested |
|  | CheckCanAuthUsersOfApp | 查询应用的候选用户成员列表,会过滤掉异常状态用户 | To be tested |
|  | CreateRomaApp | 创建应用 | To be tested |
|  | ValidateRomaApp | 校验指定条件的应用是否存在 | To be tested |
|  | UpdateRomaApp | 更新应用 | To be tested |
|  | CheckRomaAppSecret | 查询应用密钥 | To be tested |
|  | CheckAuthUsersOfApp | 查询用户成列表 | To be tested |
| APP授权管理 | ListDuplicateApisForAppV2 | 查询指定APP下路径冲突的api列表。 | To be tested |
|  | CancelingAuthorizationV2 | 解除API对APP的授权关系。解除授权后,APP将不再能够调用该API。 | To be tested |
|  | ListApisUnbindedToAppV2 | 查询指定环境上某个APP未绑定的API列表,包括自有API和从云市场购买的API。 | To be tested |
|  | ListAppsBindedToApiV2 | 查询API绑定的APP列表。 | To be tested |
|  | CreateAuthorizingAppsV2 | APP创建成功后,还不能访问API,如果想要访问某个环境上的API,需要将该API在该环境上授权给APP。授权成功后,APP即可访问该环境上的这个API。 | To be tested |
|  | ListApisBindedToAppV2 | 查询APP已经绑定的API列表。 | To be tested |
| ASSET_MANAGEMENT | CheckAssetJobStatus | 查询作业进度 | To be tested |
|  | DeleteAsset | 批量删除资产 | To be tested |
|  | ImportAsset | - 创建导入资产作业任务,资产版本和具体哪些资产从资产内容里读取 | To be tested |
|  | ExportAsset | 批量导出资产 | To be tested |
|  | DownloadAssetArchive | - 导出作业执行成功后,通过该接口获取导出作业产生的资产包,仅能下载一次 | To be tested |
| DICTIONARY_MANAGEMENT | UpdateDictionary | 更新字典 | To be tested |
|  | CreateDictionary | 创建字典 | To be tested |
|  | DeleteDictionary | 删除单个字典,会同时删除该字典的所有子字典 | To be tested |
|  | CheckDictionary | 查询字典详情, | To be tested |
|  | ValidateDictionary | 校验指定条件的字典是否存在,支持字典名称和字典编码 | To be tested |
|  | ListDictionary | 查询字典列表 | To be tested |
| INSTANCE_MANAGEMENT | CheckRomaInstanceListV2 | 获取符合条件的服务实例列表。 | To be tested |
| MQS实例管理 | ShowMqsInstance | 查询指定MQS实例详情。 | To be tested |
|  | ListMqsInstance | 查询MQS实例列表。 | To be tested |
| OpenAPI接口 | ImportLiveDataApiDefinitionsV2 | 导入自定义后端API。导入文件内容需要符合swagger标准规范,自定义扩展字段请参考用户指南的“附录:后端API的Swagger扩展定义”章节 | To be tested |
|  | ImportApiDefinitionsV2 | 导入API。导入文件内容需要符合swagger标准规范,自定义扩展字段请参考用户指南的“附录:前端API的Swagger扩展定义”章节。 | To be tested |
|  | ExportLiveDataApiDefinitionsV2 | 导出自定义后端API,导出文件内容符合swagger标准规范。 | To be tested |
|  | ExportApiDefinitionsV2 | 导出分组下API的定义信息,导出文件内容符合swagger标准规范。 | To be tested |
| PUBLIC_MANAGEMENT | ListVersion | 获取服务API版本列表,无需认证 | To be tested |
|  | CheckVersion | 获取指定版本ID的API版本信息 | To be tested |
| SSL证书管理 | BatchAssociateDomainsV2 | SSL证书绑定域名 | To be tested |
|  | UpdateCertificateV2 | 修改SSL证书 | To be tested |
|  | CreateCertificateV2 | 创建SSL证书 | To be tested |
|  | BatchAssociateCertsV2 | 域名绑定SSL证书。目前暂时仅支持单个绑定,请求体当中的certificate_ids里面有且只能有一个证书ID | To be tested |
|  | ListAttachedDomainsV2 | 获取SSL证书已绑定域名列表。 | To be tested |
|  | ListCertificatesV2 | 获取SSL证书列表。 | To be tested |
|  | BatchDisassociateDomainsV2 | SSL证书解绑域名 | To be tested |
|  | ShowDetailsOfCertificateV2 | 查看证书详情 | To be tested |
|  | DeleteCertificateV2 | 删除ssl证书接口,删除时只有没有关联域名的证书才能被删除 | To be tested |
|  | BatchDisassociateCertsV2 | 域名解绑SSL证书。目前暂时仅支持单个解绑,请求体当中的certificate_ids里面有且只能有一个证书ID | To be tested |
| VPC通道管理 | DeleteBackendInstanceV2 | 删除指定VPC通道中的后端实例 | To be tested |
|  | DeleteVpcChannelV2 | 删除指定的VPC通道 | To be tested |
|  | CreateMemberGroup | 在服务集成中创建VPC通道后端服务器组,VPC通道后端实例可以选择是否关联后端实例服务器组,以便管理后端服务器节点。 | To be tested |
|  | UpdateHealthCheck | 修改VPC通道健康检查。 | To be tested |
|  | AddingBackendInstancesV2 | 为指定的VPC通道添加后端实例 | To be tested |
|  | ShowDetailsOfVpcChannelV2 | 查看指定的VPC通道详情 | To be tested |
|  | ListBackendInstancesV2 | 查看指定VPC通道的后端实例列表。 | To be tested |
|  | UpdateVpcChannelV2 | 更新指定VPC通道的参数 | To be tested |
|  | ListMemberGroups | 查询VPC通道后端云服务组列表 | To be tested |
|  | BatchDisableMembers | 批量修改后端服务器状态不可用。 | To be tested |
|  | CreateVpcChannelV2 | 在服务集成中创建连接私有VPC资源的通道,并在创建API时将后端节点配置为使用这些VPC通道,以便服务集成直接访问私有VPC资源。 | To be tested |
|  | BatchEnableMembers | 批量修改后端服务器状态可用。 | To be tested |
|  | UpdateMemberGroup | 更新指定VPC通道后端服务器组 | To be tested |
|  | ShowDetailsOfMemberGroup | 查看指定的VPC通道后端服务器组详情 | To be tested |
|  | UpdateBackendInstancesV2 | 更新指定的VPC通道的后端实例。更新时,使用传入的请求参数对对应云服务组的后端实例进行全量覆盖修改。若未指定修改的云服务器组,则进行全量覆盖。 | To be tested |
|  | ListVpcChannelsV2 | 查看VPC通道列表 | To be tested |
|  | DeleteMemberGroup | 删除指定的VPC通道后端服务器组 | To be tested |
| VPC通道管理-项目级 | CreateProjectVpcChannel | 创建相同的VPC通道关联到多个实例。同一个项目下VPC通道名称不可重复。注意:实例特性vpc_name_modifiable配置为off时才可使用。 | To be tested |
|  | ListProjectVpcChannelsV2 | 查询项目下所有实例的VPC通道列表 | To be tested |
|  | CreateProjectVpcChannelSyncs | 同步VPC通道到多个实例。注意:实例特性vpc_name_modifiable配置为off时才可使用。 | To be tested |
|  | UpdateProjectVpcChannel | 项目下根据VPC通道名称批量修改多个多个实例下的VPC通道。若实例下不存在该VPC通道则创建。注意:实例特性vpc_name_modifiable配置为off时才可使用。 | To be tested |
| 主题管理 | ListMqsInstanceTopics | 查询Topic列表。 | To be tested |
|  | CreateMqsInstanceTopic | 创建Topic。 | To be tested |
|  | BatchDeleteMqsInstanceTopic | 批量删除Topic。 | To be tested |
|  | ImportMqsInstanceTopic | 导入Topic。 | To be tested |
|  | UpdateMqsInstanceTopic | 修改Topic。 | To be tested |
|  | ExportMqsInstanceTopic | 导出Topic。 | To be tested |
|  | DeleteMqsInstanceTopic | 删除Topic。 | To be tested |
| 产品模板 | ListProductTemplates | 查询产品模板 | To be tested |
|  | UpdateProductTemplate | 修改产品模板 | To be tested |
|  | CreateProductTemplate | 创建产品模板 | To be tested |
|  | DeleteProductTemplate | 删除产品模板 | To be tested |
| 产品管理 | ShowProductAuthentication | 查询产品鉴权信息 | To be tested |
|  | CreateProductTopic | 添加产品主题 | To be tested |
|  | UpdateProduct | 修改产品信息 | To be tested |
|  | ListProductTopics | 查询产品主题 | To be tested |
|  | ShowProduct | 查询产品详情 | To be tested |
|  | ListProducts | 查询产品 | To be tested |
|  | ListDevicesInProduct | 查询产品内设备数量 | To be tested |
|  | DeleteProduct | 删除产品 | To be tested |
|  | ResetProductAuthentication | 重置产品鉴权信息 | To be tested |
|  | CreateProduct | 创建产品 | To be tested |
|  | UpdateProductTopic | 更新产品主题 | To be tested |
|  | UploadProduct | 导入产品 | To be tested |
|  | DownloadProducts | 导出产品 | To be tested |
|  | DeleteProductTopic | 删除产品主题 | To be tested |
| 任务监控管理 | ListMonitorLog | 查询单个任务的所有日志信息 | To be tested |
|  | ListMonitorInfos | 查询所有任务的监控信息 | To be tested |
| 任务管理 | ShowDispatches | 查询调度计划 | To be tested |
|  | InstallMultiTasks | 初始化组合任务,分配任务ID,初始化映射等 | To be tested |
|  | CreateCommonTask | 创建普通任务(区别于组合任务) | To be tested |
|  | DeleteTask | 通过任务ID删除指定任务 | To be tested |
|  | CreateDispatches | 创建调度计划 | To be tested |
|  | ShowTask | 通过任务ID查询指定任务的信息 | To be tested |
|  | UpdateDispatches | 通过任务ID和调度ID修改调度计划 | To be tested |
|  | ResetMultiTaskOffset | 重置组合任务进度 | To be tested |
|  | CreateMultiTaskMappings | 创建组合任务映射 | To be tested |
|  | RunTask | 手工触发一次任务调度 | To be tested |
|  | ListTasks | 查询任务列表 | To be tested |
|  | BatchStartOrStopTasks | 批量启动\停止任务 | To be tested |
|  | UpdateMultiTasks | 修改组合任务 | To be tested |
|  | CountTasks | 统计不同类型不同状态任务数量 | To be tested |
|  | StopTask | 手工停止当前执行的任务 | To be tested |
|  | DeleteMultiTaskMapping | 通过映射ID删除指定任务映射 | To be tested |
|  | UpdateTask | 更新普通任务 | To be tested |
|  | CreateMultiTasks | 创建组合任务 | To be tested |
| 域名管理 | UpdateDomainV2 | 修改绑定的域名所对应的配置信息。 | To be tested |
|  | DisassociateCertificateV2 | 如果域名证书不再需要或者已过期,则可以删除证书内容。 | To be tested |
|  | AssociateCertificateV2 | 如果创建API时,“定义API请求”使用HTTPS请求协议,那么在独立域名中需要添加SSL证书。 | To be tested |
|  | ShowDetailsOfDomainNameCertificateV2 | 查看域名下绑定的证书详情。 | To be tested |
|  | DisassociateDomainV2 | 如果API分组不再需要绑定某个自定义域名,则可以为此API分组解绑此域名。 | To be tested |
|  | AssociateDomainV2 | 用户自定义的域名,需要CNAME到API分组的子域名上才能生效。 | To be tested |
| 实例特性管理 | CreateFeatureV2 | 为实例配置需要的特性。 | To be tested |
|  | ListFeaturesV2 | 查看实例特性列表。注意:实例不支持以下特性的需要联系技术支持升级实例版本。 | To be tested |
| 实例管理 | ShowRestrictionOfInstanceV2 | 查看实例约束信息 | To be tested |
|  | ShowDetailsOfInstanceV2 | 查看实例详情 | To be tested |
| 客户端配置 | ShowAppBoundAppQuota | 查看指定客户端应用关联的应用配额。 | To be tested |
|  | ShowDetailsOfAppAcl | 查看APP的访问控制详情。 | To be tested |
|  | DeleteAppCodeV2 | 删除App Code,App Code删除后,将无法再通过简易认证访问对应的API。 | To be tested |
|  | CreateAppCodeAutoV2 | 创建App Code时,可以不指定具体值,由后台自动生成随机字符串填充。 | To be tested |
|  | ShowDetailsOfAppV2 | 查看指定APP的详细信息。 | To be tested |
|  | CreateAppCodeV2 | App Code为APP应用下的子模块,创建App Code之后,可以实现简易的APP认证。 | To be tested |
|  | UpdateAppAcl | 设置客户端配置的访问控制。 | To be tested |
|  | DeleteAppAcl | 删除客户端配置的访问控制信息。 | To be tested |
|  | ListAppsV2 | 查询APP列表。 | To be tested |
|  | ListAppCodesV2 | 查询App Code列表。 | To be tested |
|  | ShowDetailsOfAppCodeV2 | App Code为APP应用下的子模块,创建App Code之后,可以实现简易的APP认证。 | To be tested |
| 客户端配额 | UpdateAppQuota | 修改客户端配额 | To be tested |
|  | ListAppQuotas | 获取客户端配额列表。支持根据名称模糊查询 | To be tested |
|  | CreateAppQuota | 创建客户端配额 | To be tested |
|  | ListAppQuotaBindableApps | 查询客户端配额可绑定的客户端应用列表。支持按客户端应用名称模糊搜索 | To be tested |
|  | DisassociateAppQuotaWithApp | 解除客户端配额和客户端应用的绑定 | To be tested |
|  | ListAppQuotaBoundApps | 查询客户端配额已绑定的客户端应用列表。支持按客户端应用名称模糊匹配 | To be tested |
|  | AssociateAppsForAppQuota | 客户端配额绑定客户端应用列表 | To be tested |
|  | ShowAppQuota | 获取客户端配额详情 | To be tested |
|  | DeleteAppQuota | 删除客户端配额。删除客户端配额时,同时删除客户端配额和客户端应用的关联关系 | To be tested |
| 应用权限管理 | UpdateTopicAccessPolicy | 更新Topic权限。 | To be tested |
|  | ShowMqsInstanceTopicAccessPolicy | 查询Topic权限。 | To be tested |
| 应用配置管理 | UpdateAppConfigV2 | 修改应用配置 | To be tested |
|  | DeleteAppConfigV2 | 删除应用配置 | To be tested |
|  | CreateAppConfigV2 | 创建应用配置 | To be tested |
|  | ShowDetailsOfAppConfigV2 | 查看应用配置详情 | To be tested |
|  | ListAppConfigsV2 | 查询应用配置列表 | To be tested |
| 插件管理 | DeletePlugin | 删除插件。 | To be tested |
|  | UpdatePlugin | 修改插件信息。 | To be tested |
|  | CreatePlugin | 创建插件信息。 | To be tested |
|  | ListPluginAttachedApis | 查询指定插件下绑定的API信息 | To be tested |
|  | ListPlugins | 查询一组符合条件的API网关插件详情。 | To be tested |
|  | AttachApiToPlugin | 绑定插件到API上。 | To be tested |
|  | ListApiAttachablePlugins | 查询可绑定当前API的插件信息。 | To be tested |
|  | DetachApiFromPlugin | 解除绑定在插件上的API | To be tested |
|  | ListPluginAttachableApis | 查询可绑定当前插件的API信息。 | To be tested |
|  | ShowPlugin | 查询插件详情。 | To be tested |
|  | ListApiAttachedPlugins | 查询指定API下绑定的插件信息 | To be tested |
|  | DetachPluginFromApi | 解除绑定在API上的插件 | To be tested |
|  | AttachPluginToApi | 绑定插件到API上。 | To be tested |
| 数据源管理 | ListDatasourceTables | 获取数据源中所有的表 | To be tested |
|  | CreateDatasourceInfo | 创建数据源 | To be tested |
|  | ShowDataourceDetail | 根据数据源id查询数据源 | To be tested |
|  | ListDatasourceColumns | 获取数据源中中某个表中所有字段 | To be tested |
|  | UpdateDatasourceInfo | 修改数据源 | To be tested |
|  | DeleteDatasourceInfoById | 通过数据源Id删除指定数据源信息 | To be tested |
|  | ListDatasources | 查询数据源 | To be tested |
|  | StartTestDatasource | 测试数据源连通性 | To be tested |
| 服务管理 | ListProperties | 查询属性 | To be tested |
|  | UpdateResponseProperty | 修改响应属性 | To be tested |
|  | CreateService | 创建服务 | To be tested |
|  | ShowCommand | 查询命令详情 | To be tested |
|  | ShowResponseProperty | 查询响应属性详情 | To be tested |
|  | ListResponseProperties | 查询响应属性 | To be tested |
|  | CreateRequestProperty | 创建请求属性 | To be tested |
|  | UpdateService | 修改服务 | To be tested |
|  | CreateProperty | 创建属性 | To be tested |
|  | UpdateCommand | 修改命令 | To be tested |
|  | DeleteService | 删除服务 | To be tested |
|  | CreateResponseProperty | 创建响应属性 | To be tested |
|  | DeleteCommand | 删除命令 | To be tested |
|  | UpdateRequestProperty | 修改请求属性 | To be tested |
|  | CreateCommand | 创建命令 | To be tested |
|  | DeleteRequestProperty | 删除请求属性 | To be tested |
|  | ListServices | 查询服务 | To be tested |
|  | ShowService | 查询服务详情 | To be tested |
|  | ListCommands | 查询命令 | To be tested |
|  | ListRequestProperties | 查询请求属性 | To be tested |
|  | DeleteResponseProperty | 删除响应属性 | To be tested |
| 标签管理 | ListTagsV2 | 查询标签列表 | To be tested |
| 流控策略管理 | UpdateRequestThrottlingPolicyV2 | 修改指定流控策略的详细信息。 | To be tested |
|  | DeleteRequestThrottlingPolicyV2 | 删除指定的流控策略。当该流控策略绑定了API时,需要先解除流控策略与API的所有绑定关系后再删除。 | To be tested |
|  | ShowDetailsOfRequestThrottlingPolicyV2 | 查看指定流控策略的详细信息。 | To be tested |
|  | CreateRequestThrottlingPolicyV2 | 当API上线后,系统会默认给每个API提供一个流控策略,API提供者可以根据自身API的服务能力及负载情况变更这个流控策略。 | To be tested |
|  | BatchDeleteThrottlingPolicyV2 | 批量删除流控策略。 | To be tested |
|  | ListRequestThrottlingPolicyV2 | 查询所有流控策略的信息。 | To be tested |
| 消息管理 | ResetMessages | 重发消息。 | To be tested |
|  | ShowMqsInstanceMessages | 查询消息的偏移量和消息内容。 | To be tested |
| 环境变量管理 | CreateEnvironmentVariableV2 | 将API发布到不同的环境后,对于不同的环境,可能会有不同的环境变量,比如,API的服务部署地址,请求的版本号等。 | To be tested |
|  | DeleteEnvironmentVariableV2 | 删除指定的环境变量。 | To be tested |
|  | ShowDetailsOfEnvironmentVariableV2 | 查看指定的环境变量的详情。 | To be tested |
|  | UpdateEnvironmentVariableV2 | 修改环境变量。环境变量引用位置为api的后端服务地址时,修改对应环境变量会将使用该变量的所有api重新发布。 | To be tested |
|  | ListEnvironmentVariablesV2 | 查询分组下的所有环境变量的列表。 | To be tested |
| 环境管理 | DeleteEnvironmentV2 | 删除指定的环境。 | To be tested |
|  | ListEnvironmentsV2 | 查询符合条件的环境列表。 | To be tested |
|  | UpdateEnvironmentV2 | 修改指定环境的信息。其中可修改的属性为:name、remark,其它属性不可修改。 | To be tested |
|  | CreateEnvironmentV2 | 在实际的生产中,API提供者可能有多个环境,如开发环境、测试环境、生产环境等,用户可以自由将API发布到某个环境,供调用者调用。 | To be tested |
| 监控信息查询 | ListLatelyApiStatisticsV2 | 根据API的id和最近的一段时间查询API被调用的次数,统计周期为1分钟。查询范围一小时以内,一分钟一个样本,其样本值为一分钟内的累计值。 | To be tested |
|  | ListStatisticsApi | 查询某个实例下的API统计信息。 | To be tested |
| 签名密钥管理 | ListSignatureKeysV2 | 查询所有签名密钥的信息。 | To be tested |
|  | UpdateSignatureKeyV2 | 修改指定签名密钥的详细信息。 | To be tested |
|  | DeleteSignatureKeyV2 | 删除指定的签名密钥。签名密钥绑定了API时无法删除,需要先解除与API的绑定关系后删除。 | To be tested |
|  | CreateSignatureKeyV2 | 为了保护API的安全性,建议租户为API的访问提供一套保护机制,即租户开放的API,需要对请求来源进行认证,不符合认证的请求直接拒绝访问。 | To be tested |
| 签名密钥绑定关系管理 | DisassociateSignatureKeyV2 | 解除API与签名密钥的绑定关系。 | To be tested |
|  | ListApisNotBoundWithSignatureKeyV2 | 查询所有未绑定到该签名密钥上的API列表。需要API已经发布,未发布的API不予展示。 | To be tested |
|  | ListApisBindedToSignatureKeyV2 | 查询某个签名密钥上已经绑定的API列表。 | To be tested |
|  | ListSignatureKeysBindedToApiV2 | 查询某个API绑定的签名密钥列表。每个API在每个环境上应该最多只会绑定一个签名密钥。 | To be tested |
|  | AssociateSignatureKeyV2 | 签名密钥创建后,需要绑定到API才能生效。 | To be tested |
| 自定义后端服务 | DebugLiveDataApiV2 | 测试后端API是否可用。 | To be tested |
|  | PublishLiveDataApiV2 | 在某个实例中部署后端API。 | To be tested |
|  | UpdateLiveDataApiV2 | 在某个实例中更新后端API的参数。 | To be tested |
|  | ListLiveDataDataSourcesV2 | 查询自定义后端服务数据源列表。 | To be tested |
|  | ListLiveDataApiDeploymentHistoryV2 | 在某个实例中查询后端API的部署记录。 | To be tested |
|  | DeleteLiveDataApiV2 | 在某个实例中删除后端API。 | To be tested |
|  | CheckLivedataApisV2 | 校验自定义后端API定义。校验自定义后端API的路径或名称是否已存在 | To be tested |
|  | ListLiveDataQuotaV2 | 查询自定义后端服务配额。 | To be tested |
|  | UnpublishLiveDataApiV2 | 在某个实例中取消部署后端API。 | To be tested |
|  | CreateLiveDataApiScriptV2 | 在某个实例中创建后端API脚本。 | To be tested |
|  | CreateLiveDataApiV2 | 在某个实例中创建后端API。 | To be tested |
|  | ShowLiveDataApiV2 | 查询后端API的详细信息。 | To be tested |
|  | ListLiveDataApiTestHistoryV2 | 在某个实例中查询后端API的测试结果。 | To be tested |
|  | ListLiveDataApiV2 | 获取某个实例下的所有后端API。 | To be tested |
| 自定义认证管理 | ShowDetailsOfCustomAuthorizersV2 | 查看自定义认证详情 | To be tested |
|  | ListCustomAuthorizersV2 | 查询自定义认证列表 | To be tested |
|  | CreateCustomAuthorizerV2 | 创建自定义认证 | To be tested |
|  | UpdateCustomAuthorizerV2 | 修改自定义认证 | To be tested |
|  | DeleteCustomAuthorizerV2 | 删除自定义认证 | To be tested |
| 规则引擎 | CreateRule | 创建规则 | To be tested |
|  | ShowRule | 查询规则详情 | To be tested |
|  | ListSources | 查询源数据源列表 | To be tested |
|  | DeleteSource | 删除源数据源 | To be tested |
|  | BatchDeleteRules | 批量删除规则 | To be tested |
|  | CreateSource | 添加源数据源 | To be tested |
|  | DeleteRule | 删除规则 | To be tested |
|  | DebugRule | 规则调试 | To be tested |
|  | DeleteDestination | 删除目标数据源 | To be tested |
|  | UpdateRule | 修改规则 | To be tested |
|  | ListDestinations | 查询目标数据源列表 | To be tested |
|  | CreateDestination | 添加目标数据源 | To be tested |
|  | ListRules | 查询规则 | To be tested |
| 订阅管理操作 | ListNotification | 该接口用于查询指定应用订阅管理信息的数据 | To be tested |
|  | UpdateNotification | 该接口用于修改指定的订阅管理 | To be tested |
|  | CreateNotification | 该接口用于创建指定实例下对应的应用下的设备操作,订阅到指定的topic | To be tested |
|  | DeleteNotification | 该接口用于删除指定订阅管理 | To be tested |
| 设备分组管理 | ShowDeviceGroupTree | 查询所有设备分组 | To be tested |
|  | DeleteDeviceGroup | 删除分组 | To be tested |
|  | ShowDeviceGroup | 获取设备分组及下一层分组信息 | To be tested |
|  | BatchAddDeviceToGroup | 批量添加设备到设备分组 | To be tested |
|  | DeleteDeviceFromGroup | 删除设备分组内的设备 | To be tested |
|  | CreateDeviceGroup | 创建设备分组 | To be tested |
|  | UpdateDeviceGroup | 修改设备分组 | To be tested |
| 设备管理 | ShowAuthentication | 查询设备鉴权信息 | To be tested |
|  | UpdateDevice | 修改设备信息 | To be tested |
|  | ListDevices | 查询设备 | To be tested |
|  | ListTopics | 查询设备主题 | To be tested |
|  | SendCommand | 发送命令 | To be tested |
|  | ListSubsets | 查询子设备 | To be tested |
|  | ResetAuthentication | 重置设备鉴权信息 | To be tested |
|  | BatchFreezeDevices | 设备批量下线 | To be tested |
|  | AddSubsetsToGateway | 添加子设备到网关 | To be tested |
|  | CreateDevice | 创建设备 | To be tested |
|  | ListShadows | 查询设备影子 | To be tested |
|  | ShowDevice | 查询设备详情 | To be tested |
|  | DeleteDevice | 删除指定设备ID的设备 | To be tested |
| 设置特殊流控 | ListSpecialThrottlingConfigurationsV2 | 查看给流控策略设置的特殊配置。 | To be tested |
|  | CreateSpecialThrottlingConfigurationV2 | 流控策略可以限制一段时间内可以访问API的最大次数,也可以限制一段时间内单个租户和单个APP可以访问API的最大次数。 | To be tested |
|  | DeleteSpecialThrottlingConfigurationV2 | 删除某个流控策略的某个特殊配置。 | To be tested |
|  | UpdateSpecialThrottlingConfigurationV2 | 修改某个流控策略下的某个特殊设置。 | To be tested |
| 配置管理 | ListProjectCofigsV2 | 查询某个实例的租户配置列表,用户可以通过此接口查看各类型资源配置及使用情况。 | To be tested |
