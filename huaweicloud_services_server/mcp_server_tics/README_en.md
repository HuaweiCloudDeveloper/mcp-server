# TICS MCP Server 


## Version
v0.1.0

## Overview

TICS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service TICS. Full-chain management of TICS resources can be carried out based on natural language.

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
                    <td rowspan="6">Allied management</td>
                    <td>ListNotices</td>
                    <td>Function description: Users can use this interface to query the notification management list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLeague</td>
                    <td>Function description: Users can use the interface to update alliance information. (including the alliance description, alliance version, privacy protection level, and score query privacy switch)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPartners</td>
                    <td>Function description: Users can use this interface to obtain alliance member information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodes</td>
                    <td>Function description: Users can use this API to query the list of trusted nodes (including aggregation nodes and compute nodes) in an alliance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLeagues</td>
                    <td>Function description: Users can use this interface to obtain the alliance list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLeague</td>
                    <td>Function description: Users can use this interface to obtain alliance details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Audit Log Management</td>
                    <td>ListAuditInfo</td>
                    <td>Query audit log information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Dataset Management</td>
                    <td>ListLeagueDatasets</td>
                    <td>Function description: Users can use this API to query the list of registered datasets in the alliance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Federal Analysis Job Management</td>
                    <td>ListSqlJob</td>
                    <td>Query the federated analysis job list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Federated Learning Assignment Management</td>
                    <td>ListFlJob</td>
                    <td>Query the federated learning job list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Job Instance Management</td>
                    <td>ShowJobInstanceDag</td>
                    <td>Obtain the instance execution diagram.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceHistory</td>
                    <td>Query the historical instance list of a job</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceReport</td>
                    <td>Query the instance execution report</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Statistical information management</td>
                    <td>ShowOverview</td>
                    <td>Query the number of federations and proxies of the current tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPartnerStatistics</td>
                    <td>Function description: Users can use this interface to collect statistics on alliance partners.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobStatistics</td>
                    <td>Function description: Users can use this API to collect statistics on alliance jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatasetStatistics</td>
                    <td>You can use this API to collect statistics on alliance data sets.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Trusted Node Management</td>
                    <td>ShowAgentDetail</td>
                    <td>Function description: Users can use this API to obtain the details about a single trusted computing node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgents</td>
                    <td>Function description: This API is used to obtain the list of trusted nodes. Supports fuzzy search by node name and confederation name.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
