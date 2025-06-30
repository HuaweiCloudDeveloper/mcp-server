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
                    <td rowspan="1">TAG功能</td>
                    <td>ListResourceInstances</td>
                    <td>使用标签过滤查询租户下资源的实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">临时登录指令</td>
                    <td>CreateSecret</td>
                    <td>调用该接口,通过获取响应消息头的X-Swr-Dockerlogin的值及响应消息体的host值,可生成临时登录指令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">事件管理</td>
                    <td>UpdateSecretEvent</td>
                    <td>更新指定事件的元数据信息。支持更新的元数据包含事件启用状态、基础类型列表、通知主题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecretEvent</td>
                    <td>立即删除指定的事件,且无法恢复。如事件存在凭据引用,则无法删除,请先解除关联。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotificationRecords</td>
                    <td>查询三个月内所有已触发的事件通知记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecretEvents</td>
                    <td>查询当前用户在本项目下创建的所有事件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecretEvent</td>
                    <td>创建事件,事件可配置在一个或多个凭据对象上。当事件为启用状态且包含的基础事件类型在凭据对象上触发时,云服务会将对应的事件通知发送至事件指定的通知主题上。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecretEvent</td>
                    <td>查询指定事件的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">凭据标签管理</td>
                    <td>CreateSecretTag</td>
                    <td>添加凭据标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectSecretsTags</td>
                    <td>查询用户在指定项目下的所有凭据标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecretTag</td>
                    <td>删除凭据标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecretTags</td>
                    <td>查询凭据标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">凭据检测管理</td>
                    <td>ShowSecretsConfig</td>
                    <td>获取租户的凭据检测配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecretsConfig</td>
                    <td>更改获取租户的凭据检测配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckSecrets</td>
                    <td>检测传入的凭据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">凭据版本状态管理</td>
                    <td>ShowSecretStage</td>
                    <td>查询指定凭据版本状态标记的版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecretStage</td>
                    <td>更新凭据的版本状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecretStage</td>
                    <td>删除指定的凭据版本状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">凭据版本管理</td>
                    <td>ListSecretVersions</td>
                    <td>查询指定凭据下的版本列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecretVersion</td>
                    <td>查询指定凭据版本的信息和版本中的明文凭据值,只能查询ENABLED状态的凭据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVersion</td>
                    <td>当前支持更新指定凭据版本的有效期,只能更新ENABLED状态的凭据。在关联订阅的事件包含“版本过期”基础事件类型时,每次更新版本有效期后仅会触发一次事件通知。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecretVersion</td>
                    <td>在指定的凭据中,创建一个新的凭据版本,用于加密保管新的凭据值。默认情况下,新创建的凭据版本被标记为SYSCURRENT状态,而SYSCURRENT标记的前一个凭据版本被标记为SYSPREVIOUS状态。您可以通过指定VersionStage参数来覆盖默认行为。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">凭据轮转管理</td>
                    <td>ShowSecretFunctionTemplates</td>
                    <td>获取凭据轮转函数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecretTask</td>
                    <td>查询任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">委托管理</td>
                    <td>ShowAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">密码管理</td>
                    <td>GenerateRandomPassword</td>
                    <td>生成随机密码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">密钥授权管理</td>
                    <td>ListGrants</td>
                    <td>- 功能介绍:查询密钥的授权列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">密钥管理</td>
                    <td>UpdateSecret</td>
                    <td>更新一个密钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecrets</td>
                    <td>查询密钥列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
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
                    <td rowspan="3">授权管理</td>
                    <td>UpdateGrant</td>
                    <td>更新授权</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGrants</td>
                    <td>授权操作</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGrant</td>
                    <td>删除授权</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">生命周期管理</td>
                    <td>DeleteSecretForSchedule</td>
                    <td>指定延迟删除时间,创建删除凭据的定时任务,可设置7~30天的的延迟删除时间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadSecretBlob</td>
                    <td>通过上传凭据备份文件,恢复凭据对象</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RotateSecret</td>
                    <td>立即执行轮转凭据。在指定的凭据中,创建一个新的凭据版本,用于加密存储后台随机产生的凭据值。同时将新创建的凭据版本标记为SYSCURRENT状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchImportSecrets</td>
                    <td>批量导入凭据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadSecretBlob</td>
                    <td>下载指定凭据的备份文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreSecret</td>
                    <td>取消凭据的定时删除任务,凭据对象恢复可使用状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">用户管理</td>
                    <td>ShowUserDetail</td>
                    <td>根据用户id查询用户详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserPassword</td>
                    <td>修改用户密码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">证书标签管理</td>
                    <td>BatchCreateOrDeleteTags</td>
                    <td>批量创建或删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资产管理</td>
                    <td>ListUsers</td>
                    <td>查询账号的服务器列表</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
