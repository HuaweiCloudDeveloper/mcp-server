# CPH MCP Server 


## Version
v0.1.0

## Overview

CPH MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CPH. Full-chain management of CPH resources can be carried out based on natural language.

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
                    <td rowspan="5">ADB Command</td>
                    <td>RunShellCommand</td>
                    <td>Run the shell command on the cloud phone. This interface is an asynchronous interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PushFile</td>
                    <td>Push files to the file system of the cloud phone. The system downloads and decompresses the specified file and pushes the decompressed file to the root directory of the cloud phone. You can only push files in the specified .tar format. You need to upload the .tar files to your OBS bucket in advance. This interface is an asynchronous interface. Before calling this API, ensure that the CPH service has been authorized to perform operations on OBS buckets.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InstallApk</td>
                    <td>Install the APK on the cloud phone. The system downloads the specified APK file and installs it to the cloud phone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UninstallApk</td>
                    <td>Uninstall the APK from the cloud phone. This interface is an asynchronous interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunSyncCommand</td>
                    <td>Synchronize the command in the cloud phone and return the command output. This API supports only the adb shell command. Each user can invoke the API for a maximum of six times within one minute. The allowed command execution timeout period for each cloud mobile phone is 2 seconds. The interface timeout period does not exceed 30 seconds. The more the cloud mobile phone is, the longer the interface time is.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Bandwidth</td>
                    <td>UpdateBandwidth</td>
                    <td>Update the bandwidth.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Bandwidth management</td>
                    <td>ShowBandwidthDetail</td>
                    <td>Query the bandwidth used by the cloud phone. This API applies only to servers that use the system-defined network.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Cloud Phone Server Management</td>
                    <td>DeleteShareFiles</td>
                    <td>Delete files in the shared storage directory. This function is available only on cloud phones that support shared storage.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PushShareApps</td>
                    <td>Push the app .tar file to the shared app storage directory. This function is available only on the cloud mobile phone server that supports the shared app. Before calling this API, ensure that the CPH service has been authorized to perform operations on OBS buckets.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeCloudPhoneServer</td>
                    <td>Switch the cloud phone server. You can use a new cloud phone server. After the switchover, the server name, server ID, and AZ where the server is located are the same as those of the original server, and the server charging remains unchanged. When the server is switched, the mobile phone on the server is re-created and user data is not retained. The switchover requires additional resources and resource quotas.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartCloudPhoneServer</td>
                    <td>Restarting cloud phone servers in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCloudPhoneServerDetail</td>
                    <td>Query details about the cloud mobile phone server based on server_id.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudPhoneServers</td>
                    <td>Query cloud phone servers in pagination mode. The cloud phone server list is sorted in descending order by creation time. You can specify the offset and limit for pagination query. If no cloud phone server exists, an empty list is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeCloudPhoneServerModel</td>
                    <td>Change the specifications of the cloud phone server. About 2 minutes after the API is successfully called, the specification change is complete. The order status is displayed as successful in the Order Center. In addition, the server specification name is changed to the new one.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServerName</td>
                    <td>Modify the server name based on the serverId.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListShareFiles</td>
                    <td>Query the file list in the specified path of the shared storage. This function is available only on cloud phones that support shared storage.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteShareApps</td>
                    <td>Delete a shared app from the shared app storage directory. This function is available only on cloud phones that support shared apps.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNet2CloudPhoneServer</td>
                    <td>After purchasing a cloud phone server, you can use the existing VPC to manage the cloud phone server and the cloud phone server can reuse the resources you have purchased, such as the shared bandwidth.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PushShareFiles</td>
                    <td>Push files to the shared storage directory. This function is available only on cloud phones that support shared storage. Before calling this API, ensure that the CPH service has been authorized to perform operations on OBS buckets.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCloudPhoneSingleServer</td>
                    <td>The server created by this API contains only the server and server image, but does not contain the cloud phone instance and image. To create a server that contains a cloud phone instance, use the interface for creating a cloud phone server.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudPhoneServerModels</td>
                    <td>Query the specification list of the cloud phone server.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Customized image management</td>
                    <td>UpdateImageMember</td>
                    <td>After receiving the shared image, the user chooses to accept or reject the shared image. Shared images that are not accepted cannot be used.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddImageMember</td>
                    <td>Image sharing, which indicates that the image is shared with a specified account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteImageMember</td>
                    <td>Delete a shared image</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Edge Mirror</td>
                    <td>DeleteImage</td>
                    <td>Delete the edge private image with the specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Encoding Service Management</td>
                    <td>ListEncodeServers</td>
                    <td>Query the encoding service list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartEncodeServer</td>
                    <td>Restart encoding services in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Image sharing</td>
                    <td>ListImageMembers</td>
                    <td>This API is used to obtain the list of members who accept the image during image sharing.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Key management</td>
                    <td>UpdateKeypair</td>
                    <td>Modify the key pair for connecting to the cloud phone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Mirror</td>
                    <td>ListImages</td>
                    <td>Query the image list based on different conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Mirror Task</td>
                    <td>ShowJob</td>
                    <td>This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Mobile phone instance management</td>
                    <td>BatchShowPhoneConnectInfos</td>
                    <td>Obtain the cloud phone connection information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCloudPhoneProperty</td>
                    <td>Some cloud mobile phone attributes are open to update capabilities, and some attributes cannot be updated. Some attributes take effect only after the mobile phone is restarted. For details about attribute restrictions, see the cloud mobile phone attribute list. If the mobile phone is abnormal, the update takes effect only after the mobile phone status is restored to Running. This interface is an asynchronous interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandPhoneDataVolumeSize</td>
                    <td>Expanding the Data Disk Size of the Cloud Phone</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCloudPhoneDetail</td>
                    <td>Query the details about the cloud phone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudPhones</td>
                    <td>Query cloud phones by page. The cloud phone list is sorted in descending order by creation time. You can specify the offset and limit for pagination query. If there is no cloud phone, an empty list is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePhoneName</td>
                    <td>Modify the phone name based on the phoneId.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartCloudPhone</td>
                    <td>Restarting cloud phones in batches can also be used to enable cloud phones. This interface is an asynchronous interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchExportCloudPhoneData</td>
                    <td>This API is used to export data from cloud phones in batches. This interface is an asynchronous interface. Before calling this API, ensure that the CPH service has been authorized to perform operations on OBS buckets.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetCloudPhone</td>
                    <td>Resetting cloud phones in batches to restore the cloud phones to their factory settings. This interface is an asynchronous interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportTraffic</td>
                    <td>Modify the mobile phone traffic route.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopCloudPhone</td>
                    <td>Disable cloud phones in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudPhoneModels</td>
                    <td>Query or collect statistics on the specifications of cloud mobile phones.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudPhoneImages</td>
                    <td>Query available mobile phone images based on the project ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchImportCloudPhoneData</td>
                    <td>Restore data to the cloud phone in batches. This interface is an asynchronous interface. Before calling this API, ensure that the CPH service has been authorized to perform operations on OBS buckets. For details about how to perform operations on OBS buckets</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TAG Function</td>
                    <td>ListResourceInstances</td>
                    <td>Query resource instances of a tenant by tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tag Management</td>
                    <td>BatchCreateTags</td>
                    <td>Create tags in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTags</td>
                    <td>This API is used to delete tags for a specified protected instance in batches. A maximum of 10 labels can be placed on a resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>Query all tags of a specified resource type in a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Task Center API</td>
                    <td>ListJobs</td>
                    <td>Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Use TMS</td>
                    <td>ListResourceTags</td>
                    <td>Query the label information of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
