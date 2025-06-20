# APIG MCP Server 


## Version
v0.1.0

## Overview

APIG MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service APIG. Full-chain management of APIG resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| ACL Policy Management | DeleteAclV2 | Delete a specified ACL policy. If an API is bound to the ACL policy, the ACL policy cannot be deleted. | To be tested |
|  | ShowDetailsOfAclPolicyV2 | Query the details about a specified ACL policy. | To be tested |
|  | ListAclStrategiesV2 | Query all ACL policies. | To be tested |
|  | UpdateAclStrategyV2 | Modifies the specified ACL policy. The following attributes can be modified: acl_name, acl_type, and acl_value. Other attributes cannot be modified. | To be tested |
|  | CreateAclStrategyV2 | Add an ACL policy. The policy type is specified by the acl_type field (permit or deny). The object type can be IP address or domain. The value of acl_value corresponding to domain is the tenant name. Not a network domain name like www.exampleDomain.com | To be tested |
|  | BatchDeleteAclV2 | Deletes multiple specified ACL policies in batches. | To be tested |
| API Binding ACL Policy | BatchDeleteApiAclBindingV2 | Unbind APIs from ACL policies in batches | To be tested |
|  | CreateApiAclBindingV2 | Bind the API to the ACL policy. | To be tested |
|  | ListApisBindedToAclPolicyV2 | View the list of APIs bound to the ACL policy. | To be tested |
|  | ListApisUnbindedToAclPolicyV2 | View the list of APIs that are not bound to the ACL policy. Ensure that the APIs have been published. | To be tested |
|  | ListAclPolicyBindedToApiV2 | View the list of ACL policies bound to the API | To be tested |
|  | DeleteApiAclBindingV2 | Unbind an API from an ACL policy | To be tested |
| API Group Management | CheckApiGroupsV2 | Verifies whether the API group name exists. | To be tested |
|  | ListApiGroupsV2 | Query the API group list. | To be tested |
|  | DeleteApiGroupV2 | Deletes a specified API group. | To be tested |
|  | CreateApiGroupV2 | API groups are management units of APIs. An API group is equivalent to a service entry. When an API group is created, a subdomain name is returned as the access entry. It is recommended that APIs in an API group be related to each other. | To be tested |
|  | ShowDetailsOfApiGroupV2 | Query the details about a specified group. | To be tested |
|  | UpdateApiGroupV2 | Modifies API group attributes. The name and remark attributes can be modified. Other attributes cannot be modified. | To be tested |
| API bound throttling policy | BatchDisassociateThrottlingPolicyV2 | Unbinding APIs from throttling policies in batches | To be tested |
|  | DisassociateRequestThrottlingPolicyV2 | Unbind the API from the throttling policy. | To be tested |
|  | ListApisBindedToRequestThrottlingPolicyV2 | Query the list of APIs bound to a throttling policy. | To be tested |
|  | ListRequestThrottlingPoliciesBindedToApiV2 | Query the throttling policy list bound to an API. There should be only one flow control policy in each environment. | To be tested |
|  | AssociateRequestThrottlingPolicyV2 | Apply a throttling policy to an API. All accesses to the API will be restricted by the throttling policy. | To be tested |
|  | ListApisUnbindedToRequestThrottlingPolicyV2 | Query the list of all self-owned APIs that are not bound to the throttling policy. The API must have been published. Unpublished APIs will not be displayed. | To be tested |
| API management | ListApiVersionDetailV2 | Query the details of a specified version. | To be tested |
|  | CreateApiV2 | Add an API. An API is a service interface and specific service capabilities. | To be tested |
|  | ListApiRuntimeDefinitionV2 | View the runtime definition of a specified API in the specified environment. By default, the runtime definition in the RELEASE environment is queried. | To be tested |
|  | ListApisV2 | View the API list. API details and release information is returned, but backend service information is not displayed. | To be tested |
|  | ChangeApiVersionV2 | A version is generated based on the current API definition each time an API is published. The version records the definitions and status of APIs when they are published. | To be tested |
|  | DeleteApiByVersionIdV2 | You can take an effective API version offline. After the API version is brought offline, the API cannot be invoked in the environment where the version takes effect. | To be tested |
|  | CreateOrDeletePublishRecordForApiV2 | Publish or bring an API offline. | To be tested |
|  | ListApiVersionsV2 | Query the historical versions of an API. Each API can have a maximum of 10 historical versions in an environment. | To be tested |
|  | BatchPublishOrOfflineApiV2 | Publish multiple APIs to a specified environment or take multiple APIs offline from a specified environment. | To be tested |
|  | CheckApisV2 | Verify the API definition. Check whether the path or name of the API already exists. | To be tested |
|  | ShowDetailsOfApiV2 | View the details about a specified API. | To be tested |
|  | UpdateApiV2 | Modifies the information about a specified API, including backend service information. | To be tested |
|  | DeleteApiV2 | Delete a specified API. | To be tested |
|  | DebugApiV2 | This API is used to debug the definition of an API in the specified running environment. The API caller must have the permission to operate the API. | To be tested |
| App Authorization Management | ListApisBindedToAppV2 | Query the list of APIs bound to an app. | To be tested |
|  | ListApisUnbindedToAppV2 | Query the list of APIs that are not bound to an app in a specified environment, including self-owned APIs and APIs purchased from the Marketplace. | To be tested |
|  | CreateAuthorizingAppsV2 | After an app is created, it cannot access an API. To access an API in an environment, you need to authorize the API in the environment to the app. After the authorization is successful, the app can access the API in the environment. | To be tested |
|  | CancelingAuthorizationV2 | This API is used to cancel the authorization relationship between an API and an app. After the authorization is canceled, the app cannot invoke the API any longer. | To be tested |
|  | ListAppsBindedToApiV2 | Query the list of apps bound to an API. | To be tested |
| App Template Management | ListApps | Query the application template list | To be tested |
| Client Configuration | DeleteAppCodeV2 | The App Code is deleted. After the App Code is deleted, the corresponding APIs cannot be accessed through simple authentication. | To be tested |
|  | CreateAppCodeV2 | App Code is a submodule of an app. After an app code is created, simple app authentication can be implemented. | To be tested |
|  | ListAppsV2 | Query the app list. | To be tested |
|  | UpdateAppAcl | Set the access control configured on the client. | To be tested |
|  | ShowDetailsOfAppCodeV2 | App Code is a submodule of an app. After an app code is created, simple app authentication can be implemented. | To be tested |
|  | DeleteAppAcl | Delete the access control information configured on the client. | To be tested |
|  | ShowDetailsOfAppV2 | View detailed information about a specified app. | To be tested |
|  | ShowAppBoundAppQuota | View the application quota associated with a specified client application. | To be tested |
|  | CreateAppCodeAutoV2 | When creating an app code, you do not need to specify the value. The background automatically generates a random character string to fill in the value. | To be tested |
|  | ListAppCodesV2 | Query the app code list. | To be tested |
|  | ShowDetailsOfAppAcl | View the access control details of the app. | To be tested |
| Client Quota | ShowAppQuota | Obtain the client quota details | To be tested |
|  | ListAppQuotaBindableApps | Query the list of client applications to which the client quota can be bound. Fuzzy search by client application name is supported. | To be tested |
|  | ListAppQuotas | Obtain the client quota list. Fuzzy query by name is supported. | To be tested |
|  | UpdateAppQuota | Modifying the Client Quota | To be tested |
|  | ListAppQuotaBoundApps | Query the list of client applications bound to the client quota. Fuzzy match by client application name is supported. | To be tested |
|  | CreateAppQuota | Create Client Quota | To be tested |
|  | DisassociateAppQuotaWithApp | Unbind the client quota from the client application | To be tested |
|  | AssociateAppsForAppQuota | List of client applications bound to the client quota | To be tested |
|  | DeleteAppQuota | Delete a client quota. When deleting the client quota, delete the association between the client quota and the client application. | To be tested |
| Configuration Management | ListProjectCofigsV2 | Query the tenant configuration list of an instance. You can use this API to view the resource configuration and usage of each type of resource. | To be tested |
| Customized Authentication Management | CreateCustomAuthorizerV2 | Create a user-defined authentication | To be tested |
|  | UpdateCustomAuthorizerV2 | Modifying a user-defined authentication | To be tested |
|  | ShowDetailsOfCustomAuthorizersV2 | Viewing the details of the customized authentication | To be tested |
|  | DeleteCustomAuthorizerV2 | Delete user-defined authentication | To be tested |
|  | ListCustomAuthorizersV2 | Query the user-defined authentication list | To be tested |
| Domain name management | UpdateDomainV2 | Modify the configuration information corresponding to the bound domain name. | To be tested |
|  | ShowDetailsOfDomainNameCertificateV2 | View details about the certificate bound to the domain name. | To be tested |
|  | DisassociateDomainV2 | If an API group does not need to be bound to a user-defined domain name, you can unbind the domain name from the API group. | To be tested |
|  | AssociateCertificateV2 | If the HTTPS request protocol is used for defining an API request during API creation, the SSL certificate must be added to the independent domain name. | To be tested |
|  | DisassociateCertificateV2 | If the domain name certificate is no longer needed or has expired, you can delete the certificate. | To be tested |
|  | AssociateDomainV2 | User-defined domain name, which takes effect only after the CNAME is added to the subdomain name of the API group. | To be tested |
| Environment variable management | CreateEnvironmentVariableV2 | After an API is released to different environments, the environment variables, such as the API service deployment address and request version number, may vary according to the environment. | To be tested |
|  | ShowDetailsOfEnvironmentVariableV2 | View details about a specified environment variable. | To be tested |
|  | DeleteEnvironmentVariableV2 | Delete the specified environment variables. | To be tested |
|  | UpdateEnvironmentVariableV2 | Modify environment variables. If an environment variable references the backend service address of an API, modifying the environment variable will release all APIs that use the variable again. | To be tested |
|  | ListEnvironmentVariablesV2 | Query the list of all environment variables in a group. | To be tested |
| Environmental Management | UpdateEnvironmentV2 | Modifies the information about a specified environment. The name and remark attributes can be modified. Other attributes cannot be modified. | To be tested |
|  | CreateEnvironmentV2 | In actual production, an API provider may have multiple environments, such as the development environment, test environment, and production environment. You can release APIs to an environment for callers to invoke. | To be tested |
|  | DeleteEnvironmentV2 | Delete the specified environment. | To be tested |
|  | ListEnvironmentsV2 | Query the environment list that meets the conditions. | To be tested |
| Exclusive - Group Custom Response Management | UpdateGatewayResponseTypeV2 | Modifies the customized response of a specified error type in a group. | To be tested |
|  | ListGatewayResponsesV2 | Query the customized response list of a group | To be tested |
|  | DeleteGatewayResponseV2 | Deleting a customized response from a group | To be tested |
|  | ShowDetailsOfGatewayResponseTypeV2 | View the customized response of a specified error type in a group | To be tested |
|  | DeleteGatewayResponseTypeV2 | Delete the customized response configuration for the specified error type and restore the default response configuration. | To be tested |
|  | CreateGatewayResponseV2 | Adding a customized response in a group | To be tested |
|  | ShowDetailsOfGatewayResponseV2 | Details of querying customized group information | To be tested |
|  | UpdateGatewayResponseV2 | Customized response for modifying a group | To be tested |
| Exclusive - Microservice Center Management | ImportMicroservice | Import a microservice. | To be tested |
| Exclusive-Asynchronous Task Management | ShowAsyncTaskResult | Obtain the asynchronous task result. | To be tested |
|  | ExportApiDefinitionsAsync | Exports API definitions in a group. The exported file must comply with the swagger standard. For details about the customized extended fields of API Gateway | To be tested |
|  | ImportApiDefinitionsAsync | Import an API. The content in the file to be imported must comply with the swagger standard. For details about the customized extended fields of API Gateway | To be tested |
| Exclusive-Credential Management | DeleteAppV2 | Delete a specified app. | To be tested |
|  | CreateAnAppV2 | An app is an identity that can access an API. After the API is authorized to an app, the app can invoke the API. | To be tested |
|  | ResettingAppSecretV2 | Reset the key of a specified app. | To be tested |
|  | UpdateAppV2 | Modifies the information about a specified app. The attributes that can be modified are name and remark. When the user-defined key and secret are enabled, app_key and app_secret can also be modified. Other attributes cannot be modified. | To be tested |
|  | CheckAppV2 | Verifies whether the app exists. Non-app owners can invoke this interface to verify whether the app exists. This interface displays only the basic information about the app, including the ID, name, and  | To be tested |
| Exclusive-Domain Name Management | UpdateSlDomainSettingV2 | Disable or enable the debug domain name bound to the API group. | To be tested |
| Exclusive-Monitoring Information Query | ListLatelyGroupStatisticsV2 | Query the number of times that all APIs in the API group are invoked by the API group ID. The measurement period is 1 minute. The query scope is within one hour. One sample is generated every minute. The sample value is accumulated within one minute. | To be tested |
|  | ListMetricData | Query the monitoring data of a specified indicator in a specified period of time and granularity. You can specify the data dimension to be queried by specifying the parameter. | To be tested |
| Exclusive-Summary Query | ListApiGroupsQuantitiesV2 | Query the API group overview of a tenant. | To be tested |
|  | ListApiQuantitiesV2 | Query the API overview of the tenant, including the number of APIs published to the RELEASE environment and the number of APIs not published to the RELEASE environment. | To be tested |
|  | ListAppQuantitiesV2 | Query the app overview of the tenant, including the number of apps for which API access has been granted and the number of apps for which API access has not been granted. | To be tested |
| Instance Feature Management | ListFeaturesV2 | View the DB instance feature list. Note: If the DB instance does not support the following features, contact technical support to upgrade the DB instance version. | To be tested |
|  | CreateFeatureV2 | Configure the required features for the instance. | To be tested |
| Instance Management | ShowRestrictionOfInstanceV2 | View the instance constraint information | To be tested |
|  | ShowDetailsOfInstanceV2 | Viewing DB Instance Details | To be tested |
| Monitoring information query | ListLatelyApiStatisticsV2 | Query the number of times that an API is invoked based on the API ID and the latest period. The statistical period is 1 minute. The query scope is within one hour. One sample is per minute. The sample value is accumulated within one minute. | To be tested |
| OpenAPI | ExportApiDefinitionsV2 | Export the definition information of APIs in a group. The exported file content complies with the Swagger standard. | To be tested |
|  | ImportApiDefinitionsV2 | Import an API. The imported file must comply with the swagger standard.  | To be tested |
| Plug-in management | CreatePlugin | Create plug-in information. | To be tested |
|  | DetachApiFromPlugin | Unbind the API from the plug-in | To be tested |
|  | ListPlugins | Query details about a group of API Gateway plug-ins that meet the search criteria. | To be tested |
|  | ShowPlugin | Query plug-in details. | To be tested |
|  | DetachPluginFromApi | Unbind the plug-in from the API | To be tested |
|  | UpdatePlugin | Modifies plug-in information. | To be tested |
|  | ListApiAttachedPlugins | Query information about the plug-ins bound to a specified API | To be tested |
|  | DeletePlugin | Delete the plug-in. | To be tested |
|  | ListApiAttachablePlugins | Query information about the plug-ins that can be bound to the current API. | To be tested |
|  | ListPluginAttachableApis | Query information about the APIs that can be bound to the current plug-in. | To be tested |
|  | ListPluginAttachedApis | Query information about the APIs bound to a specified plug-in | To be tested |
|  | AttachPluginToApi | Bind the plug-in to the API. | To be tested |
|  | AttachApiToPlugin | Bind the plug-in to the API. | To be tested |
| Premium-Configuration Management | ListInstanceConfigsV2 | Query the tenant instance configuration list | To be tested |
| Premium-Customized Inbound Port Management | ListCustomIngressPorts | Query the user-defined inbound port list of an instance. | To be tested |
|  | AddCustomIngressPort | User-defined inbound port of the new instance. In an instance, a port supports only one protocol. | To be tested |
|  | DeleteCustomIngressPort | Delete the user-defined inbound ports, excluding the default ports 80 and 443. | To be tested |
|  | ListCustomIngressPortDomains | Query the domain name bound to the user-defined inbound port specified by an instance. | To be tested |
| Premium-Instance Feature Management | ListInstanceFeatures | Query the feature list supported by an instance. | To be tested |
| Premium-Instance Management | CreatePrepayResize | Create a yearly/monthly specification change order. | To be tested |
|  | UpdateIngressEipV2 | Update the public network bandwidth of an instance. This parameter is supported only when the instance type is ELB. | To be tested |
|  | AddEngressEipV2 | Enable the public network egress for the instance. | To be tested |
|  | DeleteInstancesV2 | Delete a premium instance | To be tested |
|  | CreateInstanceV2 | Create a pay-per-use premium instance | To be tested |
|  | ListInstancesV2 | Query the list of premium instances | To be tested |
|  | CreatePostPayResizeOrder | Create a pay-per-use specification change order. | To be tested |
|  | ShowDetailsOfInstanceProgressV2 | View the creation progress of the premium instance | To be tested |
|  | ListAvailableZonesV2 | View AZ information | To be tested |
|  | CreateOrder | Create a yearly/monthly premium instance. | To be tested |
|  | RemoveIngressEipV2 | Disable the public network entry of an instance. This function is supported only when the instance type is ELB. | To be tested |
|  | AddEipV2 | Update or bind an EIP to an instance (supported only when the instance type is LVS) | To be tested |
|  | RemoveEipV2 | Unbinding an EIP from an instance | To be tested |
|  | RemoveEngressEipV2 | Disable the public network egress of an instance. | To be tested |
|  | UpdateInstanceV2 | Update a premium instance | To be tested |
|  | AddIngressEipV2 | Enable the public network entry for an instance. This function is supported only when the instance type is ELB. | To be tested |
|  | UpdateEngressEipV2 | Update the outbound bandwidth of an instance | To be tested |
| Premium-Instance Tag Management | BatchCreateOrDeleteInstanceTags | Add or delete tags for a single instance in batches. | To be tested |
|  | ListProjectInstanceTags | Query all instance tags in a project. | To be tested |
|  | ShowInstancesNumByTags | Query the number of instances with a specified tag. | To be tested |
| Premium-Instance VPC Endpoint Management | AcceptOrRejectEndpointConnections | Accepts or rejects the instance node connection. | To be tested |
|  | AddEndpointPermissions | Add the instance VPC endpoint connection trustlist in batches. | To be tested |
|  | ListEndpointConnections | Query the instance VPC connection list. | To be tested |
|  | ListEndpointPermissions | Query the trustlist of the VPC endpoint service of the current instance. | To be tested |
|  | DeleteEndpointPermissions | This API is used to delete the trustlist of VPC endpoint connections in batches. | To be tested |
| Premium-Orchestration Rule Management | ShowDetailsOfOrchestration | Query orchestration rule details | To be tested |
|  | DeleteOrchestration | Delete an orchestration rule | To be tested |
|  | ListOrchestrationAttachedApis | Query information about the APIs bound to a specified plug-in | To be tested |
|  | UpdateOrchestration | Updates an orchestration rule | To be tested |
|  | ListOrchestrations | View the orchestration rule list | To be tested |
|  | CreateOrchestration | Create an orchestration rule | To be tested |
| SSL Certificate Management | BatchDisassociateDomainsV2 | Unbind an SSL certificate from a domain name | To be tested |
|  | ShowDetailsOfCertificateV2 | Viewing Certificate Details | To be tested |
|  | DeleteCertificateV2 | This API is used to delete an SSL certificate. Only the certificate that is not associated with a domain name can be deleted. | To be tested |
|  | BatchDisassociateCertsV2 | This API is used to unbind an SSL certificate from a domain name. Currently, only one certificate can be unbound. The certificate_ids field in the request body contains only one certificate ID. | To be tested |
|  | BatchAssociateCertsV2 | The domain name is bound to the SSL certificate. Currently, only one binding is supported. The certificate_ids field in the request body contains only one certificate ID. | To be tested |
|  | ListCertificatesV2 | Obtain the SSL certificate list. | To be tested |
|  | UpdateCertificateV2 | Modifying the SSL Certificate | To be tested |
|  | CreateCertificateV2 | Create an SSL certificate | To be tested |
|  | ListAttachedDomainsV2 | Obtain the list of domain names bound to the SSL certificate. | To be tested |
|  | BatchAssociateDomainsV2 | Domain name bound to the SSL certificate | To be tested |
| Set Special Flow Control | ListSpecialThrottlingConfigurationsV2 | View the special configuration of the throttling policy. | To be tested |
|  | DeleteSpecialThrottlingConfigurationV2 | To delete a special configuration of a throttling policy, run the following command: | To be tested |
|  | CreateSpecialThrottlingConfigurationV2 | A throttling policy can limit the maximum number of times that an API can be accessed within a period of time, or the maximum number of times that a tenant or app can access an API within a period of time. | To be tested |
|  | UpdateSpecialThrottlingConfigurationV2 | Modify a special setting in a throttling policy. | To be tested |
| Shared edition-API group management | DeleteApiGroup | Delete a specified API group. | To be tested |
|  | ListApiGroups | Query the API group list. | To be tested |
|  | CreateApiGroup | API groups are management units of APIs. An API group is equivalent to a service entry. When an API group is created, a subdomain name is returned as the access entry. It is recommended that APIs in an API group be related to each other. | To be tested |
|  | UpdateAPIGroup | Modifies API group attributes. The name and remark attributes can be modified. Other attributes cannot be modified. | To be tested |
|  | ShowDetailsOfApiGroup | Query the details about a specified group. | To be tested |
| Shared edition-API management | UpdateApi | Modifies information about a specified API, including backend service information. | To be tested |
|  | ShowDetailsOfApi | View the details about a specified API. | To be tested |
|  | DeleteApi | Delete a specified API. When an API is deleted, all resource information or binding relationships related to the API will be deleted, such as the API release records, bound backend services, and app authorization information. | To be tested |
|  | ListApis | View the API list. The API details and release information is returned, but the backend service information is not displayed. | To be tested |
|  | CreateApi | Add an API. An API is a service interface and specific service capabilities. The API is divided into two parts. The first part is an API for API users, which defines how users invoke the API. The second part is oriented to the API provider. The API provider defines the actual backend status of the API and how API Gateway accesses the actual backend services. Currently, the real backend service of an API supports three types: traditional HTTP/HTTPS web backend, function workflow, and MOCK. | To be tested |
| Shared edition-App authorization management | CreateAuthorizingApps | After an app is created, the app cannot access the API. To access the API in an environment, you need to grant the API in the environment to the app. After the authorization is successful, the app can access the API in the environment. | To be tested |
|  | CancelingAuthorization | This API is used to cancel the authorization relationship between an API and an app. After the authorization is canceled, the app cannot invoke the API any longer. | To be tested |
|  | ListApisThatNotBoundWithAnApp | Query the list of APIs that are not bound to an app in a specified environment, including self-owned APIs and APIs purchased from the Marketplace. | To be tested |
|  | ListAPIsThatBoundWithAnApp | Query the list of APIs bound to an app. | To be tested |
|  | ListAppsBoundToAnApi | Query the list of apps bound to an API. | To be tested |
| Shared edition-App management | UpdateAnApp | Modifies the information about a specified app. The attributes that can be modified are name and remark. When the user-defined key and secret are enabled, app_key and app_secret can also be modified. Other attributes cannot be modified. | To be tested |
|  | CheckAnApp | Verifies whether the app exists. Non-app owners can invoke this interface to verify whether the app exists. This interface displays only the basic information about the app, including the ID, name, and remarks. | To be tested |
|  | ShowAppDetails | View detailed information about a specified app. | To be tested |
|  | CreateAnApp | An application is an identity that can access an API. After the API is authorized to an app, the app can invoke the API. | To be tested |
|  | DeleteAnApp | Delete a specified app. | To be tested |
|  | ResettingTheAppSecret | Reset the key of a specified app. | To be tested |
| Shared edition-Set special flow control | UpdateSpecialThrottlingConfiguration | Modify a special setting in a throttling policy. | To be tested |
|  | ListSpecialThrottlingConfigurations | View the special configuration of the throttling policy. | To be tested |
|  | CreateSpecialThrottlingConfiguration | A throttling policy can limit the maximum number of times that an API can be accessed within a period of time, or the maximum number of times that a tenant or app can access an API within a period of time. If you want to perform special settings for a specific app, for example, set the number of access times per minute for all apps to 500, and set the number of access times per minute for APP1 to 800, you can set the special app in the flow control policy. Add a special object for the throttling policy. The object can be an app or a tenant. | To be tested |
|  | DeleteSpecialThrottlingConfiguration | To delete a special configuration of a throttling policy | To be tested |
| Shared edition-flow control policy management | DeleteRequestThrottlingPolicy | Deletes a specified throttling policy and all binding relationships between the throttling policy and the API. | To be tested |
|  | ListTheRequestThrottlingPolicy | To query the information about all throttling policies | To be tested |
|  | ShowDetailsOfARequestThrottlingPolicy | View the details about a specified throttling policy. | To be tested |
|  | UpdateRequestThrottlingPolicy | Modifies the details about a specified throttling policy. | To be tested |
|  | CreateRequestThrottlingPolicy | After an API is brought online, the system provides a flow control policy for each API by default. API providers can change the flow control policy based on the API service capability and load status. The throttling policy specifies the maximum number of times that an API can be accessed within a specified period. | To be tested |
| Shared-API Binding Flow Control Policy | ListRequestThrottlingPoliciesThatBoundToAnApi | Query the throttling policy list bound to an API. There should be only one flow control policy in each environment. | To be tested |
|  | ListApisThatNotBoundWithRequestThrottlingPolicy | Query the list of self-owned APIs that are not bound to the throttling policy. The API must have been published. Unpublished APIs will not be displayed. | To be tested |
|  | DisassociateRequestThrottlingPolicy | Unbind the API from the throttling policy. | To be tested |
|  | ListApisThatBoundWithRequestThrottlingPolicy | Query the list of APIs bound to a throttling policy. | To be tested |
|  | AssociateRequestThrottlingPolicy | Apply a throttling policy to an API. All accesses to the API will be restricted by the throttling policy. If the number of access times in a specified period exceeds the maximum number of access times specified in the throttling policy, subsequent access requests will be rejected. This protects backend APIs from abnormal traffic and ensures stable service running. Bind a flow control policy to a specified shared-API. When binding a flow control policy, you need to specify the environment in which the flow control policy takes effect. The same API can be bound with different throttling policies in different environments. After an API is published to a specific environment, only one default throttling policy can be bound to the API. | To be tested |
| Shared-Domain name management | AssociateDomain | User-defined domain name, which takes effect only after the CNAME is added to the subdomain name of the API group.  | To be tested |
|  | ShowDetailsOfDomainNameCertificate | View details about the certificate bound to the domain name. | To be tested |
|  | AssociateCertificate | If the HTTPS request protocol is used for defining an API request during API creation, the SSL certificate must be added to the domain name. | To be tested |
|  | DisassociateCertificate | If the domain name certificate is no longer needed or has expired, you can delete the certificate. | To be tested |
|  | DisassociateDomain | If an API group does not need to be bound to a user-defined domain name, you can unbind the domain name from the API group. | To be tested |
| Shared-Environment variable management | ListEnvironmentVariables | Query the list of all environment variables in a group. | To be tested |
|  | DeleteEnvironmentVariable | Delete the specified environment variables. | To be tested |
|  | CreateEnvironmentVariable | After an API is released to different environments, the environment variables, such as the API service deployment address and request version number, may vary according to the environment. | To be tested |
|  | ShowEnvironmentVariableDetails | View details about a specified environment variable. | To be tested |
| Shared-Signature Key Management | CreateSignatureKey | To ensure API security, it is recommended that tenants provide a protection mechanism for API access. That is, open APIs of tenants need to authenticate the request source. Requests that do not meet the authentication requirements are directly rejected. The signature key is one of the API security protection mechanisms. If a tenant creates a signature key and binds the signature key to an API, API Gateway uses the bound signature key to encrypt request parameters and generate a signature. When a tenant's backend service receives a request, it can verify the signature. If the signature verification fails, the request is not sent by API Gateway and the tenant can reject the request, ensuring API security and preventing API attacks from unknown sources. | To be tested |
|  | UpdateSignatureKey | Modifies the details about a specified signature key. | To be tested |
|  | DeleteSignatureKey | Delete a specified signature key. When the signature key is deleted, the binding relationship configured for the signature key is also deleted, and the corresponding signature key becomes invalid. | To be tested |
|  | ListSignatureKeys | Query information about all signature keys. | To be tested |
| Shared-Signing Key Binding Relationship Management | ListSignatureKeysBoundtoAnAPI | Query the list of signature keys bound to an API. Each API should be bound to a maximum of one signing key per environment. | To be tested |
|  | DisassociateSignatureKey | Unbind the API from the signature key. | To be tested |
|  | ListApisBoundWithSignatureKey | Query the list of APIs bound to a signature key. | To be tested |
|  | AssociateSignatureKey | A signature key takes effect only after it is bound to an API. After the signature key is bound to an API, API Gateway uses the signature key to encrypt and sign requests to backend services. Backend services can verify the signature to verify the request source. Binds the specified signing key to one or more published APIs. When an API is published in different environments, different signature keys can be bound to the API. An API can be bound to only one signature key after being published to a specific environment. | To be tested |
|  | ListApisNotBoundWithSignatureKey | Query the list of APIs that are not bound to the signature key. The API must have been published. Unpublished APIs will not be displayed. | To be tested |
| Shared-Summary Query | ListAppQuantities | Query the app overview of the tenant, including the number of apps for which API access has been granted and the number of apps for which API access has not been granted. | To be tested |
|  | ListAPIsOfAPIGroup | Query the API group overview of a tenant, including the number of API groups that are released and the number of API groups that are not released. | To be tested |
|  | ListApiQuantities | Query the API overview of the tenant, including the number of APIs published to the RELEASE environment and the number of APIs not published to the RELEASE environment. | To be tested |
| Signature Key Management | UpdateSignatureKeyV2 | Modifies the details about a specified signature key. | To be tested |
|  | CreateSignatureKeyV2 | To protect API security, it is recommended that tenants provide a protection mechanism for API access. That is, open APIs of tenants need to authenticate the request source. Requests that do not meet the authentication requirements are directly rejected. | To be tested |
|  | DeleteSignatureKeyV2 | Deletes a specified signature key. A signature key cannot be deleted if it is bound to an API. You need to unbind it from the API before deleting it. | To be tested |
|  | ListSignatureKeysV2 | Query information about all signature keys. | To be tested |
| Signing Key Binding Relationship Management | AssociateSignatureKeyV2 | A signature key takes effect only after it is bound to an API. | To be tested |
|  | ListSignatureKeysBindedToApiV2 | Query the list of signature keys bound to an API. Each API should be bound with a maximum of one signing key per environment. | To be tested |
|  | DisassociateSignatureKeyV2 | Unbind the API from the signature key. | To be tested |
|  | ListApisBindedToSignatureKeyV2 | Query the list of APIs bound to a signature key. | To be tested |
|  | ListApisNotBoundWithSignatureKeyV2 | Query the list of APIs that are not bound to the signature key. The API must have been published. Unpublished APIs will not be displayed. | To be tested |
| Tag Management | ListInstanceTags | Query the instance tag. | To be tested |
|  | ListTagsV2 | Query the tag list | To be tested |
|  | ListInstancesByTags | Query a specified database instance by tag. | To be tested |
| Throttling Policy Management | ListRequestThrottlingPolicyV2 | To query the information about all throttling policies | To be tested |
|  | UpdateRequestThrottlingPolicyV2 | Modifies the details about a specified throttling policy. | To be tested |
|  | ShowDetailsOfRequestThrottlingPolicyV2 | View the details about a specified throttling policy. | To be tested |
|  | CreateRequestThrottlingPolicyV2 | After an API is brought online, the system provides a default throttling policy for each API. API providers can change the throttling policy based on the API service capability and load status. | To be tested |
|  | DeleteRequestThrottlingPolicyV2 | Deletes a specified throttling policy. If the throttling policy is bound to an API, you need to unbind the throttling policy from the API and then delete the throttling policy. | To be tested |
| VPC Channel Management | DeleteVpcChannelV2 | Delete a specified VPC channel | To be tested |
|  | UpdateHealthCheck | Modifies the VPC channel health check. | To be tested |
|  | CreateMemberGroup | Create a VPC channel backend server group on the Service Integration page. You can determine whether to associate VPC channel backend instances with the backend instance server group to manage backend server nodes. | To be tested |
|  | BatchDisableMembers | Failed to modify the status of backend servers in batches. | To be tested |
|  | ShowDetailsOfMemberGroup | View details about a specified VPC channel backend server group. | To be tested |
|  | UpdateVpcChannelV2 | Updates the parameters of a specified VPC channel. | To be tested |
|  | ListMemberGroups | Query the list of backend cloud service groups in a VPC channel | To be tested |
|  | BatchEnableMembers | Changing the status of backend servers in batches is available. | To be tested |
|  | CreateVpcChannelV2 | In the service integration, create channels for connecting to private VPC resources. When creating an API, configure backend nodes to use these VPC channels so that the service integration can directly access private VPC resources. | To be tested |
|  | UpdateBackendInstancesV2 | This API is used to update the backend instance of a specified VPC channel. During the update, the input request parameters are used to fully overwrite the backend instances of the corresponding cloud service group. If the ECS group to be modified is not specified, the system overwrites the entire ECS group. | To be tested |
|  | UpdateMemberGroup | Updates a specified VPC channel backend server group | To be tested |
|  | ShowDetailsOfVpcChannelV2 | View details about a specified VPC channel. | To be tested |
|  | AddingBackendInstancesV2 | Adding a backend instance to a specified VPC channel | To be tested |
|  | DeleteMemberGroup | Delete a specified VPC channel backend server group. | To be tested |
|  | ListVpcChannelsV2 | View the VPC channel list | To be tested |
|  | DeleteBackendInstanceV2 | Delete a backend instance from a specified VPC channel. | To be tested |
|  | ListBackendInstancesV2 | View the list of backend instances in a specified VPC channel. | To be tested |
| environment-controller-v2 | DeleteEnvironment | Delete the environment of the application. | To be tested |
|  | UpdateEnvironment | Editing environment in the application. | To be tested |
|  | CreateEnvironment | Create an environment under the application. | To be tested |
|  | ListEnvironments | Query the environment list of an application. | To be tested |

