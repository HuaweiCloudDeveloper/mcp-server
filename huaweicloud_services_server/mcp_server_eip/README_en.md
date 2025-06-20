# EIP MCP Server 


## Version
v0.1.0

## Overview

EIP MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EIP. Full-chain management of EIP resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Bandwidth | AddPublicipsIntoSharedBandwidth | The EIP is inserted into the shared bandwidth. | To be tested |
|  | UpdatePrePaidBandwidth | Update the bandwidth. | To be tested |
|  | UpdateBandwidth | Update the bandwidth. | To be tested |
|  | ListBandwidths | Query the bandwidth list. | To be tested |
|  | ChangeBandwidthToPeriod | On-demand subcontracting API for tenants. | To be tested |
|  | DeleteSharedBandwidth | Delete the shared bandwidth. | To be tested |
|  | RemovePublicipsFromSharedBandwidth | The EIP is removed from the shared bandwidth. | To be tested |
|  | ListEipBandwidths | Query the bandwidth list | To be tested |
|  | ShowBandwidth | Query bandwidth details. | To be tested |
|  | CreateSharedBandwidth | Create a shared bandwidth. | To be tested |
|  | BatchModifyBandwidth | This API is not applicable to batch bandwidth, shared bandwidth, and yearly/monthly bandwidth update. | To be tested |
|  | BatchCreateSharedBandwidths | Create shared bandwidths in batches. | To be tested |
|  | ListBandwidth | Query the bandwidth list | To be tested |
|  | ListBandwidthsLimit | Obtains the EIP bandwidth limit list. | To be tested |
| Bandwidth add-on package | ListBandwidthPkg | Query the bandwidth add-on package list | To be tested |
| Binding relationship between GEIP and instances | ListProjectGeipBindings | Query the list of tenants bound to GEIPs and instances. | To be tested |
| EIP | DeletePublicip | This API is used to delete an EIP that is bound to an EIP. The EIP cannot be deleted directly. | To be tested |
|  | ListPublicips | Query the EIP list | To be tested |
|  | DisableNat64 | Disable NAT64 for EIPs | To be tested |
|  | ChangePublicipToPeriod | On-demand subcontracting API for tenants. | To be tested |
|  | AttachBatchPublicIp | Adding shared bandwidths to EIPs in batches | To be tested |
|  | ShowPublicip | Query EIP details | To be tested |
|  | CountEipAvailableResources | The IP address pool is used to query the number of available public IP addresses. | To be tested |
|  | DisassociatePublicips | Unbinding an EIP | To be tested |
|  | EnableNat64 | Enable NAT64 for EIPs | To be tested |
|  | AssociatePublicips | Bound an EIP | To be tested |
|  | DetachShareBandwidth | Remove an EIP from the shared bandwidth | To be tested |
|  | CreatePublicip | Apply for an EIP. Both IPv4 and IPv6 are supported. | To be tested |
|  | CreatePrePaidPublicip | Applying for a yearly/monthly EIP. | To be tested |
|  | UpdatePublicip | Update EIP | To be tested |
|  | AttachShareBandwidth | Adding the shared bandwidth to an EIP | To be tested |
|  | DetachBatchPublicIp | Remove EIPs from Shared Bandwidth in Batches | To be tested |
| EIP Tag Management | ShowPublicipTags | Query the tag information of a specified EIP instance. | To be tested |
|  | BatchDeletePublicipTags | This API is used to delete tags for specified EIP instances in batches. | To be tested |
|  | CreatePublicipTag | This API is used to add tags to a specified EIP resource instance. | To be tested |
|  | BatchCreatePublicipTags | This API is used to add tags to specified EIP instances in batches. | To be tested |
|  | ListPublicipsByTags | Filter EIPs by tag. | To be tested |
|  | DeletePublicipTag | This API is used to delete the tag information of a specified EIP. In the preceding command, project_id indicates the project ID, and publicip_id indicates the ID of the EIP to be operated. key is the key of the label to be deleted. | To be tested |
|  | ListPublicipTags | Query all tags of a tenant in a specified region and instance type. | To be tested |
| Elastic IP address auxiliary interface | ShowPublicIpType | Query the public IP type | To be tested |
|  | CountPublicIp | Query the number of public IP addresses. | To be tested |
|  | CountPublicIpInstance | Query the number of PublicIp instances. | To be tested |
| OpenStack-Floating IP address | NeutronUpdateFloatingIp | Update the floating IP address. | To be tested |
|  | NeutronShowFloatingIp | Query floating IP address details, including the floating IP address status, ID of the router to which the floating IP address belongs, and external network ID of the floating IP address. | To be tested |
|  | NeutronDeleteFloatingIp | Delete a specified floating IP address. | To be tested |
|  | NeutronListFloatingIps | Query all the floating IP addresses that the tenant who submits the request has the permission to perform operations on. | To be tested |
|  | NeutronCreateFloatingIp | UUID of the external network for creating a floating IP address. Obtain the UUID using GET /v2.0/networks?router:external=True or neutron net-external-list. | To be tested |
| Operate EIPs in batches | BatchDisassociatePublicips | Unbinding EIPs in Batches | To be tested |
|  | BatchDeletePublicIp | Deleting EIPs in Batches | To be tested |
|  | BatchCreatePublicips | Creating EIPs in Batches | To be tested |
| Public pool | ListPublicipPool | Query all public IP address pools | To be tested |
|  | ListCommonPools | Query the public pool list | To be tested |
|  | ShowPublicipPool | Query the details of a public IP address pool | To be tested |
| Query Job Status | ShowResourcesJobDetail | Interface for querying the job status | To be tested |
| Quota Management | ListQuotas | Obtain quota information | To be tested |
| Shared bandwidth type | ListShareBandwidthTypes | Query the list of shared bandwidth types of a specified tenant. | To be tested |
| virtual igw | ListTenantVpcIgws | Query the virtual IGW list of a specified tenant | To be tested |
|  | DeleteTenantVpcIgw | Delete a virtual IGW | To be tested |
|  | CreateTenantVpcIgw | Create a virtual IGW | To be tested |
|  | UpdateTenantVpcIgw | Modifying a virtual IGW | To be tested |
|  | ShowInternalVpcIgw | Query virtual IGW details | To be tested |

