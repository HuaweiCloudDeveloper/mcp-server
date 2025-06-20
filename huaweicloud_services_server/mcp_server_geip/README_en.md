# GEIP MCP Server 


## Version
v0.1.0

## Overview

GEIP MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GEIP. Full-chain management of GEIP resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Access Point | ListAccessSites | Query the access point list | To be tested |
| All-domain EIP | CreateGlobalEip | Creating an EIP for all domains | To be tested |
|  | CountGlobalEips | Query the number of EIPs in all domains. | To be tested |
|  | AssociateInstance | Bind backend instance | To be tested |
|  | DetachInternetBandwidth | Unbind all-domain public network bandwidth | To be tested |
|  | BatchAttachInternetBandwidth | Binding all-domain public network bandwidths in batches | To be tested |
|  | DeleteGlobalEip | Delete an EIP in the entire domain | To be tested |
|  | AttachInternetBandwidth | Binding all-domain public network bandwidths | To be tested |
|  | ListGlobalEips | Query the EIP list in all domains | To be tested |
|  | BatchCreateGlobalEip | Creating all-domain EIPs in batches | To be tested |
|  | ShowGlobalEip | Query EIP details in all domains | To be tested |
|  | BatchDetachInternetBandwidth | Unbinding all domain public network bandwidths in batches | To be tested |
|  | UpdateGlobalEip | Updates EIP information in all domains | To be tested |
|  | DisassociateInstance | Unbinds a backend instance | To be tested |
| All-domain EIP pool | ListGeipPools | Query the list of EIP pools in all domains | To be tested |
| All-domain EIP segment | CreateGlobalEipSegment | Create an EIP segment for all domains. | To be tested |
|  | DisassociateGeipSegmentInstance | Unbind an EIP segment from a backend instance in all domains | To be tested |
|  | CountGlobalEipSegment | Query the number of EIP segments in all domains. | To be tested |
|  | ListGlobalEipSegments | Query the EIP segment list in all domains | To be tested |
|  | DeleteGlobalEipSegment | Delete an EIP segment in all domains. | To be tested |
|  | BatchDetachGeipSegmentInternetBandwidth | Unbind all-domain EIP segments from all-domain EIP segments in batches | To be tested |
|  | UpdateGlobalEipSegment | Updating an EIP segment in all domains | To be tested |
|  | AssociateGeipSegmentInstance | EIP segments in all domains are bound to backend instances. | To be tested |
|  | ShowGlobalEipSegment | Query the details of an EIP segment in all domains | To be tested |
|  | BatchAttachGeipSegmentInternetBandwidth | All-domain EIP segments are bound to all-domain public network bandwidths in batches | To be tested |
| All-domain EIP segment label | BatchDeleteGeipSegmentTags | Delete tags of EIP segments in all domains in batches | To be tested |
|  | AddGeipSegmentTags | Adding a tag to the EIP segment of all domains | To be tested |
|  | ListGeipSegmentCountFilterTags | Query the number of resource instances | To be tested |
|  | ListGeipSegmentDomainTags | Query the project tags of the EIP segment in all domains | To be tested |
|  | DeleteGeipSegmentTag | Delete the tag for the EIP segment in all domains. | To be tested |
|  | ListGeipSegmentFilterTags | Query the resource instance list | To be tested |
|  | ShowGeipSegmentTags | Query the labels of the EIP segment in all domains. | To be tested |
|  | BatchCreateGeipSegmentTags | Add labels for EIP segments in all domains in batches | To be tested |
| All-domain public network bandwidth label | ListInternetBandwidthCountFilterTags | Query the number of resource instances | To be tested |
|  | ShowInternetBandwidthTags | Query the public network bandwidth tag in the entire domain | To be tested |
|  | AddInternetBandwidthTags | Adding a global public network bandwidth tag | To be tested |
|  | BatchDeleteInternetBandwidthTags | Delete all-domain public network bandwidth tags in batches | To be tested |
|  | DeleteInternetBandwidthTag | Delete the public bandwidth tag of the entire domain. | To be tested |
|  | ListInternetBandwidthDomainTags | Query the tag of a public bandwidth project in all domains | To be tested |
|  | BatchCreateInternetBandwidthTags | Adding all-domain public network bandwidth tags in batches | To be tested |
|  | ListInternetBandwidthFilterTags | Query the resource instance list | To be tested |
| Global EIP Tag | ListGlobalEipDomainTags | Query the project tags of all EIPs in all domains | To be tested |
|  | BatchDeleteGlobalEipTags | Delete tags for EIPs in all domains in batches | To be tested |
|  | AddGlobalEipTags | Adding a tag for an EIP in the entire domain | To be tested |
|  | ListGlobalEipCountFilterTags | Query the number of resource instances | To be tested |
|  | DeleteGlobalEipTag | Delete the tag of an EIP in all domains. | To be tested |
|  | ShowGlobalEipTags | Query the EIP tags in all domains | To be tested |
|  | ListGlobalEipFilterTags | Query the resource instance list | To be tested |
|  | BatchCreateGlobalEipTags | Adding all-domain EIP tags in batches | To be tested |
| Global public network bandwidth | CountInternetBandwidth | Query the number of public network bandwidths in all domains. | To be tested |
|  | ShowInternetBandwidth | Query all-domain public network bandwidth details | To be tested |
|  | CreateInternetBandwidth | Create an all-domain public network bandwidth. | To be tested |
|  | DeleteInternetBandwidth | Delete all-domain public network bandwidth | To be tested |
|  | BatchCreateInternetBandwidth | Creating all-domain public network bandwidths in batches | To be tested |
|  | UpdateInternetBandwidth | Updating the public network bandwidth of all domains | To be tested |
|  | ListInternetBandwidths | Query the public network bandwidth list of all domains. | To be tested |
| Global public network bandwidth limit | ListInternetBandwidthLimits | Query the public network bandwidth limit list of all domains | To be tested |
| Job-related interfaces | ShowJobs | Query job details | To be tested |
| Mask Restriction | ListSupportMasks | Query the masks supported by the EIP segments in all domains. | To be tested |
| Multi-area Key | ListSupportRegions | -Function description: This API is used to query the regions supported by the cross-region key. | To be tested |
| Quota | ListGeipResourceQuotas | Query the EIP quota of a tenant in all domains | To be tested |
| Region limit | ListTenantGeipSupportInstances | The console uses this API to obtain the region instance information that can be bound to the global EIP of a specified POP. | To be tested |
| Signing of exemption clauses | CreateUserDisclaimer | Create a tenant and sign exemption clauses. | To be tested |
|  | ShowUserDisclaimer | Query the exemption clause details signed by the tenant | To be tested |
|  | DeleteUserDisclaimer | Delete the exemption clause for the tenant. | To be tested |
| Task Center API | ListJobs | Query the task center on the management plane. This API is used to query details about the asynchronous operations such as creating, closing, starting, deleting, adding, importing, exporting, and upgrading a graph. The operations include creating, closing, starting, deleting, and backing up a graph, importing, exporting, and upgrading a graph. | To be tested |

