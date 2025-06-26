# NAT MCP Server 


## Version
v0.1.0

## Overview

NAT MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service NAT. Full-chain management of NAT resources can be carried out based on natural language.

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
                    <td rowspan="5">Private Network DNAT Rule</td>
                    <td>DeletePrivateDnat</td>
                    <td>Deletes a specified DNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateDnats</td>
                    <td>Query the DNAT rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePrivateDnat</td>
                    <td>Create a DNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrivateDnat</td>
                    <td>Updates a specified DNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateDnat</td>
                    <td>Query the details about a specified DNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Private Network NAT Gateway</td>
                    <td>CreatePrivateNat</td>
                    <td>Create a private network NAT gateway instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePrivateNat</td>
                    <td>Delete the private network NAT gateway instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrivateNat</td>
                    <td>Update the private network NAT gateway instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateNat</td>
                    <td>Query the details of a specified private network NAT gateway instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateNats</td>
                    <td>Query the list of private network NAT gateway instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Private Network NAT Gateway Tag Management</td>
                    <td>CreatePrivateNatTag</td>
                    <td>-A private network NAT gateway can have a maximum of 10 labels.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePrivateNatTag</td>
                    <td>-Idempotent interface:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateNatTags</td>
                    <td>- Queries the label information of a specified private network NAT gateway instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateNatTags</td>
                    <td>- This API is used to query the set of all private NAT gateway labels of a tenant in a specified project and instance type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateNatsByTags</td>
                    <td>- Filter private network NAT gateway instances by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateDeletePrivateNatTags</td>
                    <td>-Add or delete tags in batches for a specified private network NAT gateway instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Private Network NAT Transit IP Address</td>
                    <td>CreateTransitIp</td>
                    <td>Create a transit IP address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTransitIp</td>
                    <td>Delete a transit IP address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTransitIps</td>
                    <td>Query the transit IP address list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTransitIp</td>
                    <td>Query transit IP address details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Private Network SNAT Rule</td>
                    <td>CreatePrivateSnat</td>
                    <td>Create an SNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrivateSnats</td>
                    <td>Query the SNAT rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePrivateSnat</td>
                    <td>Deletes a specified SNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePrivateSnat</td>
                    <td>Updates a specified SNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrivateSnat</td>
                    <td>Query the details of a specified SNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Public Network DNAT Rule</td>
                    <td>BatchCreateNatGatewayDnatRules</td>
                    <td>Create DNAT rules in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNatGatewayDnatRule</td>
                    <td>Updates a specified DNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNatGatewayDnatRules</td>
                    <td>Query the DNAT rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNatGatewayDnatRule</td>
                    <td>Query the details of a specified DNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNatGatewayDnatRule</td>
                    <td>Create a DNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNatGatewayDnatRule</td>
                    <td>Deletes a specified DNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Public Network NAT Gateway</td>
                    <td>ShowNatGateway</td>
                    <td>Query the details about a specified public network NAT gateway instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNatGateway</td>
                    <td>Update the public NAT gateway instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNatGateway</td>
                    <td>Create a public NAT gateway instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNatGateway</td>
                    <td>Delete the public NAT gateway instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNatGateways</td>
                    <td>Query the public network NAT gateway instance list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Public Network NAT Gateway Label</td>
                    <td>ListNatGatewayByTag</td>
                    <td>- Filter public network NAT gateway resource instances by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateDeleteNatGatewayTag</td>
                    <td>-Add or delete tags in batches for a specified public network NAT gateway instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNatGatewayTag</td>
                    <td>-Add a public network NAT gateway resource tag. A maximum of 10 labels can be placed on a resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNatGatewayTag</td>
                    <td>- This API is used to query all labels of a tenant in a specified project and public network NAT gateway instance type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNatGatewayTag</td>
                    <td>- This API is used to delete the label information of a specified public network NAT gateway resource instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNatGatewayTag</td>
                    <td>- This API is used to query the label information of a specified public network NAT gateway instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Public Network SNAT Rule</td>
                    <td>DeleteNatGatewaySnatRule</td>
                    <td>Deletes a specified SNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNatGatewaySnatRule</td>
                    <td>Updates a specified SNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNatGatewaySnatRule</td>
                    <td>Create an SNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNatGatewaySnatRules</td>
                    <td>Query the SNAT rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNatGatewaySnatRule</td>
                    <td>Query details about a specified SNAT rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Transit IP Label Management</td>
                    <td>CreateTransitIpTag</td>
                    <td>- A transit IP address can have a maximum of 10 labels.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTransitIpsByTags</td>
                    <td>- Filter transit IP instances by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTransitIpTags</td>
                    <td>- This API is used to query the label information of a specified transit IP instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTransitIpTag</td>
                    <td>-Idempotent interface:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateDeleteTransitIpTags</td>
                    <td>-Add or delete tags for specified transit IP instances in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTransitIpTags</td>
                    <td>- This API is used to query the set of all transit IP labels of a tenant in a specified project and instance type.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
