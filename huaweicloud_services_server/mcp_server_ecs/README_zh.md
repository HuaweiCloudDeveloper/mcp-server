# ECS MCP Server 

## 版本信息
v0.1.0

## 产品描述

ECS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务ECS交互的能力。可以基于自然语言对ECS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 云服务器操作管理 | NovaListServerActions | 查询弹性云服务器的所有历史操作,显示操作行为列表。 | To be tested |
|  | NovaShowServerAction | 查询弹性云服务器的某个请求行为。 | To be tested |
| 云服务器组管理 | CreateServerGroup | 创建弹性云服务器组。 | To be tested |
|  | ListServerGroups | 查询弹性云服务器组。 | To be tested |
|  | ShowServerGroup | 查询弹性云服务器组详情。 | To be tested |
|  | NovaDeleteServerGroup | 删除云服务器组。 | To be tested |
|  | AddServerGroupMember | 将云服务器加入云服务器组。添加成功后,如果该云服务器组是反亲和性策略的,则该云服务器与云服务器组中的其他成员尽量分散地创建在不同主机上。如果该云服务器时故障域类型的,则该云服务器会拥有故障域属性。 | To be tested |
|  | NovaListServerGroups | 查询云服务器组列表。 | To be tested |
|  | NovaCreateServerGroup | 创建弹性云服务器组。 | To be tested |
|  | DeleteServerGroupMember | 将弹性云服务器移出云服务器组。移出后,该云服务器与云服务器组中的成员不再遵从反亲和策略。 | To be tested |
|  | NovaShowServerGroup | 查询云服务器组详情。 | To be tested |
|  | DeleteServerGroup | 删除云服务器组。 | To be tested |
| 元数据管理 | NovaUpdateServerMetadataItem | 设置云服务器指定key的元数据。 | To be tested |
|  | NovaShowServerMetadata | 查询弹性云服务器的元数据信息。 | To be tested |
|  | DeleteServerMetadata | 删除云服务器指定元数据。 | To be tested |
|  | NovaShowServerMetadataItem | 获取云服务器指定key的元数据信息。 | To be tested |
|  | NovaUpdateServerMetadata | 更新云服务器元数据。 | To be tested |
|  | UpdateServerMetadata | 更新云服务器元数据。 | To be tested |
|  | NovaCreateServerMetadata | 设置弹性云服务器的元数据信息。 | To be tested |
|  | NovaDeleteServerMetadataItem | 删除云服务器指定元数据。 | To be tested |
| 可用区管理 | ListServerAzInfo | 查询可用区列表 | To be tested |
|  | NovaListAvailabilityZones | 查询可用域列表。 | To be tested |
| 安全组管理 | NovaDisassociateSecurityGroup | 移除弹性云服务器中的安全组。 | To be tested |
|  | NovaAssociateSecurityGroup | 为弹性云服务器添加一个安全组。 | To be tested |
|  | NovaListServerSecurityGroups | 查询指定弹性云服务器的安全组。 | To be tested |
| 密钥密码管理 | NovaDeleteKeypair | 根据SSH密钥的名称,删除指定SSH密钥。 | To be tested |
|  | NovaCreateKeypair | 创建SSH密钥,或把公钥导入系统,生成密钥对。 | To be tested |
|  | ResetServerPassword | 重置弹性云服务器管理帐号(root用户或Administrator用户)的密码。 | To be tested |
|  | ShowResetPasswordFlag | 查询弹性云服务器是否支持一键重置密码。 | To be tested |
|  | NovaListKeypairs | 查询SSH密钥信息列表。 | To be tested |
|  | DeleteServerPassword | 清除Windows云服务器初始安装时系统生成的密码记录。清除密码后,不影响云服务器密码登录功能,但不能再使用获取密码功能来查询该云服务器密码。 | To be tested |
|  | ShowServerPassword | 当通过支持Cloudbase-init功能的镜像创建Windows云服务器时,获取云服务器初始安装时系统生成的管理员帐户(Administrator帐户或Cloudbase-init设置的帐户)随机密码。 | To be tested |
|  | NovaShowKeypair | 根据SSH密钥名称查询指定SSH密钥。 | To be tested |
| 批量操作 | BatchResetServersPassword | 批量重置弹性云服务器管理帐号(root用户或Administrator用户)的密码。 | To be tested |
|  | BatchStopServers | 根据给定的云服务器ID列表,批量关闭云服务器,一次最多可以关闭1000台。 | To be tested |
|  | BatchRebootServers | 根据给定的云服务器ID列表,批量重启云服务器,一次最多可以重启1000台。 | To be tested |
|  | BatchStartServers | 根据给定的云服务器ID列表,批量启动云服务器,一次最多可以启动1000台。 | To be tested |
|  | BatchUpdateServersName | 批量修改弹性云服务器信息。 | To be tested |
|  | BatchAttachSharableVolumes | 将指定的共享磁盘一次性挂载到多个弹性云服务器,实现批量挂载。 | To be tested |
| 查询API版本信息 | NovaListVersions | 返回Nova当前所有可用的版本。 | To be tested |
|  | NovaShowVersion | 返回指定版本的信息。 | To be tested |
| 查询Job状态 | ShowJob | 查询Job的执行状态。 | To be tested |
| 标签管理 | ListServerTags | 项目(Project)用于将OpenStack的资源(计算资源、存储资源和网络资源)进行分组和隔离。项目可以是一个部门或者一个项目组。一个帐户中可以创建多个项目。 | To be tested |
|  | BatchDeleteServerTags | - 为指定云服务器批量删除标签。 | To be tested |
|  | ShowServerTags | - 查询指定云服务器的标签信息。 | To be tested |
|  | BatchCreateServerTags | - 为指定云服务器批量添加标签。 | To be tested |
| 状态管理 | ResizePostPaidServer | 当您创建的弹性云服务器规格无法满足业务需要时,可以变更云服务器规格,升级vCPU、内存。具体接口的使用,请参见本节内容。 | To be tested |
|  | NovaUnlockServer | 解锁弹性云服务器。 | To be tested |
|  | ReinstallServerWithCloudInit | 重装弹性云服务器的操作系统。支持弹性云服务器数据盘不变的情况下,使用原镜像重装系统盘。 | To be tested |
|  | NovaStartServer | 启动单台云服务器。 | To be tested |
|  | ChangeServerOsWithoutCloudInit | 切换弹性云服务器操作系统。 | To be tested |
|  | NovaLockServer | 锁定弹性云服务器。 | To be tested |
|  | RegisterServerMonitor | 将云服务器添加到监控表中。 | To be tested |
|  | ReinstallServerWithoutCloudInit | 重装弹性云服务器的操作系统。 | To be tested |
|  | ShowServerRemoteConsole | 获取弹性云服务器VNC远程登录地址。 | To be tested |
|  | MigrateServer | - 将部署在专属主机上的弹性云服务器迁移至其他专属主机。 | To be tested |
|  | UpdateServerAutoTerminateTime | 修改按需服务器,设置定时删除时间。如果设置的定时删除时间为空字符串,表示取消定时删除。 | To be tested |
|  | ChangeServerChargeMode | 更换云服务器的计费模式 | To be tested |
|  | NovaStopServer | 关闭单台云服务器。 | To be tested |
|  | ResizeServer | 变更云服务器规格。 | To be tested |
|  | NovaRebootServer | 重启单台云服务器。 | To be tested |
|  | ChangeServerOsWithCloudInit | 切换弹性云服务器操作系统。支持弹性云服务器数据盘不变的情况下,使用新镜像重装系统盘。 | To be tested |
| 生命周期管理 | ListCloudServers | 查询云服务器列表接口。 | To be tested |
|  | NovaListServersDetails | 查询云服务器详情信息列表。 | To be tested |
|  | CreateServers | 创建一台或多台云服务器。 | To be tested |
|  | NovaUpdateServer | 修改云服务器信息,目前支持修改云服务器名称及描述。 | To be tested |
|  | NovaShowServer | 根据云服务器ID,查询云服务器的详细信息。 | To be tested |
|  | UpdateServer | 修改云服务器信息,目前支持修改云服务器名称及描述和hostname。 | To be tested |
|  | CreatePostPaidServers | 创建一台或多台[按需付费](https://support.huaweicloud.com/productdesc-ecs/ecs_01_0065.html)方式的云服务器。 | To be tested |
|  | ShowServer | 查询弹性云服务器的详细信息。 | To be tested |
|  | NovaCreateServers | 创建一台弹性云服务器。 | To be tested |
|  | NovaListServers | 查询云服务器信息列表。 | To be tested |
|  | ListServersDetails | 根据用户请求条件从数据库筛选、查询所有的弹性云服务器,并关联相关表获取到弹性云服务器的详细信息。 | To be tested |
|  | DeleteServers | 根据指定的云服务器ID列表,删除云服务器。 | To be tested |
|  | NovaDeleteServer | 删除一台云服务器。 | To be tested |
| 磁盘管理 | NovaAttachVolume | 弹性云服务器挂载磁盘。 | To be tested |
|  | NovaListServerVolumes | 查询弹性云服务器挂载的磁盘信息。 | To be tested |
|  | DetachServerVolume | 从弹性云服务器中卸载磁盘。 | To be tested |
|  | AttachServerVolume | 把磁盘挂载到弹性云服务器上。 | To be tested |
|  | NovaDetachVolume | 弹性云服务器卸载磁盘。 | To be tested |
|  | ListServerBlockDevices | 查询弹性云服务器挂载的磁盘信息。 | To be tested |
|  | ListServerVolumeAttachments | 查询弹性云服务器挂载的磁盘信息。 | To be tested |
|  | ShowServerBlockDevice | 查询弹性云服务器挂载的单个磁盘信息。 | To be tested |
|  | UpdateServerBlockDevice | 修改云服务器云主机挂载的单个磁盘信息。'当前仅支持修改delete_on_termination字段。 | To be tested |
|  | NovaShowServerVolume | 根据磁盘ID,查询云服务器挂载的单个磁盘信息。 | To be tested |
| 租户配额管理 | ShowServerLimits | 查询租户配额信息。 | To be tested |
| 网卡管理 | NovaDetachInterface | 根据指定的Port ID,从云服务器中卸载网卡。 | To be tested |
|  | BatchDeleteServerNics | 卸载并删除云服务器中的一张或多张网卡。 | To be tested |
|  | NovaAttachInterface | 给云服务器添加一张网卡。 | To be tested |
|  | UpdateServerInterface | 更新云服务器网卡挂载信息。 | To be tested |
|  | DisassociateServerVirtualIp | 虚拟IP地址用于为网卡提供第二个IP地址,同时支持与多个弹性云服务器的网卡绑定,从而实现多个弹性云服务器之间的高可用性。 | To be tested |
|  | BatchAddServerNics | 给云服务器添加一张或多张网卡。 | To be tested |
|  | ChangeVpc | 云服务器切换虚拟私有云。 | To be tested |
|  | NovaListServerInterfaces | 查询云服务器网卡信息。 | To be tested |
|  | ListServerInterfaces | 查询云服务器网卡信息。 | To be tested |
|  | AssociateServerVirtualIp | 虚拟IP地址用于为网卡提供第二个IP地址,同时支持与多个弹性云服务器的网卡绑定,从而实现多个弹性云服务器之间的高可用性。 | To be tested |
|  | NovaShowServerInterface | 根据网卡ID,查询云服务器网卡信息。 | To be tested |
|  | ChangeServerNetworkInterface | 更新云服务器指定网卡属性,当前仅支持更新网卡IP。 | To be tested |
| 规格管理 | ListFlavorSellPolicies | 查询规格销售策略。 | To be tested |
|  | NovaListFlavors | 查询系统中可用的弹性云服务器规格列表。 | To be tested |
|  | NovaListFlavorsDetails | 查询云服务器规格信息列表。 | To be tested |
|  | ListFlavors | 查询云服务器规格详情信息和规格扩展信息列表。 | To be tested |
|  | NovaShowFlavor | 根据云服务器规格ID,查询云服务器规格详情信息。 | To be tested |
|  | ListResizeFlavors | 变更规格时,部分规格的云服务器之间不能互相变更。您可以通过本接口,通过指定弹性云服务器规格,查询该规格可以变更的规格列表。 | To be tested |
|  | NovaShowFlavorExtraSpecs | 查询指定的规格的详细信息。 | To be tested |
| 计划事件 | ListScheduledEvents | 查询计划事件列表 | To be tested |
