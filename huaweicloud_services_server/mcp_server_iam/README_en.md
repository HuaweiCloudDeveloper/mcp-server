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
                    <td rowspan="4">Account management</td>
                    <td>KeystoneShowSecurityComplianceByOption</td>
                    <td>This API is used to query account password strength policies by conditions. The query result contains the regular expression and description of the password strength policies.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainQuota</td>
                    <td>This API is used to query the account quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowSecurityCompliance</td>
                    <td>This API is used to query the account password strength policy. The query result contains the regular expression and description of the password strength policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListAuthDomains</td>
                    <td>This API is used to query details about accounts that can be accessed by an IAM user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">AccountSummary</td>
                    <td>GetAccountSummaryV5</td>
                    <td>This API is used to obtain the IAM entity usage and IAM quota summary information of the account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Credential Management</td>
                    <td>CreatePermanentAccessKey</td>
                    <td>This API can be used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create a permanent access key for an IAM user or an IAM user to create a permanent access key for itself.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemporaryAccessKeyByToken</td>
                    <td>This API can be used to obtain the temporary AK/SK and security token using the token.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemporaryAccessKeyByAgency</td>
                    <td>This API can be used to obtain the temporary access key (temporary AK/SK) and security token through an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePermanentAccessKey</td>
                    <td>This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify the specified permanent access key of an IAM user or an IAM user to modify the specified permanent access key of the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePermanentAccessKey</td>
                    <td>This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete the specified permanent access key of an IAM user or an IAM user to delete the specified permanent access key of the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPermanentAccessKeys</td>
                    <td>This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query all permanent access keys of an IAM user, or an IAM user to query all permanent access keys of its own.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPermanentAccessKey</td>
                    <td>This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the specified permanent access key of an IAM user, or an IAM user to query the specified permanent access key of their own.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Custom Agent</td>
                    <td>CreateLoginToken</td>
                    <td>This interface is used to obtain the logintoken of a user-defined proxy login ticket. A login token is a login ticket issued by the system to a user-defined proxy user. It carries the user identity and session information. When you call the user-defined proxy URL to log in to the cloud service console, you can use the login token obtained by this API for authentication.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Customized policy management</td>
                    <td>UpdateAgencyCustomPolicy</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify a custom agency policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCustomPolicy</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query details about a custom policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCloudServiceCustomPolicy</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create custom cloud service policies.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomPolicy</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete a user-defined policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCloudServiceCustomPolicy</td>
                    <td>This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify a cloud service policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCustomPolicies</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the user-defined policy list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgencyCustomPolicy</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create a custom agency policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Enterprise Project Management</td>
                    <td>RevokeRoleFromGroupOnEnterpriseProject</td>
                    <td>This API is used to delete the permissions of a user group associated with an enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRoleToUserOnEnterpriseProject</td>
                    <td>Authorize enterprise projects based on users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRoleToAgencyOnEnterpriseProject</td>
                    <td>This interface can be used to authorize enterprise projects based on the agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGroupsForEnterpriseProject</td>
                    <td>This API is used to query user groups associated with an enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnterpriseProjectsForUser</td>
                    <td>This API is used to query the enterprise projects associated with a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnterpriseProjectsForGroup</td>
                    <td>This API is used to query the enterprise projects associated with a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRolesForUserOnEnterpriseProject</td>
                    <td>This API is used to query the permissions of users directly associated with an enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRoleToGroupOnEnterpriseProject</td>
                    <td>This API is used to grant permissions to enterprise projects based on user groups.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRolesForGroupOnEnterpriseProject</td>
                    <td>This API is used to query the permissions of user groups associated with an enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeRoleFromUserOnEnterpriseProject</td>
                    <td>Deletes the permissions of the users directly associated with the enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsersForEnterpriseProject</td>
                    <td>This API is used to query users directly associated with an enterprise project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeRoleFromAgencyOnEnterpriseProject</td>
                    <td>This interface is used to delete authorization on an enterprise project agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">Entrusted management</td>
                    <td>DeleteAgency</td>
                    <td>This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllProjectsPermissionsForAgency</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the service permission list of all projects of an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveDomainPermissionFromAgency</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to remove the global service permission of an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckProjectPermissionForAgency</td>
                    <td>This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query whether an agency has the project service permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectPermissionsForAgency</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the agency permission in the project service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckAllProjectsPermissionForAgency</td>
                    <td>This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to check whether an agency has all project service permissions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateAgencyWithDomainPermission</td>
                    <td>This interface can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to grant global service permissions to an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckDomainPermissionForAgency</td>
                    <td>This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query whether an agency has the global service permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgency</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query agency details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveProjectPermissionFromAgency</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to remove the project service permission of an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainPermissionsForAgency</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query agency permissions in global services.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateAgencyWithAllProjectsPermission</td>
                    <td>This interface can be used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to grant all project service permissions to an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAgency</td>
                    <td>This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgency</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateAgencyWithProjectPermission</td>
                    <td>This API is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to grant project service permissions to an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgencies</td>
                    <td>This interface is used by the (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the agency list based on the specified conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveAllProjectsPermissionFromAgency</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to remove all project service permissions of an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="27">Federated identity authentication management</td>
                    <td>KeystoneUpdateIdentityProvider</td>
                    <td>This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to update the identity provider.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateScopedToken</td>
                    <td>This interface can be used to obtain a scoped token through federated authentication.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneUpdateProtocol</td>
                    <td>This interface can be used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to update the protocol.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListMappings</td>
                    <td>This interface is used to query the mapping list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListIdentityProviders</td>
                    <td>This API is used to query the identity provider list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMetadata</td>
                    <td>This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to import a metadata file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateIdentityProvider</td>
                    <td>This interface is used by the administrator to register an identity provider ((https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOpenIdConnectConfig</td>
                    <td>Modifying OpenId Connect Identity Provider Configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUnscopedTokenWithIdToken</td>
                    <td>Obtain the federated authentication token (OpenId Connect Id token mode).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateProtocol</td>
                    <td>This API can be used by the [administrator] to register the (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) protocol (associate the protocol with an identity provider).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateMapping</td>
                    <td>This interface can be used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to register mappings.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListFederationDomains</td>
                    <td>This interface is used to query the list of accounts that can be accessed by federated users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneUpdateMapping</td>
                    <td>This interface can be used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to update the mapping.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetadata</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the metadata file imported by the identity provider to IAM.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListProtocols</td>
                    <td>This interface is used to query the protocol list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneDeleteIdentityProvider</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete an identity provider.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowMapping</td>
                    <td>This API is used to query mapping details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOpenIdConnectConfig</td>
                    <td>Query the configuration of the OpenId Connect identity provider</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTokenWithIdToken</td>
                    <td>Obtain the federated authentication token (OpenId Connect Id token mode)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneDeleteProtocol</td>
                    <td>This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete a protocol.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOpenIdConnectConfig</td>
                    <td>Create an OpenId Connect identity provider configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListFederationProjects</td>
                    <td>This API is used to query the list of projects that can be accessed by federated users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowProtocol</td>
                    <td>This interface is used to query protocol details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowIdentityProvider</td>
                    <td>This API is used to query details about an identity provider.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUnscopeTokenByIdpInitiated</td>
                    <td>This API can be used to obtain the unscoped token through the federated authentication mode initiated by the IdP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKeystoneMetadataFile</td>
                    <td>This API is used to query the Keystone metadata file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneDeleteMapping</td>
                    <td>This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete a mapping.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">IAM User Management</td>
                    <td>KeystoneUpdateUserByAdmin</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify IAM user information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListGroupsForUser</td>
                    <td>This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the user group to which an IAM user belongs, or by an IAM user to query the user group to which an IAM user belongs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserLoginProtect</td>
                    <td>This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the login protection status of a specified IAM user or an IAM user to query the login protection status of the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLoginProtect</td>
                    <td>This interface can be used by [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify account operation protection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneUpdateUserPassword</td>
                    <td>This API is used by an IAM user to change their own passwords.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserMfaDevice</td>
                    <td>This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the MFA binding information of a specified IAM user, or an IAM user to query its own MFA binding information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserMfaDevices</td>
                    <td>This API is used by the (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) [administrator] to query the MFA binding information list of an IAM user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowUser</td>
                    <td>This API can be used by [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query IAM user details, or IAM users to query their own user details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserLoginProtects</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the login protection status list of IAM users.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneDeleteUser</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete a specified IAM user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListUsersForGroupByAdmin</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the IAM users in a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateUser</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create an IAM user. Change the password of the IAM user upon the first login.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListUsers</td>
                    <td>This API is used by [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the IAM user list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserInformation</td>
                    <td>This API is used by IAM users to modify their own user information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Project Management</td>
                    <td>KeystoneListAuthProjects</td>
                    <td>This API is used to query the list of projects that IAM users can access.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListProjects</td>
                    <td>This API is used to query the project list based on the specified conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateProject</td>
                    <td>This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create projects.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneUpdateProject</td>
                    <td>This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify project information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListProjectsForUser</td>
                    <td>This API can be used by [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the project list of a specified IAM user, or IAM users to query their own project list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectQuota</td>
                    <td>This API is used to query project quotas.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProjectStatus</td>
                    <td>This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to set the project status. The project status can be Normal or Frozen.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectDetailsAndStatus</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query project details and status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowProject</td>
                    <td>This API is used to query project details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Region management</td>
                    <td>KeystoneListRegions</td>
                    <td>This interface is used to query the region list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowRegion</td>
                    <td>This interface is used to query region details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">Right management</td>
                    <td>KeystoneShowPermission</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query permission details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListDomainPermissionsForGroup</td>
                    <td>This API is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query user group permissions in the global service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCheckroleForGroup</td>
                    <td>This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query whether a user group has specified permissions for all projects.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCheckDomainPermissionForGroup</td>
                    <td>This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query whether a user group has the global service permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListProjectPermissionsForGroup</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query user group permissions in a project service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneRemoveDomainPermissionFromGroup</td>
                    <td>This API is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to remove the global service permission of a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListPermissions</td>
                    <td>This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the permission list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDomainGroupInheritedRole</td>
                    <td>This API is used to remove all project service permissions from a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneAssociateGroupWithDomainPermission</td>
                    <td>This API is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to grant global service permissions to a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneRemoveProjectPermissionFromGroup</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to remove the project service permission of a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListAllProjectPermissionsForGroup</td>
                    <td>This interface is used by the administrator to query the list of all project service permissions in a user group. This API can be invoked by the endpoints of the global zone and other zones.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCheckProjectPermissionForGroup</td>
                    <td>This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query whether a user group has the project service permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainGroupInheritRole</td>
                    <td>This API can be used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to grant all project service permissions to a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainRoleAssignments</td>
                    <td>This interface is used to query the authorization records of a specified account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneAssociateGroupWithProjectPermission</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to grant project service permissions to a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Security Settings</td>
                    <td>DeleteMfaDevice</td>
                    <td>This API is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete an MFA device.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainLoginPolicy</td>
                    <td>This interface is used to query account login policies.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMfaDevice</td>
                    <td>This API is used to create an MFA device.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainProtectPolicy</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify the account operation protection policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainLoginPolicy</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify the account login policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainPasswordPolicy</td>
                    <td>This API is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify the account password policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainApiAclPolicy</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify the account interface access policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainPasswordPolicy</td>
                    <td>This interface is used to query account and password policies.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBindingDevice</td>
                    <td>This interface can be used to unbind an MFA device.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBindingDevice</td>
                    <td>This interface can be used to bind an MFA device.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainProtectPolicy</td>
                    <td>This API is used to query account operation protection policies.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainApiAclPolicy</td>
                    <td>This API is used to query the access control policy of an account interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainConsoleAclPolicy</td>
                    <td>This API is used to query the access control policy of the account console.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainConsoleAclPolicy</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to modify the account console access policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Services and Endpoints</td>
                    <td>KeystoneShowService</td>
                    <td>This API is used to query service details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListEndpoints</td>
                    <td>This API is used to query the VPC endpoint list. VPC endpoints are used as service access entries.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowCatalog</td>
                    <td>This API is used to query the service catalog corresponding to X-Auth-Token in the request header.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowEndpoint</td>
                    <td>This API is used to query VPC endpoint details. VPC endpoints are used as service access entries.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListServices</td>
                    <td>This API is used to query the service list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Token management</td>
                    <td>KeystoneCreateUserTokenByPassword</td>
                    <td>This API can be used to obtain the IAM user token through user name and password authentication.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateAgencyToken</td>
                    <td>This interface is used to obtain the token of the delegator.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateUserTokenByPasswordAndMfa</td>
                    <td>This API can be used for authentication using the username/password+virtual MFA. When the login protection function is enabled for the IAM user and the IAM user passes the virtual MFA authentication, the IAM user token is obtained.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneValidateToken</td>
                    <td>This API can be used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to verify the validity of the IAM user token in the current account, or IAM user to verify the validity of their own token. The administrator can verify the validity of the IAM user token only in the current account. If the verified token is valid, details about the token are returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">User group management</td>
                    <td>KeystoneCheckUserInGroup</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query whether an IAM user is in a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowGroup</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query user group details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneCreateGroup</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneRemoveUserFromGroup</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to remove an IAM user from a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneDeleteGroup</td>
                    <td>This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to delete a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneUpdateGroup</td>
                    <td>This interface is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to update user group information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneListGroups</td>
                    <td>This interface is used by the administrator (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the user group list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneAddUserToGroup</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to add an IAM user to a user group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">User management</td>
                    <td>CreateUser</td>
                    <td>Create a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUser</td>
                    <td>Query user details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUser</td>
                    <td>Modify user parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Version information management</td>
                    <td>KeystoneListVersions</td>
                    <td>This API is used to query the Keystone API version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>KeystoneShowVersion</td>
                    <td>This API is used to query information about Keystone API 3.0.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
