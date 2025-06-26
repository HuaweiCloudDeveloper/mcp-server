# CBH MCP Server 


## Version
v0.1.0

## Overview

CBH MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CBH. Full-chain management of CBH resources can be carried out based on natural language.

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
                    <td rowspan="1">DDM实例管理</td>
                    <td>UpdateInstanceSecurityGroup</td>
                    <td>修改DDM实例安全组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">云堡垒机信息查询</td>
                    <td>SearchQuota</td>
                    <td>查询云堡垒机配额信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAvailableZoneInfo</td>
                    <td>获取云堡垒机服务可用分区信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNetworkConfiguration</td>
                    <td>检查云堡垒机实例网络信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCbhInstance</td>
                    <td>获取当前租户下的云堡垒机实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQuotaStatus</td>
                    <td>获取当前租户所选择的可用分区、性能规格所对应的弹性云服务器是否可用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">云堡垒机管理</td>
                    <td>StopCbhInstance</td>
                    <td>关闭云堡垒机实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetLoginMethod</td>
                    <td>重置admin用户多因子认证方式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeCbhInstance</td>
                    <td>升级云堡垒机实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InstallCbhEip</td>
                    <td>云堡垒机实例绑定弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UninstallCbhEip</td>
                    <td>云堡垒机实例解绑弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartCbhInstance</td>
                    <td>启动云堡垒机实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartCbhInstance</td>
                    <td>重启云堡垒机实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeInstanceNetwork</td>
                    <td>修改云堡垒机实例网络。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">其他接口</td>
                    <td>ListAvailableZones</td>
                    <td>在创建实例时,需要配置实例所在的可用区ID,可通过该接口查询可用区的ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">委托授权</td>
                    <td>ShowAuthorization</td>
                    <td>获取租户给云堡垒机服务委托授权信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterAuthorization</td>
                    <td>租户创建或取消云堡垒机服务的委托授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">实例管理</td>
                    <td>StopInstance</td>
                    <td>实例进行关机,通过暂时停止按需实例以节省费用,实例默认停止七天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPassword</td>
                    <td>重置密码(只针对开通SSL的实例)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">操作管理</td>
                    <td>ResetInstancePassword</td>
                    <td>重置云堡垒机实例web登录admin用户密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LoginInstanceAdmin</td>
                    <td>用户登录堡垒机实例admin的console。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LoginInstance</td>
                    <td>IAM用户登录堡垒机实例console。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebootInstance</td>
                    <td>重启云堡垒机实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOmUrl</td>
                    <td>获取运维链接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetInstanceLoginMethod</td>
                    <td>重置堡垒机实例admin用户登录方式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollbackInstance</td>
                    <td>回退升级的云堡垒机实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeInstanceType</td>
                    <td>修改单机堡垒机实例类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">数据库管理</td>
                    <td>StartInstance</td>
                    <td>启动数据库,同时支持节点级别的启动操作</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">标签管理</td>
                    <td>ListInstancesByTag</td>
                    <td>使用标签过滤实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateInstanceTag</td>
                    <td>操作堡垒机实例资源标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceTags</td>
                    <td>查询指定实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountInstancesByTag</td>
                    <td>统计符合标签条件的实例数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">流水线管理</td>
                    <td>ShowInstanceStatus</td>
                    <td>检查流水线创建状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">独享实例管理</td>
                    <td>CreateInstance</td>
                    <td>创建WAF独享引擎实例。独享模式支持的局点包括:华东-青岛、中东-利雅得、华北-北京一、华北-北京四、华北-乌兰察布一、华东-上海一、华东-上海二、华南-广州、华南-深圳、中国-香港、西南-贵阳一、亚太-曼谷、 亚太-新加坡、非洲约翰内斯堡、土耳其-伊斯坦布尔;普通租户类独享支持的局点:华北-北京四、华东-上海一、华南-广州、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>删除WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">生命周期管理</td>
                    <td>UpgradeInstance</td>
                    <td>实例内核升级</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>查询租户的实例列表,支持按照条件查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">网络管理</td>
                    <td>InstallInstanceEip</td>
                    <td>云堡垒机实例绑定弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UninstallInstanceEip</td>
                    <td>为云堡垒机实例解绑弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchInstanceVpc</td>
                    <td>切换堡垒机虚拟私有云</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">获取IAM登录实例链接</td>
                    <td>LoginCbh</td>
                    <td>获取当前IAM用户登录堡垒机的免登录链接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">规格变更管理</td>
                    <td>ResizeInstance</td>
                    <td>实例规格变更。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">规格管理</td>
                    <td>ListSpecifications</td>
                    <td>查询云堡垒机规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">订单管理</td>
                    <td>CreateCbh</td>
                    <td>创建云堡垒机实例。(创建云堡垒机实例订单前,先调用此接口)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceOrder</td>
                    <td>创建云堡垒机实例订单。(调用此接口前先调用创建云堡垒机实例接口)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeInstanceOrder</td>
                    <td>创建变更云堡垒机实例订单。(调用此接口前先调用创建变更云堡垒机实例任务接口,当前接口未开放)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowQuota</td>
                    <td>查询单租户在VPC服务下的网络资源配额,包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额,vpn配额等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额管理</td>
                    <td>ShowEcsQuota</td>
                    <td>获取当前租户所选择的可用分区里的堡垒机ECS规格是否可用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像标签</td>
                    <td>ListTags</td>
                    <td>根据不同条件查询镜像标签列表信息。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
