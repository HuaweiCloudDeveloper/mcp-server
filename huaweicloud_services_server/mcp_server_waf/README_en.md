# WAF MCP Server 


## Version
v0.1.0

## Overview

WAF MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service WAF. Full-chain management of WAF resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Address Group Management | ShowIpGroup | Query IP address group details | To be tested |
|  | CreateIpGroup | Create an IP address group | To be tested |
|  | ListIpGroup | Query the address group list | To be tested |
|  | UpdateIpGroup | Modifying an IP address group | To be tested |
|  | DeleteIpGroup | Delete an IP address group | To be tested |
| Alarm management | ListNoticeConfigs | Query the alarm notification configuration. | To be tested |
|  | UpdateAlertNoticeConfig | Update alarm notification configuration | To be tested |
| Certificate Management | UpdateCertificate | Modifying a Certificate | To be tested |
|  | ApplyCertificateToHost | Bind the certificate to the domain name | To be tested |
|  | DeleteCertificate | Delete a certificate | To be tested |
|  | ShowCertificate | Querying a certificate | To be tested |
|  | CreateCertificate | Create Certificate | To be tested |
|  | ListCertificates | Query the certificate list | To be tested |
| Exclusive Instance Management | RenameInstance | Rename the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
|  | CreateInstance | Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore | To be tested |
|  | ListInstance | Query the exclusive WAF engine list. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
|  | ShowInstance | Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
|  | DeleteInstance | Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
| Log Configuration Management | UpdateLtsInfoConfig | Configure full log lts. This interface is used to enable or disable full WAF logs and configure log groups and log streams. You can obtain the log group ID and log stream ID from LTS. The configured log stream ID must belong to the configured log group. | To be tested |
|  | ShowLtsInfoConfig | Query the lts configuration information | To be tested |
| Policy Rule Management | ListCcRules | Query the CC rule list | To be tested |
|  | DeleteCustomRule | Delete a precise protection rule. | To be tested |
|  | DeleteAntitamperRule | Delete an anti-tamper protection rule | To be tested |
|  | ShowCustomRule | Query precise protection rules by ID. | To be tested |
|  | ShowAntileakageRule | Query the anti-sensitive information leakage protection rule by ID | To be tested |
|  | ListAntileakageRules | Query the list of sensitive information leakage prevention rules | To be tested |
|  | ShowCcRule | Query CC protection rules by ID | To be tested |
|  | UpdateGeoipRule | Updating a geographical location control protection rule | To be tested |
|  | CreateValueList | Create a reference table that can be referenced by CC attack defense rules and precise access protection rules. | To be tested |
|  | ListPrivacyRule | Query the privacy masking rule list | To be tested |
|  | UpdateAnticrawlerRuleType | Updates the anti-crawler rule protection mode for JS scripts. Before creating a JS script anti-crawler rule, you need to invoke this interface to specify the anti-crawler rule protection mode for JS scripts. | To be tested |
|  | DeletePrivacyRule | Delete a privacy masking rule. | To be tested |
|  | UpdatePunishmentRule | Updating an attack penalty rule | To be tested |
|  | UpdateWhiteblackipRule | Updates the blocklist and trustlist protection rule, including the IP address, IP address segment, and protection action. | To be tested |
|  | CreateWhiteblackipRule | Create a blocklist and trustlist rule | To be tested |
|  | DeleteValueList | Delete a reference table | To be tested |
|  | CreatePunishmentRule | Create an attack penalty rule | To be tested |
|  | UpdateIgnoreRule | Update the global trustlist (original false positive masking) protection rule | To be tested |
|  | DeleteCcRule | Delete a CC protection rule. | To be tested |
|  | UpdateAntileakageRule | Update the sensitive information leakage prevention rule | To be tested |
|  | DeleteIgnoreRule | Delete a global trustlist (original false positive shielding) protection rule. | To be tested |
|  | CreateAntileakageRule | Create a sensitive information leakage prevention rule | To be tested |
|  | ListWhiteblackipRule | Query the blocklist and trustlist rule list | To be tested |
|  | ShowPrivacyRule | Query a privacy masking rule | To be tested |
|  | ListCustomRules | Query the precise protection rule list | To be tested |
|  | ShowWhiteBlackIpRule | Query the blocklist and trustlist protection rule | To be tested |
|  | UpdatePolicyRuleStatus | Modifies the status of a single rule, for example, disabling a rule in precise protection. | To be tested |
|  | UpdateAnticrawlerRule | Updating the anti-crawler protection rule of the JS script | To be tested |
|  | UpdateAntiTamperRuleRefresh | WTP rule update cache | To be tested |
|  | ShowPunishmentRule | Query attack penalty protection rules by ID | To be tested |
|  | UpdateCustomRule | Update precise protection rules | To be tested |
|  | CreateGeoipRule | Create a geographical location control rule | To be tested |
|  | UpdateCcRule | Update CC protection rules | To be tested |
|  | CreateAnticrawlerRule | Before calling this API to create a JS script anti-crawler rule, you need to invoke the UpdateAnticrawlerRuleType API to specify the anti-crawler rule protection mode. | To be tested |
|  | DeleteGeoipRule | Delete a geographical location control protection rule. | To be tested |
|  | CreateAntiTamperRule | Create an anti-tamper rule | To be tested |
|  | ShowGeoipRule | Delete a geographical location control protection rule. | To be tested |
|  | DeleteAnticrawlerRule | Delete a JS script anti-crawler protection rule | To be tested |
|  | CreateIgnoreRule | Create a global trustlist (original false positive masking) rule | To be tested |
|  | ListIgnoreRule | Query the global trustlist rule list | To be tested |
|  | ListGeoipRule | Query the geolocation access control rule list | To be tested |
|  | DeleteWhiteBlackIpRule | Delete a blocklist and trustlist protection rule | To be tested |
|  | ShowValueList | Query the reference table | To be tested |
|  | DeletePunishmentRule | Delete an attack penalty rule. | To be tested |
|  | ShowAntitamperRule | Query anti-tamper protection rules | To be tested |
|  | DeleteAntileakageRule | Delete a sensitive information leakage prevention rule. | To be tested |
|  | ListPunishmentRules | Query the attack penalty rule list | To be tested |
|  | UpdatePrivacyRule | Update a privacy masking rule | To be tested |
|  | CreatePrivacyRule | Create a privacy masking rule. | To be tested |
|  | ShowAnticrawlerRule | Query the anti-crawler protection rule of the JS script by ID | To be tested |
|  | ListValueList | Query the reference table list | To be tested |
|  | ShowIgnoreRule | Query the global trustlist (original false positive shielding) protection rule | To be tested |
|  | UpdateValueList | Modifying a reference table | To be tested |
|  | ListAnticrawlerRules | Query the anti-crawler rule list of a JS script | To be tested |
|  | CreateCustomRule | Creating a Precise Protection Rule | To be tested |
|  | CreateCcRule | Create a CC rule | To be tested |
|  | ListAntitamperRule | Query the anti-tamper rule list | To be tested |
| Protection Event Management | ListEvent | Query the attack event list. Currently, this API does not support query of all defense events. The pagesize parameter cannot be set to - 1. Due to performance reasons, a larger data volume consumes more memory. A maximum of 10000 data records can be queried. For example: If the number of data records in the customized period exceeds 10000, the data records whose page is 101 and pagesize is 100 cannot be queried. You need to adjust the time period and then query the data. | To be tested |
|  | ShowEvent | Query the details of a protection event with a specified ID. | To be tested |
| Protection Policy Management | DeletePolicy | To delete a protection policy, if the policy is in use, you need to unbind the domain name from the policy before deleting the policy. | To be tested |
|  | UpdatePolicyProtectHost | Update the domain name of the protection policy | To be tested |
|  | ListPolicy | Query the protection policy list | To be tested |
|  | ShowPolicy | Query protection policies by ID | To be tested |
|  | CreatePolicy | When creating a protection policy, the system configures some default configuration items when generating the policy. To modify the default configuration items, call the interface for updating the protection policy. | To be tested |
|  | UpdatePolicy | Update the protection policy. The request body can contain only the part to be updated. | To be tested |
| Protection Website Management in Cloud Mode | ListHost | Query the domain name list in cloud mode | To be tested |
|  | ShowHost | Query details about a cloud-based domain name based on the domain name ID. | To be tested |
|  | UpdateHostProtectStatus | Modifying the domain name protection status | To be tested |
|  | UpdateHost | Update the domain name configuration in cloud mode. If the original data of the origin server is not entered, the new origin server will overwrite the origin server information instead of adding a new origin server. In addition, the request body can pass only the part that needs to be updated. | To be tested |
|  | ListHostRoute | Return routing information | To be tested |
|  | CreateHost | Creating a domain name in cloud mode | To be tested |
|  | DeleteHost | Delete the domain name in cloud mode. | To be tested |
| Protection website management in exclusive mode | DeletePremiumHost | Delete the domain name in exclusive mode. | To be tested |
|  | ListPremiumHost | Domain name list in exclusive mode | To be tested |
|  | UpdatePremiumHostProtectStatus | Modifies the domain name protection status in exclusive mode. | To be tested |
|  | ShowPremiumHost | View the domain name configuration in exclusive mode | To be tested |
|  | CreatePremiumHost | Create a domain name in exclusive mode. | To be tested |
|  | UpdatePremiumHost | Modify the domain name configuration in exclusive mode. If the original data of the origin server information is not entered, the new origin server information will overwrite the origin server information instead of adding a new origin server. In addition, the request body can pass only the part that needs to be updated. | To be tested |
| Query features supported by the site | ShowConsoleConfig | Querying features supported by the site | To be tested |
| Security Overview | ListRequestTimeline | Query the timeline statistics of the number of requests on the Security Overview page. | To be tested |
|  | ListQpsTimeline | Query the number of times the security statistics are qps. | To be tested |
|  | ListTopAbnormal | Query the top service abnormality statistics. | To be tested |
|  | ListBandwidthTimeline | Query the security bandwidth statistics. The statistics are the average bandwidth, in bit/s. | To be tested |
|  | ListStatistics | Query the number of security overview requests and attacks. | To be tested |
|  | ListOverviewsClassification | Query top security overview category statistics, including the attacked domain name, attack source IP address, attacked URL, attack source area, and attack event distribution. | To be tested |
| System Management | ShowSourceIp | Query the WAF retrieval IP address. | To be tested |
| Tenant Domain Name Query | ListCompositeHosts | Query the list of all protected domain names, including the cloud mode and exclusive mode. | To be tested |
|  | ShowCompositeHost | Query the domain name by ID. | To be tested |
| Tenant Protection Domain Name Management | MigrateCompositeHosts | Migrate domain names by enterprise project. This function is supported only by the professional and exclusive editions. | To be tested |
| Tenant subscription management | CreatePrepaidCloudWaf | Subscribe to the cloud WAF service in yearly/monthly mode. | To be tested |
|  | ShowSubscriptionInfo | Query the tenant subscription information, including the cloud mode, yearly/monthly, pay-per-use, and exclusive mode. | To be tested |
|  | ChangePrepaidCloudWaf | Change the WAF specification in the yearly/monthly cloud mode. Note: | To be tested |

