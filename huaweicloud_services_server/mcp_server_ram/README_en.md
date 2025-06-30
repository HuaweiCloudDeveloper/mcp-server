# RAM MCP Server 


## Version
v0.1.0

## Overview

RAM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RAM. Full-chain management of RAM resources can be carried out based on natural language.

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
                    <td rowspan="3">AssociatedPermission</td>
                    <td>DisassociateResourceSharePermission</td>
                    <td>Removes the shared resource permission bound to a resource sharing instance. The permission change takes effect immediately. You can remove the shared resource permission from the shared resource instance only when no related resource type is bound to the current shared resource instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateResourceSharePermission</td>
                    <td>Bind or replace shared resource permissions for resource types contained in a shared resource instance. You can set unique permissions for each resource type in a resource sharing instance. You can bind new shared resource permissions only if there are no resources of that resource type in the shared instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceSharePermissions</td>
                    <td>Retrieves the shared resource permission associated with the shared resource instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Misc</td>
                    <td>ListQuota</td>
                    <td>Query the resource sharing quota information of the current account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceTypes</td>
                    <td>Query the resource types and regions of interconnected cloud services.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">OrganizationSharing</td>
                    <td>DisableOrganizationShare</td>
                    <td>Disable sharing resources with organizations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOrganizationShare</td>
                    <td>Retrieves whether to enable sharing resources with organizations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableOrganizationShare</td>
                    <td>Enable sharing resources with organizations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Permission</td>
                    <td>ListPermissionVersions</td>
                    <td>Obtains all versions of the permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPermissions</td>
                    <td>Retrieves the shared resource permission list of the specified resource type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPermission</td>
                    <td>Retrieves the permission content of a specified version of a shared resource of a specified resource type. If no permission version is specified, the permission content of the default version is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Principal</td>
                    <td>SearchSharedPrincipals</td>
                    <td>Retrieves the consumer of the shared resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Resource</td>
                    <td>SearchSharedResources</td>
                    <td>Retrieve the resources that you share or are shared with you.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">ResourceShare</td>
                    <td>CreateResourceShare</td>
                    <td>Create a resource sharing instance. You can specify a list of resources to be shared, a list of resource consumers, and a list of permissions granted to resource consumers.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchResourceShares</td>
                    <td>Retrieves the details about the resource sharing instance that you created or shared with you.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResourceShare</td>
                    <td>This API is used to delete a specified resource sharing instance. This operation does not delete the entity resource. It only stops sharing resources with other accounts.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResourceShare</td>
                    <td>Modifies the specific attributes of a resource sharing instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ResourceShareAssociation</td>
                    <td>AssociateResourceShare</td>
                    <td>Bind the specified resource consumer list or shared resource list to the resource sharing instance. For the new shared resource, the resource consumer who has the right to access the shared resource instance obtains the permission to access the shared resource. For the new resource consumer, access to the shared resources in the resource sharing instance is granted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateResourceShare</td>
                    <td>Removes a specified resource consumer or shared resource from a specified resource sharing instance. Resource users can also proactively exit from the specified resource sharing instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchResourceShareAssociations</td>
                    <td>Retrieve the shared resources and resource consumers bound to the resource sharing instance that you own.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ResourceShareInvitation</td>
                    <td>AcceptResourceShareInvitation</td>
                    <td>Resource sharing invitations from other accounts are accepted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RejectResourceShareInvitation</td>
                    <td>Reject resource sharing invitations from other accounts.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchResourceShareInvitation</td>
                    <td>Retrieve resource sharing invitations by condition.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Tag</td>
                    <td>BatchCreateResourceShareTags</td>
                    <td>Add a tag to a resource sharing instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchResourceShareCountByTags</td>
                    <td>Query the number of resource sharing instances based on the tag information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteResourceShareTags</td>
                    <td>Delete the specified tag of a resource sharing instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceShareTags</td>
                    <td>Query the list of used tags of a resource sharing instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceSharesByTags</td>
                    <td>Query the resource sharing instance list based on the tag information.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
