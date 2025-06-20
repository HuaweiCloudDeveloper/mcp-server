# BCS MCP Server 


## Version
v0.1.0

## Overview

BCS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service BCS. Full-chain management of BCS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| BCS Alliance | HandleUnionMemberQuitList | The invited party withdraws from the alliance. | To be tested |
|  | HandleNotification | Processing the alliance invitation | To be tested |
|  | BatchInviteMembersToChannel | Inviting alliance members to join the channel in batches. This operation will send invitation notifications to the invited party. | To be tested |
|  | DeleteMemberInvite | You can invoke this interface to cancel invitations in batches or delete invitations for members who have quit, refused to join, or dismissed. | To be tested |
| BCS Management | ShowBlockchainDetail | Query the details of a specified service instance | To be tested |
|  | CreateBlockchainCertByUserName | Generate the organization user certificate for a specified service instance based on the user name. | To be tested |
|  | ShowBlockchainNodes | Query the node information of a specified service instance | To be tested |
|  | UnfreezeCert | Unfreeze the organization user certificate of the specified service instance. The certificate takes effect after half a minute to about one minute. | To be tested |
|  | ShowBlockchainFlavors | Query the specification information about the service consortium chain | To be tested |
|  | ShowBlockchainStatus | Query the creation status of a specified service instance | To be tested |
|  | BatchRemoveOrgsFromChannel | This interface is used by a BCS organization to exit a channel. | To be tested |
|  | ListOpRecord | Query the asynchronous operation result | To be tested |
|  | DownloadBlockchainCert | Download the certificate related to a specified service instance | To be tested |
|  | DeleteBlockchain | Delete the BCS instance. Yearly/Monthly DB instances are not supported.  | To be tested |
|  | CreateNewBlockchain | Create a BCS service instance. Only the instance can be created on demand. | To be tested |
|  | DownloadBlockchainSdkConfig | Download the SDK configuration file of a specified service instance | To be tested |
|  | FreezeCert | Frozen the organization user certificate of the specified service instance. The frozen certificate takes effect after half a minute to about one minute. | To be tested |
|  | BatchRemovePeersFromChannel | This interface is used by a node in a BCS organization to exit a channel. When the node is the last node in a channel, you need to use the interface for organizing the exit of the channel to exit the last node in the channel. | To be tested |
|  | BatchCreateChannels | Create a channel | To be tested |
|  | ListBlockchainChannels | Query the channel information of a specified service instance | To be tested |
|  | BatchAddPeersToChannel | The peer node can be added to a channel. Currently, only one channel can be added to the peer node. | To be tested |
|  | ListBlockchains | Query the brief information about all service instances in the current project. | To be tested |
| BCS Monitor | ListBcsMetric | This API is used to query the monitoring data of the BCS service. You can specify the metric name. | To be tested |
|  | ListInstanceMetric | This interface is used to query BCS organization instance monitoring data details. | To be tested |
|  | ListBcsEventsStatistic | This API is used to query the segmented event and alarm statistics of the BCS service. You can specify the filter criteria for the query. | To be tested |
|  | ListEntityMetric | This interface is used to query the monitoring data list of BCS organizations. | To be tested |
|  | ListBcsEvents | This API is used to query BCS events and alarm data. You can specify the filter criteria. | To be tested |
| Backend ECS | ListMembers | Query the backend ECSs in a backend ECS group. | To be tested |
| Event Channel Management | DeleteChannel | Delete a specified customized event channel. | To be tested |
| Key operation notification management | ListNotifications | Query the created key operation notification rule. | To be tested |
| Lifecycle Management | UpdateInstance | Modifies the name and description of an instance. | To be tested |
| Quota Management | ListQuotas | Obtain quota information | To be tested |

