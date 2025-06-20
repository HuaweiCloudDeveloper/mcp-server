# DBSS MCP Server 


## Version
v0.1.0

## Overview

DBSS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DBSS. Full-chain management of DBSS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Audit Agent | DownloadAuditAgent | Download the audit agent | To be tested |
|  | ListAuditAgent | Query the database agent list | To be tested |
|  | AddAuditAgent | Adding the audit database agent | To be tested |
|  | DeleteAuditAgent | Delete the database agent | To be tested |
|  | SwitchAgent | Enables or disables the Agent audit function. After the function is enabled, the system starts to capture user access information. | To be tested |
| Audit Database | DeleteAuditDatabase | Delete a database | To be tested |
|  | AddRdsDatabase | Adding an RDS database | To be tested |
|  | ListRdsDatabases | Query the RDS database list | To be tested |
|  | ListAuditDatabases | Query the database list | To be tested |
|  | SwitchAuditDatabase | Start and shut down the database | To be tested |
|  | AddAuditDatabase | Adding a self-built database | To be tested |
| Audit Instance | ListAuditInstanceJobs | Query the instance creation task information | To be tested |
|  | UpdateAuditSecurityGroup | Modifying the security group of an instance | To be tested |
|  | RebootAuditInstance | Restart the audit instance | To be tested |
|  | CreateInstancesPeriodOrder | Creating an audit instance in yearly/monthly billing mode | To be tested |
|  | StopAuditInstance | Stop the audit instance | To be tested |
|  | ListAuditInstances | Query the audit instance list | To be tested |
|  | UpdateAuditInstance | Updates audit instance information | To be tested |
|  | StartAuditInstance | Enable an audit instance | To be tested |
| Audit Rule | SwitchRiskRule | Enable or disable risk rules | To be tested |
|  | ListSqlInjectionRules | Query SQL injection rule policies | To be tested |
|  | ShowAuditRuleRisk | Query a specified risk rule policy | To be tested |
|  | ListAuditRuleScopes | Query the audit scope policy list | To be tested |
|  | ListAuditRuleRisks | Query a risk rule policy | To be tested |
|  | ListAuditSensitiveMasks | Query the privacy data anonymization rule | To be tested |
| Data analysis | ListAuditSummaryInfos | Query audit summary information | To be tested |
|  | ListAuditAlarmLog | Query audit alarm information | To be tested |
|  | ListAuditSqls | Query the SQL statement for auditing | To be tested |
| Edge Instance | DeleteInstances | This API is used to delete edge instances in batches. | To be tested |
| Interface to go offline | AddRdsNoAgentDatabase | Add an RDS database. V1 is no longer maintained and will be brought offline. | To be tested |
| Query on the management side | ListAvailabilityZoneInfos | Query AZ information | To be tested |
|  | ShowAuditQuota | Query account quota information | To be tested |
|  | ListEcsSpecification | Query ECS specifications | To be tested |
|  | ListAuditOperateLogs | Query user operation logs | To be tested |
| TMS Label | CountResourceInstanceByTag | Query the number of resource instances by tag | To be tested |
|  | ListProjectResourceTags | Query project tags | To be tested |
|  | ListResourceInstanceByTag | Query the resource instance list by tag | To be tested |
|  | BatchAddResourceTag | Add resource tags in batches | To be tested |
| Tag Management | BatchDeleteResourceTag | This API is used to delete tags from a specified cluster in batches. | To be tested |

