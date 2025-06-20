# CBH MCP Server 

## 版本信息
v0.1.0

## 产品描述

CBH MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CBH交互的能力。可以基于自然语言对CBH资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 云堡垒机信息查询 | SearchQuota | 查询云堡垒机配额信息。 | To be tested |
|  | ShowAvailableZoneInfo | 获取云堡垒机服务可用分区信息。 | To be tested |
|  | ShowNetworkConfiguration | 检查云堡垒机实例网络信息。 | To be tested |
|  | ListCbhInstance | 获取当前租户下的云堡垒机实例列表。 | To be tested |
|  | ListQuotaStatus | 获取当前租户所选择的可用分区、性能规格所对应的弹性云服务器是否可用。 | To be tested |
| 云堡垒机管理 | StopCbhInstance | 关闭云堡垒机实例。 | To be tested |
|  | ResetLoginMethod | 重置admin用户多因子认证方式。 | To be tested |
|  | UpgradeCbhInstance | 升级云堡垒机实例 | To be tested |
|  | InstallCbhEip | 云堡垒机实例绑定弹性公网IP | To be tested |
|  | UninstallCbhEip | 云堡垒机实例解绑弹性公网IP。 | To be tested |
|  | StartCbhInstance | 启动云堡垒机实例。 | To be tested |
|  | RestartCbhInstance | 重启云堡垒机实例。 | To be tested |
|  | ChangeInstanceNetwork | 修改云堡垒机实例网络。 | To be tested |
|  | ResetPassword | 修改云堡垒机实例web登录admin用户密码。 | To be tested |
| 可用区查询 | ListAvailableZones | 获取云堡垒机服务可用区信息。 | To be tested |
| 委托授权 | ShowAuthorization | 获取租户给云堡垒机服务委托授权信息。 | To be tested |
|  | RegisterAuthorization | 租户创建或取消云堡垒机服务的委托授权。 | To be tested |
| 操作管理 | ResetInstancePassword | 重置云堡垒机实例web登录admin用户密码。 | To be tested |
|  | ShowInstanceStatus | 获取堡垒机实例状态信息(未删除实例)。 | To be tested |
|  | LoginInstanceAdmin | 用户登录堡垒机实例admin的console。 | To be tested |
|  | LoginInstance | IAM用户登录堡垒机实例console。 | To be tested |
|  | RebootInstance | 重启云堡垒机实例。 | To be tested |
|  | ResizeInstance | 变更云堡垒机实例。 | To be tested |
|  | UpgradeInstance | 升级云堡垒机实例。 | To be tested |
|  | ShowOmUrl | 获取运维链接 | To be tested |
|  | DeleteInstance | 删除云堡垒机故障实例。 | To be tested |
|  | ResetInstanceLoginMethod | 重置堡垒机实例admin用户登录方式。 | To be tested |
|  | StopInstance | 关闭云堡垒机实例。 | To be tested |
|  | ListInstances | 获取当前租户下的堡垒机实例列表。 | To be tested |
|  | RollbackInstance | 回退升级的云堡垒机实例。 | To be tested |
|  | ChangeInstanceType | 修改单机堡垒机实例类型。 | To be tested |
|  | StartInstance | 启动云堡垒机实例。 | To be tested |
| 标签管理 | ListInstancesByTag | 使用标签过滤实例。 | To be tested |
|  | BatchCreateInstanceTag | 操作堡垒机实例资源标签。 | To be tested |
|  | ShowInstanceTags | 查询堡垒机实例资源的标签信息。 | To be tested |
|  | CountInstancesByTag | 统计符合标签条件的实例数量。 | To be tested |
|  | ListTags | 查询租户在项目中的资源标签集合。 | To be tested |
| 生命周期管理 | CreateInstance | 创建云堡垒机实例。 | To be tested |
| 网络管理 | UpdateInstanceSecurityGroup | 修改堡垒机实例安全组。 | To be tested |
|  | InstallInstanceEip | 云堡垒机实例绑定弹性公网IP。 | To be tested |
|  | UninstallInstanceEip | 为云堡垒机实例解绑弹性公网IP。 | To be tested |
|  | SwitchInstanceVpc | 切换堡垒机虚拟私有云 | To be tested |
| 获取IAM登录实例链接 | LoginCbh | 获取当前IAM用户登录堡垒机的免登录链接 | To be tested |
| 规格管理 | ListSpecifications | 查询云堡垒机规格信息。 | To be tested |
| 订单管理 | CreateCbh | 创建云堡垒机实例。(创建云堡垒机实例订单前,先调用此接口) | To be tested |
|  | CreateInstanceOrder | 创建云堡垒机实例订单。(调用此接口前先调用创建云堡垒机实例接口) | To be tested |
|  | ChangeInstanceOrder | 创建变更云堡垒机实例订单。(调用此接口前先调用创建变更云堡垒机实例任务接口,当前接口未开放) | To be tested |
| 配额管理 | ShowEcsQuota | 获取当前租户所选择的可用分区里的堡垒机ECS规格是否可用。 | To be tested |
|  | ShowQuota | 获取堡垒机实例配额信息。 | To be tested |
