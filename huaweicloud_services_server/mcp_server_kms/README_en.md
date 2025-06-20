# KMS MCP Server 


## Version
v0.1.0

## Overview

KMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service KMS. Full-chain management of KMS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Alias Management | ListAliases | Query all aliases associated with a key. | To be tested |
|  | CreateAlias |  | To be tested |
|  | AssociateAlias | Associated alias. | To be tested |
|  | DeleteAlias | Delete alias | To be tested |
| Data key management | DecryptDatakey | -Function description: Decrypts a data key by using the specified master key. | To be tested |
|  | CreateDatakey | -Function introduction: This interface is used to create a data key. The returned result contains both plaintext and ciphertext. | To be tested |
|  | CreateRsaDatakeyPair | -Function description: This API is used to create an RSA data key pair. The returned result contains the public key in plaintext and private key in ciphertext. Whether to return the private key in plaintext is determined based on the parameter settings. | To be tested |
|  | CreateRandom | - Function description: | To be tested |
|  | EncryptDatakey | - Function description: encrypts a DEK by using the specified master key. | To be tested |
|  | CreateEcDatakeyPair | -Function description: This API is used to create an EC data key pair. The returned result contains the public key in plaintext and private key in ciphertext. Whether to return the private key in plaintext is determined based on the parameter settings. | To be tested |
|  | CreateDatakeyWithoutPlaintext | -Function description: This API is used to create a data key. The returned result contains only ciphertext. | To be tested |
| Dedicated Key Library Management | DeleteKeyStore | Delete a tenant's dedicated keystore | To be tested |
|  | ListKeyStores | Query the dedicated keystore list of a tenant | To be tested |
|  | CreateKeyStore | - "Create a dedicated keystore for the tenant. The dedicated keystore uses the DHSM instance as the storage of keys  | To be tested |
|  | ShowKeyStore | Obtain the tenant's dedicated keystore | To be tested |
|  | EnableKeyStore | Enable the tenant-specific keystore | To be tested |
|  | DisableKeyStore | Disable the dedicated key store for the tenant. | To be tested |
| Import Key Management | CreateParametersForImport | -Function description: This interface is used to obtain the required parameters for importing a key, including the key import token and the public key for encrypting the key. | To be tested |
|  | ImportKeyMaterial | -Function introduction: Import key materials. | To be tested |
|  | DeleteImportedKeyMaterial | - Function description: This API is used to delete key material information. | To be tested |
| Key Authorization Management | CancelSelfGrant | -Function description: Retire the authorization, indicating that the authorized user no longer has the permission to operate the authorized key. | To be tested |
|  | ListRetirableGrants | -Function description: This interface is used to query the list of entitlements that can be retired by a user. | To be tested |
|  | CreateGrant | -Function introduction: This interface is used to create an authorization. Authorized users can perform operations on the authorization keys. | To be tested |
|  | ListGrants | -Function description: This API is used to query the authorized list of keys. | To be tested |
|  | CancelGrant | - Function description: This interface is used to revoke an authorized user's permission to operate keys. | To be tested |
| Key Lifecycle Management | UpdateKeyDescription | - Function description: This API is used to modify the description of the customer master key.  | To be tested |
|  | CancelKeyDeletion | - Function description: This API is used to cancel the scheduled deletion of a key. | To be tested |
|  | DeleteKey | -Function description: specifies the number of days after which the CMK is to be deleted. The value ranges from 7 days to 1096 days. | To be tested |
|  | CreateKey | Create a customer master key. The CMK can be a symmetric or asymmetric key. | To be tested |
|  | DisableKey | -Function description: This command is used to disable a key. A disabled key cannot be used. | To be tested |
|  | UpdateKeyAlias | - Function description: This command is used to modify the alias of the customer master key.  | To be tested |
|  | EnableKey | -Function description: Enable the key. The key can be used only after it is enabled. | To be tested |
| Key Tag Management | ShowKmsTags | -Function description: This interface is used to query the label of a CMK. | To be tested |
|  | ListKmsByTags | -Function description: This interface is used to query a CMK instance. This interface is used to query details about a specified customer master key by label. | To be tested |
|  | BatchCreateKmsTags | -Function description: This command is used to add or delete tags for a batch of CMKs. | To be tested |
|  | CreateKmsTag | -Function description: This command is used to add a key tag. | To be tested |
|  | DeleteTag | - Function description: This API is used to delete a key tag. | To be tested |
|  | ListKmsTags | -Function description: This interface is used to query all tag sets of a user in a specified project. | To be tested |
| Key query | ShowUserInstances | -Function description: This interface is used to query the number of instances and obtain the number of customer master key created by a user. | To be tested |
|  | ListKeys | -Function description: This interface is used to query the list of all keys of a user. | To be tested |
|  | ListKeyDetail | -Function introduction: This API is used to query details about a key. | To be tested |
|  | ShowPublicKey | - This API is used to query the public key information of the user-specified asymmetric key. | To be tested |
|  | ShowUserQuotas | -Function description: This API is used to query the total number of customer master key quotas that can be created by a user and the current usage. | To be tested |
| Key rotation management | DisableKeyRotation | - Function description: Disables customer master key rotation. | To be tested |
|  | ShowKeyRotationStatus | -Function description: This command is used to query the customer master key rotation status. | To be tested |
|  | EnableKeyRotation | -Function description: customer master key rotation is enabled. | To be tested |
|  | UpdateKeyRotationInterval | - Function description: This API is used to modify the customer master key rotation period. | To be tested |
| Message Verification Code | VerifyMac | Function description: Verify the message verification code. | To be tested |
|  | GenerateMac | Function introduction: generating a message verification code | To be tested |
| Multi-area Key | UpdatePrimaryRegion | Change the primary region to which the key belongs. After the modification, the current area becomes the duplicate area. | To be tested |
|  | ListSupportRegions | -Function description: This API is used to query the regions supported by the cross-region key. | To be tested |
|  | ReplicateKey | Copy the keys in the local area to the specified area. | To be tested |
| Query the API version information about the CMK | ShowVersion | -Function description: This API is used to query the version information of a specified API. | To be tested |
|  | ShowVersions | - Function description: This API is used to query the API version list. | To be tested |
| Signature verification | Sign | - Function description: Use the private key of the asymmetric key to digitally sign a message or message digest. | To be tested |
|  | ValidateSignature | - Function description: Use the private key of the asymmetric key to perform signature verification on the message or message digest. | To be tested |
| Small data encryption/decryption | DecryptData | - Function description: Decrypts data. | To be tested |
|  | EncryptData | - Function description: Encrypts data by using the specified customer master key. | To be tested |

