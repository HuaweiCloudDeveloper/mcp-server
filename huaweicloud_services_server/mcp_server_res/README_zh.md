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
                    <td rowspan="4">在线服务</td>
                    <td>UpdateResOnlineInstance</td>
                    <td>修改指定在线服务的元数据内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResOnlineServiceDetails</td>
                    <td>根据给定的workspace_id和resource_id及category查询在线服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResOnlineInstance</td>
                    <td>新建在线服务元数据,新建成功之后可手动发布此服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResOnlineInstance</td>
                    <td>删除在线服务实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">场景</td>
                    <td>CreateResIntelligentScene</td>
                    <td>在指定工作空间下面创建智能场景。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResScene</td>
                    <td>该接口用于删除场景,删除之后不能恢复,请您谨慎操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResScenes</td>
                    <td>查询当前工作空间下的场景列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResScene</td>
                    <td>查询指定场景的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResScene</td>
                    <td>在指定工作空间下面创建自定义场景。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResIntelligentScene</td>
                    <td>更新智能场景的内容信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResScene</td>
                    <td>更新自定义场景的内容信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">工作空间</td>
                    <td>ShowResWrokspace</td>
                    <td>查询指定工作空间的具体信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResWorkspace</td>
                    <td>用于在推荐系统下面创建独立的工作空间,用于资源的隔离,用户可以在工作空间下面继续创建数据源、场景以及推荐任务等。是否有工作空间的操作权限取决于用户是否属于当前工作空间绑定的企业项目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResEnterprises</td>
                    <td>查询用户在当前项目id下的企业项目列表。在创建工作空间时需要提供企业项目id。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResWorkspace</td>
                    <td>删除指定工作空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResWorkspace</td>
                    <td>更新工作空间信息, 只允许更新描述信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResWorkspaces</td>
                    <td>用于查询当前用户具有操作权限的工作空间列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">数据源</td>
                    <td>UpdateResDatasource</td>
                    <td>修改指定数据源的配置内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResDatasource</td>
                    <td>在指定的工作空间下面创建一个新的数据源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResDatasourceWorkDetail</td>
                    <td>查询指定数据源下离线任务的结果。其中包括数据格式,数据检测、数据探索及效果评估的内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResDatasources</td>
                    <td>查询当前工作空间下的数据源列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResDatasource</td>
                    <td>查询指定数据源的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResDatasource</td>
                    <td>删除数据源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResDatastruct</td>
                    <td>修改数据源中的特征。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询规格</td>
                    <td>ListResResourceSpec</td>
                    <td>查询当前推荐系统所提供的离线计算规格,实时计算规格和排序模型训练规格。在创建数据源和场景时,需要提供此信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">训练作业</td>
                    <td>ShowResJob</td>
                    <td>查询resource_id(数据源id或场景id)下的指定类型的作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResJob</td>
                    <td>新建训练作业元数据,新建成功之后可手动执行此任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResJobs</td>
                    <td>批量新建作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResRecallSet</td>
                    <td>查询给定workspaces_id和指定resource_id下的候选集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResJob</td>
                    <td>删除指定作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResJob</td>
                    <td>修改指定作业的元数据信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">调度</td>
                    <td>StartResJob</td>
                    <td>执行独立的作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartResSceneJobs</td>
                    <td>执行场景下面的所有作业和服务。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
