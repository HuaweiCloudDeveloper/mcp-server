# ECS MCP Server 


## Version
v0.1.0

## Overview

ECS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ECS. Full-chain management of ECS resources can be carried out based on natural language.

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
                    <td rowspan="2">云服务器操作管理</td>
                    <td>NovaListServerActions</td>
                    <td>查询弹性云服务器的所有历史操作,显示操作行为列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServerAction</td>
                    <td>查询弹性云服务器的某个请求行为。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">云服务器组管理</td>
                    <td>CreateServerGroup</td>
                    <td>创建弹性云服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerGroups</td>
                    <td>查询弹性云服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerGroup</td>
                    <td>查询弹性云服务器组详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaDeleteServerGroup</td>
                    <td>删除云服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddServerGroupMember</td>
                    <td>将云服务器加入云服务器组。添加成功后,如果该云服务器组是反亲和性策略的,则该云服务器与云服务器组中的其他成员尽量分散地创建在不同主机上。如果该云服务器时故障域类型的,则该云服务器会拥有故障域属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListServerGroups</td>
                    <td>查询云服务器组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaCreateServerGroup</td>
                    <td>创建弹性云服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServerGroupMember</td>
                    <td>将弹性云服务器移出云服务器组。移出后,该云服务器与云服务器组中的成员不再遵从反亲和策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServerGroup</td>
                    <td>查询云服务器组详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServerGroup</td>
                    <td>删除云服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">元数据管理</td>
                    <td>NovaUpdateServerMetadataItem</td>
                    <td>设置云服务器指定key的元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServerMetadata</td>
                    <td>查询弹性云服务器的元数据信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServerMetadata</td>
                    <td>删除云服务器指定元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServerMetadataItem</td>
                    <td>获取云服务器指定key的元数据信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaUpdateServerMetadata</td>
                    <td>更新云服务器元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServerMetadata</td>
                    <td>更新云服务器元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaCreateServerMetadata</td>
                    <td>设置弹性云服务器的元数据信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaDeleteServerMetadataItem</td>
                    <td>删除云服务器指定元数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">可用区管理</td>
                    <td>ListServerAzInfo</td>
                    <td>查询可用区列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListAvailabilityZones</td>
                    <td>查询可用域列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">安全组管理</td>
                    <td>NovaDisassociateSecurityGroup</td>
                    <td>移除弹性云服务器中的安全组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaAssociateSecurityGroup</td>
                    <td>为弹性云服务器添加一个安全组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListServerSecurityGroups</td>
                    <td>查询指定弹性云服务器的安全组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">密钥密码管理</td>
                    <td>NovaDeleteKeypair</td>
                    <td>根据SSH密钥的名称,删除指定SSH密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaCreateKeypair</td>
                    <td>创建SSH密钥,或把公钥导入系统,生成密钥对。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetServerPassword</td>
                    <td>重置弹性云服务器管理帐号(root用户或Administrator用户)的密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResetPasswordFlag</td>
                    <td>查询弹性云服务器是否支持一键重置密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListKeypairs</td>
                    <td>查询SSH密钥信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServerPassword</td>
                    <td>清除Windows云服务器初始安装时系统生成的密码记录。清除密码后,不影响云服务器密码登录功能,但不能再使用获取密码功能来查询该云服务器密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerPassword</td>
                    <td>当通过支持Cloudbase-init功能的镜像创建Windows云服务器时,获取云服务器初始安装时系统生成的管理员帐户(Administrator帐户或Cloudbase-init设置的帐户)随机密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowKeypair</td>
                    <td>根据SSH密钥名称查询指定SSH密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">引擎版本和规格</td>
                    <td>ListFlavors</td>
                    <td>查询数据库规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">批量操作</td>
                    <td>BatchResetServersPassword</td>
                    <td>批量重置弹性云服务器管理帐号(root用户或Administrator用户)的密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopServers</td>
                    <td>根据给定的云服务器ID列表,批量关闭云服务器,一次最多可以关闭1000台。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRebootServers</td>
                    <td>根据给定的云服务器ID列表,批量重启云服务器,一次最多可以重启1000台。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartServers</td>
                    <td>根据给定的云服务器ID列表,批量启动云服务器,一次最多可以启动1000台。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateServersName</td>
                    <td>批量修改弹性云服务器信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAttachSharableVolumes</td>
                    <td>将指定的共享磁盘一次性挂载到多个弹性云服务器,实现批量挂载。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">查询API版本信息</td>
                    <td>NovaListVersions</td>
                    <td>返回Nova当前所有可用的版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowVersion</td>
                    <td>返回指定版本的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">标签管理</td>
                    <td>ListServerTags</td>
                    <td>项目(Project)用于将OpenStack的资源(计算资源、存储资源和网络资源)进行分组和隔离。项目可以是一个部门或者一个项目组。一个帐户中可以创建多个项目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteServerTags</td>
                    <td>- 为指定云服务器批量删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerTags</td>
                    <td>- 查询指定云服务器的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateServerTags</td>
                    <td>- 为指定云服务器批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">状态管理</td>
                    <td>ResizePostPaidServer</td>
                    <td>当您创建的弹性云服务器规格无法满足业务需要时,可以变更云服务器规格,升级vCPU、内存。具体接口的使用,请参见本节内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaUnlockServer</td>
                    <td>解锁弹性云服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ReinstallServerWithCloudInit</td>
                    <td>重装弹性云服务器的操作系统。支持弹性云服务器数据盘不变的情况下,使用原镜像重装系统盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaStartServer</td>
                    <td>启动单台云服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeServerOsWithoutCloudInit</td>
                    <td>切换弹性云服务器操作系统。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaLockServer</td>
                    <td>锁定弹性云服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterServerMonitor</td>
                    <td>将云服务器添加到监控表中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ReinstallServerWithoutCloudInit</td>
                    <td>重装弹性云服务器的操作系统。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerRemoteConsole</td>
                    <td>获取弹性云服务器VNC远程登录地址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateServer</td>
                    <td>- 将部署在专属主机上的弹性云服务器迁移至其他专属主机。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServerAutoTerminateTime</td>
                    <td>修改按需服务器,设置定时删除时间。如果设置的定时删除时间为空字符串,表示取消定时删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeServerChargeMode</td>
                    <td>更换云服务器的计费模式</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaStopServer</td>
                    <td>关闭单台云服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeServer</td>
                    <td>变更云服务器规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaRebootServer</td>
                    <td>重启单台云服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeServerOsWithCloudInit</td>
                    <td>切换弹性云服务器操作系统。支持弹性云服务器数据盘不变的情况下,使用新镜像重装系统盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">生命周期管理</td>
                    <td>ListCloudServers</td>
                    <td>查询云服务器列表接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListServersDetails</td>
                    <td>查询云服务器详情信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateServers</td>
                    <td>创建一台或多台云服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaUpdateServer</td>
                    <td>修改云服务器信息,目前支持修改云服务器名称及描述。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServer</td>
                    <td>根据云服务器ID,查询云服务器的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServer</td>
                    <td>修改云服务器信息,目前支持修改云服务器名称及描述和hostname。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostPaidServers</td>
                    <td>创建一台或多台[按需付费](https://support.huaweicloud.com/productdesc-ecs/ecs_01_0065.html)方式的云服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServer</td>
                    <td>查询弹性云服务器的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaCreateServers</td>
                    <td>创建一台弹性云服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListServers</td>
                    <td>查询云服务器信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServersDetails</td>
                    <td>根据用户请求条件从数据库筛选、查询所有的弹性云服务器,并关联相关表获取到弹性云服务器的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServers</td>
                    <td>根据指定的云服务器ID列表,删除云服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaDeleteServer</td>
                    <td>删除一台云服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">磁盘管理</td>
                    <td>NovaAttachVolume</td>
                    <td>弹性云服务器挂载磁盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListServerVolumes</td>
                    <td>查询弹性云服务器挂载的磁盘信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachServerVolume</td>
                    <td>从弹性云服务器中卸载磁盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachServerVolume</td>
                    <td>把磁盘挂载到弹性云服务器上。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaDetachVolume</td>
                    <td>弹性云服务器卸载磁盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerBlockDevices</td>
                    <td>查询弹性云服务器挂载的磁盘信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerVolumeAttachments</td>
                    <td>查询弹性云服务器挂载的磁盘信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerBlockDevice</td>
                    <td>查询弹性云服务器挂载的单个磁盘信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServerBlockDevice</td>
                    <td>修改云服务器云主机挂载的单个磁盘信息。'当前仅支持修改delete_on_termination字段。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServerVolume</td>
                    <td>根据磁盘ID,查询云服务器挂载的单个磁盘信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">租户配额管理</td>
                    <td>ShowServerLimits</td>
                    <td>查询租户配额信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">网卡管理</td>
                    <td>NovaDetachInterface</td>
                    <td>根据指定的Port ID,从云服务器中卸载网卡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteServerNics</td>
                    <td>卸载并删除云服务器中的一张或多张网卡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaAttachInterface</td>
                    <td>给云服务器添加一张网卡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServerInterface</td>
                    <td>更新云服务器网卡挂载信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateServerVirtualIp</td>
                    <td>虚拟IP地址用于为网卡提供第二个IP地址,同时支持与多个弹性云服务器的网卡绑定,从而实现多个弹性云服务器之间的高可用性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddServerNics</td>
                    <td>给云服务器添加一张或多张网卡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeVpc</td>
                    <td>云服务器切换虚拟私有云。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListServerInterfaces</td>
                    <td>查询云服务器网卡信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerInterfaces</td>
                    <td>查询云服务器网卡信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateServerVirtualIp</td>
                    <td>虚拟IP地址用于为网卡提供第二个IP地址,同时支持与多个弹性云服务器的网卡绑定,从而实现多个弹性云服务器之间的高可用性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowServerInterface</td>
                    <td>根据网卡ID,查询云服务器网卡信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeServerNetworkInterface</td>
                    <td>更新云服务器指定网卡属性,当前仅支持更新网卡IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">规格管理</td>
                    <td>ListFlavorSellPolicies</td>
                    <td>查询规格销售策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListFlavors</td>
                    <td>查询系统中可用的弹性云服务器规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaListFlavorsDetails</td>
                    <td>查询云服务器规格信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowFlavor</td>
                    <td>根据云服务器规格ID,查询云服务器规格详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResizeFlavors</td>
                    <td>变更规格时,部分规格的云服务器之间不能互相变更。您可以通过本接口,通过指定弹性云服务器规格,查询该规格可以变更的规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>NovaShowFlavorExtraSpecs</td>
                    <td>查询指定的规格的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">计划事件</td>
                    <td>ListScheduledEvents</td>
                    <td>查询计划事件列表</td>
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
