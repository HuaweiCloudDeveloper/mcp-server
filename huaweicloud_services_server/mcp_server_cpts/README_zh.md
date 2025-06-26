# CPTS MCP Server 


## Version
v0.1.0

## Overview

CPTS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CPTS. Full-chain management of CPTS resources can be carried out based on natural language.

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
                    <td>UpdateTask</td>
                    <td>任务修改接口,用于修改任务配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">PerfTest工程管理</td>
                    <td>DeleteProject</td>
                    <td>删除工程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProject</td>
                    <td>创建工程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProcess</td>
                    <td>查询导入进度</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectSets</td>
                    <td>查询工程集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProject</td>
                    <td>修改工程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProject</td>
                    <td>查询工程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">事务管理</td>
                    <td>CreateTemp</td>
                    <td>创建事务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTemp</td>
                    <td>查询事务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTempSet</td>
                    <td>查询事务集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTemp</td>
                    <td>删除事务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTemp</td>
                    <td>修改事务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">任务管理</td>
                    <td>CreateNewTask</td>
                    <td>创建任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskCases</td>
                    <td>获取任务关联的用例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskStatus</td>
                    <td>更新任务状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskSet</td>
                    <td>查询任务集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNewTask</td>
                    <td>删除任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskRelatedTestCase</td>
                    <td>修改任务关联用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateTaskStatus</td>
                    <td>批量启停任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">全局变量管理</td>
                    <td>DeleteVariable</td>
                    <td>删除全局变量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVariable</td>
                    <td>修改变量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVariable</td>
                    <td>创建变量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVariables</td>
                    <td>查询全局变量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">全链路压测管理</td>
                    <td>ShowAgentConfig</td>
                    <td>全链路压测探针获取配置信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAgentHealthStatus</td>
                    <td>全链路压测探针上报健康状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">报告管理</td>
                    <td>ShowReport</td>
                    <td>查询报告</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMergeTaskCase</td>
                    <td>查询任务报告的用例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMergeCaseDetail</td>
                    <td>查询用例报告详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHistoryRunInfo</td>
                    <td>查询PerfTest任务离线报告列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskCaseAwChart</td>
                    <td>查询用例的AW曲线图</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">服务作业管理</td>
                    <td>ShowTask</td>
                    <td>该接口用于查询服务作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">用例管理</td>
                    <td>CreateCase</td>
                    <td>创建用例(旧版)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNewCase</td>
                    <td>创建用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DebugCase</td>
                    <td>调试用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNewCase</td>
                    <td>删除用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCase</td>
                    <td>修改用例(旧版)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCase</td>
                    <td>删除用例(旧版)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCase</td>
                    <td>查询用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNewCase</td>
                    <td>修改用例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">目录管理</td>
                    <td>UpdateDirectory</td>
                    <td>修改目录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDirectory</td>
                    <td>删除目录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDirectory</td>
                    <td>创建目录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectTestCase</td>
                    <td>查询用例树</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
