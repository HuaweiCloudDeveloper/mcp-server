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
                    <td>Query the number of compliant and noncompliant rules for one or more accounts in the aggregator.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConfigurationAggregator</td>
                    <td>Deletes a resource aggregator.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunAggregateResourceQuery</td>
                    <td>Performs advanced query on the specified aggregator.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAggregatePolicyAssignmentDetail</td>
                    <td>This API is used to return the details about the specified aggregation compliance rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConfigurationAggregator</td>
                    <td>Create a resource aggregator.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAggregateResourceConfig</td>
                    <td>Query details about a specific resource in the source account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAggregationAuthorization</td>
                    <td>Give the resource aggregator account the permission to collect data from the source account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurationAggregators</td>
                    <td>Query the resource aggregator list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAggregateComplianceDetailsByPolicyAssignment</td>
                    <td>Returns the evaluation result details of the specified aggregation compliance rule. Includes which resources were evaluated and whether each resource met the rules.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAggregationAuthorization</td>
                    <td>Deletes the authorization for a specified resource aggregator account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAggregationAuthorizations</td>
                    <td>Query the list of authorized resource aggregators.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAggregateComplianceByPolicyAssignment</td>
                    <td>Query the list of compliance and non-compliance rules, including the number of resources in compliance and non-compliance rules.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPendingAggregationRequests</td>
                    <td>Query the list of all suspended aggregation requests.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAggregateDiscoveredResources</td>
                    <td>Query the list of specific resources in the resource aggregator.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationAggregatorSourcesStatus</td>
                    <td>Query the status information about the aggregation account of a specified resource aggregator. The status includes the authorization information between the source account and the aggregator account. If it fails, the status contains the relevant error code or message.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAggregateDiscoveredResourceCounts</td>
                    <td>Query the number of account resources in the aggregator. The number of resources can be calculated by filter and GroupByKey.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePendingAggregationRequest</td>
                    <td>Delete the suspended authorization request from the aggregator account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationAggregator</td>
                    <td>Query the specified resource aggregator.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfigurationAggregator</td>
                    <td>Updates the resource aggregator.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Certificate Label Management</td>
                    <td>ListAllTags</td>
                    <td>Query the list of all tags.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">History</td>
                    <td>ShowResourceHistory</td>
                    <td>Query the change history of resources and resource relationships</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="21">Policy</td>
                    <td>DeletePolicyAssignment</td>
                    <td>Delete the rule based on the rule ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyStatesByDomainId</td>
                    <td>Query all compliance results of a user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOrganizationPolicyAssignment</td>
                    <td>Delete an organization compliance rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePolicyAssignments</td>
                    <td>Create a new compliance rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBuiltInPolicyDefinition</td>
                    <td>Query a single built-in policy by policy ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicyState</td>
                    <td>Update the compliance evaluation result of the user-defined compliance rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyAssignments</td>
                    <td>List the user's compliance rules</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOrganizationPolicyAssignmentDetailedStatus</td>
                    <td>Query the detailed deployment status of compliance rules for each member account in an organization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrganizationPolicyAssignment</td>
                    <td>Create or update an organization compliance rule. If the rule name already exists, the operation is an update operation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEvaluationStateByAssignmentId</td>
                    <td>Query the evaluation status of a rule based on the rule ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyStatesByResourceId</td>
                    <td>Query all compliance results by resource ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnablePolicyAssignment</td>
                    <td>The rule is enabled based on the rule ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOrganizationPolicyAssignments</td>
                    <td>Query the organization compliance rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunEvaluationByPolicyAssignmentId</td>
                    <td>Evaluate the rule based on the rule ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisablePolicyAssignment</td>
                    <td>Disable the rule based on the rule ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicyAssignment</td>
                    <td>Update user compliance rules</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBuiltInPolicyDefinitions</td>
                    <td>List the built-in policies of the user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyStatesByAssignmentId</td>
                    <td>Query all compliance results by rule ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOrganizationPolicyAssignmentStatuses</td>
                    <td>Query the deployment status of organization compliance rules.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPolicyAssignment</td>
                    <td>Obtains a single rule based on the rule ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOrganizationPolicyAssignment</td>
                    <td>Query the compliance rules of a specified organization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Query</td>
                    <td>UpdateStoredQuery</td>
                    <td>Update the customized query</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStoredQuery</td>
                    <td>Create an advanced query</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunQuery</td>
                    <td>Executing Advanced Query</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStoredQuery</td>
                    <td>Show Resource Query Language</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStoredQuery</td>
                    <td>Delete a single advanced query</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStoredQueries</td>
                    <td>List all advanced queries</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSchemas</td>
                    <td>List Schemas</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query services supported by tag management</td>
                    <td>ListProviders</td>
                    <td>Query the services supported by tag management.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Region</td>
                    <td>ListRegions</td>
                    <td>Query the area visible to the user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Relations</td>
                    <td>ShowResourceRelationsDetail</td>
                    <td>Specify the resource ID and query the relationships between the resource and other resources. The relationship direction can be in or out. The account must have the rms:resources:getRelation permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceRelations</td>
                    <td>Specify the resource ID and query the association between the resource and other resources. The relationship direction can be "in" or "out"</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Resource</td>
                    <td>CountAllResources</td>
                    <td>Query the number of resources of the current account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceDetail</td>
                    <td>Query a single resource under the current account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectAllResourcesSummary</td>
                    <td>Query the resource overview of the current account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceById</td>
                    <td>Specify the resource ID and return details about the resource. The current user must have the rms:resources:get permission. For example, if you query the ECS, the resource type corresponding to the RMS resource type is ecs.cloudservers, where the provider is ecs and the type is cloudservers. For the types of services and resources supported by the RMS, see [Supported Services and Areas] (https://console.huaweicloud.com/eps/#/resources/supported).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResources</td>
                    <td>Returns resources of a specific resource type under the current tenant. The current user must have the rms:resources:list permission. For example, if the ECS is queried, the resource type corresponding to the RMS resource type is ecs.cloudservers, where the provider is ecs and the type is cloudservers. For the types of services and resources supported by the RMS, see [Supported Services and Areas] (https://console.huaweicloud.com/eps/#/resources/supported).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllResources</td>
                    <td>All resources of the current user are returned. The current user must have the rms:resources:list permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Tracker</td>
                    <td>DeleteTrackerConfig</td>
                    <td>Delete resource logger</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrackerConfig</td>
                    <td>Only one resource logger can be created or updated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrackerConfig</td>
                    <td>Query the details about the resource logger</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
