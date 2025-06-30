# RocketMQ MCP Server 


## Version
v0.1.0

## Overview

RocketMQ MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RocketMQ. Full-chain management of RocketMQ resources can be carried out based on natural language.

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
                    <td rowspan="5">Topic管理</td>
                    <td>ListConsumerGroupOfTopic</td>
                    <td>查询主题消费组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTopicStatus</td>
                    <td>查询主题的消息数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTopicOrBatchDeleteTopic</td>
                    <td>创建主题或批量删除主题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOneTopic</td>
                    <td>查询单个主题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRocketInstanceTopics</td>
                    <td>该接口用于查询指定RocketMQ实例的Topic列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">主题操作</td>
                    <td>UpdateTopic</td>
                    <td>更新显示名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTopic</td>
                    <td>删除主题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">元数据迁移</td>
                    <td>ListRocketMqMigrationTask</td>
                    <td>1. 查询实例下所有迁移任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRocketMqMigrationTask</td>
                    <td>新建元数据迁移任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRocketMqMigrationTask</td>
                    <td>删除元数据迁移任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">其他接口</td>
                    <td>ListEngineProducts</td>
                    <td>查询相应引擎的产品规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableZones</td>
                    <td>在创建实例时,需要配置实例所在的可用区ID,可通过该接口查询可用区的ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRocketMQProductCores</td>
                    <td>查询RocketMQ产品规格核数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">参数管理</td>
                    <td>UpdateRocketMqConfigs</td>
                    <td>该接口用于修改RocketMQ配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRocketMqConfigs</td>
                    <td>该接口用于查询RocketMQ配置,若成功则返回配置的相关信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">实例管理</td>
                    <td>ShowInstanceNodes</td>
                    <td>查询实例节点信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartInstance</td>
                    <td>重启指定实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">标签管理</td>
                    <td>ShowRocketmqProjectTags</td>
                    <td>查询项目标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateOrDeleteRocketmqTag</td>
                    <td>批量添加或删除实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRocketmqTags</td>
                    <td>查询实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">消息管理</td>
                    <td>ExportDlqMessage</td>
                    <td>导出死信消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMessages</td>
                    <td>查询消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendDlqMessage</td>
                    <td>重发死信消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMessageTrace</td>
                    <td>查询消息轨迹。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateConsumedMessage</td>
                    <td>消费验证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">消费组管理</td>
                    <td>UpdateConsumerGroup</td>
                    <td>修改指定消费组参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConsumerListOrDetails</td>
                    <td>查询消费列表或详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConsumerGroups</td>
                    <td>查询消费组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConsumerConnections</td>
                    <td>查询消费组内消费者列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConsumerGroup</td>
                    <td>删除指定消费组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConsumerGroupOrBatchDeleteConsumerGroup</td>
                    <td>创建消费组或批量删除消费组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetConsumeOffset</td>
                    <td>重置消费进度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateConsumerGroup</td>
                    <td>批量修改消费组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGroup</td>
                    <td>查询指定消费组详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">独享实例管理</td>
                    <td>DeleteInstance</td>
                    <td>删除WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>查询WAF独享引擎信息。独享模式只在部分局点支持,包括:华北-北京四、华东-上海一、华南-广州、华南-深圳 、中国-香港、亚太-曼谷、 亚太-新加坡。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">生命周期管理</td>
                    <td>ListBrokers</td>
                    <td>查询代理列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableDns</td>
                    <td>开启RocketMQ实例域名访问能力。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstance</td>
                    <td>修改实例的名称和描述信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceByEngine</td>
                    <td>创建实例,该接口支持创建按需和包周期两种计费方式的实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteInstances</td>
                    <td>批量删除实例。**实例删除后,实例中原有的数据将被删除,且没有备份,请谨慎操作。**</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>查询租户的实例列表,支持按照条件查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">用户管理</td>
                    <td>ListUser</td>
                    <td>查询用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUser</td>
                    <td>修改用户参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUser</td>
                    <td>查询用户详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopicAccessPolicy</td>
                    <td>查询主题的授权用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUser</td>
                    <td>创建用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConsumeGroupAccessPolicy</td>
                    <td>查询消费组的授权用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUser</td>
                    <td>删除用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">规格变更管理</td>
                    <td>ResizeInstance</td>
                    <td>实例规格变更。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEngineInstanceExtendProductInfo</td>
                    <td>查询实例的扩容规格列表。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
