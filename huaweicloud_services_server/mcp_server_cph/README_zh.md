# CPH MCP Server 

## 版本信息
v0.1.0

## 产品描述

CPH MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CPH交互的能力。可以基于自然语言对CPH资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| ADB命令 | RunShellCommand | 在云手机中执行shell命令。该接口为异步接口。 | To be tested |
|  | PushFile | 推送文件到云手机文件系统中。系统会将所指定的文件下载解压后,将解压后的内容全部推送到云手机的根目录下。只支持指定tar格式的文件进行推送,您需要将tar文件提前上传至您的OBS桶中。该接口为异步接口。接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。 | To be tested |
|  | InstallApk | 在云手机中安装apk。系统会将指定的apk文件下载后直接安装到云手机中。 | To be tested |
|  | UninstallApk | 在云手机中卸载apk。该接口为异步接口。 | To be tested |
|  | RunSyncCommand | 在云手机中同步执行命令并返回命令执行的输出信息,该接口仅支持adb shell命令的执行。1分钟内每个用户调用接口次数上限为6次,每个云手机允许执行命令超时时间为2秒,接口时间不超过30秒,执行云手机数越多,接口耗时相应越长。 | To be tested |
| 云手机服务器管理 | DeleteShareFiles | 删除共享存储目录中文件,该功能仅在支持共享存储的云手机规格上可实现。 | To be tested |
|  | PushShareApps | 推送应用tar文件至共享应用存储目录中,该功能仅在支持共享应用的云手机服务器上可实现。接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。 | To be tested |
|  | ChangeCloudPhoneServer | 切换云手机服务器, 支持您换一台新的云手机服务器。切换后服务器名称、服务器ID和服务器所在AZ与原服务器相同, 服务器计费保持不变。服务器切换的同时服务器上的手机重新创建,不保留用户数据。切换需要额外的资源和资源配额。 | To be tested |
|  | RestartCloudPhoneServer | 批量重启云手机服务器。 | To be tested |
|  | ShowCloudPhoneServerDetail | 根据server_id查询云手机服务器的详细信息。 | To be tested |
|  | ListCloudPhoneServers | 分页查询云手机服务器,云手机服务器列表按照创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在云手机服务器,则返回空列表。 | To be tested |
|  | ChangeCloudPhoneServerModel | 变更云手机服务器规格。接口调用成功后,大约2分钟左右规格会变更结束,在订单中心可以查看到变更的订单状态为成功,且查询服务器的详细信息,可以查看到服务器规格名称已经变成新的规格名称。 | To be tested |
|  | UpdateServerName | 根据serverId修改serverName。 | To be tested |
|  | ListShareFiles | 查询共享存储指定路径下的文件列表,该功能仅在支持共享存储的云手机规格上可实现。 | To be tested |
|  | DeleteShareApps | 在共享应用存储目录中删除共享应用,该功能仅在支持共享应用的云手机规格上可实现。 | To be tested |
|  | CreateNet2CloudPhoneServer | 购买云手机服务器,支持您复用已有的VPC网络管理云手机服务器,支持云手机服务器复用您已购买的共享带宽等资源。 | To be tested |
|  | PushShareFiles | 推送文件至共享存储目录中,该功能仅在支持共享存储的云手机规格上可实现。接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。 | To be tested |
|  | CreateCloudPhoneSingleServer | 该接口创建的服务器仅包含服务器和服务器的镜像,不包含云手机实例和镜像等内容。若需要创建包含云手机实例的服务器,请使用创建云手机服务器接口。 | To be tested |
|  | ListCloudPhoneServerModels | 查询云手机服务器的规格列表。 | To be tested |
| 任务管理 | ShowJob | 查询任务的执行状态。 | To be tested |
|  | ListJobs | 查询同一个request id下的任务。 | To be tested |
| 密钥管理 | UpdateKeypair | 修改连接云手机的密钥对。 | To be tested |
| 带宽管理 | ShowBandwidthDetail | 查询云手机使用的带宽信息,本接口只适用于使用系统定义网络的服务器。 | To be tested |
|  | UpdateBandwidth | 修改云手机使用的共享带宽大小,本接口只适用于使用系统定义网络的服务器。 | To be tested |
| 手机实例管理 | BatchShowPhoneConnectInfos | 获取云手机连接信息。 | To be tested |
|  | UpdateCloudPhoneProperty | 部分云手机属性开放更新能力,部分属性无法更新,部分属性需要重启手机生效,属性约束请云手机属性列表。如果手机处于异常状态,属性更新后需恢复手机状态为运行中才可生效。该接口为异步接口。 | To be tested |
|  | ExpandPhoneDataVolumeSize | 扩容云手机数据盘大小 | To be tested |
|  | ShowCloudPhoneDetail | 查询云手机的详细信息。 | To be tested |
|  | ListCloudPhones | 分页查询云手机,云手机列表按照创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在云手机,则返回空列表。 | To be tested |
|  | UpdatePhoneName | 根据phoneId修改phoneName。 | To be tested |
|  | RestartCloudPhone | 批量重启云手机,也可用于开启云手机。该接口为异步接口。 | To be tested |
|  | BatchExportCloudPhoneData | 批量导出云手机中的数据。该接口为异步接口。接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。 | To be tested |
|  | ResetCloudPhone | 批量重置云手机,将云手机恢复出厂设置。该接口为异步接口。 | To be tested |
|  | ImportTraffic | 手机流量路由修改。 | To be tested |
|  | StopCloudPhone | 批量关闭云手机。 | To be tested |
|  | ListCloudPhoneModels | 查询或统计云手机的规格列表。 | To be tested |
|  | ListCloudPhoneImages | 根据项目ID查询可用的手机镜像。 | To be tested |
|  | BatchImportCloudPhoneData | 批量恢复数据到云手机中。该接口为异步接口。接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。 | To be tested |
| 标签管理 | ListResourceInstances | 查询资源实例。 | To be tested |
|  | BatchCreateTags | 批量添加标签。 | To be tested |
|  | ListResourceTags | 查询资源标签列表。 | To be tested |
|  | BatchDeleteTags | 批量删除标签。 | To be tested |
|  | ListProjectTags | 查询租户在指定区域和资源类型的所有标签集合。 | To be tested |
| 编码服务管理 | ListEncodeServers | 查询编码服务列表。 | To be tested |
|  | RestartEncodeServer | 批量重启编码服务。 | To be tested |
| 自定义镜像管理 | ListImageMembers | 获取镜像已共享账号列表 | To be tested |
|  | UpdateImageMember | 用户收到共享镜像后,选择接受或拒绝共享镜像。未接受的共享镜像无法使用。 | To be tested |
|  | DeleteImage | 删除自定义镜像 | To be tested |
|  | AddImageMember | 镜像共享,共享镜像给指定账号。 | To be tested |
|  | ListImages | 查询自定义镜像列表 | To be tested |
|  | DeleteImageMember | 删除共享镜像 | To be tested |
