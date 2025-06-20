# EVS MCP Server 


## Version
v0.1.0

## Overview

EVS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EVS. Full-chain management of EVS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| EVS Snapshot | RollbackSnapshot | This API is used to roll back the snapshot data to the EVS disk. Enterprise project authorization is supported. | To be tested |
|  | ListSnapshots | Query the details about EVS snapshots. | To be tested |
|  | DeleteSnapshot | Delete an EVS snapshot. | To be tested |
|  | CreateSnapshot | Create an EVS snapshot. | To be tested |
|  | ShowSnapshot | Query the snapshot information of a single EVS disk. The enterprise project authorization function is supported. | To be tested |
|  | UpdateSnapshot | This API is used to update an EVS snapshot. Enterprise project authorization is supported. | To be tested |
| EVS disk | RetypeVolume | Change the disk type of a pay-per-use or yearly/monthly EVS disk. | To be tested |
|  | ListVolumes | Query details about all EVS disks. | To be tested |
|  | CinderListAvailabilityZones | Query information about all AZs. | To be tested |
|  | ResizeVolume | Expand the capacity of a pay-per-use or yearly/monthly EVS disk. | To be tested |
|  | DeleteVolume | Delete an EVS disk. | To be tested |
|  | UpdateVolume | This API is used to update the name and description of an EVS disk. | To be tested |
|  | UnsubscribePostpaidVolume | Unsubscribe from a yearly/monthly EVS disk with the following restrictions: | To be tested |
|  | ModifyVolumeQoS | Adjust the IOPS or throughput of the EVS disk. | To be tested |
|  | CreateVolume | Create a pay-per-use or yearly/monthly EVS disk. | To be tested |
|  | CinderListQuotas | Query detailed quotas of a tenant. | To be tested |
|  | CinderListVolumeTypes | Query the EVS disk type list. | To be tested |
| EVS disk tag | ShowVolumeTags | Query the tag information of a specified EVS disk. | To be tested |
|  | ListVolumeTags | This API is used to obtain the tags of all EVS resources of a tenant. | To be tested |
|  | ListVolumesByTags | This API is used to query details about an EVS instance by tag. | To be tested |
|  | BatchCreateVolumeTags | Add tags to specified EVS disks in batches. | To be tested |
|  | BatchDeleteVolumeTags | This API is used to delete tags for specified EVS disks in batches. | To be tested |
| EVS disk transfer | CinderDeleteVolumeTransfer | If the EVS disk ownership transfer is not accepted, you can delete the EVS disk ownership transfer record. After the transfer is accepted, you cannot delete the EVS disk ownership. | To be tested |
|  | CinderListVolumeTransfers | Query the ownership transfer records of all EVS disks of the current tenant. | To be tested |
|  | CinderCreateVolumeTransfer | Specify an EVS disk to create an EVS disk transfer record. After the EVS disk is created successfully, the transfer record ID and identity authentication key are returned. | To be tested |
|  | CinderShowVolumeTransfer | Query the details about the ownership transfer record of a single EVS disk, including the creation time, ID, and name of the transfer record. | To be tested |
|  | CinderAcceptVolumeTransfer | The transfer record ID and identity authentication key are used to accept the transfer of the EVS disk ownership. | To be tested |
| Edge disk | ShowVolume | Query disk details. | To be tested |
| Mirror Task | ShowJob | This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task. | To be tested |
| Query the API version information about the CMK | ShowVersion | -Function description: This API is used to query the version information of a specified API. | To be tested |
| Query version operation | ListVersions | Query the version number supported by SMN open APIs. | To be tested |

