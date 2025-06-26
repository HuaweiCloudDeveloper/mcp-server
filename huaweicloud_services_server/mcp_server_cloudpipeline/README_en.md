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
                    <td rowspan="1">Logstash interface</td>
                    <td>ListPipelines</td>
                    <td>This API is used to query the pipeline list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Pipeline Management--New</td>
                    <td>CreatePipelineByTemplateId</td>
                    <td>Create a pipeline based on a template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopPipelineRun</td>
                    <td>Stop the pipeline</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowPipelinesLatestStatus</td>
                    <td>Obtain pipeline status in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPipelineRuns</td>
                    <td>Obtains pipeline execution records.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePipeline</td>
                    <td>Delete pipeline</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPipelineRunDetail</td>
                    <td>Obtain the pipeline status/Obtain the pipeline execution details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunPipeline</td>
                    <td>Start pipeline</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Pipeline Template Management--New</td>
                    <td>ListPipelineTemplates</td>
                    <td>Query the pipeline template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPipelineTemplateDetail</td>
                    <td>Query template details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Pipeline management</td>
                    <td>CreatePipelineByTemplate</td>
                    <td>Quickly create pipelines and pipeline tasks based on templates</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPipleineBuildResult</td>
                    <td>Obtain the pipeline execution status of a project</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartNewPipeline</td>
                    <td>Start the pipeline</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPipleineStatus</td>
                    <td>Obtain the pipeline status, phase, and task information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemovePipeline</td>
                    <td>Delete a pipeline by ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopPipelineNew</td>
                    <td>Stop the pipeline</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceStatus</td>
                    <td>Check the pipeline creation status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowPipelinesStatus</td>
                    <td>Obtain pipeline status and phase information in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPipelineSimpleInfo</td>
                    <td>API for obtaining the pipeline list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Project Information</td>
                    <td>ListTemplates</td>
                    <td>Query project template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Template Management</td>
                    <td>ShowTemplateDetail</td>
                    <td>Query template details</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
