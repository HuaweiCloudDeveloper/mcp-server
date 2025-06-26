# CloudPipeline MCP Server 


## Version
v0.1.0

## Overview

CloudPipeline MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CloudPipeline. Full-chain management of CloudPipeline resources can be carried out based on natural language.

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
                    <td rowspan="1">Logstash接口</td>
                    <td>ListPipelines</td>
                    <td>该接口用于查询pipeline列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">模板管理</td>
                    <td>ShowTemplateDetail</td>
                    <td>查询模板详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">流水线模板管理--新</td>
                    <td>ListPipelineTemplates</td>
                    <td>查询流水线模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPipelineTemplateDetail</td>
                    <td>查询模板详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">流水线管理</td>
                    <td>CreatePipelineByTemplate</td>
                    <td>基于模板快速创建流水线及流水线内任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPipleineBuildResult</td>
                    <td>获取项目下流水线执行状况</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartNewPipeline</td>
                    <td>启动流水线</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPipleineStatus</td>
                    <td>获取流水线状态,阶段及任务信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemovePipeline</td>
                    <td>根据id删除流水线</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopPipelineNew</td>
                    <td>停止流水线</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceStatus</td>
                    <td>检查流水线创建状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowPipelinesStatus</td>
                    <td>批量获取流水线状态和阶段信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPipelineSimpleInfo</td>
                    <td>获取流水线列表接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">流水线管理--新</td>
                    <td>CreatePipelineByTemplateId</td>
                    <td>基于模板创建流水线</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopPipelineRun</td>
                    <td>停止流水线</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowPipelinesLatestStatus</td>
                    <td>批量获取流水线状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPipelineRuns</td>
                    <td>获取流水线执行记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePipeline</td>
                    <td>删除流水线</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPipelineRunDetail</td>
                    <td>获取流水线状态/获取流水线执行详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunPipeline</td>
                    <td>启动流水线</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">项目信息</td>
                    <td>ListTemplates</td>
                    <td>查询项目模板</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
