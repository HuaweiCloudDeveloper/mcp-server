# CodeArtsInspector MCP Server 


## Version
v0.1.0

## Overview

CodeArtsInspector MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeArtsInspector. Full-chain management of CodeArtsInspector resources can be carried out based on natural language.

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
                    <td rowspan="1">Cluster management interface</td>
                    <td>ListHosts</td>
                    <td>This API is used to query details about the host list in the input cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Group</td>
                    <td>DeleteGroup</td>
                    <td>Delete a code group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Protection Website Management in Cloud Mode</td>
                    <td>DeleteHost</td>
                    <td>Delete the domain name in cloud mode.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Service Job Management</td>
                    <td>CreateTasks</td>
                    <td>This API is used to create a service job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">host_groups</td>
                    <td>ListGroups</td>
                    <td>Obtain the host group list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddGroup</td>
                    <td>Create host groups in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">host_results</td>
                    <td>ListHostResults</td>
                    <td>Obtain the host vulnerability scanning result</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">host_tasks</td>
                    <td>BatchStartHostTasks</td>
                    <td>Start or cancel host vulnerability scanning tasks in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">hosts</td>
                    <td>BatchCreateHosts</td>
                    <td>Creating host assets for tenants in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">purchase</td>
                    <td>CreatePurchaseOrder</td>
                    <td>Subscription and order placement interface</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubscription</td>
                    <td>Resource version query interface</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePurchaseOrder</td>
                    <td>Change the order placement interface</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">web_results</td>
                    <td>ShowReportStatus</td>
                    <td>Obtain the PDF report generation status of website scanning</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadTaskReport</td>
                    <td>Download the PDF report of the website scanning task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFalsePositive</td>
                    <td>Updating the false positive status of website scanning vulnerabilities</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteGenerateReport</td>
                    <td>Generate the PDF report for website scanning</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPortResults</td>
                    <td>Obtain the website port scanning result</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBusinessRisks</td>
                    <td>Obtain website service risk scanning results</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResults</td>
                    <td>Obtain website vulnerability scanning results</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">web_tasks</td>
                    <td>CancelTasks</td>
                    <td>Cancel or restart a website vulnerability scanning task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTasks</td>
                    <td>Obtain the website vulnerability scanning task details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskHistories</td>
                    <td>Obtain historical scanning tasks of website vulnerability scanning</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">websites</td>
                    <td>DeleteDomains</td>
                    <td>Delete the website assets of the tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AuthorizeDomains</td>
                    <td>Authentication of the tenant's website assets</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainSettings</td>
                    <td>Update website login configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDomains</td>
                    <td>Create a website asset for the tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomains</td>
                    <td>Obtain all website assets of a tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainSettings</td>
                    <td>Obtain website login configuration</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
