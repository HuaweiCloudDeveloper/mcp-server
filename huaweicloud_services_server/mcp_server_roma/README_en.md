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
                    <td rowspan="6">ACL Policy Management</td>
                    <td>UpdateAclStrategyV2</td>
                    <td>Modifies the specified ACL policy. The following attributes can be modified: acl_name, acl_type, and acl_value. Other attributes cannot be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAclV2</td>
                    <td>Delete a specified ACL policy. If an API is bound to the ACL policy, the ACL policy cannot be deleted.</td>
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
                    <td rowspan="6">API Binding ACL Policy</td>
                    <td>CreateApiAclBindingV2</td>
                    <td>Bind the API to the ACL policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiAclBindingV2</td>
                    <td>Unbind an API from an ACL policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteApiAclBindingV2</td>
                    <td>Unbind APIs from ACL policies in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisUnbindedToAclPolicyV2</td>
                    <td>View the list of APIs that are not bound to the ACL policy. Ensure that the APIs have been published.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToAclPolicyV2</td>
                    <td>View the list of APIs bound to the ACL policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAclPolicyBindedToApiV2</td>
                    <td>View the list of ACL policies bound to the API</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">API Group Management</td>
                    <td>ShowDetailsOfApiGroupV2</td>
                    <td>Query the details about a specified group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiGroupV2</td>
                    <td>Deletes a specified API group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckApiGroupsV2</td>
                    <td>Verifies whether the API group name exists.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApiGroupV2</td>
                    <td>Modifies API group attributes. The name and remark attributes can be modified. Other attributes cannot be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApiGroupV2</td>
                    <td>API groups are management units of APIs. An API group is equivalent to a service entry. When an API group is created, a subdomain name is returned as the access entry. It is recommended that APIs in an API group be related to each other.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiGroupsV2</td>
                    <td>Query the API group list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">API bound throttling policy</td>
                    <td>DisassociateRequestThrottlingPolicyV2</td>
                    <td>Unbind the API from the throttling policy.</td>
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
                    <td>BatchDisassociateThrottlingPolicyV2</td>
                    <td>Unbinding APIs from throttling policies in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToRequestThrottlingPolicyV2</td>
                    <td>Query the list of APIs bound to a throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">API management</td>
                    <td>DeleteApiV2</td>
                    <td>Delete a specified API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisV2</td>
                    <td>View the API list. API details and release information is returned, but backend service information is not displayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrDeletePublishRecordForApiV2</td>
                    <td>Publish or bring an API offline.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersionDetailV2</td>
                    <td>Query the details of a specified version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeApiVersionV2</td>
                    <td>A version is generated based on the current API definition each time an API is published. The version records the definitions and status of APIs when they are published.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersionsV2</td>
                    <td>Query the historical versions of an API. Each API can have a maximum of 10 historical versions in an environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DebugApiV2</td>
                    <td>This API is used to debug the definition of an API in the specified running environment. The API caller must have the permission to operate the API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchPublishOrOfflineApiV2</td>
                    <td>Publish multiple APIs to a specified environment or take multiple APIs offline from a specified environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfApiV2</td>
                    <td>View the details about a specified API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiRuntimeDefinitionV2</td>
                    <td>View the runtime definition of a specified API in the specified environment. By default, the runtime definition in the RELEASE environment is queried.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApiV2</td>
                    <td>Modifies the information about a specified API, including backend service information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckApisV2</td>
                    <td>Verify the API definition. Check whether the path or name of the API already exists.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApiV2</td>
                    <td>Add an API. An API is a service interface and specific service capabilities.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiByVersionIdV2</td>
                    <td>You can take an effective API version offline. After the API version is brought offline, the API cannot be invoked in the environment where the version takes effect.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">APPLICATION_MANAGEMENT</td>
                    <td>CheckRomaAppDetails</td>
                    <td>Query application details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddUserToApp</td>
                    <td>- Set the user members of the application. If the array is empty, the existing application member list will be cleared.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRomaApp</td>
                    <td>Query the application list. Query by conditions is supported. All conditions are in the AND relationship.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetRomaAppSecret</td>
                    <td>Reset the application key</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRomaApp</td>
                    <td>Delete a single application</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckCanAuthUsersOfApp</td>
                    <td>Query the candidate user list of the application. Abnormal users will be filtered out.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRomaApp</td>
                    <td>Create Application</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateRomaApp</td>
                    <td>Check whether the application that meets the specified conditions exists.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRomaApp</td>
                    <td>Update application</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckRomaAppSecret</td>
                    <td>Query the application key</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckAuthUsersOfApp</td>
                    <td>Query the user list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">ASSET_MANAGEMENT</td>
                    <td>CheckAssetJobStatus</td>
                    <td>Querying the job progress</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAsset</td>
                    <td>Delete assets in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportAsset</td>
                    <td>-Create an asset import task. The asset version and specific assets are read from the asset content.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportAsset</td>
                    <td>Exporting assets in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadAssetArchive</td>
                    <td>-After an export job is successfully executed, this API is used to obtain the asset package generated by the export job. The asset package can be downloaded only once.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">App Authorization Management</td>
                    <td>ListDuplicateApisForAppV2</td>
                    <td>Query the list of APIs with conflicting paths in a specified app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelingAuthorizationV2</td>
                    <td>This API is used to cancel the authorization relationship between an API and an app. After the authorization is canceled, the app cannot invoke the API any longer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisUnbindedToAppV2</td>
                    <td>Query the list of APIs that are not bound to an app in a specified environment, including self-owned APIs and APIs purchased from the Marketplace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppsBindedToApiV2</td>
                    <td>Query the list of apps bound to an API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAuthorizingAppsV2</td>
                    <td>After an app is created, it cannot access an API. To access an API in an environment, you need to authorize the API in the environment to the app. After the authorization is successful, the app can access the API in the environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToAppV2</td>
                    <td>Query the list of APIs bound to an app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">App Permission Management</td>
                    <td>UpdateTopicAccessPolicy</td>
                    <td>Update the topic permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMqsInstanceTopicAccessPolicy</td>
                    <td>Query the topic permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Application Configuration Management</td>
                    <td>UpdateAppConfigV2</td>
                    <td>Modifying Application Configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppConfigV2</td>
                    <td>Delete application configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppConfigV2</td>
                    <td>Create Application Configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppConfigV2</td>
                    <td>Viewing Application Configuration Details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppConfigsV2</td>
                    <td>Query the application configuration list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Client Configuration</td>
                    <td>ShowAppBoundAppQuota</td>
                    <td>View the application quota associated with a specified client application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppAcl</td>
                    <td>View the access control details of the app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppCodeV2</td>
                    <td>The App Code is deleted. After the App Code is deleted, the corresponding APIs cannot be accessed through simple authentication.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppCodeAutoV2</td>
                    <td>When creating an app code, you do not need to specify the value. The background automatically generates a random character string to fill in the value.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppV2</td>
                    <td>View detailed information about a specified app.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppCodeV2</td>
                    <td>App Code is a submodule of an app. After an app code is created, simple app authentication can be implemented.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppAcl</td>
                    <td>Set the access control configured on the client.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppAcl</td>
                    <td>Delete the access control information configured on the client.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppsV2</td>
                    <td>Query the app list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppCodesV2</td>
                    <td>Query the app code list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfAppCodeV2</td>
                    <td>App Code is a submodule of an app. After an app code is created, simple app authentication can be implemented.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Client Quota</td>
                    <td>UpdateAppQuota</td>
                    <td>Modifying the Client Quota</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuotas</td>
                    <td>Obtain the client quota list. Fuzzy query by name is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppQuota</td>
                    <td>Create Client Quota</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuotaBindableApps</td>
                    <td>Query the list of client applications to which the client quota can be bound. Fuzzy search by client application name is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateAppQuotaWithApp</td>
                    <td>Unbind the client quota from the client application</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppQuotaBoundApps</td>
                    <td>Query the list of client applications bound to the client quota. Fuzzy match by client application name is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateAppsForAppQuota</td>
                    <td>List of client applications bound to the client quota</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppQuota</td>
                    <td>Obtain the client quota details</td>
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
                    <td rowspan="14">Custom Backend Service</td>
                    <td>DebugLiveDataApiV2</td>
                    <td>Check whether the backend API is available.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishLiveDataApiV2</td>
                    <td>Deploy backend APIs in an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLiveDataApiV2</td>
                    <td>Updates backend API parameters in an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLiveDataDataSourcesV2</td>
                    <td>Query the list of customized backend service data sources.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLiveDataApiDeploymentHistoryV2</td>
                    <td>Query the deployment records of backend APIs in an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLiveDataApiV2</td>
                    <td>This API is used to delete a backend API from an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckLivedataApisV2</td>
                    <td>Verify the definition of the customized backend API. Check whether the path or name of the custom backend API already exists.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLiveDataQuotaV2</td>
                    <td>Query the quota of a user-defined backend service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnpublishLiveDataApiV2</td>
                    <td>Undeploy backend APIs in an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLiveDataApiScriptV2</td>
                    <td>Create a backend API script in an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLiveDataApiV2</td>
                    <td>Create a backend API in an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLiveDataApiV2</td>
                    <td>Query details about a backend API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLiveDataApiTestHistoryV2</td>
                    <td>Query the backend API test result in an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLiveDataApiV2</td>
                    <td>Obtains all backend APIs in an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Customized Authentication Management</td>
                    <td>ShowDetailsOfCustomAuthorizersV2</td>
                    <td>Viewing the details of the customized authentication</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCustomAuthorizersV2</td>
                    <td>Query the user-defined authentication list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
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
                    <td>DeleteCustomAuthorizerV2</td>
                    <td>Delete user-defined authentication</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">DICTIONARY_MANAGEMENT</td>
                    <td>UpdateDictionary</td>
                    <td>Update dictionary</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDictionary</td>
                    <td>creation dictionary</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDictionary</td>
                    <td>When a single dictionary is deleted, all subdictionaries of the dictionary will be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckDictionary</td>
                    <td>Query dictionary details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateDictionary</td>
                    <td>Verifies whether the dictionary for the specified condition exists. The dictionary name and code are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDictionary</td>
                    <td>Query the dictionary list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Data Source Management</td>
                    <td>ListDatasourceTables</td>
                    <td>Obtain all tables in the data source</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatasourceInfo</td>
                    <td>Create a data source</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataourceDetail</td>
                    <td>Query data sources by data source ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatasourceColumns</td>
                    <td>Obtain all fields in a table in the data source</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDatasourceInfo</td>
                    <td>Modifying a Data Source</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatasourceInfoById</td>
                    <td>Deletes the specified data source information based on the data source ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatasources</td>
                    <td>Query the data source</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartTestDatasource</td>
                    <td>Test the data source connectivity</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Device group management</td>
                    <td>ShowDeviceGroupTree</td>
                    <td>Query all device groups</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceGroup</td>
                    <td>Delete a group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeviceGroup</td>
                    <td>Obtain the device group and lower-layer group information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddDeviceToGroup</td>
                    <td>Adding devices to a device group in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceFromGroup</td>
                    <td>Deleting a device from a device group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeviceGroup</td>
                    <td>Create a device group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceGroup</td>
                    <td>Modifying a device group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Device management</td>
                    <td>ShowAuthentication</td>
                    <td>Query device authentication information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDevice</td>
                    <td>Modifying device information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevices</td>
                    <td>This interface is used to obtain the list of registered GB/T 28181 devices.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendCommand</td>
                    <td>Send command</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubsets</td>
                    <td>Querying a subdevice</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetAuthentication</td>
                    <td>Reset device authentication information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchFreezeDevices</td>
                    <td>Batch device offline</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddSubsetsToGateway</td>
                    <td>Adding a subdevice to the gateway</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDevice</td>
                    <td>Create Device</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListShadows</td>
                    <td>Query the device shadow</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDevice</td>
                    <td>Query device details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDevice</td>
                    <td>This API is used to delete a specified device.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Domain name management</td>
                    <td>UpdateDomainV2</td>
                    <td>Modify the configuration information corresponding to the bound domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateCertificateV2</td>
                    <td>If the domain name certificate is no longer needed or has expired, you can delete the certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateCertificateV2</td>
                    <td>If the HTTPS request protocol is used for defining an API request during API creation, the SSL certificate must be added to the independent domain name.</td>
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
                    <td>DeleteEnvironmentVariableV2</td>
                    <td>Delete the specified environment variables.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfEnvironmentVariableV2</td>
                    <td>View details about a specified environment variable.</td>
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
                    <td rowspan="1">INSTANCE_MANAGEMENT</td>
                    <td>CheckRomaInstanceListV2</td>
                    <td>Obtain the service instance list that meets the conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ITaskController</td>
                    <td>DeleteTask</td>
                    <td>Delete a single task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTasks</td>
                    <td>Obtain the task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTask</td>
                    <td>Task modification interface, used to modify task configurations</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Instance Feature Management</td>
                    <td>CreateFeatureV2</td>
                    <td>Configure the required features for the instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFeaturesV2</td>
                    <td>View the DB instance feature list. Note: If the DB instance does not support the following features, contact technical support to upgrade the DB instance version.</td>
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
                    <td rowspan="2">MQS Instance Management</td>
                    <td>ShowMqsInstance</td>
                    <td>Query details about a specified MQS instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMqsInstance</td>
                    <td>Query the MQS instance list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Message management</td>
                    <td>ResetMessages</td>
                    <td>Resend the message.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMqsInstanceMessages</td>
                    <td>Query the offset and content of a message.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Monitoring information query</td>
                    <td>ListLatelyApiStatisticsV2</td>
                    <td>Query the number of times that an API is invoked based on the API ID and the latest period. The statistical period is 1 minute. The query scope is within one hour. One sample is per minute. The sample value is accumulated within one minute.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStatisticsApi</td>
                    <td>Query the API statistics of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">OpenAPI</td>
                    <td>ImportLiveDataApiDefinitionsV2</td>
                    <td>Import a customized backend API. The content of the imported file must comply with the swagger standard.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportApiDefinitionsV2</td>
                    <td>Import an API. The imported file must comply with the swagger standard.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportLiveDataApiDefinitionsV2</td>
                    <td>Export the customized backend API. The exported file content complies with the swagger standard.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportApiDefinitionsV2</td>
                    <td>Export the definition information of APIs in a group. The exported file content complies with the Swagger standard.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">PUBLIC_MANAGEMENT</td>
                    <td>CheckVersion</td>
                    <td>Obtains the API version with a specified version ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">Plug-in management</td>
                    <td>DeletePlugin</td>
                    <td>Delete the plug-in.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePlugin</td>
                    <td>Modifies plug-in information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlugin</td>
                    <td>Create plug-in information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPluginAttachedApis</td>
                    <td>Query information about the APIs bound to a specified plug-in</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlugins</td>
                    <td>Query details about a group of API Gateway plug-ins that meet the search criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachApiToPlugin</td>
                    <td>Bind the plug-in to the API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiAttachablePlugins</td>
                    <td>Query information about the plug-ins that can be bound to the current API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachApiFromPlugin</td>
                    <td>Unbind the API from the plug-in</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPluginAttachableApis</td>
                    <td>Query information about the APIs that can be bound to the current plug-in.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlugin</td>
                    <td>Query plug-in details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiAttachedPlugins</td>
                    <td>Query information about the plug-ins bound to a specified API</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachPluginFromApi</td>
                    <td>Unbind the plug-in from the API</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachPluginToApi</td>
                    <td>Bind the plug-in to the API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Product Management</td>
                    <td>ShowProductAuthentication</td>
                    <td>Query product authentication information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProductTopic</td>
                    <td>Adding a product theme</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProduct</td>
                    <td>Modifying product information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProductTopics</td>
                    <td>Query product theme</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProduct</td>
                    <td>Query product details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProducts</td>
                    <td>Query products</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevicesInProduct</td>
                    <td>Query the number of devices in a product</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProduct</td>
                    <td>Delete a product</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetProductAuthentication</td>
                    <td>Reset product authentication information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProduct</td>
                    <td>Create a product</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProductTopic</td>
                    <td>Update the product theme</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadProduct</td>
                    <td>Importing a Product</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadProducts</td>
                    <td>Export products</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProductTopic</td>
                    <td>Delete a product theme</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Product Template</td>
                    <td>ListProductTemplates</td>
                    <td>Query a product template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProductTemplate</td>
                    <td>Modifying a product template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProductTemplate</td>
                    <td>Create a product template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProductTemplate</td>
                    <td>Delete a product template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query version operation</td>
                    <td>ListVersion</td>
                    <td>Query the SMN API V2 version information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">Rule engine</td>
                    <td>CreateRule</td>
                    <td>Create Rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRule</td>
                    <td>Querying Rule Details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSources</td>
                    <td>Query the source data source list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSource</td>
                    <td>Delete the source data source</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteRules</td>
                    <td>Delete rules in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSource</td>
                    <td>Add source data source</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRule</td>
                    <td>Delete a rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DebugRule</td>
                    <td>Rule debugging</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDestination</td>
                    <td>Delete the target data source</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRule</td>
                    <td>Modifying a rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDestinations</td>
                    <td>Query the target data source list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDestination</td>
                    <td>Add the target data source</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRules</td>
                    <td>Query Rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">SSL Certificate Management</td>
                    <td>BatchAssociateDomainsV2</td>
                    <td>Domain name bound to the SSL certificate</td>
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
                    <td>BatchAssociateCertsV2</td>
                    <td>The domain name is bound to the SSL certificate. Currently, only one binding is supported. The certificate_ids field in the request body contains only one certificate ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAttachedDomainsV2</td>
                    <td>Obtain the list of domain names bound to the SSL certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificatesV2</td>
                    <td>Obtain the SSL certificate list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
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
                    <td rowspan="2">Service Job Management</td>
                    <td>ShowTask</td>
                    <td>This interface is used to query service jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopTask</td>
                    <td>This interface is used to stop a service job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="21">Service Management</td>
                    <td>ListProperties</td>
                    <td>Query attributes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResponseProperty</td>
                    <td>Modifying response attributes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateService</td>
                    <td>Create a service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCommand</td>
                    <td>Query command details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResponseProperty</td>
                    <td>Query response attribute details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResponseProperties</td>
                    <td>Query response attributes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRequestProperty</td>
                    <td>Create a request attribute</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateService</td>
                    <td>Modifying a service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProperty</td>
                    <td>Create attribute</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCommand</td>
                    <td>Modification command</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteService</td>
                    <td>Delete a service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResponseProperty</td>
                    <td>Response attribute creation</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCommand</td>
                    <td>Deletion command</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRequestProperty</td>
                    <td>Modifying request attributes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCommand</td>
                    <td>Create command</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRequestProperty</td>
                    <td>Delete request attribute</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServices</td>
                    <td>Query service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowService</td>
                    <td>Query service details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCommands</td>
                    <td>Query command</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRequestProperties</td>
                    <td>Query request attributes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResponseProperty</td>
                    <td>Deleting a response attribute</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Set Special Flow Control</td>
                    <td>ListSpecialThrottlingConfigurationsV2</td>
                    <td>View the special configuration of the throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSpecialThrottlingConfigurationV2</td>
                    <td>A throttling policy can limit the maximum number of times that an API can be accessed within a period of time, or the maximum number of times that a tenant or app can access an API within a period of time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSpecialThrottlingConfigurationV2</td>
                    <td>To delete a special configuration of a throttling policy, run the following command:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSpecialThrottlingConfigurationV2</td>
                    <td>Modify a special setting in a throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Signature Key Management</td>
                    <td>ListSignatureKeysV2</td>
                    <td>Query information about all signature keys.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSignatureKeyV2</td>
                    <td>Modifies the details about a specified signature key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSignatureKeyV2</td>
                    <td>Deletes a specified signature key. A signature key cannot be deleted if it is bound to an API. You need to unbind it from the API before deleting it.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSignatureKeyV2</td>
                    <td>To protect API security, it is recommended that tenants provide a protection mechanism for API access. That is, open APIs of tenants need to authenticate the request source. Requests that do not meet the authentication requirements are directly rejected.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Signing Key Binding Relationship Management</td>
                    <td>DisassociateSignatureKeyV2</td>
                    <td>Unbind the API from the signature key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisNotBoundWithSignatureKeyV2</td>
                    <td>Query the list of APIs that are not bound to the signature key. The API must have been published. Unpublished APIs will not be displayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisBindedToSignatureKeyV2</td>
                    <td>Query the list of APIs bound to a signature key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSignatureKeysBindedToApiV2</td>
                    <td>Query the list of signature keys bound to an API. Each API should be bound with a maximum of one signing key per environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateSignatureKeyV2</td>
                    <td>A signature key takes effect only after it is bound to an API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Subject Management</td>
                    <td>ListMqsInstanceTopics</td>
                    <td>Query the topic list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMqsInstanceTopic</td>
                    <td>Create a topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteMqsInstanceTopic</td>
                    <td>Delete topics in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportMqsInstanceTopic</td>
                    <td>Import a topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMqsInstanceTopic</td>
                    <td>Modify a topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportMqsInstanceTopic</td>
                    <td>Export a topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMqsInstanceTopic</td>
                    <td>Delete a topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Subscription management operation</td>
                    <td>ListNotification</td>
                    <td>This interface is used to query the subscription management information of a specified application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNotification</td>
                    <td>This interface is used to modify the specified subscription management.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNotification</td>
                    <td>This API is used to create device operations under the corresponding application in a specified instance and subscribe to the operation to the specified topic.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNotification</td>
                    <td>This interface is used to delete a specified subscription management.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tag Management</td>
                    <td>ListTagsV2</td>
                    <td>Query the tag list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">Task Management</td>
                    <td>ShowDispatches</td>
                    <td>Query scheduling plans</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InstallMultiTasks</td>
                    <td>Initialize combined tasks, assign task IDs, and initialize mapping</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCommonTask</td>
                    <td>Create a common task (different from a combined task)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDispatches</td>
                    <td>Create a scheduling plan</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDispatches</td>
                    <td>Modifying a scheduling plan by task ID and scheduling ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetMultiTaskOffset</td>
                    <td>Resetting the progress of a combined task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMultiTaskMappings</td>
                    <td>Create combined task mapping</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTask</td>
                    <td>Manually trigger task scheduling</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartOrStopTasks</td>
                    <td>Start/Stop Tasks in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMultiTasks</td>
                    <td>Modifying a combined task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountTasks</td>
                    <td>Count the number of tasks in different states of different types.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMultiTaskMapping</td>
                    <td>Delete a task mapping by mapping ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMultiTasks</td>
                    <td>Create a combined task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Task Monitor Management</td>
                    <td>ListMonitorLog</td>
                    <td>Query all logs of a single task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMonitorInfos</td>
                    <td>Query the monitoring information about all tasks</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Throttling Policy Management</td>
                    <td>UpdateRequestThrottlingPolicyV2</td>
                    <td>Modifies the details about a specified throttling policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRequestThrottlingPolicyV2</td>
                    <td>Deletes a specified throttling policy. If the throttling policy is bound to an API, you need to unbind the throttling policy from the API and then delete the throttling policy.</td>
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
                    <td>BatchDeleteThrottlingPolicyV2</td>
                    <td>Delete throttling policies in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRequestThrottlingPolicyV2</td>
                    <td>To query the information about all throttling policies</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Topic operation</td>
                    <td>ListTopics</td>
                    <td>Query the topic list by page. Topics are sorted in descending order by topic creation time. You can specify the offset and limit for pagination query. If no topic exists, an empty list is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">VPC Channel Management</td>
                    <td>DeleteBackendInstanceV2</td>
                    <td>Delete a backend instance from a specified VPC channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpcChannelV2</td>
                    <td>Delete a specified VPC channel</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMemberGroup</td>
                    <td>Create a VPC channel backend server group on the Service Integration page. You can determine whether to associate VPC channel backend instances with the backend instance server group to manage backend server nodes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHealthCheck</td>
                    <td>Modifies the VPC channel health check.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddingBackendInstancesV2</td>
                    <td>Adding a backend instance to a specified VPC channel</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfVpcChannelV2</td>
                    <td>View details about a specified VPC channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackendInstancesV2</td>
                    <td>View the list of backend instances in a specified VPC channel.</td>
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
                    <td>BatchDisableMembers</td>
                    <td>Failed to modify the status of backend servers in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpcChannelV2</td>
                    <td>In the service integration, create channels for connecting to private VPC resources. When creating an API, configure backend nodes to use these VPC channels so that the service integration can directly access private VPC resources.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchEnableMembers</td>
                    <td>Changing the status of backend servers in batches is available.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMemberGroup</td>
                    <td>Updates a specified VPC channel backend server group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDetailsOfMemberGroup</td>
                    <td>View details about a specified VPC channel backend server group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBackendInstancesV2</td>
                    <td>This API is used to update the backend instance of a specified VPC channel. During the update, the input request parameters are used to fully overwrite the backend instances of the corresponding cloud service group. If the ECS group to be modified is not specified, the system overwrites the entire ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcChannelsV2</td>
                    <td>View the VPC channel list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMemberGroup</td>
                    <td>Delete a specified VPC channel backend server group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">VPC channel management-project</td>
                    <td>CreateProjectVpcChannel</td>
                    <td>This API is used to create a VPC channel and associate it with multiple instances. The VPC channel name must be unique in the same project. Note: The instance feature vpc_name_modifiable is available only when it is set to off.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectVpcChannelsV2</td>
                    <td>Query the VPC channel list of all instances in a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectVpcChannelSyncs</td>
                    <td>This API is used to synchronize VPC channels to multiple instances. Note: The instance feature vpc_name_modifiable is available only when it is set to off.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProjectVpcChannel</td>
                    <td>This API is used to modify VPC channels in multiple instances in a project in batches based on the VPC channel name. If the VPC channel does not exist in the instance, create it. Note: The instance feature vpc_name_modifiable is available only when it is set to off.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
