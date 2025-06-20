# AAD MCP Server 


## Version
v0.1.0

## Overview

AAD MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service AAD. Full-chain management of AAD resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AAD - Overview | ListPeak | Query the peak traffic and attack count | To be tested |
|  | ListDDoSAttackEvent | Query the DDoS attack event list | To be tested |
|  | ListWafAttackEvent | Query the attack event list | To be tested |
|  | ListDDoSFlow | Query the BPS/PPS traffic of DDoS attack defense | To be tested |
|  | ShowWafQps | Query QPS for CC attack defense | To be tested |
|  | ListWafBandwidth | Bandwidth curve | To be tested |
|  | ListWafQps | Query request QPS | To be tested |
|  | ListDDoSConnectionNumber | Query the number of new connections and the number of concurrent connections | To be tested |
| AAD-Domain name management | ModifyDomainWebSwitch | Modifying the basic web/CC protection switch for a domain name | To be tested |
|  | ListDomain | Query the domain name list | To be tested |
|  | ShowDomainCertificate | Query the certificate information associated with a domain name | To be tested |
|  | ListInstanceId | Query the ID of the instance associated with a domain name | To be tested |
|  | SetCertForDomain | Uploading or Modifying the Certificate Corresponding to a Domain Name | To be tested |
|  | CreateAadDomain | Create a domain name. | To be tested |
|  | UpdateDomain | Update domain name origin server configuration information | To be tested |
|  | ListSourceIps | Query the retrieval IP address segment list of Advanced Anti-DDoS | To be tested |
| AAD-Forwarding Rule Management | BatchDeleteInstanceIpRule | Delete forwarding rules for IP addresses of AAD instances in batches | To be tested |
|  | BatchCreateInstanceIpRule | Adding Forwarding Rules for IP Addresses of Advanced Anti-DDoS Instances in Batches | To be tested |
|  | UpdateInstanceIpRule | Modifying the origin server IP address in the forwarding configuration of the AAD instance | To be tested |
|  | ListInstanceIpRule | Query the forwarding rule list of the IP address of the AAD instance | To be tested |
| AAD-Instance List | ListInstanceDomains | Query the domain name associated with an instance. | To be tested |
|  | UpgradeInstanceSpec | Modifying an instance specification | To be tested |
| AAD-Protection Policy | AddBlackWhiteIpList | Adding an AAD instance to the blocklist and whitelist | To be tested |
|  | ListFrequencyControlRule | Query the frequency control rule list | To be tested |
|  | DeleteWafWhiteIpRule | Protection policy web-cc blocklist and trustlit-deleting a blocklist and trustlist rule | To be tested |
|  | ShowWafPolicy | Query the web protection policy configuration | To be tested |
|  | ShowFlowBlock | Query the traffic blocking information | To be tested |
|  | ListWhiteBlackIpRule | Query the trustlist and trustlist of DDoS attack defense | To be tested |
|  | AddWafWhiteIpRule | Protection policy web-cc blocklist and trustlit-creating a blocklist and trustlist rule | To be tested |
|  | DeleteBlackWhiteIpList | Delete AAD instances from the blocklist and trustlist. | To be tested |
|  | ListWafGeoIpRule | Query area barring rules | To be tested |
|  | ListWafCustomRule | Query precise protection rules | To be tested |
|  | ListWafWhiteIpRule | Protection policy web-cc blocklist and trustlit-query blocklist and trustlist rules | To be tested |
| Alarm Configuration Management | UpdateAlarmConfig | Modifying the alarm configuration interface | To be tested |
|  | ShowAlarmConfig | Obtain alarm configuration information | To be tested |
| Domain | CreateDomain | Create a domain name. | To be tested |
|  | DeleteDomain | Delete a domain name. | To be tested |
| Exclusive Instance Management | ListInstance | Query the exclusive WAF engine list. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
| Native Advanced Anti-DDoS - Policy Management | DisassociateIpFromPolicyAndPackage | Unbind a policy from an instance to a Zone | To be tested |
|  | AssociateIpToPolicyAndPackage | Binding a policy to an instance to a Zone | To be tested |
|  | AssociateIpToPolicy | Bind the policy to the Zone | To be tested |
|  | AddPolicyBlackAndWhiteIpList | Adding a policy to the blocklist or whitelist | To be tested |
|  | DeletePolicyBlackAndWhiteIpList | Delete a policy from the blocklist or whitelist | To be tested |
|  | DisassociateIpFromPolicy | Unbind a policy from a Zone | To be tested |
| Native Advanced Anti-DDoS - Zone Management | ListProtectedIp | Querying the Zone List | To be tested |
|  | UpdateTagForProtectedIp | Setting Tags for Zones | To be tested |
| Native Advanced Anti-DDoS-Alarm Configuration Management | DeleteAlarmConfig | Delete alarm configuration | To be tested |
| Native Advanced Anti-DDoS-Instance Management | UpdatePackageName | Update the instance name | To be tested |
|  | ListUnboundProtectedIp | Query the list of Zones that can be bound | To be tested |
|  | ListPackage | Query the DB instance list | To be tested |
|  | UpdatePackageIp | Updates all Zones bound to an instance | To be tested |
| Protection Policy Management | DeletePolicy | To delete a protection policy, if the policy is in use, you need to unbind the domain name from the policy before deleting the policy. | To be tested |
|  | ShowPolicy | Query protection policies by ID | To be tested |
|  | ListPolicy | Query the protection policy list | To be tested |
|  | UpdatePolicy | Update the protection policy. The request body can contain only the part to be updated. | To be tested |
|  | CreatePolicy | When creating a protection policy, the system configures some default configuration items when generating the policy. To modify the default configuration items, call the interface for updating the protection policy. | To be tested |
| Unblocking Center-Unblocking Management | ShowBlockStatistics | Query the blocking statistics. | To be tested |
|  | ListBlockIps | Query the blocked tenant list | To be tested |
|  | ListUnblockQuotaStatistics | Query the unblocking quota | To be tested |
|  | ShowUnblockRecord | Query the unpacking records of a tenant. | To be tested |
|  | ExecuteUnblockIp | Unblocking the IP address | To be tested |

