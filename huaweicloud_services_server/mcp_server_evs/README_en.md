# EVS MCP Server 


## Version
v0.1.0

## Overview

EVS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EVS. Full-chain management of EVS resources can be carried out based on natural language.

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
                    <td rowspan="6">EVS Snapshot</td>
                    <td>RollbackSnapshot</td>
                    <td>This API is used to roll back the snapshot data to the EVS disk. Enterprise project authorization is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshots</td>
                    <td>Query the details about EVS snapshots.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSnapshot</td>
                    <td>Delete an EVS snapshot.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSnapshot</td>
                    <td>Create an EVS snapshot.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSnapshot</td>
                    <td>Query the snapshot information of a single EVS disk. The enterprise project authorization function is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSnapshot</td>
                    <td>This API is used to update an EVS snapshot. Enterprise project authorization is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">EVS disk</td>
                    <td>RetypeVolume</td>
                    <td>Change the disk type of a pay-per-use or yearly/monthly EVS disk.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVolumes</td>
                    <td>Query details about all EVS disks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderListAvailabilityZones</td>
                    <td>Query information about all AZs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeVolume</td>
                    <td>Expand the capacity of a pay-per-use or yearly/monthly EVS disk.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVolume</td>
                    <td>Delete an EVS disk.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVolume</td>
                    <td>This API is used to update the name and description of an EVS disk.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnsubscribePostpaidVolume</td>
                    <td>Unsubscribe from a yearly/monthly EVS disk with the following restrictions:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyVolumeQoS</td>
                    <td>Adjust the IOPS or throughput of the EVS disk.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVolume</td>
                    <td>Create a pay-per-use or yearly/monthly EVS disk.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderListQuotas</td>
                    <td>Query detailed quotas of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderListVolumeTypes</td>
                    <td>Query the EVS disk type list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">EVS disk tag</td>
                    <td>ShowVolumeTags</td>
                    <td>Query the tag information of a specified EVS disk.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVolumeTags</td>
                    <td>This API is used to obtain the tags of all EVS resources of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVolumesByTags</td>
                    <td>This API is used to query details about an EVS instance by tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateVolumeTags</td>
                    <td>Add tags to specified EVS disks in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteVolumeTags</td>
                    <td>This API is used to delete tags for specified EVS disks in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">EVS disk transfer</td>
                    <td>CinderDeleteVolumeTransfer</td>
                    <td>If the EVS disk ownership transfer is not accepted, you can delete the EVS disk ownership transfer record. After the transfer is accepted, you cannot delete the EVS disk ownership.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderListVolumeTransfers</td>
                    <td>Query the ownership transfer records of all EVS disks of the current tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderCreateVolumeTransfer</td>
                    <td>Specify an EVS disk to create an EVS disk transfer record. After the EVS disk is created successfully, the transfer record ID and identity authentication key are returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderShowVolumeTransfer</td>
                    <td>Query the details about the ownership transfer record of a single EVS disk, including the creation time, ID, and name of the transfer record.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CinderAcceptVolumeTransfer</td>
                    <td>The transfer record ID and identity authentication key are used to accept the transfer of the EVS disk ownership.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Edge disk</td>
                    <td>ShowVolume</td>
                    <td>Query disk details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Mirror Task</td>
                    <td>ShowJob</td>
                    <td>This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query the API version information about the CMK</td>
                    <td>ShowVersion</td>
                    <td>-Function description: This API is used to query the version information of a specified API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query version operation</td>
                    <td>ListVersions</td>
                    <td>Query the version number supported by SMN open APIs.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
