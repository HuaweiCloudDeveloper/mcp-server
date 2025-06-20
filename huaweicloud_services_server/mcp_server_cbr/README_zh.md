# CBR MCP Server 

## 版本信息
v0.1.0

## 产品描述

CBR MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CBR交互的能力。可以基于自然语言对CBR资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 任务 | ListOpLogs | 查询任务列表 | To be tested |
|  | ShowOpLog | 根据指定任务ID查询任务 | To be tested |
| 可保护性 | ShowReplicationCapabilities | 查询本区域的复制能力 | To be tested |
|  | ListProtectable | 查询可保护性资源列表 | To be tested |
|  | CheckAgent | 检查应用一致性Agent状态 | To be tested |
|  | ShowProtectable | 根据ID查询可保护性资源 | To be tested |
| 备份 | ShowBackup | 根据指定id查询单个副本。 | To be tested |
|  | DeleteBackup | 删除单个备份。 | To be tested |
|  | ImportBackup | 同步线下混合云VMware备份副本 | To be tested |
|  | ShowMetadata | 查询备份时资源的元数据 | To be tested |
|  | CopyBackup | 跨区域复制备份。 | To be tested |
|  | ListBackups | 查询所有副本 | To be tested |
|  | UpdateBackup | 根据备份id更改备份 | To be tested |
|  | RestoreBackup | 恢复备份数据 | To be tested |
| 备份共享 | AddMember | 添加备份可共享的成员,只有云服务器备份可以添加备份共享成员,且仅支持在同一区域的不同用户间共享。 | To be tested |
|  | ShowMembersDetail | 获取备份共享成员的列表信息 | To be tested |
|  | UpdateMemberStatus | 更新备份共享成员的状态,需要接收方执行此API。 | To be tested |
|  | DeleteMember | 删除指定的备份共享成员 | To be tested |
|  | ShowMemberDetail | 获取备份成员的详情 | To be tested |
| 存储库 | ShowVault | 根据ID查询指定存储库 | To be tested |
|  | UpdateVault | 根据存储库ID修改存储库 | To be tested |
|  | ListVault | 查询存储库列表 | To be tested |
|  | DisassociateVaultPolicy | 存储库解除策略 | To be tested |
|  | MigrateVaultResource | 支持资源迁移到另一个存储库,不删除备份。 | To be tested |
|  | BatchUpdateVault | 批量修改项目下所有存储库 | To be tested |
|  | DeleteVault | 删除存储库。若删除储存库,将一并删除存储库中的所有备份。 | To be tested |
|  | ListExternalVault | 查询其他区域的存储库列表 | To be tested |
|  | AssociateVaultPolicy | 存储库设置策略 | To be tested |
|  | CreatePostPaidVault | 创建包周期存储库 | To be tested |
|  | SetVaultResource | 设置存储库资源是否自动备份 | To be tested |
|  | ShowSummary | 查询项目下所有存储库的总容量和总使用量 | To be tested |
|  | RemoveVaultResource | 移除存储库中的资源,若移除资源,将一并删除该资源在保管库中的备份 | To be tested |
|  | CreateVault | 创建存储库 | To be tested |
|  | AddVaultResource | 存储库添加资源 | To be tested |
| 文件应用备份 | UpdateAgent | 修改客户端状态 | To be tested |
|  | UnregisterAgent | 移除客户端,移除客户端时将会删除该客户端所有备份,请谨慎操作。 | To be tested |
|  | RegisterAgent | 注册客户端,安装时候由Agent调用,无需手动注册。 | To be tested |
|  | ListAgent | 查询客户端列表 | To be tested |
|  | RemoveAgentPath | 移除已添加的文件备份路径。 | To be tested |
|  | ShowAgent | 查询指定客户端 | To be tested |
|  | AddAgentPath | 对客户端新增备份路径,新增的路径不会校验是否存在。 | To be tested |
| 标签 | DeleteVaultTag | 幂等接口:删除时,如果删除的标签不存在,返回404。Key不能为空或者空字符串。 | To be tested |
|  | ShowVaultTag | 查询指定实例的标签信息 | To be tested |
|  | CreateVaultTags | 一个资源上最多有10个标签。 | To be tested |
|  | ShowVaultResourceInstances | 使用标签过滤实例 | To be tested |
|  | ShowVaultProjectTag | 查询租户在指定Region和实例类型的所有标签集合 | To be tested |
|  | BatchCreateAndDeleteVaultTags | 为指定实例批量添加或删除标签 | To be tested |
| 策略 | ListPolicies | 查询策略列表 | To be tested |
|  | DeletePolicy | 删除策略 | To be tested |
|  | ShowPolicy | 查询单个策略 | To be tested |
|  | UpdatePolicy | 修改策略 | To be tested |
|  | CreatePolicy | 创建策略,策略分为备份策略和复制策略。 | To be tested |
| 组织策略 | DeleteOrganizationPolicy | 删除组织策略 | To be tested |
|  | ListOrganizationPolicyDetail | 查询组织策略每个账号下策略部署状态列表 | To be tested |
|  | ShowOrganizationPolicy | 查询指定组织策略 | To be tested |
|  | UpdateOrganizationPolicy | 更新组织策略 | To be tested |
|  | ListOrganizationPolicies | 查询组织策略列表 | To be tested |
|  | CreateOrganizationPolicy | 创建组织策略 | To be tested |
| 计量 | ShowStorageUsage | 查询容量统计 | To be tested |
| 运营 | ChangeVaultChargeMode | 修改资源的付费模式,暂时只支持按需资源转包周期资源。 | To be tested |
|  | UpdateOrder | 订单更新,支付cbc订单后,调用该接口更新包周期产品订单信息。该接口已废弃。 | To be tested |
|  | ChangeOrder | 订单更新,调用该接口更新包周期产品订单信息,返回待支付订单信息。 | To be tested |
| 还原点 | CreateCheckpoint | 对存储库执行备份,生成备份还原点 | To be tested |
|  | ImportCheckpoint | 针对vault同步备份副本 | To be tested |
|  | ShowCheckpoint | 根据还原点ID查询指定还原点 | To be tested |
|  | CopyCheckpoint | 执行复制 | To be tested |
| 项目 | ListDomainProjects | 根据指定租户名称查询项目列表。 | To be tested |
|  | ShowMigrateStatus | 查询迁移结果 | To be tested |
|  | ShowDomain | 由控制台调用的内部接口,用于仅在查询共享备份时获取源project_id的域名信息。 | To be tested |
|  | MigrateDomain | 将CSBS/VBS资源迁移到CBR。 | To be tested |
|  | ListProjects | 查询租户的企业项目信息 | To be tested |
