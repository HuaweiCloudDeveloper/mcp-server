# OMS MCP Server 


## Version
v0.1.0

## Overview

OMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service OMS. Full-chain management of OMS resources can be carried out based on natural language.

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
                    <td rowspan="3">ITaskController</td>
                    <td>DeleteTask</td>
                    <td>删除单个任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTask</td>
                    <td>该接口用于创建任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTasks</td>
                    <td>获取任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">云服务</td>
                    <td>ShowCloudType</td>
                    <td>查询所有支持的云厂商</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">区域</td>
                    <td>ShowRegionInfo</td>
                    <td>查询云厂商支持的reigon</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">同步任务</td>
                    <td>DeleteSyncTask</td>
                    <td>调用该接口删除同步任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSyncTaskStatistic</td>
                    <td>查询指定ID同步任务的接收同步请求对象数、同步成功对象数、同步失败对象数、同步跳过对象数、同步成功对象容量统计数据(目前只支持华北-北京四、华东-上海一地区)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSyncTask</td>
                    <td>创建同步任务,创建成功后,任务会被自动启动,不需要额外调用启动任务命令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSyncEvents</td>
                    <td>源端有对象需要进行同步时,调用该接口创建一个同步事件,系统将根据同步事件中包含的对象名称进行同步(目前只支持华北-北京四、华东-上海一地区)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopSyncTask</td>
                    <td>当同步任务处于同步中时,调用该接口停止任务(目前只支持华北-北京四、华东-上海一地区)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSyncTasks</td>
                    <td>查询用户名下所有同步任务信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartSyncTask</td>
                    <td>同步任务停止后,调用该接口以启动同步任务(目前只支持华北-北京四、华东-上海一地区)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSyncTask</td>
                    <td>查询指定ID的同步任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">服务作业管理</td>
                    <td>StopTask</td>
                    <td>该接口用于停止服务作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTask</td>
                    <td>该接口用于查询服务作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartTask</td>
                    <td>该接口用于启动服务作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询API版本信息</td>
                    <td>ShowApiInfo</td>
                    <td>查询对象存储迁移服务指定API版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询版本操作</td>
                    <td>ListApiVersions</td>
                    <td>查询标签管理服务的API版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">桶操作</td>
                    <td>ShowBucketRegion</td>
                    <td>查询桶对应的region</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBucketObjects</td>
                    <td>查询桶对象列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBucketList</td>
                    <td>查询桶列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckPrefix</td>
                    <td>检查前缀是否在源端桶中存在</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCdnInfo</td>
                    <td>查桶对应的CDN信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">迁移任务管理</td>
                    <td>BatchUpdateTasks</td>
                    <td>批量更新迁移任务,可指定单个迁移任务组下所有的迁移任务或通过迁移任务ID来执行。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBandwidthPolicy</td>
                    <td>当迁移任务未执行完成时,修改迁移任务的流量控制策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">迁移任务组管理</td>
                    <td>StopTaskGroup</td>
                    <td>当迁移任务组处于创建任务中或监控中时,调用该接口暂停指定迁移任务组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTaskGroup</td>
                    <td>删除指定的迁移任务组.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskGroup</td>
                    <td>当迁移任务组未执行完成时,修改迁移任务组的流量控制策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskGroup</td>
                    <td>获取指定id的taskgroup信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryTaskGroup</td>
                    <td>当迁移任务组处于迁移失败状态时,调用该接口重启指定id的迁移任务组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartTaskGroup</td>
                    <td>当迁移任务组处于暂停状态时,调用该接口启动指定id的迁移任务组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTaskGroup</td>
                    <td>创建迁移任务组,创建成功后,迁移任务组会自动创建迁移任务,不需要额外调用启动任务命令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskGroup</td>
                    <td>查询用户账户下的任务组信息</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
