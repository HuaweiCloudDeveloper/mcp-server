# RAM MCP Server 

## 版本信息
v0.1.0

## 产品描述

RAM MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务RAM交互的能力。可以基于自然语言对RAM资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AssociatedPermission | DisassociateResourceSharePermission | 移除资源共享实例绑定的共享资源权限。权限更改立即生效。只有当目前资源共享实例中没有绑定相关资源类型时,您才能从资源共享实例中移除共享资源权限。 | To be tested |
|  | AssociateResourceSharePermission | 为资源共享实例中包含的资源类型绑定或替换共享资源权限。 对于资源共享实例中的每一种资源类型,您可以设置唯一权限。仅当资源共享实例中当前没有该资源类型的资源时,您才能绑定新的共享资源权限。 | To be tested |
|  | ListResourceSharePermissions | 检索资源共享实例关联的共享资源权限。 | To be tested |
| Misc | ListQuota | 查询当前账号的资源共享配额信息。 | To be tested |
|  | ListResourceTypes | 查询已对接云服务的资源类型和区域等信息。 | To be tested |
| OrganizationSharing | DisableOrganizationShare | 关闭与组织共享资源。 | To be tested |
|  | ShowOrganizationShare | 检索是否启用与组织共享资源。 | To be tested |
|  | EnableOrganizationShare | 启用与组织共享资源。 | To be tested |
| Permission | ListPermissionVersions | 获取权限的所有版本。 | To be tested |
|  | ListPermissions | 检索指定资源类型的共享资源权限列表。 | To be tested |
|  | ShowPermission | 检索指定资源类型的共享资源指定版本的权限内容,如果不指定权限版本,则返回默认版本的权限内容。 | To be tested |
| Principal | SearchSharedPrincipals | 检索共享资源的使用者。 | To be tested |
| Resource | SearchSharedResources | 检索您共享的或共享给您的资源。 | To be tested |
| ResourceShare | CreateResourceShare | 创建一个资源共享实例。您可以指定需要共享的资源列表,资源使用者列表,以及授予资源使用者的权限列表。 | To be tested |
|  | SearchResourceShares | 检索您创建的或者共享给您的资源共享实例详情。 | To be tested |
|  | DeleteResourceShare | 删除指定的资源共享实例。此操作不会删除实体资源,仅停止向其他账号共享资源。 | To be tested |
|  | UpdateResourceShare | 修改资源共享实例的特定属性。 | To be tested |
| ResourceShareAssociation | AssociateResourceShare | 向资源共享实例绑定指定的资源使用者列表或共享资源列表。对于新增的共享资源,有权访问此资源共享实例的资源使用者获得该共享资源的访问权限。对于新增的资源使用者,获得对此资源共享实例中共享资源的访问权限。 | To be tested |
|  | DisassociateResourceShare | 将指定的资源使用者或共享资源从指定的资源共享实例中移除。资源使用者也可以从指定的资源共享实例中主动退出。 | To be tested |
|  | SearchResourceShareAssociations | 检索您拥有的资源共享实例中绑定的共享资源和资源使用者。 | To be tested |
| ResourceShareInvitation | AcceptResourceShareInvitation | 接受来自其他账号的资源共享邀请。 | To be tested |
|  | RejectResourceShareInvitation | 拒绝来自其他账号的资源共享邀请。 | To be tested |
|  | SearchResourceShareInvitation | 通过条件检索资源共享邀请。 | To be tested |
| Tag | BatchCreateResourceShareTags | 资源共享实例增加标签。 | To be tested |
|  | SearchResourceShareCountByTags | 根据标签信息查询资源共享实例数量。 | To be tested |
|  | BatchDeleteResourceShareTags | 删除资源共享实例指定的标签。 | To be tested |
|  | ListResourceShareTags | 查询资源共享实例已使用标签的列表。 | To be tested |
|  | ListResourceSharesByTags | 根据标签信息查询资源共享实例列表。 | To be tested |
