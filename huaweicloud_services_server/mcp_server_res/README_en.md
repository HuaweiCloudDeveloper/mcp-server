# RES MCP Server 


## Version
v0.1.0

## Overview

RES MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RES. Full-chain management of RES resources can be carried out based on natural language.

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
                    <td rowspan="7">Data Source</td>
                    <td>UpdateResDatasource</td>
                    <td>Modifies the configuration of a specified data source.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResDatasource</td>
                    <td>Creates a data source under the specified workspace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResDatasourceWorkDetail</td>
                    <td>Query the results of offline tasks in a specified data source. It includes data format, data detection, data exploration and effect evaluation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResDatasources</td>
                    <td>Query the data source list in the current workspace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResDatasource</td>
                    <td>Query details about a specified data source.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResDatasource</td>
                    <td>Delete a data source.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResDatastruct</td>
                    <td>Modify the feature in the data source.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Online Services</td>
                    <td>UpdateResOnlineInstance</td>
                    <td>Modifies the metadata of a specified online service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResOnlineServiceDetails</td>
                    <td>Query online services based on the specified workspace_id, resource_id, and category.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResOnlineInstance</td>
                    <td>Create online service metadata. After the metadata is created, the service can be manually published.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResOnlineInstance</td>
                    <td>Delete the online service instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query Specifications</td>
                    <td>ListResResourceSpec</td>
                    <td>Query the offline computing specifications, real-time computing specifications, and sorting model training specifications provided by the current Recommendation System. This information is required when creating data sources and scenarios.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Scenario</td>
                    <td>CreateResIntelligentScene</td>
                    <td>Create an intelligent scene in the specified workspace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResScene</td>
                    <td>This API is used to delete a scenario and cannot be restored after being deleted. Exercise caution when performing this operation.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResScenes</td>
                    <td>Query the scenario list in the current workspace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResScene</td>
                    <td>Query details about a specified scenario.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResScene</td>
                    <td>Create a custom scenario in the specified workspace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResIntelligentScene</td>
                    <td>Updates the content information in the intelligent scenario.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResScene</td>
                    <td>Updates the content information of the customized scenario.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Schedule</td>
                    <td>StartResJob</td>
                    <td>Execute an independent job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartResSceneJobs</td>
                    <td>Execute all jobs and services in the scenario.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Training Job</td>
                    <td>ShowResJob</td>
                    <td>Query the specified type of jobs under resource_id (data source ID or scenario ID).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResJob</td>
                    <td>Create a training job metadata. After the metadata is created, you can manually perform the task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResJobs</td>
                    <td>Create jobs in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResRecallSet</td>
                    <td>Query the candidate sets under the specified workspaces_id and resource_id.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResJob</td>
                    <td>Delete a specified job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResJob</td>
                    <td>Modifies the metadata of a specified job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Workspace</td>
                    <td>ShowResWrokspace</td>
                    <td>Query detailed information about a specified workspace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResWorkspace</td>
                    <td>Creates an independent workspace in the Recommendation system for resource isolation. Users can create data sources, scenarios, and recommendation tasks in the workspace. Whether the user has the operation permission on the workspace depends on whether the user belongs to the enterprise project bound to the current workspace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResEnterprises</td>
                    <td>Query the enterprise project list of the current project ID. The enterprise project id is required when creating the workspace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResWorkspace</td>
                    <td>Delete a specified workspace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResWorkspace</td>
                    <td>Update workspace information. Only description information can be updated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResWorkspaces</td>
                    <td>Query the workspace list on which the current user has the operation permission.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
