# ECS MCP Server 


## Version
v0.1.0

## Overview

ECS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ECS. Full-chain management of ECS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AZ management | ListServerAzInfo | Query the AZ list | To be tested |
|  | NovaListAvailabilityZones | Query the AZ list. | To be tested |
| Batch operation | BatchResetServersPassword | Resetting the passwords of ECS management accounts (root or Administrator) in batches. | To be tested |
|  | BatchStopServers | Stops a maximum of 1000 ECSs in a batch based on the specified ECS ID list. | To be tested |
|  | BatchRebootServers | Restarts ECSs in batches based on the specified ECS ID list. A maximum of 1000 ECSs can be restarted at a time. | To be tested |
|  | BatchStartServers | Starts ECSs in batches based on the specified ECS ID list. A maximum of 1000 ECSs can be started at a time. | To be tested |
|  | BatchUpdateServersName | This API is used to modify ECS information in batches. | To be tested |
|  | BatchAttachSharableVolumes | Attach a specified shared disk to multiple ECSs at a time to implement batch attachment. | To be tested |
| Cloud Server Group Management | CreateServerGroup | Create an ECS group. | To be tested |
|  | ListServerGroups | Query the ECS group. | To be tested |
|  | ShowServerGroup | Query ECS group details. | To be tested |
|  | NovaDeleteServerGroup | Delete an ECS group. | To be tested |
|  | AddServerGroupMember | Add the ECS to the ECS group. After the ECS group is added successfully, if the ECS group is configured with the anti-affinity policy, the ECS and other members in the ECS group are created on different hosts. If the ECS is of the Fault Domain type, the ECS has the Fault Domain attribute. | To be tested |
|  | NovaListServerGroups | Query the ECS group list. | To be tested |
|  | NovaCreateServerGroup | Create an ECS group. | To be tested |
|  | DeleteServerGroupMember | This API is used to remove the ECS from the ECS group. After the ECS is removed, the ECS and members in the ECS group do not comply with the anti-affinity policy. | To be tested |
|  | NovaShowServerGroup | Query details about an ECS group. | To be tested |
|  | DeleteServerGroup | Delete an ECS group. | To be tested |
| Cloud Server Operation Management | NovaListServerActions | Query all historical operations on an ECS. The operation list is displayed. | To be tested |
|  | NovaShowServerAction | Query a request behavior of an ECS. | To be tested |
| Disk management | NovaAttachVolume | A disk is attached to the ECS. | To be tested |
|  | NovaListServerVolumes | Query the information about the disks attached to the ECS. | To be tested |
|  | DetachServerVolume | Detaching a disk from an ECS. | To be tested |
|  | AttachServerVolume | Attach the disk to the ECS. | To be tested |
|  | NovaDetachVolume | Detaching a disk from an ECS. | To be tested |
|  | ListServerBlockDevices | Query the information about the disks attached to the ECS. | To be tested |
|  | ListServerVolumeAttachments | Query the information about the disks attached to the ECS. | To be tested |
|  | ShowServerBlockDevice | Query information about a single disk attached to an ECS. | To be tested |
|  | UpdateServerBlockDevice | Modifies the information about a single disk attached to an ECS. 'Currently, only the delete_on_termination field can be modified. | To be tested |
|  | NovaShowServerVolume | Query information about a single disk attached to an ECS based on the disk ID. | To be tested |
| Engine version and specification | ListFlavors | Query database specifications. | To be tested |
| Key password management | NovaDeleteKeypair | Delete the specified SSH key based on the SSH key name. | To be tested |
|  | NovaCreateKeypair | Create an SSH key or import the public key to the system to generate a key pair. | To be tested |
|  | ResetServerPassword | Reset the password of the ECS management account (root or Administrator). | To be tested |
|  | ShowResetPasswordFlag | Query whether the ECS supports one-click password reset. | To be tested |
|  | NovaListKeypairs | Query the SSH key list. | To be tested |
|  | DeleteServerPassword | Clear the password records generated during the initial installation of the Windows ECS. Clearing the password does not affect the login to the ECS. However, you cannot obtain the password to query the ECS password. | To be tested |
|  | ShowServerPassword | When creating a Windows ECS using an image that supports Cloudbase-Init, obtain the random password of the administrator account (administrator account or the account set by Cloudbase-Init) generated during the initial installation of the ECS. | To be tested |
|  | NovaShowKeypair | Query the specified SSH key based on the SSH key name. | To be tested |
| Lifecycle Management | ListCloudServers | API for querying the ECS list. | To be tested |
|  | NovaListServersDetails | Query the ECS details list. | To be tested |
|  | CreateServers | Create one or more ECSs. | To be tested |
|  | NovaUpdateServer | Modifies the ECS information. Currently, the name and description of the ECS can be modified. | To be tested |
|  | NovaShowServer | Query details about an ECS based on the ECS ID. | To be tested |
|  | UpdateServer | Modifies the ECS information. Currently, the name, description, and host name of an ECS can be modified. | To be tested |
|  | CreatePostPaidServers | Create one or more pay-per-use (https://support.huaweicloud.com/productdesc-ecs/ecs_01_0065.html) ECSs. | To be tested |
|  | ShowServer | Query details about an ECS. | To be tested |
|  | NovaCreateServers | Create an ECS. | To be tested |
|  | NovaListServers | Query the ECS list. | To be tested |
|  | ListServersDetails | Filter and query all ECSs in the database based on the user's request conditions, and associate the query results with related tables to obtain ECS details. | To be tested |
|  | DeleteServers | Deletes ECSs based on the specified ECS ID list. | To be tested |
|  | NovaDeleteServer | Delete an ECS. | To be tested |
| Metadata management | NovaUpdateServerMetadataItem | Set the metadata of a specified key for the ECS. | To be tested |
|  | NovaShowServerMetadata | Query the ECS metadata. | To be tested |
|  | DeleteServerMetadata | This API is used to delete the specified metadata of an ECS. | To be tested |
|  | NovaShowServerMetadataItem | Obtain the metadata of a specified key on an ECS. | To be tested |
|  | NovaUpdateServerMetadata | Update the ECS metadata. | To be tested |
|  | UpdateServerMetadata | Update the ECS metadata. | To be tested |
|  | NovaCreateServerMetadata | This API is used to set ECS metadata information. | To be tested |
|  | NovaDeleteServerMetadataItem | Delete the specified metadata of an ECS. | To be tested |
| Mirror Task | ShowJob | This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task. | To be tested |
| Network adapter management | NovaDetachInterface | Detaches a NIC from an ECS based on the specified port ID. | To be tested |
|  | BatchDeleteServerNics | Unmount and delete one or more NICs from the ECS. | To be tested |
|  | NovaAttachInterface | Add a NIC to the ECS. | To be tested |
|  | UpdateServerInterface | Update the ECS NIC attachment information. | To be tested |
|  | DisassociateServerVirtualIp | A virtual IP address is used to provide a second IP address for the NIC. It can be bound to the NICs of multiple ECSs to achieve high availability among multiple ECSs. | To be tested |
|  | BatchAddServerNics | Add one or more NICs to the ECS. | To be tested |
|  | ChangeVpc | The ECS was switched to the VPC. | To be tested |
|  | NovaListServerInterfaces | Query the ECS NIC information. | To be tested |
|  | ListServerInterfaces | Query the ECS NIC information. | To be tested |
|  | AssociateServerVirtualIp | A virtual IP address is used to provide a second IP address for the NIC. It can be bound to the NICs of multiple ECSs to achieve high availability among multiple ECSs. | To be tested |
|  | NovaShowServerInterface | Query the ECS NIC information based on the NIC ID. | To be tested |
|  | ChangeServerNetworkInterface | This API is used to update the attributes of a specified ECS NIC. Currently, only the NIC IP address can be updated. | To be tested |
| Query API version information | NovaListVersions | All available Nova versions are returned. | To be tested |
|  | NovaShowVersion | Information about the specified version is returned. | To be tested |
| Schedule Event | ListScheduledEvents | Query the list of scheduled events | To be tested |
| Security Group Management | NovaDisassociateSecurityGroup | Removes a security group from an ECS. | To be tested |
|  | NovaAssociateSecurityGroup | Add a security group to the ECS. | To be tested |
|  | NovaListServerSecurityGroups | Query the security group of a specified ECS. | To be tested |
| Specification Management | ListFlavorSellPolicies | Query the specification sales policy. | To be tested |
|  | NovaListFlavors | Query the available ECS flavors in the system. | To be tested |
|  | NovaListFlavorsDetails | Query the ECS flavor list. | To be tested |
|  | NovaShowFlavor | Query ECS flavor details based on the ECS flavor ID. | To be tested |
|  | ListResizeFlavors | When ECSs are changing flavors, ECSs with some flavors cannot be changed to each other. You can use this API to query the list of ECS flavors that can be modified. | To be tested |
|  | NovaShowFlavorExtraSpecs | Query the details about a specified flavor. | To be tested |
| Status management | ResizePostPaidServer | If the ECS specifications cannot meet service requirements, you can modify the ECS specifications and upgrade the vCPU and memory. For details about how to use the interface, see this section. | To be tested |
|  | NovaUnlockServer | Unlock the ECS. | To be tested |
|  | ReinstallServerWithCloudInit | Reinstall the ECS OS. You can use the original image to reinstall the system disk of an ECS without changing the data disk of the ECS. | To be tested |
|  | NovaStartServer | Start a single ECS. | To be tested |
|  | ChangeServerOsWithoutCloudInit | Switch the ECS OS. | To be tested |
|  | NovaLockServer | Lock the ECS. | To be tested |
|  | RegisterServerMonitor | Add the ECS to the monitoring table. | To be tested |
|  | ReinstallServerWithoutCloudInit | Reinstall the ECS OS. | To be tested |
|  | ShowServerRemoteConsole | Obtain the VNC remote login address of the ECS. | To be tested |
|  | MigrateServer | -Migrate the ECSs deployed on a DeH to another DeH. | To be tested |
|  | UpdateServerAutoTerminateTime | Modify the on-demand server and set the scheduled deletion time. If the scheduled deletion time is null, the scheduled deletion is canceled. | To be tested |
|  | ChangeServerChargeMode | Changing the billing mode of the ECS | To be tested |
|  | NovaStopServer | Stop a single ECS. | To be tested |
|  | ResizeServer | Change the ECS flavor. | To be tested |
|  | NovaRebootServer | Restart a single ECS. | To be tested |
|  | ChangeServerOsWithCloudInit | Switch the ECS OS. You can use a new image to reinstall the system disk when the data disk of the ECS remains unchanged. | To be tested |
| Tag Management | ListServerTags | Project is used to group and isolate OpenStack resources (computing, storage, and network resources). A project can be a department or a project team. Multiple projects can be created in an account. | To be tested |
|  | BatchDeleteServerTags | - This API is used to delete tags from specified ECSs in batches. | To be tested |
|  | ShowServerTags | -Query the tag information of a specified ECS. | To be tested |
|  | BatchCreateServerTags | - Add tags to specified ECSs in batches. | To be tested |
| Tenant Quota Management | ShowServerLimits | Query tenant quota information. | To be tested |

