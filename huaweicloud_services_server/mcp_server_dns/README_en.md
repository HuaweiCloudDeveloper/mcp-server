# DNS MCP Server 


## Version
v0.1.0

## Overview

DNS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DNS. Full-chain management of DNS resources can be carried out based on natural language.

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
                    <td rowspan="1">Access Endpoint Management</td>
                    <td>UpdateEndpoint</td>
                    <td>Update the access endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Account management</td>
                    <td>ShowDomainQuota</td>
                    <td>This API is used to query the account quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Batch Interface Management</td>
                    <td>BatchDeleteRecordSetWithLine</td>
                    <td>If the resource to be deleted does not exist, the resource is deleted successfully.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetRecordSetsStatus</td>
                    <td>Set the status of the record sets in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRecordSetWithBatchLines</td>
                    <td>Record set for batch line creation. This operation is atomic. If a parameter fails to be verified, the creation fails. This parameter is supported only by public network domain names.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteZones</td>
                    <td>Delete domain names in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePtrRecords</td>
                    <td>Delete reverse lookups in batches. This interface is an atomic operation. All records must be deleted successfully or failed to be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetZonesStatus</td>
                    <td>Set the domain name status in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteRecordSets</td>
                    <td>Delete record sets in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateRecordSetWithLine</td>
                    <td>Modify record sets in batches. This is an atomic operation, and the request recordset will be completely modified or not modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Custom Line Management</td>
                    <td>ListCustomLine</td>
                    <td>Query the user-defined line.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCustomLine</td>
                    <td>Create a custom line.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCustomLine</td>
                    <td>Update the customized line.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomLine</td>
                    <td>Delete a user-defined line.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">DNSSEC</td>
                    <td>EnableDnssecConfig</td>
                    <td>Enable DNSSEC for the public zone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDnssecConfig</td>
                    <td>Query the DNSSEC of a public zone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableDnssecConfig</td>
                    <td>Disable the DNSSEC for the public zone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Forwarding Rule Management</td>
                    <td>AssociateResolverRuleRouter</td>
                    <td>Associate the parser forwarding rule with the VPC.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResolverRules</td>
                    <td>Query the forwarding rule list of the parser.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResolverRule</td>
                    <td>Deletes a parser forwarding rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResolverRule</td>
                    <td>Query the forwarding rule of the parser.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResolverRule</td>
                    <td>Create a parser forwarding rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResolverRule</td>
                    <td>Modifies the forwarding rule of the parser.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateResolverRuleRouter</td>
                    <td>Disassociate the parser forwarding rule from the VPC.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Image Tag</td>
                    <td>ListTags</td>
                    <td>Query the image tag list based on different conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Key Tag Management</td>
                    <td>DeleteTag</td>
                    <td>- Function description: This API is used to delete a key tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Label</td>
                    <td>ListTag</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Line Group Management</td>
                    <td>ShowLineGroup</td>
                    <td>Query the line group. This interface is not available in some regions. To use this interface, submit a service ticket to enable it.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLineGroups</td>
                    <td>Updates a line group. This interface is not available in some regions. To use this interface, submit a service ticket to enable it.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLineGroup</td>
                    <td>Delete a line group. This interface is not available in some regions. To use this interface, submit a service ticket to enable it.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLineGroup</td>
                    <td>Create a line group. This interface is not available in some regions. To use this interface, submit a service ticket to enable it.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLineGroups</td>
                    <td>Query the line group list. This interface is not available in some regions. To use this interface, submit a service ticket to enable it.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Name Server Management</td>
                    <td>ListNameServers</td>
                    <td>Query the name server list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Private domain name management</td>
                    <td>DeletePrivateZone</td>
                    <td>Delete a private zone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetPrivateZoneProxyPattern</td>
                    <td>Set the recursive resolution proxy for the subdomain name of the private domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateZone</td>
                    <td>Query the private network domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateZones</td>
                    <td>Query the private zone list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateZoneNameServer</td>
                    <td>Query the name server of the private zone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrivateZoneStatus</td>
                    <td>Sets the status of the private zone domain name. The domain name can be suspended or enabled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRouter</td>
                    <td>Associate the private domain name with the VPC.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePrivateZone</td>
                    <td>Create a private zone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateRouter</td>
                    <td>Disassociate the VPC from the private domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrivateZone</td>
                    <td>Change the private zone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Public Zone Management</td>
                    <td>ShowPublicZoneNameServer</td>
                    <td>Query the name server of a public domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublicZoneStatus</td>
                    <td>Sets the status of a public zone. You can suspend or enable the domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublicZones</td>
                    <td>Query the public zone list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePublicZone</td>
                    <td>Create a public zone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublicZone</td>
                    <td>Change the public zone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPublicZone</td>
                    <td>Query the public zone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePublicZone</td>
                    <td>Delete a public zone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query API version information</td>
                    <td>ShowApiInfo</td>
                    <td>Query the API version of the Object Storage Migration Service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query version operation</td>
                    <td>ListApiVersions</td>
                    <td>Query the TMS API version list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Recordset Management (New Version)</td>
                    <td>SetRecordSetsStatus</td>
                    <td>Sets the record set status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRecordSets</td>
                    <td>Delete a record set.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecordSetsWithLine</td>
                    <td>Query the tenant record set list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordSetByZone</td>
                    <td>Query the record set list under a domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordSetWithLine</td>
                    <td>Query a record set.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRecordSets</td>
                    <td>Modifies a record set.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublicZoneLines</td>
                    <td>Query the line list of a public zone.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRecordSetWithLine</td>
                    <td>Create a record set.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Recordset Management (to be discarded)</td>
                    <td>ListRecordSets</td>
                    <td>Query the tenant record set list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordSet</td>
                    <td>Query a record set.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRecordSet</td>
                    <td>Delete a record set. To delete a record set for which the intelligent resolution function is added, you need to use the interface for deleting the record set in the record set management module (new version) to delete the record set.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRecordSet</td>
                    <td>Modifies a record set.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecordSetsByZone</td>
                    <td>Query the record set list under a domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRecordSet</td>
                    <td>Create a record set.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Resource Tag</td>
                    <td>ShowResourceTag</td>
                    <td>Query the tags of a single resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Reverse lookup management (new version)</td>
                    <td>ListPtrs</td>
                    <td>Query the list of PTR records for EIPs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePtr</td>
                    <td>Restore the PTR record of the EIP to the default value.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePtr</td>
                    <td>Modifies the PTR record of an EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePtr</td>
                    <td>Create a PRP lookup record for an EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPtr</td>
                    <td>Query the reverse lookup records of an EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Reverse lookup management (to be discarded)</td>
                    <td>UpdatePtrRecord</td>
                    <td>Modify the PTR record of the EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPtrRecords</td>
                    <td>Query the list of PTR records for EIPs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestorePtrRecord</td>
                    <td>Restore the PTR record of the EIP to the default value.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPtrRecordSet</td>
                    <td>Query the reverse lookup records of an EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEipRecordSet</td>
                    <td>Set the reverse lookup record for the EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tag Management</td>
                    <td>CreateTag</td>
                    <td>Add a tag to a resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateTag</td>
                    <td>Add or delete tags for specified instances in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">VPC Endpoint Function</td>
                    <td>DeleteEndpoint</td>
                    <td>Delete the VPC endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEndpoint</td>
                    <td>Create a VPC endpoint so that it can access the VPC endpoint service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpoints</td>
                    <td>Query the list of VPC endpoints of the current user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">VPC Endpoint Management</td>
                    <td>DisassociateEndpointIpaddress</td>
                    <td>Unbind the IP address from the VPC endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEndpoint</td>
                    <td>Query the VPC endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpointVpcs</td>
                    <td>Query the VPC list of VPC endpoints.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateEndpointIpaddress</td>
                    <td>Bound IP address to the VPC endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpointIpaddresses</td>
                    <td>Query the IP address list under a VPC endpoint.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
