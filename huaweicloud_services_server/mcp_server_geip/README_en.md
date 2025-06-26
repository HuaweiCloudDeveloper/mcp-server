# GEIP MCP Server 


## Version
v0.1.0

## Overview

GEIP MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GEIP. Full-chain management of GEIP resources can be carried out based on natural language.

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
                    <td rowspan="1">Access Point</td>
                    <td>ListAccessSites</td>
                    <td>Query the access point list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">All-domain EIP</td>
                    <td>CreateGlobalEip</td>
                    <td>Creating an EIP for all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountGlobalEips</td>
                    <td>Query the number of EIPs in all domains.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateInstance</td>
                    <td>Bind backend instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachInternetBandwidth</td>
                    <td>Unbind all-domain public network bandwidth</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAttachInternetBandwidth</td>
                    <td>Binding all-domain public network bandwidths in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGlobalEip</td>
                    <td>Delete an EIP in the entire domain</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachInternetBandwidth</td>
                    <td>Binding all-domain public network bandwidths</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalEips</td>
                    <td>Query the EIP list in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateGlobalEip</td>
                    <td>Creating all-domain EIPs in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGlobalEip</td>
                    <td>Query EIP details in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDetachInternetBandwidth</td>
                    <td>Unbinding all domain public network bandwidths in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGlobalEip</td>
                    <td>Updates EIP information in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateInstance</td>
                    <td>Unbinds a backend instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">All-domain EIP pool</td>
                    <td>ListGeipPools</td>
                    <td>Query the list of EIP pools in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">All-domain EIP segment</td>
                    <td>CreateGlobalEipSegment</td>
                    <td>Create an EIP segment for all domains.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateGeipSegmentInstance</td>
                    <td>Unbind an EIP segment from a backend instance in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountGlobalEipSegment</td>
                    <td>Query the number of EIP segments in all domains.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalEipSegments</td>
                    <td>Query the EIP segment list in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGlobalEipSegment</td>
                    <td>Delete an EIP segment in all domains.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDetachGeipSegmentInternetBandwidth</td>
                    <td>Unbind all-domain EIP segments from all-domain EIP segments in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGlobalEipSegment</td>
                    <td>Updating an EIP segment in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateGeipSegmentInstance</td>
                    <td>EIP segments in all domains are bound to backend instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGlobalEipSegment</td>
                    <td>Query the details of an EIP segment in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAttachGeipSegmentInternetBandwidth</td>
                    <td>All-domain EIP segments are bound to all-domain public network bandwidths in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">All-domain EIP segment label</td>
                    <td>BatchDeleteGeipSegmentTags</td>
                    <td>Delete tags of EIP segments in all domains in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddGeipSegmentTags</td>
                    <td>Adding a tag to the EIP segment of all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGeipSegmentCountFilterTags</td>
                    <td>Query the number of resource instances</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGeipSegmentDomainTags</td>
                    <td>Query the project tags of the EIP segment in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGeipSegmentTag</td>
                    <td>Delete the tag for the EIP segment in all domains.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGeipSegmentFilterTags</td>
                    <td>Query the resource instance list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGeipSegmentTags</td>
                    <td>Query the labels of the EIP segment in all domains.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateGeipSegmentTags</td>
                    <td>Add labels for EIP segments in all domains in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">All-domain public network bandwidth label</td>
                    <td>ListInternetBandwidthCountFilterTags</td>
                    <td>Query the number of resource instances</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInternetBandwidthTags</td>
                    <td>Query the public network bandwidth tag in the entire domain</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddInternetBandwidthTags</td>
                    <td>Adding a global public network bandwidth tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteInternetBandwidthTags</td>
                    <td>Delete all-domain public network bandwidth tags in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInternetBandwidthTag</td>
                    <td>Delete the public bandwidth tag of the entire domain.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInternetBandwidthDomainTags</td>
                    <td>Query the tag of a public bandwidth project in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateInternetBandwidthTags</td>
                    <td>Adding all-domain public network bandwidth tags in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInternetBandwidthFilterTags</td>
                    <td>Query the resource instance list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Global EIP Tag</td>
                    <td>ListGlobalEipDomainTags</td>
                    <td>Query the project tags of all EIPs in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteGlobalEipTags</td>
                    <td>Delete tags for EIPs in all domains in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddGlobalEipTags</td>
                    <td>Adding a tag for an EIP in the entire domain</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalEipCountFilterTags</td>
                    <td>Query the number of resource instances</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGlobalEipTag</td>
                    <td>Delete the tag of an EIP in all domains.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGlobalEipTags</td>
                    <td>Query the EIP tags in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalEipFilterTags</td>
                    <td>Query the resource instance list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateGlobalEipTags</td>
                    <td>Adding all-domain EIP tags in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Global public network bandwidth</td>
                    <td>CountInternetBandwidth</td>
                    <td>Query the number of public network bandwidths in all domains.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInternetBandwidth</td>
                    <td>Query all-domain public network bandwidth details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInternetBandwidth</td>
                    <td>Create an all-domain public network bandwidth.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInternetBandwidth</td>
                    <td>Delete all-domain public network bandwidth</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateInternetBandwidth</td>
                    <td>Creating all-domain public network bandwidths in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInternetBandwidth</td>
                    <td>Updating the public network bandwidth of all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInternetBandwidths</td>
                    <td>Query the public network bandwidth list of all domains.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Global public network bandwidth limit</td>
                    <td>ListInternetBandwidthLimits</td>
                    <td>Query the public network bandwidth limit list of all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job-related interfaces</td>
                    <td>ShowJobs</td>
                    <td>Query job details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Mask Restriction</td>
                    <td>ListSupportMasks</td>
                    <td>Query the masks supported by the EIP segments in all domains.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Multi-area Key</td>
                    <td>ListSupportRegions</td>
                    <td>-Function description: This API is used to query the regions supported by the cross-region key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ListGeipResourceQuotas</td>
                    <td>Query the EIP quota of a tenant in all domains</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Region limit</td>
                    <td>ListTenantGeipSupportInstances</td>
                    <td>The console uses this API to obtain the region instance information that can be bound to the global EIP of a specified POP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Signing of exemption clauses</td>
                    <td>CreateUserDisclaimer</td>
                    <td>Create a tenant and sign exemption clauses.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserDisclaimer</td>
                    <td>Query the exemption clause details signed by the tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUserDisclaimer</td>
                    <td>Delete the exemption clause for the tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Task Center API</td>
                    <td>ListJobs</td>
                    <td>Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
