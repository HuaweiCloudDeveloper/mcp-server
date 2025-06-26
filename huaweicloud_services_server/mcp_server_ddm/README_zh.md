# DDM MCP Server 


## Version
v0.1.0

## Overview

DDM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DDM. Full-chain management of DDM resources can be carried out based on natural language.

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
                    <td rowspan="5">DDM会话管理</td>
                    <td>ExecuteKillPhysicalProcesses</td>
                    <td>kill物理会话</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProcessesAuditLog</td>
                    <td>查询kill会话审计日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLogicalProcesses</td>
                    <td>查询逻辑会话列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPhysicalProcesses</td>
                    <td>查询物理会话列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteKillLogicalProcesses</td>
                    <td>kill逻辑会话</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">DDM实例管理</td>
                    <td>UpdateReadAndWriteStrategy</td>
                    <td>修改DDM已关联的数据库实例的读策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandDdmInstanceNodes</td>
                    <td>对指定的DDM实例的节点个数进行扩容,支持按需实例与包周期实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceParam</td>
                    <td>查询DDM指定实例的参数详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDdmEngines</td>
                    <td>查询DDM引擎信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDatabaseInfo</td>
                    <td>同步当前DDM实例已关联的所有DN实例配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNode</td>
                    <td>查询DDM实例节点详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGroup</td>
                    <td>创建组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceParam</td>
                    <td>修改DDM实例参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceSecurityGroup</td>
                    <td>修改DDM实例安全组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDdmJobResult</td>
                    <td>获取指定ID的任务信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGroup</td>
                    <td>获取实例组信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeFlavor</td>
                    <td>变更DDM实例规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDdmFlavors</td>
                    <td>查询DDM可用区规格信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEngines</td>
                    <td>查询DDM引擎信息详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDdmInstance</td>
                    <td>删除指定的DDM实例,释放该实例的所有资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebuildConfig</td>
                    <td>DDM实例跨region容灾场景下,针对目标DDM实例实现表数据reload,使数据同步。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandInstanceNodes</td>
                    <td>对指定的DDM实例的节点个数进行扩容,支持按需实例与包周期实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">DDM帐号管理</td>
                    <td>ResetAdministrator</td>
                    <td>首次调用时新建DDM管理员帐号并设置密码。后续调用时仅更新管理员密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetUserPassword</td>
                    <td>重置现有DDM帐号的密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUsers</td>
                    <td>DDM帐号用于连接和管理逻辑库。一个DDM实例最多能创建100个DDM帐号,一个DDM帐号可以关联多个逻辑库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">DDM监控管理</td>
                    <td>ListSlowLog</td>
                    <td>查询指定时间段内在DDM实例上执行过的慢sql相关信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReadWriteRatio</td>
                    <td>查询指定时间段内在DDM实例的读写次数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">DDM逻辑库管理</td>
                    <td>ShowDatabase</td>
                    <td>查询指定逻辑库的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDdmDatabase</td>
                    <td>创建DDM逻辑库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableRdsList</td>
                    <td>查询创建逻辑库可选取的数据库实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDdmDatabase</td>
                    <td>删除指定的逻辑库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">OpenStack - API版本信息</td>
                    <td>ListApiVersion</td>
                    <td>返回当前API所有可用的版本(仅针对OpenStack原生接口)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">参数配置</td>
                    <td>ListDdmConfigurations</td>
                    <td>获取参数模板列表,包括所有DDM的默认参数模板和用户创建的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfiguration</td>
                    <td>获取指定参数模板的参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">实例管理</td>
                    <td>ShrinkInstanceNodes</td>
                    <td>删除实例的节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartInstance</td>
                    <td>重启指定实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateWeakPassword</td>
                    <td>校验数据库root用户密码的安全性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceName</td>
                    <td>修改实例名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">引擎版本和规格</td>
                    <td>ListFlavors</td>
                    <td>查询数据库规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">数据库安全性</td>
                    <td>SwitchSsl</td>
                    <td>设置SSL数据加密。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">版本管理</td>
                    <td>ChangeDatabaseVersion</td>
                    <td>变更内核版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRiskInfo</td>
                    <td>内核版本风险提醒</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseAvailableVersions</td>
                    <td>查询可变更内核版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollBackDatabaseVersion</td>
                    <td>回滚内核版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">独享实例管理</td>
                    <td>CreateInstance</td>
                    <td>创建WAF独享引擎实例。独享模式支持的局点包括:华东-青岛、中东-利雅得、华北-北京一、华北-北京四、华北-乌兰察布一、华东-上海一、华东-上海二、华南-广州、华南-深圳、中国-香港、西南-贵阳一、亚太-曼谷、 亚太-新加坡、非洲约翰内斯堡、土耳其-伊斯坦布尔;普通租户类独享支持的局点:华北-北京四、华东-上海一、华南-广州、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>查询WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>删除WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">生命周期管理</td>
                    <td>ListInstances</td>
                    <td>查询租户的实例列表,支持按照条件查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">用户管理</td>
                    <td>UpdateUser</td>
                    <td>修改用户参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUser</td>
                    <td>删除用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">管理数据库和用户(MySQL)</td>
                    <td>DeleteDatabase</td>
                    <td>删除数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabases</td>
                    <td>查询数据库列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabase</td>
                    <td>创建数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">联盟管理</td>
                    <td>ListNodes</td>
                    <td>功能描述:用户可以使用该接口查询联盟可信节点(包含聚合节点和计算节点)列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">获取日志信息</td>
                    <td>ListSlowLogs</td>
                    <td>查询数据库慢日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资产管理</td>
                    <td>ListUsers</td>
                    <td>查询账号的服务器列表</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
