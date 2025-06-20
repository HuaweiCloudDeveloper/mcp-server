# GSL MCP Server 


## Version
v0.1.0

## Overview

GSL MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GSL. Full-chain management of GSL resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Attribute | CreateAttribute | Interface for adding user-defined attributes | To be tested |
|  | EnableAttribute | Enable the interface for customizing attributes | To be tested |
|  | DisableAttribute | Interface for disabling customized attributes | To be tested |
|  | ListAttributes | Interface for querying the user-defined attribute list | To be tested |
|  | UpdateAttribute | Interface for modifying customized attributes | To be tested |
|  | BatchSetAttributes | API for setting customized attributes in batches | To be tested |
| BackPool | ListBackPools | Query the backward traffic pool list | To be tested |
|  | ListBackPoolMembers | Query the backward traffic pool member list | To be tested |
| Image Tag | ListTags | Query the image tag list based on different conditions. | To be tested |
| Key Tag Management | DeleteTag | - Function description: This API is used to delete a key tag. | To be tested |
| NetworkSwitchPolicies | ListNetworkSwitchPolicies | Query the policy list | To be tested |
|  | AddNetworkSwitchPolicy | Adding a network handover policy | To be tested |
| PricePlans | ListProPricePlans | Query the bundle list | To be tested |
| SimCards | ListSimCards | Query the SIM card list | To be tested |
|  | StartStopNet | This interface is used to apply for SIM card disconnection or resumption. This interface can be invoked only by China Telecom SIM cards. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time. | To be tested |
|  | SetSpeedValue | Interface for limiting the rate of a physical card. This interface can be invoked only by physical cards of China Telecom and China Unicom. China Unicom cards can use the speed limit function only after personal real-name authentication. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time. | To be tested |
|  | ShowMonthUsages | Monthly device usage statistics | To be tested |
|  | DeleteRealName | Clears real-name authentication information. This interface can be invoked only by China Telecom cards. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time. | To be tested |
|  | ShowSimCard | Query SIM card details | To be tested |
|  | StopSimCard | Create a suspension application and return the business handling order number. Shut down the system within one to two working days. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time. | To be tested |
|  | EnableSimCard | Create an application for activating an entity card. The business handling order number is returned. The activation is completed within one to two working days. Note: Due to the service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time. | To be tested |
|  | ListSimCardFlowPerDay | Interface for querying the daily usage of SIM cards in batches. The query by day or month is supported. You can select only one of the SIM card ID and container ID, day, and month parameters. | To be tested |
|  | ShowRealNamed | Query real-time SIM card real-name authentication information. This API supports query of only the real-name authentication information of carrier cards in Chinese Mainland. | To be tested |
|  | RegisterImei | Fixed phone and SIM card rebinding is supported. (You need to upload the IMEI and bind the SIM card to the device with the specified IMEI.) Rebinding with the common phone card (The previously bound device will be deleted and the SIM card will be bound to the device in use.). This interface can be invoked only by China Telecom cards and China Mobile cards. A single China Telecom card can be re-bound only twice a month. A China Mobile card can be re-bound only for common phone cards. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time. | To be tested |
|  | SetExceedCutNet | This interface can be invoked only by SIM cards of China Telecom and group pool cards of China Unicom and China Mobile. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time. | To be tested |
|  | ResetSimCard | Create a resumption application and return the business handling order number. Resume the subscriber within one to two working days. Note: Due to service restrictions on the carrier side, it is recommended that you do not perform multiple service operations on the same SIM card at the same time. | To be tested |
| SimDeviceMultiply | SwitchNetwork | Switch the network | To be tested |
|  | ListSimDeviceMultiply | Query the list of three NICs by CID or all NICs | To be tested |
|  | SetNetworkSwitchPolicy | This API is used to set the network switchover policy for the SIM card. Only three NICs can be invoked. | To be tested |
| SimPool | ListSimPools | Query the traffic pool list | To be tested |
|  | ListSimPoolMembers | Query the traffic pool member list | To be tested |
| SimPricePlans | ListSimPricePlans | Query the SIM card package list. Only one package exists for a physical card, and multiple packages may exist for the eSIM or vSIM card. | To be tested |
|  | ListFlowBySimCards | Query traffic of physical cards in batches | To be tested |
| Sms | SendSms | The interface for sending SMS messages can be invoked only by China Mobile and China Telecom cards that have subscribed to SMS packages. | To be tested |
|  | ListSmsDetails | SMS message sending details. This interface can be invoked only by China Mobile and China Telecom cards that have subscribed to SMS packages. | To be tested |
| Tag | BatchSetTags | API for batch setting or canceling label setting | To be tested |
| Tag Management | CreateTag | Add a tag to a resource. | To be tested |
| WorkOrder | ListWorkOrders | Query service handling orders by page | To be tested |
|  | ListWorkOrderDetails | Query service handling details by page | To be tested |

