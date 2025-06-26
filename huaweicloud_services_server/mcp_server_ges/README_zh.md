# GES MCP Server 


## Version
v0.1.0

## Overview

GES MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GES. Full-chain management of GES resources can be carried out based on natural language.

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
                    <td rowspan="3">GraphPlugins管理API</td>
                    <td>ListScenes2</td>
                    <td>查询scenes场景下的应用分析能力详情,可以获得对应场景下的application、参数和功能介绍详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeregisterScenes2</td>
                    <td>取消订阅scenes场景应用分析能力,取消订阅后对应scene下的application业务面API将不能使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterScenes2</td>
                    <td>订阅scenes应用场景分析能力,便于业务面API使用对应功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">任务中心API</td>
                    <td>ShowJob2</td>
                    <td>查询Job的执行状态。对创建图、关闭图、启动图、删除图、导入图等异步API命令下发后,会返回jobId,通过jobId查询任务的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobs</td>
                    <td>查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务,该API用于查询这些任务的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobs2</td>
                    <td>查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务,该API用于查询这些任务的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">元数据管理API</td>
                    <td>DeleteMetadata2</td>
                    <td>删除元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetadata2</td>
                    <td>查询某个元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadFromObs2</td>
                    <td>从OBS导入元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMetadata</td>
                    <td>删除元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetadatas2</td>
                    <td>查询元数据列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMetadata2</td>
                    <td>新增元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetadatas</td>
                    <td>查询元数据列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadFromObs</td>
                    <td>从OBS导入元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGraphMetadatas</td>
                    <td>查询某个图下的元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="29">图管理API</td>
                    <td>ExpandGraph2</td>
                    <td>扩副本能力允许动态扩容多个从节点,扩容的从节点可以处理读请求,从而提高读请求性能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGraph2</td>
                    <td>删除一个图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportGraph2</td>
                    <td>增量导入图数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopGraph</td>
                    <td>关闭一个图。如果图创建好了,暂时不用可以先关闭,需要使用时再启用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGraph2</td>
                    <td>创建一个图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartGraph2</td>
                    <td>启动一个图。暂时不用的图可以先关闭,需要使用时再启动。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandGraph</td>
                    <td>扩副本能力允许动态扩容多个从节点,扩容的从节点可以处理读请求,从而提高读请求性能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachEip2</td>
                    <td>当无需继续使用EIP时,您可通过解绑EIP来释放网络资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeGraph2</td>
                    <td>变更图规格规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ClearGraph2</td>
                    <td>清空图中所有数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGraphs2</td>
                    <td>查询当前租户所有的图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachEip2</td>
                    <td>可以通过绑定弹性公网IP(简称EIP)访问GES服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGraph</td>
                    <td>删除一个图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGraph</td>
                    <td>根据图ID查询某个图详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachEip</td>
                    <td>当无需继续使用EIP时,您可通过解绑EIP来释放网络资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGraphs</td>
                    <td>查询当前租户所有的图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartGraph</td>
                    <td>启动一个图。暂时不用的图可以先关闭,需要使用时再启动。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeGraph</td>
                    <td>升级图。图引擎服务会定期升级版本,用户可根据需要升级图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeGraph2</td>
                    <td>升级图。图引擎服务会定期升级版本,用户可根据需要升级图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGraph2</td>
                    <td>根据图ID查询某个图详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopGraph2</td>
                    <td>关闭一个图。如果图创建好了,暂时不用可以先关闭,需要使用时再启用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportGraph</td>
                    <td>增量导入图数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportGraph2</td>
                    <td>导出图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ClearGraph</td>
                    <td>清空图中所有数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartGraph2</td>
                    <td>强制启动一个图。针对导入、导出 、运行中 、清空中的图。强制重启图,会将该图执行中的异步任务变为失败,然后停止图、启动图到运行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportGraph</td>
                    <td>导出图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGraph</td>
                    <td>创建一个图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeGraph</td>
                    <td>扩容图规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartGraph</td>
                    <td>强制启动一个图。针对导入、导出 、运行中 、清空中的图。强制重启图,会将该图执行中的异步任务变为失败,然后停止图、启动图到运行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">备份与恢复</td>
                    <td>ShowBackupDownloadLink</td>
                    <td>获取备份下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackups</td>
                    <td>获取备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">备份管理API</td>
                    <td>ListGraphBackups</td>
                    <td>查询某个图下的备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackup2</td>
                    <td>删除备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBackup2</td>
                    <td>新增备份。当前图数据出现错误或故障时,可以启动备份图进行恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackups2</td>
                    <td>查询备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBackup</td>
                    <td>新增备份。当前图数据出现错误或故障时,可以启动备份图进行恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGraphBackups2</td>
                    <td>查询某个图下的备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportBackup2</td>
                    <td>导入备份</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackup</td>
                    <td>删除备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportBackup2</td>
                    <td>导出备份</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">实例管理</td>
                    <td>AttachEip</td>
                    <td>绑定和解绑弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">系统管理API</td>
                    <td>ListQuotas2</td>
                    <td>查询租户配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">联邦身份认证管理</td>
                    <td>CreateMetadata</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)导入Metadata文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">连接管理</td>
                    <td>ChangeSecurityGroup</td>
                    <td>修改SFS Turbo文件系统绑定的安全组。修改安全组为异步任务,可以通过“查询单个文件系统”返回的子状态字段“sub_status”来判断是否修改安全组状态,子状态为“232”即为修改安全组成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额管理</td>
                    <td>ListQuotas</td>
                    <td>获取配额信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像任务</td>
                    <td>ShowJob</td>
                    <td>该接口为扩展接口,主要用于查询异步接口执行情况,比如查询导出镜像任务的执行状态。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
