# KMS MCP Server 


## Version
v0.1.0

## Overview

KMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service KMS. Full-chain management of KMS resources can be carried out based on natural language.

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
                    <td rowspan="4">Alias Management</td>
                    <td>ListAliases</td>
                    <td>Query all aliases associated with a key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlias</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateAlias</td>
                    <td>Associated alias.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlias</td>
                    <td>Delete alias</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Data key management</td>
                    <td>DecryptDatakey</td>
                    <td>-Function description: Decrypts a data key by using the specified master key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatakey</td>
                    <td>-Function introduction: This interface is used to create a data key. The returned result contains both plaintext and ciphertext.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRsaDatakeyPair</td>
                    <td>-Function description: This API is used to create an RSA data key pair. The returned result contains the public key in plaintext and private key in ciphertext. Whether to return the private key in plaintext is determined based on the parameter settings.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRandom</td>
                    <td>- Function description:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EncryptDatakey</td>
                    <td>- Function description: encrypts a DEK by using the specified master key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEcDatakeyPair</td>
                    <td>-Function description: This API is used to create an EC data key pair. The returned result contains the public key in plaintext and private key in ciphertext. Whether to return the private key in plaintext is determined based on the parameter settings.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatakeyWithoutPlaintext</td>
                    <td>-Function description: This API is used to create a data key. The returned result contains only ciphertext.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Dedicated Key Library Management</td>
                    <td>DeleteKeyStore</td>
                    <td>Delete a tenant's dedicated keystore</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeyStores</td>
                    <td>Query the dedicated keystore list of a tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKeyStore</td>
                    <td>- "Create a dedicated keystore for the tenant. The dedicated keystore uses the DHSM instance as the storage of keys</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKeyStore</td>
                    <td>Obtain the tenant's dedicated keystore</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableKeyStore</td>
                    <td>Enable the tenant-specific keystore</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableKeyStore</td>
                    <td>Disable the dedicated key store for the tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Import Key Management</td>
                    <td>CreateParametersForImport</td>
                    <td>-Function description: This interface is used to obtain the required parameters for importing a key, including the key import token and the public key for encrypting the key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportKeyMaterial</td>
                    <td>-Function introduction: Import key materials.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteImportedKeyMaterial</td>
                    <td>- Function description: This API is used to delete key material information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Key Authorization Management</td>
                    <td>CancelSelfGrant</td>
                    <td>-Function description: Retire the authorization, indicating that the authorized user no longer has the permission to operate the authorized key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRetirableGrants</td>
                    <td>-Function description: This interface is used to query the list of entitlements that can be retired by a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGrant</td>
                    <td>-Function introduction: This interface is used to create an authorization. Authorized users can perform operations on the authorization keys.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGrants</td>
                    <td>-Function description: This API is used to query the authorized list of keys.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelGrant</td>
                    <td>- Function description: This interface is used to revoke an authorized user's permission to operate keys.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Key Lifecycle Management</td>
                    <td>UpdateKeyDescription</td>
                    <td>- Function description: This API is used to modify the description of the customer master key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelKeyDeletion</td>
                    <td>- Function description: This API is used to cancel the scheduled deletion of a key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKey</td>
                    <td>-Function description: specifies the number of days after which the CMK is to be deleted. The value ranges from 7 days to 1096 days.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKey</td>
                    <td>Create a customer master key. The CMK can be a symmetric or asymmetric key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableKey</td>
                    <td>-Function description: This command is used to disable a key. A disabled key cannot be used.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKeyAlias</td>
                    <td>- Function description: This command is used to modify the alias of the customer master key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableKey</td>
                    <td>-Function description: Enable the key. The key can be used only after it is enabled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Key Tag Management</td>
                    <td>ShowKmsTags</td>
                    <td>-Function description: This interface is used to query the label of a CMK.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKmsByTags</td>
                    <td>-Function description: This interface is used to query a CMK instance. This interface is used to query details about a specified customer master key by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateKmsTags</td>
                    <td>-Function description: This command is used to add or delete tags for a batch of CMKs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKmsTag</td>
                    <td>-Function description: This command is used to add a key tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTag</td>
                    <td>- Function description: This API is used to delete a key tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKmsTags</td>
                    <td>-Function description: This interface is used to query all tag sets of a user in a specified project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Key query</td>
                    <td>ShowUserInstances</td>
                    <td>-Function description: This interface is used to query the number of instances and obtain the number of customer master key created by a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeys</td>
                    <td>-Function description: This interface is used to query the list of all keys of a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeyDetail</td>
                    <td>-Function introduction: This API is used to query details about a key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPublicKey</td>
                    <td>- This API is used to query the public key information of the user-specified asymmetric key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserQuotas</td>
                    <td>-Function description: This API is used to query the total number of customer master key quotas that can be created by a user and the current usage.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Key rotation management</td>
                    <td>DisableKeyRotation</td>
                    <td>- Function description: Disables customer master key rotation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKeyRotationStatus</td>
                    <td>-Function description: This command is used to query the customer master key rotation status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableKeyRotation</td>
                    <td>-Function description: customer master key rotation is enabled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKeyRotationInterval</td>
                    <td>- Function description: This API is used to modify the customer master key rotation period.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Message Verification Code</td>
                    <td>VerifyMac</td>
                    <td>Function description: Verify the message verification code.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GenerateMac</td>
                    <td>Function introduction: generating a message verification code</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Multi-area Key</td>
                    <td>UpdatePrimaryRegion</td>
                    <td>Change the primary region to which the key belongs. After the modification, the current area becomes the duplicate area.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSupportRegions</td>
                    <td>-Function description: This API is used to query the regions supported by the cross-region key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ReplicateKey</td>
                    <td>Copy the keys in the local area to the specified area.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Query the API version information about the CMK</td>
                    <td>ShowVersion</td>
                    <td>-Function description: This API is used to query the version information of a specified API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVersions</td>
                    <td>- Function description: This API is used to query the API version list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Signature verification</td>
                    <td>Sign</td>
                    <td>- Function description: Use the private key of the asymmetric key to digitally sign a message or message digest.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateSignature</td>
                    <td>- Function description: Use the private key of the asymmetric key to perform signature verification on the message or message digest.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Small data encryption/decryption</td>
                    <td>DecryptData</td>
                    <td>- Function description: Decrypts data.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EncryptData</td>
                    <td>- Function description: Encrypts data by using the specified customer master key.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
