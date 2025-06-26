# WAF MCP Server 


## Version
v0.1.0

## Overview

WAF MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service WAF. Full-chain management of WAF resources can be carried out based on natural language.

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
                    <td rowspan="5">Address Group Management</td>
                    <td>ShowIpGroup</td>
                    <td>Query IP address group details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIpGroup</td>
                    <td>Create an IP address group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIpGroup</td>
                    <td>Query the address group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIpGroup</td>
                    <td>Modifying an IP address group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIpGroup</td>
                    <td>Delete an IP address group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Alarm management</td>
                    <td>ListNoticeConfigs</td>
                    <td>Query the alarm notification configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlertNoticeConfig</td>
                    <td>Update alarm notification configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Certificate Management</td>
                    <td>UpdateCertificate</td>
                    <td>Modifying a Certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplyCertificateToHost</td>
                    <td>Bind the certificate to the domain name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCertificate</td>
                    <td>Delete a certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificate</td>
                    <td>Querying a certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificate</td>
                    <td>Create Certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificates</td>
                    <td>Query the certificate list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Exclusive Instance Management</td>
                    <td>RenameInstance</td>
                    <td>Rename the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstance</td>
                    <td>Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstance</td>
                    <td>Query the exclusive WAF engine list. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Log Configuration Management</td>
                    <td>UpdateLtsInfoConfig</td>
                    <td>Configure full log lts. This interface is used to enable or disable full WAF logs and configure log groups and log streams. You can obtain the log group ID and log stream ID from LTS. The configured log stream ID must belong to the configured log group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLtsInfoConfig</td>
                    <td>Query the lts configuration information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="57">Policy Rule Management</td>
                    <td>ListCcRules</td>
                    <td>Query the CC rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomRule</td>
                    <td>Delete a precise protection rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAntitamperRule</td>
                    <td>Delete an anti-tamper protection rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCustomRule</td>
                    <td>Query precise protection rules by ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAntileakageRule</td>
                    <td>Query the anti-sensitive information leakage protection rule by ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAntileakageRules</td>
                    <td>Query the list of sensitive information leakage prevention rules</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCcRule</td>
                    <td>Query CC protection rules by ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGeoipRule</td>
                    <td>Updating a geographical location control protection rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateValueList</td>
                    <td>Create a reference table that can be referenced by CC attack defense rules and precise access protection rules.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivacyRule</td>
                    <td>Query the privacy masking rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAnticrawlerRuleType</td>
                    <td>Updates the anti-crawler rule protection mode for JS scripts. Before creating a JS script anti-crawler rule, you need to invoke this interface to specify the anti-crawler rule protection mode for JS scripts.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePrivacyRule</td>
                    <td>Delete a privacy masking rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePunishmentRule</td>
                    <td>Updating an attack penalty rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWhiteblackipRule</td>
                    <td>Updates the blocklist and trustlist protection rule, including the IP address, IP address segment, and protection action.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWhiteblackipRule</td>
                    <td>Create a blocklist and trustlist rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteValueList</td>
                    <td>Delete a reference table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePunishmentRule</td>
                    <td>Create an attack penalty rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIgnoreRule</td>
                    <td>Update the global trustlist (original false positive masking) protection rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCcRule</td>
                    <td>Delete a CC protection rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAntileakageRule</td>
                    <td>Update the sensitive information leakage prevention rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIgnoreRule</td>
                    <td>Delete a global trustlist (original false positive shielding) protection rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAntileakageRule</td>
                    <td>Create a sensitive information leakage prevention rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWhiteblackipRule</td>
                    <td>Query the blocklist and trustlist rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivacyRule</td>
                    <td>Query a privacy masking rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCustomRules</td>
                    <td>Query the precise protection rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWhiteBlackIpRule</td>
                    <td>Query the blocklist and trustlist protection rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicyRuleStatus</td>
                    <td>Modifies the status of a single rule, for example, disabling a rule in precise protection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAnticrawlerRule</td>
                    <td>Updating the anti-crawler protection rule of the JS script</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAntiTamperRuleRefresh</td>
                    <td>WTP rule update cache</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPunishmentRule</td>
                    <td>Query attack penalty protection rules by ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCustomRule</td>
                    <td>Update precise protection rules</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGeoipRule</td>
                    <td>Create a geographical location control rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCcRule</td>
                    <td>Update CC protection rules</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAnticrawlerRule</td>
                    <td>Before calling this API to create a JS script anti-crawler rule, you need to invoke the UpdateAnticrawlerRuleType API to specify the anti-crawler rule protection mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGeoipRule</td>
                    <td>Delete a geographical location control protection rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAntiTamperRule</td>
                    <td>Create an anti-tamper rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGeoipRule</td>
                    <td>Delete a geographical location control protection rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAnticrawlerRule</td>
                    <td>Delete a JS script anti-crawler protection rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIgnoreRule</td>
                    <td>Create a global trustlist (original false positive masking) rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIgnoreRule</td>
                    <td>Query the global trustlist rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGeoipRule</td>
                    <td>Query the geolocation access control rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWhiteBlackIpRule</td>
                    <td>Delete a blocklist and trustlist protection rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowValueList</td>
                    <td>Query the reference table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePunishmentRule</td>
                    <td>Delete an attack penalty rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAntitamperRule</td>
                    <td>Query anti-tamper protection rules</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAntileakageRule</td>
                    <td>Delete a sensitive information leakage prevention rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPunishmentRules</td>
                    <td>Query the attack penalty rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrivacyRule</td>
                    <td>Update a privacy masking rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePrivacyRule</td>
                    <td>Create a privacy masking rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAnticrawlerRule</td>
                    <td>Query the anti-crawler protection rule of the JS script by ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListValueList</td>
                    <td>Query the reference table list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIgnoreRule</td>
                    <td>Query the global trustlist (original false positive shielding) protection rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateValueList</td>
                    <td>Modifying a reference table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAnticrawlerRules</td>
                    <td>Query the anti-crawler rule list of a JS script</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCustomRule</td>
                    <td>Creating a Precise Protection Rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCcRule</td>
                    <td>Create a CC rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAntitamperRule</td>
                    <td>Query the anti-tamper rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Protection Event Management</td>
                    <td>ListEvent</td>
                    <td>Query the attack event list. Currently, this API does not support query of all defense events. The pagesize parameter cannot be set to - 1. Due to performance reasons, a larger data volume consumes more memory. A maximum of 10000 data records can be queried. For example: If the number of data records in the customized period exceeds 10000, the data records whose page is 101 and pagesize is 100 cannot be queried. You need to adjust the time period and then query the data.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEvent</td>
                    <td>Query the details of a protection event with a specified ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Protection Policy Management</td>
                    <td>DeletePolicy</td>
                    <td>To delete a protection policy, if the policy is in use, you need to unbind the domain name from the policy before deleting the policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicyProtectHost</td>
                    <td>Update the domain name of the protection policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicy</td>
                    <td>Query the protection policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPolicy</td>
                    <td>Query protection policies by ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePolicy</td>
                    <td>When creating a protection policy, the system configures some default configuration items when generating the policy. To modify the default configuration items, call the interface for updating the protection policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicy</td>
                    <td>Update the protection policy. The request body can contain only the part to be updated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Protection Website Management in Cloud Mode</td>
                    <td>ListHost</td>
                    <td>Query the domain name list in cloud mode</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHost</td>
                    <td>Query details about a cloud-based domain name based on the domain name ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHostProtectStatus</td>
                    <td>Modifying the domain name protection status</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHost</td>
                    <td>Update the domain name configuration in cloud mode. If the original data of the origin server is not entered, the new origin server will overwrite the origin server information instead of adding a new origin server. In addition, the request body can pass only the part that needs to be updated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostRoute</td>
                    <td>Return routing information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHost</td>
                    <td>Creating a domain name in cloud mode</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHost</td>
                    <td>Delete the domain name in cloud mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Protection website management in exclusive mode</td>
                    <td>DeletePremiumHost</td>
                    <td>Delete the domain name in exclusive mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPremiumHost</td>
                    <td>Domain name list in exclusive mode</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePremiumHostProtectStatus</td>
                    <td>Modifies the domain name protection status in exclusive mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPremiumHost</td>
                    <td>View the domain name configuration in exclusive mode</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePremiumHost</td>
                    <td>Create a domain name in exclusive mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePremiumHost</td>
                    <td>Modify the domain name configuration in exclusive mode. If the original data of the origin server information is not entered, the new origin server information will overwrite the origin server information instead of adding a new origin server. In addition, the request body can pass only the part that needs to be updated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query features supported by the site</td>
                    <td>ShowConsoleConfig</td>
                    <td>Querying features supported by the site</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Security Overview</td>
                    <td>ListRequestTimeline</td>
                    <td>Query the timeline statistics of the number of requests on the Security Overview page.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQpsTimeline</td>
                    <td>Query the number of times the security statistics are qps.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopAbnormal</td>
                    <td>Query the top service abnormality statistics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidthTimeline</td>
                    <td>Query the security bandwidth statistics. The statistics are the average bandwidth, in bit/s.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStatistics</td>
                    <td>Query the number of security overview requests and attacks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOverviewsClassification</td>
                    <td>Query top security overview category statistics, including the attacked domain name, attack source IP address, attacked URL, attack source area, and attack event distribution.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">System Management</td>
                    <td>ShowSourceIp</td>
                    <td>Query the WAF retrieval IP address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tenant Domain Name Query</td>
                    <td>ListCompositeHosts</td>
                    <td>Query the list of all protected domain names, including the cloud mode and exclusive mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCompositeHost</td>
                    <td>Query the domain name by ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tenant Protection Domain Name Management</td>
                    <td>MigrateCompositeHosts</td>
                    <td>Migrate domain names by enterprise project. This function is supported only by the professional and exclusive editions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Tenant subscription management</td>
                    <td>CreatePrepaidCloudWaf</td>
                    <td>Subscribe to the cloud WAF service in yearly/monthly mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubscriptionInfo</td>
                    <td>Query the tenant subscription information, including the cloud mode, yearly/monthly, pay-per-use, and exclusive mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangePrepaidCloudWaf</td>
                    <td>Change the WAF specification in the yearly/monthly cloud mode. Note:</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
