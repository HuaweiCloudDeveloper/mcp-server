# CPH MCP Server 


## Version
v0.1.0

## Overview

CPH MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CPH. Full-chain management of CPH resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| ADB Command | RunShellCommand | Run the shell command on the cloud phone. This interface is an asynchronous interface. | To be tested |
|  | PushFile | Push files to the file system of the cloud phone. The system downloads and decompresses the specified file and pushes the decompressed file to the root directory of the cloud phone. You can only push files in the specified .tar format. You need to upload the .tar files to your OBS bucket in advance. This interface is an asynchronous interface. Before calling this API, ensure that the CPH service has been authorized to perform operations on OBS buckets. | To be tested |
|  | InstallApk | Install the APK on the cloud phone. The system downloads the specified APK file and installs it to the cloud phone. | To be tested |
|  | UninstallApk | Uninstall the APK from the cloud phone. This interface is an asynchronous interface. | To be tested |
|  | RunSyncCommand | Synchronize the command in the cloud phone and return the command output. This API supports only the adb shell command. Each user can invoke the API for a maximum of six times within one minute. The allowed command execution timeout period for each cloud mobile phone is 2 seconds. The interface timeout period does not exceed 30 seconds. The more the cloud mobile phone is, the longer the interface time is. | To be tested |
| Bandwidth | UpdateBandwidth | Update the bandwidth. | To be tested |
| Bandwidth management | ShowBandwidthDetail | Query the bandwidth used by the cloud phone. This API applies only to servers that use the system-defined network. | To be tested |
| Cloud Phone Server Management | DeleteShareFiles | Delete files in the shared storage directory. This function is available only on cloud phones that support shared storage. | To be tested |
|  | PushShareApps | Push the app .tar file to the shared app storage directory. This function is available only on the cloud mobile phone server that supports the shared app. Before calling this API, ensure that the CPH service has been authorized to perform operations on OBS buckets.  | To be tested |
|  | ChangeCloudPhoneServer | Switch the cloud phone server. You can use a new cloud phone server. After the switchover, the server name, server ID, and AZ where the server is located are the same as those of the original server, and the server charging remains unchanged. When the server is switched, the mobile phone on the server is re-created and user data is not retained. The switchover requires additional resources and resource quotas. | To be tested |
|  | RestartCloudPhoneServer | Restarting cloud phone servers in batches. | To be tested |
|  | ShowCloudPhoneServerDetail | Query details about the cloud mobile phone server based on server_id. | To be tested |
|  | ListCloudPhoneServers | Query cloud phone servers in pagination mode. The cloud phone server list is sorted in descending order by creation time. You can specify the offset and limit for pagination query. If no cloud phone server exists, an empty list is returned. | To be tested |
|  | ChangeCloudPhoneServerModel | Change the specifications of the cloud phone server. About 2 minutes after the API is successfully called, the specification change is complete. The order status is displayed as successful in the Order Center. In addition, the server specification name is changed to the new one. | To be tested |
|  | UpdateServerName | Modify the server name based on the serverId. | To be tested |
|  | ListShareFiles | Query the file list in the specified path of the shared storage. This function is available only on cloud phones that support shared storage. | To be tested |
|  | DeleteShareApps | Delete a shared app from the shared app storage directory. This function is available only on cloud phones that support shared apps. | To be tested |
|  | CreateNet2CloudPhoneServer | After purchasing a cloud phone server, you can use the existing VPC to manage the cloud phone server and the cloud phone server can reuse the resources you have purchased, such as the shared bandwidth. | To be tested |
|  | PushShareFiles | Push files to the shared storage directory. This function is available only on cloud phones that support shared storage. Before calling this API, ensure that the CPH service has been authorized to perform operations on OBS buckets.  | To be tested |
|  | CreateCloudPhoneSingleServer | The server created by this API contains only the server and server image, but does not contain the cloud phone instance and image. To create a server that contains a cloud phone instance, use the interface for creating a cloud phone server. | To be tested |
|  | ListCloudPhoneServerModels | Query the specification list of the cloud phone server. | To be tested |
| Customized image management | UpdateImageMember | After receiving the shared image, the user chooses to accept or reject the shared image. Shared images that are not accepted cannot be used. | To be tested |
|  | AddImageMember | Image sharing, which indicates that the image is shared with a specified account. | To be tested |
|  | DeleteImageMember | Delete a shared image | To be tested |
| Edge Mirror | DeleteImage | Delete the edge private image with the specified ID. | To be tested |
| Encoding Service Management | ListEncodeServers | Query the encoding service list. | To be tested |
|  | RestartEncodeServer | Restart encoding services in batches. | To be tested |
| Image sharing | ListImageMembers | This API is used to obtain the list of members who accept the image during image sharing. | To be tested |
| Key management | UpdateKeypair | Modify the key pair for connecting to the cloud phone. | To be tested |
| Mirror | ListImages | Query the image list based on different conditions. | To be tested |
| Mirror Task | ShowJob | This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task. | To be tested |
| Mobile phone instance management | BatchShowPhoneConnectInfos | Obtain the cloud phone connection information. | To be tested |
|  | UpdateCloudPhoneProperty | Some cloud mobile phone attributes are open to update capabilities, and some attributes cannot be updated. Some attributes take effect only after the mobile phone is restarted. For details about attribute restrictions, see the cloud mobile phone attribute list. If the mobile phone is abnormal, the update takes effect only after the mobile phone status is restored to Running. This interface is an asynchronous interface. | To be tested |
|  | ExpandPhoneDataVolumeSize | Expanding the Data Disk Size of the Cloud Phone | To be tested |
|  | ShowCloudPhoneDetail | Query the details about the cloud phone. | To be tested |
|  | ListCloudPhones | Query cloud phones by page. The cloud phone list is sorted in descending order by creation time. You can specify the offset and limit for pagination query. If there is no cloud phone, an empty list is returned. | To be tested |
|  | UpdatePhoneName | Modify the phone name based on the phoneId. | To be tested |
|  | RestartCloudPhone | Restarting cloud phones in batches can also be used to enable cloud phones. This interface is an asynchronous interface. | To be tested |
|  | BatchExportCloudPhoneData | This API is used to export data from cloud phones in batches. This interface is an asynchronous interface. Before calling this API, ensure that the CPH service has been authorized to perform operations on OBS buckets. | To be tested |
|  | ResetCloudPhone | Resetting cloud phones in batches to restore the cloud phones to their factory settings. This interface is an asynchronous interface. | To be tested |
|  | ImportTraffic | Modify the mobile phone traffic route. | To be tested |
|  | StopCloudPhone | Disable cloud phones in batches. | To be tested |
|  | ListCloudPhoneModels | Query or collect statistics on the specifications of cloud mobile phones. | To be tested |
|  | ListCloudPhoneImages | Query available mobile phone images based on the project ID. | To be tested |
|  | BatchImportCloudPhoneData | Restore data to the cloud phone in batches. This interface is an asynchronous interface. Before calling this API, ensure that the CPH service has been authorized to perform operations on OBS buckets. For details about how to perform operations on OBS buckets | To be tested |
| TAG Function | ListResourceInstances | Query resource instances of a tenant by tag. | To be tested |
| Tag Management | BatchCreateTags | Create tags in batches | To be tested |
|  | BatchDeleteTags | This API is used to delete tags for a specified protected instance in batches. A maximum of 10 labels can be placed on a resource. | To be tested |
| Tags | ListProjectTags | Query all tags of a specified resource type in a specified project | To be tested |
| Task Center API | ListJobs | Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph. | To be tested |
| Use TMS | ListResourceTags | Query the label information of a specified DB instance. | To be tested |

