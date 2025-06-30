# CSMS MCP Server 


## Version
v0.1.0

## Overview

CSMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CSMS. Full-chain management of CSMS resources can be carried out based on natural language.

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
                    <td rowspan="1">Asset Management</td>
                    <td>ListUsers</td>
                    <td>Query the server list of the account</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Authorization management</td>
                    <td>UpdateGrant</td>
                    <td>Update Authorization</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGrants</td>
                    <td>Authentication operation</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGrant</td>
                    <td>Delete an authorization</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Certificate Label Management</td>
                    <td>BatchCreateOrDeleteTags</td>
                    <td>Create or delete tags in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Credential Label Management</td>
                    <td>CreateSecretTag</td>
                    <td>Add a credential label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectSecretsTags</td>
                    <td>Query the set of all credential labels of a user in a specified project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecretTag</td>
                    <td>Delete the credential label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecretTags</td>
                    <td>Query the credential label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Credential Rotation Management</td>
                    <td>ShowSecretFunctionTemplates</td>
                    <td>Obtain the credential rotation function template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecretTask</td>
                    <td>Query the task list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Credential Version Management</td>
                    <td>ListSecretVersions</td>
                    <td>Query the version list under a specified credential.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecretVersion</td>
                    <td>Query the information about the specified credential version and the plaintext credential value in the version. Only the credentials in the Enabled state can be queried.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVersion</td>
                    <td>Currently, the validity period of a specified credential version can be updated. Only the credentials in the Enabled state can be updated. When the associated subscribed event contains the 'Version Expired' base event type, only one event notification is triggered after the version validity period is updated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecretVersion</td>
                    <td>In the specified credential, create a new credential version to encrypt the new credential value. By default, the newly created version of the credential is marked with the SYS/2000/present state, while the previous version of the credential for the SYS/2000/present tag is marked with the SYSPREVIVEIOUS state. You can override the default behavior by specifying the VersionStage parameter.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Credential detection management</td>
                    <td>ShowSecretsConfig</td>
                    <td>Obtain the credential detection configuration of the tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecretsConfig</td>
                    <td>Modify the configuration for detecting the tenant's credentials.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckSecrets</td>
                    <td>Detects incoming credentials.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Credential version status management</td>
                    <td>ShowSecretStage</td>
                    <td>Query the version information of the specified credential version status tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecretStage</td>
                    <td>Update the version status of the credential.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecretStage</td>
                    <td>Deletes the specified credential version status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Entrusted management</td>
                    <td>ShowAgency</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query agency details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgency</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Event Management</td>
                    <td>UpdateSecretEvent</td>
                    <td>Updates the metadata of a specified event. The metadata that can be updated includes the event enabling status, basic type list, and notification subject.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecretEvent</td>
                    <td>The specified event is deleted immediately and cannot be restored. If the event has a credential reference, it cannot be deleted. Disassociate the event first.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotificationRecords</td>
                    <td>Query all triggered event notification records in the last three months.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecretEvents</td>
                    <td>Query all events created by the current user in the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecretEvent</td>
                    <td>Create an event. The event can be configured on one or more credential objects. When an event is enabled and the underlying event type is triggered on the credential object, the cloud service sends the event notification to the notification topic specified by the event.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecretEvent</td>
                    <td>Query the information about a specified event.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Key Authorization Management</td>
                    <td>ListGrants</td>
                    <td>-Function description: This API is used to query the authorized list of keys.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Key Management</td>
                    <td>DeleteSecret</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecret</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Key management</td>
                    <td>UpdateSecret</td>
                    <td>Update a key</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecrets</td>
                    <td>Query the list of keys</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Lifecycle Management</td>
                    <td>DeleteSecretForSchedule</td>
                    <td>Specify the deletion delay. Create a scheduled task for deleting credentials. The deletion delay can be set to a value ranging from 7 to 30 days.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadSecretBlob</td>
                    <td>Recover the credential object by uploading the credential backup file</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RotateSecret</td>
                    <td>Recycle credentials immediately. Creates a new version of the credential in the specified credential, which is used to encrypt and store the credential values randomly generated in the background. Also marks the newly created credential version with the SYS/2000/state.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchImportSecrets</td>
                    <td>Import credentials in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadSecretBlob</td>
                    <td>Download the backup file of the specified credential</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreSecret</td>
                    <td>Cancel the scheduled deletion task of the credential and restore the credential object to the available state.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Password management</td>
                    <td>GenerateRandomPassword</td>
                    <td>Generate a random password</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TAG Function</td>
                    <td>ListResourceInstances</td>
                    <td>Query resource instances of a tenant by tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Temporary login command</td>
                    <td>CreateSecret</td>
                    <td>Invoke this interface to obtain the value of X-Swr-Dockerlogin in the response message header and the value of host in the response message body to generate a temporary login command.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">User management</td>
                    <td>ShowUserDetail</td>
                    <td>Query user details based on the user ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserPassword</td>
                    <td>Change the user password</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
