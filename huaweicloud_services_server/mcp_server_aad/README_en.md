# AAD MCP Server 


## Version
v0.1.0

## Overview

AAD MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service AAD. Full-chain management of AAD resources can be carried out based on natural language.

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
                    <td rowspan="8">AAD - Overview</td>
                    <td>ListPeak</td>
                    <td>Query the peak traffic and attack count</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDDoSAttackEvent</td>
                    <td>Query the DDoS attack event list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWafAttackEvent</td>
                    <td>Query the attack event list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDDoSFlow</td>
                    <td>Query the BPS/PPS traffic of DDoS attack defense</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWafQps</td>
                    <td>Query QPS for CC attack defense</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWafBandwidth</td>
                    <td>Bandwidth curve</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWafQps</td>
                    <td>Query request QPS</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDDoSConnectionNumber</td>
                    <td>Query the number of new connections and the number of concurrent connections</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">AAD-Domain name management</td>
                    <td>ModifyDomainWebSwitch</td>
                    <td>Modifying the basic web/CC protection switch for a domain name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomain</td>
                    <td>Query the domain name list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainCertificate</td>
                    <td>Query the certificate information associated with a domain name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceId</td>
                    <td>Query the ID of the instance associated with a domain name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetCertForDomain</td>
                    <td>Uploading or Modifying the Certificate Corresponding to a Domain Name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAadDomain</td>
                    <td>Create a domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomain</td>
                    <td>Update domain name origin server configuration information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSourceIps</td>
                    <td>Query the retrieval IP address segment list of Advanced Anti-DDoS</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">AAD-Forwarding Rule Management</td>
                    <td>BatchDeleteInstanceIpRule</td>
                    <td>Delete forwarding rules for IP addresses of AAD instances in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateInstanceIpRule</td>
                    <td>Adding Forwarding Rules for IP Addresses of Advanced Anti-DDoS Instances in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceIpRule</td>
                    <td>Modifying the origin server IP address in the forwarding configuration of the AAD instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceIpRule</td>
                    <td>Query the forwarding rule list of the IP address of the AAD instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">AAD-Instance List</td>
                    <td>ListInstanceDomains</td>
                    <td>Query the domain name associated with an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeInstanceSpec</td>
                    <td>Modifying an instance specification</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">AAD-Protection Policy</td>
                    <td>AddBlackWhiteIpList</td>
                    <td>Adding an AAD instance to the blocklist and whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFrequencyControlRule</td>
                    <td>Query the frequency control rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWafWhiteIpRule</td>
                    <td>Protection policy web-cc blocklist and trustlit-deleting a blocklist and trustlist rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWafPolicy</td>
                    <td>Query the web protection policy configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlowBlock</td>
                    <td>Query the traffic blocking information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWhiteBlackIpRule</td>
                    <td>Query the trustlist and trustlist of DDoS attack defense</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddWafWhiteIpRule</td>
                    <td>Protection policy web-cc blocklist and trustlit-creating a blocklist and trustlist rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBlackWhiteIpList</td>
                    <td>Delete AAD instances from the blocklist and trustlist.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWafGeoIpRule</td>
                    <td>Query area barring rules</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWafCustomRule</td>
                    <td>Query precise protection rules</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWafWhiteIpRule</td>
                    <td>Protection policy web-cc blocklist and trustlit-query blocklist and trustlist rules</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Alarm Configuration Management</td>
                    <td>UpdateAlarmConfig</td>
                    <td>Modifying the alarm configuration interface</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlarmConfig</td>
                    <td>Obtain alarm configuration information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Domain</td>
                    <td>CreateDomain</td>
                    <td>Create a domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDomain</td>
                    <td>Delete a domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Exclusive Instance Management</td>
                    <td>ListInstance</td>
                    <td>Query the exclusive WAF engine list. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Native Advanced Anti-DDoS - Policy Management</td>
                    <td>DisassociateIpFromPolicyAndPackage</td>
                    <td>Unbind a policy from an instance to a Zone</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateIpToPolicyAndPackage</td>
                    <td>Binding a policy to an instance to a Zone</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateIpToPolicy</td>
                    <td>Bind the policy to the Zone</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddPolicyBlackAndWhiteIpList</td>
                    <td>Adding a policy to the blocklist or whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePolicyBlackAndWhiteIpList</td>
                    <td>Delete a policy from the blocklist or whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateIpFromPolicy</td>
                    <td>Unbind a policy from a Zone</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Native Advanced Anti-DDoS - Zone Management</td>
                    <td>ListProtectedIp</td>
                    <td>Querying the Zone List</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTagForProtectedIp</td>
                    <td>Setting Tags for Zones</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Native Advanced Anti-DDoS-Alarm Configuration Management</td>
                    <td>DeleteAlarmConfig</td>
                    <td>Delete alarm configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Native Advanced Anti-DDoS-Instance Management</td>
                    <td>UpdatePackageName</td>
                    <td>Update the instance name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUnboundProtectedIp</td>
                    <td>Query the list of Zones that can be bound</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPackage</td>
                    <td>Query the DB instance list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePackageIp</td>
                    <td>Updates all Zones bound to an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Protection Policy Management</td>
                    <td>DeletePolicy</td>
                    <td>To delete a protection policy, if the policy is in use, you need to unbind the domain name from the policy before deleting the policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPolicy</td>
                    <td>Query protection policies by ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicy</td>
                    <td>Query the protection policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicy</td>
                    <td>Update the protection policy. The request body can contain only the part to be updated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePolicy</td>
                    <td>When creating a protection policy, the system configures some default configuration items when generating the policy. To modify the default configuration items, call the interface for updating the protection policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Unblocking Center-Unblocking Management</td>
                    <td>ShowBlockStatistics</td>
                    <td>Query the blocking statistics.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBlockIps</td>
                    <td>Query the blocked tenant list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUnblockQuotaStatistics</td>
                    <td>Query the unblocking quota</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUnblockRecord</td>
                    <td>Query the unpacking records of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteUnblockIp</td>
                    <td>Unblocking the IP address</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
