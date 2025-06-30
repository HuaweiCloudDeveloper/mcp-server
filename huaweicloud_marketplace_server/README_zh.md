# Product&Order MCP Server 

## 版本信息
v0.1.0

## 产品描述

Product&Order MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云商店交互的能力。可以基于自然语言管理商品和订单。

## 可用工具
更多工具将陆续开放，已开放列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| ContractV2Query | contractQuery4Internal | 机机接口查询合同信息  | To be tested |
| OrderAuthentication | orderAuthentication | 购买镜像、云主机鉴权接口  | To be tested |
|  | machineOrderAuthentication | 购买镜像、云主机鉴权接口  | To be tested |
| OrderChannelSource | queryOrderChannelSourceListManager | 查询下单来源配置列表信息。  | To be tested |
|  | saveOrderChannelSourceConfigManager | 新增&编辑下单渠道来源配置。  | To be tested |
|  | configOrderChannelSourceStatusManager | 停用启用下单来源配置  | To be tested |
|  | getOrderSource | 根据专区页地址查询下单来源配置来源信息  | To be tested |
|  | getOrderSourceNew | 根据专区页地址查询下单来源配置来源信息  | To be tested |
|  | getOrderSource4User | 根据专区页地址查询下单来源配置来源信息  | To be tested |
| OrderFlow | orderListBatchFetch | 订单分页列表信息。  | To be tested |
|  | orderList | 订单分页列表信息。  | To be tested |
|  | machineOrderList | 订单分页列表信息。  | To be tested |
|  | resaleOrdersQuery | 转售子市场：晋云、鄂尔多斯 | To be tested |
|  | resaleOrdersQueryNew | 转售子市场：晋云、鄂尔多斯 | To be tested |
|  | resaleOrderDetail | 转售子市场：晋云、鄂尔多斯 | To be tested |
|  | resaleOrderDetailNew | 转售子市场：晋云、鄂尔多斯 | To be tested |
|  | queryOrderStatus | 订单状态信息。  | To be tested |
|  | orderDetail | 查询订单详情信息。  | To be tested |
|  | orderDetailExt | 查询订单详情信息。  | To be tested |
|  | orderCancel | 待支付订单取消。  | To be tested |
|  | orderCount | 订单数量统计。  | To be tested |
|  | saaSInstanceInfo | 查询管理实例应用信息。  | To be tested |
|  | queryRelatedOrderBatch | 查询订单批次信息（买家中心订单取消、支付必须要查询并校验）。 性能要求：对外接口响应时延：100%成功率时，95%样本小于等于1000ms。 | To be tested |
|  | queryRelatedOrderBatchMigration | 查询订单批次信息（买家中心订单取消、支付必须要查询并校验）。 性能要求：对外接口响应时延：100%成功率时，95%样本小于等于1000ms。 | To be tested |
|  | batchCancelOrder | 批量取消订单。  | To be tested |
|  | batchCancelOrderMigration | 批量取消订单。  | To be tested |
|  | queryResIdByInsId | 通过实例id查看订单资源id  | To be tested |
|  | queryResIdByInsIdMigration | 通过实例id查看订单资源id  | To be tested |
| OrderPuchaseds | aopPurchaseds |  | To be tested |
|  | bssPurchaseds |  | To be tested |
|  | bssPurchasedsNew |  | To be tested |
|  | AopGetPurchaseDetail |  | To be tested |
|  | BssGetPurchaseDetail |  | To be tested |
|  | BssGetPurchaseDetailNew |  | To be tested |
| ProductV2Query | productSearch4User | 买家搜索商品ID(V2模型)  | To be tested |
|  | productSearch4Auth | 授权搜索商品ID(V2模型)  | To be tested |
|  | productSearch4Internal | 机机搜索商品ID(V2模型)  | To be tested |
|  | productSearch4Escalation | 提权搜索商品ID(V2模型)  | To be tested |
|  | productSearch4Management | 管理台搜索商品ID(V2模型)  | To be tested |
|  | productSearch4Console | 卖家中心搜索商品ID(V2模型)  | To be tested |
|  | simpleQuery4Internal | 机机接口查询L4简要信息  | To be tested |
|  | simpleQuery4Console | Console查询L4简要信息(V2模型)  | To be tested |
|  | simpleQuery4Management | 运营管理台查询L4简要信息  | To be tested |
|  | simpleQuery4User | 买家查询L4简要信息  | To be tested |
|  | queryProduct4Guest | 游客查询商品详情  | To be tested |
|  | detailQuery | 机机接口查询L4详情  | To be tested |
|  | userDetailQuery | portal接口查询L4详情  | To be tested |
|  | queryProductDetail4Guest | 游客查询商品详情  | To be tested |
|  | productNumQuery4Internal | 机机接口查询商品数量  | To be tested |
|  | defaultProductPricePlanQuery4Internal | 机机接口查询商品默认定价计划  | To be tested |
|  | productQueryWithoutFeature4Internal | 机机接口查询商家没有关联商品的通用商品和严选商品  | To be tested |
| RenewOrder | renewOrderForResource | 买家中心资源续费操作调用 | To be tested |
|  | renewOrderForResourceMigration | 买家中心资源续费操作调用 | To be tested |
| UnsubscribeOrder | unsubscribeOrderForResource | 买家中心资源创建退订订单操作调用 | To be tested |
|  | unsubscribeOrderForResourceMigration | 买家中心资源创建退订订单操作调用 | To be tested |
