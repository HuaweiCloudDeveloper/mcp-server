# CPH MCP Server 


## Version
v0.1.0

## Overview

CPH MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CPH. Full-chain management of CPH resources can be carried out based on natural language.

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
                    <td rowspan="5">ADB命令</td>
                    <td>RunShellCommand</td>
                    <td>在云手机中执行shell命令。该接口为异步接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PushFile</td>
                    <td>推送文件到云手机文件系统中。系统会将所指定的文件下载解压后,将解压后的内容全部推送到云手机的根目录下。只支持指定tar格式的文件进行推送,您需要将tar文件提前上传至您的OBS桶中。该接口为异步接口。接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InstallApk</td>
                    <td>在云手机中安装apk。系统会将指定的apk文件下载后直接安装到云手机中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UninstallApk</td>
                    <td>在云手机中卸载apk。该接口为异步接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunSyncCommand</td>
                    <td>在云手机中同步执行命令并返回命令执行的输出信息,该接口仅支持adb shell命令的执行。1分钟内每个用户调用接口次数上限为6次,每个云手机允许执行命令超时时间为2秒,接口时间不超过30秒,执行云手机数越多,接口耗时相应越长。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TAG功能</td>
                    <td>ListResourceInstances</td>
                    <td>使用标签过滤查询租户下资源的实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>查询租户在指定项目中指定资源类型下的所有标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">云手机服务器管理</td>
                    <td>DeleteShareFiles</td>
                    <td>删除共享存储目录中文件,该功能仅在支持共享存储的云手机规格上可实现。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PushShareApps</td>
                    <td>推送应用tar文件至共享应用存储目录中,该功能仅在支持共享应用的云手机服务器上可实现。接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeCloudPhoneServer</td>
                    <td>切换云手机服务器, 支持您换一台新的云手机服务器。切换后服务器名称、服务器ID和服务器所在AZ与原服务器相同, 服务器计费保持不变。服务器切换的同时服务器上的手机重新创建,不保留用户数据。切换需要额外的资源和资源配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartCloudPhoneServer</td>
                    <td>批量重启云手机服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCloudPhoneServerDetail</td>
                    <td>根据server_id查询云手机服务器的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudPhoneServers</td>
                    <td>分页查询云手机服务器,云手机服务器列表按照创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在云手机服务器,则返回空列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeCloudPhoneServerModel</td>
                    <td>变更云手机服务器规格。接口调用成功后,大约2分钟左右规格会变更结束,在订单中心可以查看到变更的订单状态为成功,且查询服务器的详细信息,可以查看到服务器规格名称已经变成新的规格名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServerName</td>
                    <td>根据serverId修改serverName。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListShareFiles</td>
                    <td>查询共享存储指定路径下的文件列表,该功能仅在支持共享存储的云手机规格上可实现。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteShareApps</td>
                    <td>在共享应用存储目录中删除共享应用,该功能仅在支持共享应用的云手机规格上可实现。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNet2CloudPhoneServer</td>
                    <td>购买云手机服务器,支持您复用已有的VPC网络管理云手机服务器,支持云手机服务器复用您已购买的共享带宽等资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PushShareFiles</td>
                    <td>推送文件至共享存储目录中,该功能仅在支持共享存储的云手机规格上可实现。接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCloudPhoneSingleServer</td>
                    <td>该接口创建的服务器仅包含服务器和服务器的镜像,不包含云手机实例和镜像等内容。若需要创建包含云手机实例的服务器,请使用创建云手机服务器接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudPhoneServerModels</td>
                    <td>查询云手机服务器的规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">任务中心API</td>
                    <td>ListJobs</td>
                    <td>查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务,该API用于查询这些任务的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">使用标签管理服务</td>
                    <td>ListResourceTags</td>
                    <td>查询指定实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">密钥管理</td>
                    <td>UpdateKeypair</td>
                    <td>修改连接云手机的密钥对。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">带宽</td>
                    <td>UpdateBandwidth</td>
                    <td>更新带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">带宽管理</td>
                    <td>ShowBandwidthDetail</td>
                    <td>查询云手机使用的带宽信息,本接口只适用于使用系统定义网络的服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">手机实例管理</td>
                    <td>BatchShowPhoneConnectInfos</td>
                    <td>获取云手机连接信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCloudPhoneProperty</td>
                    <td>部分云手机属性开放更新能力,部分属性无法更新,部分属性需要重启手机生效,属性约束请云手机属性列表。如果手机处于异常状态,属性更新后需恢复手机状态为运行中才可生效。该接口为异步接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandPhoneDataVolumeSize</td>
                    <td>扩容云手机数据盘大小</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCloudPhoneDetail</td>
                    <td>查询云手机的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudPhones</td>
                    <td>分页查询云手机,云手机列表按照创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在云手机,则返回空列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePhoneName</td>
                    <td>根据phoneId修改phoneName。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartCloudPhone</td>
                    <td>批量重启云手机,也可用于开启云手机。该接口为异步接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchExportCloudPhoneData</td>
                    <td>批量导出云手机中的数据。该接口为异步接口。接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetCloudPhone</td>
                    <td>批量重置云手机,将云手机恢复出厂设置。该接口为异步接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportTraffic</td>
                    <td>手机流量路由修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopCloudPhone</td>
                    <td>批量关闭云手机。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudPhoneModels</td>
                    <td>查询或统计云手机的规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudPhoneImages</td>
                    <td>根据项目ID查询可用的手机镜像。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchImportCloudPhoneData</td>
                    <td>批量恢复数据到云手机中。该接口为异步接口。接口调用前请先确保已完成CPH服务操作OBS桶的委托授权。委托CPH操作OBS桶请参见[委托CPH操作OBS桶](https://support.huaweicloud.com/bestpractice-cph/cph_bp_0050.html)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">标签管理</td>
                    <td>BatchCreateTags</td>
                    <td>批量创建标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTags</td>
                    <td>为指定保护实例批量删除标签。一个资源上最多有10个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">编码服务管理</td>
                    <td>ListEncodeServers</td>
                    <td>查询编码服务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartEncodeServer</td>
                    <td>批量重启编码服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">自定义镜像管理</td>
                    <td>UpdateImageMember</td>
                    <td>用户收到共享镜像后,选择接受或拒绝共享镜像。未接受的共享镜像无法使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddImageMember</td>
                    <td>镜像共享,共享镜像给指定账号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteImageMember</td>
                    <td>删除共享镜像</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">边缘镜像</td>
                    <td>DeleteImage</td>
                    <td>将指定ID的边缘私有镜像删除</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像</td>
                    <td>ListImages</td>
                    <td>根据不同条件查询镜像列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像任务</td>
                    <td>ShowJob</td>
                    <td>该接口为扩展接口,主要用于查询异步接口执行情况,比如查询导出镜像任务的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像共享</td>
                    <td>ListImageMembers</td>
                    <td>该接口用于共享镜像过程中,获取接受该镜像的成员列表。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
