# SFSTurbo MCP Server 

## 版本信息
v0.1.0

## 产品描述

SFSTurbo MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务SFSTurbo交互的能力。可以基于自然语言对SFSTurbo资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 任务管理 | ShowJobDetail | 查询job的执行状态。 可用于查询SFS Turbo异步API的执行状态。例如:可使用调用创建并绑定ldap配置接口时返回的jobId,通过该接口查询job的执行状态。 | To be tested |
| 共享标签 | ListSharedTags | 查询租户所有共享的标签集合。 | To be tested |
|  | ShowSharedTags | 查询指定共享的所有标签信息。 | To be tested |
|  | CreateSharedTag | 指定共享添加一个标签。 | To be tested |
|  | BatchAddSharedTags | 指定共享批量添加标签。 | To be tested |
|  | DeleteSharedTag | 指定共享删除一个标签。当共享中不存在指定要删除的key时,接口调用将会返回404错误。 | To be tested |
|  | ListSharesByTag | 通过标签查询文件系统列表 | To be tested |
| 名称管理 | ChangeShareName | 修改文件系统名称 | To be tested |
| 存储联动管理 | ListHpcCacheTasks | 查询数据导入导出任务列表 | To be tested |
|  | UpdateObsTargetAttributes | 更新后端存储属性 | To be tested |
|  | DeleteHpcCacheTask | 删除数据导入导出任务 | To be tested |
|  | DeleteBackendTarget | 删除后端存储 | To be tested |
|  | CreateHpcCacheTask | 创建数据导入导出任务 | To be tested |
|  | ShowBackendTargetInfo | 获取后端存储详细信息 | To be tested |
|  | UpdateHpcShare | 更新文件系统冷数据淘汰时间 | To be tested |
|  | UpdateObsTargetPolicy | 更新后端存储自动同步策略 | To be tested |
|  | ListBackendTargets | 查询后端存储列表 | To be tested |
|  | ShowHpcCacheTask | 查询数据导入导出任务详情 | To be tested |
|  | CreateBackendTarget | 为SFS Turbo 文件系统绑定后端存储 | To be tested |
| 文件系统管理 | ShowFsTask | 获取文件系统异步任务详情。仅支持查询目录资源使用情况的任务,API请求路径的feature取值为dir-usage,以下简称为DU任务。 | To be tested |
|  | CreateFsTask | 创建文件系统异步任务,仅支持异步查询目录资源使用情况,API请求路径的feature取值为dir-usage,以下简称为DU任务。 | To be tested |
|  | SetHpcCacheBackend | 配置hpc缓存型后端信息 | To be tested |
|  | ListFsTasks | 获取文件系统异步任务列表。仅支持查询目录资源使用情况的任务,API请求路径的feature取值为dir-usage,以下简称为DU任务。 | To be tested |
|  | DeleteFsTask | 如果异步任务正在执行,则取消并删除任务;否则,删除任务。仅支持删除目录资源使用情况的任务,API请求路径的feature取值为dir-usage,以下简称为DU任务。 | To be tested |
| 权限管理 | CreateLdapConfig | 创建并绑定ldap配置。LDAP(Lightweight Directory Access Protocol),中文名称轻量级目录访问协议,是对目录服务器(Directory Server)进行访问、控制的一种标准协议。LDAP服务器可以集中式地管理用户和群组的归属关系,通过绑定LDAP服务器,当一个用户访问您的文件系统的文件时,SFS Turbo将会访问您的LDAP服务器以进行用户身份验证,并且获取用户和群组的归属关系,从而进行Linux标准的文件UGO权限的检查。要使用此功能,首先您需要搭建好LDAP服务器(当前SFS Turbo仅支持LDAP v3协议),常见提供LDAP协议访问的目录服务器实现有OpenLdap(Linux),Active Directory(Windows)等,不同目录服务器的实现细节有所差别,绑定时需要指定对应的Schema(Schema配置错误将会导致SFS Turbo无法正确获取用户以及群组信息,可能导致无权限访问文件系统内文件),当前SFS Turbo支持的Schema有: | To be tested |
|  | ShowLdapConfig | 查询Ldap的配置。LDAP(Lightweight Directory Access Protocol),中文名称轻量级目录访问协议,是对目录服务器(Directory Server)进行访问、控制的一种标准协议。LDAP服务器可以集中式地管理用户和群组的归属关系,通过绑定LDAP服务器,当一个用户访问您的文件系统的文件时,SFS Turbo将会访问您的LDAP服务器以进行用户身份验证,并且获取用户和群组的归属关系,从而进行Linux标准的文件UGO权限的检查。要使用此功能,首先您需要搭建好LDAP服务器(当前SFS Turbo仅支持LDAP v3协议),常见提供LDAP协议访问的目录服务器实现有OpenLdap(Linux),Active Directory(Windows)等,不同目录服务器的实现细节有所差别,绑定时需要指定对应的Schema(Schema配置错误将会导致SFS Turbo无法正确获取用户以及群组信息,可能导致无权限访问文件系统内文件),当前SFS Turbo支持的Schema有: | To be tested |
|  | UpdatePermRule | 修改权限规则 | To be tested |
|  | CreatePermRule | 创建权限规则 | To be tested |
|  | DeletePermRule | 删除权限规则 | To be tested |
|  | ShowPermRule | 查询文件系统的某一个权限规则 | To be tested |
|  | UpdateLdapConfig | 修改ldap配置。LDAP(Lightweight Directory Access Protocol),中文名称轻量级目录访问协议,是对目录服务器(Directory Server)进行访问、控制的一种标准协议。LDAP服务器可以集中式地管理用户和群组的归属关系,通过绑定LDAP服务器,当一个用户访问您的文件系统的文件时,SFS Turbo将会访问您的LDAP服务器以进行用户身份验证,并且获取用户和群组的归属关系,从而进行Linux标准的文件UGO权限的检查。要使用此功能,首先您需要搭建好LDAP服务器(当前SFS Turbo仅支持LDAP v3协议),常见提供LDAP协议访问的目录服务器实现有OpenLdap(Linux),Active Directory(Windows)等,不同目录服务器的实现细节有所差别,绑定时需要指定对应的Schema(Schema配置错误将会导致SFS Turbo无法正确获取用户以及群组信息,可能导致无权限访问文件系统内文件),当前SFS Turbo支持的Schema有: | To be tested |
|  | ListPermRules | 查询文件系统的权限规则列表 | To be tested |
|  | DeleteLdapConfig | 删除ldap配置。LDAP(Lightweight Directory Access Protocol),中文名称轻量级目录访问协议,是对目录服务器(Directory Server)进行访问、控制的一种标准协议。LDAP服务器可以集中式地管理用户和群组的归属关系,通过绑定LDAP服务器,当一个用户访问您的文件系统的文件时,SFS Turbo将会访问您的LDAP服务器以进行用户身份验证,并且获取用户和群组的归属关系,从而进行Linux标准的文件UGO权限的检查。要使用此功能,首先您需要搭建好LDAP服务器(当前SFS Turbo仅支持LDAP v3协议),常见提供LDAP协议访问的目录服务器实现有OpenLdap(Linux),Active Directory(Windows)等,不同目录服务器的实现细节有所差别,绑定时需要指定对应的Schema(Schema配置错误将会导致SFS Turbo无法正确获取用户以及群组信息,可能导致无权限访问文件系统内文件),当前SFS Turbo支持的Schema有: | To be tested |
| 生命周期管理 | ExpandShare | 扩容文件系统。 | To be tested |
|  | DeleteShare | 删除文件系统。 | To be tested |
|  | CreateShare | 创建文件系统。 | To be tested |
|  | ShowShare | 查询SFS Turbo文件系统详细信息。 | To be tested |
|  | ListShares | 获取文件系统列表 | To be tested |
| 目录管理 | UpdateFsDirQuota | 更新目标文件夹quota | To be tested |
|  | CreateFsDir | 创建目录 | To be tested |
|  | ShowFsDirUsage | 查询目录资源使用情况(包括子目录的资源)。后端有5min的缓存时间,查询的数据可能有延迟。 | To be tested |
|  | CreateFsDirQuota | 创建目标文件夹quota。 | To be tested |
|  | DeleteFsDir | 删除文件系统目录 | To be tested |
|  | ShowFsDir | 查询目录是否存在 | To be tested |
|  | ShowFsDirQuota | 查询目标文件夹quota。查询的used_capacity、used_inode数据可能有延迟。 | To be tested |
|  | DeleteFsDirQuota | 删除目标文件夹quota。 | To be tested |
| 连接管理 | ChangeSecurityGroup | 修改SFS Turbo文件系统绑定的安全组。修改安全组为异步任务,可以通过“查询单个文件系统”返回的子状态字段“sub_status”来判断是否修改安全组状态,子状态为“232”即为修改安全组成功。 | To be tested |
