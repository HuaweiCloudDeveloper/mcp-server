# CodeArtsInspector MCP Server 


## Version
v0.1.0

## Overview

CodeArtsInspector MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeArtsInspector. Full-chain management of CodeArtsInspector resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Cluster management interface | ListHosts | This API is used to query details about the host list in the input cluster. | To be tested |
| Group | DeleteGroup | Delete a code group | To be tested |
| Protection Website Management in Cloud Mode | DeleteHost | Delete the domain name in cloud mode. | To be tested |
| Service Job Management | CreateTasks | This API is used to create a service job. | To be tested |
| host_groups | ListGroups | Obtain the host group list | To be tested |
|  | AddGroup | Create host groups in batches | To be tested |
| host_results | ListHostResults | Obtain the host vulnerability scanning result | To be tested |
| host_tasks | BatchStartHostTasks | Start or cancel host vulnerability scanning tasks in batches | To be tested |
| hosts | BatchCreateHosts | Creating host assets for tenants in batches | To be tested |
| purchase | CreatePurchaseOrder | Subscription and order placement interface | To be tested |
|  | ShowSubscription | Resource version query interface | To be tested |
|  | UpdatePurchaseOrder | Change the order placement interface | To be tested |
| web_results | ShowReportStatus | Obtain the PDF report generation status of website scanning | To be tested |
|  | DownloadTaskReport | Download the PDF report of the website scanning task | To be tested |
|  | UpdateFalsePositive | Updating the false positive status of website scanning vulnerabilities | To be tested |
|  | ExecuteGenerateReport | Generate the PDF report for website scanning | To be tested |
|  | ListPortResults | Obtain the website port scanning result | To be tested |
|  | ListBusinessRisks | Obtain website service risk scanning results | To be tested |
|  | ShowResults | Obtain website vulnerability scanning results | To be tested |
| web_tasks | CancelTasks | Cancel or restart a website vulnerability scanning task | To be tested |
|  | ShowTasks | Obtain the website vulnerability scanning task details | To be tested |
|  | ListTaskHistories | Obtain historical scanning tasks of website vulnerability scanning | To be tested |
| websites | DeleteDomains | Delete the website assets of the tenant | To be tested |
|  | AuthorizeDomains | Authentication of the tenant's website assets | To be tested |
|  | UpdateDomainSettings | Update website login configuration | To be tested |
|  | CreateDomains | Create a website asset for the tenant. | To be tested |
|  | ListDomains | Obtain all website assets of a tenant | To be tested |
|  | ShowDomainSettings | Obtain website login configuration | To be tested |

