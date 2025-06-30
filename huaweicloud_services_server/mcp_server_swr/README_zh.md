# SWR MCP Server 


## Version
v0.1.0

## Overview

SWR MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SWR. Full-chain management of SWR resources can be carried out based on natural language.

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
                    <td rowspan="2">临时登录指令</td>
                    <td>CreateAuthorizationToken</td>
                    <td>调用该接口,通过获取响应消息头的X-Swr-Dockerlogin的值及响应消息体的host值,可生成增强型登录指令,注:此接口只支持IAM新平面的调用方式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecret</td>
                    <td>调用该接口,通过获取响应消息头的X-Swr-Dockerlogin的值及响应消息体的host值,可生成临时登录指令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">共享帐号管理</td>
                    <td>UpdateRepoDomains</td>
                    <td>更新共享帐号</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRepoDomains</td>
                    <td>获取共享帐号列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRepoDomains</td>
                    <td>删除共享帐号</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAccessDomain</td>
                    <td>判断共享租户是否存在</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRepoDomains</td>
                    <td>创建共享帐号。镜像上传后,您可以共享私有镜像给其他帐号,并授予下载该镜像的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">其他</td>
                    <td>ShowShareFeatureGates</td>
                    <td>查询服务特性开关信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainOverview</td>
                    <td>获取租户总览信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainResourceReports</td>
                    <td>获取租户资源统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">查询版本操作</td>
                    <td>ShowApiVersion</td>
                    <td>查询指定的标签管理服务API版本号详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersions</td>
                    <td>查询标签管理服务的API版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">组织权限管理</td>
                    <td>ShowNamespaceAuth</td>
                    <td>查询组织权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNamespaceAuth</td>
                    <td>创建组织权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNamespaceAuth</td>
                    <td>更新组织权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNamespaceAuth</td>
                    <td>删除组织权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">组织管理</td>
                    <td>DeleteNamespaces</td>
                    <td>删除组织</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNamespace</td>
                    <td>创建组织</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNamespaces</td>
                    <td>查询组织列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNamespace</td>
                    <td>获取组织详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">视频流管理</td>
                    <td>UpdateRetention</td>
                    <td>此接口用于更新视频转储信息。创建的视频流默认没有转储信息,即视频数据不会保存。更新转储信息后可以将视频流保存到指定的存储媒介,如OBS。后续用户可以从OBS上获取到转储的视频。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">触发器管理</td>
                    <td>ListTriggersDetails</td>
                    <td>获取镜像仓库下的触发器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrigger</td>
                    <td>创建触发器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTrigger</td>
                    <td>更新触发器配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrigger</td>
                    <td>获取触发器详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrigger</td>
                    <td>删除触发器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额管理</td>
                    <td>ListQuotas</td>
                    <td>获取配额信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">镜像仓库管理</td>
                    <td>ListReposDetails</td>
                    <td>查询镜像仓库列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSharedReposDetails</td>
                    <td>查询共享镜像列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRepo</td>
                    <td>在组织下创建镜像仓库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRepo</td>
                    <td>删除组织下的镜像仓库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRepo</td>
                    <td>更新租户组织下的镜像概要信息,包括镜像类型、是否公有、描述信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRepository</td>
                    <td>查询镜像仓库概要信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">镜像同步管理</td>
                    <td>ListImageAutoSyncReposDetails</td>
                    <td>获取为当前镜像仓库所创建的所有自动同步任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateImageSyncRepo</td>
                    <td>创建镜像自动同步任务,帮助您把最新推送的镜像自动同步到其他区域镜像仓库内。 镜像自动同步帮助您把最新推送的镜像自动同步到其他区域镜像仓库内,后期镜像有更新时,目标仓库的镜像也会自动更新,但已有的镜像不会自动同步。已有镜像的同步需要手动操作,详情请参见手动同步镜像。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteImageSyncRepo</td>
                    <td>根据目标区域、目标组织删除指定的镜像自动同步任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateManualImageSyncRepo</td>
                    <td>对于镜像仓库已有的镜像,如果想在其他区域使用,需要手动触发镜像同步。 判断是否同步成功的方法如下:响应状态码为200,无报错信息,表示同步成功。通过SWR管理控制台或调用查询镜像仓库概要信息接口,在目标区域的目标组织下,若存在所同步的镜像版本表示同步成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSyncJob</td>
                    <td>创建镜像自动同步任务后,可以通过此接口查询该任务的状态,以判断是否同步成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">镜像权限管理</td>
                    <td>UpdateUserRepositoryAuth</td>
                    <td>更新镜像权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserRepositoryAuth</td>
                    <td>查询镜像权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUserRepositoryAuth</td>
                    <td>创建镜像权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUserRepositoryAuth</td>
                    <td>删除镜像权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">镜像版本管理</td>
                    <td>CreateRepoTag</td>
                    <td>创建镜像tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRepoTag</td>
                    <td>删除镜像仓库中指定tag的镜像</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRepositoryTags</td>
                    <td>查询镜像tag列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">镜像老化规则管理</td>
                    <td>DeleteRetention</td>
                    <td>删除镜像老化规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRetentions</td>
                    <td>获取镜像老化规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRetentionHistories</td>
                    <td>获取镜像老化记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRetention</td>
                    <td>创建镜像老化规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRetention</td>
                    <td>获取镜像老化规则记录</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
