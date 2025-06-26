# CodeArtsCheck MCP Server 


## Version
v0.1.0

## Overview

CodeArtsCheck MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeArtsCheck. Full-chain management of CodeArtsCheck resources can be carried out based on natural language.

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
                    <td rowspan="2">ITaskController</td>
                    <td>CreateTask</td>
                    <td>该接口用于创建任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTask</td>
                    <td>删除单个任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">任务管理</td>
                    <td>ShowTasksRulesets</td>
                    <td>查询任务的已选规则集列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskListByProjectId</td>
                    <td>根据DEVCLOUD_PROJECT_UUID查询该项目下的任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckRecord</td>
                    <td>提供每次扫描的问题数量统计</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskRuleset</td>
                    <td>查询任务的已选规则集列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskSettings</td>
                    <td>查询任务的高级选项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskPathTree</td>
                    <td>获取任务的目录树</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTasklog</td>
                    <td>查询任务检查失败日志,不传execute_id则查询最近一次的检查日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskSettings</td>
                    <td>任务配置高级选项,如自定义镜像</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProgressDetail</td>
                    <td>根据任务ID查询任务执行状态。任务状态:0表示检查中,1表示检查失败,2表示检查成功,3表示任务中止。只有正在检查中才有进度的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckRulesetParameters</td>
                    <td>查询任务规则集的检查参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopTaskById</td>
                    <td>根据任务ID终止检查任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskParameter</td>
                    <td>任务配置检查参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskRuleset</td>
                    <td>修改任务规则集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTask</td>
                    <td>手工触发一次任务调度</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckParameters</td>
                    <td>查询任务规则集的检查参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIgnorePath</td>
                    <td>任务配置屏蔽目录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">缺陷管理</td>
                    <td>ShowTaskCmetrics</td>
                    <td>根据检查任务ID查询cmertrics缺陷概要。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskDefects</td>
                    <td>根据检查任务ID分页查询缺陷结果详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDefectStatus</td>
                    <td>修改检查出的缺陷的状态为已解决、已忽略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskDefectsStatistic</td>
                    <td>根据检查任务ID查询缺陷详情的统计</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskDetail</td>
                    <td>根据检查任务ID查询缺陷结果的概要。包括问题概述、问题状态、圈复杂度、代码重复率等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">规则引擎</td>
                    <td>ListRules</td>
                    <td>查询规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">规则管理</td>
                    <td>SetDefaulTemplate</td>
                    <td>设置每个项目对应语言的默认规则集配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplateRules</td>
                    <td>根据项目ID、规则集ID等条件查询规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRuleset</td>
                    <td>删除自定义规则集,正在使用中的或默认规则集不能删除</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRuleset</td>
                    <td>可根据需求灵活的组合规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRulesets</td>
                    <td>根据项目ID、语言等条件查询规则集列表。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
