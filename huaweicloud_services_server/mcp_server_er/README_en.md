# ER MCP Server 


## Version
v0.1.0

## Overview

ER MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ER. Full-chain management of ER resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Association | ListAssociations | Query the route association list. | To be tested |
| Attachments | ListAttachments | Query the connection list of an enterprise router instance. | To be tested |
|  | ShowAttachment | Query connection details | To be tested |
|  | UpdateAttachment | Modify the basic connection information. | To be tested |
|  | RejectAttachment | Rejecting the creation of a shared connection | To be tested |
|  | AcceptAttachment | Received the creation of a shared connection | To be tested |
| AvailableZone | ListAvailabilityZone | Query the list of AZs where enterprise router instances can be created. When the AZ status is available, enterprise router instances can be created. | To be tested |
| EnterpriseRouterInstance | ChangeAvailabilityZone | This command is used to update the AZ information of the enterprise router. The AZ information can be updated only when the enterprise router instance is in the available state. | To be tested |
|  | ListEnterpriseRouters | Query the enterprise router list | To be tested |
|  | CreateEnterpriseRouter | Create an enterprise router instance. If the default associated routing table or the default transit routing table is enabled, the system creates a routing table by default as the default associated routing table or the default transit routing table. | To be tested |
|  | UpdateEnterpriseRouter | Updating the basic information about the enterprise router. | To be tested |
|  | ShowEnterpriseRouter | Query enterprise router details | To be tested |
|  | DeleteEnterpriseRouter | Delete an enterprise router. | To be tested |
| FDR | ShowFlowLog | Query FDR details | To be tested |
|  | UpdateFlowLog | Update FDR | To be tested |
|  | DeleteFlowLog | Delete the FDR | To be tested |
|  | ListFlowLogs | Query the list of all FDRs of the tenant that submits the request and filter the FDRs based on the filter criteria. | To be tested |
|  | CreateFlowLog | Create an FDR. | To be tested |
| FlowLog | EnableFlowLog | Enable the FDR function. | To be tested |
|  | DisableFlowLog | Disabling the FDR function | To be tested |
| Propagation | ListPropagations | Query the route propagation list. | To be tested |
|  | DisablePropagation | Unbinds the connection from the routing table. | To be tested |
|  | EnablePropagation | Each connection can establish propagation relationships with multiple routing tables. Routes learned from the connection will be applied to the routing tables with propagation relationships. | To be tested |
| Quota | ShowQuotas | Query the resource quota of the current project. | To be tested |
| Resource Tag | ShowResourceTag | Query the tags of a single resource. | To be tested |
|  | CreateResourceTag | Add tags to multiple cloud service resources. A maximum of 10 tags can be added to each resource. A maximum of 20 tags can be operated at a time. | To be tested |
|  | DeleteResourceTag | This API is used to remove tags of multiple cloud service resources in batches. A maximum of 10 tags can be removed for each resource. A maximum of 20 tags can be removed at a time. | To be tested |
| Route | ListStaticRoutes | Query the static route list. | To be tested |
|  | ListEffectiveRoutes | Query the valid route list. Pagination query is supported. | To be tested |
|  | CreateStaticRoute | Create a static route | To be tested |
|  | UpdateStaticRoute | Update static routes | To be tested |
|  | ShowStaticRoute | Query static route details | To be tested |
|  | DeleteStaticRoute | Delete a static route | To be tested |
| Routing table | ListRouteTables | Query the list of all routing tables of the account that submits the request and filter the routing tables based on the filtering conditions. | To be tested |
|  | DisassociateRouteTable | Disassociating a Subnet from the Routing Table | To be tested |
|  | CreateRouteTable | Create a routing table | To be tested |
|  | DeleteRouteTable | Delete the routing table | To be tested |
|  | AssociateRouteTable | Associate the routing table with the subnet. A subnet is associated with routing table A and then associated with routing table B. It does not need to be disassociated from routing table A and then associated with routing table B. | To be tested |
|  | ShowRouteTable | Query the routing table details | To be tested |
|  | UpdateRouteTable | Updates the routing table, including the name and description of the routing table, and adds, updates, and deletes routing entries. | To be tested |
| Tags | ListProjectTags | Query all tags of a specified resource type in a specified project | To be tested |
|  | BatchCreateResourceTags | Adding tags to specified instances in batches | To be tested |
| VPCAttachment | ListVpcAttachments | Query the VPC connection list of an enterprise router instance. | To be tested |
|  | ShowVpcAttachment | Query VPC connection details | To be tested |
|  | UpdateVpcAttachment | Modify the basic information about a VPC connection. | To be tested |
|  | CreateVpcAttachment | This API is used to create a VPC connection for the ER instance. | To be tested |
|  | DeleteVpcAttachment | Delete a VPC connection. | To be tested |

