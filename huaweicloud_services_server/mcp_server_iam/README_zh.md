# IAM MCP Server 

## 版本信息
v0.1.0

## 产品描述

IAM MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IAM交互的能力。可以基于自然语言对IAM资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| AccountSummary | GetAccountSummaryV5 | 该接口可以用于获取此账号中IAM实体使用情况和IAM配额的摘要信息。 | To be tested |
| Credential管理 | CreatePermanentAccessKey | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)给IAM用户创建永久访问密钥,或IAM用户给自己创建永久访问密钥。 | To be tested |
|  | CreateTemporaryAccessKeyByToken | 该接口可以用于通过token来获取临时AK/SK和securitytoken。 | To be tested |
|  | CreateTemporaryAccessKeyByAgency | 该接口可以用于通过委托来获取临时访问密钥(临时AK/SK)和securitytoken。 | To be tested |
|  | UpdatePermanentAccessKey | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户的指定永久访问密钥,或IAM用户修改自己的指定永久访问密钥。 | To be tested |
|  | DeletePermanentAccessKey | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除IAM用户的指定永久访问密钥,或IAM用户删除自己的指定永久访问密钥。 | To be tested |
|  | ListPermanentAccessKeys | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的所有永久访问密钥,或IAM用户查询自己的所有永久访问密钥。 | To be tested |
|  | ShowPermanentAccessKey | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的指定永久访问密钥,或IAM用户查询自己的指定永久访问密钥。 | To be tested |
| IAM用户管理 | KeystoneUpdateUserByAdmin | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户信息。 | To be tested |
|  | KeystoneListGroupsForUser | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户所属用户组,或IAM用户查询自己所属用户组。 | To be tested |
|  | ShowUserLoginProtect | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的登录保护状态信息,或IAM用户查询自己的登录保护状态信息。 | To be tested |
|  | UpdateLoginProtect | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号操作保护。 | To be tested |
|  | CreateUser | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建IAM用户。 | To be tested |
|  | KeystoneUpdateUserPassword | 该接口可以用于IAM用户修改自己的密码。 | To be tested |
|  | ShowUserMfaDevice | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的MFA绑定信息,或IAM用户查询自己的MFA绑定信息。 | To be tested |
|  | ListUserMfaDevices | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的MFA绑定信息列表。 | To be tested |
|  | KeystoneShowUser | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户详情,或IAM用户查询自己的用户详情。 | To be tested |
|  | ListUserLoginProtects | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的登录保护状态列表。 | To be tested |
|  | KeystoneDeleteUser | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除指定IAM用户。 | To be tested |
|  | KeystoneListUsersForGroupByAdmin | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组中所包含的IAM用户。 | To be tested |
|  | KeystoneCreateUser | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建IAM用户。IAM用户首次登录时需要修改密码。 | To be tested |
|  | KeystoneListUsers | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户列表。 | To be tested |
|  | ShowUser | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户详情,或IAM用户查询自己的详情。 | To be tested |
|  | UpdateUser | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户信息 。 | To be tested |
|  | UpdateUserInformation | 该接口可以用于IAM用户修改自己的用户信息。 | To be tested |
| Token管理 | KeystoneCreateUserTokenByPassword | 该接口可以用于通过用户名/密码的方式进行认证来获取IAM用户token。 | To be tested |
|  | KeystoneCreateAgencyToken | 该接口可以用于获取委托方的token。 | To be tested |
|  | KeystoneCreateUserTokenByPasswordAndMfa | 该接口可以用于通过用户名/密码+虚拟MFA的方式进行认证,在IAM用户开启了的登录保护功能,并选择通过虚拟MFA验证时获取IAM用户token。 | To be tested |
|  | KeystoneValidateToken | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)校验本账号中IAM用户token的有效性,或IAM用户校验自己token的有效性。管理员仅能校验本账号中IAM用户token的有效性,不能校验其他账号中IAM用户token的有效性。如果被校验的token有效,则返回该token的详细信息。 | To be tested |
| 企业项目管理 | RevokeRoleFromGroupOnEnterpriseProject | 该接口用于删除企业项目关联用户组的权限。 | To be tested |
|  | AssociateRoleToUserOnEnterpriseProject | 基于用户为企业项目授权。 | To be tested |
|  | AssociateRoleToAgencyOnEnterpriseProject | 该接口可以基于委托为企业项目授权 | To be tested |
|  | ListGroupsForEnterpriseProject | 该接口可用于查询企业项目关联的用户组。 | To be tested |
|  | ListEnterpriseProjectsForUser | 该接口可用于查询用户所关联的企业项目。 | To be tested |
|  | ListEnterpriseProjectsForGroup | 该接口可用于查询用户组所关联的企业项目。 | To be tested |
|  | ListRolesForUserOnEnterpriseProject | 该接口可用于查询企业项目直接关联用户的权限。 | To be tested |
|  | AssociateRoleToGroupOnEnterpriseProject | 该接口用于基于用户组为企业项目授权。 | To be tested |
|  | ListRolesForGroupOnEnterpriseProject | 该接口可用于查询企业项目已关联用户组的权限。 | To be tested |
|  | RevokeRoleFromUserOnEnterpriseProject | 删除企业项目直接关联用户的权限。 | To be tested |
|  | ListUsersForEnterpriseProject | 该接口可用于查询企业项目直接关联的用户。 | To be tested |
|  | RevokeRoleFromAgencyOnEnterpriseProject | 该接口可以删除企业项目委托上的授权 | To be tested |
| 区域管理 | KeystoneListRegions | 该接口可以用于查询区域列表。 | To be tested |
|  | KeystoneShowRegion | 该接口可以用于查询区域详情。 | To be tested |
| 委托管理 | DeleteAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除委托。 | To be tested |
|  | ListAllProjectsPermissionsForAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托所有项目服务权限列表。 | To be tested |
|  | RemoveDomainPermissionFromAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的全局服务权限。 | To be tested |
|  | CheckProjectPermissionForAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托是否拥有项目服务权限。 | To be tested |
|  | ListProjectPermissionsForAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目服务中的委托权限。 | To be tested |
|  | CheckAllProjectsPermissionForAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)检查委托是否具有所有项目服务权限。 | To be tested |
|  | AssociateAgencyWithDomainPermission | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予全局服务权限。 | To be tested |
|  | CheckDomainPermissionForAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托是否拥有全局服务权限。 | To be tested |
|  | ShowAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托详情。 | To be tested |
|  | RemoveProjectPermissionFromAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的项目服务权限。 | To be tested |
|  | ListDomainPermissionsForAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询全局服务中的委托权限。 | To be tested |
|  | AssociateAgencyWithAllProjectsPermission | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予所有项目服务权限。 | To be tested |
|  | UpdateAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改委托。 | To be tested |
|  | CreateAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托。 | To be tested |
|  | AssociateAgencyWithProjectPermission | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予项目服务权限。 | To be tested |
|  | ListAgencies | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定条件下的委托列表。 | To be tested |
|  | RemoveAllProjectsPermissionFromAgency | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的所有项目服务权限。 | To be tested |
| 安全设置 | DeleteMfaDevice | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除MFA设备。 | To be tested |
|  | ShowDomainLoginPolicy | 该接口可以用于查询账号登录策略。 | To be tested |
|  | CreateMfaDevice | 该接口可以用于创建MFA设备。 | To be tested |
|  | UpdateDomainProtectPolicy | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号操作保护策略。 | To be tested |
|  | UpdateDomainLoginPolicy | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号登录策略。 | To be tested |
|  | UpdateDomainPasswordPolicy | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号密码策略。 | To be tested |
|  | UpdateDomainApiAclPolicy | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号接口访问策略。 | To be tested |
|  | ShowDomainPasswordPolicy | 该接口可以用于查询账号密码策略。 | To be tested |
|  | DeleteBindingDevice | 该接口可以用于解绑MFA设备 | To be tested |
|  | CreateBindingDevice | 该接口可以用于绑定MFA设备。 | To be tested |
|  | ShowDomainProtectPolicy | 该接口可以用于查询账号操作保护策略。 | To be tested |
|  | ShowDomainApiAclPolicy | 该接口可以用于查询账号接口访问控制策略。 | To be tested |
|  | ShowDomainConsoleAclPolicy | 该接口可以用于查询账号控制台访问控制策略。 | To be tested |
|  | UpdateDomainConsoleAclPolicy | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号控制台访问策略。 | To be tested |
| 服务和终端节点 | KeystoneShowService | 该接口可以用于查询服务详情。 | To be tested |
|  | KeystoneListEndpoints | 该接口可以用于查询终端节点列表。终端节点用来提供服务访问入口。 | To be tested |
|  | KeystoneShowCatalog | 该接口可以用于查询请求头中X-Auth-Token对应的服务目录。 | To be tested |
|  | KeystoneShowEndpoint | 该接口可以用于查询终端节点详情。终端节点用来提供服务访问入口。 | To be tested |
|  | KeystoneListServices | 该接口可以用于查询服务列表。 | To be tested |
| 权限管理 | KeystoneShowPermission | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询权限详情。 | To be tested |
|  | KeystoneListDomainPermissionsForGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询全局服务中的用户组权限。 | To be tested |
|  | KeystoneCheckroleForGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有所有项目指定权限。 | To be tested |
|  | KeystoneCheckDomainPermissionForGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有全局服务权限。 | To be tested |
|  | KeystoneListProjectPermissionsForGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目服务中的用户组权限。 | To be tested |
|  | KeystoneRemoveDomainPermissionFromGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组的全局服务权限。 | To be tested |
|  | KeystoneListPermissions | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询权限列表。 | To be tested |
|  | DeleteDomainGroupInheritedRole | 该接口可以用于移除用户组的所有项目服务权限。 | To be tested |
|  | KeystoneAssociateGroupWithDomainPermission | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予全局服务权限。 | To be tested |
|  | KeystoneRemoveProjectPermissionFromGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组的项目服务权限。 | To be tested |
|  | KeystoneListAllProjectPermissionsForGroup | 该接口可以用于管理员查询用户组所有项目服务权限列表。 该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见:[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。 | To be tested |
|  | KeystoneCheckProjectPermissionForGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有项目服务权限。 | To be tested |
|  | UpdateDomainGroupInheritRole | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予所有项目服务权限。 | To be tested |
|  | ShowDomainRoleAssignments | 该接口用于查询指定账号中的授权记录。 | To be tested |
|  | KeystoneAssociateGroupWithProjectPermission | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予项目服务权限。 | To be tested |
| 版本信息管理 | KeystoneListVersions | 该接口用于查询Keystone API的版本信息。 | To be tested |
|  | KeystoneShowVersion | 该接口用于查询Keystone API的3.0版本的信息。 | To be tested |
| 用户组管理 | KeystoneCheckUserInGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户是否在用户组中。 | To be tested |
|  | KeystoneShowGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组详情。 | To be tested |
|  | KeystoneCreateGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建用户组。 | To be tested |
|  | KeystoneRemoveUserFromGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组中的IAM用户。 | To be tested |
|  | KeystoneDeleteGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除用户组。 | To be tested |
|  | KeystoneUpdateGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新用户组信息。 | To be tested |
|  | KeystoneListGroups | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组列表。 | To be tested |
|  | KeystoneAddUserToGroup | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)添加IAM用户到用户组。 | To be tested |
| 联邦身份认证管理 | KeystoneUpdateIdentityProvider | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新身份提供商。 | To be tested |
|  | KeystoneCreateScopedToken | 该接口可以用于通过联邦认证方式获取scoped token。 | To be tested |
|  | KeystoneUpdateProtocol | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新协议。 | To be tested |
|  | KeystoneListMappings | 该接口可以用于查询映射列表。 | To be tested |
|  | KeystoneListIdentityProviders | 该接口可以用于查询身份提供商列表。 | To be tested |
|  | CreateMetadata | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)导入Metadata文件。 | To be tested |
|  | KeystoneCreateIdentityProvider | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)注册身份提供商。 | To be tested |
|  | UpdateOpenIdConnectConfig | 修改OpenId Connect身份提供商配置 | To be tested |
|  | CreateUnscopedTokenWithIdToken | 获取联邦认证token(OpenId Connect Id token方式)。 | To be tested |
|  | KeystoneCreateProtocol | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)注册协议(将协议关联到某一身份提供商)。 | To be tested |
|  | KeystoneCreateMapping | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)注册映射。 | To be tested |
|  | KeystoneListFederationDomains | 该接口用于查询联邦用户可以访问的账号列表。 | To be tested |
|  | KeystoneUpdateMapping | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新映射。 | To be tested |
|  | ShowMetadata | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询身份提供商导入到IAM中的Metadata文件。 | To be tested |
|  | KeystoneListProtocols | 该接口可以用于查询协议列表。 | To be tested |
|  | KeystoneDeleteIdentityProvider | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) 删除身份提供商。 | To be tested |
|  | KeystoneShowMapping | 该接口可以用于查询映射详情。 | To be tested |
|  | ShowOpenIdConnectConfig | 查询OpenId Connect身份提供商配置 | To be tested |
|  | CreateTokenWithIdToken | 获取联邦认证token(OpenId Connect Id token方式) | To be tested |
|  | KeystoneDeleteProtocol | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除协议。 | To be tested |
|  | CreateOpenIdConnectConfig | 创建OpenId Connect身份提供商配置 | To be tested |
|  | KeystoneListFederationProjects | 该接口可以用于查询联邦用户可以访问的项目列表。 | To be tested |
|  | KeystoneShowProtocol | 该接口可以用于查询协议详情。 | To be tested |
|  | KeystoneShowIdentityProvider | 该接口可以用于查询身份提供商详情。 | To be tested |
|  | CreateUnscopeTokenByIdpInitiated | 该接口可以用于通过IdP initiated的联邦认证方式获取unscoped token。 | To be tested |
|  | ShowKeystoneMetadataFile | 该接口可以用于查询keystone的Metadata文件。 | To be tested |
|  | KeystoneDeleteMapping | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除映射。 | To be tested |
| 自定义代理 | CreateLoginToken | 该接口用于用于获取自定义代理登录票据logintoken。logintoken是系统颁发给自定义代理用户的登录票据,承载用户的身份、session等信息。调用自定义代理URL登录云服务控制台时,可以使用本接口获取的logintoken进行认证。 | To be tested |
| 自定义策略管理 | UpdateAgencyCustomPolicy | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改委托自定义策略。 | To be tested |
|  | ShowCustomPolicy | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询自定义策略详情。 | To be tested |
|  | CreateCloudServiceCustomPolicy | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建云服务自定义策略。 | To be tested |
|  | DeleteCustomPolicy | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除自定义策略。 | To be tested |
|  | UpdateCloudServiceCustomPolicy | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改云服务自定义策略。 | To be tested |
|  | ListCustomPolicies | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询自定义策略列表。 | To be tested |
|  | CreateAgencyCustomPolicy | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托自定义策略。 | To be tested |
| 账号管理 | KeystoneShowSecurityComplianceByOption | 该接口可以用于按条件查询账号密码强度策略,查询结果包括密码强度策略的正则表达式及其描述。 | To be tested |
|  | ShowDomainQuota | 该接口可以用于查询账号配额。 | To be tested |
|  | KeystoneShowSecurityCompliance | 该接口可以用于查询账号密码强度策略,查询结果包括密码强度策略的正则表达式及其描述。 | To be tested |
|  | KeystoneListAuthDomains | 该接口可以用于查询IAM用户可以用访问的账号详情。 | To be tested |
| 项目管理 | KeystoneListAuthProjects | 该接口可以用于查询IAM用户可以访问的项目列表。 | To be tested |
|  | KeystoneListProjects | 该接口可以用于查询指定条件下的项目列表。 | To be tested |
|  | KeystoneCreateProject | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建项目。 | To be tested |
|  | KeystoneUpdateProject | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改项目信息。 | To be tested |
|  | KeystoneListProjectsForUser | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的项目列表,或IAM用户查询自己的项目列表。 | To be tested |
|  | ShowProjectQuota | 该接口可以用于查询项目配额。 | To be tested |
|  | UpdateProjectStatus | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)设置项目状态。项目状态包括:正常、冻结。 | To be tested |
|  | ShowProjectDetailsAndStatus | 该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目详情与状态。 | To be tested |
|  | KeystoneShowProject | 该接口可以用于查询项目详情。 | To be tested |
