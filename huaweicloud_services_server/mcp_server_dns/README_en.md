# DNS MCP Server 


## Version
v0.1.0

## Overview

DNS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DNS. Full-chain management of DNS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Access Endpoint Management | UpdateEndpoint | Update the access endpoint. | To be tested |
| Account management | ShowDomainQuota | This API is used to query the account quota. | To be tested |
| Batch Interface Management | BatchDeleteRecordSetWithLine | If the resource to be deleted does not exist, the resource is deleted successfully. | To be tested |
|  | BatchSetRecordSetsStatus | Set the status of the record sets in batches. | To be tested |
|  | CreateRecordSetWithBatchLines | Record set for batch line creation. This operation is atomic. If a parameter fails to be verified, the creation fails. This parameter is supported only by public network domain names. | To be tested |
|  | BatchDeleteZones | Delete domain names in batches. | To be tested |
|  | BatchDeletePtrRecords | Delete reverse lookups in batches. This interface is an atomic operation. All records must be deleted successfully or failed to be deleted. | To be tested |
|  | BatchSetZonesStatus | Set the domain name status in batches. | To be tested |
|  | BatchDeleteRecordSets | Delete record sets in batches. | To be tested |
|  | BatchUpdateRecordSetWithLine | Modify record sets in batches. This is an atomic operation, and the request recordset will be completely modified or not modified. | To be tested |
| Custom Line Management | ListCustomLine | Query the user-defined line. | To be tested |
|  | CreateCustomLine | Create a custom line. | To be tested |
|  | UpdateCustomLine | Update the customized line. | To be tested |
|  | DeleteCustomLine | Delete a user-defined line. | To be tested |
| DNSSEC | EnableDnssecConfig | Enable DNSSEC for the public zone. | To be tested |
|  | ShowDnssecConfig | Query the DNSSEC of a public zone. | To be tested |
|  | DisableDnssecConfig | Disable the DNSSEC for the public zone. | To be tested |
| Forwarding Rule Management | AssociateResolverRuleRouter | Associate the parser forwarding rule with the VPC. | To be tested |
|  | ListResolverRules | Query the forwarding rule list of the parser. | To be tested |
|  | DeleteResolverRule | Deletes a parser forwarding rule. | To be tested |
|  | ShowResolverRule | Query the forwarding rule of the parser. | To be tested |
|  | CreateResolverRule | Create a parser forwarding rule. | To be tested |
|  | UpdateResolverRule | Modifies the forwarding rule of the parser. | To be tested |
|  | DisassociateResolverRuleRouter | Disassociate the parser forwarding rule from the VPC. | To be tested |
| Image Tag | ListTags | Query the image tag list based on different conditions. | To be tested |
| Key Tag Management | DeleteTag | - Function description: This API is used to delete a key tag. | To be tested |
| Label | ListTag |  | To be tested |
| Line Group Management | ShowLineGroup | Query the line group. This interface is not available in some regions. To use this interface, submit a service ticket to enable it. | To be tested |
|  | UpdateLineGroups | Updates a line group. This interface is not available in some regions. To use this interface, submit a service ticket to enable it. | To be tested |
|  | DeleteLineGroup | Delete a line group. This interface is not available in some regions. To use this interface, submit a service ticket to enable it. | To be tested |
|  | CreateLineGroup | Create a line group. This interface is not available in some regions. To use this interface, submit a service ticket to enable it. | To be tested |
|  | ListLineGroups | Query the line group list. This interface is not available in some regions. To use this interface, submit a service ticket to enable it. | To be tested |
| Name Server Management | ListNameServers | Query the name server list | To be tested |
| Private domain name management | DeletePrivateZone | Delete a private zone. | To be tested |
|  | SetPrivateZoneProxyPattern | Set the recursive resolution proxy for the subdomain name of the private domain name. | To be tested |
|  | ShowPrivateZone | Query the private network domain name. | To be tested |
|  | ListPrivateZones | Query the private zone list. | To be tested |
|  | ShowPrivateZoneNameServer | Query the name server of the private zone. | To be tested |
|  | UpdatePrivateZoneStatus | Sets the status of the private zone domain name. The domain name can be suspended or enabled. | To be tested |
|  | AssociateRouter | Associate the private domain name with the VPC. | To be tested |
|  | CreatePrivateZone | Create a private zone. | To be tested |
|  | DisassociateRouter | Disassociate the VPC from the private domain name. | To be tested |
|  | UpdatePrivateZone | Change the private zone. | To be tested |
| Public Zone Management | ShowPublicZoneNameServer | Query the name server of a public domain name. | To be tested |
|  | UpdatePublicZoneStatus | Sets the status of a public zone. You can suspend or enable the domain name. | To be tested |
|  | ListPublicZones | Query the public zone list. | To be tested |
|  | CreatePublicZone | Create a public zone. | To be tested |
|  | UpdatePublicZone | Change the public zone. | To be tested |
|  | ShowPublicZone | Query the public zone. | To be tested |
|  | DeletePublicZone | Delete a public zone. | To be tested |
| Query API version information | ShowApiInfo | Query the API version of the Object Storage Migration Service. | To be tested |
| Query version operation | ListApiVersions | Query the TMS API version list. | To be tested |
| Recordset Management (New Version) | SetRecordSetsStatus | Sets the record set status. | To be tested |
|  | DeleteRecordSets | Delete a record set. | To be tested |
|  | ListRecordSetsWithLine | Query the tenant record set list. | To be tested |
|  | ShowRecordSetByZone | Query the record set list under a domain name. | To be tested |
|  | ShowRecordSetWithLine | Query a record set. | To be tested |
|  | UpdateRecordSets | Modifies a record set. | To be tested |
|  | ListPublicZoneLines | Query the line list of a public zone. | To be tested |
|  | CreateRecordSetWithLine | Create a record set. | To be tested |
| Recordset Management (to be discarded) | ListRecordSets | Query the tenant record set list. | To be tested |
|  | ShowRecordSet | Query a record set. | To be tested |
|  | DeleteRecordSet | Delete a record set. To delete a record set for which the intelligent resolution function is added, you need to use the interface for deleting the record set in the record set management module (new version) to delete the record set. | To be tested |
|  | UpdateRecordSet | Modifies a record set. | To be tested |
|  | ListRecordSetsByZone | Query the record set list under a domain name. | To be tested |
|  | CreateRecordSet | Create a record set. | To be tested |
| Resource Tag | ShowResourceTag | Query the tags of a single resource. | To be tested |
| Reverse lookup management (new version) | ListPtrs | Query the list of PTR records for EIPs. | To be tested |
|  | DeletePtr | Restore the PTR record of the EIP to the default value. | To be tested |
|  | UpdatePtr | Modifies the PTR record of an EIP. | To be tested |
|  | CreatePtr | Create a PRP lookup record for an EIP. | To be tested |
|  | ShowPtr | Query the reverse lookup records of an EIP. | To be tested |
| Reverse lookup management (to be discarded) | UpdatePtrRecord | Modify the PTR record of the EIP. | To be tested |
|  | ListPtrRecords | Query the list of PTR records for EIPs. | To be tested |
|  | RestorePtrRecord | Restore the PTR record of the EIP to the default value. | To be tested |
|  | ShowPtrRecordSet | Query the reverse lookup records of an EIP. | To be tested |
|  | CreateEipRecordSet | Set the reverse lookup record for the EIP. | To be tested |
| Tag Management | CreateTag | Add a tag to a resource. | To be tested |
|  | BatchCreateTag | Add or delete tags for specified instances in batches | To be tested |
| VPC Endpoint Function | DeleteEndpoint | Delete the VPC endpoint. | To be tested |
|  | CreateEndpoint | Create a VPC endpoint so that it can access the VPC endpoint service. | To be tested |
|  | ListEndpoints | Query the list of VPC endpoints of the current user. | To be tested |
| VPC Endpoint Management | DisassociateEndpointIpaddress | Unbind the IP address from the VPC endpoint. | To be tested |
|  | ShowEndpoint | Query the VPC endpoint. | To be tested |
|  | ListEndpointVpcs | Query the VPC list of VPC endpoints. | To be tested |
|  | AssociateEndpointIpaddress | Bound IP address to the VPC endpoint. | To be tested |
|  | ListEndpointIpaddresses | Query the IP address list under a VPC endpoint. | To be tested |

