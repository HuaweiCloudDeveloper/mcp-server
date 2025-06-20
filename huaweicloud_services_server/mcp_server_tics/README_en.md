# TICS MCP Server 


## Version
v0.1.0

## Overview

TICS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service TICS. Full-chain management of TICS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Allied management | ListNotices | Function description: Users can use this interface to query the notification management list. | To be tested |
|  | UpdateLeague | Function description: Users can use the interface to update alliance information. (including the alliance description, alliance version, privacy protection level, and score query privacy switch) | To be tested |
|  | ListPartners | Function description: Users can use this interface to obtain alliance member information. | To be tested |
|  | ListNodes | Function description: Users can use this API to query the list of trusted nodes (including aggregation nodes and compute nodes) in an alliance. | To be tested |
|  | ListLeagues | Function description: Users can use this interface to obtain the alliance list. | To be tested |
|  | ShowLeague | Function description: Users can use this interface to obtain alliance details. | To be tested |
| Audit Log Management | ListAuditInfo | Query audit log information | To be tested |
| Dataset Management | ListLeagueDatasets | Function description: Users can use this API to query the list of registered datasets in the alliance. | To be tested |
| Federal Analysis Job Management | ListSqlJob | Query the federated analysis job list | To be tested |
| Federated Learning Assignment Management | ListFlJob | Query the federated learning job list | To be tested |
| Job Instance Management | ShowJobInstanceDag | Obtain the instance execution diagram. | To be tested |
|  | ListInstanceHistory | Query the historical instance list of a job | To be tested |
|  | ShowInstanceReport | Query the instance execution report | To be tested |
| Statistical information management | ShowOverview | Query the number of federations and proxies of the current tenant | To be tested |
|  | ShowPartnerStatistics | Function description: Users can use this interface to collect statistics on alliance partners. | To be tested |
|  | ShowJobStatistics | Function description: Users can use this API to collect statistics on alliance jobs. | To be tested |
|  | ShowDatasetStatistics | You can use this API to collect statistics on alliance data sets. | To be tested |
| Trusted Node Management | ShowAgentDetail | Function description: Users can use this API to obtain the details about a single trusted computing node. | To be tested |
|  | ListAgents | Function description: This API is used to obtain the list of trusted nodes. Supports fuzzy search by node name and confederation name. | To be tested |

