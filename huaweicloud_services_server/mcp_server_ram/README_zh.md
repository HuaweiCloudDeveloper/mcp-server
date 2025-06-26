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
                    <td>移除资源共享实例绑定的共享资源权限。权限更改立即生效。只有当目前资源共享实例中没有绑定相关资源类型时,您才能从资源共享实例中移除共享资源权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateResourceSharePermission</td>
                    <td>为资源共享实例中包含的资源类型绑定或替换共享资源权限。 对于资源共享实例中的每一种资源类型,您可以设置唯一权限。仅当资源共享实例中当前没有该资源类型的资源时,您才能绑定新的共享资源权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceSharePermissions</td>
                    <td>检索资源共享实例关联的共享资源权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Misc</td>
                    <td>ListQuota</td>
                    <td>查询当前账号的资源共享配额信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceTypes</td>
                    <td>查询已对接云服务的资源类型和区域等信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">OrganizationSharing</td>
                    <td>DisableOrganizationShare</td>
                    <td>关闭与组织共享资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOrganizationShare</td>
                    <td>检索是否启用与组织共享资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableOrganizationShare</td>
                    <td>启用与组织共享资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Permission</td>
                    <td>ListPermissionVersions</td>
                    <td>获取权限的所有版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPermissions</td>
                    <td>检索指定资源类型的共享资源权限列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPermission</td>
                    <td>检索指定资源类型的共享资源指定版本的权限内容,如果不指定权限版本,则返回默认版本的权限内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Principal</td>
                    <td>SearchSharedPrincipals</td>
                    <td>检索共享资源的使用者。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Resource</td>
                    <td>SearchSharedResources</td>
                    <td>检索您共享的或共享给您的资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">ResourceShare</td>
                    <td>CreateResourceShare</td>
                    <td>创建一个资源共享实例。您可以指定需要共享的资源列表,资源使用者列表,以及授予资源使用者的权限列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchResourceShares</td>
                    <td>检索您创建的或者共享给您的资源共享实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResourceShare</td>
                    <td>删除指定的资源共享实例。此操作不会删除实体资源,仅停止向其他账号共享资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResourceShare</td>
                    <td>修改资源共享实例的特定属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ResourceShareAssociation</td>
                    <td>AssociateResourceShare</td>
                    <td>向资源共享实例绑定指定的资源使用者列表或共享资源列表。对于新增的共享资源,有权访问此资源共享实例的资源使用者获得该共享资源的访问权限。对于新增的资源使用者,获得对此资源共享实例中共享资源的访问权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateResourceShare</td>
                    <td>将指定的资源使用者或共享资源从指定的资源共享实例中移除。资源使用者也可以从指定的资源共享实例中主动退出。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchResourceShareAssociations</td>
                    <td>检索您拥有的资源共享实例中绑定的共享资源和资源使用者。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ResourceShareInvitation</td>
                    <td>AcceptResourceShareInvitation</td>
                    <td>接受来自其他账号的资源共享邀请。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RejectResourceShareInvitation</td>
                    <td>拒绝来自其他账号的资源共享邀请。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchResourceShareInvitation</td>
                    <td>通过条件检索资源共享邀请。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Tag</td>
                    <td>BatchCreateResourceShareTags</td>
                    <td>资源共享实例增加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchResourceShareCountByTags</td>
                    <td>根据标签信息查询资源共享实例数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteResourceShareTags</td>
                    <td>删除资源共享实例指定的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceShareTags</td>
                    <td>查询资源共享实例已使用标签的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceSharesByTags</td>
                    <td>根据标签信息查询资源共享实例列表。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
