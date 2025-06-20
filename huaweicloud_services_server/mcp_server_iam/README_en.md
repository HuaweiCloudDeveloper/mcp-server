# IAM MCP Server 


## Version
v0.1.0

## Overview

IAM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IAM. Full-chain management of IAM resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Account management | KeystoneShowSecurityComplianceByOption | This API is used to query account password strength policies by conditions. The query result contains the regular expression and description of the password strength policies. | To be tested |
|  | ShowDomainQuota | This API is used to query the account quota. | To be tested |
|  | KeystoneShowSecurityCompliance | This API is used to query the account password strength policy. The query result contains the regular expression and description of the password strength policy. | To be tested |
|  | KeystoneListAuthDomains | This API is used to query details about accounts that can be accessed by an IAM user. | To be tested |
| AccountSummary | GetAccountSummaryV5 | This API is used to obtain the IAM entity usage and IAM quota summary information of the account. | To be tested |
| Credential Management | CreatePermanentAccessKey | This API can be used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create a permanent access key for an IAM user or an IAM user to create a permanent access key for itself. | To be tested |
|  | CreateTemporaryAccessKeyByToken | This API can be used to obtain the temporary AK/SK and security token using the token. | To be tested |
|  | CreateTemporaryAccessKeyByAgency | This API can be used to obtain the temporary access key (temporary AK/SK) and security token through an agency. | To be tested |
|  | UpdatePermanentAccessKey | This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify the specified permanent access key of an IAM user or an IAM user to modify the specified permanent access key of the user. | To be tested |
|  | DeletePermanentAccessKey | This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete the specified permanent access key of an IAM user or an IAM user to delete the specified permanent access key of the user. | To be tested |
|  | ListPermanentAccessKeys | This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query all permanent access keys of an IAM user, or an IAM user to query all permanent access keys of its own. | To be tested |
|  | ShowPermanentAccessKey | This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the specified permanent access key of an IAM user, or an IAM user to query the specified permanent access key of their own. | To be tested |
| Custom Agent | CreateLoginToken | This interface is used to obtain the logintoken of a user-defined proxy login ticket. A login token is a login ticket issued by the system to a user-defined proxy user. It carries the user identity and session information. When you call the user-defined proxy URL to log in to the cloud service console, you can use the login token obtained by this API for authentication. | To be tested |
| Customized policy management | UpdateAgencyCustomPolicy | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify a custom agency policy. | To be tested |
|  | ShowCustomPolicy | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query details about a custom policy. | To be tested |
|  | CreateCloudServiceCustomPolicy | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create custom cloud service policies. | To be tested |
|  | DeleteCustomPolicy | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete a user-defined policy. | To be tested |
|  | UpdateCloudServiceCustomPolicy | This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify a cloud service policy. | To be tested |
|  | ListCustomPolicies | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the user-defined policy list. | To be tested |
|  | CreateAgencyCustomPolicy | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create a custom agency policy. | To be tested |
| Enterprise Project Management | RevokeRoleFromGroupOnEnterpriseProject | This API is used to delete the permissions of a user group associated with an enterprise project. | To be tested |
|  | AssociateRoleToUserOnEnterpriseProject | Authorize enterprise projects based on users. | To be tested |
|  | AssociateRoleToAgencyOnEnterpriseProject | This interface can be used to authorize enterprise projects based on the agency. | To be tested |
|  | ListGroupsForEnterpriseProject | This API is used to query user groups associated with an enterprise project. | To be tested |
|  | ListEnterpriseProjectsForUser | This API is used to query the enterprise projects associated with a user. | To be tested |
|  | ListEnterpriseProjectsForGroup | This API is used to query the enterprise projects associated with a user group. | To be tested |
|  | ListRolesForUserOnEnterpriseProject | This API is used to query the permissions of users directly associated with an enterprise project. | To be tested |
|  | AssociateRoleToGroupOnEnterpriseProject | This API is used to grant permissions to enterprise projects based on user groups. | To be tested |
|  | ListRolesForGroupOnEnterpriseProject | This API is used to query the permissions of user groups associated with an enterprise project. | To be tested |
|  | RevokeRoleFromUserOnEnterpriseProject | Deletes the permissions of the users directly associated with the enterprise project. | To be tested |
|  | ListUsersForEnterpriseProject | This API is used to query users directly associated with an enterprise project. | To be tested |
|  | RevokeRoleFromAgencyOnEnterpriseProject | This interface is used to delete authorization on an enterprise project agency. | To be tested |
| Entrusted management | DeleteAgency | This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete an agency. | To be tested |
|  | ListAllProjectsPermissionsForAgency | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the service permission list of all projects of an agency. | To be tested |
|  | RemoveDomainPermissionFromAgency | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to remove the global service permission of an agency. | To be tested |
|  | CheckProjectPermissionForAgency | This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query whether an agency has the project service permission. | To be tested |
|  | ListProjectPermissionsForAgency | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the agency permission in the project service. | To be tested |
|  | CheckAllProjectsPermissionForAgency | This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to check whether an agency has all project service permissions. | To be tested |
|  | AssociateAgencyWithDomainPermission | This interface can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to grant global service permissions to an agency. | To be tested |
|  | CheckDomainPermissionForAgency | This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query whether an agency has the global service permission. | To be tested |
|  | ShowAgency | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query agency details. | To be tested |
|  | RemoveProjectPermissionFromAgency | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to remove the project service permission of an agency. | To be tested |
|  | ListDomainPermissionsForAgency | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query agency permissions in global services. | To be tested |
|  | AssociateAgencyWithAllProjectsPermission | This interface can be used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to grant all project service permissions to an agency. | To be tested |
|  | UpdateAgency | This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify an agency. | To be tested |
|  | CreateAgency | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create an agency. | To be tested |
|  | AssociateAgencyWithProjectPermission | This API is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to grant project service permissions to an agency. | To be tested |
|  | ListAgencies | This interface is used by the (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the agency list based on the specified conditions. | To be tested |
|  | RemoveAllProjectsPermissionFromAgency | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to remove all project service permissions of an agency. | To be tested |
| Federated identity authentication management | KeystoneUpdateIdentityProvider | This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to update the identity provider. | To be tested |
|  | KeystoneCreateScopedToken | This interface can be used to obtain a scoped token through federated authentication. | To be tested |
|  | KeystoneUpdateProtocol | This interface can be used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to update the protocol. | To be tested |
|  | KeystoneListMappings | This interface is used to query the mapping list. | To be tested |
|  | KeystoneListIdentityProviders | This API is used to query the identity provider list. | To be tested |
|  | CreateMetadata | This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to import a metadata file. | To be tested |
|  | KeystoneCreateIdentityProvider | This interface is used by the administrator to register an identity provider ((https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)). | To be tested |
|  | UpdateOpenIdConnectConfig | Modifying OpenId Connect Identity Provider Configuration | To be tested |
|  | CreateUnscopedTokenWithIdToken | Obtain the federated authentication token (OpenId Connect Id token mode). | To be tested |
|  | KeystoneCreateProtocol | This API can be used by the [administrator] to register the (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) protocol (associate the protocol with an identity provider). | To be tested |
|  | KeystoneCreateMapping | This interface can be used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to register mappings. | To be tested |
|  | KeystoneListFederationDomains | This interface is used to query the list of accounts that can be accessed by federated users. | To be tested |
|  | KeystoneUpdateMapping | This interface can be used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to update the mapping. | To be tested |
|  | ShowMetadata | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the metadata file imported by the identity provider to IAM. | To be tested |
|  | KeystoneListProtocols | This interface is used to query the protocol list. | To be tested |
|  | KeystoneDeleteIdentityProvider | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete an identity provider. | To be tested |
|  | KeystoneShowMapping | This API is used to query mapping details. | To be tested |
|  | ShowOpenIdConnectConfig | Query the configuration of the OpenId Connect identity provider | To be tested |
|  | CreateTokenWithIdToken | Obtain the federated authentication token (OpenId Connect Id token mode) | To be tested |
|  | KeystoneDeleteProtocol | This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete a protocol. | To be tested |
|  | CreateOpenIdConnectConfig | Create an OpenId Connect identity provider configuration | To be tested |
|  | KeystoneListFederationProjects | This API is used to query the list of projects that can be accessed by federated users. | To be tested |
|  | KeystoneShowProtocol | This interface is used to query protocol details. | To be tested |
|  | KeystoneShowIdentityProvider | This API is used to query details about an identity provider. | To be tested |
|  | CreateUnscopeTokenByIdpInitiated | This API can be used to obtain the unscoped token through the federated authentication mode initiated by the IdP. | To be tested |
|  | ShowKeystoneMetadataFile | This API is used to query the Keystone metadata file. | To be tested |
|  | KeystoneDeleteMapping | This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete a mapping. | To be tested |
| IAM User Management | KeystoneUpdateUserByAdmin | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify IAM user information. | To be tested |
|  | KeystoneListGroupsForUser | This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the user group to which an IAM user belongs, or by an IAM user to query the user group to which an IAM user belongs. | To be tested |
|  | ShowUserLoginProtect | This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the login protection status of a specified IAM user or an IAM user to query the login protection status of the user. | To be tested |
|  | UpdateLoginProtect | This interface can be used by [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify account operation protection. | To be tested |
|  | KeystoneUpdateUserPassword | This API is used by an IAM user to change their own passwords. | To be tested |
|  | ShowUserMfaDevice | This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the MFA binding information of a specified IAM user, or an IAM user to query its own MFA binding information. | To be tested |
|  | ListUserMfaDevices | This API is used by the (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) [administrator] to query the MFA binding information list of an IAM user. | To be tested |
|  | KeystoneShowUser | This API can be used by [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query IAM user details, or IAM users to query their own user details. | To be tested |
|  | ListUserLoginProtects | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the login protection status list of IAM users. | To be tested |
|  | KeystoneDeleteUser | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete a specified IAM user. | To be tested |
|  | KeystoneListUsersForGroupByAdmin | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the IAM users in a user group. | To be tested |
|  | KeystoneCreateUser | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create an IAM user. Change the password of the IAM user upon the first login. | To be tested |
|  | KeystoneListUsers | This API is used by [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the IAM user list. | To be tested |
|  | UpdateUserInformation | This API is used by IAM users to modify their own user information. | To be tested |
| Project Management | KeystoneListAuthProjects | This API is used to query the list of projects that IAM users can access. | To be tested |
|  | KeystoneListProjects | This API is used to query the project list based on the specified conditions. | To be tested |
|  | KeystoneCreateProject | This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create projects. | To be tested |
|  | KeystoneUpdateProject | This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify project information. | To be tested |
|  | KeystoneListProjectsForUser | This API can be used by [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the project list of a specified IAM user, or IAM users to query their own project list. | To be tested |
|  | ShowProjectQuota | This API is used to query project quotas. | To be tested |
|  | UpdateProjectStatus | This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to set the project status. The project status can be Normal or Frozen. | To be tested |
|  | ShowProjectDetailsAndStatus | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query project details and status. | To be tested |
|  | KeystoneShowProject | This API is used to query project details. | To be tested |
| Region management | KeystoneListRegions | This interface is used to query the region list. | To be tested |
|  | KeystoneShowRegion | This interface is used to query region details. | To be tested |
| Right management | KeystoneShowPermission | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query permission details. | To be tested |
|  | KeystoneListDomainPermissionsForGroup | This API is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query user group permissions in the global service. | To be tested |
|  | KeystoneCheckroleForGroup | This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query whether a user group has specified permissions for all projects. | To be tested |
|  | KeystoneCheckDomainPermissionForGroup | This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query whether a user group has the global service permission. | To be tested |
|  | KeystoneListProjectPermissionsForGroup | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query user group permissions in a project service. | To be tested |
|  | KeystoneRemoveDomainPermissionFromGroup | This API is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to remove the global service permission of a user group. | To be tested |
|  | KeystoneListPermissions | This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the permission list. | To be tested |
|  | DeleteDomainGroupInheritedRole | This API is used to remove all project service permissions from a user group. | To be tested |
|  | KeystoneAssociateGroupWithDomainPermission | This API is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to grant global service permissions to a user group. | To be tested |
|  | KeystoneRemoveProjectPermissionFromGroup | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to remove the project service permission of a user group. | To be tested |
|  | KeystoneListAllProjectPermissionsForGroup | This interface is used by the administrator to query the list of all project service permissions in a user group. This API can be invoked by the endpoints of the global zone and other zones.  | To be tested |
|  | KeystoneCheckProjectPermissionForGroup | This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query whether a user group has the project service permission. | To be tested |
|  | UpdateDomainGroupInheritRole | This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to grant all project service permissions to a user group. | To be tested |
|  | ShowDomainRoleAssignments | This interface is used to query the authorization records of a specified account. | To be tested |
|  | KeystoneAssociateGroupWithProjectPermission | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to grant project service permissions to a user group. | To be tested |
| Security Settings | DeleteMfaDevice | This API is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete an MFA device. | To be tested |
|  | ShowDomainLoginPolicy | This interface is used to query account login policies. | To be tested |
|  | CreateMfaDevice | This API is used to create an MFA device. | To be tested |
|  | UpdateDomainProtectPolicy | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify the account operation protection policy. | To be tested |
|  | UpdateDomainLoginPolicy | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify the account login policy. | To be tested |
|  | UpdateDomainPasswordPolicy | This API is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify the account password policy. | To be tested |
|  | UpdateDomainApiAclPolicy | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify the account interface access policy. | To be tested |
|  | ShowDomainPasswordPolicy | This interface is used to query account and password policies. | To be tested |
|  | DeleteBindingDevice | This interface can be used to unbind an MFA device. | To be tested |
|  | CreateBindingDevice | This interface can be used to bind an MFA device. | To be tested |
|  | ShowDomainProtectPolicy | This API is used to query account operation protection policies. | To be tested |
|  | ShowDomainApiAclPolicy | This API is used to query the access control policy of an account interface. | To be tested |
|  | ShowDomainConsoleAclPolicy | This API is used to query the access control policy of the account console. | To be tested |
|  | UpdateDomainConsoleAclPolicy | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify the account console access policy. | To be tested |
| Services and Endpoints | KeystoneShowService | This API is used to query service details. | To be tested |
|  | KeystoneListEndpoints | This API is used to query the VPC endpoint list. VPC endpoints are used as service access entries. | To be tested |
|  | KeystoneShowCatalog | This API is used to query the service catalog corresponding to X-Auth-Token in the request header. | To be tested |
|  | KeystoneShowEndpoint | This API is used to query VPC endpoint details. VPC endpoints are used as service access entries. | To be tested |
|  | KeystoneListServices | This API is used to query the service list. | To be tested |
| Token management | KeystoneCreateUserTokenByPassword | This API can be used to obtain the IAM user token through user name and password authentication. | To be tested |
|  | KeystoneCreateAgencyToken | This interface is used to obtain the token of the delegator. | To be tested |
|  | KeystoneCreateUserTokenByPasswordAndMfa | This API can be used for authentication using the username/password+virtual MFA. When the login protection function is enabled for the IAM user and the IAM user passes the virtual MFA authentication, the IAM user token is obtained. | To be tested |
|  | KeystoneValidateToken | This API can be used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to verify the validity of the IAM user token in the current account, or IAM user to verify the validity of their own token. The administrator can verify the validity of the IAM user token only in the current account. If the verified token is valid, details about the token are returned. | To be tested |
| User group management | KeystoneCheckUserInGroup | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query whether an IAM user is in a user group. | To be tested |
|  | KeystoneShowGroup | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query user group details. | To be tested |
|  | KeystoneCreateGroup | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create a user group. | To be tested |
|  | KeystoneRemoveUserFromGroup | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to remove an IAM user from a user group. | To be tested |
|  | KeystoneDeleteGroup | This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete a user group. | To be tested |
|  | KeystoneUpdateGroup | This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to update user group information. | To be tested |
|  | KeystoneListGroups | This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the user group list. | To be tested |
|  | KeystoneAddUserToGroup | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to add an IAM user to a user group. | To be tested |
| User management | CreateUser | Create a user. | To be tested |
|  | ShowUser | Query user details. | To be tested |
|  | UpdateUser | Modify user parameters. | To be tested |
| Version information management | KeystoneListVersions | This API is used to query the Keystone API version. | To be tested |
|  | KeystoneShowVersion | This API is used to query information about Keystone API 3.0. | To be tested |

