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
                    <td rowspan="6">ACL Policy Management</td>
                    <td>DeleteAclV2</td>
                    <td>Delete a specified ACL policy. If an API is bound to the ACL policy, the ACL policy cannot be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAclPolicyV2</td>
                    <td>Query the details about a specified ACL policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAclStrategiesV2</td>
                    <td>Query all ACL policies.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAclStrategyV2</td>
                    <td>Modifies the specified ACL policy. The following attributes can be modified: acl_name, acl_type, and acl_value. Other attributes cannot be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAclStrategyV2</td>
                    <td>Add an ACL policy. The policy type is specified by the acl_type field (permit or deny). The object type can be IP address or domain. The value of acl_value corresponding to domain is the tenant name. Not a network domain name like www.exampleDomain.com</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAclV2</td>
                    <td>Deletes multiple specified ACL policies in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">API Binding ACL Policy</td>
                    <td>BatchDeleteApiAclBindingV2</td>
                    <td>Unbind APIs from ACL policies in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApiAclBindingV2</td>
                    <td>Bind the API to the ACL policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToAclPolicyV2</td>
                    <td>View the list of APIs bound to the ACL policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisUnbindedToAclPolicyV2</td>
                    <td>View the list of APIs that are not bound to the ACL policy. Ensure that the APIs have been published.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAclPolicyBindedToApiV2</td>
                    <td>View the list of ACL policies bound to the API</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiAclBindingV2</td>
                    <td>Unbind an API from an ACL policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">API Group Management</td>
                    <td>CheckApiGroupsV2</td>
                    <td>Verifies whether the API group name exists.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiGroupsV2</td>
                    <td>Query the API group list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiGroupV2</td>
                    <td>Deletes a specified API group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApiGroupV2</td>
                    <td>API groups are management units of APIs. An API group is equivalent to a service entry. When an API group is created, a subdomain name is returned as the access entry. It is recommended that APIs in an API group be related to each other.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfApiGroupV2</td>
                    <td>Query the details about a specified group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApiGroupV2</td>
                    <td>Modifies API group attributes. The name and remark attributes can be modified. Other attributes cannot be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">API bound throttling policy</td>
                    <td>BatchDisassociateThrottlingPolicyV2</td>
                    <td>Unbinding APIs from throttling policies in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateRequestThrottlingPolicyV2</td>
                    <td>Unbind the API from the throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToRequestThrottlingPolicyV2</td>
                    <td>Query the list of APIs bound to a throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRequestThrottlingPoliciesBindedToApiV2</td>
                    <td>Query the throttling policy list bound to an API. There should be only one flow control policy in each environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRequestThrottlingPolicyV2</td>
                    <td>Apply a throttling policy to an API. All accesses to the API will be restricted by the throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisUnbindedToRequestThrottlingPolicyV2</td>
                    <td>Query the list of all self-owned APIs that are not bound to the throttling policy. The API must have been published. Unpublished APIs will not be displayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">API management</td>
                    <td>ListApiVersionDetailV2</td>
                    <td>Query the details of a specified version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApiV2</td>
                    <td>Add an API. An API is a service interface and specific service capabilities.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiRuntimeDefinitionV2</td>
                    <td>View the runtime definition of a specified API in the specified environment. By default, the runtime definition in the RELEASE environment is queried.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisV2</td>
                    <td>View the API list. API details and release information is returned, but backend service information is not displayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeApiVersionV2</td>
                    <td>A version is generated based on the current API definition each time an API is published. The version records the definitions and status of APIs when they are published.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiByVersionIdV2</td>
                    <td>You can take an effective API version offline. After the API version is brought offline, the API cannot be invoked in the environment where the version takes effect.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrDeletePublishRecordForApiV2</td>
                    <td>Publish or bring an API offline.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersionsV2</td>
                    <td>Query the historical versions of an API. Each API can have a maximum of 10 historical versions in an environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchPublishOrOfflineApiV2</td>
                    <td>Publish multiple APIs to a specified environment or take multiple APIs offline from a specified environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckApisV2</td>
                    <td>Verify the API definition. Check whether the path or name of the API already exists.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfApiV2</td>
                    <td>View the details about a specified API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApiV2</td>
                    <td>Modifies the information about a specified API, including backend service information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiV2</td>
                    <td>Delete a specified API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DebugApiV2</td>
                    <td>This API is used to debug the definition of an API in the specified running environment. The API caller must have the permission to operate the API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">App Authorization Management</td>
                    <td>ListApisBindedToAppV2</td>
                    <td>Query the list of APIs bound to an app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisUnbindedToAppV2</td>
                    <td>Query the list of APIs that are not bound to an app in a specified environment, including self-owned APIs and APIs purchased from the Marketplace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAuthorizingAppsV2</td>
                    <td>After an app is created, it cannot access an API. To access an API in an environment, you need to authorize the API in the environment to the app. After the authorization is successful, the app can access the API in the environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelingAuthorizationV2</td>
                    <td>This API is used to cancel the authorization relationship between an API and an app. After the authorization is canceled, the app cannot invoke the API any longer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppsBindedToApiV2</td>
                    <td>Query the list of apps bound to an API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">App Template Management</td>
                    <td>ListApps</td>
                    <td>Query the application template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Client Configuration</td>
                    <td>DeleteAppCodeV2</td>
                    <td>The App Code is deleted. After the App Code is deleted, the corresponding APIs cannot be accessed through simple authentication.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppCodeV2</td>
                    <td>App Code is a submodule of an app. After an app code is created, simple app authentication can be implemented.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppsV2</td>
                    <td>Query the app list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppAcl</td>
                    <td>Set the access control configured on the client.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppCodeV2</td>
                    <td>App Code is a submodule of an app. After an app code is created, simple app authentication can be implemented.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppAcl</td>
                    <td>Delete the access control information configured on the client.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppV2</td>
                    <td>View detailed information about a specified app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppBoundAppQuota</td>
                    <td>View the application quota associated with a specified client application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppCodeAutoV2</td>
                    <td>When creating an app code, you do not need to specify the value. The background automatically generates a random character string to fill in the value.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppCodesV2</td>
                    <td>Query the app code list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppAcl</td>
                    <td>View the access control details of the app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Client Quota</td>
                    <td>ShowAppQuota</td>
                    <td>Obtain the client quota details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuotaBindableApps</td>
                    <td>Query the list of client applications to which the client quota can be bound. Fuzzy search by client application name is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuotas</td>
                    <td>Obtain the client quota list. Fuzzy query by name is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppQuota</td>
                    <td>Modifying the Client Quota</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuotaBoundApps</td>
                    <td>Query the list of client applications bound to the client quota. Fuzzy match by client application name is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppQuota</td>
                    <td>Create Client Quota</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateAppQuotaWithApp</td>
                    <td>Unbind the client quota from the client application</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateAppsForAppQuota</td>
                    <td>List of client applications bound to the client quota</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppQuota</td>
                    <td>Delete a client quota. When deleting the client quota, delete the association between the client quota and the client application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Configuration Management</td>
                    <td>ListProjectCofigsV2</td>
                    <td>Query the tenant configuration list of an instance. You can use this API to view the resource configuration and usage of each type of resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Customized Authentication Management</td>
                    <td>CreateCustomAuthorizerV2</td>
                    <td>Create a user-defined authentication</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCustomAuthorizerV2</td>
                    <td>Modifying a user-defined authentication</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfCustomAuthorizersV2</td>
                    <td>Viewing the details of the customized authentication</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomAuthorizerV2</td>
                    <td>Delete user-defined authentication</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCustomAuthorizersV2</td>
                    <td>Query the user-defined authentication list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Domain name management</td>
                    <td>UpdateDomainV2</td>
                    <td>Modify the configuration information corresponding to the bound domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfDomainNameCertificateV2</td>
                    <td>View details about the certificate bound to the domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateDomainV2</td>
                    <td>If an API group does not need to be bound to a user-defined domain name, you can unbind the domain name from the API group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateCertificateV2</td>
                    <td>If the HTTPS request protocol is used for defining an API request during API creation, the SSL certificate must be added to the independent domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateCertificateV2</td>
                    <td>If the domain name certificate is no longer needed or has expired, you can delete the certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateDomainV2</td>
                    <td>User-defined domain name, which takes effect only after the CNAME is added to the subdomain name of the API group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Environment variable management</td>
                    <td>CreateEnvironmentVariableV2</td>
                    <td>After an API is released to different environments, the environment variables, such as the API service deployment address and request version number, may vary according to the environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfEnvironmentVariableV2</td>
                    <td>View details about a specified environment variable.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnvironmentVariableV2</td>
                    <td>Delete the specified environment variables.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnvironmentVariableV2</td>
                    <td>Modify environment variables. If an environment variable references the backend service address of an API, modifying the environment variable will release all APIs that use the variable again.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvironmentVariablesV2</td>
                    <td>Query the list of all environment variables in a group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Environmental Management</td>
                    <td>UpdateEnvironmentV2</td>
                    <td>Modifies the information about a specified environment. The name and remark attributes can be modified. Other attributes cannot be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnvironmentV2</td>
                    <td>In actual production, an API provider may have multiple environments, such as the development environment, test environment, and production environment. You can release APIs to an environment for callers to invoke.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnvironmentV2</td>
                    <td>Delete the specified environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvironmentsV2</td>
                    <td>Query the environment list that meets the conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Exclusive - Group Custom Response Management</td>
                    <td>UpdateGatewayResponseTypeV2</td>
                    <td>Modifies the customized response of a specified error type in a group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGatewayResponsesV2</td>
                    <td>Query the customized response list of a group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGatewayResponseV2</td>
                    <td>Deleting a customized response from a group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfGatewayResponseTypeV2</td>
                    <td>View the customized response of a specified error type in a group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGatewayResponseTypeV2</td>
                    <td>Delete the customized response configuration for the specified error type and restore the default response configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGatewayResponseV2</td>
                    <td>Adding a customized response in a group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfGatewayResponseV2</td>
                    <td>Details of querying customized group information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGatewayResponseV2</td>
                    <td>Customized response for modifying a group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Exclusive - Microservice Center Management</td>
                    <td>ImportMicroservice</td>
                    <td>Import a microservice.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Exclusive-Asynchronous Task Management</td>
                    <td>ShowAsyncTaskResult</td>
                    <td>Obtain the asynchronous task result.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportApiDefinitionsAsync</td>
                    <td>Exports API definitions in a group. The exported file must comply with the swagger standard. For details about the customized extended fields of API Gateway</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportApiDefinitionsAsync</td>
                    <td>Import an API. The content in the file to be imported must comply with the swagger standard. For details about the customized extended fields of API Gateway</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Exclusive-Credential Management</td>
                    <td>DeleteAppV2</td>
                    <td>Delete a specified app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAnAppV2</td>
                    <td>An app is an identity that can access an API. After the API is authorized to an app, the app can invoke the API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResettingAppSecretV2</td>
                    <td>Reset the key of a specified app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppV2</td>
                    <td>Modifies the information about a specified app. The attributes that can be modified are name and remark. When the user-defined key and secret are enabled, app_key and app_secret can also be modified. Other attributes cannot be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckAppV2</td>
                    <td>Verifies whether the app exists. Non-app owners can invoke this interface to verify whether the app exists. This interface displays only the basic information about the app, including the ID, name, and</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Exclusive-Domain Name Management</td>
                    <td>UpdateSlDomainSettingV2</td>
                    <td>Disable or enable the debug domain name bound to the API group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Exclusive-Monitoring Information Query</td>
                    <td>ListLatelyGroupStatisticsV2</td>
                    <td>Query the number of times that all APIs in the API group are invoked by the API group ID. The measurement period is 1 minute. The query scope is within one hour. One sample is generated every minute. The sample value is accumulated within one minute.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetricData</td>
                    <td>Query the monitoring data of a specified indicator in a specified period of time and granularity. You can specify the data dimension to be queried by specifying the parameter.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Exclusive-Summary Query</td>
                    <td>ListApiGroupsQuantitiesV2</td>
                    <td>Query the API group overview of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiQuantitiesV2</td>
                    <td>Query the API overview of the tenant, including the number of APIs published to the RELEASE environment and the number of APIs not published to the RELEASE environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuantitiesV2</td>
                    <td>Query the app overview of the tenant, including the number of apps for which API access has been granted and the number of apps for which API access has not been granted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Instance Feature Management</td>
                    <td>ListFeaturesV2</td>
                    <td>View the DB instance feature list. Note: If the DB instance does not support the following features, contact technical support to upgrade the DB instance version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFeatureV2</td>
                    <td>Configure the required features for the instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Instance Management</td>
                    <td>ShowRestrictionOfInstanceV2</td>
                    <td>View the instance constraint information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfInstanceV2</td>
                    <td>Viewing DB Instance Details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Monitoring information query</td>
                    <td>ListLatelyApiStatisticsV2</td>
                    <td>Query the number of times that an API is invoked based on the API ID and the latest period. The statistical period is 1 minute. The query scope is within one hour. One sample is per minute. The sample value is accumulated within one minute.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">OpenAPI</td>
                    <td>ExportApiDefinitionsV2</td>
                    <td>Export the definition information of APIs in a group. The exported file content complies with the Swagger standard.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportApiDefinitionsV2</td>
                    <td>Import an API. The imported file must comply with the swagger standard.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">Plug-in management</td>
                    <td>CreatePlugin</td>
                    <td>Create plug-in information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachApiFromPlugin</td>
                    <td>Unbind the API from the plug-in</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlugins</td>
                    <td>Query details about a group of API Gateway plug-ins that meet the search criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlugin</td>
                    <td>Query plug-in details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachPluginFromApi</td>
                    <td>Unbind the plug-in from the API</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePlugin</td>
                    <td>Modifies plug-in information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiAttachedPlugins</td>
                    <td>Query information about the plug-ins bound to a specified API</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePlugin</td>
                    <td>Delete the plug-in.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiAttachablePlugins</td>
                    <td>Query information about the plug-ins that can be bound to the current API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPluginAttachableApis</td>
                    <td>Query information about the APIs that can be bound to the current plug-in.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPluginAttachedApis</td>
                    <td>Query information about the APIs bound to a specified plug-in</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachPluginToApi</td>
                    <td>Bind the plug-in to the API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachApiToPlugin</td>
                    <td>Bind the plug-in to the API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Premium-Configuration Management</td>
                    <td>ListInstanceConfigsV2</td>
                    <td>Query the tenant instance configuration list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Premium-Customized Inbound Port Management</td>
                    <td>ListCustomIngressPorts</td>
                    <td>Query the user-defined inbound port list of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddCustomIngressPort</td>
                    <td>User-defined inbound port of the new instance. In an instance, a port supports only one protocol.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomIngressPort</td>
                    <td>Delete the user-defined inbound ports, excluding the default ports 80 and 443.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCustomIngressPortDomains</td>
                    <td>Query the domain name bound to the user-defined inbound port specified by an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Premium-Instance Feature Management</td>
                    <td>ListInstanceFeatures</td>
                    <td>Query the feature list supported by an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">Premium-Instance Management</td>
                    <td>CreatePrepayResize</td>
                    <td>Create a yearly/monthly specification change order.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIngressEipV2</td>
                    <td>Update the public network bandwidth of an instance. This parameter is supported only when the instance type is ELB.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddEngressEipV2</td>
                    <td>Enable the public network egress for the instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstancesV2</td>
                    <td>Delete a premium instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceV2</td>
                    <td>Create a pay-per-use premium instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesV2</td>
                    <td>Query the list of premium instances</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostPayResizeOrder</td>
                    <td>Create a pay-per-use specification change order.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfInstanceProgressV2</td>
                    <td>View the creation progress of the premium instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableZonesV2</td>
                    <td>View AZ information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrder</td>
                    <td>Create a yearly/monthly premium instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveIngressEipV2</td>
                    <td>Disable the public network entry of an instance. This function is supported only when the instance type is ELB.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddEipV2</td>
                    <td>Update or bind an EIP to an instance (supported only when the instance type is LVS)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveEipV2</td>
                    <td>Unbinding an EIP from an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveEngressEipV2</td>
                    <td>Disable the public network egress of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceV2</td>
                    <td>Update a premium instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddIngressEipV2</td>
                    <td>Enable the public network entry for an instance. This function is supported only when the instance type is ELB.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEngressEipV2</td>
                    <td>Update the outbound bandwidth of an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Premium-Instance Tag Management</td>
                    <td>BatchCreateOrDeleteInstanceTags</td>
                    <td>Add or delete tags for a single instance in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectInstanceTags</td>
                    <td>Query all instance tags in a project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstancesNumByTags</td>
                    <td>Query the number of instances with a specified tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Premium-Instance VPC Endpoint Management</td>
                    <td>AcceptOrRejectEndpointConnections</td>
                    <td>Accepts or rejects the instance node connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddEndpointPermissions</td>
                    <td>Add the instance VPC endpoint connection trustlist in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpointConnections</td>
                    <td>Query the instance VPC connection list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpointPermissions</td>
                    <td>Query the trustlist of the VPC endpoint service of the current instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEndpointPermissions</td>
                    <td>This API is used to delete the trustlist of VPC endpoint connections in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Premium-Orchestration Rule Management</td>
                    <td>ShowDetailsOfOrchestration</td>
                    <td>Query orchestration rule details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOrchestration</td>
                    <td>Delete an orchestration rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOrchestrationAttachedApis</td>
                    <td>Query information about the APIs bound to a specified plug-in</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOrchestration</td>
                    <td>Updates an orchestration rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOrchestrations</td>
                    <td>View the orchestration rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrchestration</td>
                    <td>Create an orchestration rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">SSL Certificate Management</td>
                    <td>BatchDisassociateDomainsV2</td>
                    <td>Unbind an SSL certificate from a domain name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfCertificateV2</td>
                    <td>Viewing Certificate Details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCertificateV2</td>
                    <td>This API is used to delete an SSL certificate. Only the certificate that is not associated with a domain name can be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDisassociateCertsV2</td>
                    <td>This API is used to unbind an SSL certificate from a domain name. Currently, only one certificate can be unbound. The certificate_ids field in the request body contains only one certificate ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAssociateCertsV2</td>
                    <td>The domain name is bound to the SSL certificate. Currently, only one binding is supported. The certificate_ids field in the request body contains only one certificate ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificatesV2</td>
                    <td>Obtain the SSL certificate list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCertificateV2</td>
                    <td>Modifying the SSL Certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificateV2</td>
                    <td>Create an SSL certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAttachedDomainsV2</td>
                    <td>Obtain the list of domain names bound to the SSL certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAssociateDomainsV2</td>
                    <td>Domain name bound to the SSL certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Set Special Flow Control</td>
                    <td>ListSpecialThrottlingConfigurationsV2</td>
                    <td>View the special configuration of the throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSpecialThrottlingConfigurationV2</td>
                    <td>To delete a special configuration of a throttling policy, run the following command:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSpecialThrottlingConfigurationV2</td>
                    <td>A throttling policy can limit the maximum number of times that an API can be accessed within a period of time, or the maximum number of times that a tenant or app can access an API within a period of time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSpecialThrottlingConfigurationV2</td>
                    <td>Modify a special setting in a throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Shared edition-API group management</td>
                    <td>DeleteApiGroup</td>
                    <td>Delete a specified API group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiGroups</td>
                    <td>Query the API group list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApiGroup</td>
                    <td>API groups are management units of APIs. An API group is equivalent to a service entry. When an API group is created, a subdomain name is returned as the access entry. It is recommended that APIs in an API group be related to each other.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAPIGroup</td>
                    <td>Modifies API group attributes. The name and remark attributes can be modified. Other attributes cannot be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfApiGroup</td>
                    <td>Query the details about a specified group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Shared edition-API management</td>
                    <td>UpdateApi</td>
                    <td>Modifies information about a specified API, including backend service information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfApi</td>
                    <td>View the details about a specified API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApi</td>
                    <td>Delete a specified API. When an API is deleted, all resource information or binding relationships related to the API will be deleted, such as the API release records, bound backend services, and app authorization information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApis</td>
                    <td>View the API list. The API details and release information is returned, but the backend service information is not displayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApi</td>
                    <td>Add an API. An API is a service interface and specific service capabilities. The API is divided into two parts. The first part is an API for API users, which defines how users invoke the API. The second part is oriented to the API provider. The API provider defines the actual backend status of the API and how API Gateway accesses the actual backend services. Currently, the real backend service of an API supports three types: traditional HTTP/HTTPS web backend, function workflow, and MOCK.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Shared edition-App authorization management</td>
                    <td>CreateAuthorizingApps</td>
                    <td>After an app is created, the app cannot access the API. To access the API in an environment, you need to grant the API in the environment to the app. After the authorization is successful, the app can access the API in the environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelingAuthorization</td>
                    <td>This API is used to cancel the authorization relationship between an API and an app. After the authorization is canceled, the app cannot invoke the API any longer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisThatNotBoundWithAnApp</td>
                    <td>Query the list of APIs that are not bound to an app in a specified environment, including self-owned APIs and APIs purchased from the Marketplace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAPIsThatBoundWithAnApp</td>
                    <td>Query the list of APIs bound to an app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppsBoundToAnApi</td>
                    <td>Query the list of apps bound to an API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Shared edition-App management</td>
                    <td>UpdateAnApp</td>
                    <td>Modifies the information about a specified app. The attributes that can be modified are name and remark. When the user-defined key and secret are enabled, app_key and app_secret can also be modified. Other attributes cannot be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckAnApp</td>
                    <td>Verifies whether the app exists. Non-app owners can invoke this interface to verify whether the app exists. This interface displays only the basic information about the app, including the ID, name, and remarks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppDetails</td>
                    <td>View detailed information about a specified app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAnApp</td>
                    <td>An application is an identity that can access an API. After the API is authorized to an app, the app can invoke the API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAnApp</td>
                    <td>Delete a specified app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResettingTheAppSecret</td>
                    <td>Reset the key of a specified app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Shared edition-Set special flow control</td>
                    <td>UpdateSpecialThrottlingConfiguration</td>
                    <td>Modify a special setting in a throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSpecialThrottlingConfigurations</td>
                    <td>View the special configuration of the throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSpecialThrottlingConfiguration</td>
                    <td>A throttling policy can limit the maximum number of times that an API can be accessed within a period of time, or the maximum number of times that a tenant or app can access an API within a period of time. If you want to perform special settings for a specific app, for example, set the number of access times per minute for all apps to 500, and set the number of access times per minute for APP1 to 800, you can set the special app in the flow control policy. Add a special object for the throttling policy. The object can be an app or a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSpecialThrottlingConfiguration</td>
                    <td>To delete a special configuration of a throttling policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Shared edition-flow control policy management</td>
                    <td>DeleteRequestThrottlingPolicy</td>
                    <td>Deletes a specified throttling policy and all binding relationships between the throttling policy and the API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTheRequestThrottlingPolicy</td>
                    <td>To query the information about all throttling policies</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfARequestThrottlingPolicy</td>
                    <td>View the details about a specified throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRequestThrottlingPolicy</td>
                    <td>Modifies the details about a specified throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRequestThrottlingPolicy</td>
                    <td>After an API is brought online, the system provides a flow control policy for each API by default. API providers can change the flow control policy based on the API service capability and load status. The throttling policy specifies the maximum number of times that an API can be accessed within a specified period.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Shared-API Binding Flow Control Policy</td>
                    <td>ListRequestThrottlingPoliciesThatBoundToAnApi</td>
                    <td>Query the throttling policy list bound to an API. There should be only one flow control policy in each environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisThatNotBoundWithRequestThrottlingPolicy</td>
                    <td>Query the list of self-owned APIs that are not bound to the throttling policy. The API must have been published. Unpublished APIs will not be displayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateRequestThrottlingPolicy</td>
                    <td>Unbind the API from the throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisThatBoundWithRequestThrottlingPolicy</td>
                    <td>Query the list of APIs bound to a throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRequestThrottlingPolicy</td>
                    <td>Apply a throttling policy to an API. All accesses to the API will be restricted by the throttling policy. If the number of access times in a specified period exceeds the maximum number of access times specified in the throttling policy, subsequent access requests will be rejected. This protects backend APIs from abnormal traffic and ensures stable service running. Bind a flow control policy to a specified shared-API. When binding a flow control policy, you need to specify the environment in which the flow control policy takes effect. The same API can be bound with different throttling policies in different environments. After an API is published to a specific environment, only one default throttling policy can be bound to the API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Shared-Domain name management</td>
                    <td>AssociateDomain</td>
                    <td>User-defined domain name, which takes effect only after the CNAME is added to the subdomain name of the API group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfDomainNameCertificate</td>
                    <td>View details about the certificate bound to the domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateCertificate</td>
                    <td>If the HTTPS request protocol is used for defining an API request during API creation, the SSL certificate must be added to the domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateCertificate</td>
                    <td>If the domain name certificate is no longer needed or has expired, you can delete the certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateDomain</td>
                    <td>If an API group does not need to be bound to a user-defined domain name, you can unbind the domain name from the API group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Shared-Environment variable management</td>
                    <td>ListEnvironmentVariables</td>
                    <td>Query the list of all environment variables in a group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnvironmentVariable</td>
                    <td>Delete the specified environment variables.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnvironmentVariable</td>
                    <td>After an API is released to different environments, the environment variables, such as the API service deployment address and request version number, may vary according to the environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnvironmentVariableDetails</td>
                    <td>View details about a specified environment variable.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Shared-Signature Key Management</td>
                    <td>CreateSignatureKey</td>
                    <td>To ensure API security, it is recommended that tenants provide a protection mechanism for API access. That is, open APIs of tenants need to authenticate the request source. Requests that do not meet the authentication requirements are directly rejected. The signature key is one of the API security protection mechanisms. If a tenant creates a signature key and binds the signature key to an API, API Gateway uses the bound signature key to encrypt request parameters and generate a signature. When a tenant's backend service receives a request, it can verify the signature. If the signature verification fails, the request is not sent by API Gateway and the tenant can reject the request, ensuring API security and preventing API attacks from unknown sources.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSignatureKey</td>
                    <td>Modifies the details about a specified signature key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSignatureKey</td>
                    <td>Delete a specified signature key. When the signature key is deleted, the binding relationship configured for the signature key is also deleted, and the corresponding signature key becomes invalid.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSignatureKeys</td>
                    <td>Query information about all signature keys.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Shared-Signing Key Binding Relationship Management</td>
                    <td>ListSignatureKeysBoundtoAnAPI</td>
                    <td>Query the list of signature keys bound to an API. Each API should be bound to a maximum of one signing key per environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateSignatureKey</td>
                    <td>Unbind the API from the signature key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBoundWithSignatureKey</td>
                    <td>Query the list of APIs bound to a signature key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateSignatureKey</td>
                    <td>A signature key takes effect only after it is bound to an API. After the signature key is bound to an API, API Gateway uses the signature key to encrypt and sign requests to backend services. Backend services can verify the signature to verify the request source. Binds the specified signing key to one or more published APIs. When an API is published in different environments, different signature keys can be bound to the API. An API can be bound to only one signature key after being published to a specific environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisNotBoundWithSignatureKey</td>
                    <td>Query the list of APIs that are not bound to the signature key. The API must have been published. Unpublished APIs will not be displayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Shared-Summary Query</td>
                    <td>ListAppQuantities</td>
                    <td>Query the app overview of the tenant, including the number of apps for which API access has been granted and the number of apps for which API access has not been granted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAPIsOfAPIGroup</td>
                    <td>Query the API group overview of a tenant, including the number of API groups that are released and the number of API groups that are not released.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiQuantities</td>
                    <td>Query the API overview of the tenant, including the number of APIs published to the RELEASE environment and the number of APIs not published to the RELEASE environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Signature Key Management</td>
                    <td>UpdateSignatureKeyV2</td>
                    <td>Modifies the details about a specified signature key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSignatureKeyV2</td>
                    <td>To protect API security, it is recommended that tenants provide a protection mechanism for API access. That is, open APIs of tenants need to authenticate the request source. Requests that do not meet the authentication requirements are directly rejected.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSignatureKeyV2</td>
                    <td>Deletes a specified signature key. A signature key cannot be deleted if it is bound to an API. You need to unbind it from the API before deleting it.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSignatureKeysV2</td>
                    <td>Query information about all signature keys.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Signing Key Binding Relationship Management</td>
                    <td>AssociateSignatureKeyV2</td>
                    <td>A signature key takes effect only after it is bound to an API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSignatureKeysBindedToApiV2</td>
                    <td>Query the list of signature keys bound to an API. Each API should be bound with a maximum of one signing key per environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateSignatureKeyV2</td>
                    <td>Unbind the API from the signature key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToSignatureKeyV2</td>
                    <td>Query the list of APIs bound to a signature key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisNotBoundWithSignatureKeyV2</td>
                    <td>Query the list of APIs that are not bound to the signature key. The API must have been published. Unpublished APIs will not be displayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Tag Management</td>
                    <td>ListInstanceTags</td>
                    <td>Query the instance tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagsV2</td>
                    <td>Query the tag list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesByTags</td>
                    <td>Query a specified database instance by tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Throttling Policy Management</td>
                    <td>ListRequestThrottlingPolicyV2</td>
                    <td>To query the information about all throttling policies</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRequestThrottlingPolicyV2</td>
                    <td>Modifies the details about a specified throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfRequestThrottlingPolicyV2</td>
                    <td>View the details about a specified throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRequestThrottlingPolicyV2</td>
                    <td>After an API is brought online, the system provides a default throttling policy for each API. API providers can change the throttling policy based on the API service capability and load status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRequestThrottlingPolicyV2</td>
                    <td>Deletes a specified throttling policy. If the throttling policy is bound to an API, you need to unbind the throttling policy from the API and then delete the throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">VPC Channel Management</td>
                    <td>DeleteVpcChannelV2</td>
                    <td>Delete a specified VPC channel</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHealthCheck</td>
                    <td>Modifies the VPC channel health check.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMemberGroup</td>
                    <td>Create a VPC channel backend server group on the Service Integration page. You can determine whether to associate VPC channel backend instances with the backend instance server group to manage backend server nodes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDisableMembers</td>
                    <td>Failed to modify the status of backend servers in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfMemberGroup</td>
                    <td>View details about a specified VPC channel backend server group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpcChannelV2</td>
                    <td>Updates the parameters of a specified VPC channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMemberGroups</td>
                    <td>Query the list of backend cloud service groups in a VPC channel</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchEnableMembers</td>
                    <td>Changing the status of backend servers in batches is available.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpcChannelV2</td>
                    <td>In the service integration, create channels for connecting to private VPC resources. When creating an API, configure backend nodes to use these VPC channels so that the service integration can directly access private VPC resources.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBackendInstancesV2</td>
                    <td>This API is used to update the backend instance of a specified VPC channel. During the update, the input request parameters are used to fully overwrite the backend instances of the corresponding cloud service group. If the ECS group to be modified is not specified, the system overwrites the entire ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMemberGroup</td>
                    <td>Updates a specified VPC channel backend server group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfVpcChannelV2</td>
                    <td>View details about a specified VPC channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddingBackendInstancesV2</td>
                    <td>Adding a backend instance to a specified VPC channel</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMemberGroup</td>
                    <td>Delete a specified VPC channel backend server group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcChannelsV2</td>
                    <td>View the VPC channel list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackendInstanceV2</td>
                    <td>Delete a backend instance from a specified VPC channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackendInstancesV2</td>
                    <td>View the list of backend instances in a specified VPC channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">environment-controller-v2</td>
                    <td>DeleteEnvironment</td>
                    <td>Delete the environment of the application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnvironment</td>
                    <td>Editing environment in the application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnvironment</td>
                    <td>Create an environment under the application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvironments</td>
                    <td>Query the environment list of an application.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
