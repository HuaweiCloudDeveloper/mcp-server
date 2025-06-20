# TMS MCP Server 


## Version
v0.1.0

## Overview

TMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service TMS. Full-chain management of TMS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Predefined label operation | CreatePredefineTags | Creates a predefined tag. After creating predefined tags, you can use the predefined tags to create tags for resources. This interface supports idempotent features and bulk data processing. | To be tested |
|  | DeletePredefineTags | This command is used to delete a predetermined tag. | To be tested |
|  | UpdatePredefineTags | Modify the predefined tag. | To be tested |
|  | ListPredefineTags | Query the list of predefined tags. | To be tested |
| Query services supported by tag management | ListProviders | Query the services supported by tag management. | To be tested |
| Query version operation | ShowApiVersion | Query the details about a specified TMS API version. | To be tested |
|  | ListApiVersions | Query the TMS API version list. | To be tested |
| Quota | ShowTagQuota | Query the quota information about a tag. | To be tested |
| Resource Tag | DeleteResourceTag | This API is used to remove tags of multiple cloud service resources in batches. A maximum of 10 tags can be removed for each resource. A maximum of 20 tags can be removed at a time. | To be tested |
|  | ListResource | Filter resources by tag. | To be tested |
|  | ShowResourceTag | Query the tags of a single resource. | To be tested |
|  | ListTagValues | Query all tag values under a tag key in a specified region. | To be tested |
|  | ListTagKeys | Query all tag keys in a specified region. | To be tested |
|  | CreateResourceTag | Add tags to multiple cloud service resources. A maximum of 10 tags can be added to each resource. A maximum of 20 tags can be operated at a time. | To be tested |

