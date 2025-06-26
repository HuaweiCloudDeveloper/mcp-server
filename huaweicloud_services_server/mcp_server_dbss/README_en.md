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
                    <td rowspan="5">Audit Agent</td>
                    <td>DownloadAuditAgent</td>
                    <td>Download the audit agent</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditAgent</td>
                    <td>Query the database agent list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAuditAgent</td>
                    <td>Adding the audit database agent</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAuditAgent</td>
                    <td>Delete the database agent</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchAgent</td>
                    <td>Enables or disables the Agent audit function. After the function is enabled, the system starts to capture user access information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Audit Database</td>
                    <td>DeleteAuditDatabase</td>
                    <td>Delete a database</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddRdsDatabase</td>
                    <td>Adding an RDS database</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRdsDatabases</td>
                    <td>Query the RDS database list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditDatabases</td>
                    <td>Query the database list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchAuditDatabase</td>
                    <td>Start and shut down the database</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAuditDatabase</td>
                    <td>Adding a self-built database</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Audit Instance</td>
                    <td>ListAuditInstanceJobs</td>
                    <td>Query the instance creation task information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAuditSecurityGroup</td>
                    <td>Modifying the security group of an instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebootAuditInstance</td>
                    <td>Restart the audit instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstancesPeriodOrder</td>
                    <td>Creating an audit instance in yearly/monthly billing mode</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopAuditInstance</td>
                    <td>Stop the audit instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditInstances</td>
                    <td>Query the audit instance list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAuditInstance</td>
                    <td>Updates audit instance information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartAuditInstance</td>
                    <td>Enable an audit instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Audit Rule</td>
                    <td>SwitchRiskRule</td>
                    <td>Enable or disable risk rules</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSqlInjectionRules</td>
                    <td>Query SQL injection rule policies</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAuditRuleRisk</td>
                    <td>Query a specified risk rule policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditRuleScopes</td>
                    <td>Query the audit scope policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditRuleRisks</td>
                    <td>Query a risk rule policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditSensitiveMasks</td>
                    <td>Query the privacy data anonymization rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Data analysis</td>
                    <td>ListAuditSummaryInfos</td>
                    <td>Query audit summary information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditAlarmLog</td>
                    <td>Query audit alarm information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditSqls</td>
                    <td>Query the SQL statement for auditing</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Edge Instance</td>
                    <td>DeleteInstances</td>
                    <td>This API is used to delete edge instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Interface to go offline</td>
                    <td>AddRdsNoAgentDatabase</td>
                    <td>Add an RDS database. V1 is no longer maintained and will be brought offline.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Query on the management side</td>
                    <td>ListAvailabilityZoneInfos</td>
                    <td>Query AZ information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAuditQuota</td>
                    <td>Query account quota information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEcsSpecification</td>
                    <td>Query ECS specifications</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditOperateLogs</td>
                    <td>Query user operation logs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">TMS Label</td>
                    <td>CountResourceInstanceByTag</td>
                    <td>Query the number of resource instances by tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectResourceTags</td>
                    <td>Query project tags</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceInstanceByTag</td>
                    <td>Query the resource instance list by tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddResourceTag</td>
                    <td>Add resource tags in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tag Management</td>
                    <td>BatchDeleteResourceTag</td>
                    <td>This API is used to delete tags from a specified cluster in batches.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
