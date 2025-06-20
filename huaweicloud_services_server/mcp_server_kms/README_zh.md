# KMS MCP Server 

## 版本信息
v0.1.0

## 产品描述

KMS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务KMS交互的能力。可以基于自然语言对KMS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 专属密钥库管理 | DeleteKeyStore | 删除租户专属密钥库 | To be tested |
|  | ListKeyStores | 查询租户专属密钥库列表 | To be tested |
|  | CreateKeyStore | - "创建租户专属密钥库,专属密钥库使用DHSM实例作为密钥的存储" | To be tested |
|  | ShowKeyStore | 获取租户专属密钥库 | To be tested |
|  | EnableKeyStore | 启用租户专属密钥库 | To be tested |
|  | DisableKeyStore | 禁用租户专属密钥库 | To be tested |
| 别名管理 | ListAliases | 查询一个密钥关联的所有别名 | To be tested |
|  | CreateAlias |  | To be tested |
|  | AssociateAlias | 关联别名。 | To be tested |
|  | DeleteAlias | 删除别名 | To be tested |
| 多区域密钥 | UpdatePrimaryRegion | 修改密钥所属的主区域。修改后当前区域会变为副本区域。 | To be tested |
|  | ListSupportRegions | - 功能介绍:查询跨区域密钥所支持的区域。 | To be tested |
|  | ReplicateKey | 将本区域的密钥复制到指定区域。 | To be tested |
| 密钥授权管理 | CancelSelfGrant | - 功能介绍:退役授权,表示被授权用户不再具有授权密钥的操作权。 | To be tested |
|  | ListRetirableGrants | - 功能介绍:查询用户可以退役的授权列表。 | To be tested |
|  | CreateGrant | - 功能介绍:创建授权,被授权用户可以对授权密钥进行操作。 | To be tested |
|  | ListGrants | - 功能介绍:查询密钥的授权列表。 | To be tested |
|  | CancelGrant | - 功能介绍:撤销授权,授权用户撤销被授权用户操作密钥的权限。 | To be tested |
| 密钥查询 | ShowUserInstances | - 功能介绍:查询实例数,获取用户已经创建的用户主密钥数量。 | To be tested |
|  | ListKeys | - 功能介绍:查询用户所有密钥列表。 | To be tested |
|  | ListKeyDetail | - 功能介绍:查询密钥详细信息。 | To be tested |
|  | ShowPublicKey | - 查询用户指定非对称密钥的公钥信息。 | To be tested |
|  | ShowUserQuotas | - 功能介绍:查询配额,查询用户可以创建的用户主密钥配额总数及当前使用量信息。 | To be tested |
| 密钥标签管理 | ShowKmsTags | - 功能介绍:查询密钥标签。 | To be tested |
|  | ListKmsByTags | - 功能介绍:查询密钥实例。通过标签过滤,查询指定用户主密钥的详细信息。 | To be tested |
|  | BatchCreateKmsTags | - 功能介绍:批量添加删除密钥标签。 | To be tested |
|  | CreateKmsTag | - 功能介绍:添加密钥标签。 | To be tested |
|  | DeleteTag | - 功能介绍:删除密钥标签。 | To be tested |
|  | ListKmsTags | - 功能介绍:查询用户在指定项目下的所有标签集合。 | To be tested |
| 密钥生命周期管理 | UpdateKeyDescription | - 功能介绍:修改用户主密钥描述信息。 | To be tested |
|  | CancelKeyDeletion | - 功能介绍:取消计划删除密钥。 | To be tested |
|  | DeleteKey | - 功能介绍:计划多少天后删除密钥,可设置7天~1096天内删除密钥。 | To be tested |
|  | CreateKey | 创建用户主密钥,用户主密钥可以为对称密钥或非对称密钥。 | To be tested |
|  | DisableKey | - 功能介绍:禁用密钥,密钥禁用后不可以使用。 | To be tested |
|  | UpdateKeyAlias | - 功能介绍:修改用户主密钥别名。 | To be tested |
|  | EnableKey | - 功能介绍:启用密钥,密钥启用后才可以使用。 | To be tested |
| 密钥轮换管理 | DisableKeyRotation | - 功能介绍:关闭用户主密钥轮换。 | To be tested |
|  | ShowKeyRotationStatus | - 功能介绍:查询用户主密钥轮换状态。 | To be tested |
|  | EnableKeyRotation | - 功能介绍:开启用户主密钥轮换。 | To be tested |
|  | UpdateKeyRotationInterval | - 功能介绍:修改用户主密钥轮换周期。 | To be tested |
| 导入密钥管理 | CreateParametersForImport | - 功能介绍:获取导入密钥的必要参数,包括密钥导入令牌和密钥加密公钥。 | To be tested |
|  | ImportKeyMaterial | - 功能介绍:导入密钥材料。 | To be tested |
|  | DeleteImportedKeyMaterial | - 功能介绍:删除密钥材料信息。 | To be tested |
| 小数据加解密 | DecryptData | - 功能介绍:解密数据。 | To be tested |
|  | EncryptData | - 功能介绍:加密数据,用指定的用户主密钥加密数据。 | To be tested |
| 数据密钥管理 | DecryptDatakey | - 功能介绍:解密数据密钥,用指定的主密钥解密数据密钥。 | To be tested |
|  | CreateDatakey | - 功能介绍:创建数据密钥,返回结果包含明文和密文。 | To be tested |
|  | CreateRsaDatakeyPair | - 功能介绍:创建rsa数据密钥对,返回结果包含明文公钥和密文私钥,根据参数决定是否返回明文私钥。 | To be tested |
|  | CreateRandom | - 功能介绍: | To be tested |
|  | EncryptDatakey | - 功能介绍:加密数据密钥,用指定的主密钥加密数据密钥。 | To be tested |
|  | CreateEcDatakeyPair | - 功能介绍:创建EC数据密钥对,返回结果包含明文公钥和密文私钥,根据参数决定是否返回明文私钥。 | To be tested |
|  | CreateDatakeyWithoutPlaintext | - 功能介绍:创建数据密钥,返回结果只包含密文。 | To be tested |
| 查询密钥API版本信息 | ShowVersion | - 功能介绍:查指定API版本信息。 | To be tested |
|  | ShowVersions | - 功能介绍:查询API版本信息列表。 | To be tested |
| 消息验证码 | VerifyMac | 功能介绍:校验消息验证码 | To be tested |
|  | GenerateMac | 功能介绍:生成消息验证码 | To be tested |
| 签名验签 | Sign | - 功能介绍:使用非对称密钥的私钥对消息或消息摘要进行数字签名。 | To be tested |
|  | ValidateSignature | - 功能介绍:使用非对称密钥的私钥对消息或消息摘要进行签名验证。 | To be tested |
