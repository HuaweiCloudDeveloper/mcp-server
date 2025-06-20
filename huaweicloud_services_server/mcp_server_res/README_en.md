# RES MCP Server 


## Version
v0.1.0

## Overview

RES MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RES. Full-chain management of RES resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Data Source | UpdateResDatasource | Modifies the configuration of a specified data source. | To be tested |
|  | CreateResDatasource | Creates a data source under the specified workspace. | To be tested |
|  | ShowResDatasourceWorkDetail | Query the results of offline tasks in a specified data source. It includes data format, data detection, data exploration and effect evaluation. | To be tested |
|  | ListResDatasources | Query the data source list in the current workspace. | To be tested |
|  | ShowResDatasource | Query details about a specified data source. | To be tested |
|  | DeleteResDatasource | Delete a data source. | To be tested |
|  | UpdateResDatastruct | Modify the feature in the data source. | To be tested |
| Online Services | UpdateResOnlineInstance | Modifies the metadata of a specified online service. | To be tested |
|  | ListResOnlineServiceDetails | Query online services based on the specified workspace_id, resource_id, and category. | To be tested |
|  | CreateResOnlineInstance | Create online service metadata. After the metadata is created, the service can be manually published. | To be tested |
|  | DeleteResOnlineInstance | Delete the online service instance. | To be tested |
| Query Specifications | ListResResourceSpec | Query the offline computing specifications, real-time computing specifications, and sorting model training specifications provided by the current Recommendation System. This information is required when creating data sources and scenarios. | To be tested |
| Scenario | CreateResIntelligentScene | Create an intelligent scene in the specified workspace. | To be tested |
|  | DeleteResScene | This API is used to delete a scenario and cannot be restored after being deleted. Exercise caution when performing this operation. | To be tested |
|  | ListResScenes | Query the scenario list in the current workspace. | To be tested |
|  | ShowResScene | Query details about a specified scenario. | To be tested |
|  | CreateResScene | Create a custom scenario in the specified workspace. | To be tested |
|  | UpdateResIntelligentScene | Updates the content information in the intelligent scenario. | To be tested |
|  | UpdateResScene | Updates the content information of the customized scenario. | To be tested |
| Schedule | StartResJob | Execute an independent job. | To be tested |
|  | StartResSceneJobs | Execute all jobs and services in the scenario. | To be tested |
| Training Job | ShowResJob | Query the specified type of jobs under resource_id (data source ID or scenario ID). | To be tested |
|  | CreateResJob | Create a training job metadata. After the metadata is created, you can manually perform the task. | To be tested |
|  | CreateResJobs | Create jobs in batches. | To be tested |
|  | ShowResRecallSet | Query the candidate sets under the specified workspaces_id and resource_id. | To be tested |
|  | DeleteResJob | Delete a specified job. | To be tested |
|  | UpdateResJob | Modifies the metadata of a specified job. | To be tested |
| Workspace | ShowResWrokspace | Query detailed information about a specified workspace. | To be tested |
|  | CreateResWorkspace | Creates an independent workspace in the Recommendation system for resource isolation. Users can create data sources, scenarios, and recommendation tasks in the workspace. Whether the user has the operation permission on the workspace depends on whether the user belongs to the enterprise project bound to the current workspace. | To be tested |
|  | ListResEnterprises | Query the enterprise project list of the current project ID. The enterprise project id is required when creating the workspace. | To be tested |
|  | DeleteResWorkspace | Delete a specified workspace. | To be tested |
|  | UpdateResWorkspace | Update workspace information. Only description information can be updated. | To be tested |
|  | ListResWorkspaces | Query the workspace list on which the current user has the operation permission. | To be tested |

