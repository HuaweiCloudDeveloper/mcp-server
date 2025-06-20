# CSMS MCP Server 


## Version
v0.1.0

## Overview

CSMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CSMS. Full-chain management of CSMS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Asset Management | ListUsers | Query the server list of the account | To be tested |
| Authorization management | UpdateGrant | Update Authorization | To be tested |
|  | CreateGrants | Authentication operation | To be tested |
|  | DeleteGrant | Delete an authorization | To be tested |
| Certificate Label Management | BatchCreateOrDeleteTags | Create or delete tags in batches. | To be tested |
| Credential Label Management | CreateSecretTag | Add a credential label. | To be tested |
|  | ListProjectSecretsTags | Query the set of all credential labels of a user in a specified project. | To be tested |
|  | DeleteSecretTag | Delete the credential label. | To be tested |
|  | ListSecretTags | Query the credential label. | To be tested |
| Credential Rotation Management | ShowSecretFunctionTemplates | Obtain the credential rotation function template. | To be tested |
|  | ListSecretTask | Query the task list. | To be tested |
| Credential Version Management | ListSecretVersions | Query the version list under a specified credential. | To be tested |
|  | ShowSecretVersion | Query the information about the specified credential version and the plaintext credential value in the version. Only the credentials in the Enabled state can be queried. | To be tested |
|  | UpdateVersion | Currently, the validity period of a specified credential version can be updated. Only the credentials in the Enabled state can be updated. When the associated subscribed event contains the 'Version Expired' base event type, only one event notification is triggered after the version validity period is updated. | To be tested |
|  | CreateSecretVersion | In the specified credential, create a new credential version to encrypt the new credential value. By default, the newly created version of the credential is marked with the SYS/2000/present state, while the previous version of the credential for the SYS/2000/present tag is marked with the SYSPREVIVEIOUS state. You can override the default behavior by specifying the VersionStage parameter. | To be tested |
| Credential detection management | ShowSecretsConfig | Obtain the credential detection configuration of the tenant. | To be tested |
|  | UpdateSecretsConfig | Modify the configuration for detecting the tenant's credentials. | To be tested |
|  | CheckSecrets | Detects incoming credentials. | To be tested |
| Credential version status management | ShowSecretStage | Query the version information of the specified credential version status tag. | To be tested |
|  | UpdateSecretStage | Update the version status of the credential. | To be tested |
|  | DeleteSecretStage | Deletes the specified credential version status. | To be tested |
| Entrusted management | ShowAgency | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query agency details. | To be tested |
|  | CreateAgency | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create an agency. | To be tested |
| Event Management | UpdateSecretEvent | Updates the metadata of a specified event. The metadata that can be updated includes the event enabling status, basic type list, and notification subject. | To be tested |
|  | DeleteSecretEvent | The specified event is deleted immediately and cannot be restored. If the event has a credential reference, it cannot be deleted. Disassociate the event first. | To be tested |
|  | ListNotificationRecords | Query all triggered event notification records in the last three months. | To be tested |
|  | ListSecretEvents | Query all events created by the current user in the current project. | To be tested |
|  | CreateSecretEvent | Create an event. The event can be configured on one or more credential objects. When an event is enabled and the underlying event type is triggered on the credential object, the cloud service sends the event notification to the notification topic specified by the event. | To be tested |
|  | ShowSecretEvent | Query the information about a specified event. | To be tested |
| Key Authorization Management | ListGrants | -Function description: This API is used to query the authorized list of keys. | To be tested |
| Key Management | DeleteSecret |  | To be tested |
|  | ShowSecret |  | To be tested |
| Key management | UpdateSecret | Update a key | To be tested |
|  | ListSecrets | Query the list of keys | To be tested |
| Lifecycle Management | DeleteSecretForSchedule | Specify the deletion delay. Create a scheduled task for deleting credentials. The deletion delay can be set to a value ranging from 7 to 30 days. | To be tested |
|  | UploadSecretBlob | Recover the credential object by uploading the credential backup file | To be tested |
|  | RotateSecret | Recycle credentials immediately. Creates a new version of the credential in the specified credential, which is used to encrypt and store the credential values randomly generated in the background. Also marks the newly created credential version with the SYS/2000/state. | To be tested |
|  | BatchImportSecrets | Import credentials in batches. | To be tested |
|  | DownloadSecretBlob | Download the backup file of the specified credential | To be tested |
|  | RestoreSecret | Cancel the scheduled deletion task of the credential and restore the credential object to the available state. | To be tested |
| Password management | GenerateRandomPassword | Generate a random password | To be tested |
| TAG Function | ListResourceInstances | Query resource instances of a tenant by tag. | To be tested |
| Temporary login command | CreateSecret | Invoke this interface to obtain the value of X-Swr-Dockerlogin in the response message header and the value of host in the response message body to generate a temporary login command. | To be tested |
| User management | ShowUserDetail | Query user details based on the user ID. | To be tested |
|  | UpdateUserPassword | Change the user password | To be tested |

