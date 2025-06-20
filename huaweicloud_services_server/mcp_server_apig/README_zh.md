# APIG MCP Server 

## 版本信息
v0.1.0

## 产品描述

APIG MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务APIG交互的能力。可以基于自然语言对APIG资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 专享版-ACL策略管理 | DeleteAclV2 | 删除指定的ACL策略, 如果存在api与该ACL策略的绑定关系,则无法删除 | To be tested |
|  | ShowDetailsOfAclPolicyV2 | 查询指定ACL策略的详情。 | To be tested |
|  | ListAclStrategiesV2 | 查询所有的ACL策略列表。 | To be tested |
|  | UpdateAclStrategyV2 | 修改指定的ACL策略,其中可修改的属性为:acl_name、acl_type、acl_value,其它属性不可修改。 | To be tested |
|  | CreateAclStrategyV2 | 增加一个ACL策略,策略类型通过字段acl_type来确定(permit或者deny),限制的对象的类型可以为IP或者DOMAIN,这里的DOMAIN对应的acl_value的值为租户名称,而非“www.exampleDomain.com”之类的网络域名。 | To be tested |
|  | BatchDeleteAclV2 | 批量删除指定的多个ACL策略。 | To be tested |
| 专享版-API分组管理 | CheckApiGroupsV2 | 校验API分组名称是否存在。 | To be tested |
|  | ListApiGroupsV2 | 查询API分组列表。 | To be tested |
|  | DeleteApiGroupV2 | 删除指定的API分组。 | To be tested |
|  | CreateApiGroupV2 | API分组是API的管理单元,一个API分组等同于一个服务入口,创建API分组时,返回一个子域名作为访问入口。建议一个API分组下的API具有一定的相关性。 | To be tested |
|  | ShowDetailsOfApiGroupV2 | 查询指定分组的详细信息。 | To be tested |
|  | UpdateApiGroupV2 | 修改API分组属性。其中name和remark可修改,其他属性不可修改。 | To be tested |
| 专享版-API管理 | ListApiVersionDetailV2 | 查询某个指定的版本详情。 | To be tested |
|  | CreateApiV2 | 添加一个API,API即一个服务接口,具体的服务能力。 | To be tested |
|  | ListApiRuntimeDefinitionV2 | 查看指定的API在指定的环境上的运行时定义,默认查询RELEASE环境上的运行时定义。 | To be tested |
|  | ListApisV2 | 查看API列表,返回API详细信息、发布信息等,但不能查看到后端服务信息和API请求参数信息 | To be tested |
|  | ChangeApiVersionV2 | API每次发布时,会基于当前的API定义生成一个版本。版本记录了API发布时的各种定义及状态。 | To be tested |
|  | DeleteApiByVersionIdV2 | 对某个生效中的API版本进行下线操作,下线后,API在该版本生效的环境中将不再能够被调用。 | To be tested |
|  | CreateOrDeletePublishRecordForApiV2 | 对API进行发布或下线。 | To be tested |
|  | ListApiVersionsV2 | 查询某个API的历史版本。每个API在一个环境上最多存在10个历史版本。 | To be tested |
|  | BatchPublishOrOfflineApiV2 | 将多个API发布到一个指定的环境,或将多个API从指定的环境下线。 | To be tested |
|  | CheckApisV2 | 校验API定义。校验API的路径或名称是否已存在 | To be tested |
|  | ShowDetailsOfApiV2 | 查看指定的API的详细信息。 | To be tested |
|  | UpdateApiV2 | 修改指定API的信息,包括后端服务信息。 | To be tested |
|  | DeleteApiV2 | 删除指定的API。 | To be tested |
|  | DebugApiV2 | 调试一个API在指定运行环境下的定义,接口调用者需要具有操作该API的权限。 | To be tested |
| 专享版-API绑定ACL策略 | BatchDeleteApiAclBindingV2 | 批量解除API与ACL策略的绑定 | To be tested |
|  | CreateApiAclBindingV2 | 将API与ACL策略进行绑定。 | To be tested |
|  | ListApisBindedToAclPolicyV2 | 查看ACL策略绑定的API列表 | To be tested |
|  | ListApisUnbindedToAclPolicyV2 | 查看ACL策略未绑定的API列表,需要API已发布 | To be tested |
|  | ListAclPolicyBindedToApiV2 | 查看API绑定的ACL策略列表 | To be tested |
|  | DeleteApiAclBindingV2 | 解除某条API与ACL策略的绑定关系 | To be tested |
| 专享版-API绑定流控策略 | BatchDisassociateThrottlingPolicyV2 | 批量解除API与流控策略的绑定关系 | To be tested |
|  | DisassociateRequestThrottlingPolicyV2 | 解除API与流控策略的绑定关系。 | To be tested |
|  | ListApisBindedToRequestThrottlingPolicyV2 | 查询某个流控策略上已经绑定的API列表。 | To be tested |
|  | ListRequestThrottlingPoliciesBindedToApiV2 | 查询某个API绑定的流控策略列表。每个环境上应该最多只有一个流控策略。 | To be tested |
|  | AssociateRequestThrottlingPolicyV2 | 将流控策略应用于API,则所有对该API的访问将会受到该流控策略的限制。 | To be tested |
|  | ListApisUnbindedToRequestThrottlingPolicyV2 | 查询所有未绑定到该流控策略上的自有API列表。需要API已经发布,未发布的API不予展示。 | To be tested |
| 专享版-APP授权管理 | ListApisBindedToAppV2 | 查询APP已经绑定的API列表。 | To be tested |
|  | ListApisUnbindedToAppV2 | 查询指定环境上某个APP未绑定的API列表,包括自有API和从云商店购买的API。 | To be tested |
|  | CreateAuthorizingAppsV2 | APP创建成功后,还不能访问API,如果想要访问某个环境上的API,需要将该API在该环境上授权给APP。授权成功后,APP即可访问该环境上的这个API。 | To be tested |
|  | CancelingAuthorizationV2 | 解除API对APP的授权关系。解除授权后,APP将不再能够调用该API。 | To be tested |
|  | ListAppsBindedToApiV2 | 查询API绑定的APP列表。 | To be tested |
| 专享版-OpenAPI接口 | ExportApiDefinitionsV2 | 导出分组下API的定义信息。导出文件内容符合swagger标准规范,API网关自定义扩展字段请参考《API网关用户指南》的“导入导出API:扩展定义”章节。 | To be tested |
|  | ImportApiDefinitionsV2 | 导入API。导入文件内容需要符合swagger标准规范,API网关自定义扩展字段请参考《API网关用户指南》的“导入导出API:扩展定义”章节。 | To be tested |
| 专享版-SSL证书管理 | BatchDisassociateDomainsV2 | SSL证书解绑域名。在使用自定义入方向端口的特性时,相同的域名会同时解绑证书。 | To be tested |
|  | ShowDetailsOfCertificateV2 | 查看证书详情。 | To be tested |
|  | DeleteCertificateV2 | 删除ssl证书接口,删除时只有没有关联域名的证书才能被删除。 | To be tested |
|  | BatchDisassociateCertsV2 | 域名解绑SSL证书。目前暂时仅支持单个解绑,请求体当中的certificate_ids里面有且只能有一个证书ID。在使用自定义入方向端口的特性时,相同的域名会同时解绑证书。 | To be tested |
|  | BatchAssociateCertsV2 | 域名绑定SSL证书。目前暂时仅支持单个绑定,请求体当中的certificate_ids里面有且只能有一个证书ID。使用实例自定义入方向端口的特性时,相同的域名会同时绑定证书,注意开启/关闭客户端校验会对相同域名的不同端口同时生效。 | To be tested |
|  | ListCertificatesV2 | 获取SSL证书列表。 | To be tested |
|  | UpdateCertificateV2 | 修改SSL证书。 | To be tested |
|  | CreateCertificateV2 | 创建SSL证书。 | To be tested |
|  | ListAttachedDomainsV2 | 获取SSL证书已绑定域名列表。 | To be tested |
|  | BatchAssociateDomainsV2 | SSL证书绑定域名。使用实例自定义入方向端口的特性时,相同的域名会同时绑定证书,注意开启/关闭客户端校验会对相同域名的不同端口同时生效。 | To be tested |
| 专享版-VPC通道管理 | DeleteVpcChannelV2 | 删除指定的VPC通道 | To be tested |
|  | UpdateHealthCheck | 修改VPC通道健康检查。 | To be tested |
|  | CreateMemberGroup | 在APIG中创建VPC通道后端服务器组,VPC通道后端实例可以选择是否关联后端实例服务器组,以便管理后端服务器节点。 | To be tested |
|  | BatchDisableMembers | 批量修改后端服务器状态不可用。 | To be tested |
|  | ShowDetailsOfMemberGroup | 查看指定的VPC通道后端服务器组详情 | To be tested |
|  | UpdateVpcChannelV2 | 更新指定VPC通道的参数 | To be tested |
|  | ListMemberGroups | 查询VPC通道后端云服务组列表 | To be tested |
|  | BatchEnableMembers | 批量修改后端服务器状态可用。 | To be tested |
|  | CreateVpcChannelV2 | 在API网关中创建连接私有VPC资源的通道,并在创建API时将后端节点配置为使用这些VPC通道,以便API网关直接访问私有VPC资源。 | To be tested |
|  | UpdateBackendInstancesV2 | 更新指定的VPC通道的后端实例。更新时,使用传入的请求参数对对应云服务组的后端实例进行全量覆盖修改。如果未指定修改的云服务器组,则进行全量覆盖。 | To be tested |
|  | UpdateMemberGroup | 更新指定VPC通道后端服务器组。当负载通道为nacos微服务类型时,不支持修改服务器组权重。 | To be tested |
|  | ShowDetailsOfVpcChannelV2 | 查看指定的VPC通道详情 | To be tested |
|  | AddingBackendInstancesV2 | 为指定的VPC通道添加后端实例 | To be tested |
|  | DeleteMemberGroup | 删除指定的VPC通道后端服务器组 | To be tested |
|  | ListVpcChannelsV2 | 查看VPC通道列表 | To be tested |
|  | DeleteBackendInstanceV2 | 删除指定VPC通道中的后端实例 | To be tested |
|  | ListBackendInstancesV2 | 查看指定VPC通道的后端实例列表。 | To be tested |
| 专享版-凭据管理 | DeleteAppCodeV2 | 删除App Code,App Code删除后,将无法再通过简易认证访问对应的API。 | To be tested |
|  | CreateAppCodeV2 | App Code为APP应用下的子模块,创建App Code之后,可以实现简易的APP认证。 | To be tested |
|  | ListAppsV2 | 查询APP列表。 | To be tested |
|  | UpdateAppAcl | 设置凭据的访问控制。 | To be tested |
|  | DeleteAppV2 | 删除指定的APP。 | To be tested |
|  | CreateAnAppV2 | APP即应用,是一个可以访问API的身份标识。将API授权给APP后,APP即可调用API。 | To be tested |
|  | ResettingAppSecretV2 | 重置指定APP的密钥。 | To be tested |
|  | ShowDetailsOfAppCodeV2 | App Code为APP应用下的子模块,创建App Code之后,可以实现简易的APP认证。 | To be tested |
|  | UpdateAppV2 | 修改指定APP的信息。其中可修改的属性为:name、remark,当支持用户自定义key和secret的开关开启时,app_key和app_secret也支持修改,其它属性不可修改。 | To be tested |
|  | DeleteAppAcl | 删除凭据的访问控制信息。 | To be tested |
|  | ShowDetailsOfAppV2 | 查看指定APP的详细信息。 | To be tested |
|  | ShowAppBoundAppQuota | 查看指定凭据关联的凭据配额。 | To be tested |
|  | CreateAppCodeAutoV2 | 创建App Code时,可以不指定具体值,由后台自动生成随机字符串填充。 | To be tested |
|  | CheckAppV2 | 校验app是否存在,非APP所有者可以调用该接口校验APP是否真实存在。这个接口只展示app的基本信息id 、name、 | To be tested |
|  | ListAppCodesV2 | 查询App Code列表。 | To be tested |
|  | ShowDetailsOfAppAcl | 查看APP的访问控制详情。 | To be tested |
| 专享版-凭据配额管理 | ShowAppQuota | 获取凭据配额详情 | To be tested |
|  | ListAppQuotaBindableApps | 查询凭据配额可绑定的凭据列表。支持按凭据名称模糊搜索 | To be tested |
|  | ListAppQuotas | 获取凭据配额列表。支持根据名称模糊查询 | To be tested |
|  | UpdateAppQuota | 修改凭据配额 | To be tested |
|  | ListAppQuotaBoundApps | 查询凭据配额已绑定的凭据列表。支持按凭据名称模糊匹配 | To be tested |
|  | CreateAppQuota | 创建凭据配额 | To be tested |
|  | DisassociateAppQuotaWithApp | 解除凭据配额和凭据的绑定 | To be tested |
|  | AssociateAppsForAppQuota | 凭据配额绑定凭据列表 | To be tested |
|  | DeleteAppQuota | 删除凭据配额。删除凭据配额时,同时删除凭据配额和凭据的关联关系 | To be tested |
| 专享版-分组自定义响应管理 | UpdateGatewayResponseTypeV2 | 修改分组下指定错误类型的自定义响应。 | To be tested |
|  | ListGatewayResponsesV2 | 查询分组自定义响应列表 | To be tested |
|  | DeleteGatewayResponseV2 | 删除分组自定义响应 | To be tested |
|  | ShowDetailsOfGatewayResponseTypeV2 | 查看分组下指定错误类型的自定义响应 | To be tested |
|  | DeleteGatewayResponseTypeV2 | 删除分组指定错误类型的自定义响应配置,还原为使用默认值的配置。 | To be tested |
|  | CreateGatewayResponseV2 | 新增分组下自定义响应 | To be tested |
|  | ShowDetailsOfGatewayResponseV2 | 查询分组自定义响应详情 | To be tested |
|  | UpdateGatewayResponseV2 | 修改分组自定义响应 | To be tested |
| 专享版-域名管理 | UpdateSlDomainSettingV2 | 禁用或启用API分组绑定的调试域名 | To be tested |
|  | UpdateDomainV2 | 修改绑定的域名所对应的配置信息。使用实例自定义入方向端口的特性时,注意开启/关闭客户端校验会对相同域名的不同端口同时生效。 | To be tested |
|  | ShowDetailsOfDomainNameCertificateV2 | 查看域名下绑定的证书详情。 | To be tested |
|  | DisassociateDomainV2 | 如果API分组不再需要绑定某个自定义域名,则可以为此API分组解绑此域名。 | To be tested |
|  | AssociateCertificateV2 | 如果创建API时,“定义API请求”使用HTTPS请求协议,那么在独立域名中需要添加SSL证书。 | To be tested |
|  | DisassociateCertificateV2 | 如果域名证书不再需要或者已过期,则可以删除证书内容。在使用自定义入方向端口的特性时,相同的域名会同时解绑证书。 | To be tested |
|  | AssociateDomainV2 | 用户自定义的域名,需要增加A记录才能生效,具体方法请参见《云解析服务用户指南》的“添加A类型记录集”章节。 | To be tested |
| 专享版-实例标签管理 | BatchCreateOrDeleteInstanceTags | 批量添加或删除单个实例的标签。 | To be tested |
|  | ListProjectInstanceTags | 查询项目下所有实例标签。 | To be tested |
|  | ListInstanceTags | 查询单个实例的标签。 | To be tested |
|  | ListInstancesByTags | 通过标签查询实例列表 | To be tested |
|  | ShowInstancesNumByTags | 查询包含指定标签的实例数量。 | To be tested |
| 专享版-实例特性管理 | ListInstanceFeatures | 查询实例支持的特性列表。 | To be tested |
|  | ListFeaturesV2 | 查看实例特性列表。注意:实例不支持以下特性的需要联系技术支持升级实例版本。 | To be tested |
|  | CreateFeatureV2 | 为实例配置需要的特性。 | To be tested |
| 专享版-实例管理 | CreatePrepayResize | 创建包周期规格变更订单。 | To be tested |
|  | UpdateIngressEipV2 | 更新实例入公网带宽,仅当实例为ELB类型时支持 | To be tested |
|  | AddEngressEipV2 | 实例开启公网出口 | To be tested |
|  | DeleteInstancesV2 | 删除专享版实例 | To be tested |
|  | CreateInstanceV2 | 创建按需专享版实例 | To be tested |
|  | ListInstancesV2 | 查询专享版实例列表 | To be tested |
|  | CreatePostPayResizeOrder | 创建按需规格变更订单。 | To be tested |
|  | ShowDetailsOfInstanceProgressV2 | 查看专享版实例创建进度 | To be tested |
|  | ShowRestrictionOfInstanceV2 | 查看实例约束信息 | To be tested |
|  | ListAvailableZonesV2 | 查看可用区信息 | To be tested |
|  | CreateOrder | 创建包周期专享版实例。 | To be tested |
|  | RemoveIngressEipV2 | 关闭实例公网入口,仅当实例为ELB类型时支持 | To be tested |
|  | AddEipV2 | 实例更新或绑定EIP(仅当实例为LVS类型时支持) | To be tested |
|  | RemoveEipV2 | 实例解绑EIP | To be tested |
|  | ShowDetailsOfInstanceV2 | 查看专享版实例详情 | To be tested |
|  | RemoveEngressEipV2 | 关闭实例公网出口 | To be tested |
|  | UpdateInstanceV2 | 更新专享版实例 | To be tested |
|  | AddIngressEipV2 | 开启实例开启公网入口,仅当实例为ELB类型时支持 | To be tested |
|  | UpdateEngressEipV2 | 更新实例出公网带宽 | To be tested |
| 专享版-实例终端节点管理 | AcceptOrRejectEndpointConnections | 接受或拒绝实例节点连接。 | To be tested |
|  | AddEndpointPermissions | 批量添加实例终端节点连接白名单。 | To be tested |
|  | ListEndpointConnections | 查询实例终端节点连接列表。 | To be tested |
|  | ListEndpointPermissions | 查询当前实例终端节点服务的白名单列表。 | To be tested |
|  | DeleteEndpointPermissions | 批量删除实例终端节点连接白名单。 | To be tested |
| 专享版-实例自定义入方向端口管理 | ListCustomIngressPorts | 查询实例的自定义入方向端口列表。 | To be tested |
|  | AddCustomIngressPort | 新增实例的自定义入方向端口,在同个实例中,一个端口仅能支持一种协议。 | To be tested |
|  | DeleteCustomIngressPort | 删除实例指定的自定义入方向端口,不包含默认端口80和443。 | To be tested |
|  | ListCustomIngressPortDomains | 查询实例指定的自定义入方向端口绑定的域名信息。 | To be tested |
| 专享版-异步任务管理 | ShowAsyncTaskResult | 获取异步任务结果。 | To be tested |
|  | ExportApiDefinitionsAsync | 导出分组下API的定义信息。导出文件内容符合swagger标准规范,API网关自定义扩展字段请参考《API网关用户指南》的“导入导出API:扩展定义”章节。 | To be tested |
|  | ImportApiDefinitionsAsync | 导入API。导入文件内容需要符合swagger标准规范,API网关自定义扩展字段请参考《API网关用户指南》的“导入导出API:扩展定义”章节。 | To be tested |
| 专享版-微服务中心管理 | ImportMicroservice | 导入微服务。 | To be tested |
| 专享版-插件管理 | CreatePlugin | 创建插件信息。 | To be tested |
|  | DetachApiFromPlugin | 解除绑定在插件上的API。 | To be tested |
|  | ListPlugins | 查询一组符合条件的API网关插件详情。 | To be tested |
|  | ShowPlugin | 查询插件详情。 | To be tested |
|  | DetachPluginFromApi | 解除绑定在API上的插件。 | To be tested |
|  | UpdatePlugin | 修改插件信息。 | To be tested |
|  | ListApiAttachedPlugins | 查询指定API下绑定的插件信息。 | To be tested |
|  | DeletePlugin | 删除插件。 | To be tested |
|  | ListApiAttachablePlugins | 查询可绑定当前API的插件信息。 | To be tested |
|  | ListPluginAttachableApis | 查询可绑定当前插件的API信息。 | To be tested |
|  | ListPluginAttachedApis | 查询指定插件下绑定的API信息。 | To be tested |
|  | AttachPluginToApi | 绑定插件到API上。 | To be tested |
|  | AttachApiToPlugin | 绑定插件到API上。 | To be tested |
| 专享版-标签管理 | ListTagsV2 | 查询标签列表 | To be tested |
| 专享版-概要查询 | ListApiGroupsQuantitiesV2 | 查询租户名下的API分组概况。 | To be tested |
|  | ListApiQuantitiesV2 | 查询租户名下的API概况:已发布到RELEASE环境的API个数,未发布到RELEASE环境的API个数。 | To be tested |
|  | ListAppQuantitiesV2 | 查询租户名下的APP概况:已进行API访问授权的APP个数,未进行API访问授权的APP个数。 | To be tested |
| 专享版-流控策略管理 | ListRequestThrottlingPolicyV2 | 查询所有流控策略的信息。 | To be tested |
|  | UpdateRequestThrottlingPolicyV2 | 修改指定流控策略的详细信息。 | To be tested |
|  | ShowDetailsOfRequestThrottlingPolicyV2 | 查看指定流控策略的详细信息。 | To be tested |
|  | CreateRequestThrottlingPolicyV2 | 当API上线后,系统会默认给每个API提供一个流控策略,API提供者可以根据自身API的服务能力及负载情况变更这个流控策略。 | To be tested |
|  | DeleteRequestThrottlingPolicyV2 | 删除指定的流控策略,以及该流控策略与API的所有绑定关系。 | To be tested |
| 专享版-环境变量管理 | CreateEnvironmentVariableV2 | 将API发布到不同的环境后,对于不同的环境,可能会有不同的环境变量,比如,API的服务部署地址,请求的版本号等。 | To be tested |
|  | ShowDetailsOfEnvironmentVariableV2 | 查看指定的环境变量的详情。 | To be tested |
|  | DeleteEnvironmentVariableV2 | 删除指定的环境变量。 | To be tested |
|  | UpdateEnvironmentVariableV2 | 修改环境变量。环境变量引用位置为api的后端服务地址时,修改对应环境变量会将使用该变量的所有api重新发布。 | To be tested |
|  | ListEnvironmentVariablesV2 | 查询分组下的所有环境变量的列表。 | To be tested |
| 专享版-环境管理 | UpdateEnvironmentV2 | 修改指定环境的信息。其中可修改的属性为:name、remark,其它属性不可修改。 | To be tested |
|  | CreateEnvironmentV2 | 在实际的生产中,API提供者可能有多个环境,如开发环境、测试环境、生产环境等,用户可以自由将API发布到某个环境,供调用者调用。 | To be tested |
|  | DeleteEnvironmentV2 | 删除指定的环境。 | To be tested |
|  | ListEnvironmentsV2 | 查询符合条件的环境列表。 | To be tested |
| 专享版-监控信息查询 | ListLatelyGroupStatisticsV2 | 根据API分组的编号查询该分组下所有API被调用的总次数,统计周期为1分钟。查询范围一小时以内,一分钟一个样本,其样本值为一分钟内的累计值。 | To be tested |
|  | ListMetricData | 查询指定时间范围指定指标的指定粒度的监控数据,可以通过参数指定需要查询的数据维度。 | To be tested |
|  | ListLatelyApiStatisticsV2 | 根据API的id和最近的一段时间查询API被调用的次数,统计周期为1分钟。查询范围一小时以内,一分钟一个样本,其样本值为一分钟内的累计值。 | To be tested |
| 专享版-签名密钥管理 | UpdateSignatureKeyV2 | 修改指定签名密钥的详细信息。 | To be tested |
|  | CreateSignatureKeyV2 | 为了保护API的安全性,建议租户为API的访问提供一套保护机制,即租户开放的API,需要对请求来源进行认证,不符合认证的请求直接拒绝访问。 | To be tested |
|  | DeleteSignatureKeyV2 | 删除指定的签名密钥,删除签名密钥时,其配置的绑定关系会一并删除,相应的签名密钥会失效。 | To be tested |
|  | ListSignatureKeysV2 | 查询所有签名密钥的信息。 | To be tested |
| 专享版-签名密钥绑定关系管理 | AssociateSignatureKeyV2 | 签名密钥创建后,需要绑定到API才能生效。 | To be tested |
|  | ListSignatureKeysBindedToApiV2 | 查询某个API绑定的签名密钥列表。每个API在每个环境上应该最多只会绑定一个签名密钥。 | To be tested |
|  | DisassociateSignatureKeyV2 | 解除API与签名密钥的绑定关系。 | To be tested |
|  | ListApisBindedToSignatureKeyV2 | 查询某个签名密钥上已经绑定的API列表。 | To be tested |
|  | ListApisNotBoundWithSignatureKeyV2 | 查询所有未绑定到该签名密钥上的API列表。需要API已经发布,未发布的API不予展示。 | To be tested |
| 专享版-编排规则管理 | ShowDetailsOfOrchestration | 查询编排规则详情 | To be tested |
|  | DeleteOrchestration | 删除编排规则 | To be tested |
|  | ListOrchestrationAttachedApis | 查询指定插件下绑定的API信息 | To be tested |
|  | UpdateOrchestration | 更新编排规则 | To be tested |
|  | ListOrchestrations | 查看编排规则列表 | To be tested |
|  | CreateOrchestration | 创建编排规则 | To be tested |
| 专享版-自定义认证管理 | CreateCustomAuthorizerV2 | 创建自定义认证 | To be tested |
|  | UpdateCustomAuthorizerV2 | 修改自定义认证 | To be tested |
|  | ShowDetailsOfCustomAuthorizersV2 | 查看自定义认证详情 | To be tested |
|  | DeleteCustomAuthorizerV2 | 删除自定义认证 | To be tested |
|  | ListCustomAuthorizersV2 | 查询自定义认证列表 | To be tested |
| 专享版-设置特殊流控 | ListSpecialThrottlingConfigurationsV2 | 查看给流控策略设置的特殊配置。 | To be tested |
|  | DeleteSpecialThrottlingConfigurationV2 | 删除某个流控策略的某个特殊配置。 | To be tested |
|  | CreateSpecialThrottlingConfigurationV2 | 流控策略可以限制一段时间内可以访问API的最大次数,也可以限制一段时间内单个租户和单个APP可以访问API的最大次数。 | To be tested |
|  | UpdateSpecialThrottlingConfigurationV2 | 修改某个流控策略下的某个特殊设置。 | To be tested |
| 专享版-配置管理 | ListInstanceConfigsV2 | 查询租户实例配置列表 | To be tested |
|  | ListProjectCofigsV2 | 查询某个实例的租户配置列表,用户可以通过此接口查看各类型资源配置及使用情况。 | To be tested |
| 共享版-API分组管理 | DeleteApiGroup | 删除指定的API分组。 | To be tested |
|  | ListApiGroups | 查询API分组列表。 | To be tested |
|  | CreateApiGroup | API分组是API的管理单元,一个API分组等同于一个服务入口,创建API分组时,返回一个子域名作为访问入口。建议一个API分组下的API具有一定的相关性。 | To be tested |
|  | UpdateAPIGroup | 修改API分组属性。其中name和remark可修改,其他属性不可修改。 | To be tested |
|  | ShowDetailsOfApiGroup | 查询指定分组的详细信息。 | To be tested |
| 共享版-API管理 | UpdateApi | 修改指定API的信息,包括后端服务信息。 | To be tested |
|  | ShowDetailsOfApi | 查看指定的API的详细信息。 | To be tested |
|  | DeleteApi | 删除指定的API 删除API时,会删除该API所有相关的资源信息或绑定关系,如API的发布记录,绑定的后端服务,对APP的授权信息等。 | To be tested |
|  | ListApis | 查看API列表,返回API详细信息、发布信息等,但不能查看到后端服务信息。 | To be tested |
|  | CreateApi | 添加一个API,API即一个服务接口,具体的服务能力。API分为两部分,第一部分为面向API使用者的API接口,定义了使用者如何调用这个API。第二部分面向API提供者,由API提供者定义这个API的真实的后端情况,定义了API网关如何去访问真实的后端服务。API的真实后端服务目前支持三种类型:传统的HTTP/HTTPS形式的web后端、函数工作流、MOCK。 | To be tested |
| 共享版-API绑定流控策略 | ListRequestThrottlingPoliciesThatBoundToAnApi | 查询某个API绑定的流控策略列表。每个环境上应该最多只有一个流控策略。 | To be tested |
|  | ListApisThatNotBoundWithRequestThrottlingPolicy | 查询所有未绑定到该流控策略上的自有API列表。需要API已经发布,未发布的API不予展示。 | To be tested |
|  | DisassociateRequestThrottlingPolicy | 解除API与流控策略的绑定关系。 | To be tested |
|  | ListApisThatBoundWithRequestThrottlingPolicy | 查询某个流控策略上已经绑定的API列表。 | To be tested |
|  | AssociateRequestThrottlingPolicy | 将流控策略应用于API,则所有对该API的访问将会受到该流控策略的限制。当一定时间内的访问次数超过流控策略设置的API最大访问次数限制后,后续的访问将会被拒绝,从而能够较好的保护后端API免受异常流量的冲击,保障服务的稳定运行。为指定的共享版-API绑定流控策略,绑定时,需要指定在哪个环境上生效。同一个API发布到不同的环境可以绑定不同的流控策略;一个API在发布到特定环境后只能绑定一个默认的流控策略。 | To be tested |
| 共享版-APP授权管理 | CreateAuthorizingApps | APP创建成功后,还不能访问API,如果想要访问某个环境上的API,需要将该API在该环境上授权给APP。授权成功后,APP即可访问该环境上的这个API。 | To be tested |
|  | CancelingAuthorization | 解除API对APP的授权关系。解除授权后,APP将不再能够调用该API。 | To be tested |
|  | ListApisThatNotBoundWithAnApp | 查询指定环境上某个APP未绑定的API列表,包括自有API和从云市场购买的API。 | To be tested |
|  | ListAPIsThatBoundWithAnApp | 查询APP已经绑定的API列表。 | To be tested |
|  | ListAppsBoundToAnApi | 查询API绑定的APP列表。 | To be tested |
| 共享版-APP管理 | UpdateAnApp | 修改指定APP的信息。其中可修改的属性为:name、remark,当支持用户自定义key和secret的开关开启时,app_key和app_secret也支持修改,其它属性不可修改。 | To be tested |
|  | CheckAnApp | 校验app是否存在,非APP所有者可以调用该接口校验APP是否真实存在。这个接口只展示app的基本信息id 、name、 remark,其他信息不显示。 | To be tested |
|  | ShowAppDetails | 查看指定APP的详细信息。 | To be tested |
|  | CreateAnApp | APP即应用,是一个可以访问API的身份标识。将API授权给APP后,APP即可调用API。 | To be tested |
|  | DeleteAnApp | 删除指定的APP。 | To be tested |
|  | ListApps | 查询APP列表。 | To be tested |
|  | ResettingTheAppSecret | 重置指定APP的密钥。 | To be tested |
| 共享版-域名管理 | AssociateDomain | 用户自定义的域名,需要CNAME到API分组的子域名上才能生效,具体方法请参见[增加CNAME类型记录集](https://support.huaweicloud.com/usermanual-dns/dns_usermanual_0010.html)。 | To be tested |
|  | ShowDetailsOfDomainNameCertificate | 查看域名下绑定的证书详情。 | To be tested |
|  | AssociateCertificate | 如果创建API时,“定义API请求”使用HTTPS请求协议,那么在独立域名中需要添加SSL证书。 | To be tested |
|  | DisassociateCertificate | 如果域名证书不再需要或者已过期,则可以删除证书内容。 | To be tested |
|  | DisassociateDomain | 如果API分组不再需要绑定某个自定义域名,则可以为此API分组解绑此域名。 | To be tested |
| 共享版-概要查询 | ListAppQuantities | 查询租户名下的APP概况:已进行API访问授权的APP个数,未进行API访问授权的APP个数。 | To be tested |
|  | ListAPIsOfAPIGroup | 查询租户名下的API分组概况:上架的API分组个数,未上架的API分组个数。 | To be tested |
|  | ListApiQuantities | 查询租户名下的API概况:已发布到RELEASE环境的API个数,未发布到RELEASE环境的API个数。 | To be tested |
| 共享版-流控策略管理 | DeleteRequestThrottlingPolicy | 删除指定的流控策略,以及该流控策略与API的所有绑定关系。 | To be tested |
|  | ListTheRequestThrottlingPolicy | 查询所有流控策略的信息。 | To be tested |
|  | ShowDetailsOfARequestThrottlingPolicy | 查看指定流控策略的详细信息。 | To be tested |
|  | UpdateRequestThrottlingPolicy | 修改指定流控策略的详细信息。 | To be tested |
|  | CreateRequestThrottlingPolicy | 当API上线后,系统会默认给每个API提供一个流控策略,API提供者可以根据自身API的服务能力及负载情况变更这个流控策略。 流控策略即限制API在一定长度的时间内,能够允许被访问的最大次数。 | To be tested |
| 共享版-环境变量管理 | ListEnvironmentVariables | 查询分组下的所有环境变量的列表。 | To be tested |
|  | DeleteEnvironmentVariable | 删除指定的环境变量。 | To be tested |
|  | CreateEnvironmentVariable | 将API发布到不同的环境后,对于不同的环境,可能会有不同的环境变量,比如,API的服务部署地址,请求的版本号等。 | To be tested |
|  | ShowEnvironmentVariableDetails | 查看指定的环境变量的详情。 | To be tested |
| 共享版-环境管理 | DeleteEnvironment | 删除指定的环境。 | To be tested |
|  | UpdateEnvironment | 修改指定环境的信息。其中可修改的属性为:name、remark,其它属性不可修改。 | To be tested |
|  | CreateEnvironment | 在实际的生产中,API提供者可能有多个环境,如开发环境、测试环境、生产环境等,用户可以自由将API发布到某个环境,供调用者调用。对于不同的环境,API的版本、请求地址甚至于包括请求消息等均有可能不同。如:某个API,v1.0的版本为稳定版本,发布到了生产环境供生产使用,同时,该API正处于迭代中,v1.1的版本是开发人员交付测试人员进行测试的版本,发布在测试环境上,而v1.2的版本目前开发团队正处于开发过程中,可以发布到开发环境进行自测等。 | To be tested |
|  | ListEnvironments | 查询符合条件的环境列表。 | To be tested |
| 共享版-签名密钥管理 | CreateSignatureKey | 为了保护API的安全性,建议租户为API的访问提供一套保护机制,即租户开放的API,需要对请求来源进行认证,不符合认证的请求直接拒绝访问。 其中,签名密钥就是API安全保护机制的一种。 租户创建一个签名密钥,并将签名密钥与API进行绑定,则API网关在请求这个API时,就会使用绑定的签名密钥对请求参数进行数据加密,生成签名。当租户的后端服务收到请求时,可以校验这个签名,如果签名校验不通过,则该请求不是API网关发出的请求,租户可以拒绝这个请求,从而保证API的安全性,避免API被未知来源的请求攻击。 | To be tested |
|  | UpdateSignatureKey | 修改指定签名密钥的详细信息。 | To be tested |
|  | DeleteSignatureKey | 删除指定的签名密钥,删除签名密钥时,其配置的绑定关系会一并删除,相应的签名密钥会失效。 | To be tested |
|  | ListSignatureKeys | 查询所有签名密钥的信息。 | To be tested |
| 共享版-签名密钥绑定关系管理 | ListSignatureKeysBoundtoAnAPI | 查询某个API绑定的签名密钥列表。每个API在每个环境上应该最多只会绑定一个签名密钥。 | To be tested |
|  | DisassociateSignatureKey | 解除API与签名密钥的绑定关系。 | To be tested |
|  | ListApisBoundWithSignatureKey | 查询某个签名密钥上已经绑定的API列表。 | To be tested |
|  | AssociateSignatureKey | 签名密钥创建后,需要绑定到API才能生效。将签名密钥绑定到API后,则API网关请求后端服务时就会使用这个签名密钥进行加密签名,后端服务可以校验这个签名来验证请求来源。 将指定的签名密钥绑定到一个或多个已发布的API上。 同一个API发布到不同的环境可以绑定不同的签名密钥;一个API在发布到特定环境后只能绑定一个签名密钥。 | To be tested |
|  | ListApisNotBoundWithSignatureKey | 查询所有未绑定到该签名密钥上的API列表。需要API已经发布,未发布的API不予展示。 | To be tested |
| 共享版-设置特殊流控 | UpdateSpecialThrottlingConfiguration | 修改某个流控策略下的某个特殊设置。 | To be tested |
|  | ListSpecialThrottlingConfigurations | 查看给流控策略设置的特殊配置。 | To be tested |
|  | CreateSpecialThrottlingConfiguration | 流控策略可以限制一段时间内可以访问API的最大次数,也可以限制一段时间内单个租户和单个APP可以访问API的最大次数。 如果想要对某个特定的APP进行特殊设置,例如设置所有APP每分钟的访问次数为500次,但想设置APP1每分钟的访问次数为800次,可以通过在流控策略中设置特殊APP来实现该功能。 为流控策略添加一个特殊设置的对象,可以是APP,也可以是租户。 | To be tested |
|  | DeleteSpecialThrottlingConfiguration | 删除某个流控策略的某个特殊配置。 | To be tested |
