# DGC MCP Server 


## Version
v0.1.0

## Overview

DGC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DGC. Full-chain management of DGC resources can be carried out based on natural language.

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
                    <td rowspan="1">Job管理</td>
                    <td>ShowJobStatus</td>
                    <td>查询job的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Resource</td>
                    <td>ListResources</td>
                    <td>返回当前租户下特定资源类型的资源,需要当前用户有rms:resources:list权限。比如查询云服务器,对应的RMS资源类型是ecs.cloudservers,其中provider为ecs,type为cloudservers。 RMS支持的服务和资源类型参见[支持的服务和区域](https://console.huaweicloud.com/eps/#/resources/supported)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">任务中心API</td>
                    <td>ListJobs</td>
                    <td>查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务,该API用于查询这些任务的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">任务管理</td>
                    <td>DeleteJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">作业相关的API</td>
                    <td>StopJobInstance</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobInstances</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSystemTasks</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunOnce</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportJobList</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreJobInstance</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobInstance</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFileInfo</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">作业管理接口</td>
                    <td>StopJob</td>
                    <td>在MRS集群中终止指定作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">实例管理</td>
                    <td>CreateJob</td>
                    <td>创建单个任务,根据请求参数不同,可以创建单个实时迁移、实时同步、实时灾备等任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateJob</td>
                    <td>更新租户指定ID任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">目标连接管理</td>
                    <td>CreateConnection</td>
                    <td>创建目标连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConnections</td>
                    <td>查询目标连接列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConnection</td>
                    <td>更新目标连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">脚本相关的API</td>
                    <td>ListScripts</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScriptResults</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteScript</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">资源相关的API</td>
                    <td>ShowResource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResource</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">连接相关的API</td>
                    <td>ImportConnections</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConnection</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnction</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportConnections</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像任务</td>
                    <td>ShowJob</td>
                    <td>该接口为扩展接口,主要用于查询异步接口执行情况,比如查询导出镜像任务的执行状态。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
