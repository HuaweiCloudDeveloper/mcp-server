# MRS MCP Server 


## Version
v0.1.0

## Overview

MRS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service MRS. Full-chain management of MRS resources can be carried out based on natural language.

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
                    <td rowspan="3">ClusterManagement</td>
                    <td>ExpandCluster</td>
                    <td>对MRS集群进行扩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddComponent</td>
                    <td>集群添加组件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShrinkCluster</td>
                    <td>对MRS集群进行缩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">DataConnectorManagement</td>
                    <td>UpdateDataConnector</td>
                    <td>更新数据连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataConnector</td>
                    <td>查询数据连接列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataConnector</td>
                    <td>创建数据连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDataConnector</td>
                    <td>删除数据连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">IAMSyncManagement</td>
                    <td>UpdateSyncIamUser</td>
                    <td>将IAM用户和用户组同步到manager,指定用户的情况下,会将该用户关联的IAM用户组也同步到manager。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelSyncIamUser</td>
                    <td>指定用户、用户组取消同步</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSyncIamUser</td>
                    <td>获取已经同步的IAM用户和用户组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">SQL接口</td>
                    <td>CancelSql</td>
                    <td>在MRS集群中取消一条SQL的执行任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlResult</td>
                    <td>在MRS集群中查询一条SQL的执行结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteSql</td>
                    <td>在MRS集群中提交并执行一条SQL语句。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">TagManagement</td>
                    <td>SwitchClusterTags</td>
                    <td>对已有集群启用或关闭集群默认标签。开启后,集群内节点会打上集群默认标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTagStatus</td>
                    <td>查询集群默认标签状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">VersionMetaQuery</td>
                    <td>ShowMrsVersionList</td>
                    <td>展示MRS版本列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMrsFlavors</td>
                    <td>查询MRS集群版本可用的规格</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMrsVersionMetadata</td>
                    <td>查询对应版本元数据。如果参数里指定集群id,则可查询集群更新过补丁之后的最新元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">作业管理接口</td>
                    <td>ShowJobExeListNew</td>
                    <td>在MRS指定集群中查询作业列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSingleJobExe</td>
                    <td>在MRS集群中查询指定作业的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlResultWithJob</td>
                    <td>在MRS集群中查询SparkSql和SparkScript两种类型作业的SQL语句运行完成后返回的查询结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteJobs</td>
                    <td>在MRS集群中批量删除作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopJob</td>
                    <td>在MRS集群中终止指定作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateExecuteJob</td>
                    <td>在MRS集群中新增并提交一个作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">其他接口</td>
                    <td>ListAvailableZones</td>
                    <td>在创建实例时,需要配置实例所在的可用区ID,可通过该接口查询可用区的ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">委托管理</td>
                    <td>UpdateAgencyMapping</td>
                    <td>更新用户(组)与IAM委托之间的映射关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgencyMapping</td>
                    <td>获取用户(组)与IAM委托之间的映射关系的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">弹性伸缩接口</td>
                    <td>DeleteAutoScalingPolicy</td>
                    <td>删除弹性伸缩策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScalingPolicy</td>
                    <td>对弹性伸缩规则进行编辑。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutoScalingPolicy</td>
                    <td>更新弹性伸缩策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoScalingPolicy</td>
                    <td>查看指定集群的所有的弹性伸缩策略信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutoScalingPolicy</td>
                    <td>创建弹性伸缩策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">标签管理接口</td>
                    <td>CreateClusterTag</td>
                    <td>为特定的集群添加一个tag。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClustersByTags</td>
                    <td>使用标签过滤集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterTags</td>
                    <td>查询指定集群的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteClusterTags</td>
                    <td>为指定集群批量删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClusterTag</td>
                    <td>删除特定集群的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateClusterTags</td>
                    <td>为指定集群批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">联盟管理</td>
                    <td>ListNodes</td>
                    <td>功能描述:用户可以使用该接口查询联盟可信节点(包含聚合节点和计算节点)列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">证书标签管理</td>
                    <td>ListAllTags</td>
                    <td>查询所有标签列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowTagQuota</td>
                    <td>查询标签的配额信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">集群HDFS文件接口</td>
                    <td>ShowHdfsFileList</td>
                    <td>在MRS集群中获取指定目录文件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">集群管理接口</td>
                    <td>UpdateClusterScaling</td>
                    <td>创建集群后,扩容/缩容集群Core节点或者Task节点。MRS集群创建成功后不支持调整Master节点数量,即不支持扩缩容Master节点。该接口不兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunJobFlow</td>
                    <td>创建一个MRS集群并提交作业,并支持作业完成后删除集群,支持MRS 1.8.9及以上集群版本使用。使用接口前,您需要先获取下的资源信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCluster</td>
                    <td>数据完成处理分析后或者集群运行异常无法提供服务时可删除集群服务。该接口兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusters</td>
                    <td>查看用户创建的集群列表信息。该接口不兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHosts</td>
                    <td>该接口用于查询输入集群的主机列表详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCluster</td>
                    <td>创建一个MRS集群,并在集群中提交一个作业。该接口不兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterDetails</td>
                    <td>查看指定集群的详细信息。该接口不兼容Sahara。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClusterName</td>
                    <td>修改集群名称</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
