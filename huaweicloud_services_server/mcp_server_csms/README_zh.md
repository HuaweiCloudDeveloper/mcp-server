# CSMS MCP Server 

## 版本信息
v0.1.0

## 产品描述

CSMS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CSMS交互的能力。可以基于自然语言对CSMS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 事件管理 | UpdateSecretEvent | 更新指定事件的元数据信息。支持更新的元数据包含事件启用状态、基础类型列表、通知主题。 | To be tested |
|  | DeleteSecretEvent | 立即删除指定的事件,且无法恢复。如事件存在凭据引用,则无法删除,请先解除关联。 | To be tested |
|  | ListNotificationRecords | 查询三个月内所有已触发的事件通知记录。 | To be tested |
|  | ListSecretEvents | 查询当前用户在本项目下创建的所有事件。 | To be tested |
|  | CreateSecretEvent | 创建事件,事件可配置在一个或多个凭据对象上。当事件为启用状态且包含的基础事件类型在凭据对象上触发时,云服务会将对应的事件通知发送至事件指定的通知主题上。 | To be tested |
|  | ShowSecretEvent | 查询指定事件的信息。 | To be tested |
| 凭据标签管理 | CreateSecretTag | 添加凭据标签。 | To be tested |
|  | ListProjectSecretsTags | 查询用户在指定项目下的所有凭据标签集合。 | To be tested |
|  | DeleteSecretTag | 删除凭据标签。 | To be tested |
|  | BatchCreateOrDeleteTags | - 功能介绍:批量添加或删除凭据标签。 | To be tested |
|  | ListResourceInstances | 查询凭据实例。通过标签过滤,筛选用户凭据,返回凭据列表。 | To be tested |
|  | ListSecretTags | 查询凭据标签。 | To be tested |
| 凭据检测管理 | ShowSecretsConfig | 获取租户的凭据检测配置。 | To be tested |
|  | UpdateSecretsConfig | 更改获取租户的凭据检测配置。 | To be tested |
|  | CheckSecrets | 检测传入的凭据。 | To be tested |
| 凭据版本状态管理 | ShowSecretStage | 查询指定凭据版本状态标记的版本信息。 | To be tested |
|  | UpdateSecretStage | 更新凭据的版本状态。 | To be tested |
|  | DeleteSecretStage | 删除指定的凭据版本状态。 | To be tested |
| 凭据版本管理 | ListSecretVersions | 查询指定凭据下的版本列表信息。 | To be tested |
|  | ShowSecretVersion | 查询指定凭据版本的信息和版本中的明文凭据值,只能查询ENABLED状态的凭据。 | To be tested |
|  | UpdateVersion | 当前支持更新指定凭据版本的有效期,只能更新ENABLED状态的凭据。在关联订阅的事件包含“版本过期”基础事件类型时,每次更新版本有效期后仅会触发一次事件通知。 | To be tested |
|  | CreateSecretVersion | 在指定的凭据中,创建一个新的凭据版本,用于加密保管新的凭据值。默认情况下,新创建的凭据版本被标记为SYSCURRENT状态,而SYSCURRENT标记的前一个凭据版本被标记为SYSPREVIOUS状态。您可以通过指定VersionStage参数来覆盖默认行为。 | To be tested |
| 凭据轮转管理 | ShowSecretFunctionTemplates | 获取凭据轮转函数模板。 | To be tested |
|  | ShowAgency | 查看是否有服务委托 | To be tested |
|  | ListSecretTask | 查询任务列表。 | To be tested |
|  | CreateAgency | 创建服务委托。用于创建凭据管理服务相关委托和函数工作流相关委托。 | To be tested |
| 密码管理 | GenerateRandomPassword | 生成随机密码 | To be tested |
| 授权管理 | UpdateGrant | 更新授权 | To be tested |
|  | CreateGrants | 授权操作 | To be tested |
|  | ListGrants | 授权列表 | To be tested |
|  | DeleteGrant | 删除授权 | To be tested |
| 生命周期管理 | UpdateSecret | 更新指定凭据的元数据信息。 | To be tested |
|  | CreateSecret | 创建新的凭据,并将凭据值存入凭据的初始版本。 | To be tested |
|  | DeleteSecretForSchedule | 指定延迟删除时间,创建删除凭据的定时任务,可设置7~30天的的延迟删除时间。 | To be tested |
|  | UploadSecretBlob | 通过上传凭据备份文件,恢复凭据对象 | To be tested |
|  | ListSecrets | 查询当前用户在本项目下创建的所有凭据。 | To be tested |
|  | RotateSecret | 立即执行轮转凭据。在指定的凭据中,创建一个新的凭据版本,用于加密存储后台随机产生的凭据值。同时将新创建的凭据版本标记为SYSCURRENT状态。 | To be tested |
|  | BatchImportSecrets | 批量导入凭据。 | To be tested |
|  | DownloadSecretBlob | 下载指定凭据的备份文件 | To be tested |
|  | RestoreSecret | 取消凭据的定时删除任务,凭据对象恢复可使用状态。 | To be tested |
|  | DeleteSecret | 立即删除指定的凭据,且无法恢复。 | To be tested |
|  | ShowSecret | 查询指定凭据的信息。 | To be tested |
| 用户管理 | ShowUserDetail | 根据用户id查询用户详情。 | To be tested |
|  | ListUsers | 查询用户列表。 | To be tested |
|  | UpdateUserPassword | 修改用户密码 | To be tested |
