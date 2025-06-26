# LTS MCP Server 


## Version
v0.1.0

## Overview

LTS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service LTS. Full-chain management of LTS resources can be carried out based on natural language.

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
                    <td rowspan="5">AOM容器日志接入LTS</td>
                    <td>DeleteAomMappingRules</td>
                    <td>该接口用于删除lts接入规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAomMappingRules</td>
                    <td>该接口用于查询aom日志所有接入lts规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAomMappingRules</td>
                    <td>该接口用于创建aom日志接入lts规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAomMappingRule</td>
                    <td>该接口用于查询单个aom日志接入lts</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAomMappingRules</td>
                    <td>该接口用于修改接入规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">SDK流式消费开放API</td>
                    <td>ListDetailsConsumerGroup</td>
                    <td>查询消费组详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCursorByTime</td>
                    <td>通过时间查询cursor</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCheckPoint</td>
                    <td>更新消费组位点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConsumerGroup</td>
                    <td>创建消费组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConsumerGroupHeartBeat</td>
                    <td>消费者发送心跳到服务端</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCursorTime</td>
                    <td>通过cursor查询服务端时间</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConsumerGroup</td>
                    <td>查询消费组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLogStreamShards</td>
                    <td>流消费获取所有的query shards</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">SQL告警规则</td>
                    <td>UpdateAlarmRuleStatus</td>
                    <td>改变告警规则状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlAlarmRule</td>
                    <td>该接口用于创建SQL告警,目前每个帐户最多可以创建共200个关键词告警与SQL告警</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlAlarmRules</td>
                    <td>该接口用于查询SQL告警</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlAlarmRule</td>
                    <td>该接口用于删除SQL告警</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSqlAlarmRule</td>
                    <td>该接口用于修改SQL告警</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">主机组管理</td>
                    <td>UpdateHostGroup</td>
                    <td>修改主机组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostGroup</td>
                    <td>查询主机组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHostGroup</td>
                    <td>删除主机组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHostGroup</td>
                    <td>创建主机组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">云模式防护网站管理</td>
                    <td>ListHost</td>
                    <td>查询云模式防护域名列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">仪表盘管理</td>
                    <td>CreateDashboardGroup</td>
                    <td>创建仪表盘分组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDashBoard</td>
                    <td>创建仪表盘</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDashboard</td>
                    <td>删除仪表盘</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">关键词告警规则</td>
                    <td>UpdateKeywordsAlarmRule</td>
                    <td>该接口用于修改关键词告警。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKeywordsAlarmRule</td>
                    <td>该接口用于删除关键词告警。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKeywordsAlarmRule</td>
                    <td>该接口用于创建关键词告警,目前每个帐户最多可以创建共200个关键词告警与SQL告警。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeywordsAlarmRules</td>
                    <td>该接口用于查询关键词告警。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">告警主题</td>
                    <td>ListNotificationTopics</td>
                    <td>该接口用于查询SMN主题</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">告警列表</td>
                    <td>DeleteActiveAlarms</td>
                    <td>该接口用于删除活动告警</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListActiveOrHistoryAlarms</td>
                    <td>该接口用于查询告警列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">多账号日志汇聚</td>
                    <td>UpdateLogConvergeConfig</td>
                    <td>只能由管理员或者委托管理员 ,更新汇聚配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLogConvergeConfig</td>
                    <td>只能由组织管理员或者委托管理员调用 获取组织成员汇聚配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAdminConfig</td>
                    <td>只能由管理员或者委托管理员调用 获取日志汇聚开关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSwitch</td>
                    <td>只能由管理员或者委托管理员调用 修改日志汇聚开关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMemberGroupAndStream</td>
                    <td>只能由管理员或者委托管理员调用,获取组织成员日志组日志流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">快速查询</td>
                    <td>CreateSearchCriterias</td>
                    <td>添加快速查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryAllSearchCriterias</td>
                    <td>查询日志组下所有快速查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCriterias</td>
                    <td>获取快速查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHistorySql</td>
                    <td>查询用户历史sql</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSearchCriterias</td>
                    <td>删除快速查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">日志接入</td>
                    <td>DeleteAccessConfig</td>
                    <td>删除日志接入</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAccessConfig</td>
                    <td>修改日志接入</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgencyAccess</td>
                    <td>新建跨账号日志接入</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccessConfig</td>
                    <td>查询日志接入列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAccessConfig</td>
                    <td>创建日志接入</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">日志流图表</td>
                    <td>ListCharts</td>
                    <td>该接口用于查询日志流图表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">日志流管理</td>
                    <td>UpdateLogStream</td>
                    <td>该接口用于修改指定日志流下的日志存储时长。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogStream</td>
                    <td>该接口用于查询指定日志组下的所有日志流信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogStreams</td>
                    <td>该接口用于查询LTS日志流信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogStream</td>
                    <td>该接口用于创建某个指定日志组下的日志流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogStream</td>
                    <td>该接口用于删除指定日志组下的指定日志流。当该日志流配置了日志转储,需要取消日志转储后才可删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogStreamIndex</td>
                    <td>向指定流创建索引</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">日志管理</td>
                    <td>ListLogContext</td>
                    <td>查询上下文日志 该接口用于查询指定日志前(上文)后(下文)的若干条日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStructuredLogsWithTimeRange</td>
                    <td>该接口用于查询指定日志流下的结构化日志内容(新版)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogHistogram</td>
                    <td>查询关键词搜索条数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopnTrafficStatistics</td>
                    <td>统计top n的日志组或日志流流量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Deletefavorite</td>
                    <td>取消收藏</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTimeLineTrafficStatistics</td>
                    <td>按时间段统计查询资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Createfavorite</td>
                    <td>创建日志收藏</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogs</td>
                    <td>该接口用于查询指定日志流下的日志内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryStructuredLogs</td>
                    <td>该接口用于查询指定日志流下的结构化日志内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">日志组管理</td>
                    <td>ListLogGroups</td>
                    <td>该接口用于查询账号下所有日志组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogGroup</td>
                    <td>该接口用于删除指定日志组。当日志组中的日志流配置了日志转储,需要取消日志转储后才可删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogGroup</td>
                    <td>该接口用于创建一个日志组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogGroup</td>
                    <td>该接口用于修改指定日志组下的日志存储时长。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">日志转储</td>
                    <td>UpdateTransfer</td>
                    <td>该接口用于更新OBS转储,DIS转储,DMS转储。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterDmsKafkaInstance</td>
                    <td>该接口用于注册DMS kafka实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogDumpObs</td>
                    <td>该接口用于将指定的一个或多个日志流的日志转储到OBS服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTransfers</td>
                    <td>该接口用于查询OBS转储,DIS转储,DMS转储配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTransfer</td>
                    <td>该接口用于创建OBS转储,DIS转储,DMS转储。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTransfer</td>
                    <td>该接口用于删除OBS转储,DIS转储,DMS转储。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">标签管理</td>
                    <td>CreateTags</td>
                    <td>添加标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">消息模板管理</td>
                    <td>UpdateNotificationTemplate</td>
                    <td>该接口用于修改通知模板,根据名称进行修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNotificationTemplate</td>
                    <td>该接口用于查询单个通知模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNotificationTemplate</td>
                    <td>该接口用于删除通知模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotificationTemplate</td>
                    <td>该接口用于预览通知模板邮件格式</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotificationTemplates</td>
                    <td>该接口用于查询通知模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNotificationTemplate</td>
                    <td>该接口用于创建通知模板,目前每个帐户最多可以创建共100个通知模板,创建后名称不可修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">消费组管理</td>
                    <td>DeleteConsumerGroup</td>
                    <td>删除指定消费组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">结构化配置</td>
                    <td>DeleteStructTemplate</td>
                    <td>该接口用于删除指定日志流下的结构化配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStructTemplate</td>
                    <td>该接口用于查询结构化模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStructConfig</td>
                    <td>该接口通过结构化模板创建结构化配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStructTemplate</td>
                    <td>该接口用于修改指定日志流下的结构化配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStructTemplate</td>
                    <td>该接口用于查询指定日志流下的结构化配置内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStructTemplate</td>
                    <td>该接口用于创建指定日志流下的结构化配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStructConfig</td>
                    <td>该接口通过结构化模板修改结构化配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBreifStructTemplate</td>
                    <td>该接口用于查询结构化模板简略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">超额采集</td>
                    <td>EnableLogCollection</td>
                    <td>该接口用于将超额采集日志功能打开。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableLogCollection</td>
                    <td>该接口用于将超额采集日志功能关闭。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
