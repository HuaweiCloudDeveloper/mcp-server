# SWR MCP Server 


## Version
v0.1.0

## Overview

SWR MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SWR. Full-chain management of SWR resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Image Aging Rule Management | DeleteRetention | Deleting an image aging rule | To be tested |
|  | ListRetentions | Obtain the image aging rule list | To be tested |
|  | ListRetentionHistories | Obtains the aging records of the image. | To be tested |
|  | CreateRetention | Create an image aging rule | To be tested |
|  | ShowRetention | Obtains the image aging rule records. | To be tested |
| Image Repository Management | ListReposDetails | Query the image repository list | To be tested |
|  | ListSharedReposDetails | Query the list of shared images | To be tested |
|  | CreateRepo | Create an image repository under the organization. | To be tested |
|  | DeleteRepo | Delete an image repository from an organization. | To be tested |
|  | UpdateRepo | Updates the image summary information in the tenant organization, including the image type, whether the image is public, and description. | To be tested |
|  | ShowRepository | Query the general information about the image repository | To be tested |
| Image permission management | UpdateUserRepositoryAuth | Update image permissions | To be tested |
|  | ShowUserRepositoryAuth | Query image permissions | To be tested |
|  | CreateUserRepositoryAuth | Permission to create an image | To be tested |
|  | DeleteUserRepositoryAuth | Deleting the Image Permission | To be tested |
| Image version management | CreateRepoTag | Create an image tag | To be tested |
|  | DeleteRepoTag | Delete an image with a specified tag from the image repository. | To be tested |
|  | ListRepositoryTags | Query the image tag list | To be tested |
| Mirror synchronization management | ListImageAutoSyncReposDetails | Obtain all automatic synchronization tasks created for the current image repository. | To be tested |
|  | CreateImageSyncRepo | Create an automatic image synchronization task to help you synchronize the latest images to image repositories in other regions. Automatic image synchronization helps you synchronize the latest image to the image repository in other regions. When the image is updated, the image in the target repository will be automatically updated, but the existing image will not be automatically synchronized. You need to manually synchronize existing images. For details, see Manually Synchronizing Images. | To be tested |
|  | DeleteImageSyncRepo | This command is used to delete a specified automatic image synchronization task based on the target region and organization. | To be tested |
|  | CreateManualImageSyncRepo | If you want to use an existing image in the image repository in another region, you need to manually trigger image synchronization. To check whether the synchronization is successful, if the response status code is 200 and no error information is reported, the synchronization is successful. Use the SWR management console or call the API for querying image repository overview information. If the image version to be synchronized exists in the target organization in the target region, the synchronization is successful. | To be tested |
|  | ShowSyncJob | After creating an automatic image synchronization task, you can use this API to query the task status to determine whether the synchronization is successful. | To be tested |
| Organization Management | DeleteNamespaces | Delete an organization | To be tested |
|  | CreateNamespace | Create an organization | To be tested |
|  | ListNamespaces | Query the organization list | To be tested |
|  | ShowNamespace | Obtain organization details | To be tested |
| Organization Permission Management | ShowNamespaceAuth | Query organization permissions | To be tested |
|  | CreateNamespaceAuth | Create Organization Permission | To be tested |
|  | UpdateNamespaceAuth | Update organization permission | To be tested |
|  | DeleteNamespaceAuth | Deleting Organization Permission | To be tested |
| Other | ShowShareFeatureGates | Query service feature switch information | To be tested |
|  | ShowDomainOverview | Obtain the tenant overview information | To be tested |
|  | ShowDomainResourceReports | Obtain tenant resource statistics | To be tested |
| Query version operation | ShowApiVersion | Query the details about a specified TMS API version. | To be tested |
|  | ListApiVersions | Query the TMS API version list. | To be tested |
| Quota Management | ListQuotas | Obtain quota information | To be tested |
| Shared Account Management | UpdateRepoDomains | Updating a shared account | To be tested |
|  | ListRepoDomains | Obtain the list of shared accounts. | To be tested |
|  | DeleteRepoDomains | Delete a shared account | To be tested |
|  | ShowAccessDomain | Check whether the shared tenant exists. | To be tested |
|  | CreateRepoDomains | Create a shared account. After an image is uploaded, you can share the image with other accounts and grant the permission to download the image. | To be tested |
| Temporary login command | CreateAuthorizationToken | Invoke this API to obtain the value of X-Swr-Dockerlogin in the response message header and the value of host in the response message body to generate an enhanced login command. Note: This API can be invoked only on the new IAM plane. | To be tested |
|  | CreateSecret | Invoke this interface to obtain the value of X-Swr-Dockerlogin in the response message header and the value of host in the response message body to generate a temporary login command. | To be tested |
| Trigger Management | ListTriggersDetails | Obtain the trigger list in the image repository. | To be tested |
|  | CreateTrigger | Create a trigger | To be tested |
|  | UpdateTrigger | Update trigger configuration | To be tested |
|  | ShowTrigger | Obtain trigger details | To be tested |
|  | DeleteTrigger | Delete a trigger | To be tested |
| Video Stream Management | UpdateRetention | This interface is used to update video dump information. By default, the created video stream does not contain dump information. That is, the video data is not saved. After the dumping information is updated, video streams can be saved to a specified storage medium, such as OBS. You can obtain dumped videos from OBS later. | To be tested |

