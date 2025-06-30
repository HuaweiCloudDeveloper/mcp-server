# Kafka MCP Server 


## Version
v0.1.0

## Overview

Kafka MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service Kafka. Full-chain management of Kafka resources can be carried out based on natural language.

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
                    <td rowspan="9">Smart Connect</td>
                    <td>PauseConnectorTask</td>
                    <td>暂停Smart Connect任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartConnectorTask</td>
                    <td>用于**启动未启动的Smart Connect任务**以及**重启已暂停或者运行中的Smart Connect任务**。注意,重启Smart Connect任务将重置同步进度,并重新开始同步任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConnectorTask</td>
                    <td>查询Smart Connector任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnector</td>
                    <td>介绍按需实例如何关闭Smart Connect。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConnectorTasks</td>
                    <td>查询Smart Connect任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnectorTask</td>
                    <td>删除Smart Connector任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResumeConnectorTask</td>
                    <td>启动已暂停的Smart Connect任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnector</td>
                    <td>开启Smart Connect,提交创建Smart Connect节点任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnectorTask</td>
                    <td>创建Smart Connect任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">主题管理</td>
                    <td>DeleteKafkaTopicQuota</td>
                    <td>该接口用于向Kafka实例提交删除topic级别的流控任务,若成功则返回流控任务的job_id。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopicPartitions</td>
                    <td>查询Topic的分区列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceTopicDetail</td>
                    <td>查询Kafka实例Topic详细信息。(单个实例调用不要超过1s一次)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceTopic</td>
                    <td>该接口用于向Kafka实例创建Topic。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKafkaTopicQuota</td>
                    <td>该接口用于向Kafka实例提交创建topic级别的流控任务,若成功则返回流控任务的job_id。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaTopicQuota</td>
                    <td>该接口用于查询topic级别的流控任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopicProducers</td>
                    <td>查询Topic的当前生产者列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendKafkaMessage</td>
                    <td>在控制台发送指定消息到Kafka实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceTopics</td>
                    <td>该接口用于查询指定Kafka实例的Topic详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceTopic</td>
                    <td>修改Kafka实例Topic</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyKafkaTopicQuota</td>
                    <td>该接口用于向Kafka实例提交修改topic级别的流控任务,若成功则返回流控任务的job_id。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteInstanceTopic</td>
                    <td>该接口用于向Kafka实例批量删除Topic。批量删除多个Topic时,部分删除成功,部分失败,此时接口返回删除成功,并在返回中显示删除失败的Topic信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">其他接口</td>
                    <td>ListAvailableZones</td>
                    <td>在创建实例时,需要配置实例所在的可用区ID,可通过该接口查询可用区的ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaProductCores</td>
                    <td>查询Kafka产品规格核数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCesHierarchy</td>
                    <td>查询实例在CES的监控层级关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEngineProducts</td>
                    <td>查询相应引擎的产品规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMaintainWindows</td>
                    <td>查询维护时间窗开始时间和结束时间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">后台任务管理</td>
                    <td>ShowBackgroundTask</td>
                    <td>查询后台任务管理中的指定记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackgroundTasks</td>
                    <td>查询实例的后台任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackgroundTask</td>
                    <td>删除后台任务管理中的指定记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">实例管理</td>
                    <td>ShowCoordinators</td>
                    <td>查询Kafka实例的协调器信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKafkaPortProtocol</td>
                    <td>修改Kafka的内网或者公网接入方式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKafkaReassignmentTask</td>
                    <td>该接口用于向Kafka实例提交分区平衡任务,若成功则返回分区平衡任务的job id。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaTopicPartitionDiskusage</td>
                    <td>查询topic在Broker上磁盘占用情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateReassignmentTask</td>
                    <td>该接口用于向Kafka实例提交分区平衡任务或计算分区平衡预估时间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetManagerPassword</td>
                    <td>重置Manager密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPassword</td>
                    <td>重置密码(只针对开通SSL的实例)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKafkaUserClientQuotaTask</td>
                    <td>该接口用于向Kafka实例提交删除用户、客户端级别的流控任务,若成功则返回流控任务的job_id。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartManager</td>
                    <td>重启Manager。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKafkaUserClientQuotaTask</td>
                    <td>该接口用于向Kafka实例提交创建用户、客户端级别的流控任务,若成功则返回流控任务的job_id。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceAutoCreateTopic</td>
                    <td>开启或关闭实例自动创建topic功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCluster</td>
                    <td>查询Kafka集群元数据信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CloseKafkaManager</td>
                    <td>关闭Kafka Manager,相应的原来开放出的management相关接口也将不可用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceCrossVpcIp</td>
                    <td>修改实例跨VPC访问的内网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTopicReplica</td>
                    <td>修改Kafka实例Topic分区的副本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKafkaUserClientQuotaTask</td>
                    <td>该接口用于向Kafka实例提交修改用户、客户端级别的流控任务,若成功则返回流控任务的job_id。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaUserClientQuota</td>
                    <td>该接口用于向Kafka实例查询流控的配置,若成功则返回流控配置的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">应用权限管理</td>
                    <td>UpdateTopicAccessPolicy</td>
                    <td>更新Topic权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">标签管理</td>
                    <td>BatchCreateOrDeleteKafkaTag</td>
                    <td>批量添加或删除实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaProjectTags</td>
                    <td>查询项目标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaTags</td>
                    <td>查询实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">消息管理</td>
                    <td>ShowPartitionEndMessage</td>
                    <td>查询分区最新消息的位置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceMessages</td>
                    <td>查询消息的偏移量和消息内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMessages</td>
                    <td>查询分区指定时间段的消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPartitionBeginningMessage</td>
                    <td>查询分区最早消息的位置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPartitionMessage</td>
                    <td>查询分区指定偏移量的消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKafkaMessage</td>
                    <td>Kafka删除消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">消费组管理</td>
                    <td>DeleteInstanceConsumerGroup</td>
                    <td>删除指定消费组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetMessageOffsetWithEngine</td>
                    <td>Kafka实例不支持在线重置消费进度。在执行重置消费进度之前,必须停止被重置消费组客户端。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConsumerGroupOffsets</td>
                    <td>删除消费组在指定Topic的消费位点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKafkaConsumerGroup</td>
                    <td>实例创建消费组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConsumerGroupMessageOffset</td>
                    <td>查询消费组消息位点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConsumerGroups</td>
                    <td>查询消费组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConsumerGroup</td>
                    <td>修改指定消费组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteGroup</td>
                    <td>该接口用于向Kafka实例批量删除消费组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConsumerGroupTopics</td>
                    <td>查询指定消费组的Topic。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGroups</td>
                    <td>查询消费组信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceGroup</td>
                    <td>修改所有消费组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConsumerGroup</td>
                    <td>查询指定消费组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConsumerGroupMembers</td>
                    <td>查询指定消费组的消费成员。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">独享实例管理</td>
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
                    <td rowspan="9">生命周期管理</td>
                    <td>ShowInstanceConfigs</td>
                    <td>获取实例配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRestartOrDeleteInstances</td>
                    <td>批量重启或删除实例。</td>
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
                    <td>ModifyInstanceConfigs</td>
                    <td>修改实例配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostPaidKafkaInstance</td>
                    <td>创建实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
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
                    <td rowspan="6">用户管理</td>
                    <td>CreateInstanceUser</td>
                    <td>创建Kafka实例的用户,用户可连接开启SASL的Kafka实例。 2023年7月15日前创建的Kafka实例,一个实例最多创建20个用户。2023年7月15日及以后创建的Kafka实例,一个实例最多创建500个用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTopicAccessPolicy</td>
                    <td>查询用户权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceUser</td>
                    <td>修改用户参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteInstanceUsers</td>
                    <td>批量删除Kafka实例的用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceUsers</td>
                    <td>查询用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetUserPasswrod</td>
                    <td>重置用户密码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">规格变更管理</td>
                    <td>ShowEngineInstanceExtendProductInfo</td>
                    <td>查询实例的扩容规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKafkaInstanceExtendProductInfo</td>
                    <td>查询实例的扩容规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeKafkaInstance</td>
                    <td>实例规格变更。当前通过调用API,只支持按需实例进行实例扩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeEngineInstance</td>
                    <td>实例规格变更。当前通过调用API,只支持按需实例进行实例扩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">诊断管理</td>
                    <td>ShowDiagnosisPreCheck</td>
                    <td>消息积压诊断预检查</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMessageDiagnosisReport</td>
                    <td>查询诊断报告详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMessageDiagnosisTask</td>
                    <td>创建消息积压诊断任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMessageDiagnosisReports</td>
                    <td>查询消息积压诊断报告列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteMessageDiagnosisReports</td>
                    <td>批量删除消息积压诊断报告</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
