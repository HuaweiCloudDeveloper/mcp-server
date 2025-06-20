# SWR MCP Server 

## 版本信息
v0.1.0

## 产品描述

SWR MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务SWR交互的能力。可以基于自然语言对SWR资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| API版本信息 | ShowApiVersion | 查询指定API版本信息 | To be tested |
|  | ListApiVersions | 查询所有API版本信息 | To be tested |
| 临时登录指令 | CreateAuthorizationToken | 调用该接口,通过获取响应消息头的X-Swr-Dockerlogin的值及响应消息体的host值,可生成增强型登录指令,注:此接口只支持IAM新平面的调用方式。 | To be tested |
|  | CreateSecret | 调用该接口,通过获取响应消息头的X-Swr-Dockerlogin的值及响应消息体的host值,可生成临时登录指令。 | To be tested |
| 共享帐号管理 | UpdateRepoDomains | 更新共享帐号 | To be tested |
|  | ListRepoDomains | 获取共享帐号列表 | To be tested |
|  | DeleteRepoDomains | 删除共享帐号 | To be tested |
|  | ShowAccessDomain | 判断共享租户是否存在 | To be tested |
|  | CreateRepoDomains | 创建共享帐号。镜像上传后,您可以共享私有镜像给其他帐号,并授予下载该镜像的权限。 | To be tested |
| 其他 | ShowShareFeatureGates | 查询服务特性开关信息 | To be tested |
|  | ShowDomainOverview | 获取租户总览信息 | To be tested |
|  | ShowDomainResourceReports | 获取租户资源统计信息 | To be tested |
| 组织权限管理 | ShowNamespaceAuth | 查询组织权限 | To be tested |
|  | CreateNamespaceAuth | 创建组织权限 | To be tested |
|  | UpdateNamespaceAuth | 更新组织权限 | To be tested |
|  | DeleteNamespaceAuth | 删除组织权限 | To be tested |
| 组织管理 | DeleteNamespaces | 删除组织 | To be tested |
|  | CreateNamespace | 创建组织 | To be tested |
|  | ListNamespaces | 查询组织列表 | To be tested |
|  | ShowNamespace | 获取组织详情 | To be tested |
| 触发器管理 | ListTriggersDetails | 获取镜像仓库下的触发器列表 | To be tested |
|  | CreateTrigger | 创建触发器 | To be tested |
|  | UpdateTrigger | 更新触发器配置 | To be tested |
|  | ShowTrigger | 获取触发器详情 | To be tested |
|  | DeleteTrigger | 删除触发器 | To be tested |
| 配额管理 | ListQuotas | 获取配额信息 | To be tested |
| 镜像仓库管理 | ListReposDetails | 查询镜像仓库列表 | To be tested |
|  | ListSharedReposDetails | 查询共享镜像列表 | To be tested |
|  | CreateRepo | 在组织下创建镜像仓库。 | To be tested |
|  | DeleteRepo | 删除组织下的镜像仓库。 | To be tested |
|  | UpdateRepo | 更新租户组织下的镜像概要信息,包括镜像类型、是否公有、描述信息 | To be tested |
|  | ShowRepository | 查询镜像仓库概要信息 | To be tested |
| 镜像同步管理 | ListImageAutoSyncReposDetails | 获取为当前镜像仓库所创建的所有自动同步任务。 | To be tested |
|  | CreateImageSyncRepo | 创建镜像自动同步任务,帮助您把最新推送的镜像自动同步到其他区域镜像仓库内。 镜像自动同步帮助您把最新推送的镜像自动同步到其他区域镜像仓库内,后期镜像有更新时,目标仓库的镜像也会自动更新,但已有的镜像不会自动同步。已有镜像的同步需要手动操作,详情请参见手动同步镜像。 | To be tested |
|  | DeleteImageSyncRepo | 根据目标区域、目标组织删除指定的镜像自动同步任务。 | To be tested |
|  | CreateManualImageSyncRepo | 对于镜像仓库已有的镜像,如果想在其他区域使用,需要手动触发镜像同步。 判断是否同步成功的方法如下:响应状态码为200,无报错信息,表示同步成功。通过SWR管理控制台或调用查询镜像仓库概要信息接口,在目标区域的目标组织下,若存在所同步的镜像版本表示同步成功。 | To be tested |
|  | ShowSyncJob | 创建镜像自动同步任务后,可以通过此接口查询该任务的状态,以判断是否同步成功。 | To be tested |
| 镜像权限管理 | UpdateUserRepositoryAuth | 更新镜像权限 | To be tested |
|  | ShowUserRepositoryAuth | 查询镜像权限 | To be tested |
|  | CreateUserRepositoryAuth | 创建镜像权限 | To be tested |
|  | DeleteUserRepositoryAuth | 删除镜像权限 | To be tested |
| 镜像版本管理 | CreateRepoTag | 创建镜像tag | To be tested |
|  | DeleteRepoTag | 删除镜像仓库中指定tag的镜像 | To be tested |
|  | ListRepositoryTags | 查询镜像tag列表 | To be tested |
| 镜像老化规则管理 | DeleteRetention | 删除镜像老化规则 | To be tested |
|  | ListRetentions | 获取镜像老化规则列表 | To be tested |
|  | UpdateRetention | 修改镜像老化规则 | To be tested |
|  | ListRetentionHistories | 获取镜像老化记录 | To be tested |
|  | CreateRetention | 创建镜像老化规则 | To be tested |
|  | ShowRetention | 获取镜像老化规则记录 | To be tested |
