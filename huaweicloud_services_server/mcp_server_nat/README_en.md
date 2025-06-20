# NAT MCP Server 


## Version
v0.1.0

## Overview

NAT MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service NAT. Full-chain management of NAT resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Private Network DNAT Rule | DeletePrivateDnat | Deletes a specified DNAT rule. | To be tested |
|  | ListPrivateDnats | Query the DNAT rule list. | To be tested |
|  | CreatePrivateDnat | Create a DNAT rule. | To be tested |
|  | UpdatePrivateDnat | Updates a specified DNAT rule. | To be tested |
|  | ShowPrivateDnat | Query the details about a specified DNAT rule. | To be tested |
| Private Network NAT Gateway | CreatePrivateNat | Create a private network NAT gateway instance. | To be tested |
|  | DeletePrivateNat | Delete the private network NAT gateway instance. | To be tested |
|  | UpdatePrivateNat | Update the private network NAT gateway instance. | To be tested |
|  | ShowPrivateNat | Query the details of a specified private network NAT gateway instance. | To be tested |
|  | ListPrivateNats | Query the list of private network NAT gateway instances. | To be tested |
| Private Network NAT Gateway Tag Management | CreatePrivateNatTag | -A private network NAT gateway can have a maximum of 10 labels. | To be tested |
|  | DeletePrivateNatTag | -Idempotent interface: | To be tested |
|  | ShowPrivateNatTags | - Queries the label information of a specified private network NAT gateway instance. | To be tested |
|  | ListPrivateNatTags | - This API is used to query the set of all private NAT gateway labels of a tenant in a specified project and instance type. | To be tested |
|  | ListPrivateNatsByTags | - Filter private network NAT gateway instances by label. | To be tested |
|  | BatchCreateDeletePrivateNatTags | -Add or delete tags in batches for a specified private network NAT gateway instance. | To be tested |
| Private Network NAT Transit IP Address | CreateTransitIp | Create a transit IP address. | To be tested |
|  | DeleteTransitIp | Delete a transit IP address. | To be tested |
|  | ListTransitIps | Query the transit IP address list. | To be tested |
|  | ShowTransitIp | Query transit IP address details. | To be tested |
| Private Network SNAT Rule | CreatePrivateSnat | Create an SNAT rule. | To be tested |
|  | ListPrivateSnats | Query the SNAT rule list. | To be tested |
|  | DeletePrivateSnat | Deletes a specified SNAT rule. | To be tested |
|  | UpdatePrivateSnat | Updates a specified SNAT rule. | To be tested |
|  | ShowPrivateSnat | Query the details of a specified SNAT rule. | To be tested |
| Public Network DNAT Rule | BatchCreateNatGatewayDnatRules | Create DNAT rules in batches. | To be tested |
|  | UpdateNatGatewayDnatRule | Updates a specified DNAT rule. | To be tested |
|  | ListNatGatewayDnatRules | Query the DNAT rule list. | To be tested |
|  | ShowNatGatewayDnatRule | Query the details of a specified DNAT rule. | To be tested |
|  | CreateNatGatewayDnatRule | Create a DNAT rule. | To be tested |
|  | DeleteNatGatewayDnatRule | Deletes a specified DNAT rule. | To be tested |
| Public Network NAT Gateway | ShowNatGateway | Query the details about a specified public network NAT gateway instance. | To be tested |
|  | UpdateNatGateway | Update the public NAT gateway instance. | To be tested |
|  | CreateNatGateway | Create a public NAT gateway instance. | To be tested |
|  | DeleteNatGateway | Delete the public NAT gateway instance. | To be tested |
|  | ListNatGateways | Query the public network NAT gateway instance list. | To be tested |
| Public Network NAT Gateway Label | ListNatGatewayByTag | - Filter public network NAT gateway resource instances by label. | To be tested |
|  | BatchCreateDeleteNatGatewayTag | -Add or delete tags in batches for a specified public network NAT gateway instance. | To be tested |
|  | CreateNatGatewayTag | -Add a public network NAT gateway resource tag. A maximum of 10 labels can be placed on a resource. | To be tested |
|  | ListNatGatewayTag | - This API is used to query all labels of a tenant in a specified project and public network NAT gateway instance type. | To be tested |
|  | DeleteNatGatewayTag | - This API is used to delete the label information of a specified public network NAT gateway resource instance. | To be tested |
|  | ShowNatGatewayTag | - This API is used to query the label information of a specified public network NAT gateway instance. | To be tested |
| Public Network SNAT Rule | DeleteNatGatewaySnatRule | Deletes a specified SNAT rule. | To be tested |
|  | UpdateNatGatewaySnatRule | Updates a specified SNAT rule. | To be tested |
|  | CreateNatGatewaySnatRule | Create an SNAT rule. | To be tested |
|  | ListNatGatewaySnatRules | Query the SNAT rule list. | To be tested |
|  | ShowNatGatewaySnatRule | Query details about a specified SNAT rule. | To be tested |
| Transit IP Label Management | CreateTransitIpTag | - A transit IP address can have a maximum of 10 labels. | To be tested |
|  | ListTransitIpsByTags | - Filter transit IP instances by label. | To be tested |
|  | ShowTransitIpTags | - This API is used to query the label information of a specified transit IP instance. | To be tested |
|  | DeleteTransitIpTag | -Idempotent interface: | To be tested |
|  | BatchCreateDeleteTransitIpTags | -Add or delete tags for specified transit IP instances in batches | To be tested |
|  | ListTransitIpTags | - This API is used to query the set of all transit IP labels of a tenant in a specified project and instance type. | To be tested |

