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
                    <td rowspan="6">专属密钥库管理</td>
                    <td>DeleteKeyStore</td>
                    <td>删除租户专属密钥库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeyStores</td>
                    <td>查询租户专属密钥库列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKeyStore</td>
                    <td>- "创建租户专属密钥库,专属密钥库使用DHSM实例作为密钥的存储"</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKeyStore</td>
                    <td>获取租户专属密钥库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableKeyStore</td>
                    <td>启用租户专属密钥库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableKeyStore</td>
                    <td>禁用租户专属密钥库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">别名管理</td>
                    <td>ListAliases</td>
                    <td>查询一个密钥关联的所有别名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlias</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateAlias</td>
                    <td>关联别名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlias</td>
                    <td>删除别名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">多区域密钥</td>
                    <td>UpdatePrimaryRegion</td>
                    <td>修改密钥所属的主区域。修改后当前区域会变为副本区域。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSupportRegions</td>
                    <td>- 功能介绍:查询跨区域密钥所支持的区域。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ReplicateKey</td>
                    <td>将本区域的密钥复制到指定区域。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">密钥授权管理</td>
                    <td>CancelSelfGrant</td>
                    <td>- 功能介绍:退役授权,表示被授权用户不再具有授权密钥的操作权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRetirableGrants</td>
                    <td>- 功能介绍:查询用户可以退役的授权列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGrant</td>
                    <td>- 功能介绍:创建授权,被授权用户可以对授权密钥进行操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGrants</td>
                    <td>- 功能介绍:查询密钥的授权列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelGrant</td>
                    <td>- 功能介绍:撤销授权,授权用户撤销被授权用户操作密钥的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">密钥查询</td>
                    <td>ShowUserInstances</td>
                    <td>- 功能介绍:查询实例数,获取用户已经创建的用户主密钥数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeys</td>
                    <td>- 功能介绍:查询用户所有密钥列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeyDetail</td>
                    <td>- 功能介绍:查询密钥详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPublicKey</td>
                    <td>- 查询用户指定非对称密钥的公钥信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserQuotas</td>
                    <td>- 功能介绍:查询配额,查询用户可以创建的用户主密钥配额总数及当前使用量信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">密钥标签管理</td>
                    <td>ShowKmsTags</td>
                    <td>- 功能介绍:查询密钥标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKmsByTags</td>
                    <td>- 功能介绍:查询密钥实例。通过标签过滤,查询指定用户主密钥的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateKmsTags</td>
                    <td>- 功能介绍:批量添加删除密钥标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKmsTag</td>
                    <td>- 功能介绍:添加密钥标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTag</td>
                    <td>- 功能介绍:删除密钥标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKmsTags</td>
                    <td>- 功能介绍:查询用户在指定项目下的所有标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">密钥生命周期管理</td>
                    <td>UpdateKeyDescription</td>
                    <td>- 功能介绍:修改用户主密钥描述信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelKeyDeletion</td>
                    <td>- 功能介绍:取消计划删除密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKey</td>
                    <td>- 功能介绍:计划多少天后删除密钥,可设置7天~1096天内删除密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKey</td>
                    <td>创建用户主密钥,用户主密钥可以为对称密钥或非对称密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableKey</td>
                    <td>- 功能介绍:禁用密钥,密钥禁用后不可以使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKeyAlias</td>
                    <td>- 功能介绍:修改用户主密钥别名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableKey</td>
                    <td>- 功能介绍:启用密钥,密钥启用后才可以使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">密钥轮换管理</td>
                    <td>DisableKeyRotation</td>
                    <td>- 功能介绍:关闭用户主密钥轮换。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKeyRotationStatus</td>
                    <td>- 功能介绍:查询用户主密钥轮换状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableKeyRotation</td>
                    <td>- 功能介绍:开启用户主密钥轮换。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKeyRotationInterval</td>
                    <td>- 功能介绍:修改用户主密钥轮换周期。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">导入密钥管理</td>
                    <td>CreateParametersForImport</td>
                    <td>- 功能介绍:获取导入密钥的必要参数,包括密钥导入令牌和密钥加密公钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportKeyMaterial</td>
                    <td>- 功能介绍:导入密钥材料。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteImportedKeyMaterial</td>
                    <td>- 功能介绍:删除密钥材料信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">小数据加解密</td>
                    <td>DecryptData</td>
                    <td>- 功能介绍:解密数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EncryptData</td>
                    <td>- 功能介绍:加密数据,用指定的用户主密钥加密数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">数据密钥管理</td>
                    <td>DecryptDatakey</td>
                    <td>- 功能介绍:解密数据密钥,用指定的主密钥解密数据密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatakey</td>
                    <td>- 功能介绍:创建数据密钥,返回结果包含明文和密文。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRsaDatakeyPair</td>
                    <td>- 功能介绍:创建rsa数据密钥对,返回结果包含明文公钥和密文私钥,根据参数决定是否返回明文私钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRandom</td>
                    <td>- 功能介绍:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EncryptDatakey</td>
                    <td>- 功能介绍:加密数据密钥,用指定的主密钥加密数据密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEcDatakeyPair</td>
                    <td>- 功能介绍:创建EC数据密钥对,返回结果包含明文公钥和密文私钥,根据参数决定是否返回明文私钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatakeyWithoutPlaintext</td>
                    <td>- 功能介绍:创建数据密钥,返回结果只包含密文。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">查询密钥API版本信息</td>
                    <td>ShowVersion</td>
                    <td>- 功能介绍:查指定API版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVersions</td>
                    <td>- 功能介绍:查询API版本信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">消息验证码</td>
                    <td>VerifyMac</td>
                    <td>功能介绍:校验消息验证码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GenerateMac</td>
                    <td>功能介绍:生成消息验证码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">签名验签</td>
                    <td>Sign</td>
                    <td>- 功能介绍:使用非对称密钥的私钥对消息或消息摘要进行数字签名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateSignature</td>
                    <td>- 功能介绍:使用非对称密钥的私钥对消息或消息摘要进行签名验证。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
