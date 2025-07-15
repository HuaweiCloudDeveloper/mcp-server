# CodeArtsPipeline MCP Server

## Version Information
v0.1.0

## Product Description

CodeArtsPipeline MCP Server is a Model Context Protocol server that provides MCP clients (such as Claude Desktop, Cline, and Cursor) with the ability to interact with Huawei Cloud Service CodeArtsPipeline. CodeArtsPipeline resources can be managed in the entire chain based on natural language.

## Available tools
Covering the entire API, use as needed, the list and status are as follows:

| Category | Tool name | Function description | Status |
| --- | --- | --- | --- |
| Extension plugin management | CreatePublisher | Create publisher | To be tested |
| | UploadBasicPlugin | Upload basic plugin | To be tested |
| | ShowPluginVersion | Query plugin version details | To be tested |
| | DeletePublisher | Delete publisher | To be tested |
| | CreatePluginVersion | Create plugin version | To be tested |
| | ListBasePluginsNewPost | Paginated query of optional plugin list | To be tested |
| | DeleteBasicPlugin | Delete basic plugin | To be tested |
| | ShowBasicPlugin | Query basic plugin details | To be tested |
| | ListAvailablePublisher | Query available publishers | To be tested |
| | ShowPublisher | Query publisher details | To be tested |
| | UpdatePluginBaseInfo | Update plugin basic information | To be tested |
| | ListPLuginVersion | Query all plugin version information | To be tested |
| | UploadPluginIcon | Update plugin icon | To be tested |
| | ListPlugins | Query plugin list | To be tested |
| | UploadPublisherIcon | Update publisher icon | To be tested |
| | CreatePluginDraft | Create plugin draft version | To be tested |
| | UpdatePluginDraft | Update plugin draft | To be tested |
| | ListStagePlugins | Query optional plugin list | To be tested |
| | ShowPluginOutputs | Query plugin output configuration | To be tested |
| | ListPublisher | Query publisher list | To be tested |
| | DeletePluginDraft | Delete plugin draft | To be tested |
| | PublishPluginDraft | Publish plugin draft | To be tested |
| | ShowPluginInputs | Query plugin input configuration | To be tested |
| | PublishPlugin | Publish plugin | To be tested |
| | PublishPluginBind | Plugin binding publisher | To be tested |
| | UpdateBasicPlugin | Update basic plugin | To be tested |
| | ListPluginVersionNumber | Query plugin version number | To be tested |
| | ShowPluginMetrics | Query plugin metric configuration | To be tested |
| | CreateBasicPlugin | Create basic plugin | To be tested |
| | ListBasePlugins | Query basic plugin list | To be tested |
| Template management | ListTemplates | Query template list, support paging query, support template name fuzzy query | To be tested |
| | ShowTemplateDetail | Query template details | To be tested |
| Pipeline group management | UpdatePipelineGroup | Update pipeline group | To be tested |
| | ShowPipelineGroupTree | Query the pipeline group tree | To be tested |
| | CreatePipelineGroup | Create a new pipeline group | To be tested |
| | BatchMovePipelineToGroup | Batch move pipelines to a group | To be tested |
| | DeletePipelineGroup | Delete a pipeline group | To be tested |
| Pipeline template management--new | DeletePipelineTemplate | Delete a pipeline template | To be tested |
| | ShowPipelineTemplateDetail | Query template details | To be tested |
| | UpdatePipelineTemplate | Update pipeline template | To be tested |
| | ListPipelineTemplates | Query pipeline template list | To be tested |
| | CreatePipelineTemplate | Create a pipeline template | To be tested |
| Pipeline management | ShowPipelineDetail | Query pipeline details | To be tested |
| | UpdatePipelineInfo | Modify pipeline information | To be tested |
| | ListPipleineBuildResult | Get the pipeline execution status under the project | To be tested |
| | ListPipelineSimpleInfo | Get the pipeline list interface | To be tested |
| | StartNewPipeline | Start the pipeline | To be tested |
| | RemovePipeline | Delete the pipeline by id | To be tested |
| | ShowPipleineStatus | Get the pipeline status, stage and task information | To be tested |
| | CreatePipelineByTemplate | Quickly create pipelines and tasks in pipelines based on templates | To be tested |
| | BatchShowPipelinesStatus | Batch get pipeline status and stage information | To be tested |
| | StopPipelineNew | Stop the pipeline | To be tested |
| | ShowInstanceStatus | Check the pipeline creation status | To be tested |
| Pipeline Management--New | CreatePipelineNew | Create a pipeline | To be tested |
| | RetryPipelineRun | Retry the pipeline | To be tested |
| | ShowPipelineLog | Query the pipeline log | To be tested |
| | StopPipelineRun | Stop the pipeline | To be tested |
| | DeletePipeline | Delete the pipeline | To be tested |
| | BatchShowPipelinesLatestStatus | Get the pipeline status in batches | To be tested |
| | RejectManualReview | Reject manual review | To be tested |
| | AcceptManualReview | Accept manual review | To be tested |
| | RunPipeline | Start the pipeline | To be tested |
| | ListPipelineRuns | Get the pipeline execution record | To be tested |
| | ShowStepOutputs | Get the pipeline step execution output | To be tested |
| | CreatePipelineByTemplateId | Create a pipeline based on a template | To be tested |
| | ShowPipelineArtifacts | Query the build products on the pipeline | To be tested |
| | ListPipelines | Get the pipeline list/get the pipeline execution status under the project | To be tested |
| | ShowPipelineRunDetail | Get the pipeline status/get the pipeline execution details | To be tested |
| Tenant-level policy management | DeleteStrategy | Delete a policy | To be tested |
| | ListStrategy | Get a policy list | To be tested |
| | SwitchStrategy | Modify the policy status | To be tested |
| | CreateStrategy | Create a policy | To be tested |
| | UpdateStrategy | Modify a policy | To be tested |
| | ShowStrategy | Get policy details | To be tested |
| Rule management | ShowRule | Get the details of a single rule | To be tested |
| | DeleteRule | Delete a rule | To be tested |
| | CreateRule | Create a rule | To be tested |
| | UpdateRule | Update a rule | To be tested |
| | ListRule | Get rule list by page | To be tested |
| Project-level strategy management | ListProjectStrategy | Get strategy list | To be tested |
| | ShowProjectStrategy | Query project-level strategy details | To be tested |