# BMS MCP Server 


## Version
v0.1.0

## Overview

BMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service BMS. Full-chain management of BMS resources can be carried out based on natural language.

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
                    <td rowspan="1">Job管理</td>
                    <td>ShowJobInfos</td>
                    <td>查询Job的执行状态。对于创建裸金属服务器物理机、挂卸卷等异步API,命令下发后,会返回job_id,通过job_id可以查询任务的执行状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">查询API版本信息</td>
                    <td>ShowVersionsInfo</td>
                    <td>查询裸金属服务器当前所有可用的API版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSpecifiedVersion</td>
                    <td>查询裸金属服务指定接口版本的信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">状态管理</td>
                    <td>ShowServerRemoteConsole</td>
                    <td>获取弹性云服务器VNC远程登录地址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">裸金属服务器二维标签管理</td>
                    <td>BatchDeleteBaremetalServerTags</td>
                    <td>- 为指定云服务器批量删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateBaremetalServerTags</td>
                    <td>- 为指定裸金属服务器批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBaremetalServerTags</td>
                    <td>- 查询指定云服务器的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">裸金属服务器云硬盘管理</td>
                    <td>AttachBaremetalServerVolume</td>
                    <td>裸金属服务器创建成功后,如果发现磁盘不够用或者当前磁盘不满足要求,可以将已有云硬盘挂载给裸金属服务器,作为数据盘使用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachBaremetalServerVolume</td>
                    <td>将挂载至裸金属服务器中的磁盘卸载;对于挂载在系统盘盘位(也就是“/dev/sda”挂载点)上的磁盘,不允许执行卸载操作;对于挂载在数据盘盘位(非“/dev/sda”挂载点)上的磁盘,支持离线卸载和在线卸载(裸金属服务器处于“运行中”状态)磁盘</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBaremetalServerVolumeInfo</td>
                    <td>查询裸金属服务器挂载的磁盘信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">裸金属服务器元数据管理</td>
                    <td>UpdateBaremetalServerMetadata</td>
                    <td>更新裸金属服务器元数据。如果元数据中没有待更新字段,则自动添加该字段。如果元数据中已存在待更新字段,则直接更新字段值;如果元数据中的字段不再请求参数中,则保持不变</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">裸金属服务器密码管理</td>
                    <td>ShowResetPwd</td>
                    <td>查询是否支持一键重置密码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPwdOneClick</td>
                    <td>在裸金属服务器支持一键重置密码功能的前提下,重置裸金属服务器管理帐号(root用户或Administrator用户)的密码。可以通过6.10.1-查询是否支持一键重置密码API查询是否支持一键重置密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWindowsBaremetalServerPwd</td>
                    <td>获取Windows裸金属服务器初始安装时系统生成的管理员帐户(Administrator帐户或Cloudbase-init设置的帐户)随机密码。如果裸金属服务器是通过私有镜像创建的,请确保已安装Cloudbase-init。公共镜像默认已安装该软件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWindowsBareMetalServerPassword</td>
                    <td>清除Windows裸金属服务器初始安装时系统生成的密码记录。清除密码后,不影响裸金属服务器密码登录功能,但不能再使用获取密码功能来查询该裸金属服务器密码。如果裸金属服务器是通过私有镜像创建的,请确保已安装Cloudbase-init。公共镜像默认已安装该软件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">裸金属服务器状态管理</td>
                    <td>BatchStopBaremetalServers</td>
                    <td>根据给定的裸金属服务器ID列表,批量关闭裸金属服务器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartBaremetalServers</td>
                    <td>根据给定的裸金属服务器ID列表,批量启动裸金属服务器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRebootBaremetalServers</td>
                    <td>根据给定的裸金属服务器ID列表,批量重启裸金属服务器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeBaremetalServerName</td>
                    <td>修改裸金属服务器名称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeBaremetalServerOs</td>
                    <td>切换裸金属服务器的操作系统。切换操作系统支持密码或者密钥注入,该接口支持企业项目细粒度权限的校验,具体细粒度请参见 bms:servers:changeOS</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ReinstallBaremetalServerOs</td>
                    <td>重装裸金属服务器的操作系统。快速发放裸金属服务器支持裸金属服务器数据盘不变的情况下,使用原镜像重装系统盘。重装操作系统支持密码或者密钥注入</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">裸金属服务器生命周期管理</td>
                    <td>ListBareMetalServers</td>
                    <td>用户根据设置的请求条件筛选裸金属服务器,并获取裸金属服务器的详细信息。该接口支持查询裸金属服务器计费方式,以及是否被冻结。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBareMetalServerDetails</td>
                    <td>获取裸金属服务器详细信息,该接口支持查询裸金属服务器的计费方式,以及是否被冻结</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBareMetalServersDetail</td>
                    <td>用户根据设置的请求条件筛选裸金属服务器,并获取裸金属服务器的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBareMetalServers</td>
                    <td>创建一台或多台裸金属服务器,裸金属服务器的登录鉴权方式包括两种:密钥对、密码。为安全起见,推荐使用密钥对方式</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">裸金属服务器租户配额管理</td>
                    <td>ShowTenantQuota</td>
                    <td>查询该租户下,所有资源的配额信息,包括已使用配额</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">裸金属服务器网卡管理</td>
                    <td>UpdateBaremetalServerInterfaceAttachments</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBaremetalServerInterfaceAttachments</td>
                    <td>查询裸金属服务器的网卡信息,比如网卡的IP地址、MAC地址</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddServerNics</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServerNics</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">裸金属服务器规格管理</td>
                    <td>ListBaremetalFlavorDetailExtends</td>
                    <td>查询裸金属服务器的规格详情和规格的扩展信息。您可以调用此接口查询“baremetal:extBootType”参数取值,以确认某个规格是否支持快速发放</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
