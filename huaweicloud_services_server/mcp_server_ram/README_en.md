# RAM MCP Server 


## Version
v0.1.0

## Overview

RAM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RAM. Full-chain management of RAM resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AssociatedPermission | DisassociateResourceSharePermission | Removes the shared resource permission bound to a resource sharing instance. The permission change takes effect immediately. You can remove the shared resource permission from the shared resource instance only when no related resource type is bound to the current shared resource instance. | To be tested |
|  | AssociateResourceSharePermission | Bind or replace shared resource permissions for resource types contained in a shared resource instance. You can set unique permissions for each resource type in a resource sharing instance. You can bind new shared resource permissions only if there are no resources of that resource type in the shared instance. | To be tested |
|  | ListResourceSharePermissions | Retrieves the shared resource permission associated with the shared resource instance. | To be tested |
| Misc | ListQuota | Query the resource sharing quota information of the current account. | To be tested |
|  | ListResourceTypes | Query the resource types and regions of interconnected cloud services. | To be tested |
| OrganizationSharing | DisableOrganizationShare | Disable sharing resources with organizations. | To be tested |
|  | ShowOrganizationShare | Retrieves whether to enable sharing resources with organizations. | To be tested |
|  | EnableOrganizationShare | Enable sharing resources with organizations. | To be tested |
| Permission | ListPermissionVersions | Obtains all versions of the permission. | To be tested |
|  | ListPermissions | Retrieves the shared resource permission list of the specified resource type. | To be tested |
|  | ShowPermission | Retrieves the permission content of a specified version of a shared resource of a specified resource type. If no permission version is specified, the permission content of the default version is returned. | To be tested |
| Principal | SearchSharedPrincipals | Retrieves the consumer of the shared resource. | To be tested |
| Resource | SearchSharedResources | Retrieve the resources that you share or are shared with you. | To be tested |
| ResourceShare | CreateResourceShare | Create a resource sharing instance. You can specify a list of resources to be shared, a list of resource consumers, and a list of permissions granted to resource consumers. | To be tested |
|  | SearchResourceShares | Retrieves the details about the resource sharing instance that you created or shared with you. | To be tested |
|  | DeleteResourceShare | This API is used to delete a specified resource sharing instance. This operation does not delete the entity resource. It only stops sharing resources with other accounts. | To be tested |
|  | UpdateResourceShare | Modifies the specific attributes of a resource sharing instance. | To be tested |
| ResourceShareAssociation | AssociateResourceShare | Bind the specified resource consumer list or shared resource list to the resource sharing instance. For the new shared resource, the resource consumer who has the right to access the shared resource instance obtains the permission to access the shared resource. For the new resource consumer, access to the shared resources in the resource sharing instance is granted. | To be tested |
|  | DisassociateResourceShare | Removes a specified resource consumer or shared resource from a specified resource sharing instance. Resource users can also proactively exit from the specified resource sharing instance. | To be tested |
|  | SearchResourceShareAssociations | Retrieve the shared resources and resource consumers bound to the resource sharing instance that you own. | To be tested |
| ResourceShareInvitation | AcceptResourceShareInvitation | Resource sharing invitations from other accounts are accepted. | To be tested |
|  | RejectResourceShareInvitation | Reject resource sharing invitations from other accounts. | To be tested |
|  | SearchResourceShareInvitation | Retrieve resource sharing invitations by condition. | To be tested |
| Tag | BatchCreateResourceShareTags | Add a tag to a resource sharing instance. | To be tested |
|  | SearchResourceShareCountByTags | Query the number of resource sharing instances based on the tag information. | To be tested |
|  | BatchDeleteResourceShareTags | Delete the specified tag of a resource sharing instance. | To be tested |
|  | ListResourceShareTags | Query the list of used tags of a resource sharing instance. | To be tested |
|  | ListResourceSharesByTags | Query the resource sharing instance list based on the tag information. | To be tested |

