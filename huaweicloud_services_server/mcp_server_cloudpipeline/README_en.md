# CloudPipeline MCP Server 


## Version
v0.1.0

## Overview

CloudPipeline MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CloudPipeline. Full-chain management of CloudPipeline resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Logstash interface | ListPipelines | This API is used to query the pipeline list. | To be tested |
| Pipeline Management--New | CreatePipelineByTemplateId | Create a pipeline based on a template | To be tested |
|  | StopPipelineRun | Stop the pipeline | To be tested |
|  | BatchShowPipelinesLatestStatus | Obtain pipeline status in batches | To be tested |
|  | ListPipelineRuns | Obtains pipeline execution records. | To be tested |
|  | DeletePipeline | Delete pipeline | To be tested |
|  | ShowPipelineRunDetail | Obtain the pipeline status/Obtain the pipeline execution details | To be tested |
|  | RunPipeline | Start pipeline | To be tested |
| Pipeline Template Management--New | ListPipelineTemplates | Query the pipeline template list | To be tested |
|  | ShowPipelineTemplateDetail | Query template details | To be tested |
| Pipeline management | CreatePipelineByTemplate | Quickly create pipelines and pipeline tasks based on templates | To be tested |
|  | ListPipleineBuildResult | Obtain the pipeline execution status of a project | To be tested |
|  | StartNewPipeline | Start the pipeline | To be tested |
|  | ShowPipleineStatus | Obtain the pipeline status, phase, and task information | To be tested |
|  | RemovePipeline | Delete a pipeline by ID | To be tested |
|  | StopPipelineNew | Stop the pipeline | To be tested |
|  | ShowInstanceStatus | Check the pipeline creation status. | To be tested |
|  | BatchShowPipelinesStatus | Obtain pipeline status and phase information in batches | To be tested |
|  | ListPipelineSimpleInfo | API for obtaining the pipeline list | To be tested |
| Project Information | ListTemplates | Query project template | To be tested |
| Template Management | ShowTemplateDetail | Query template details | To be tested |

