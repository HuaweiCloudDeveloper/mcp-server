# ECS MCP Server 


## Version
v0.1.0

## Overview

ECS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ECS. Full-chain management of ECS resources can be carried out based on natural language.

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
                    <td rowspan="2">AZ management</td>
                    <td>ListServerAzInfo</td>
                    <td>Query the AZ list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListAvailabilityZones</td>
                    <td>Query the AZ list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Batch operation</td>
                    <td>BatchResetServersPassword</td>
                    <td>Resetting the passwords of ECS management accounts (root or Administrator) in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopServers</td>
                    <td>Stops a maximum of 1000 ECSs in a batch based on the specified ECS ID list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRebootServers</td>
                    <td>Restarts ECSs in batches based on the specified ECS ID list. A maximum of 1000 ECSs can be restarted at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartServers</td>
                    <td>Starts ECSs in batches based on the specified ECS ID list. A maximum of 1000 ECSs can be started at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateServersName</td>
                    <td>This API is used to modify ECS information in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAttachSharableVolumes</td>
                    <td>Attach a specified shared disk to multiple ECSs at a time to implement batch attachment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Cloud Server Group Management</td>
                    <td>CreateServerGroup</td>
                    <td>Create an ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerGroups</td>
                    <td>Query the ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerGroup</td>
                    <td>Query ECS group details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaDeleteServerGroup</td>
                    <td>Delete an ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddServerGroupMember</td>
                    <td>Add the ECS to the ECS group. After the ECS group is added successfully, if the ECS group is configured with the anti-affinity policy, the ECS and other members in the ECS group are created on different hosts. If the ECS is of the Fault Domain type, the ECS has the Fault Domain attribute.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListServerGroups</td>
                    <td>Query the ECS group list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaCreateServerGroup</td>
                    <td>Create an ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServerGroupMember</td>
                    <td>This API is used to remove the ECS from the ECS group. After the ECS is removed, the ECS and members in the ECS group do not comply with the anti-affinity policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServerGroup</td>
                    <td>Query details about an ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServerGroup</td>
                    <td>Delete an ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Cloud Server Operation Management</td>
                    <td>NovaListServerActions</td>
                    <td>Query all historical operations on an ECS. The operation list is displayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServerAction</td>
                    <td>Query a request behavior of an ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Disk management</td>
                    <td>NovaAttachVolume</td>
                    <td>A disk is attached to the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListServerVolumes</td>
                    <td>Query the information about the disks attached to the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachServerVolume</td>
                    <td>Detaching a disk from an ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachServerVolume</td>
                    <td>Attach the disk to the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaDetachVolume</td>
                    <td>Detaching a disk from an ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerBlockDevices</td>
                    <td>Query the information about the disks attached to the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerVolumeAttachments</td>
                    <td>Query the information about the disks attached to the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerBlockDevice</td>
                    <td>Query information about a single disk attached to an ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServerBlockDevice</td>
                    <td>Modifies the information about a single disk attached to an ECS. 'Currently, only the delete_on_termination field can be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServerVolume</td>
                    <td>Query information about a single disk attached to an ECS based on the disk ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Engine version and specification</td>
                    <td>ListFlavors</td>
                    <td>Query database specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Key password management</td>
                    <td>NovaDeleteKeypair</td>
                    <td>Delete the specified SSH key based on the SSH key name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaCreateKeypair</td>
                    <td>Create an SSH key or import the public key to the system to generate a key pair.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetServerPassword</td>
                    <td>Reset the password of the ECS management account (root or Administrator).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResetPasswordFlag</td>
                    <td>Query whether the ECS supports one-click password reset.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListKeypairs</td>
                    <td>Query the SSH key list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServerPassword</td>
                    <td>Clear the password records generated during the initial installation of the Windows ECS. Clearing the password does not affect the login to the ECS. However, you cannot obtain the password to query the ECS password.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerPassword</td>
                    <td>When creating a Windows ECS using an image that supports Cloudbase-Init, obtain the random password of the administrator account (administrator account or the account set by Cloudbase-Init) generated during the initial installation of the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowKeypair</td>
                    <td>Query the specified SSH key based on the SSH key name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">Lifecycle Management</td>
                    <td>ListCloudServers</td>
                    <td>API for querying the ECS list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListServersDetails</td>
                    <td>Query the ECS details list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateServers</td>
                    <td>Create one or more ECSs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaUpdateServer</td>
                    <td>Modifies the ECS information. Currently, the name and description of the ECS can be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServer</td>
                    <td>Query details about an ECS based on the ECS ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServer</td>
                    <td>Modifies the ECS information. Currently, the name, description, and host name of an ECS can be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostPaidServers</td>
                    <td>Create one or more pay-per-use (https://support.huaweicloud.com/productdesc-ecs/ecs_01_0065.html) ECSs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServer</td>
                    <td>Query details about an ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaCreateServers</td>
                    <td>Create an ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListServers</td>
                    <td>Query the ECS list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServersDetails</td>
                    <td>Filter and query all ECSs in the database based on the user's request conditions, and associate the query results with related tables to obtain ECS details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServers</td>
                    <td>Deletes ECSs based on the specified ECS ID list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaDeleteServer</td>
                    <td>Delete an ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Metadata management</td>
                    <td>NovaUpdateServerMetadataItem</td>
                    <td>Set the metadata of a specified key for the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServerMetadata</td>
                    <td>Query the ECS metadata.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServerMetadata</td>
                    <td>This API is used to delete the specified metadata of an ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServerMetadataItem</td>
                    <td>Obtain the metadata of a specified key on an ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaUpdateServerMetadata</td>
                    <td>Update the ECS metadata.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServerMetadata</td>
                    <td>Update the ECS metadata.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaCreateServerMetadata</td>
                    <td>This API is used to set ECS metadata information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaDeleteServerMetadataItem</td>
                    <td>Delete the specified metadata of an ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Mirror Task</td>
                    <td>ShowJob</td>
                    <td>This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Network adapter management</td>
                    <td>NovaDetachInterface</td>
                    <td>Detaches a NIC from an ECS based on the specified port ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteServerNics</td>
                    <td>Unmount and delete one or more NICs from the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaAttachInterface</td>
                    <td>Add a NIC to the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServerInterface</td>
                    <td>Update the ECS NIC attachment information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateServerVirtualIp</td>
                    <td>A virtual IP address is used to provide a second IP address for the NIC. It can be bound to the NICs of multiple ECSs to achieve high availability among multiple ECSs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddServerNics</td>
                    <td>Add one or more NICs to the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeVpc</td>
                    <td>The ECS was switched to the VPC.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListServerInterfaces</td>
                    <td>Query the ECS NIC information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerInterfaces</td>
                    <td>Query the ECS NIC information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateServerVirtualIp</td>
                    <td>A virtual IP address is used to provide a second IP address for the NIC. It can be bound to the NICs of multiple ECSs to achieve high availability among multiple ECSs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServerInterface</td>
                    <td>Query the ECS NIC information based on the NIC ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeServerNetworkInterface</td>
                    <td>This API is used to update the attributes of a specified ECS NIC. Currently, only the NIC IP address can be updated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Query API version information</td>
                    <td>NovaListVersions</td>
                    <td>All available Nova versions are returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowVersion</td>
                    <td>Information about the specified version is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Schedule Event</td>
                    <td>ListScheduledEvents</td>
                    <td>Query the list of scheduled events</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Security Group Management</td>
                    <td>NovaDisassociateSecurityGroup</td>
                    <td>Removes a security group from an ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaAssociateSecurityGroup</td>
                    <td>Add a security group to the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListServerSecurityGroups</td>
                    <td>Query the security group of a specified ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Specification Management</td>
                    <td>ListFlavorSellPolicies</td>
                    <td>Query the specification sales policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListFlavors</td>
                    <td>Query the available ECS flavors in the system.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListFlavorsDetails</td>
                    <td>Query the ECS flavor list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowFlavor</td>
                    <td>Query ECS flavor details based on the ECS flavor ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResizeFlavors</td>
                    <td>When ECSs are changing flavors, ECSs with some flavors cannot be changed to each other. You can use this API to query the list of ECS flavors that can be modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowFlavorExtraSpecs</td>
                    <td>Query the details about a specified flavor.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">Status management</td>
                    <td>ResizePostPaidServer</td>
                    <td>If the ECS specifications cannot meet service requirements, you can modify the ECS specifications and upgrade the vCPU and memory. For details about how to use the interface, see this section.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaUnlockServer</td>
                    <td>Unlock the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ReinstallServerWithCloudInit</td>
                    <td>Reinstall the ECS OS. You can use the original image to reinstall the system disk of an ECS without changing the data disk of the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaStartServer</td>
                    <td>Start a single ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeServerOsWithoutCloudInit</td>
                    <td>Switch the ECS OS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaLockServer</td>
                    <td>Lock the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterServerMonitor</td>
                    <td>Add the ECS to the monitoring table.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ReinstallServerWithoutCloudInit</td>
                    <td>Reinstall the ECS OS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerRemoteConsole</td>
                    <td>Obtain the VNC remote login address of the ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateServer</td>
                    <td>-Migrate the ECSs deployed on a DeH to another DeH.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServerAutoTerminateTime</td>
                    <td>Modify the on-demand server and set the scheduled deletion time. If the scheduled deletion time is null, the scheduled deletion is canceled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeServerChargeMode</td>
                    <td>Changing the billing mode of the ECS</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaStopServer</td>
                    <td>Stop a single ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeServer</td>
                    <td>Change the ECS flavor.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaRebootServer</td>
                    <td>Restart a single ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeServerOsWithCloudInit</td>
                    <td>Switch the ECS OS. You can use a new image to reinstall the system disk when the data disk of the ECS remains unchanged.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Tag Management</td>
                    <td>ListServerTags</td>
                    <td>Project is used to group and isolate OpenStack resources (computing, storage, and network resources). A project can be a department or a project team. Multiple projects can be created in an account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteServerTags</td>
                    <td>- This API is used to delete tags from specified ECSs in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerTags</td>
                    <td>-Query the tag information of a specified ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateServerTags</td>
                    <td>- Add tags to specified ECSs in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tenant Quota Management</td>
                    <td>ShowServerLimits</td>
                    <td>Query tenant quota information.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
