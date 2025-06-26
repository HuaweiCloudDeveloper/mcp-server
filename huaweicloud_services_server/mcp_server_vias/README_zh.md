# VIAS MCP Server 


## Version
v0.1.0

## Overview

VIAS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service VIAS. Full-chain management of VIAS resources can be carried out based on natural language.

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
                    <td rowspan="4">IAlgorithmController</td>
                    <td>ShowServiceDetail</td>
                    <td>获取服务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopDeployAlgorithm</td>
                    <td>停止算法部署</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserServices</td>
                    <td>我的算法服务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeployAlgorithm</td>
                    <td>部署算法</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">IBatchTaskController</td>
                    <td>CreateBatchTask</td>
                    <td>新增批量任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBatchTask</td>
                    <td>删除批量配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBatchTasks</td>
                    <td>获取批量配置任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartStopTask</td>
                    <td>启动/停止批量配置任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBatchTask</td>
                    <td>修改批量配置任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">IEdgePoolController</td>
                    <td>CreateEdgePool</td>
                    <td>创建边缘资源池</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgePoolInfo</td>
                    <td>查询边缘资源池详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgePool</td>
                    <td>删除边缘资源池</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgePools</td>
                    <td>查询边缘资源池列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">ITaskController</td>
                    <td>ShowTaskInfo</td>
                    <td>用于获取视频智能分析任务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTask</td>
                    <td>删除单个任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTask</td>
                    <td>任务修改接口,用于修改任务配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTask</td>
                    <td>该接口用于创建任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartStopTask</td>
                    <td>该接口用于启动或停止任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTasks</td>
                    <td>获取任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">IVideoGroupController</td>
                    <td>ShowVideoGroupDetail</td>
                    <td>获取视频源分组详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVideoGroup</td>
                    <td>更新视频源分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVideoGroup</td>
                    <td>删除视频源分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVideoGroups</td>
                    <td>获取视频源分组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVideoGroup</td>
                    <td>创建视频源分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">IVideoSourceController</td>
                    <td>CreateVideoSource</td>
                    <td>创建视频源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVideoSources</td>
                    <td>获取视频源列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVideoSource</td>
                    <td>删除视频源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVideoSourceDetail</td>
                    <td>视频源详情展示</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVideoSource</td>
                    <td>修改视频源</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
