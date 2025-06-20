# CFW MCP Server 


## Version
v0.1.0

## Overview

CFW MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CFW. Full-chain management of CFW resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| ACL Rule Management | UpdateAclRuleOrder | Setting the priority of an ACL protection rule | To be tested |
|  | ListAclRuleHitCount | Obtains the number of times a rule is hit. | To be tested |
|  | ListRuleAclTags | Query Rule Tag | To be tested |
|  | BatchDeleteAclRules | Delete ACL rules in batches | To be tested |
|  | UpdateAclRule | Updating an ACL rule | To be tested |
|  | ListAclRules | Querying a protection rule | To be tested |
|  | DeleteAclRuleHitCount | Number of times a rule is cleared | To be tested |
|  | ShowImportStatus | Interface for viewing the import status | To be tested |
|  | BatchUpdateAclRuleActions | Batch rule update action | To be tested |
|  | DeleteAclRule | Delete an ACL rule group | To be tested |
|  | AddAclRule | Create an ACL rule | To be tested |
| Address Group Management | AddAddressSet | Adding an Address Group | To be tested |
|  | UpdateAddressSet | Update address group information | To be tested |
|  | DeleteAddressSet | Delete an address group | To be tested |
|  | ListAddressItems | Querying the members of an address group | To be tested |
|  | DeleteAddressItem | Delete an address group member | To be tested |
|  | AddAddressItem | Adding an address group member | To be tested |
|  | UpdateObjectConfigDesc | Editing the description of a member in an object group | To be tested |
|  | ListAddressSets | Query the address group list | To be tested |
|  | ListAddressSetDetail | Query the details of an address group | To be tested |
|  | BatchDeleteAddressItems | Delete address group members in batches | To be tested |
| Alarm Configuration Management | UpdateAlarmConfig | Modifying the alarm configuration interface | To be tested |
|  | ShowAlarmConfig | Obtain alarm configuration information | To be tested |
| Antivirus management | ShowAntiVirusRule | Obtain the antivirus rule information of the firewall | To be tested |
|  | UpdateAntiVirusSwitch | Modifying the antivirus function | To be tested |
|  | UpdateAntiVirusRule | Modifying an antivirus rule | To be tested |
|  | ShowAntiVirusSwitch | View the antivirus function. | To be tested |
| Black and Trust List Management | DeleteBlackWhiteList | Delete a blocklist or trustlist rule. | To be tested |
|  | UpdateBlackWhiteList | Update the blocklist and whitelist | To be tested |
|  | ListBlackWhiteLists | Query the blocklist and whitelist | To be tested |
|  | AddBlackWhiteList | Create a blocklist and trustlist rule | To be tested |
| Domain name resolution and domain name group management | ShowDomainSetDetail | View domain group details | To be tested |
|  | UpdateDnsServers | Update the DNS server list | To be tested |
|  | BatchDeleteDomainSet | Delete domain groups in batches | To be tested |
|  | ListDomainSets | Query the domain group list | To be tested |
|  | AddDomains | Add domain name list | To be tested |
|  | AddDomainSet | Add domain group | To be tested |
|  | UpdateDomainSet | Update domain group | To be tested |
|  | ListDnsServers | Query the list of DNS servers | To be tested |
|  | ListDomainParseDetail | Test the validity of the domain name | To be tested |
|  | ListDomainParseIp | Obtain the domain name address resolution result | To be tested |
|  | DeleteDomainSet | Delete a domain group | To be tested |
| EIP Management | ChangeEipStatus | Enable or disable EIP. Before enabling EIP protection for the first time after purchasing an EIP, you need to use ListEips to synchronize EIP assets and set sync to 1. | To be tested |
|  | ListEipCount | Query the number of EIPs. | To be tested |
|  | ListEips | Querying the EIP list | To be tested |
|  | ShowAutoProtectStatus | Obtain the EIP automatic protection status information | To be tested |
|  | SwitchAutoProtectStatus | Modifying the EIP automatic protection function | To be tested |
|  | ListAlarmWhitelist | View the EIP alarm trustlist. | To be tested |
| FDR | ListFlowLogs | Query the list of all FDRs of the tenant that submits the request and filter the FDRs based on the filter criteria. | To be tested |
| Firewall management | ListJob | Obtain the execution status of the CFW task. | To be tested |
|  | CreateEastWestFirewall | Create an east-west firewall | To be tested |
|  | ListFirewallList | Query the firewall list | To be tested |
|  | ListProtectedVpcs | Query the protected VPC information | To be tested |
|  | ChangeEastWestFirewallStatus | Enabling or disabling east-west protection | To be tested |
|  | ListEastWestFirewall | Obtain the east-west firewall information. | To be tested |
|  | ListFirewallDetail | Querying a firewall instance | To be tested |
| IPS Management | ListIpsSwitchStatus | Query the status of the IPS feature switch. | To be tested |
|  | ListIpsProtectMode | Query the protection mode. | To be tested |
|  | ListIpsRules | Querying the frequency IPS rule information | To be tested |
|  | ChangeIpsProtectMode | Switch the protection mode | To be tested |
|  | ShowIpsUpdateTime | Obtain the IPS rule details | To be tested |
|  | ChangeIpsRuleMode | Change the IPS rule mode. | To be tested |
|  | ChangeIpsSwitchStatus | Switch status | To be tested |
|  | ListCustomerIps | Obtain the user-defined IPS rule. | To be tested |
|  | UpdateAdvancedIpsRule | Create a frequency IPS rule | To be tested |
|  | ListIpsRules1 | Obtains the IPS rule list. | To be tested |
| Key Tag Management | DeleteTag | - Function description: This API is used to delete a key tag. | To be tested |
| Log management | ListLogConfig | Obtain log configuration | To be tested |
|  | UpdateLogConfig | Update log configuration | To be tested |
|  | AddLogConfig | Create log configuration | To be tested |
|  | ListAttackLogs | Query attack logs | To be tested |
|  | ListAccessControlLogs | Query access control logs | To be tested |
| Network ACL | CreateFirewall | Create a network ACL | To be tested |
|  | DeleteFirewall | Delete a network ACL | To be tested |
| Packet capture management | CancelCaptureTask | Cancel the packet capture task | To be tested |
|  | ListCaptureTask | Querying a packet capture task | To be tested |
|  | CreateCaptureTask | Create a packet capture task. Each task can be executed only once. | To be tested |
|  | ListCaptureResult | Obtain the packet capture result | To be tested |
|  | DeleteCaptureTask | Delete packet capture tasks in batches | To be tested |
| Region | ListRegions | Query the area visible to the user | To be tested |
| Service group management | DeleteServiceSet | Delete a service group | To be tested |
|  | AddServiceSet | Create a service group | To be tested |
|  | ListServiceItems | Query the service group member list | To be tested |
|  | UpdateServiceSet | Update a service group | To be tested |
|  | ListServiceSets | Obtain the service group list | To be tested |
|  | AddServiceItems | Adding Service Group Members in Batches | To be tested |
|  | BatchDeleteServiceItems | Delete service group members in batches | To be tested |
|  | DeleteServiceItem | Delete a service group member | To be tested |
|  | ListServiceSetDetail | Query service group details | To be tested |
| Tag Management | CreateTag | Add a tag to a resource. | To be tested |
|  | SaveTags | API for saving resource tags | To be tested |
| Tags | ListProjectTags | Query all tags of a specified resource type in a specified project | To be tested |
| Use TMS | ListResourceTags | Query the label information of a specified DB instance. | To be tested |
| websites | DeleteDomains | Delete the website assets of the tenant | To be tested |
|  | ListDomains | Obtain all website assets of a tenant | To be tested |

