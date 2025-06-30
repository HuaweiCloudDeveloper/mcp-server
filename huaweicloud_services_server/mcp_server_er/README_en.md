# ER MCP Server 


## Version
v0.1.0

## Overview

ER MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ER. Full-chain management of ER resources can be carried out based on natural language.

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
                    <td rowspan="1">Association</td>
                    <td>ListAssociations</td>
                    <td>Query the route association list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Attachments</td>
                    <td>ListAttachments</td>
                    <td>Query the connection list of an enterprise router instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAttachment</td>
                    <td>Query connection details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAttachment</td>
                    <td>Modify the basic connection information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RejectAttachment</td>
                    <td>Rejecting the creation of a shared connection</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AcceptAttachment</td>
                    <td>Received the creation of a shared connection</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">AvailableZone</td>
                    <td>ListAvailabilityZone</td>
                    <td>Query the list of AZs where enterprise router instances can be created. When the AZ status is available, enterprise router instances can be created.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">EnterpriseRouterInstance</td>
                    <td>ChangeAvailabilityZone</td>
                    <td>This command is used to update the AZ information of the enterprise router. The AZ information can be updated only when the enterprise router instance is in the available state.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnterpriseRouters</td>
                    <td>Query the enterprise router list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnterpriseRouter</td>
                    <td>Create an enterprise router instance. If the default associated routing table or the default transit routing table is enabled, the system creates a routing table by default as the default associated routing table or the default transit routing table.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnterpriseRouter</td>
                    <td>Updating the basic information about the enterprise router.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnterpriseRouter</td>
                    <td>Query enterprise router details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnterpriseRouter</td>
                    <td>Delete an enterprise router.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">FDR</td>
                    <td>ShowFlowLog</td>
                    <td>Query FDR details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlowLog</td>
                    <td>Update FDR</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFlowLog</td>
                    <td>Delete the FDR</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlowLogs</td>
                    <td>Query the list of all FDRs of the tenant that submits the request and filter the FDRs based on the filter criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFlowLog</td>
                    <td>Create an FDR.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">FlowLog</td>
                    <td>EnableFlowLog</td>
                    <td>Enable the FDR function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableFlowLog</td>
                    <td>Disabling the FDR function</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Propagation</td>
                    <td>ListPropagations</td>
                    <td>Query the route propagation list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisablePropagation</td>
                    <td>Unbinds the connection from the routing table.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnablePropagation</td>
                    <td>Each connection can establish propagation relationships with multiple routing tables. Routes learned from the connection will be applied to the routing tables with propagation relationships.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowQuotas</td>
                    <td>Query the resource quota of the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Resource Tag</td>
                    <td>ShowResourceTag</td>
                    <td>Query the tags of a single resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResourceTag</td>
                    <td>Add tags to multiple cloud service resources. A maximum of 10 tags can be added to each resource. A maximum of 20 tags can be operated at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResourceTag</td>
                    <td>This API is used to remove tags of multiple cloud service resources in batches. A maximum of 10 tags can be removed for each resource. A maximum of 20 tags can be removed at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Route</td>
                    <td>ListStaticRoutes</td>
                    <td>Query the static route list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEffectiveRoutes</td>
                    <td>Query the valid route list. Pagination query is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStaticRoute</td>
                    <td>Create a static route</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStaticRoute</td>
                    <td>Update static routes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStaticRoute</td>
                    <td>Query static route details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStaticRoute</td>
                    <td>Delete a static route</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Routing table</td>
                    <td>ListRouteTables</td>
                    <td>Query the list of all routing tables of the account that submits the request and filter the routing tables based on the filtering conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateRouteTable</td>
                    <td>Disassociating a Subnet from the Routing Table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRouteTable</td>
                    <td>Create a routing table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRouteTable</td>
                    <td>Delete the routing table</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRouteTable</td>
                    <td>Associate the routing table with the subnet. A subnet is associated with routing table A and then associated with routing table B. It does not need to be disassociated from routing table A and then associated with routing table B.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRouteTable</td>
                    <td>Query the routing table details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRouteTable</td>
                    <td>Updates the routing table, including the name and description of the routing table, and adds, updates, and deletes routing entries.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tags</td>
                    <td>ListProjectTags</td>
                    <td>Query all tags of a specified resource type in a specified project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateResourceTags</td>
                    <td>Adding tags to specified instances in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">VPCAttachment</td>
                    <td>ListVpcAttachments</td>
                    <td>Query the VPC connection list of an enterprise router instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVpcAttachment</td>
                    <td>Query VPC connection details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpcAttachment</td>
                    <td>Modify the basic information about a VPC connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVpcAttachment</td>
                    <td>This API is used to create a VPC connection for the ER instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpcAttachment</td>
                    <td>Delete a VPC connection.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
