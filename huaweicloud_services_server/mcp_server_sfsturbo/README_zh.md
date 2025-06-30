# SFSTurbo MCP Server 


## Version
v0.1.0

## Overview

SFSTurbo MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SFSTurbo. Full-chain management of SFSTurbo resources can be carried out based on natural language.

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
                    <td rowspan="1">任务管理</td>
                    <td>ShowJobDetail</td>
                    <td>查询job的执行状态。 可用于查询SFS Turbo异步API的执行状态。例如:可使用调用创建并绑定ldap配置接口时返回的jobId,通过该接口查询job的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">共享标签</td>
                    <td>ListSharedTags</td>
                    <td>查询租户所有共享的标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSharedTags</td>
                    <td>查询指定共享的所有标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSharedTag</td>
                    <td>指定共享添加一个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddSharedTags</td>
                    <td>指定共享批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSharedTag</td>
                    <td>指定共享删除一个标签。当共享中不存在指定要删除的key时,接口调用将会返回404错误。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSharesByTag</td>
                    <td>通过标签查询文件系统列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">名称管理</td>
                    <td>ChangeShareName</td>
                    <td>修改文件系统名称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">存储联动管理</td>
                    <td>ListHpcCacheTasks</td>
                    <td>查询数据导入导出任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateObsTargetAttributes</td>
                    <td>更新后端存储属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHpcCacheTask</td>
                    <td>删除数据导入导出任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackendTarget</td>
                    <td>删除后端存储</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHpcCacheTask</td>
                    <td>创建数据导入导出任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackendTargetInfo</td>
                    <td>获取后端存储详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHpcShare</td>
                    <td>更新文件系统冷数据淘汰时间</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateObsTargetPolicy</td>
                    <td>更新后端存储自动同步策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackendTargets</td>
                    <td>查询后端存储列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHpcCacheTask</td>
                    <td>查询数据导入导出任务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBackendTarget</td>
                    <td>为SFS Turbo 文件系统绑定后端存储</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">文件系统管理</td>
                    <td>ShowFsTask</td>
                    <td>获取文件系统异步任务详情。仅支持查询目录资源使用情况的任务,API请求路径的feature取值为dir-usage,以下简称为DU任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFsTask</td>
                    <td>创建文件系统异步任务,仅支持异步查询目录资源使用情况,API请求路径的feature取值为dir-usage,以下简称为DU任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetHpcCacheBackend</td>
                    <td>配置hpc缓存型后端信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFsTasks</td>
                    <td>获取文件系统异步任务列表。仅支持查询目录资源使用情况的任务,API请求路径的feature取值为dir-usage,以下简称为DU任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFsTask</td>
                    <td>如果异步任务正在执行,则取消并删除任务;否则,删除任务。仅支持删除目录资源使用情况的任务,API请求路径的feature取值为dir-usage,以下简称为DU任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">权限管理</td>
                    <td>CreateLdapConfig</td>
                    <td>创建并绑定ldap配置。LDAP(Lightweight Directory Access Protocol),中文名称轻量级目录访问协议,是对目录服务器(Directory Server)进行访问、控制的一种标准协议。LDAP服务器可以集中式地管理用户和群组的归属关系,通过绑定LDAP服务器,当一个用户访问您的文件系统的文件时,SFS Turbo将会访问您的LDAP服务器以进行用户身份验证,并且获取用户和群组的归属关系,从而进行Linux标准的文件UGO权限的检查。要使用此功能,首先您需要搭建好LDAP服务器(当前SFS Turbo仅支持LDAP v3协议),常见提供LDAP协议访问的目录服务器实现有OpenLdap(Linux),Active Directory(Windows)等,不同目录服务器的实现细节有所差别,绑定时需要指定对应的Schema(Schema配置错误将会导致SFS Turbo无法正确获取用户以及群组信息,可能导致无权限访问文件系统内文件),当前SFS Turbo支持的Schema有:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLdapConfig</td>
                    <td>查询Ldap的配置。LDAP(Lightweight Directory Access Protocol),中文名称轻量级目录访问协议,是对目录服务器(Directory Server)进行访问、控制的一种标准协议。LDAP服务器可以集中式地管理用户和群组的归属关系,通过绑定LDAP服务器,当一个用户访问您的文件系统的文件时,SFS Turbo将会访问您的LDAP服务器以进行用户身份验证,并且获取用户和群组的归属关系,从而进行Linux标准的文件UGO权限的检查。要使用此功能,首先您需要搭建好LDAP服务器(当前SFS Turbo仅支持LDAP v3协议),常见提供LDAP协议访问的目录服务器实现有OpenLdap(Linux),Active Directory(Windows)等,不同目录服务器的实现细节有所差别,绑定时需要指定对应的Schema(Schema配置错误将会导致SFS Turbo无法正确获取用户以及群组信息,可能导致无权限访问文件系统内文件),当前SFS Turbo支持的Schema有:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePermRule</td>
                    <td>修改权限规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePermRule</td>
                    <td>创建权限规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePermRule</td>
                    <td>删除权限规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPermRule</td>
                    <td>查询文件系统的某一个权限规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLdapConfig</td>
                    <td>修改ldap配置。LDAP(Lightweight Directory Access Protocol),中文名称轻量级目录访问协议,是对目录服务器(Directory Server)进行访问、控制的一种标准协议。LDAP服务器可以集中式地管理用户和群组的归属关系,通过绑定LDAP服务器,当一个用户访问您的文件系统的文件时,SFS Turbo将会访问您的LDAP服务器以进行用户身份验证,并且获取用户和群组的归属关系,从而进行Linux标准的文件UGO权限的检查。要使用此功能,首先您需要搭建好LDAP服务器(当前SFS Turbo仅支持LDAP v3协议),常见提供LDAP协议访问的目录服务器实现有OpenLdap(Linux),Active Directory(Windows)等,不同目录服务器的实现细节有所差别,绑定时需要指定对应的Schema(Schema配置错误将会导致SFS Turbo无法正确获取用户以及群组信息,可能导致无权限访问文件系统内文件),当前SFS Turbo支持的Schema有:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPermRules</td>
                    <td>查询文件系统的权限规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLdapConfig</td>
                    <td>删除ldap配置。LDAP(Lightweight Directory Access Protocol),中文名称轻量级目录访问协议,是对目录服务器(Directory Server)进行访问、控制的一种标准协议。LDAP服务器可以集中式地管理用户和群组的归属关系,通过绑定LDAP服务器,当一个用户访问您的文件系统的文件时,SFS Turbo将会访问您的LDAP服务器以进行用户身份验证,并且获取用户和群组的归属关系,从而进行Linux标准的文件UGO权限的检查。要使用此功能,首先您需要搭建好LDAP服务器(当前SFS Turbo仅支持LDAP v3协议),常见提供LDAP协议访问的目录服务器实现有OpenLdap(Linux),Active Directory(Windows)等,不同目录服务器的实现细节有所差别,绑定时需要指定对应的Schema(Schema配置错误将会导致SFS Turbo无法正确获取用户以及群组信息,可能导致无权限访问文件系统内文件),当前SFS Turbo支持的Schema有:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">生命周期管理</td>
                    <td>ExpandShare</td>
                    <td>扩容文件系统。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteShare</td>
                    <td>删除文件系统。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateShare</td>
                    <td>创建文件系统。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowShare</td>
                    <td>查询SFS Turbo文件系统详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListShares</td>
                    <td>获取文件系统列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">目录管理</td>
                    <td>UpdateFsDirQuota</td>
                    <td>更新目标文件夹quota</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFsDir</td>
                    <td>创建目录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFsDirUsage</td>
                    <td>查询目录资源使用情况(包括子目录的资源)。后端有5min的缓存时间,查询的数据可能有延迟。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFsDirQuota</td>
                    <td>创建目标文件夹quota。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFsDir</td>
                    <td>删除文件系统目录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFsDir</td>
                    <td>查询目录是否存在</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFsDirQuota</td>
                    <td>查询目标文件夹quota。查询的used_capacity、used_inode数据可能有延迟。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFsDirQuota</td>
                    <td>删除目标文件夹quota。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">连接管理</td>
                    <td>ChangeSecurityGroup</td>
                    <td>修改SFS Turbo文件系统绑定的安全组。修改安全组为异步任务,可以通过“查询单个文件系统”返回的子状态字段“sub_status”来判断是否修改安全组状态,子状态为“232”即为修改安全组成功。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
