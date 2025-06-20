# BMS MCP Server 


## Version
v0.1.0

## Overview

BMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service BMS. Full-chain management of BMS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
|  bare metal server 2D Tag Management | BatchDeleteBaremetalServerTags | - This API is used to delete tags for specified ECSs in batches. | To be tested |
|  | BatchCreateBaremetalServerTags | -Add tags to specified bare metal server in batches. | To be tested |
|  | ShowBaremetalServerTags | - This API is used to query the tag information of a specified ECS. | To be tested |
|  bare metal server Lifecycle Management | ListBareMetalServers | Filter bare metal server based on the specified request conditions and obtain details about the BMS. This API is used to query the BMS billing mode and whether the BMS is frozen. | To be tested |
|  | ListBareMetalServerDetails | Obtains bare metal server details. This API can be used to query the billing mode of a BMS and whether the BMS is frozen. | To be tested |
|  | ListBareMetalServersDetail | Filter bare metal server based on the specified request conditions and obtain details about the BMS. | To be tested |
|  | CreateBareMetalServers | Create one or more bare metal server. The BMS login authentication modes include key pair and password. For security purposes, the key pair mode is recommended. | To be tested |
|  bare metal server Management | AttachBaremetalServerVolume | After the bare metal server is created, if the disk space is insufficient or the current disk does not meet the requirements, you can attach the existing EVS disk to the BMS as a data disk. | To be tested |
|  | DetachBaremetalServerVolume | Demount the disk attached to the bare metal server. Do not detach disks attached to the system disk slot (that is, the /dev/sda mount point). Disks attached to data disk slots (not /dev/sda) can be detached offline or online (BMS is in the Running state)  | To be tested |
|  | ShowBaremetalServerVolumeInfo | Query the information about the disks attached to the bare metal server  | To be tested |
|  bare metal server Metadata Management | UpdateBaremetalServerMetadata | Updates the bare metal server metadata. If the metadata does not contain the field to be updated, the field is automatically added. If the field to be updated already exists in the metadata, the field value is directly updated. If the field in the metadata is not in the request parameter, it remains unchanged. | To be tested |
|  bare metal server NIC Management | UpdateBaremetalServerInterfaceAttachments |  | To be tested |
|  | ShowBaremetalServerInterfaceAttachments | Query the bare metal server network adapter information, such as the IP address and MAC address of the network adapter. | To be tested |
|  | AddServerNics |  | To be tested |
|  | DeleteServerNics |  | To be tested |
|  bare metal server Password Management | ShowResetPwd | Query whether one-click password reset is supported. | To be tested |
|  | ResetPwdOneClick | Reset the password of the BMS management account (root or Administrator) on the premise that bare metal server supports one-click password reset. You can use the 6.10.1-Querying Whether One-Click Password Reset API to query whether one-click password reset is supported. | To be tested |
|  | ShowWindowsBaremetalServerPwd | Obtain the random password of the administrator account (Administrator account or Cloudbase-Init account) generated during the initial installation of Windows bare metal server. If the BMS is created using a private image, ensure that Cloudbase-Init has been installed. This software is installed on the public image by default. | To be tested |
|  | DeleteWindowsBareMetalServerPassword | Clear the password records generated during the initial installation of Windows bare metal server. After the password is cleared, the login to the BMS password is not affected. However, you cannot obtain the password to query the BMS password. If the BMS is created using a private image, ensure that Cloudbase-Init has been installed. This software is installed on the public image by default. | To be tested |
|  bare metal server Specification Management | ListBaremetalFlavorDetailExtends | Query the specification details and extended information about bare metal server. You can call this API to query the value of baremetal:extBootType to check whether a flavor supports quick provisioning.  | To be tested |
|  bare metal server Status Management | BatchStopBaremetalServers | Stops BMSs in batches based on the specified bare metal server ID list. | To be tested |
|  | BatchStartBaremetalServers | Starts BMSs in batches based on the specified bare metal server ID list. | To be tested |
|  | BatchRebootBaremetalServers | Restarts BMSs in batches based on the specified bare metal server ID list. | To be tested |
|  | ChangeBaremetalServerName | Change the bare metal server name. | To be tested |
|  | ChangeBaremetalServerOs | Switch the operating system of the bare metal server. Switching the OS supports password or key injection. This API supports fine-grained permission verification for enterprise projects.  | To be tested |
|  | ReinstallBaremetalServerOs | Reinstall the operating system of the bare metal server. When quickly provisioning a BMS, you can use the original image to reinstall the system disk when the data disk of the BMS remains unchanged. Password or key injection is supported during OS reinstallation.  | To be tested |
|  bare metal server Tenant Quota Management | ShowTenantQuota | Query the quota information about all resources under the tenant, including the used quota. | To be tested |
| Job management | ShowJobInfos | Query the execution status of a job. For asynchronous APIs, such as creating bare metal server physical machines and mounting and detaching volumes, after the command is delivered, job_id is returned. You can use job_id to query the execution status of the task.  | To be tested |
| Query API version information | ShowVersionsInfo | Query all available API versions of the bare metal server. | To be tested |
|  | ShowSpecifiedVersion | Query the version of a specified API of the BMS service | To be tested |
| Status management | ShowServerRemoteConsole | Obtain the VNC remote login address of the ECS. | To be tested |

