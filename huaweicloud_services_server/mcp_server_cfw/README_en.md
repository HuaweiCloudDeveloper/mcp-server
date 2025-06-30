# CFW MCP Server 


## Version
v0.1.0

## Overview

CFW MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CFW. Full-chain management of CFW resources can be carried out based on natural language.

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
                    <td rowspan="11">ACL Rule Management</td>
                    <td>UpdateAclRuleOrder</td>
                    <td>Setting the priority of an ACL protection rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAclRuleHitCount</td>
                    <td>Obtains the number of times a rule is hit.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRuleAclTags</td>
                    <td>Query Rule Tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAclRules</td>
                    <td>Delete ACL rules in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAclRule</td>
                    <td>Updating an ACL rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAclRules</td>
                    <td>Querying a protection rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAclRuleHitCount</td>
                    <td>Number of times a rule is cleared</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImportStatus</td>
                    <td>Interface for viewing the import status</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateAclRuleActions</td>
                    <td>Batch rule update action</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAclRule</td>
                    <td>Delete an ACL rule group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAclRule</td>
                    <td>Create an ACL rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Address Group Management</td>
                    <td>AddAddressSet</td>
                    <td>Adding an Address Group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAddressSet</td>
                    <td>Update address group information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAddressSet</td>
                    <td>Delete an address group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAddressItems</td>
                    <td>Querying the members of an address group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAddressItem</td>
                    <td>Delete an address group member</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAddressItem</td>
                    <td>Adding an address group member</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateObjectConfigDesc</td>
                    <td>Editing the description of a member in an object group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAddressSets</td>
                    <td>Query the address group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAddressSetDetail</td>
                    <td>Query the details of an address group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAddressItems</td>
                    <td>Delete address group members in batches</td>
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
                    <td rowspan="4">Antivirus management</td>
                    <td>ShowAntiVirusRule</td>
                    <td>Obtain the antivirus rule information of the firewall</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAntiVirusSwitch</td>
                    <td>Modifying the antivirus function</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAntiVirusRule</td>
                    <td>Modifying an antivirus rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAntiVirusSwitch</td>
                    <td>View the antivirus function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Black and Trust List Management</td>
                    <td>DeleteBlackWhiteList</td>
                    <td>Delete a blocklist or trustlist rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBlackWhiteList</td>
                    <td>Update the blocklist and whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBlackWhiteLists</td>
                    <td>Query the blocklist and whitelist</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddBlackWhiteList</td>
                    <td>Create a blocklist and trustlist rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Domain name resolution and domain name group management</td>
                    <td>ShowDomainSetDetail</td>
                    <td>View domain group details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDnsServers</td>
                    <td>Update the DNS server list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteDomainSet</td>
                    <td>Delete domain groups in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainSets</td>
                    <td>Query the domain group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDomains</td>
                    <td>Add domain name list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDomainSet</td>
                    <td>Add domain group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainSet</td>
                    <td>Update domain group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDnsServers</td>
                    <td>Query the list of DNS servers</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainParseDetail</td>
                    <td>Test the validity of the domain name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainParseIp</td>
                    <td>Obtain the domain name address resolution result</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDomainSet</td>
                    <td>Delete a domain group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">EIP Management</td>
                    <td>ChangeEipStatus</td>
                    <td>Enable or disable EIP. Before enabling EIP protection for the first time after purchasing an EIP, you need to use ListEips to synchronize EIP assets and set sync to 1.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEipCount</td>
                    <td>Query the number of EIPs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEips</td>
                    <td>Querying the EIP list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoProtectStatus</td>
                    <td>Obtain the EIP automatic protection status information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchAutoProtectStatus</td>
                    <td>Modifying the EIP automatic protection function</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmWhitelist</td>
                    <td>View the EIP alarm trustlist.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">FDR</td>
                    <td>ListFlowLogs</td>
                    <td>Query the list of all FDRs of the tenant that submits the request and filter the FDRs based on the filter criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Firewall management</td>
                    <td>ListJob</td>
                    <td>Obtain the execution status of the CFW task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEastWestFirewall</td>
                    <td>Create an east-west firewall</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFirewallList</td>
                    <td>Query the firewall list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectedVpcs</td>
                    <td>Query the protected VPC information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeEastWestFirewallStatus</td>
                    <td>Enabling or disabling east-west protection</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEastWestFirewall</td>
                    <td>Obtain the east-west firewall information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFirewallDetail</td>
                    <td>Querying a firewall instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">IPS Management</td>
                    <td>ListIpsSwitchStatus</td>
                    <td>Query the status of the IPS feature switch.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIpsProtectMode</td>
                    <td>Query the protection mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIpsRules</td>
                    <td>Querying the frequency IPS rule information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeIpsProtectMode</td>
                    <td>Switch the protection mode</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIpsUpdateTime</td>
                    <td>Obtain the IPS rule details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeIpsRuleMode</td>
                    <td>Change the IPS rule mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeIpsSwitchStatus</td>
                    <td>Switch status</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCustomerIps</td>
                    <td>Obtain the user-defined IPS rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAdvancedIpsRule</td>
                    <td>Create a frequency IPS rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIpsRules1</td>
                    <td>Obtains the IPS rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Key Tag Management</td>
                    <td>DeleteTag</td>
                    <td>- Function description: This API is used to delete a key tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Log management</td>
                    <td>ListLogConfig</td>
                    <td>Obtain log configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogConfig</td>
                    <td>Update log configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddLogConfig</td>
                    <td>Create log configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAttackLogs</td>
                    <td>Query attack logs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccessControlLogs</td>
                    <td>Query access control logs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Network ACL</td>
                    <td>CreateFirewall</td>
                    <td>Create a network ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFirewall</td>
                    <td>Delete a network ACL</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Packet capture management</td>
                    <td>CancelCaptureTask</td>
                    <td>Cancel the packet capture task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCaptureTask</td>
                    <td>Querying a packet capture task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCaptureTask</td>
                    <td>Create a packet capture task. Each task can be executed only once.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCaptureResult</td>
                    <td>Obtain the packet capture result</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCaptureTask</td>
                    <td>Delete packet capture tasks in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Region</td>
                    <td>ListRegions</td>
                    <td>Query the area visible to the user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Service group management</td>
                    <td>DeleteServiceSet</td>
                    <td>Delete a service group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddServiceSet</td>
                    <td>Create a service group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceItems</td>
                    <td>Query the service group member list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServiceSet</td>
                    <td>Update a service group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceSets</td>
                    <td>Obtain the service group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddServiceItems</td>
                    <td>Adding Service Group Members in Batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteServiceItems</td>
                    <td>Delete service group members in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServiceItem</td>
                    <td>Delete a service group member</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceSetDetail</td>
                    <td>Query service group details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tag Management</td>
                    <td>CreateTag</td>
                    <td>Add a tag to a resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveTags</td>
                    <td>API for saving resource tags</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>Query all tags of a specified resource type in a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Use TMS</td>
                    <td>ListResourceTags</td>
                    <td>Query the label information of a specified DB instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">websites</td>
                    <td>DeleteDomains</td>
                    <td>Delete the website assets of the tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomains</td>
                    <td>Obtain all website assets of a tenant</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
