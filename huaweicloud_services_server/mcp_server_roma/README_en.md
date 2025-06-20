# ROMA MCP Server 


## Version
v0.1.0

## Overview

ROMA MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ROMA. Full-chain management of ROMA resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| ACL Policy Management | UpdateAclStrategyV2 | Modifies the specified ACL policy. The following attributes can be modified: acl_name, acl_type, and acl_value. Other attributes cannot be modified. | To be tested |
|  | DeleteAclV2 | Delete a specified ACL policy. If an API is bound to the ACL policy, the ACL policy cannot be deleted. | To be tested |
|  | CreateAclStrategyV2 | Add an ACL policy. The policy type is specified by the acl_type field (permit or deny). The object type can be IP address or domain. The value of acl_value corresponding to domain is the tenant name. Not a network domain name like www.exampleDomain.com | To be tested |
|  | BatchDeleteAclV2 | Deletes multiple specified ACL policies in batches. | To be tested |
|  | ShowDetailsOfAclPolicyV2 | Query the details about a specified ACL policy. | To be tested |
|  | ListAclStrategiesV2 | Query all ACL policies. | To be tested |
| API Binding ACL Policy | CreateApiAclBindingV2 | Bind the API to the ACL policy. | To be tested |
|  | DeleteApiAclBindingV2 | Unbind an API from an ACL policy | To be tested |
|  | BatchDeleteApiAclBindingV2 | Unbind APIs from ACL policies in batches | To be tested |
|  | ListApisUnbindedToAclPolicyV2 | View the list of APIs that are not bound to the ACL policy. Ensure that the APIs have been published. | To be tested |
|  | ListApisBindedToAclPolicyV2 | View the list of APIs bound to the ACL policy. | To be tested |
|  | ListAclPolicyBindedToApiV2 | View the list of ACL policies bound to the API | To be tested |
| API Group Management | ShowDetailsOfApiGroupV2 | Query the details about a specified group. | To be tested |
|  | DeleteApiGroupV2 | Deletes a specified API group. | To be tested |
|  | CheckApiGroupsV2 | Verifies whether the API group name exists. | To be tested |
|  | UpdateApiGroupV2 | Modifies API group attributes. The name and remark attributes can be modified. Other attributes cannot be modified. | To be tested |
|  | CreateApiGroupV2 | API groups are management units of APIs. An API group is equivalent to a service entry. When an API group is created, a subdomain name is returned as the access entry. It is recommended that APIs in an API group be related to each other. | To be tested |
|  | ListApiGroupsV2 | Query the API group list. | To be tested |
| API bound throttling policy | DisassociateRequestThrottlingPolicyV2 | Unbind the API from the throttling policy. | To be tested |
|  | ListRequestThrottlingPoliciesBindedToApiV2 | Query the throttling policy list bound to an API. There should be only one flow control policy in each environment. | To be tested |
|  | AssociateRequestThrottlingPolicyV2 | Apply a throttling policy to an API. All accesses to the API will be restricted by the throttling policy. | To be tested |
|  | ListApisUnbindedToRequestThrottlingPolicyV2 | Query the list of all self-owned APIs that are not bound to the throttling policy. The API must have been published. Unpublished APIs will not be displayed. | To be tested |
|  | BatchDisassociateThrottlingPolicyV2 | Unbinding APIs from throttling policies in batches | To be tested |
|  | ListApisBindedToRequestThrottlingPolicyV2 | Query the list of APIs bound to a throttling policy. | To be tested |
| API management | DeleteApiV2 | Delete a specified API. | To be tested |
|  | ListApisV2 | View the API list. API details and release information is returned, but backend service information is not displayed. | To be tested |
|  | CreateOrDeletePublishRecordForApiV2 | Publish or bring an API offline. | To be tested |
|  | ListApiVersionDetailV2 | Query the details of a specified version. | To be tested |
|  | ChangeApiVersionV2 | A version is generated based on the current API definition each time an API is published. The version records the definitions and status of APIs when they are published. | To be tested |
|  | ListApiVersionsV2 | Query the historical versions of an API. Each API can have a maximum of 10 historical versions in an environment. | To be tested |
|  | DebugApiV2 | This API is used to debug the definition of an API in the specified running environment. The API caller must have the permission to operate the API. | To be tested |
|  | BatchPublishOrOfflineApiV2 | Publish multiple APIs to a specified environment or take multiple APIs offline from a specified environment. | To be tested |
|  | ShowDetailsOfApiV2 | View the details about a specified API. | To be tested |
|  | ListApiRuntimeDefinitionV2 | View the runtime definition of a specified API in the specified environment. By default, the runtime definition in the RELEASE environment is queried. | To be tested |
|  | UpdateApiV2 | Modifies the information about a specified API, including backend service information. | To be tested |
|  | CheckApisV2 | Verify the API definition. Check whether the path or name of the API already exists. | To be tested |
|  | CreateApiV2 | Add an API. An API is a service interface and specific service capabilities. | To be tested |
|  | DeleteApiByVersionIdV2 | You can take an effective API version offline. After the API version is brought offline, the API cannot be invoked in the environment where the version takes effect. | To be tested |
| APPLICATION_MANAGEMENT | CheckRomaAppDetails | Query application details | To be tested |
|  | AddUserToApp | - Set the user members of the application. If the array is empty, the existing application member list will be cleared. | To be tested |
|  | ListRomaApp | Query the application list. Query by conditions is supported. All conditions are in the AND relationship. | To be tested |
|  | ResetRomaAppSecret | Reset the application key | To be tested |
|  | DeleteRomaApp | Delete a single application | To be tested |
|  | CheckCanAuthUsersOfApp | Query the candidate user list of the application. Abnormal users will be filtered out. | To be tested |
|  | CreateRomaApp | Create Application | To be tested |
|  | ValidateRomaApp | Check whether the application that meets the specified conditions exists. | To be tested |
|  | UpdateRomaApp | Update application | To be tested |
|  | CheckRomaAppSecret | Query the application key | To be tested |
|  | CheckAuthUsersOfApp | Query the user list | To be tested |
| ASSET_MANAGEMENT | CheckAssetJobStatus | Querying the job progress | To be tested |
|  | DeleteAsset | Delete assets in batches | To be tested |
|  | ImportAsset | -Create an asset import task. The asset version and specific assets are read from the asset content. | To be tested |
|  | ExportAsset | Exporting assets in batches | To be tested |
|  | DownloadAssetArchive | -After an export job is successfully executed, this API is used to obtain the asset package generated by the export job. The asset package can be downloaded only once. | To be tested |
| App Authorization Management | ListDuplicateApisForAppV2 | Query the list of APIs with conflicting paths in a specified app. | To be tested |
|  | CancelingAuthorizationV2 | This API is used to cancel the authorization relationship between an API and an app. After the authorization is canceled, the app cannot invoke the API any longer. | To be tested |
|  | ListApisUnbindedToAppV2 | Query the list of APIs that are not bound to an app in a specified environment, including self-owned APIs and APIs purchased from the Marketplace. | To be tested |
|  | ListAppsBindedToApiV2 | Query the list of apps bound to an API. | To be tested |
|  | CreateAuthorizingAppsV2 | After an app is created, it cannot access an API. To access an API in an environment, you need to authorize the API in the environment to the app. After the authorization is successful, the app can access the API in the environment. | To be tested |
|  | ListApisBindedToAppV2 | Query the list of APIs bound to an app. | To be tested |
| App Permission Management | UpdateTopicAccessPolicy | Update the topic permission. | To be tested |
|  | ShowMqsInstanceTopicAccessPolicy | Query the topic permission. | To be tested |
| Application Configuration Management | UpdateAppConfigV2 | Modifying Application Configuration | To be tested |
|  | DeleteAppConfigV2 | Delete application configuration | To be tested |
|  | CreateAppConfigV2 | Create Application Configuration | To be tested |
|  | ShowDetailsOfAppConfigV2 | Viewing Application Configuration Details | To be tested |
|  | ListAppConfigsV2 | Query the application configuration list | To be tested |
| Client Configuration | ShowAppBoundAppQuota | View the application quota associated with a specified client application. | To be tested |
|  | ShowDetailsOfAppAcl | View the access control details of the app. | To be tested |
|  | DeleteAppCodeV2 | The App Code is deleted. After the App Code is deleted, the corresponding APIs cannot be accessed through simple authentication. | To be tested |
|  | CreateAppCodeAutoV2 | When creating an app code, you do not need to specify the value. The background automatically generates a random character string to fill in the value. | To be tested |
|  | ShowDetailsOfAppV2 | View detailed information about a specified app. | To be tested |
|  | CreateAppCodeV2 | App Code is a submodule of an app. After an app code is created, simple app authentication can be implemented. | To be tested |
|  | UpdateAppAcl | Set the access control configured on the client. | To be tested |
|  | DeleteAppAcl | Delete the access control information configured on the client. | To be tested |
|  | ListAppsV2 | Query the app list. | To be tested |
|  | ListAppCodesV2 | Query the app code list. | To be tested |
|  | ShowDetailsOfAppCodeV2 | App Code is a submodule of an app. After an app code is created, simple app authentication can be implemented. | To be tested |
| Client Quota | UpdateAppQuota | Modifying the Client Quota | To be tested |
|  | ListAppQuotas | Obtain the client quota list. Fuzzy query by name is supported. | To be tested |
|  | CreateAppQuota | Create Client Quota | To be tested |
|  | ListAppQuotaBindableApps | Query the list of client applications to which the client quota can be bound. Fuzzy search by client application name is supported. | To be tested |
|  | DisassociateAppQuotaWithApp | Unbind the client quota from the client application | To be tested |
|  | ListAppQuotaBoundApps | Query the list of client applications bound to the client quota. Fuzzy match by client application name is supported. | To be tested |
|  | AssociateAppsForAppQuota | List of client applications bound to the client quota | To be tested |
|  | ShowAppQuota | Obtain the client quota details | To be tested |
|  | DeleteAppQuota | Delete a client quota. When deleting the client quota, delete the association between the client quota and the client application. | To be tested |
| Configuration Management | ListProjectCofigsV2 | Query the tenant configuration list of an instance. You can use this API to view the resource configuration and usage of each type of resource. | To be tested |
| Custom Backend Service | DebugLiveDataApiV2 | Check whether the backend API is available. | To be tested |
|  | PublishLiveDataApiV2 | Deploy backend APIs in an instance. | To be tested |
|  | UpdateLiveDataApiV2 | Updates backend API parameters in an instance. | To be tested |
|  | ListLiveDataDataSourcesV2 | Query the list of customized backend service data sources. | To be tested |
|  | ListLiveDataApiDeploymentHistoryV2 | Query the deployment records of backend APIs in an instance. | To be tested |
|  | DeleteLiveDataApiV2 | This API is used to delete a backend API from an instance. | To be tested |
|  | CheckLivedataApisV2 | Verify the definition of the customized backend API. Check whether the path or name of the custom backend API already exists. | To be tested |
|  | ListLiveDataQuotaV2 | Query the quota of a user-defined backend service. | To be tested |
|  | UnpublishLiveDataApiV2 | Undeploy backend APIs in an instance. | To be tested |
|  | CreateLiveDataApiScriptV2 | Create a backend API script in an instance. | To be tested |
|  | CreateLiveDataApiV2 | Create a backend API in an instance. | To be tested |
|  | ShowLiveDataApiV2 | Query details about a backend API. | To be tested |
|  | ListLiveDataApiTestHistoryV2 | Query the backend API test result in an instance. | To be tested |
|  | ListLiveDataApiV2 | Obtains all backend APIs in an instance. | To be tested |
| Customized Authentication Management | ShowDetailsOfCustomAuthorizersV2 | Viewing the details of the customized authentication | To be tested |
|  | ListCustomAuthorizersV2 | Query the user-defined authentication list | To be tested |
|  | CreateCustomAuthorizerV2 | Create a user-defined authentication | To be tested |
|  | UpdateCustomAuthorizerV2 | Modifying a user-defined authentication | To be tested |
|  | DeleteCustomAuthorizerV2 | Delete user-defined authentication | To be tested |
| DICTIONARY_MANAGEMENT | UpdateDictionary | Update dictionary | To be tested |
|  | CreateDictionary | creation dictionary | To be tested |
|  | DeleteDictionary | When a single dictionary is deleted, all subdictionaries of the dictionary will be deleted. | To be tested |
|  | CheckDictionary | Query dictionary details. | To be tested |
|  | ValidateDictionary | Verifies whether the dictionary for the specified condition exists. The dictionary name and code are supported. | To be tested |
|  | ListDictionary | Query the dictionary list | To be tested |
| Data Source Management | ListDatasourceTables | Obtain all tables in the data source | To be tested |
|  | CreateDatasourceInfo | Create a data source | To be tested |
|  | ShowDataourceDetail | Query data sources by data source ID | To be tested |
|  | ListDatasourceColumns | Obtain all fields in a table in the data source | To be tested |
|  | UpdateDatasourceInfo | Modifying a Data Source | To be tested |
|  | DeleteDatasourceInfoById | Deletes the specified data source information based on the data source ID. | To be tested |
|  | ListDatasources | Query the data source | To be tested |
|  | StartTestDatasource | Test the data source connectivity | To be tested |
| Device group management | ShowDeviceGroupTree | Query all device groups | To be tested |
|  | DeleteDeviceGroup | Delete a group | To be tested |
|  | ShowDeviceGroup | Obtain the device group and lower-layer group information. | To be tested |
|  | BatchAddDeviceToGroup | Adding devices to a device group in batches | To be tested |
|  | DeleteDeviceFromGroup | Deleting a device from a device group | To be tested |
|  | CreateDeviceGroup | Create a device group | To be tested |
|  | UpdateDeviceGroup | Modifying a device group | To be tested |
| Device management | ShowAuthentication | Query device authentication information | To be tested |
|  | UpdateDevice | Modifying device information | To be tested |
|  | ListDevices | This interface is used to obtain the list of registered GB/T 28181 devices. | To be tested |
|  | SendCommand | Send command | To be tested |
|  | ListSubsets | Querying a subdevice | To be tested |
|  | ResetAuthentication | Reset device authentication information | To be tested |
|  | BatchFreezeDevices | Batch device offline | To be tested |
|  | AddSubsetsToGateway | Adding a subdevice to the gateway | To be tested |
|  | CreateDevice | Create Device | To be tested |
|  | ListShadows | Query the device shadow | To be tested |
|  | ShowDevice | Query device details | To be tested |
|  | DeleteDevice | This API is used to delete a specified device. | To be tested |
| Domain name management | UpdateDomainV2 | Modify the configuration information corresponding to the bound domain name. | To be tested |
|  | DisassociateCertificateV2 | If the domain name certificate is no longer needed or has expired, you can delete the certificate. | To be tested |
|  | AssociateCertificateV2 | If the HTTPS request protocol is used for defining an API request during API creation, the SSL certificate must be added to the independent domain name. | To be tested |
|  | ShowDetailsOfDomainNameCertificateV2 | View details about the certificate bound to the domain name. | To be tested |
|  | DisassociateDomainV2 | If an API group does not need to be bound to a user-defined domain name, you can unbind the domain name from the API group. | To be tested |
|  | AssociateDomainV2 | User-defined domain name, which takes effect only after the CNAME is added to the subdomain name of the API group. | To be tested |
| Environment variable management | CreateEnvironmentVariableV2 | After an API is released to different environments, the environment variables, such as the API service deployment address and request version number, may vary according to the environment. | To be tested |
|  | DeleteEnvironmentVariableV2 | Delete the specified environment variables. | To be tested |
|  | ShowDetailsOfEnvironmentVariableV2 | View details about a specified environment variable. | To be tested |
|  | UpdateEnvironmentVariableV2 | Modify environment variables. If an environment variable references the backend service address of an API, modifying the environment variable will release all APIs that use the variable again. | To be tested |
|  | ListEnvironmentVariablesV2 | Query the list of all environment variables in a group. | To be tested |
| Environmental Management | DeleteEnvironmentV2 | Delete the specified environment. | To be tested |
|  | ListEnvironmentsV2 | Query the environment list that meets the conditions. | To be tested |
|  | UpdateEnvironmentV2 | Modifies the information about a specified environment. The name and remark attributes can be modified. Other attributes cannot be modified. | To be tested |
|  | CreateEnvironmentV2 | In actual production, an API provider may have multiple environments, such as the development environment, test environment, and production environment. You can release APIs to an environment for callers to invoke. | To be tested |
| INSTANCE_MANAGEMENT | CheckRomaInstanceListV2 | Obtain the service instance list that meets the conditions. | To be tested |
| ITaskController | DeleteTask | Delete a single task | To be tested |
|  | ListTasks | Obtain the task list | To be tested |
|  | UpdateTask | Task modification interface, used to modify task configurations | To be tested |
| Instance Feature Management | CreateFeatureV2 | Configure the required features for the instance. | To be tested |
|  | ListFeaturesV2 | View the DB instance feature list. Note: If the DB instance does not support the following features, contact technical support to upgrade the DB instance version. | To be tested |
| Instance Management | ShowRestrictionOfInstanceV2 | View the instance constraint information | To be tested |
|  | ShowDetailsOfInstanceV2 | Viewing DB Instance Details | To be tested |
| MQS Instance Management | ShowMqsInstance | Query details about a specified MQS instance. | To be tested |
|  | ListMqsInstance | Query the MQS instance list. | To be tested |
| Message management | ResetMessages | Resend the message. | To be tested |
|  | ShowMqsInstanceMessages | Query the offset and content of a message. | To be tested |
| Monitoring information query | ListLatelyApiStatisticsV2 | Query the number of times that an API is invoked based on the API ID and the latest period. The statistical period is 1 minute. The query scope is within one hour. One sample is per minute. The sample value is accumulated within one minute. | To be tested |
|  | ListStatisticsApi | Query the API statistics of an instance. | To be tested |
| OpenAPI | ImportLiveDataApiDefinitionsV2 | Import a customized backend API. The content of the imported file must comply with the swagger standard.  | To be tested |
|  | ImportApiDefinitionsV2 | Import an API. The imported file must comply with the swagger standard.  | To be tested |
|  | ExportLiveDataApiDefinitionsV2 | Export the customized backend API. The exported file content complies with the swagger standard. | To be tested |
|  | ExportApiDefinitionsV2 | Export the definition information of APIs in a group. The exported file content complies with the Swagger standard. | To be tested |
| PUBLIC_MANAGEMENT | CheckVersion | Obtains the API version with a specified version ID. | To be tested |
| Plug-in management | DeletePlugin | Delete the plug-in. | To be tested |
|  | UpdatePlugin | Modifies plug-in information. | To be tested |
|  | CreatePlugin | Create plug-in information. | To be tested |
|  | ListPluginAttachedApis | Query information about the APIs bound to a specified plug-in | To be tested |
|  | ListPlugins | Query details about a group of API Gateway plug-ins that meet the search criteria. | To be tested |
|  | AttachApiToPlugin | Bind the plug-in to the API. | To be tested |
|  | ListApiAttachablePlugins | Query information about the plug-ins that can be bound to the current API. | To be tested |
|  | DetachApiFromPlugin | Unbind the API from the plug-in | To be tested |
|  | ListPluginAttachableApis | Query information about the APIs that can be bound to the current plug-in. | To be tested |
|  | ShowPlugin | Query plug-in details. | To be tested |
|  | ListApiAttachedPlugins | Query information about the plug-ins bound to a specified API | To be tested |
|  | DetachPluginFromApi | Unbind the plug-in from the API | To be tested |
|  | AttachPluginToApi | Bind the plug-in to the API. | To be tested |
| Product Management | ShowProductAuthentication | Query product authentication information | To be tested |
|  | CreateProductTopic | Adding a product theme | To be tested |
|  | UpdateProduct | Modifying product information | To be tested |
|  | ListProductTopics | Query product theme | To be tested |
|  | ShowProduct | Query product details | To be tested |
|  | ListProducts | Query products | To be tested |
|  | ListDevicesInProduct | Query the number of devices in a product | To be tested |
|  | DeleteProduct | Delete a product | To be tested |
|  | ResetProductAuthentication | Reset product authentication information | To be tested |
|  | CreateProduct | Create a product | To be tested |
|  | UpdateProductTopic | Update the product theme | To be tested |
|  | UploadProduct | Importing a Product | To be tested |
|  | DownloadProducts | Export products | To be tested |
|  | DeleteProductTopic | Delete a product theme | To be tested |
| Product Template | ListProductTemplates | Query a product template | To be tested |
|  | UpdateProductTemplate | Modifying a product template | To be tested |
|  | CreateProductTemplate | Create a product template | To be tested |
|  | DeleteProductTemplate | Delete a product template | To be tested |
| Query version operation | ListVersion | Query the SMN API V2 version information. | To be tested |
| Rule engine | CreateRule | Create Rule | To be tested |
|  | ShowRule | Querying Rule Details | To be tested |
|  | ListSources | Query the source data source list | To be tested |
|  | DeleteSource | Delete the source data source | To be tested |
|  | BatchDeleteRules | Delete rules in batches | To be tested |
|  | CreateSource | Add source data source | To be tested |
|  | DeleteRule | Delete a rule | To be tested |
|  | DebugRule | Rule debugging | To be tested |
|  | DeleteDestination | Delete the target data source | To be tested |
|  | UpdateRule | Modifying a rule | To be tested |
|  | ListDestinations | Query the target data source list | To be tested |
|  | CreateDestination | Add the target data source | To be tested |
|  | ListRules | Query Rule | To be tested |
| SSL Certificate Management | BatchAssociateDomainsV2 | Domain name bound to the SSL certificate | To be tested |
|  | UpdateCertificateV2 | Modifying the SSL Certificate | To be tested |
|  | CreateCertificateV2 | Create an SSL certificate | To be tested |
|  | BatchAssociateCertsV2 | The domain name is bound to the SSL certificate. Currently, only one binding is supported. The certificate_ids field in the request body contains only one certificate ID. | To be tested |
|  | ListAttachedDomainsV2 | Obtain the list of domain names bound to the SSL certificate. | To be tested |
|  | ListCertificatesV2 | Obtain the SSL certificate list. | To be tested |
|  | BatchDisassociateDomainsV2 | Unbind an SSL certificate from a domain name | To be tested |
|  | ShowDetailsOfCertificateV2 | Viewing Certificate Details | To be tested |
|  | DeleteCertificateV2 | This API is used to delete an SSL certificate. Only the certificate that is not associated with a domain name can be deleted. | To be tested |
|  | BatchDisassociateCertsV2 | This API is used to unbind an SSL certificate from a domain name. Currently, only one certificate can be unbound. The certificate_ids field in the request body contains only one certificate ID. | To be tested |
| Service Job Management | ShowTask | This interface is used to query service jobs. | To be tested |
|  | StopTask | This interface is used to stop a service job. | To be tested |
| Service Management | ListProperties | Query attributes | To be tested |
|  | UpdateResponseProperty | Modifying response attributes | To be tested |
|  | CreateService | Create a service | To be tested |
|  | ShowCommand | Query command details | To be tested |
|  | ShowResponseProperty | Query response attribute details | To be tested |
|  | ListResponseProperties | Query response attributes | To be tested |
|  | CreateRequestProperty | Create a request attribute | To be tested |
|  | UpdateService | Modifying a service | To be tested |
|  | CreateProperty | Create attribute | To be tested |
|  | UpdateCommand | Modification command | To be tested |
|  | DeleteService | Delete a service | To be tested |
|  | CreateResponseProperty | Response attribute creation | To be tested |
|  | DeleteCommand | Deletion command | To be tested |
|  | UpdateRequestProperty | Modifying request attributes | To be tested |
|  | CreateCommand | Create command | To be tested |
|  | DeleteRequestProperty | Delete request attribute | To be tested |
|  | ListServices | Query service | To be tested |
|  | ShowService | Query service details | To be tested |
|  | ListCommands | Query command | To be tested |
|  | ListRequestProperties | Query request attributes | To be tested |
|  | DeleteResponseProperty | Deleting a response attribute | To be tested |
| Set Special Flow Control | ListSpecialThrottlingConfigurationsV2 | View the special configuration of the throttling policy. | To be tested |
|  | CreateSpecialThrottlingConfigurationV2 | A throttling policy can limit the maximum number of times that an API can be accessed within a period of time, or the maximum number of times that a tenant or app can access an API within a period of time. | To be tested |
|  | DeleteSpecialThrottlingConfigurationV2 | To delete a special configuration of a throttling policy, run the following command: | To be tested |
|  | UpdateSpecialThrottlingConfigurationV2 | Modify a special setting in a throttling policy. | To be tested |
| Signature Key Management | ListSignatureKeysV2 | Query information about all signature keys. | To be tested |
|  | UpdateSignatureKeyV2 | Modifies the details about a specified signature key. | To be tested |
|  | DeleteSignatureKeyV2 | Deletes a specified signature key. A signature key cannot be deleted if it is bound to an API. You need to unbind it from the API before deleting it. | To be tested |
|  | CreateSignatureKeyV2 | To protect API security, it is recommended that tenants provide a protection mechanism for API access. That is, open APIs of tenants need to authenticate the request source. Requests that do not meet the authentication requirements are directly rejected. | To be tested |
| Signing Key Binding Relationship Management | DisassociateSignatureKeyV2 | Unbind the API from the signature key. | To be tested |
|  | ListApisNotBoundWithSignatureKeyV2 | Query the list of APIs that are not bound to the signature key. The API must have been published. Unpublished APIs will not be displayed. | To be tested |
|  | ListApisBindedToSignatureKeyV2 | Query the list of APIs bound to a signature key. | To be tested |
|  | ListSignatureKeysBindedToApiV2 | Query the list of signature keys bound to an API. Each API should be bound with a maximum of one signing key per environment. | To be tested |
|  | AssociateSignatureKeyV2 | A signature key takes effect only after it is bound to an API. | To be tested |
| Subject Management | ListMqsInstanceTopics | Query the topic list. | To be tested |
|  | CreateMqsInstanceTopic | Create a topic. | To be tested |
|  | BatchDeleteMqsInstanceTopic | Delete topics in batches. | To be tested |
|  | ImportMqsInstanceTopic | Import a topic. | To be tested |
|  | UpdateMqsInstanceTopic | Modify a topic. | To be tested |
|  | ExportMqsInstanceTopic | Export a topic. | To be tested |
|  | DeleteMqsInstanceTopic | Delete a topic. | To be tested |
| Subscription management operation | ListNotification | This interface is used to query the subscription management information of a specified application. | To be tested |
|  | UpdateNotification | This interface is used to modify the specified subscription management. | To be tested |
|  | CreateNotification | This API is used to create device operations under the corresponding application in a specified instance and subscribe to the operation to the specified topic. | To be tested |
|  | DeleteNotification | This interface is used to delete a specified subscription management. | To be tested |
| Tag Management | ListTagsV2 | Query the tag list | To be tested |
| Task Management | ShowDispatches | Query scheduling plans | To be tested |
|  | InstallMultiTasks | Initialize combined tasks, assign task IDs, and initialize mapping | To be tested |
|  | CreateCommonTask | Create a common task (different from a combined task) | To be tested |
|  | CreateDispatches | Create a scheduling plan | To be tested |
|  | UpdateDispatches | Modifying a scheduling plan by task ID and scheduling ID | To be tested |
|  | ResetMultiTaskOffset | Resetting the progress of a combined task | To be tested |
|  | CreateMultiTaskMappings | Create combined task mapping | To be tested |
|  | RunTask | Manually trigger task scheduling | To be tested |
|  | BatchStartOrStopTasks | Start/Stop Tasks in Batches | To be tested |
|  | UpdateMultiTasks | Modifying a combined task | To be tested |
|  | CountTasks | Count the number of tasks in different states of different types. | To be tested |
|  | DeleteMultiTaskMapping | Delete a task mapping by mapping ID | To be tested |
|  | CreateMultiTasks | Create a combined task | To be tested |
| Task Monitor Management | ListMonitorLog | Query all logs of a single task | To be tested |
|  | ListMonitorInfos | Query the monitoring information about all tasks | To be tested |
| Throttling Policy Management | UpdateRequestThrottlingPolicyV2 | Modifies the details about a specified throttling policy. | To be tested |
|  | DeleteRequestThrottlingPolicyV2 | Deletes a specified throttling policy. If the throttling policy is bound to an API, you need to unbind the throttling policy from the API and then delete the throttling policy. | To be tested |
|  | ShowDetailsOfRequestThrottlingPolicyV2 | View the details about a specified throttling policy. | To be tested |
|  | CreateRequestThrottlingPolicyV2 | After an API is brought online, the system provides a default throttling policy for each API. API providers can change the throttling policy based on the API service capability and load status. | To be tested |
|  | BatchDeleteThrottlingPolicyV2 | Delete throttling policies in batches. | To be tested |
|  | ListRequestThrottlingPolicyV2 | To query the information about all throttling policies | To be tested |
| Topic operation | ListTopics | Query the topic list by page. Topics are sorted in descending order by topic creation time. You can specify the offset and limit for pagination query. If no topic exists, an empty list is returned. | To be tested |
| VPC Channel Management | DeleteBackendInstanceV2 | Delete a backend instance from a specified VPC channel. | To be tested |
|  | DeleteVpcChannelV2 | Delete a specified VPC channel | To be tested |
|  | CreateMemberGroup | Create a VPC channel backend server group on the Service Integration page. You can determine whether to associate VPC channel backend instances with the backend instance server group to manage backend server nodes. | To be tested |
|  | UpdateHealthCheck | Modifies the VPC channel health check. | To be tested |
|  | AddingBackendInstancesV2 | Adding a backend instance to a specified VPC channel | To be tested |
|  | ShowDetailsOfVpcChannelV2 | View details about a specified VPC channel. | To be tested |
|  | ListBackendInstancesV2 | View the list of backend instances in a specified VPC channel. | To be tested |
|  | UpdateVpcChannelV2 | Updates the parameters of a specified VPC channel. | To be tested |
|  | ListMemberGroups | Query the list of backend cloud service groups in a VPC channel | To be tested |
|  | BatchDisableMembers | Failed to modify the status of backend servers in batches. | To be tested |
|  | CreateVpcChannelV2 | In the service integration, create channels for connecting to private VPC resources. When creating an API, configure backend nodes to use these VPC channels so that the service integration can directly access private VPC resources. | To be tested |
|  | BatchEnableMembers | Changing the status of backend servers in batches is available. | To be tested |
|  | UpdateMemberGroup | Updates a specified VPC channel backend server group | To be tested |
|  | ShowDetailsOfMemberGroup | View details about a specified VPC channel backend server group. | To be tested |
|  | UpdateBackendInstancesV2 | This API is used to update the backend instance of a specified VPC channel. During the update, the input request parameters are used to fully overwrite the backend instances of the corresponding cloud service group. If the ECS group to be modified is not specified, the system overwrites the entire ECS group. | To be tested |
|  | ListVpcChannelsV2 | View the VPC channel list | To be tested |
|  | DeleteMemberGroup | Delete a specified VPC channel backend server group. | To be tested |
| VPC channel management-project | CreateProjectVpcChannel | This API is used to create a VPC channel and associate it with multiple instances. The VPC channel name must be unique in the same project. Note: The instance feature vpc_name_modifiable is available only when it is set to off. | To be tested |
|  | ListProjectVpcChannelsV2 | Query the VPC channel list of all instances in a project | To be tested |
|  | CreateProjectVpcChannelSyncs | This API is used to synchronize VPC channels to multiple instances. Note: The instance feature vpc_name_modifiable is available only when it is set to off. | To be tested |
|  | UpdateProjectVpcChannel | This API is used to modify VPC channels in multiple instances in a project in batches based on the VPC channel name. If the VPC channel does not exist in the instance, create it. Note: The instance feature vpc_name_modifiable is available only when it is set to off. | To be tested |

