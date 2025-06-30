# Product&Order MCP Server

## Version Information
v0.1.0

## Product Description

Product&Order MCP Server is a Model Context Protocol server that provides MCP clients (such as Claude Desktop, Cline, and Cursor) with the ability to interact with Huawei Cloud Store. It can manage products and orders based on natural language.

## Available Tools
More tools will be released in succession. The list of tools that have been released and their status are as follows:

| Category | Tool Name | Function Description | Status |
| --- | --- | --- | --- |
| ContractV2Query | contractQuery4Internal | Machine-to-machine interface to query contract information | To be tested |
| OrderAuthentication | orderAuthentication | Purchase image, cloud host authentication interface | To be tested |
| | machineOrderAuthentication | Purchase image, cloud host authentication interface | To be tested |
| OrderChannelSource | queryOrderChannelSourceListManager | Query order source configuration list information. | To be tested |
| | saveOrderChannelSourceConfigManager | Add & edit order channel source configuration. | To be tested |
| | configOrderChannelSourceStatusManager | Disable and enable order source configuration | To be tested |
| | getOrderSource | Query order source configuration source information based on the zone page address | To be tested |
| | getOrderSourceNew | Query order source configuration source information based on the zone page address | To be tested |
| | getOrderSource4User | Query order source configuration source information based on the zone page address | To be tested |
| OrderFlow | orderListBatchFetch | Order page list information. | To be tested |
| | orderList | Order page list information. | To be tested |
| | machineOrderList | Order page list information. | To be tested |
| | resaleOrdersQuery | Resale submarket: Jinyun, Ordos | To be tested |
| | resaleOrdersQueryNew | Resale submarket: Jinyun, Ordos | To be tested |
| | resaleOrderDetail | Resale submarket: Jinyun, Ordos | To be tested |
| | resaleOrderDetailNew | Resale submarket: Jinyun, Ordos | To be tested |
| | queryOrderStatus | Order status information. | To be tested |
| | orderDetail | Query order details information. | To be tested |
| | orderDetailExt | Query order details information. | To be tested |
| | orderCancel | Cancel pending payment order. | To be tested |
| | orderCount | Order quantity statistics. | To be tested |
| | saaSInstanceInfo | Query management instance application information. | To be tested |
| | queryRelatedOrderBatch | Query order batch information (order cancellation and payment in the buyer center must be queried and verified). Performance requirements: External interface response delay: 95% of samples are less than or equal to 1000ms when the success rate is 100%. | To be tested |
| | queryRelatedOrderBatchMigration | Query order batch information (order cancellation and payment in the buyer center must be queried and verified). Performance requirements: External interface response delay: 95% of samples are less than or equal to 1000ms when the success rate is 100%. | To be tested |
| | batchCancelOrder | Cancel orders in batches. | To be tested |
| | batchCancelOrderMigration | Cancel orders in batches. | To be tested |
| | queryResIdByInsId | View order resource id by instance id | To be tested |
| | queryResIdByInsIdMigration | View order resource id by instance id | To be tested |
| OrderPuchaseds | aopPurchaseds | | To be tested |
| | bssPurchaseds | | To be tested |
| | bssPurchasedsNew | | To be tested |
| | AopGetPurchaseDetail | | To be tested |
| | BssGetPurchaseDetail | | To be tested |
| | BssGetPurchaseDetailNew | | To be tested |
| ProductV2Query | productSearch4User | Buyer search product ID (V2 model) | To be tested |
| | productSearch4Auth | Authorized search product ID (V2 model) | To be tested |
| | productSearch4Internal | Machine-to-machine search for product ID (V2 model) | To be tested |
| | productSearch4Escalation | Search for product ID with escalation of privileges (V2 model) | To be tested |
| | productSearch4Management | Search for product ID in the management console (V2 model) | To be tested |
| | productSearch4Console | Search for product ID in the seller center (V2 model) | To be tested |
| | simpleQuery4Internal | Machine-to-machine interface query for L4 brief information | To be tested |
| | simpleQuery4Console | Console query for L4 brief information (V2 model) | To be tested |
| | simpleQuery4Management | Operation management console query for L4 brief information | To be tested |
| | simpleQuery4User | Buyer query for L4 brief information | To be tested |
| | queryProduct4Guest | Visitor query for product details | To be tested |
| | detailQuery | Machine-to-machine interface query for L4 details | To be tested |
| | userDetailQuery | Portal interface query for L4 details | To be tested |
| | queryProductDetail4Guest | Guest query product details | To be tested |
| | productNumQuery4Internal | Machine-to-machine interface query product quantity | To be tested |
| | defaultProductPricePlanQuery4Internal | Machine-to-machine interface query product default pricing plan | To be tested |
| | productQueryWithoutFeature4Internal | Machine-to-machine interface query merchant general products and selected products without associated products | To be tested |
| RenewOrder | renewOrderForResource | Buyer center resource renewal operation call | To be tested |
| | renewOrderForResourceMigration | Buyer center resource renewal operation call | To be tested |
| UnsubscribeOrder | unsubscribeOrderForResource | Buyer center resource create unsubscribe order operation call | To be tested |
| | unsubscribeOrderForResourceMigration | Buyer center resource create unsubscribe order operation call | To be tested |