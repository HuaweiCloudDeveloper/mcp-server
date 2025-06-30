# SWR MCP Server 


## Version
v0.1.0

## Overview

SWR MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SWR. Full-chain management of SWR resources can be carried out based on natural language.

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
                    <td rowspan="5">Image Aging Rule Management</td>
                    <td>DeleteRetention</td>
                    <td>Deleting an image aging rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRetentions</td>
                    <td>Obtain the image aging rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRetentionHistories</td>
                    <td>Obtains the aging records of the image.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRetention</td>
                    <td>Create an image aging rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRetention</td>
                    <td>Obtains the image aging rule records.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Image Repository Management</td>
                    <td>ListReposDetails</td>
                    <td>Query the image repository list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSharedReposDetails</td>
                    <td>Query the list of shared images</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRepo</td>
                    <td>Create an image repository under the organization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRepo</td>
                    <td>Delete an image repository from an organization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRepo</td>
                    <td>Updates the image summary information in the tenant organization, including the image type, whether the image is public, and description.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRepository</td>
                    <td>Query the general information about the image repository</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Image permission management</td>
                    <td>UpdateUserRepositoryAuth</td>
                    <td>Update image permissions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserRepositoryAuth</td>
                    <td>Query image permissions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUserRepositoryAuth</td>
                    <td>Permission to create an image</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUserRepositoryAuth</td>
                    <td>Deleting the Image Permission</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Image version management</td>
                    <td>CreateRepoTag</td>
                    <td>Create an image tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRepoTag</td>
                    <td>Delete an image with a specified tag from the image repository.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRepositoryTags</td>
                    <td>Query the image tag list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Mirror synchronization management</td>
                    <td>ListImageAutoSyncReposDetails</td>
                    <td>Obtain all automatic synchronization tasks created for the current image repository.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateImageSyncRepo</td>
                    <td>Create an automatic image synchronization task to help you synchronize the latest images to image repositories in other regions. Automatic image synchronization helps you synchronize the latest image to the image repository in other regions. When the image is updated, the image in the target repository will be automatically updated, but the existing image will not be automatically synchronized. You need to manually synchronize existing images. For details, see Manually Synchronizing Images.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteImageSyncRepo</td>
                    <td>This command is used to delete a specified automatic image synchronization task based on the target region and organization.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateManualImageSyncRepo</td>
                    <td>If you want to use an existing image in the image repository in another region, you need to manually trigger image synchronization. To check whether the synchronization is successful, if the response status code is 200 and no error information is reported, the synchronization is successful. Use the SWR management console or call the API for querying image repository overview information. If the image version to be synchronized exists in the target organization in the target region, the synchronization is successful.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSyncJob</td>
                    <td>After creating an automatic image synchronization task, you can use this API to query the task status to determine whether the synchronization is successful.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Organization Management</td>
                    <td>DeleteNamespaces</td>
                    <td>Delete an organization</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNamespace</td>
                    <td>Create an organization</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNamespaces</td>
                    <td>Query the organization list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNamespace</td>
                    <td>Obtain organization details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Organization Permission Management</td>
                    <td>ShowNamespaceAuth</td>
                    <td>Query organization permissions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNamespaceAuth</td>
                    <td>Create Organization Permission</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNamespaceAuth</td>
                    <td>Update organization permission</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNamespaceAuth</td>
                    <td>Deleting Organization Permission</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Other</td>
                    <td>ShowShareFeatureGates</td>
                    <td>Query service feature switch information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainOverview</td>
                    <td>Obtain the tenant overview information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainResourceReports</td>
                    <td>Obtain tenant resource statistics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Query version operation</td>
                    <td>ShowApiVersion</td>
                    <td>Query the details about a specified TMS API version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersions</td>
                    <td>Query the TMS API version list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota Management</td>
                    <td>ListQuotas</td>
                    <td>Obtain quota information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Shared Account Management</td>
                    <td>UpdateRepoDomains</td>
                    <td>Updating a shared account</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRepoDomains</td>
                    <td>Obtain the list of shared accounts.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRepoDomains</td>
                    <td>Delete a shared account</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAccessDomain</td>
                    <td>Check whether the shared tenant exists.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRepoDomains</td>
                    <td>Create a shared account. After an image is uploaded, you can share the image with other accounts and grant the permission to download the image.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Temporary login command</td>
                    <td>CreateAuthorizationToken</td>
                    <td>Invoke this API to obtain the value of X-Swr-Dockerlogin in the response message header and the value of host in the response message body to generate an enhanced login command. Note: This API can be invoked only on the new IAM plane.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecret</td>
                    <td>Invoke this interface to obtain the value of X-Swr-Dockerlogin in the response message header and the value of host in the response message body to generate a temporary login command.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Trigger Management</td>
                    <td>ListTriggersDetails</td>
                    <td>Obtain the trigger list in the image repository.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrigger</td>
                    <td>Create a trigger</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTrigger</td>
                    <td>Update trigger configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrigger</td>
                    <td>Obtain trigger details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrigger</td>
                    <td>Delete a trigger</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Video Stream Management</td>
                    <td>UpdateRetention</td>
                    <td>This interface is used to update video dump information. By default, the created video stream does not contain dump information. That is, the video data is not saved. After the dumping information is updated, video streams can be saved to a specified storage medium, such as OBS. You can obtain dumped videos from OBS later.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
