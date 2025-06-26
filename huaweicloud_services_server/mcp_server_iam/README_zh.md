# IAM MCP Server 


## Version
v0.1.0

## Overview

IAM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IAM. Full-chain management of IAM resources can be carried out based on natural language.

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
                    <td rowspan="1">AccountSummary</td>
                    <td>GetAccountSummaryV5</td>
                    <td>该接口可以用于获取此账号中IAM实体使用情况和IAM配额的摘要信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Credential管理</td>
                    <td>CreatePermanentAccessKey</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)给IAM用户创建永久访问密钥,或IAM用户给自己创建永久访问密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemporaryAccessKeyByToken</td>
                    <td>该接口可以用于通过token来获取临时AK/SK和securitytoken。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemporaryAccessKeyByAgency</td>
                    <td>该接口可以用于通过委托来获取临时访问密钥(临时AK/SK)和securitytoken。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePermanentAccessKey</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户的指定永久访问密钥,或IAM用户修改自己的指定永久访问密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePermanentAccessKey</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除IAM用户的指定永久访问密钥,或IAM用户删除自己的指定永久访问密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPermanentAccessKeys</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的所有永久访问密钥,或IAM用户查询自己的所有永久访问密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPermanentAccessKey</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的指定永久访问密钥,或IAM用户查询自己的指定永久访问密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">IAM用户管理</td>
                    <td>KeystoneUpdateUserByAdmin</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListGroupsForUser</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户所属用户组,或IAM用户查询自己所属用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserLoginProtect</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的登录保护状态信息,或IAM用户查询自己的登录保护状态信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLoginProtect</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号操作保护。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneUpdateUserPassword</td>
                    <td>该接口可以用于IAM用户修改自己的密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserMfaDevice</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的MFA绑定信息,或IAM用户查询自己的MFA绑定信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserMfaDevices</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的MFA绑定信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowUser</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户详情,或IAM用户查询自己的用户详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserLoginProtects</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的登录保护状态列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneDeleteUser</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除指定IAM用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListUsersForGroupByAdmin</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组中所包含的IAM用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateUser</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建IAM用户。IAM用户首次登录时需要修改密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListUsers</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserInformation</td>
                    <td>该接口可以用于IAM用户修改自己的用户信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Token管理</td>
                    <td>KeystoneCreateUserTokenByPassword</td>
                    <td>该接口可以用于通过用户名/密码的方式进行认证来获取IAM用户token。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateAgencyToken</td>
                    <td>该接口可以用于获取委托方的token。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateUserTokenByPasswordAndMfa</td>
                    <td>该接口可以用于通过用户名/密码+虚拟MFA的方式进行认证,在IAM用户开启了的登录保护功能,并选择通过虚拟MFA验证时获取IAM用户token。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneValidateToken</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)校验本账号中IAM用户token的有效性,或IAM用户校验自己token的有效性。管理员仅能校验本账号中IAM用户token的有效性,不能校验其他账号中IAM用户token的有效性。如果被校验的token有效,则返回该token的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">企业项目管理</td>
                    <td>RevokeRoleFromGroupOnEnterpriseProject</td>
                    <td>该接口用于删除企业项目关联用户组的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRoleToUserOnEnterpriseProject</td>
                    <td>基于用户为企业项目授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRoleToAgencyOnEnterpriseProject</td>
                    <td>该接口可以基于委托为企业项目授权</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGroupsForEnterpriseProject</td>
                    <td>该接口可用于查询企业项目关联的用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnterpriseProjectsForUser</td>
                    <td>该接口可用于查询用户所关联的企业项目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnterpriseProjectsForGroup</td>
                    <td>该接口可用于查询用户组所关联的企业项目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRolesForUserOnEnterpriseProject</td>
                    <td>该接口可用于查询企业项目直接关联用户的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRoleToGroupOnEnterpriseProject</td>
                    <td>该接口用于基于用户组为企业项目授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRolesForGroupOnEnterpriseProject</td>
                    <td>该接口可用于查询企业项目已关联用户组的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeRoleFromUserOnEnterpriseProject</td>
                    <td>删除企业项目直接关联用户的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsersForEnterpriseProject</td>
                    <td>该接口可用于查询企业项目直接关联的用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeRoleFromAgencyOnEnterpriseProject</td>
                    <td>该接口可以删除企业项目委托上的授权</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">区域管理</td>
                    <td>KeystoneListRegions</td>
                    <td>该接口可以用于查询区域列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowRegion</td>
                    <td>该接口可以用于查询区域详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">委托管理</td>
                    <td>DeleteAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllProjectsPermissionsForAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托所有项目服务权限列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveDomainPermissionFromAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的全局服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckProjectPermissionForAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托是否拥有项目服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectPermissionsForAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目服务中的委托权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckAllProjectsPermissionForAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)检查委托是否具有所有项目服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateAgencyWithDomainPermission</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予全局服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckDomainPermissionForAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托是否拥有全局服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveProjectPermissionFromAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的项目服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainPermissionsForAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询全局服务中的委托权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateAgencyWithAllProjectsPermission</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予所有项目服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateAgencyWithProjectPermission</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予项目服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgencies</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定条件下的委托列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveAllProjectsPermissionFromAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的所有项目服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">安全设置</td>
                    <td>DeleteMfaDevice</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除MFA设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainLoginPolicy</td>
                    <td>该接口可以用于查询账号登录策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMfaDevice</td>
                    <td>该接口可以用于创建MFA设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainProtectPolicy</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号操作保护策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainLoginPolicy</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号登录策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainPasswordPolicy</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号密码策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainApiAclPolicy</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号接口访问策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainPasswordPolicy</td>
                    <td>该接口可以用于查询账号密码策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBindingDevice</td>
                    <td>该接口可以用于解绑MFA设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBindingDevice</td>
                    <td>该接口可以用于绑定MFA设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainProtectPolicy</td>
                    <td>该接口可以用于查询账号操作保护策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainApiAclPolicy</td>
                    <td>该接口可以用于查询账号接口访问控制策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainConsoleAclPolicy</td>
                    <td>该接口可以用于查询账号控制台访问控制策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainConsoleAclPolicy</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号控制台访问策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">服务和终端节点</td>
                    <td>KeystoneShowService</td>
                    <td>该接口可以用于查询服务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListEndpoints</td>
                    <td>该接口可以用于查询终端节点列表。终端节点用来提供服务访问入口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowCatalog</td>
                    <td>该接口可以用于查询请求头中X-Auth-Token对应的服务目录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowEndpoint</td>
                    <td>该接口可以用于查询终端节点详情。终端节点用来提供服务访问入口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListServices</td>
                    <td>该接口可以用于查询服务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">权限管理</td>
                    <td>KeystoneShowPermission</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询权限详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListDomainPermissionsForGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询全局服务中的用户组权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCheckroleForGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有所有项目指定权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCheckDomainPermissionForGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有全局服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListProjectPermissionsForGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目服务中的用户组权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneRemoveDomainPermissionFromGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组的全局服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListPermissions</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询权限列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDomainGroupInheritedRole</td>
                    <td>该接口可以用于移除用户组的所有项目服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneAssociateGroupWithDomainPermission</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予全局服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneRemoveProjectPermissionFromGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组的项目服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListAllProjectPermissionsForGroup</td>
                    <td>该接口可以用于管理员查询用户组所有项目服务权限列表。 该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见:[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCheckProjectPermissionForGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有项目服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainGroupInheritRole</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予所有项目服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainRoleAssignments</td>
                    <td>该接口用于查询指定账号中的授权记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneAssociateGroupWithProjectPermission</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予项目服务权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">版本信息管理</td>
                    <td>KeystoneListVersions</td>
                    <td>该接口用于查询Keystone API的版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowVersion</td>
                    <td>该接口用于查询Keystone API的3.0版本的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">用户管理</td>
                    <td>CreateUser</td>
                    <td>创建用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUser</td>
                    <td>查询用户详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUser</td>
                    <td>修改用户参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">用户组管理</td>
                    <td>KeystoneCheckUserInGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户是否在用户组中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneRemoveUserFromGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组中的IAM用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneDeleteGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneUpdateGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新用户组信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListGroups</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneAddUserToGroup</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)添加IAM用户到用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="27">联邦身份认证管理</td>
                    <td>KeystoneUpdateIdentityProvider</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新身份提供商。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateScopedToken</td>
                    <td>该接口可以用于通过联邦认证方式获取scoped token。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneUpdateProtocol</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新协议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListMappings</td>
                    <td>该接口可以用于查询映射列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListIdentityProviders</td>
                    <td>该接口可以用于查询身份提供商列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMetadata</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)导入Metadata文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateIdentityProvider</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)注册身份提供商。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOpenIdConnectConfig</td>
                    <td>修改OpenId Connect身份提供商配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUnscopedTokenWithIdToken</td>
                    <td>获取联邦认证token(OpenId Connect Id token方式)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateProtocol</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)注册协议(将协议关联到某一身份提供商)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateMapping</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)注册映射。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListFederationDomains</td>
                    <td>该接口用于查询联邦用户可以访问的账号列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneUpdateMapping</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新映射。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetadata</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询身份提供商导入到IAM中的Metadata文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListProtocols</td>
                    <td>该接口可以用于查询协议列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneDeleteIdentityProvider</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) 删除身份提供商。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowMapping</td>
                    <td>该接口可以用于查询映射详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOpenIdConnectConfig</td>
                    <td>查询OpenId Connect身份提供商配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTokenWithIdToken</td>
                    <td>获取联邦认证token(OpenId Connect Id token方式)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneDeleteProtocol</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除协议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOpenIdConnectConfig</td>
                    <td>创建OpenId Connect身份提供商配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListFederationProjects</td>
                    <td>该接口可以用于查询联邦用户可以访问的项目列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowProtocol</td>
                    <td>该接口可以用于查询协议详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowIdentityProvider</td>
                    <td>该接口可以用于查询身份提供商详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUnscopeTokenByIdpInitiated</td>
                    <td>该接口可以用于通过IdP initiated的联邦认证方式获取unscoped token。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKeystoneMetadataFile</td>
                    <td>该接口可以用于查询keystone的Metadata文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneDeleteMapping</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除映射。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">自定义代理</td>
                    <td>CreateLoginToken</td>
                    <td>该接口用于用于获取自定义代理登录票据logintoken。logintoken是系统颁发给自定义代理用户的登录票据,承载用户的身份、session等信息。调用自定义代理URL登录云服务控制台时,可以使用本接口获取的logintoken进行认证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">自定义策略管理</td>
                    <td>UpdateAgencyCustomPolicy</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改委托自定义策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCustomPolicy</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询自定义策略详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCloudServiceCustomPolicy</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建云服务自定义策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomPolicy</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除自定义策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCloudServiceCustomPolicy</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改云服务自定义策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCustomPolicies</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询自定义策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgencyCustomPolicy</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托自定义策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">账号管理</td>
                    <td>KeystoneShowSecurityComplianceByOption</td>
                    <td>该接口可以用于按条件查询账号密码强度策略,查询结果包括密码强度策略的正则表达式及其描述。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainQuota</td>
                    <td>该接口可以用于查询账号配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowSecurityCompliance</td>
                    <td>该接口可以用于查询账号密码强度策略,查询结果包括密码强度策略的正则表达式及其描述。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListAuthDomains</td>
                    <td>该接口可以用于查询IAM用户可以用访问的账号详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">项目管理</td>
                    <td>KeystoneListAuthProjects</td>
                    <td>该接口可以用于查询IAM用户可以访问的项目列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListProjects</td>
                    <td>该接口可以用于查询指定条件下的项目列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateProject</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建项目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneUpdateProject</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改项目信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListProjectsForUser</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的项目列表,或IAM用户查询自己的项目列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectQuota</td>
                    <td>该接口可以用于查询项目配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProjectStatus</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)设置项目状态。项目状态包括:正常、冻结。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectDetailsAndStatus</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目详情与状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowProject</td>
                    <td>该接口可以用于查询项目详情。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
