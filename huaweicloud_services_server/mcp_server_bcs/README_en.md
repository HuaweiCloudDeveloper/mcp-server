# BCS MCP Server 


## Version
v0.1.0

## Overview

BCS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service BCS. Full-chain management of BCS resources can be carried out based on natural language.

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
                    <td rowspan="4">BCS Alliance</td>
                    <td>HandleUnionMemberQuitList</td>
                    <td>The invited party withdraws from the alliance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>HandleNotification</td>
                    <td>Processing the alliance invitation</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchInviteMembersToChannel</td>
                    <td>Inviting alliance members to join the channel in batches. This operation will send invitation notifications to the invited party.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMemberInvite</td>
                    <td>You can invoke this interface to cancel invitations in batches or delete invitations for members who have quit, refused to join, or dismissed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="18">BCS Management</td>
                    <td>ShowBlockchainDetail</td>
                    <td>Query the details of a specified service instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBlockchainCertByUserName</td>
                    <td>Generate the organization user certificate for a specified service instance based on the user name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBlockchainNodes</td>
                    <td>Query the node information of a specified service instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnfreezeCert</td>
                    <td>Unfreeze the organization user certificate of the specified service instance. The certificate takes effect after half a minute to about one minute.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBlockchainFlavors</td>
                    <td>Query the specification information about the service consortium chain</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBlockchainStatus</td>
                    <td>Query the creation status of a specified service instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRemoveOrgsFromChannel</td>
                    <td>This interface is used by a BCS organization to exit a channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOpRecord</td>
                    <td>Query the asynchronous operation result</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadBlockchainCert</td>
                    <td>Download the certificate related to a specified service instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBlockchain</td>
                    <td>Delete the BCS instance. Yearly/Monthly DB instances are not supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNewBlockchain</td>
                    <td>Create a BCS service instance. Only the instance can be created on demand.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadBlockchainSdkConfig</td>
                    <td>Download the SDK configuration file of a specified service instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>FreezeCert</td>
                    <td>Frozen the organization user certificate of the specified service instance. The frozen certificate takes effect after half a minute to about one minute.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRemovePeersFromChannel</td>
                    <td>This interface is used by a node in a BCS organization to exit a channel. When the node is the last node in a channel, you need to use the interface for organizing the exit of the channel to exit the last node in the channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateChannels</td>
                    <td>Create a channel</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBlockchainChannels</td>
                    <td>Query the channel information of a specified service instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddPeersToChannel</td>
                    <td>The peer node can be added to a channel. Currently, only one channel can be added to the peer node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBlockchains</td>
                    <td>Query the brief information about all service instances in the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">BCS Monitor</td>
                    <td>ListBcsMetric</td>
                    <td>This API is used to query the monitoring data of the BCS service. You can specify the metric name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceMetric</td>
                    <td>This interface is used to query BCS organization instance monitoring data details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBcsEventsStatistic</td>
                    <td>This API is used to query the segmented event and alarm statistics of the BCS service. You can specify the filter criteria for the query.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEntityMetric</td>
                    <td>This interface is used to query the monitoring data list of BCS organizations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBcsEvents</td>
                    <td>This API is used to query BCS events and alarm data. You can specify the filter criteria.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Backend ECS</td>
                    <td>ListMembers</td>
                    <td>Query the backend ECSs in a backend ECS group.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Event Channel Management</td>
                    <td>DeleteChannel</td>
                    <td>Delete a specified customized event channel.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Key operation notification management</td>
                    <td>ListNotifications</td>
                    <td>Query the created key operation notification rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Lifecycle Management</td>
                    <td>UpdateInstance</td>
                    <td>Modifies the name and description of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota Management</td>
                    <td>ListQuotas</td>
                    <td>Obtain quota information</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
