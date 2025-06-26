# DBSS MCP Server 


## Version
v0.1.0

## Overview

DBSS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DBSS. Full-chain management of DBSS resources can be carried out based on natural language.

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
                    <td rowspan="4">TMS标签</td>
                    <td>CountResourceInstanceByTag</td>
                    <td>根据标签查询资源实例数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectResourceTags</td>
                    <td>查询项目标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceInstanceByTag</td>
                    <td>根据标签查询资源实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddResourceTag</td>
                    <td>批量添加资源标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">审计Agent</td>
                    <td>DownloadAuditAgent</td>
                    <td>下载审计Agent</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditAgent</td>
                    <td>查询数据库Agent列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAuditAgent</td>
                    <td>添加审计数据库Agent</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAuditAgent</td>
                    <td>删除数据库Agent</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchAgent</td>
                    <td>用于开启和关闭Agent审计的功能,当开启后,开始抓取用户的访问信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">审计实例</td>
                    <td>ListAuditInstanceJobs</td>
                    <td>查询实例创建任务信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAuditSecurityGroup</td>
                    <td>修改实例安全组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebootAuditInstance</td>
                    <td>重启审计实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstancesPeriodOrder</td>
                    <td>包年包月计费模式创建审计实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopAuditInstance</td>
                    <td>关闭审计实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditInstances</td>
                    <td>查询审计实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAuditInstance</td>
                    <td>更新审计实例信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartAuditInstance</td>
                    <td>开启审计实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">审计数据库</td>
                    <td>DeleteAuditDatabase</td>
                    <td>删除数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddRdsDatabase</td>
                    <td>添加RDS数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRdsDatabases</td>
                    <td>查询RDS数据库列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditDatabases</td>
                    <td>查询数据库列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchAuditDatabase</td>
                    <td>开启关闭数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAuditDatabase</td>
                    <td>添加自建数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">审计规则</td>
                    <td>SwitchRiskRule</td>
                    <td>开启关闭风险规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlInjectionRules</td>
                    <td>查询SQL注入规则策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAuditRuleRisk</td>
                    <td>查询指定风险规则策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditRuleScopes</td>
                    <td>查询审计范围策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditRuleRisks</td>
                    <td>查询风险规则策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditSensitiveMasks</td>
                    <td>查询隐私数据脱敏规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">待下线接口</td>
                    <td>AddRdsNoAgentDatabase</td>
                    <td>添加RDS数据库。V1版本已不再维护,待下线。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">数据分析</td>
                    <td>ListAuditSummaryInfos</td>
                    <td>查询审计汇总信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditAlarmLog</td>
                    <td>查询审计告警信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditSqls</td>
                    <td>查询审计SQL语句</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">标签管理</td>
                    <td>BatchDeleteResourceTag</td>
                    <td>为指定集群批量删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">管理侧查询</td>
                    <td>ListAvailabilityZoneInfos</td>
                    <td>查询可用区信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAuditQuota</td>
                    <td>查询账户配额信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEcsSpecification</td>
                    <td>查询ECS服务器规格信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditOperateLogs</td>
                    <td>查询用户操作日志信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">边缘实例</td>
                    <td>DeleteInstances</td>
                    <td>批量删除边缘实例。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
