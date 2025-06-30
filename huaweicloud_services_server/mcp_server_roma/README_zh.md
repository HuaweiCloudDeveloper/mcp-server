# ROMA MCP Server 


## Version
v0.1.0

## Overview

ROMA MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ROMA. Full-chain management of ROMA resources can be carried out based on natural language.

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
                    <td rowspan="6">ACL策略管理</td>
                    <td>UpdateAclStrategyV2</td>
                    <td>修改指定的ACL策略,其中可修改的属性为:acl_name、acl_type、acl_value,其它属性不可修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAclV2</td>
                    <td>删除指定的ACL策略, 如果存在api与该ACL策略的绑定关系,则无法删除</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAclStrategyV2</td>
                    <td>增加一个ACL策略,策略类型通过字段acl_type来确定(permit或者deny),限制的对象的类型可以为IP或者DOMAIN,这里的DOMAIN对应的acl_value的值为租户名称,而非“www.exampleDomain.com"之类的网络域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAclV2</td>
                    <td>批量删除指定的多个ACL策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAclPolicyV2</td>
                    <td>查询指定ACL策略的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAclStrategiesV2</td>
                    <td>查询所有的ACL策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">API分组管理</td>
                    <td>ShowDetailsOfApiGroupV2</td>
                    <td>查询指定分组的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiGroupV2</td>
                    <td>删除指定的API分组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckApiGroupsV2</td>
                    <td>校验API分组名称是否存在。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApiGroupV2</td>
                    <td>修改API分组属性。其中name和remark可修改,其他属性不可修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApiGroupV2</td>
                    <td>API分组是API的管理单元,一个API分组等同于一个服务入口,创建API分组时,返回一个子域名作为访问入口。建议一个API分组下的API具有一定的相关性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiGroupsV2</td>
                    <td>查询API分组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">API管理</td>
                    <td>DeleteApiV2</td>
                    <td>删除指定的API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisV2</td>
                    <td>查看API列表,返回API详细信息、发布信息等,但不能查看到后端服务信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrDeletePublishRecordForApiV2</td>
                    <td>对API进行发布或下线。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersionDetailV2</td>
                    <td>查询某个指定的版本详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeApiVersionV2</td>
                    <td>API每次发布时,会基于当前的API定义生成一个版本。版本记录了API发布时的各种定义及状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersionsV2</td>
                    <td>查询某个API的历史版本。每个API在一个环境上最多存在10个历史版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DebugApiV2</td>
                    <td>调试一个API在指定运行环境下的定义,接口调用者需要具有操作该API的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchPublishOrOfflineApiV2</td>
                    <td>将多个API发布到一个指定的环境,或将多个API从指定的环境下线。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfApiV2</td>
                    <td>查看指定的API的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiRuntimeDefinitionV2</td>
                    <td>查看指定的API在指定的环境上的运行时定义,默认查询RELEASE环境上的运行时定义。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApiV2</td>
                    <td>修改指定API的信息,包括后端服务信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckApisV2</td>
                    <td>校验API定义。校验API的路径或名称是否已存在</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApiV2</td>
                    <td>添加一个API,API即一个服务接口,具体的服务能力。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiByVersionIdV2</td>
                    <td>对某个生效中的API版本进行下线操作,下线后,API在该版本生效的环境中将不再能够被调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">API绑定ACL策略</td>
                    <td>CreateApiAclBindingV2</td>
                    <td>将API与ACL策略进行绑定。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiAclBindingV2</td>
                    <td>解除某条API与ACL策略的绑定关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteApiAclBindingV2</td>
                    <td>批量解除API与ACL策略的绑定</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisUnbindedToAclPolicyV2</td>
                    <td>查看ACL策略未绑定的API列表,需要API已发布</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToAclPolicyV2</td>
                    <td>查看ACL策略绑定的API列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAclPolicyBindedToApiV2</td>
                    <td>查看API绑定的ACL策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">API绑定流控策略</td>
                    <td>DisassociateRequestThrottlingPolicyV2</td>
                    <td>解除API与流控策略的绑定关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRequestThrottlingPoliciesBindedToApiV2</td>
                    <td>查询某个API绑定的流控策略列表。每个环境上应该最多只有一个流控策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRequestThrottlingPolicyV2</td>
                    <td>将流控策略应用于API,则所有对该API的访问将会受到该流控策略的限制。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisUnbindedToRequestThrottlingPolicyV2</td>
                    <td>查询所有未绑定到该流控策略上的自有API列表。需要API已经发布,未发布的API不予展示。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDisassociateThrottlingPolicyV2</td>
                    <td>批量解除API与流控策略的绑定关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToRequestThrottlingPolicyV2</td>
                    <td>查询某个流控策略上已经绑定的API列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">APPLICATION_MANAGEMENT</td>
                    <td>CheckRomaAppDetails</td>
                    <td>查询应用详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddUserToApp</td>
                    <td>- 设置应用的用户成员,为空数组时会清空已有应用成员列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRomaApp</td>
                    <td>查询应用列表,支持条件查询,所有条件是并且的关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetRomaAppSecret</td>
                    <td>重置应用密钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRomaApp</td>
                    <td>删除单个应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckCanAuthUsersOfApp</td>
                    <td>查询应用的候选用户成员列表,会过滤掉异常状态用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRomaApp</td>
                    <td>创建应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateRomaApp</td>
                    <td>校验指定条件的应用是否存在</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRomaApp</td>
                    <td>更新应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckRomaAppSecret</td>
                    <td>查询应用密钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckAuthUsersOfApp</td>
                    <td>查询用户成列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">APP授权管理</td>
                    <td>ListDuplicateApisForAppV2</td>
                    <td>查询指定APP下路径冲突的api列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelingAuthorizationV2</td>
                    <td>解除API对APP的授权关系。解除授权后,APP将不再能够调用该API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisUnbindedToAppV2</td>
                    <td>查询指定环境上某个APP未绑定的API列表,包括自有API和从云市场购买的API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppsBindedToApiV2</td>
                    <td>查询API绑定的APP列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAuthorizingAppsV2</td>
                    <td>APP创建成功后,还不能访问API,如果想要访问某个环境上的API,需要将该API在该环境上授权给APP。授权成功后,APP即可访问该环境上的这个API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToAppV2</td>
                    <td>查询APP已经绑定的API列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">ASSET_MANAGEMENT</td>
                    <td>CheckAssetJobStatus</td>
                    <td>查询作业进度</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAsset</td>
                    <td>批量删除资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportAsset</td>
                    <td>- 创建导入资产作业任务,资产版本和具体哪些资产从资产内容里读取</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportAsset</td>
                    <td>批量导出资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadAssetArchive</td>
                    <td>- 导出作业执行成功后,通过该接口获取导出作业产生的资产包,仅能下载一次</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">DICTIONARY_MANAGEMENT</td>
                    <td>UpdateDictionary</td>
                    <td>更新字典</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDictionary</td>
                    <td>创建字典</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDictionary</td>
                    <td>删除单个字典,会同时删除该字典的所有子字典</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckDictionary</td>
                    <td>查询字典详情,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateDictionary</td>
                    <td>校验指定条件的字典是否存在,支持字典名称和字典编码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDictionary</td>
                    <td>查询字典列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">INSTANCE_MANAGEMENT</td>
                    <td>CheckRomaInstanceListV2</td>
                    <td>获取符合条件的服务实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ITaskController</td>
                    <td>DeleteTask</td>
                    <td>删除单个任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTasks</td>
                    <td>获取任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTask</td>
                    <td>任务修改接口,用于修改任务配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">MQS实例管理</td>
                    <td>ShowMqsInstance</td>
                    <td>查询指定MQS实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMqsInstance</td>
                    <td>查询MQS实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">OpenAPI接口</td>
                    <td>ImportLiveDataApiDefinitionsV2</td>
                    <td>导入自定义后端API。导入文件内容需要符合swagger标准规范,自定义扩展字段请参考用户指南的“附录:后端API的Swagger扩展定义”章节</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportApiDefinitionsV2</td>
                    <td>导入API。导入文件内容需要符合swagger标准规范,自定义扩展字段请参考用户指南的“附录:前端API的Swagger扩展定义”章节。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportLiveDataApiDefinitionsV2</td>
                    <td>导出自定义后端API,导出文件内容符合swagger标准规范。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportApiDefinitionsV2</td>
                    <td>导出分组下API的定义信息,导出文件内容符合swagger标准规范。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">PUBLIC_MANAGEMENT</td>
                    <td>CheckVersion</td>
                    <td>获取指定版本ID的API版本信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">SSL证书管理</td>
                    <td>BatchAssociateDomainsV2</td>
                    <td>SSL证书绑定域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCertificateV2</td>
                    <td>修改SSL证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificateV2</td>
                    <td>创建SSL证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAssociateCertsV2</td>
                    <td>域名绑定SSL证书。目前暂时仅支持单个绑定,请求体当中的certificate_ids里面有且只能有一个证书ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAttachedDomainsV2</td>
                    <td>获取SSL证书已绑定域名列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificatesV2</td>
                    <td>获取SSL证书列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDisassociateDomainsV2</td>
                    <td>SSL证书解绑域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfCertificateV2</td>
                    <td>查看证书详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCertificateV2</td>
                    <td>删除ssl证书接口,删除时只有没有关联域名的证书才能被删除</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDisassociateCertsV2</td>
                    <td>域名解绑SSL证书。目前暂时仅支持单个解绑,请求体当中的certificate_ids里面有且只能有一个证书ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">VPC通道管理</td>
                    <td>DeleteBackendInstanceV2</td>
                    <td>删除指定VPC通道中的后端实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpcChannelV2</td>
                    <td>删除指定的VPC通道</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMemberGroup</td>
                    <td>在服务集成中创建VPC通道后端服务器组,VPC通道后端实例可以选择是否关联后端实例服务器组,以便管理后端服务器节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHealthCheck</td>
                    <td>修改VPC通道健康检查。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddingBackendInstancesV2</td>
                    <td>为指定的VPC通道添加后端实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfVpcChannelV2</td>
                    <td>查看指定的VPC通道详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackendInstancesV2</td>
                    <td>查看指定VPC通道的后端实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpcChannelV2</td>
                    <td>更新指定VPC通道的参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMemberGroups</td>
                    <td>查询VPC通道后端云服务组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDisableMembers</td>
                    <td>批量修改后端服务器状态不可用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpcChannelV2</td>
                    <td>在服务集成中创建连接私有VPC资源的通道,并在创建API时将后端节点配置为使用这些VPC通道,以便服务集成直接访问私有VPC资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchEnableMembers</td>
                    <td>批量修改后端服务器状态可用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMemberGroup</td>
                    <td>更新指定VPC通道后端服务器组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfMemberGroup</td>
                    <td>查看指定的VPC通道后端服务器组详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBackendInstancesV2</td>
                    <td>更新指定的VPC通道的后端实例。更新时,使用传入的请求参数对对应云服务组的后端实例进行全量覆盖修改。若未指定修改的云服务器组,则进行全量覆盖。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcChannelsV2</td>
                    <td>查看VPC通道列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMemberGroup</td>
                    <td>删除指定的VPC通道后端服务器组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">VPC通道管理-项目级</td>
                    <td>CreateProjectVpcChannel</td>
                    <td>创建相同的VPC通道关联到多个实例。同一个项目下VPC通道名称不可重复。注意:实例特性vpc_name_modifiable配置为off时才可使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectVpcChannelsV2</td>
                    <td>查询项目下所有实例的VPC通道列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectVpcChannelSyncs</td>
                    <td>同步VPC通道到多个实例。注意:实例特性vpc_name_modifiable配置为off时才可使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProjectVpcChannel</td>
                    <td>项目下根据VPC通道名称批量修改多个多个实例下的VPC通道。若实例下不存在该VPC通道则创建。注意:实例特性vpc_name_modifiable配置为off时才可使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">主题操作</td>
                    <td>ListTopics</td>
                    <td>分页查询Topic列表,Topic列表按照Topic创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在Topic,则返回空列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">主题管理</td>
                    <td>ListMqsInstanceTopics</td>
                    <td>查询Topic列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMqsInstanceTopic</td>
                    <td>创建Topic。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteMqsInstanceTopic</td>
                    <td>批量删除Topic。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportMqsInstanceTopic</td>
                    <td>导入Topic。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMqsInstanceTopic</td>
                    <td>修改Topic。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportMqsInstanceTopic</td>
                    <td>导出Topic。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMqsInstanceTopic</td>
                    <td>删除Topic。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">产品模板</td>
                    <td>ListProductTemplates</td>
                    <td>查询产品模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProductTemplate</td>
                    <td>修改产品模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProductTemplate</td>
                    <td>创建产品模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProductTemplate</td>
                    <td>删除产品模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">产品管理</td>
                    <td>ShowProductAuthentication</td>
                    <td>查询产品鉴权信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProductTopic</td>
                    <td>添加产品主题</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProduct</td>
                    <td>修改产品信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProductTopics</td>
                    <td>查询产品主题</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProduct</td>
                    <td>查询产品详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProducts</td>
                    <td>查询产品</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevicesInProduct</td>
                    <td>查询产品内设备数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProduct</td>
                    <td>删除产品</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetProductAuthentication</td>
                    <td>重置产品鉴权信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProduct</td>
                    <td>创建产品</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProductTopic</td>
                    <td>更新产品主题</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadProduct</td>
                    <td>导入产品</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadProducts</td>
                    <td>导出产品</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProductTopic</td>
                    <td>删除产品主题</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">任务监控管理</td>
                    <td>ListMonitorLog</td>
                    <td>查询单个任务的所有日志信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMonitorInfos</td>
                    <td>查询所有任务的监控信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">任务管理</td>
                    <td>ShowDispatches</td>
                    <td>查询调度计划</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InstallMultiTasks</td>
                    <td>初始化组合任务,分配任务ID,初始化映射等</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCommonTask</td>
                    <td>创建普通任务(区别于组合任务)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDispatches</td>
                    <td>创建调度计划</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDispatches</td>
                    <td>通过任务ID和调度ID修改调度计划</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetMultiTaskOffset</td>
                    <td>重置组合任务进度</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMultiTaskMappings</td>
                    <td>创建组合任务映射</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTask</td>
                    <td>手工触发一次任务调度</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartOrStopTasks</td>
                    <td>批量启动\停止任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMultiTasks</td>
                    <td>修改组合任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountTasks</td>
                    <td>统计不同类型不同状态任务数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMultiTaskMapping</td>
                    <td>通过映射ID删除指定任务映射</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMultiTasks</td>
                    <td>创建组合任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">域名管理</td>
                    <td>UpdateDomainV2</td>
                    <td>修改绑定的域名所对应的配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateCertificateV2</td>
                    <td>如果域名证书不再需要或者已过期,则可以删除证书内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateCertificateV2</td>
                    <td>如果创建API时,“定义API请求”使用HTTPS请求协议,那么在独立域名中需要添加SSL证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfDomainNameCertificateV2</td>
                    <td>查看域名下绑定的证书详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateDomainV2</td>
                    <td>如果API分组不再需要绑定某个自定义域名,则可以为此API分组解绑此域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateDomainV2</td>
                    <td>用户自定义的域名,需要CNAME到API分组的子域名上才能生效。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">实例特性管理</td>
                    <td>CreateFeatureV2</td>
                    <td>为实例配置需要的特性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFeaturesV2</td>
                    <td>查看实例特性列表。注意:实例不支持以下特性的需要联系技术支持升级实例版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">实例管理</td>
                    <td>ShowRestrictionOfInstanceV2</td>
                    <td>查看实例约束信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfInstanceV2</td>
                    <td>查看实例详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">客户端配置</td>
                    <td>ShowAppBoundAppQuota</td>
                    <td>查看指定客户端应用关联的应用配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppAcl</td>
                    <td>查看APP的访问控制详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppCodeV2</td>
                    <td>删除App Code,App Code删除后,将无法再通过简易认证访问对应的API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppCodeAutoV2</td>
                    <td>创建App Code时,可以不指定具体值,由后台自动生成随机字符串填充。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppV2</td>
                    <td>查看指定APP的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppCodeV2</td>
                    <td>App Code为APP应用下的子模块,创建App Code之后,可以实现简易的APP认证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppAcl</td>
                    <td>设置客户端配置的访问控制。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppAcl</td>
                    <td>删除客户端配置的访问控制信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppsV2</td>
                    <td>查询APP列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppCodesV2</td>
                    <td>查询App Code列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppCodeV2</td>
                    <td>App Code为APP应用下的子模块,创建App Code之后,可以实现简易的APP认证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">客户端配额</td>
                    <td>UpdateAppQuota</td>
                    <td>修改客户端配额</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuotas</td>
                    <td>获取客户端配额列表。支持根据名称模糊查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppQuota</td>
                    <td>创建客户端配额</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuotaBindableApps</td>
                    <td>查询客户端配额可绑定的客户端应用列表。支持按客户端应用名称模糊搜索</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateAppQuotaWithApp</td>
                    <td>解除客户端配额和客户端应用的绑定</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuotaBoundApps</td>
                    <td>查询客户端配额已绑定的客户端应用列表。支持按客户端应用名称模糊匹配</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateAppsForAppQuota</td>
                    <td>客户端配额绑定客户端应用列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppQuota</td>
                    <td>获取客户端配额详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppQuota</td>
                    <td>删除客户端配额。删除客户端配额时,同时删除客户端配额和客户端应用的关联关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">应用权限管理</td>
                    <td>UpdateTopicAccessPolicy</td>
                    <td>更新Topic权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMqsInstanceTopicAccessPolicy</td>
                    <td>查询Topic权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">应用配置管理</td>
                    <td>UpdateAppConfigV2</td>
                    <td>修改应用配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppConfigV2</td>
                    <td>删除应用配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppConfigV2</td>
                    <td>创建应用配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppConfigV2</td>
                    <td>查看应用配置详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppConfigsV2</td>
                    <td>查询应用配置列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">插件管理</td>
                    <td>DeletePlugin</td>
                    <td>删除插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePlugin</td>
                    <td>修改插件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlugin</td>
                    <td>创建插件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPluginAttachedApis</td>
                    <td>查询指定插件下绑定的API信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlugins</td>
                    <td>查询一组符合条件的API网关插件详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachApiToPlugin</td>
                    <td>绑定插件到API上。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiAttachablePlugins</td>
                    <td>查询可绑定当前API的插件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachApiFromPlugin</td>
                    <td>解除绑定在插件上的API</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPluginAttachableApis</td>
                    <td>查询可绑定当前插件的API信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlugin</td>
                    <td>查询插件详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiAttachedPlugins</td>
                    <td>查询指定API下绑定的插件信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachPluginFromApi</td>
                    <td>解除绑定在API上的插件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachPluginToApi</td>
                    <td>绑定插件到API上。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">数据源管理</td>
                    <td>ListDatasourceTables</td>
                    <td>获取数据源中所有的表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatasourceInfo</td>
                    <td>创建数据源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataourceDetail</td>
                    <td>根据数据源id查询数据源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatasourceColumns</td>
                    <td>获取数据源中中某个表中所有字段</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDatasourceInfo</td>
                    <td>修改数据源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatasourceInfoById</td>
                    <td>通过数据源Id删除指定数据源信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatasources</td>
                    <td>查询数据源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartTestDatasource</td>
                    <td>测试数据源连通性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">服务作业管理</td>
                    <td>ShowTask</td>
                    <td>该接口用于查询服务作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopTask</td>
                    <td>该接口用于停止服务作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="21">服务管理</td>
                    <td>ListProperties</td>
                    <td>查询属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResponseProperty</td>
                    <td>修改响应属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateService</td>
                    <td>创建服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCommand</td>
                    <td>查询命令详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResponseProperty</td>
                    <td>查询响应属性详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResponseProperties</td>
                    <td>查询响应属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRequestProperty</td>
                    <td>创建请求属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateService</td>
                    <td>修改服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProperty</td>
                    <td>创建属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCommand</td>
                    <td>修改命令</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteService</td>
                    <td>删除服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResponseProperty</td>
                    <td>创建响应属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCommand</td>
                    <td>删除命令</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRequestProperty</td>
                    <td>修改请求属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCommand</td>
                    <td>创建命令</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRequestProperty</td>
                    <td>删除请求属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServices</td>
                    <td>查询服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowService</td>
                    <td>查询服务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCommands</td>
                    <td>查询命令</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRequestProperties</td>
                    <td>查询请求属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResponseProperty</td>
                    <td>删除响应属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询版本操作</td>
                    <td>ListVersion</td>
                    <td>查询SMN API V2版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">标签管理</td>
                    <td>ListTagsV2</td>
                    <td>查询标签列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">流控策略管理</td>
                    <td>UpdateRequestThrottlingPolicyV2</td>
                    <td>修改指定流控策略的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRequestThrottlingPolicyV2</td>
                    <td>删除指定的流控策略。当该流控策略绑定了API时,需要先解除流控策略与API的所有绑定关系后再删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfRequestThrottlingPolicyV2</td>
                    <td>查看指定流控策略的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRequestThrottlingPolicyV2</td>
                    <td>当API上线后,系统会默认给每个API提供一个流控策略,API提供者可以根据自身API的服务能力及负载情况变更这个流控策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteThrottlingPolicyV2</td>
                    <td>批量删除流控策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRequestThrottlingPolicyV2</td>
                    <td>查询所有流控策略的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">消息管理</td>
                    <td>ResetMessages</td>
                    <td>重发消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMqsInstanceMessages</td>
                    <td>查询消息的偏移量和消息内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">环境变量管理</td>
                    <td>CreateEnvironmentVariableV2</td>
                    <td>将API发布到不同的环境后,对于不同的环境,可能会有不同的环境变量,比如,API的服务部署地址,请求的版本号等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnvironmentVariableV2</td>
                    <td>删除指定的环境变量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfEnvironmentVariableV2</td>
                    <td>查看指定的环境变量的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnvironmentVariableV2</td>
                    <td>修改环境变量。环境变量引用位置为api的后端服务地址时,修改对应环境变量会将使用该变量的所有api重新发布。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvironmentVariablesV2</td>
                    <td>查询分组下的所有环境变量的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">环境管理</td>
                    <td>DeleteEnvironmentV2</td>
                    <td>删除指定的环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvironmentsV2</td>
                    <td>查询符合条件的环境列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnvironmentV2</td>
                    <td>修改指定环境的信息。其中可修改的属性为:name、remark,其它属性不可修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnvironmentV2</td>
                    <td>在实际的生产中,API提供者可能有多个环境,如开发环境、测试环境、生产环境等,用户可以自由将API发布到某个环境,供调用者调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">监控信息查询</td>
                    <td>ListLatelyApiStatisticsV2</td>
                    <td>根据API的id和最近的一段时间查询API被调用的次数,统计周期为1分钟。查询范围一小时以内,一分钟一个样本,其样本值为一分钟内的累计值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStatisticsApi</td>
                    <td>查询某个实例下的API统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">签名密钥管理</td>
                    <td>ListSignatureKeysV2</td>
                    <td>查询所有签名密钥的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSignatureKeyV2</td>
                    <td>修改指定签名密钥的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSignatureKeyV2</td>
                    <td>删除指定的签名密钥。签名密钥绑定了API时无法删除,需要先解除与API的绑定关系后删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSignatureKeyV2</td>
                    <td>为了保护API的安全性,建议租户为API的访问提供一套保护机制,即租户开放的API,需要对请求来源进行认证,不符合认证的请求直接拒绝访问。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">签名密钥绑定关系管理</td>
                    <td>DisassociateSignatureKeyV2</td>
                    <td>解除API与签名密钥的绑定关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisNotBoundWithSignatureKeyV2</td>
                    <td>查询所有未绑定到该签名密钥上的API列表。需要API已经发布,未发布的API不予展示。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToSignatureKeyV2</td>
                    <td>查询某个签名密钥上已经绑定的API列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSignatureKeysBindedToApiV2</td>
                    <td>查询某个API绑定的签名密钥列表。每个API在每个环境上应该最多只会绑定一个签名密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateSignatureKeyV2</td>
                    <td>签名密钥创建后,需要绑定到API才能生效。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">自定义后端服务</td>
                    <td>DebugLiveDataApiV2</td>
                    <td>测试后端API是否可用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishLiveDataApiV2</td>
                    <td>在某个实例中部署后端API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLiveDataApiV2</td>
                    <td>在某个实例中更新后端API的参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLiveDataDataSourcesV2</td>
                    <td>查询自定义后端服务数据源列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLiveDataApiDeploymentHistoryV2</td>
                    <td>在某个实例中查询后端API的部署记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLiveDataApiV2</td>
                    <td>在某个实例中删除后端API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckLivedataApisV2</td>
                    <td>校验自定义后端API定义。校验自定义后端API的路径或名称是否已存在</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLiveDataQuotaV2</td>
                    <td>查询自定义后端服务配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnpublishLiveDataApiV2</td>
                    <td>在某个实例中取消部署后端API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLiveDataApiScriptV2</td>
                    <td>在某个实例中创建后端API脚本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLiveDataApiV2</td>
                    <td>在某个实例中创建后端API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLiveDataApiV2</td>
                    <td>查询后端API的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLiveDataApiTestHistoryV2</td>
                    <td>在某个实例中查询后端API的测试结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLiveDataApiV2</td>
                    <td>获取某个实例下的所有后端API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">自定义认证管理</td>
                    <td>ShowDetailsOfCustomAuthorizersV2</td>
                    <td>查看自定义认证详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCustomAuthorizersV2</td>
                    <td>查询自定义认证列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCustomAuthorizerV2</td>
                    <td>创建自定义认证</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCustomAuthorizerV2</td>
                    <td>修改自定义认证</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomAuthorizerV2</td>
                    <td>删除自定义认证</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">规则引擎</td>
                    <td>CreateRule</td>
                    <td>创建规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRule</td>
                    <td>查询规则详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSources</td>
                    <td>查询源数据源列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSource</td>
                    <td>删除源数据源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteRules</td>
                    <td>批量删除规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSource</td>
                    <td>添加源数据源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRule</td>
                    <td>删除规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DebugRule</td>
                    <td>规则调试</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDestination</td>
                    <td>删除目标数据源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRule</td>
                    <td>修改规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDestinations</td>
                    <td>查询目标数据源列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDestination</td>
                    <td>添加目标数据源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRules</td>
                    <td>查询规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">订阅管理操作</td>
                    <td>ListNotification</td>
                    <td>该接口用于查询指定应用订阅管理信息的数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNotification</td>
                    <td>该接口用于修改指定的订阅管理</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNotification</td>
                    <td>该接口用于创建指定实例下对应的应用下的设备操作,订阅到指定的topic</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNotification</td>
                    <td>该接口用于删除指定订阅管理</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">设备分组管理</td>
                    <td>ShowDeviceGroupTree</td>
                    <td>查询所有设备分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceGroup</td>
                    <td>删除分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeviceGroup</td>
                    <td>获取设备分组及下一层分组信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddDeviceToGroup</td>
                    <td>批量添加设备到设备分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceFromGroup</td>
                    <td>删除设备分组内的设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeviceGroup</td>
                    <td>创建设备分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceGroup</td>
                    <td>修改设备分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">设备管理</td>
                    <td>ShowAuthentication</td>
                    <td>查询设备鉴权信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDevice</td>
                    <td>修改设备信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevices</td>
                    <td>此接口用于获取已经注册成功的GB/T28181设备列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendCommand</td>
                    <td>发送命令</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubsets</td>
                    <td>查询子设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetAuthentication</td>
                    <td>重置设备鉴权信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchFreezeDevices</td>
                    <td>设备批量下线</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddSubsetsToGateway</td>
                    <td>添加子设备到网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDevice</td>
                    <td>创建设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListShadows</td>
                    <td>查询设备影子</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDevice</td>
                    <td>查询设备详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDevice</td>
                    <td>此接口用于删除指定设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">设置特殊流控</td>
                    <td>ListSpecialThrottlingConfigurationsV2</td>
                    <td>查看给流控策略设置的特殊配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSpecialThrottlingConfigurationV2</td>
                    <td>流控策略可以限制一段时间内可以访问API的最大次数,也可以限制一段时间内单个租户和单个APP可以访问API的最大次数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSpecialThrottlingConfigurationV2</td>
                    <td>删除某个流控策略的某个特殊配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSpecialThrottlingConfigurationV2</td>
                    <td>修改某个流控策略下的某个特殊设置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配置管理</td>
                    <td>ListProjectCofigsV2</td>
                    <td>查询某个实例的租户配置列表,用户可以通过此接口查看各类型资源配置及使用情况。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
