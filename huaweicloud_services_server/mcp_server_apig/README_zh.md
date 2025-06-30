# APIG MCP Server 


## Version
v0.1.0

## Overview

APIG MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service APIG. Full-chain management of APIG resources can be carried out based on natural language.

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
                    <td>DeleteAclV2</td>
                    <td>删除指定的ACL策略, 如果存在api与该ACL策略的绑定关系,则无法删除</td>
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
                    <td>UpdateAclStrategyV2</td>
                    <td>修改指定的ACL策略,其中可修改的属性为:acl_name、acl_type、acl_value,其它属性不可修改。</td>
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
                    <td rowspan="6">API分组管理</td>
                    <td>CheckApiGroupsV2</td>
                    <td>校验API分组名称是否存在。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiGroupsV2</td>
                    <td>查询API分组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiGroupV2</td>
                    <td>删除指定的API分组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApiGroupV2</td>
                    <td>API分组是API的管理单元,一个API分组等同于一个服务入口,创建API分组时,返回一个子域名作为访问入口。建议一个API分组下的API具有一定的相关性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfApiGroupV2</td>
                    <td>查询指定分组的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApiGroupV2</td>
                    <td>修改API分组属性。其中name和remark可修改,其他属性不可修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">API管理</td>
                    <td>ListApiVersionDetailV2</td>
                    <td>查询某个指定的版本详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApiV2</td>
                    <td>添加一个API,API即一个服务接口,具体的服务能力。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiRuntimeDefinitionV2</td>
                    <td>查看指定的API在指定的环境上的运行时定义,默认查询RELEASE环境上的运行时定义。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisV2</td>
                    <td>查看API列表,返回API详细信息、发布信息等,但不能查看到后端服务信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeApiVersionV2</td>
                    <td>API每次发布时,会基于当前的API定义生成一个版本。版本记录了API发布时的各种定义及状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiByVersionIdV2</td>
                    <td>对某个生效中的API版本进行下线操作,下线后,API在该版本生效的环境中将不再能够被调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrDeletePublishRecordForApiV2</td>
                    <td>对API进行发布或下线。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersionsV2</td>
                    <td>查询某个API的历史版本。每个API在一个环境上最多存在10个历史版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchPublishOrOfflineApiV2</td>
                    <td>将多个API发布到一个指定的环境,或将多个API从指定的环境下线。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckApisV2</td>
                    <td>校验API定义。校验API的路径或名称是否已存在</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfApiV2</td>
                    <td>查看指定的API的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApiV2</td>
                    <td>修改指定API的信息,包括后端服务信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiV2</td>
                    <td>删除指定的API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DebugApiV2</td>
                    <td>调试一个API在指定运行环境下的定义,接口调用者需要具有操作该API的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">API绑定ACL策略</td>
                    <td>BatchDeleteApiAclBindingV2</td>
                    <td>批量解除API与ACL策略的绑定</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApiAclBindingV2</td>
                    <td>将API与ACL策略进行绑定。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToAclPolicyV2</td>
                    <td>查看ACL策略绑定的API列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisUnbindedToAclPolicyV2</td>
                    <td>查看ACL策略未绑定的API列表,需要API已发布</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAclPolicyBindedToApiV2</td>
                    <td>查看API绑定的ACL策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiAclBindingV2</td>
                    <td>解除某条API与ACL策略的绑定关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">API绑定流控策略</td>
                    <td>BatchDisassociateThrottlingPolicyV2</td>
                    <td>批量解除API与流控策略的绑定关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateRequestThrottlingPolicyV2</td>
                    <td>解除API与流控策略的绑定关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToRequestThrottlingPolicyV2</td>
                    <td>查询某个流控策略上已经绑定的API列表。</td>
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
                    <td rowspan="5">APP授权管理</td>
                    <td>ListApisBindedToAppV2</td>
                    <td>查询APP已经绑定的API列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisUnbindedToAppV2</td>
                    <td>查询指定环境上某个APP未绑定的API列表,包括自有API和从云市场购买的API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAuthorizingAppsV2</td>
                    <td>APP创建成功后,还不能访问API,如果想要访问某个环境上的API,需要将该API在该环境上授权给APP。授权成功后,APP即可访问该环境上的这个API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelingAuthorizationV2</td>
                    <td>解除API对APP的授权关系。解除授权后,APP将不再能够调用该API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppsBindedToApiV2</td>
                    <td>查询API绑定的APP列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">OpenAPI接口</td>
                    <td>ExportApiDefinitionsV2</td>
                    <td>导出分组下API的定义信息,导出文件内容符合swagger标准规范。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportApiDefinitionsV2</td>
                    <td>导入API。导入文件内容需要符合swagger标准规范,自定义扩展字段请参考用户指南的“附录:前端API的Swagger扩展定义”章节。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">SSL证书管理</td>
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
                    <td>BatchAssociateCertsV2</td>
                    <td>域名绑定SSL证书。目前暂时仅支持单个绑定,请求体当中的certificate_ids里面有且只能有一个证书ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificatesV2</td>
                    <td>获取SSL证书列表。</td>
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
                    <td>ListAttachedDomainsV2</td>
                    <td>获取SSL证书已绑定域名列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAssociateDomainsV2</td>
                    <td>SSL证书绑定域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">VPC通道管理</td>
                    <td>DeleteVpcChannelV2</td>
                    <td>删除指定的VPC通道</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHealthCheck</td>
                    <td>修改VPC通道健康检查。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMemberGroup</td>
                    <td>在服务集成中创建VPC通道后端服务器组,VPC通道后端实例可以选择是否关联后端实例服务器组,以便管理后端服务器节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDisableMembers</td>
                    <td>批量修改后端服务器状态不可用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfMemberGroup</td>
                    <td>查看指定的VPC通道后端服务器组详情</td>
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
                    <td>BatchEnableMembers</td>
                    <td>批量修改后端服务器状态可用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpcChannelV2</td>
                    <td>在服务集成中创建连接私有VPC资源的通道,并在创建API时将后端节点配置为使用这些VPC通道,以便服务集成直接访问私有VPC资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBackendInstancesV2</td>
                    <td>更新指定的VPC通道的后端实例。更新时,使用传入的请求参数对对应云服务组的后端实例进行全量覆盖修改。若未指定修改的云服务器组,则进行全量覆盖。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMemberGroup</td>
                    <td>更新指定VPC通道后端服务器组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfVpcChannelV2</td>
                    <td>查看指定的VPC通道详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddingBackendInstancesV2</td>
                    <td>为指定的VPC通道添加后端实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMemberGroup</td>
                    <td>删除指定的VPC通道后端服务器组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcChannelsV2</td>
                    <td>查看VPC通道列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackendInstanceV2</td>
                    <td>删除指定VPC通道中的后端实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackendInstancesV2</td>
                    <td>查看指定VPC通道的后端实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">environment-controller-v2</td>
                    <td>DeleteEnvironment</td>
                    <td>删除应用下的环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnvironment</td>
                    <td>应用下编辑环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnvironment</td>
                    <td>应用下创建环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvironments</td>
                    <td>查询应用下环境列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">专享版-凭据管理</td>
                    <td>DeleteAppV2</td>
                    <td>删除指定的APP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAnAppV2</td>
                    <td>APP即应用,是一个可以访问API的身份标识。将API授权给APP后,APP即可调用API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResettingAppSecretV2</td>
                    <td>重置指定APP的密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppV2</td>
                    <td>修改指定APP的信息。其中可修改的属性为:name、remark,当支持用户自定义key和secret的开关开启时,app_key和app_secret也支持修改,其它属性不可修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckAppV2</td>
                    <td>校验app是否存在,非APP所有者可以调用该接口校验APP是否真实存在。这个接口只展示app的基本信息id 、name、</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">专享版-分组自定义响应管理</td>
                    <td>UpdateGatewayResponseTypeV2</td>
                    <td>修改分组下指定错误类型的自定义响应。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGatewayResponsesV2</td>
                    <td>查询分组自定义响应列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGatewayResponseV2</td>
                    <td>删除分组自定义响应</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfGatewayResponseTypeV2</td>
                    <td>查看分组下指定错误类型的自定义响应</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGatewayResponseTypeV2</td>
                    <td>删除分组指定错误类型的自定义响应配置,还原为使用默认值的配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGatewayResponseV2</td>
                    <td>新增分组下自定义响应</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfGatewayResponseV2</td>
                    <td>查询分组自定义响应详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGatewayResponseV2</td>
                    <td>修改分组自定义响应</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">专享版-域名管理</td>
                    <td>UpdateSlDomainSettingV2</td>
                    <td>禁用或启用API分组绑定的调试域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">专享版-实例标签管理</td>
                    <td>BatchCreateOrDeleteInstanceTags</td>
                    <td>批量添加或删除单个实例的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectInstanceTags</td>
                    <td>查询项目下所有实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstancesNumByTags</td>
                    <td>查询包含指定标签的实例数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">专享版-实例特性管理</td>
                    <td>ListInstanceFeatures</td>
                    <td>查询实例支持的特性列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">专享版-实例管理</td>
                    <td>CreatePrepayResize</td>
                    <td>创建包周期规格变更订单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIngressEipV2</td>
                    <td>更新实例入公网带宽,仅当实例为ELB类型时支持</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddEngressEipV2</td>
                    <td>实例开启公网出口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstancesV2</td>
                    <td>删除专享版实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceV2</td>
                    <td>创建按需专享版实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesV2</td>
                    <td>查询专享版实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostPayResizeOrder</td>
                    <td>创建按需规格变更订单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfInstanceProgressV2</td>
                    <td>查看专享版实例创建进度</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableZonesV2</td>
                    <td>查看可用区信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrder</td>
                    <td>创建包周期专享版实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveIngressEipV2</td>
                    <td>关闭实例公网入口,仅当实例为ELB类型时支持</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddEipV2</td>
                    <td>实例更新或绑定EIP(仅当实例为LVS类型时支持)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveEipV2</td>
                    <td>实例解绑EIP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveEngressEipV2</td>
                    <td>关闭实例公网出口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceV2</td>
                    <td>更新专享版实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddIngressEipV2</td>
                    <td>开启实例开启公网入口,仅当实例为ELB类型时支持</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEngressEipV2</td>
                    <td>更新实例出公网带宽</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">专享版-实例终端节点管理</td>
                    <td>AcceptOrRejectEndpointConnections</td>
                    <td>接受或拒绝实例节点连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddEndpointPermissions</td>
                    <td>批量添加实例终端节点连接白名单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpointConnections</td>
                    <td>查询实例终端节点连接列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpointPermissions</td>
                    <td>查询当前实例终端节点服务的白名单列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEndpointPermissions</td>
                    <td>批量删除实例终端节点连接白名单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">专享版-实例自定义入方向端口管理</td>
                    <td>ListCustomIngressPorts</td>
                    <td>查询实例的自定义入方向端口列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddCustomIngressPort</td>
                    <td>新增实例的自定义入方向端口,在同个实例中,一个端口仅能支持一种协议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomIngressPort</td>
                    <td>删除实例指定的自定义入方向端口,不包含默认端口80和443。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCustomIngressPortDomains</td>
                    <td>查询实例指定的自定义入方向端口绑定的域名信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">专享版-异步任务管理</td>
                    <td>ShowAsyncTaskResult</td>
                    <td>获取异步任务结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportApiDefinitionsAsync</td>
                    <td>导出分组下API的定义信息。导出文件内容符合swagger标准规范,API网关自定义扩展字段请参考《API网关用户指南》的“导入导出API:扩展定义”章节。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportApiDefinitionsAsync</td>
                    <td>导入API。导入文件内容需要符合swagger标准规范,API网关自定义扩展字段请参考《API网关用户指南》的“导入导出API:扩展定义”章节。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">专享版-微服务中心管理</td>
                    <td>ImportMicroservice</td>
                    <td>导入微服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">专享版-概要查询</td>
                    <td>ListApiGroupsQuantitiesV2</td>
                    <td>查询租户名下的API分组概况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiQuantitiesV2</td>
                    <td>查询租户名下的API概况:已发布到RELEASE环境的API个数,未发布到RELEASE环境的API个数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuantitiesV2</td>
                    <td>查询租户名下的APP概况:已进行API访问授权的APP个数,未进行API访问授权的APP个数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">专享版-监控信息查询</td>
                    <td>ListLatelyGroupStatisticsV2</td>
                    <td>根据API分组的编号查询该分组下所有API被调用的总次数,统计周期为1分钟。查询范围一小时以内,一分钟一个样本,其样本值为一分钟内的累计值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetricData</td>
                    <td>查询指定时间范围指定指标的指定粒度的监控数据,可以通过参数指定需要查询的数据维度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">专享版-编排规则管理</td>
                    <td>ShowDetailsOfOrchestration</td>
                    <td>查询编排规则详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOrchestration</td>
                    <td>删除编排规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOrchestrationAttachedApis</td>
                    <td>查询指定插件下绑定的API信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOrchestration</td>
                    <td>更新编排规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOrchestrations</td>
                    <td>查看编排规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrchestration</td>
                    <td>创建编排规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">专享版-配置管理</td>
                    <td>ListInstanceConfigsV2</td>
                    <td>查询租户实例配置列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">共享版-API分组管理</td>
                    <td>DeleteApiGroup</td>
                    <td>删除指定的API分组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiGroups</td>
                    <td>查询API分组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApiGroup</td>
                    <td>API分组是API的管理单元,一个API分组等同于一个服务入口,创建API分组时,返回一个子域名作为访问入口。建议一个API分组下的API具有一定的相关性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAPIGroup</td>
                    <td>修改API分组属性。其中name和remark可修改,其他属性不可修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfApiGroup</td>
                    <td>查询指定分组的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">共享版-API管理</td>
                    <td>UpdateApi</td>
                    <td>修改指定API的信息,包括后端服务信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfApi</td>
                    <td>查看指定的API的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApi</td>
                    <td>删除指定的API 删除API时,会删除该API所有相关的资源信息或绑定关系,如API的发布记录,绑定的后端服务,对APP的授权信息等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApis</td>
                    <td>查看API列表,返回API详细信息、发布信息等,但不能查看到后端服务信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApi</td>
                    <td>添加一个API,API即一个服务接口,具体的服务能力。API分为两部分,第一部分为面向API使用者的API接口,定义了使用者如何调用这个API。第二部分面向API提供者,由API提供者定义这个API的真实的后端情况,定义了API网关如何去访问真实的后端服务。API的真实后端服务目前支持三种类型:传统的HTTP/HTTPS形式的web后端、函数工作流、MOCK。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">共享版-API绑定流控策略</td>
                    <td>ListRequestThrottlingPoliciesThatBoundToAnApi</td>
                    <td>查询某个API绑定的流控策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisThatNotBoundWithRequestThrottlingPolicy</td>
                    <td>查询所有未绑定到该流控策略上的自有API列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateRequestThrottlingPolicy</td>
                    <td>解除API与流控策略的绑定关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisThatBoundWithRequestThrottlingPolicy</td>
                    <td>查询某个流控策略上已经绑定的API列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRequestThrottlingPolicy</td>
                    <td>将流控策略应用于API,则所有对该API的访问将会受到该流控策略的限制。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">共享版-APP授权管理</td>
                    <td>CreateAuthorizingApps</td>
                    <td>APP创建成功后,还不能访问API,如果想要访问某个环境上的API,需要将该API在该环境上授权给APP。授权成功后,APP即可访问该环境上的这个API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelingAuthorization</td>
                    <td>解除API对APP的授权关系。解除授权后,APP将不再能够调用该API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisThatNotBoundWithAnApp</td>
                    <td>查询指定环境上某个APP未绑定的API列表,包括自有API和从云市场购买的API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAPIsThatBoundWithAnApp</td>
                    <td>查询APP已经绑定的API列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppsBoundToAnApi</td>
                    <td>查询API绑定的APP列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">共享版-APP管理</td>
                    <td>UpdateAnApp</td>
                    <td>修改指定APP的信息。其中可修改的属性为:name、remark,当支持用户自定义key和secret的开关开启时,app_key和app_secret也支持修改,其它属性不可修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckAnApp</td>
                    <td>校验app是否存在,非APP所有者可以调用该接口校验APP是否真实存在。这个接口只展示app的基本信息id 、name、 remark,其他信息不显示。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppDetails</td>
                    <td>查看指定APP的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAnApp</td>
                    <td>APP即应用,是一个可以访问API的身份标识。将API授权给APP后,APP即可调用API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAnApp</td>
                    <td>删除指定的APP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResettingTheAppSecret</td>
                    <td>重置指定APP的密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">共享版-域名管理</td>
                    <td>AssociateDomain</td>
                    <td>用户自定义的域名,需要CNAME到API分组的子域名上才能生效</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfDomainNameCertificate</td>
                    <td>查看域名下绑定的证书详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateCertificate</td>
                    <td>如果创建API时,“定义API请求”使用HTTPS请求协议,那么在独立域名中需要添加SSL证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateCertificate</td>
                    <td>如果域名证书不再需要或者已过期,则可以删除证书内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateDomain</td>
                    <td>如果API分组不再需要绑定某个自定义域名,则可以为此API分组解绑此域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">共享版-概要查询</td>
                    <td>ListAppQuantities</td>
                    <td>查询租户名下的APP概况:已进行API访问授权的APP个数,未进行API访问授权的APP个数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAPIsOfAPIGroup</td>
                    <td>查询租户名下的API分组概况:上架的API分组个数,未上架的API分组个数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiQuantities</td>
                    <td>查询租户名下的API概况:已发布到RELEASE环境的API个数,未发布到RELEASE环境的API个数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">共享版-流控策略管理</td>
                    <td>DeleteRequestThrottlingPolicy</td>
                    <td>删除指定的流控策略,以及该流控策略与API的所有绑定关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTheRequestThrottlingPolicy</td>
                    <td>查询所有流控策略的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfARequestThrottlingPolicy</td>
                    <td>查看指定流控策略的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRequestThrottlingPolicy</td>
                    <td>修改指定流控策略的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRequestThrottlingPolicy</td>
                    <td>当API上线后,系统会默认给每个API提供一个流控策略,API提供者可以根据自身API的服务能力及负载情况变更这个流控策略。 流控策略即限制API在一定长度的时间内,能够允许被访问的最大次数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">共享版-环境变量管理</td>
                    <td>ListEnvironmentVariables</td>
                    <td>查询分组下的所有环境变量的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnvironmentVariable</td>
                    <td>删除指定的环境变量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnvironmentVariable</td>
                    <td>将API发布到不同的环境后,对于不同的环境,可能会有不同的环境变量,比如,API的服务部署地址,请求的版本号等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnvironmentVariableDetails</td>
                    <td>查看指定的环境变量的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">共享版-签名密钥管理</td>
                    <td>CreateSignatureKey</td>
                    <td>为了保护API的安全性,建议租户为API的访问提供一套保护机制,即租户开放的API,需要对请求来源进行认证,不符合认证的请求直接拒绝访问。 其中,签名密钥就是API安全保护机制的一种。 租户创建一个签名密钥,并将签名密钥与API进行绑定,则API网关在请求这个API时,就会使用绑定的签名密钥对请求参数进行数据加密,生成签名。当租户的后端服务收到请求时,可以校验这个签名,如果签名校验不通过,则该请求不是API网关发出的请求,租户可以拒绝这个请求,从而保证API的安全性,避免API被未知来源的请求攻击。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSignatureKey</td>
                    <td>修改指定签名密钥的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSignatureKey</td>
                    <td>删除指定的签名密钥,删除签名密钥时,其配置的绑定关系会一并删除,相应的签名密钥会失效。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSignatureKeys</td>
                    <td>查询所有签名密钥的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">共享版-签名密钥绑定关系管理</td>
                    <td>ListSignatureKeysBoundtoAnAPI</td>
                    <td>查询某个API绑定的签名密钥列表。每个API在每个环境上应该最多只会绑定一个签名密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateSignatureKey</td>
                    <td>解除API与签名密钥的绑定关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBoundWithSignatureKey</td>
                    <td>查询某个签名密钥上已经绑定的API列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateSignatureKey</td>
                    <td>签名密钥创建后,需要绑定到API才能生效。将签名密钥绑定到API后,则API网关请求后端服务时就会使用这个签名密钥进行加密签名,后端服务可以校验这个签名来验证请求来源。 将指定的签名密钥绑定到一个或多个已发布的API上。 同一个API发布到不同的环境可以绑定不同的签名密钥;一个API在发布到特定环境后只能绑定一个签名密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisNotBoundWithSignatureKey</td>
                    <td>查询所有未绑定到该签名密钥上的API列表。需要API已经发布,未发布的API不予展示。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">共享版-设置特殊流控</td>
                    <td>UpdateSpecialThrottlingConfiguration</td>
                    <td>修改某个流控策略下的某个特殊设置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSpecialThrottlingConfigurations</td>
                    <td>查看给流控策略设置的特殊配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSpecialThrottlingConfiguration</td>
                    <td>流控策略可以限制一段时间内可以访问API的最大次数,也可以限制一段时间内单个租户和单个APP可以访问API的最大次数。 如果想要对某个特定的APP进行特殊设置,例如设置所有APP每分钟的访问次数为500次,但想设置APP1每分钟的访问次数为800次,可以通过在流控策略中设置特殊APP来实现该功能。 为流控策略添加一个特殊设置的对象,可以是APP,也可以是租户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSpecialThrottlingConfiguration</td>
                    <td>删除某个流控策略的某个特殊配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">域名管理</td>
                    <td>UpdateDomainV2</td>
                    <td>修改绑定的域名所对应的配置信息。</td>
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
                    <td>AssociateCertificateV2</td>
                    <td>如果创建API时,“定义API请求”使用HTTPS请求协议,那么在独立域名中需要添加SSL证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateCertificateV2</td>
                    <td>如果域名证书不再需要或者已过期,则可以删除证书内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateDomainV2</td>
                    <td>用户自定义的域名,需要CNAME到API分组的子域名上才能生效。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">实例特性管理</td>
                    <td>ListFeaturesV2</td>
                    <td>查看实例特性列表。注意:实例不支持以下特性的需要联系技术支持升级实例版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFeatureV2</td>
                    <td>为实例配置需要的特性。</td>
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
                    <td>DeleteAppCodeV2</td>
                    <td>删除App Code,App Code删除后,将无法再通过简易认证访问对应的API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppCodeV2</td>
                    <td>App Code为APP应用下的子模块,创建App Code之后,可以实现简易的APP认证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppsV2</td>
                    <td>查询APP列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppAcl</td>
                    <td>设置客户端配置的访问控制。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppCodeV2</td>
                    <td>App Code为APP应用下的子模块,创建App Code之后,可以实现简易的APP认证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppAcl</td>
                    <td>删除客户端配置的访问控制信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppV2</td>
                    <td>查看指定APP的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppBoundAppQuota</td>
                    <td>查看指定客户端应用关联的应用配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppCodeAutoV2</td>
                    <td>创建App Code时,可以不指定具体值,由后台自动生成随机字符串填充。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppCodesV2</td>
                    <td>查询App Code列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppAcl</td>
                    <td>查看APP的访问控制详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">客户端配额</td>
                    <td>ShowAppQuota</td>
                    <td>获取客户端配额详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuotaBindableApps</td>
                    <td>查询客户端配额可绑定的客户端应用列表。支持按客户端应用名称模糊搜索</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuotas</td>
                    <td>获取客户端配额列表。支持根据名称模糊查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppQuota</td>
                    <td>修改客户端配额</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuotaBoundApps</td>
                    <td>查询客户端配额已绑定的客户端应用列表。支持按客户端应用名称模糊匹配</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppQuota</td>
                    <td>创建客户端配额</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateAppQuotaWithApp</td>
                    <td>解除客户端配额和客户端应用的绑定</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateAppsForAppQuota</td>
                    <td>客户端配额绑定客户端应用列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppQuota</td>
                    <td>删除客户端配额。删除客户端配额时,同时删除客户端配额和客户端应用的关联关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">应用模板管理</td>
                    <td>ListApps</td>
                    <td>查询应用模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">插件管理</td>
                    <td>CreatePlugin</td>
                    <td>创建插件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachApiFromPlugin</td>
                    <td>解除绑定在插件上的API</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlugins</td>
                    <td>查询一组符合条件的API网关插件详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlugin</td>
                    <td>查询插件详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachPluginFromApi</td>
                    <td>解除绑定在API上的插件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePlugin</td>
                    <td>修改插件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiAttachedPlugins</td>
                    <td>查询指定API下绑定的插件信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePlugin</td>
                    <td>删除插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiAttachablePlugins</td>
                    <td>查询可绑定当前API的插件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPluginAttachableApis</td>
                    <td>查询可绑定当前插件的API信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPluginAttachedApis</td>
                    <td>查询指定插件下绑定的API信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachPluginToApi</td>
                    <td>绑定插件到API上。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachApiToPlugin</td>
                    <td>绑定插件到API上。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">标签管理</td>
                    <td>ListInstanceTags</td>
                    <td>查询实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagsV2</td>
                    <td>查询标签列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesByTags</td>
                    <td>根据标签查询指定的数据库实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">流控策略管理</td>
                    <td>ListRequestThrottlingPolicyV2</td>
                    <td>查询所有流控策略的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRequestThrottlingPolicyV2</td>
                    <td>修改指定流控策略的详细信息。</td>
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
                    <td>DeleteRequestThrottlingPolicyV2</td>
                    <td>删除指定的流控策略。当该流控策略绑定了API时,需要先解除流控策略与API的所有绑定关系后再删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">环境变量管理</td>
                    <td>CreateEnvironmentVariableV2</td>
                    <td>将API发布到不同的环境后,对于不同的环境,可能会有不同的环境变量,比如,API的服务部署地址,请求的版本号等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfEnvironmentVariableV2</td>
                    <td>查看指定的环境变量的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnvironmentVariableV2</td>
                    <td>删除指定的环境变量。</td>
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
                    <td rowspan="1">监控信息查询</td>
                    <td>ListLatelyApiStatisticsV2</td>
                    <td>根据API的id和最近的一段时间查询API被调用的次数,统计周期为1分钟。查询范围一小时以内,一分钟一个样本,其样本值为一分钟内的累计值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">签名密钥管理</td>
                    <td>UpdateSignatureKeyV2</td>
                    <td>修改指定签名密钥的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSignatureKeyV2</td>
                    <td>为了保护API的安全性,建议租户为API的访问提供一套保护机制,即租户开放的API,需要对请求来源进行认证,不符合认证的请求直接拒绝访问。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSignatureKeyV2</td>
                    <td>删除指定的签名密钥。签名密钥绑定了API时无法删除,需要先解除与API的绑定关系后删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSignatureKeysV2</td>
                    <td>查询所有签名密钥的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">签名密钥绑定关系管理</td>
                    <td>AssociateSignatureKeyV2</td>
                    <td>签名密钥创建后,需要绑定到API才能生效。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSignatureKeysBindedToApiV2</td>
                    <td>查询某个API绑定的签名密钥列表。每个API在每个环境上应该最多只会绑定一个签名密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateSignatureKeyV2</td>
                    <td>解除API与签名密钥的绑定关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToSignatureKeyV2</td>
                    <td>查询某个签名密钥上已经绑定的API列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisNotBoundWithSignatureKeyV2</td>
                    <td>查询所有未绑定到该签名密钥上的API列表。需要API已经发布,未发布的API不予展示。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">自定义认证管理</td>
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
                    <td>ShowDetailsOfCustomAuthorizersV2</td>
                    <td>查看自定义认证详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomAuthorizerV2</td>
                    <td>删除自定义认证</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCustomAuthorizersV2</td>
                    <td>查询自定义认证列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">设置特殊流控</td>
                    <td>ListSpecialThrottlingConfigurationsV2</td>
                    <td>查看给流控策略设置的特殊配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSpecialThrottlingConfigurationV2</td>
                    <td>删除某个流控策略的某个特殊配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSpecialThrottlingConfigurationV2</td>
                    <td>流控策略可以限制一段时间内可以访问API的最大次数,也可以限制一段时间内单个租户和单个APP可以访问API的最大次数。</td>
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
