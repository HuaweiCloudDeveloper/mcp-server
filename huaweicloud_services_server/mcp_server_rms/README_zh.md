# RMS MCP Server 

## 版本信息
v0.1.0

## 产品描述

RMS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务RMS交互的能力。可以基于自然语言对RMS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Aggregator | ShowAggregatePolicyStateComplianceSummary | 查询聚合器中一个或多个帐户的合规和不合规规则数。 | To be tested |
|  | DeleteConfigurationAggregator | 删除资源聚合器。 | To be tested |
|  | RunAggregateResourceQuery | 对指定聚合器执行高级查询。 | To be tested |
|  | ShowAggregatePolicyAssignmentDetail | 返回指定聚合合规规则详情。 | To be tested |
|  | CreateConfigurationAggregator | 创建资源聚合器。 | To be tested |
|  | ShowAggregateResourceConfig | 查询源帐号中特定资源的详情。 | To be tested |
|  | CreateAggregationAuthorization | 给资源聚合器帐号授予从源帐号收集数据的权限。 | To be tested |
|  | ListConfigurationAggregators | 查询资源聚合器列表。 | To be tested |
|  | ShowAggregateComplianceDetailsByPolicyAssignment | 返回指定聚合合规规则的评估结果详情。包含评估了哪些资源,以及每个资源是否符合规则。 | To be tested |
|  | DeleteAggregationAuthorization | 删除指定资源聚合器帐号的授权。 | To be tested |
|  | ListAggregationAuthorizations | 查询授权过的资源聚合器列表。 | To be tested |
|  | ListAggregateComplianceByPolicyAssignment | 查询合规和不合规规则的列表,其中包含合规和不合规规则的资源数量。 | To be tested |
|  | ListPendingAggregationRequests | 查询所有挂起的聚合请求列表。 | To be tested |
|  | ListAggregateDiscoveredResources | 查询资源聚合器中特定资源的列表。 | To be tested |
|  | ShowConfigurationAggregatorSourcesStatus | 查询指定资源聚合器聚合帐号的状态信息,状态包括验证源帐号和聚合器帐号之间授权的信息。如果失败,状态包含相关的错误码或消息。 | To be tested |
|  | ShowAggregateDiscoveredResourceCounts | 查询聚合器中帐号资源的计数,支持通过过滤器和GroupByKey来统计资源数量。 | To be tested |
|  | DeletePendingAggregationRequest | 删除聚合器帐号中挂起的授权请求。 | To be tested |
|  | ShowConfigurationAggregator | 查询指定资源聚合器。 | To be tested |
|  | UpdateConfigurationAggregator | 更新资源聚合器。 | To be tested |
| History | ShowResourceHistory | 查询资源与资源关系的变更历史 | To be tested |
| Policy | DeletePolicyAssignment | 根据规则ID删除此规则 | To be tested |
|  | ListPolicyStatesByDomainId | 查询用户所有的合规结果 | To be tested |
|  | DeleteOrganizationPolicyAssignment | 删除组织合规规则。 | To be tested |
|  | CreatePolicyAssignments | 创建新的合规规则 | To be tested |
|  | ShowBuiltInPolicyDefinition | 根据策略ID查询单个内置策略 | To be tested |
|  | UpdatePolicyState | 更新用户自定义合规规则的合规评估结果 | To be tested |
|  | ListPolicyAssignments | 列出用户的合规规则 | To be tested |
|  | ShowOrganizationPolicyAssignmentDetailedStatus | 查询组织内每个成员帐号合规规则部署的详细状态。 | To be tested |
|  | CreateOrganizationPolicyAssignment | 创建或更新组织合规规则,如果规则名称已存在,则为更新操作。 | To be tested |
|  | ShowEvaluationStateByAssignmentId | 根据规则ID查询此规则的评估状态 | To be tested |
|  | ListPolicyStatesByResourceId | 根据资源ID查询所有合规结果 | To be tested |
|  | EnablePolicyAssignment | 根据规则ID启用此规则 | To be tested |
|  | ListOrganizationPolicyAssignments | 查询组织合规规则列表。 | To be tested |
|  | RunEvaluationByPolicyAssignmentId | 根据规则ID评估此规则 | To be tested |
|  | DisablePolicyAssignment | 根据规则ID停用此规则 | To be tested |
|  | UpdatePolicyAssignment | 更新用户的合规规则 | To be tested |
|  | ListBuiltInPolicyDefinitions | 列出用户的内置策略 | To be tested |
|  | ListPolicyStatesByAssignmentId | 根据规则ID查询所有的合规结果 | To be tested |
|  | ShowOrganizationPolicyAssignmentStatuses | 查询组织合规规则部署状态。 | To be tested |
|  | ShowPolicyAssignment | 根据规则ID获取单个规则 | To be tested |
|  | ShowOrganizationPolicyAssignment | 查询指定组织合规规则。 | To be tested |
| Query | UpdateStoredQuery | 更新自定义查询 | To be tested |
|  | CreateStoredQuery | 创建新的高级查询 | To be tested |
|  | RunQuery | 执行高级查询 | To be tested |
|  | ShowStoredQuery | Show Resource Query Language | To be tested |
|  | DeleteStoredQuery | 删除单个高级查询 | To be tested |
|  | ListStoredQueries | 列举所有高级查询 | To be tested |
|  | ListSchemas | List Schemas | To be tested |
| Region | ListRegions | 查询用户可见的区域 | To be tested |
| Relations | ShowResourceRelationsDetail | 指定资源ID,查询该资源与其他资源的关联关系,可以指定关系方向为“in”或者“out”,需要当帐号有rms:resources:getRelation权限。 | To be tested |
|  | ShowResourceRelations | 指定资源ID,查询该资源与其他资源的关联关系,可以指定关系方向为"in" 或者"out" | To be tested |
| Resource | ListAllTags | 查询当前帐号下所有资源的标签。 | To be tested |
|  | ListProviders | 查询RMS支持的云服务、资源、区域列表 | To be tested |
|  | CountAllResources | 查询当前帐号的资源数量。 | To be tested |
|  | ShowResourceDetail | 查询当前帐号下的单个资源。 | To be tested |
|  | CollectAllResourcesSummary | 查询当前帐号的资源概览。 | To be tested |
|  | ShowResourceById | 指定资源ID,返回该资源的详细信息,需要当前用户有rms:resources:get权限。比如查询云服务器,对应的RMS资源类型是ecs.cloudservers,其中provider为ecs,type为cloudservers。RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。 | To be tested |
|  | ListResources | 返回当前租户下特定资源类型的资源,需要当前用户有rms:resources:list权限。比如查询云服务器,对应的RMS资源类型是ecs.cloudservers,其中provider为ecs,type为cloudservers。 RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。 | To be tested |
|  | ListAllResources | 返回当前用户下所有资源,需要当前用户有rms:resources:list权限。 | To be tested |
| Tracker | DeleteTrackerConfig | 删除资源记录器 | To be tested |
|  | CreateTrackerConfig | 创建或更新资源记录器,只能存在一个资源记录器 | To be tested |
|  | ShowTrackerConfig | 查询资源记录器的详细信息 | To be tested |
