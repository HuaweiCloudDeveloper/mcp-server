# BMS MCP Server 


## Version
v0.1.0

## Overview

BMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service BMS. Full-chain management of BMS resources can be carried out based on natural language.

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
                    <td rowspan="3">bare metal server 2D Tag Management</td>
                    <td>BatchDeleteBaremetalServerTags</td>
                    <td>- This API is used to delete tags for specified ECSs in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateBaremetalServerTags</td>
                    <td>-Add tags to specified bare metal server in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBaremetalServerTags</td>
                    <td>- This API is used to query the tag information of a specified ECS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">bare metal server Lifecycle Management</td>
                    <td>ListBareMetalServers</td>
                    <td>Filter bare metal server based on the specified request conditions and obtain details about the BMS. This API is used to query the BMS billing mode and whether the BMS is frozen.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBareMetalServerDetails</td>
                    <td>Obtains bare metal server details. This API can be used to query the billing mode of a BMS and whether the BMS is frozen.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBareMetalServersDetail</td>
                    <td>Filter bare metal server based on the specified request conditions and obtain details about the BMS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBareMetalServers</td>
                    <td>Create one or more bare metal server. The BMS login authentication modes include key pair and password. For security purposes, the key pair mode is recommended.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">bare metal server Management</td>
                    <td>AttachBaremetalServerVolume</td>
                    <td>After the bare metal server is created, if the disk space is insufficient or the current disk does not meet the requirements, you can attach the existing EVS disk to the BMS as a data disk.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachBaremetalServerVolume</td>
                    <td>Demount the disk attached to the bare metal server. Do not detach disks attached to the system disk slot (that is, the /dev/sda mount point). Disks attached to data disk slots (not /dev/sda) can be detached offline or online (BMS is in the Running state)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBaremetalServerVolumeInfo</td>
                    <td>Query the information about the disks attached to the bare metal server</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">bare metal server Metadata Management</td>
                    <td>UpdateBaremetalServerMetadata</td>
                    <td>Updates the bare metal server metadata. If the metadata does not contain the field to be updated, the field is automatically added. If the field to be updated already exists in the metadata, the field value is directly updated. If the field in the metadata is not in the request parameter, it remains unchanged.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">bare metal server NIC Management</td>
                    <td>UpdateBaremetalServerInterfaceAttachments</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBaremetalServerInterfaceAttachments</td>
                    <td>Query the bare metal server network adapter information, such as the IP address and MAC address of the network adapter.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddServerNics</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServerNics</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">bare metal server Password Management</td>
                    <td>ShowResetPwd</td>
                    <td>Query whether one-click password reset is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPwdOneClick</td>
                    <td>Reset the password of the BMS management account (root or Administrator) on the premise that bare metal server supports one-click password reset. You can use the 6.10.1-Querying Whether One-Click Password Reset API to query whether one-click password reset is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWindowsBaremetalServerPwd</td>
                    <td>Obtain the random password of the administrator account (Administrator account or Cloudbase-Init account) generated during the initial installation of Windows bare metal server. If the BMS is created using a private image, ensure that Cloudbase-Init has been installed. This software is installed on the public image by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWindowsBareMetalServerPassword</td>
                    <td>Clear the password records generated during the initial installation of Windows bare metal server. After the password is cleared, the login to the BMS password is not affected. However, you cannot obtain the password to query the BMS password. If the BMS is created using a private image, ensure that Cloudbase-Init has been installed. This software is installed on the public image by default.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">bare metal server Specification Management</td>
                    <td>ListBaremetalFlavorDetailExtends</td>
                    <td>Query the specification details and extended information about bare metal server. You can call this API to query the value of baremetal:extBootType to check whether a flavor supports quick provisioning.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">bare metal server Status Management</td>
                    <td>BatchStopBaremetalServers</td>
                    <td>Stops BMSs in batches based on the specified bare metal server ID list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartBaremetalServers</td>
                    <td>Starts BMSs in batches based on the specified bare metal server ID list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRebootBaremetalServers</td>
                    <td>Restarts BMSs in batches based on the specified bare metal server ID list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeBaremetalServerName</td>
                    <td>Change the bare metal server name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeBaremetalServerOs</td>
                    <td>Switch the operating system of the bare metal server. Switching the OS supports password or key injection. This API supports fine-grained permission verification for enterprise projects.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ReinstallBaremetalServerOs</td>
                    <td>Reinstall the operating system of the bare metal server. When quickly provisioning a BMS, you can use the original image to reinstall the system disk when the data disk of the BMS remains unchanged. Password or key injection is supported during OS reinstallation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">bare metal server Tenant Quota Management</td>
                    <td>ShowTenantQuota</td>
                    <td>Query the quota information about all resources under the tenant, including the used quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job management</td>
                    <td>ShowJobInfos</td>
                    <td>Query the execution status of a job. For asynchronous APIs, such as creating bare metal server physical machines and mounting and detaching volumes, after the command is delivered, job_id is returned. You can use job_id to query the execution status of the task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Query API version information</td>
                    <td>ShowVersionsInfo</td>
                    <td>Query all available API versions of the bare metal server.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSpecifiedVersion</td>
                    <td>Query the version of a specified API of the BMS service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Status management</td>
                    <td>ShowServerRemoteConsole</td>
                    <td>Obtain the VNC remote login address of the ECS.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
