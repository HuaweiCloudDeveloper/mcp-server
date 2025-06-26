# RMS MCP Server 


## Version
v0.1.0

## Overview

RMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RMS. Full-chain management of RMS resources can be carried out based on natural language.

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
                    <td rowspan="19">Aggregator</td>
                    <td>ShowAggregatePolicyStateComplianceSummary</td>
                    <td>查询聚合器中一个或多个帐户的合规和不合规规则数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConfigurationAggregator</td>
                    <td>删除资源聚合器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunAggregateResourceQuery</td>
                    <td>对指定聚合器执行高级查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAggregatePolicyAssignmentDetail</td>
                    <td>返回指定聚合合规规则详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConfigurationAggregator</td>
                    <td>创建资源聚合器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAggregateResourceConfig</td>
                    <td>查询源帐号中特定资源的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAggregationAuthorization</td>
                    <td>给资源聚合器帐号授予从源帐号收集数据的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurationAggregators</td>
                    <td>查询资源聚合器列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAggregateComplianceDetailsByPolicyAssignment</td>
                    <td>返回指定聚合合规规则的评估结果详情。包含评估了哪些资源,以及每个资源是否符合规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAggregationAuthorization</td>
                    <td>删除指定资源聚合器帐号的授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAggregationAuthorizations</td>
                    <td>查询授权过的资源聚合器列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAggregateComplianceByPolicyAssignment</td>
                    <td>查询合规和不合规规则的列表,其中包含合规和不合规规则的资源数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPendingAggregationRequests</td>
                    <td>查询所有挂起的聚合请求列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAggregateDiscoveredResources</td>
                    <td>查询资源聚合器中特定资源的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationAggregatorSourcesStatus</td>
                    <td>查询指定资源聚合器聚合帐号的状态信息,状态包括验证源帐号和聚合器帐号之间授权的信息。如果失败,状态包含相关的错误码或消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAggregateDiscoveredResourceCounts</td>
                    <td>查询聚合器中帐号资源的计数,支持通过过滤器和GroupByKey来统计资源数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePendingAggregationRequest</td>
                    <td>删除聚合器帐号中挂起的授权请求。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationAggregator</td>
                    <td>查询指定资源聚合器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfigurationAggregator</td>
                    <td>更新资源聚合器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">History</td>
                    <td>ShowResourceHistory</td>
                    <td>查询资源与资源关系的变更历史</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="21">Policy</td>
                    <td>DeletePolicyAssignment</td>
                    <td>根据规则ID删除此规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyStatesByDomainId</td>
                    <td>查询用户所有的合规结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOrganizationPolicyAssignment</td>
                    <td>删除组织合规规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePolicyAssignments</td>
                    <td>创建新的合规规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBuiltInPolicyDefinition</td>
                    <td>根据策略ID查询单个内置策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicyState</td>
                    <td>更新用户自定义合规规则的合规评估结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyAssignments</td>
                    <td>列出用户的合规规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOrganizationPolicyAssignmentDetailedStatus</td>
                    <td>查询组织内每个成员帐号合规规则部署的详细状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrganizationPolicyAssignment</td>
                    <td>创建或更新组织合规规则,如果规则名称已存在,则为更新操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEvaluationStateByAssignmentId</td>
                    <td>根据规则ID查询此规则的评估状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyStatesByResourceId</td>
                    <td>根据资源ID查询所有合规结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnablePolicyAssignment</td>
                    <td>根据规则ID启用此规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOrganizationPolicyAssignments</td>
                    <td>查询组织合规规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunEvaluationByPolicyAssignmentId</td>
                    <td>根据规则ID评估此规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisablePolicyAssignment</td>
                    <td>根据规则ID停用此规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicyAssignment</td>
                    <td>更新用户的合规规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBuiltInPolicyDefinitions</td>
                    <td>列出用户的内置策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyStatesByAssignmentId</td>
                    <td>根据规则ID查询所有的合规结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOrganizationPolicyAssignmentStatuses</td>
                    <td>查询组织合规规则部署状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPolicyAssignment</td>
                    <td>根据规则ID获取单个规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOrganizationPolicyAssignment</td>
                    <td>查询指定组织合规规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Query</td>
                    <td>UpdateStoredQuery</td>
                    <td>更新自定义查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStoredQuery</td>
                    <td>创建新的高级查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunQuery</td>
                    <td>执行高级查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStoredQuery</td>
                    <td>Show Resource Query Language</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStoredQuery</td>
                    <td>删除单个高级查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStoredQueries</td>
                    <td>列举所有高级查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSchemas</td>
                    <td>List Schemas</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Region</td>
                    <td>ListRegions</td>
                    <td>查询用户可见的区域</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Relations</td>
                    <td>ShowResourceRelationsDetail</td>
                    <td>指定资源ID,查询该资源与其他资源的关联关系,可以指定关系方向为“in”或者“out”,需要当帐号有rms:resources:getRelation权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceRelations</td>
                    <td>指定资源ID,查询该资源与其他资源的关联关系,可以指定关系方向为"in" 或者"out"</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Resource</td>
                    <td>CountAllResources</td>
                    <td>查询当前帐号的资源数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceDetail</td>
                    <td>查询当前帐号下的单个资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectAllResourcesSummary</td>
                    <td>查询当前帐号的资源概览。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceById</td>
                    <td>指定资源ID,返回该资源的详细信息,需要当前用户有rms:resources:get权限。比如查询云服务器,对应的RMS资源类型是ecs.cloudservers,其中provider为ecs,type为cloudservers。RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResources</td>
                    <td>返回当前租户下特定资源类型的资源,需要当前用户有rms:resources:list权限。比如查询云服务器,对应的RMS资源类型是ecs.cloudservers,其中provider为ecs,type为cloudservers。 RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllResources</td>
                    <td>返回当前用户下所有资源,需要当前用户有rms:resources:list权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Tracker</td>
                    <td>DeleteTrackerConfig</td>
                    <td>删除资源记录器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrackerConfig</td>
                    <td>创建或更新资源记录器,只能存在一个资源记录器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrackerConfig</td>
                    <td>查询资源记录器的详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询标签管理支持的服务</td>
                    <td>ListProviders</td>
                    <td>查询标签管理支持的服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">证书标签管理</td>
                    <td>ListAllTags</td>
                    <td>查询所有标签列表。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
