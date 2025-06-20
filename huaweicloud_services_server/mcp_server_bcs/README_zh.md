# BCS MCP Server 

## 版本信息
v0.1.0

## 产品描述

BCS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务BCS交互的能力。可以基于自然语言对BCS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| BCS监控 | ListBcsMetric | 该接口用于查询BCS服务的监控数据,可以指定相应的指标名称。 | To be tested |
|  | ListInstanceMetric | 该接口用于BCS组织实例监控数据详情。 | To be tested |
|  | ListBcsEventsStatistic | 该接口用于查询BCS服务的分段事件、告警统计数据,可以指定查询时的过滤条件。 | To be tested |
|  | ListEntityMetric | 该接口用于查询BCS组织的监控数据列表。 | To be tested |
|  | ListBcsEvents | 该接口用于查询BCS服务的事件、告警数据,可以指定查询时的过滤条件。 | To be tested |
| BCS管理 | ShowBlockchainDetail | 查询指定服务实例详细信息 | To be tested |
|  | CreateBlockchainCertByUserName | 通过用户名生成指定服务实例组织用户证书 | To be tested |
|  | ShowBlockchainNodes | 查询指定服务实例节点信息 | To be tested |
|  | DeleteChannel | 该接口用于BCS删除某个通道。仅支持删除空通道 | To be tested |
|  | UnfreezeCert | 解冻指定服务实例组织用户证书,解冻后需等待半分钟到一分钟左右生效 | To be tested |
|  | ShowBlockchainFlavors | 查询服务联盟链规格信息 | To be tested |
|  | ShowBlockchainStatus | 查询指定服务实例创建状态 | To be tested |
|  | BatchRemoveOrgsFromChannel | 该接口用于BCS组织退出某通道。 | To be tested |
|  | ListOpRecord | 查询异步操作结果 | To be tested |
|  | DownloadBlockchainCert | 下载指定服务实例相关证书 | To be tested |
|  | DeleteBlockchain | 删除bcs实例。包周期实例不支持 | To be tested |
|  | UpdateInstance | 修改实例的节点、组织,目前仅支持添加、删除节点(IEF模式不支持添加、删除节点),添加、删除组织,共4种类型,每次操作只可以操作一种类型。此接口不支持包周期模式; 注意注册IEF节点时,IEF节点名称长度应该为4-24位的字符 | To be tested |
|  | CreateNewBlockchain | 创建BCS服务实例,只支持按需创建 | To be tested |
|  | ListQuotas | 查询当前项目下BCS服务所有资源的配额信息 | To be tested |
|  | DownloadBlockchainSdkConfig | 下载指定服务实例SDK配置文件 | To be tested |
|  | FreezeCert | 冻结指定服务实例组织用户证书,冻结后需等待半分钟到一分钟左右生效 | To be tested |
|  | BatchRemovePeersFromChannel | 该接口用于BCS某个组织中的节点退出某通道。当节点为通道中最后一个节点时,需要使用组织退通道的接口来将通道中的最后一个节点退出。 | To be tested |
|  | BatchCreateChannels | 创建通道 | To be tested |
|  | ListBlockchainChannels | 查询指定服务实例通道信息 | To be tested |
|  | BatchAddPeersToChannel | peer节点加入通道,目前仅支持往一个通道中加入peer | To be tested |
|  | ListBlockchains | 查询当前项目下所有服务实例的简要信息 | To be tested |
| BCS联盟 | HandleUnionMemberQuitList | 被邀请方退出联盟 | To be tested |
|  | HandleNotification | 处理联盟邀请 | To be tested |
|  | BatchInviteMembersToChannel | 批量邀请联盟成员加入通道,此操作会向被邀请方发出邀请通知 | To be tested |
|  | ListNotifications | 获取全部通知 | To be tested |
|  | ListMembers | 获取联盟成员列表 | To be tested |
|  | DeleteMemberInvite | 可通过此接口批量取消邀请或删除对已退出或拒绝加入或解散的成员邀请信息 | To be tested |
