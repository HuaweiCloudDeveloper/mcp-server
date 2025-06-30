# GSL MCP Server 


## Version
v0.1.0

## Overview

GSL MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GSL. Full-chain management of GSL resources can be carried out based on natural language.

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
                    <td rowspan="6">Attribute</td>
                    <td>CreateAttribute</td>
                    <td>Interface for adding user-defined attributes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableAttribute</td>
                    <td>Enable the interface for customizing attributes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableAttribute</td>
                    <td>Interface for disabling customized attributes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAttributes</td>
                    <td>Interface for querying the user-defined attribute list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAttribute</td>
                    <td>Interface for modifying customized attributes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSetAttributes</td>
                    <td>API for setting customized attributes in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">BackPool</td>
                    <td>ListBackPools</td>
                    <td>Query the backward traffic pool list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackPoolMembers</td>
                    <td>Query the backward traffic pool member list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Image Tag</td>
                    <td>ListTags</td>
                    <td>Query the image tag list based on different conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Key Tag Management</td>
                    <td>DeleteTag</td>
                    <td>- Function description: This API is used to delete a key tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">NetworkSwitchPolicies</td>
                    <td>ListNetworkSwitchPolicies</td>
                    <td>Query the policy list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddNetworkSwitchPolicy</td>
                    <td>Adding a network handover policy</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">PricePlans</td>
                    <td>ListProPricePlans</td>
                    <td>Query the bundle list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">SimCards</td>
                    <td>ListSimCards</td>
                    <td>Query the SIM card list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartStopNet</td>
                    <td>This interface is used to apply for SIM card disconnection or resumption. This interface can be invoked only by China Telecom SIM cards. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetSpeedValue</td>
                    <td>Interface for limiting the rate of a physical card. This interface can be invoked only by physical cards of China Telecom and China Unicom. China Unicom cards can use the speed limit function only after personal real-name authentication. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonthUsages</td>
                    <td>Monthly device usage statistics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRealName</td>
                    <td>Clears real-name authentication information. This interface can be invoked only by China Telecom cards. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSimCard</td>
                    <td>Query SIM card details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopSimCard</td>
                    <td>Create a suspension application and return the business handling order number. Shut down the system within one to two working days. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableSimCard</td>
                    <td>Create an application for activating an entity card. The business handling order number is returned. The activation is completed within one to two working days. Note: Due to the service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSimCardFlowPerDay</td>
                    <td>Interface for querying the daily usage of SIM cards in batches. The query by day or month is supported. You can select only one of the SIM card ID and container ID, day, and month parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRealNamed</td>
                    <td>Query real-time SIM card real-name authentication information. This API supports query of only the real-name authentication information of carrier cards in Chinese Mainland.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterImei</td>
                    <td>Fixed phone and SIM card rebinding is supported. (You need to upload the IMEI and bind the SIM card to the device with the specified IMEI.) Rebinding with the common phone card (The previously bound device will be deleted and the SIM card will be bound to the device in use.). This interface can be invoked only by China Telecom cards and China Mobile cards. A single China Telecom card can be re-bound only twice a month. A China Mobile card can be re-bound only for common phone cards. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetExceedCutNet</td>
                    <td>This interface can be invoked only by SIM cards of China Telecom and group pool cards of China Unicom and China Mobile. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetSimCard</td>
                    <td>Create a resumption application and return the business handling order number. Resume the subscriber within one to two working days. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">SimDeviceMultiply</td>
                    <td>SwitchNetwork</td>
                    <td>Switch the network</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSimDeviceMultiply</td>
                    <td>Query the list of three NICs by CID or all NICs</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetNetworkSwitchPolicy</td>
                    <td>This API is used to set the network switchover policy for the SIM card. Only three NICs can be invoked.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">SimPool</td>
                    <td>ListSimPools</td>
                    <td>Query the traffic pool list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSimPoolMembers</td>
                    <td>Query the traffic pool member list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">SimPricePlans</td>
                    <td>ListSimPricePlans</td>
                    <td>Query the SIM card package list. Only one package exists for a physical card, and multiple packages may exist for the eSIM or vSIM card.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlowBySimCards</td>
                    <td>Query traffic of physical cards in batches</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Sms</td>
                    <td>SendSms</td>
                    <td>The interface for sending SMS messages can be invoked only by China Mobile and China Telecom cards that have subscribed to SMS packages.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSmsDetails</td>
                    <td>SMS message sending details. This interface can be invoked only by China Mobile and China Telecom cards that have subscribed to SMS packages.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tag</td>
                    <td>BatchSetTags</td>
                    <td>API for batch setting or canceling label setting</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tag Management</td>
                    <td>CreateTag</td>
                    <td>Add a tag to a resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">WorkOrder</td>
                    <td>ListWorkOrders</td>
                    <td>Query service handling orders by page</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkOrderDetails</td>
                    <td>Query service handling details by page</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
