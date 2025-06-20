# RMS MCP Server 


## Version
v0.1.0

## Overview

RMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RMS. Full-chain management of RMS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Aggregator | ShowAggregatePolicyStateComplianceSummary | Query the number of compliant and noncompliant rules for one or more accounts in the aggregator. | To be tested |
|  | DeleteConfigurationAggregator | Deletes a resource aggregator. | To be tested |
|  | RunAggregateResourceQuery | Performs advanced query on the specified aggregator. | To be tested |
|  | ShowAggregatePolicyAssignmentDetail | This API is used to return the details about the specified aggregation compliance rule. | To be tested |
|  | CreateConfigurationAggregator | Create a resource aggregator. | To be tested |
|  | ShowAggregateResourceConfig | Query details about a specific resource in the source account. | To be tested |
|  | CreateAggregationAuthorization | Give the resource aggregator account the permission to collect data from the source account. | To be tested |
|  | ListConfigurationAggregators | Query the resource aggregator list. | To be tested |
|  | ShowAggregateComplianceDetailsByPolicyAssignment | Returns the evaluation result details of the specified aggregation compliance rule. Includes which resources were evaluated and whether each resource met the rules. | To be tested |
|  | DeleteAggregationAuthorization | Deletes the authorization for a specified resource aggregator account. | To be tested |
|  | ListAggregationAuthorizations | Query the list of authorized resource aggregators. | To be tested |
|  | ListAggregateComplianceByPolicyAssignment | Query the list of compliance and non-compliance rules, including the number of resources in compliance and non-compliance rules. | To be tested |
|  | ListPendingAggregationRequests | Query the list of all suspended aggregation requests. | To be tested |
|  | ListAggregateDiscoveredResources | Query the list of specific resources in the resource aggregator. | To be tested |
|  | ShowConfigurationAggregatorSourcesStatus | Query the status information about the aggregation account of a specified resource aggregator. The status includes the authorization information between the source account and the aggregator account. If it fails, the status contains the relevant error code or message. | To be tested |
|  | ShowAggregateDiscoveredResourceCounts | Query the number of account resources in the aggregator. The number of resources can be calculated by filter and GroupByKey. | To be tested |
|  | DeletePendingAggregationRequest | Delete the suspended authorization request from the aggregator account. | To be tested |
|  | ShowConfigurationAggregator | Query the specified resource aggregator. | To be tested |
|  | UpdateConfigurationAggregator | Updates the resource aggregator. | To be tested |
| Certificate Label Management | ListAllTags | Query the list of all tags. | To be tested |
| History | ShowResourceHistory | Query the change history of resources and resource relationships | To be tested |
| Policy | DeletePolicyAssignment | Delete the rule based on the rule ID. | To be tested |
|  | ListPolicyStatesByDomainId | Query all compliance results of a user | To be tested |
|  | DeleteOrganizationPolicyAssignment | Delete an organization compliance rule. | To be tested |
|  | CreatePolicyAssignments | Create a new compliance rule | To be tested |
|  | ShowBuiltInPolicyDefinition | Query a single built-in policy by policy ID | To be tested |
|  | UpdatePolicyState | Update the compliance evaluation result of the user-defined compliance rule | To be tested |
|  | ListPolicyAssignments | List the user's compliance rules | To be tested |
|  | ShowOrganizationPolicyAssignmentDetailedStatus | Query the detailed deployment status of compliance rules for each member account in an organization. | To be tested |
|  | CreateOrganizationPolicyAssignment | Create or update an organization compliance rule. If the rule name already exists, the operation is an update operation. | To be tested |
|  | ShowEvaluationStateByAssignmentId | Query the evaluation status of a rule based on the rule ID. | To be tested |
|  | ListPolicyStatesByResourceId | Query all compliance results by resource ID | To be tested |
|  | EnablePolicyAssignment | The rule is enabled based on the rule ID. | To be tested |
|  | ListOrganizationPolicyAssignments | Query the organization compliance rule list. | To be tested |
|  | RunEvaluationByPolicyAssignmentId | Evaluate the rule based on the rule ID. | To be tested |
|  | DisablePolicyAssignment | Disable the rule based on the rule ID. | To be tested |
|  | UpdatePolicyAssignment | Update user compliance rules | To be tested |
|  | ListBuiltInPolicyDefinitions | List the built-in policies of the user | To be tested |
|  | ListPolicyStatesByAssignmentId | Query all compliance results by rule ID | To be tested |
|  | ShowOrganizationPolicyAssignmentStatuses | Query the deployment status of organization compliance rules. | To be tested |
|  | ShowPolicyAssignment | Obtains a single rule based on the rule ID. | To be tested |
|  | ShowOrganizationPolicyAssignment | Query the compliance rules of a specified organization. | To be tested |
| Query | UpdateStoredQuery | Update the customized query | To be tested |
|  | CreateStoredQuery | Create an advanced query | To be tested |
|  | RunQuery | Executing Advanced Query | To be tested |
|  | ShowStoredQuery | Show Resource Query Language | To be tested |
|  | DeleteStoredQuery | Delete a single advanced query | To be tested |
|  | ListStoredQueries | List all advanced queries | To be tested |
|  | ListSchemas | List Schemas | To be tested |
| Query services supported by tag management | ListProviders | Query the services supported by tag management. | To be tested |
| Region | ListRegions | Query the area visible to the user | To be tested |
| Relations | ShowResourceRelationsDetail | Specify the resource ID and query the relationships between the resource and other resources. The relationship direction can be in or out. The account must have the rms:resources:getRelation permission. | To be tested |
|  | ShowResourceRelations | Specify the resource ID and query the association between the resource and other resources. The relationship direction can be "in" or "out" | To be tested |
| Resource | CountAllResources | Query the number of resources of the current account. | To be tested |
|  | ShowResourceDetail | Query a single resource under the current account. | To be tested |
|  | CollectAllResourcesSummary | Query the resource overview of the current account. | To be tested |
|  | ShowResourceById | Specify the resource ID and return details about the resource. The current user must have the rms:resources:get permission. For example, if you query the ECS, the resource type corresponding to the RMS resource type is ecs.cloudservers, where the provider is ecs and the type is cloudservers. For the types of services and resources supported by the RMS, see [Supported Services and Areas] (https://console.huaweicloud.com/eps/#/resources/supported). | To be tested |
|  | ListResources | Returns resources of a specific resource type under the current tenant. The current user must have the rms:resources:list permission. For example, if the ECS is queried, the resource type corresponding to the RMS resource type is ecs.cloudservers, where the provider is ecs and the type is cloudservers. For the types of services and resources supported by the RMS, see [Supported Services and Areas] (https://console.huaweicloud.com/eps/#/resources/supported). | To be tested |
|  | ListAllResources | All resources of the current user are returned. The current user must have the rms:resources:list permission. | To be tested |
| Tracker | DeleteTrackerConfig | Delete resource logger | To be tested |
|  | CreateTrackerConfig | Only one resource logger can be created or updated. | To be tested |
|  | ShowTrackerConfig | Query the details about the resource logger | To be tested |

