# DAS MCP Server 


## Version
v0.1.0

## Overview

DAS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DAS. Full-chain management of DAS resources can be carried out based on natural language.

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
                    <td rowspan="52">云DBA</td>
                    <td>ChangeChargeMode</td>
                    <td>设置付费实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFullSqlTasks</td>
                    <td>全量SQL开关打开后,查询SQL洞察任务列表。该功能仅支持付费实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlSwitchStatus</td>
                    <td>查询DAS收集全量SQL和慢SQL的开关状态。该功能仅支持付费实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSqlLimitRules</td>
                    <td>删除SQL限流规则。目前仅支持MySQL和PostgreSQL数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTuning</td>
                    <td>获取诊断结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSqlLimitRules</td>
                    <td>添加SQL限流规则。目前仅支持MySQL和PostgreSQL数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlExecutionPlan</td>
                    <td>查询SQL执行计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlLimitRules</td>
                    <td>查询SQL限流规则。目前仅支持MySQL和PostgreSQL数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetThresholdForMetric</td>
                    <td>设置指标阈值</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SynchronizeInstances</td>
                    <td>同步实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudDbaInstances</td>
                    <td>获取DAS云DBA实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProcesses</td>
                    <td>支持根据数据库、用户查询实例会话列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportFullSqlDetails</td>
                    <td>全量SQL开关打开后,创建SQL洞察任务,支持按节点、用户名、数据库、操作类型等导出全量SQL明细数据。该功能仅支持付费实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRiskItems</td>
                    <td>查询资源风险实例风险项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeSqlSwitch</td>
                    <td>打开或者关闭DAS收集全量SQL开关,开启后,实例的性能损耗在5%以内。开启全量SQL后,本服务会对SQL的文本内容进行存储,以便进行分析。用户可自行设置全量SQL的保存时间范围,到期后会自动删除;如果未设置,数据默认保留7天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceTopSlowLog</td>
                    <td>查询实例的TOP慢SQL列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportTopSqlTrendDetails</td>
                    <td>TopSQL开关打开后,导出SQL执行耗时区间数据。该功能仅支持付费实例。查询时间间隔最长六小时。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeTransactionSwitchStatus</td>
                    <td>开启/关闭历史事务开关,仅支持MySQL引擎,并且依赖开启全量SQL或者慢SQL功能</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlExplain</td>
                    <td>查询SQL执行计划。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTuning</td>
                    <td>执行SQL诊断,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSpaceAnalysisTask</td>
                    <td>创建空间分析任务,如触发重新分析,支持MySQL和GaussDB(for MySQL)引擎</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportSlowSqlStatistics</td>
                    <td>慢SQL开关打开后,导出慢SQL统计数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInnodbLocks</td>
                    <td>查询InnoDB锁等待列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportSqlStatements</td>
                    <td>全量SQL开关打开后,一次性导出指定时间范围内的全量SQL数据,支持分页滚动获取。该功能仅支持付费实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTransactionSwitchStatus</td>
                    <td>查询历史事务开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopSlowLog</td>
                    <td>查询TOP慢SQL列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProcess</td>
                    <td>查杀会话。支持按照用户、数据库、会话列表查杀会话,三个条件至少指定一个。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterDbUser</td>
                    <td>此接口是将数据库用户和密码注册进DAS系统,同时会返回一个数据库用户ID ,后续调用其他接口时(如查询实例会话列表接口)需要用到此数据库用户ID。密码为加密存储,且仅用于DAS API相关功能。此接口不会在数据库实例上创建数据库用户对象。请确保输入的用户名和密码是已经存在并且是正确的。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportSlowQueryLogs</td>
                    <td>DAS收集慢SQL开关打开后,一次性导出指定时间范围内的慢SQL数据,支持分页滚动获取。免费实例仅支持查看最近一小时数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDbUser</td>
                    <td>查询注册在DAS里的数据库用户信息。此接口不能查询数据库实例上的数据库用户对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSpaceAnalysis</td>
                    <td>获取空间分析数据列表。实例级别数据来源于文件系统,库级别和表级别数据来源于information_schema.tables表。空间&amp;元数据分析最多分析10000张表,若缺少库表空间数据,可能是因为数据库实例表个数过多或者账号未保存密码。如果为保存密码,请使用用户管理接口或页面录入数据库账号。 支持MySQL、GaussDB(for MySQL)和SQLServer引擎。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportSlowSqlTrendDetails</td>
                    <td>慢SQL开关打开后,导出慢SQL数量趋势。免费实例仅支持查看最近一小时数据。查询时间间隔最长一天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ParseSqlLimitRules</td>
                    <td>根据原始SQL生成SQL限流关键字,目前支持MySQL、MariaDB、GaussDB(for MySQL)三种引擎。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceMultiNodesSingleMetric</td>
                    <td>获取多节点单指标数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetadataLocks</td>
                    <td>查询元数据锁列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRiskTrend</td>
                    <td>查询资源风险实例风险趋势</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDbUser</td>
                    <td>修改注册在DAS里的数据库用户名和密码。此接口不会修改数据库实例上的数据库用户对象的用户名和密码。请确保输入的用户名和密码是已经存在并且是正确的。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHealthReportTask</td>
                    <td>查询实例健康诊断报告列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlLimitJobInfo</td>
                    <td>查询指定ID的SQL限流任务信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportTopRiskInstances</td>
                    <td>导出TOP风险实例列表,支持查看最近24小时数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddFullSqlTask</td>
                    <td>创建全量SQL明细解析任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceDistribution</td>
                    <td>查询实例分布情况</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceHealthReport</td>
                    <td>获取实例健康诊断报告内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlLimitSwitchStatus</td>
                    <td>查询SQL限流的开关状态。目前仅支持MySQL实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTransactions</td>
                    <td>查询历史事务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeSqlLimitSwitchStatus</td>
                    <td>设置SQL限流开关状态。目前仅支持MySQL数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSqlLimitRules</td>
                    <td>修改SQL限流规则。目前仅支持PostgreSQL数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceNodesInfo</td>
                    <td>获取单个实例节点信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHealthReportTask</td>
                    <td>创建实例健康诊断任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetricNamesSupport</td>
                    <td>多节点单指标支持指标信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportTopSqlTemplatesDetails</td>
                    <td>TopSQL开关打开后,导出TopSQL模板列表。该功能仅支持付费实例。查询时间间隔最长一小时。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportSlowSqlTemplatesDetails</td>
                    <td>慢SQL开关打开后,导出慢SQL模板列表。免费实例仅支持查看最近一小时数据。查询时间间隔最长一天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">开发工具</td>
                    <td>CancelShareConnections</td>
                    <td>删除共享链接,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceConnection</td>
                    <td>创建实例连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateShareConnections</td>
                    <td>设置共享链接,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">查询版本操作</td>
                    <td>ShowApiVersion</td>
                    <td>查询指定的标签管理服务API版本号详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiVersions</td>
                    <td>查询标签管理服务的API版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">目标连接管理</td>
                    <td>ListConnections</td>
                    <td>查询目标连接列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">管理数据库和用户(MySQL)</td>
                    <td>DeleteDbUser</td>
                    <td>删除数据库用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbUsers</td>
                    <td>查询数据库用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowQuotas</td>
                    <td>查询当前项目下资源配额情况。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
