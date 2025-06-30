# CDM MCP Server 


## Version
v0.1.0

## Overview

CDM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CDM. Full-chain management of CDM resources can be carried out based on natural language.

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
                    <td rowspan="1">Job相关接口</td>
                    <td>ShowJobs</td>
                    <td>查询Job详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job管理</td>
                    <td>ShowJobStatus</td>
                    <td>查询job的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">任务管理</td>
                    <td>DeleteJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">作业相关的API</td>
                    <td>StartJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">作业管理</td>
                    <td>ShowSubmissions</td>
                    <td>查询作业执行历史接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAndStartRandomClusterJob</td>
                    <td>随机集群创建作业并执行接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">作业管理接口</td>
                    <td>StopJob</td>
                    <td>在MRS集群中终止指定作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">实例管理</td>
                    <td>UpdateJob</td>
                    <td>更新租户指定ID任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateJob</td>
                    <td>创建单个任务,根据请求参数不同,可以创建单个实时迁移、实时同步、实时灾备等任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">连接管理</td>
                    <td>UpdateLink</td>
                    <td>修改连接接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLink</td>
                    <td>删除连接接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLink</td>
                    <td>创建连接接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLink</td>
                    <td>查询连接接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">集群管理</td>
                    <td>StartCluster</td>
                    <td>启动集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatastores</td>
                    <td>查询CDM集群支持的版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlavorDetail</td>
                    <td>查询指定规格ID的规格详请。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyCluster</td>
                    <td>修改CDM集群配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterEnterpriseProjects</td>
                    <td>查询指定集群的企业项目ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnterpriseProjects</td>
                    <td>查询当前项目下的所有集群的企业项目ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartCluster</td>
                    <td>此接口用于重启集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAvailabilityZones</td>
                    <td>查询CDM集群的所有可用区。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlavors</td>
                    <td>按版本ID查询所有兼容规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceDetail</td>
                    <td>查询集群实例信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">集群管理接口</td>
                    <td>DeleteCluster</td>
                    <td>数据完成处理分析后或者集群运行异常无法提供服务时可删除集群服务。该接口兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCluster</td>
                    <td>创建一个MRS集群,并在集群中提交一个作业。该接口不兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterDetail</td>
                    <td>该接口用于查询并显示单个集群详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusters</td>
                    <td>查看用户创建的集群列表信息。该接口不兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
