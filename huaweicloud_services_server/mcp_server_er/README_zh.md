# ER MCP Server 

## 版本信息
v0.1.0

## 产品描述

ER MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务ER交互的能力。可以基于自然语言对ER资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Association | DisassociateRouteTable | 解绑连接和路由表的关联关系。 | To be tested |
|  | ListAssociations | 查询路由关联列表。 | To be tested |
|  | AssociateRouteTable | 每个连接只能关联到一张路由表。通过创建关联将连接关联到路由表,从该连接收到的报文会用被关联的路由表进行路由。 | To be tested |
| Attachments | ListAttachments | 查询企业路由器实例下的连接列表。 | To be tested |
|  | ShowAttachment | 查询连接详情 | To be tested |
|  | UpdateAttachment | 修改连接基本信息。 | To be tested |
|  | RejectAttachment | 拒绝共享连接创建 | To be tested |
|  | AcceptAttachment | 接受共享连接创建 | To be tested |
| AvailableZone | ListAvailabilityZone | 查询支持创建企业路由器实例的可用区列表,当可用区状态为available时,表示可以创建企业路由器实例。 | To be tested |
| EnterpriseRouterInstance | ChangeAvailabilityZone | 更新企业路由器的可用区信息,企业路由器实例状态为available的时候才能更新。 | To be tested |
|  | ListEnterpriseRouters | 查询企业路由器列表 | To be tested |
|  | CreateEnterpriseRouter | 创建企业路由器实例,如果使能默认关联路由表或使能默认传递路由表,那么系统会默认创建一张路由表,作为默认关联路由表或默认传递路由表。 | To be tested |
|  | UpdateEnterpriseRouter | 更新企业路由器基本信息。 | To be tested |
|  | ShowEnterpriseRouter | 查询企业路由器详情 | To be tested |
|  | DeleteEnterpriseRouter | 删除企业路由器。 | To be tested |
| FlowLog | ShowFlowLog | 查询流日志详情 | To be tested |
|  | EnableFlowLog | 开启流日志 | To be tested |
|  | UpdateFlowLog | 更新流日志基本信息 | To be tested |
|  | DeleteFlowLog | 删除流日志 | To be tested |
|  | DisableFlowLog | 关闭流日志 | To be tested |
|  | ListFlowLogs | 查询企业路由器实例下的流日志列表 | To be tested |
|  | CreateFlowLog | 给ER实例创建流日志。 | To be tested |
| Propagation | ListPropagations | 查询路由传播列表。 | To be tested |
|  | DisablePropagation | 解绑连接和路由表的传播关系。 | To be tested |
|  | EnablePropagation | 每个连接可以和多个路由表建立传播关系,从该连接学习到的路由会应用到具有传播关系的路由表。 | To be tested |
| QuotaManager | ShowQuotas | 查询租户各类资源的使用情况,如企业路由器的使用量,VPC连接的使用量等。 | To be tested |
| Route | ListStaticRoutes | 查询静态路由列表。 | To be tested |
|  | ListEffectiveRoutes | 查询有效的路由列表,支持分页查询能力 | To be tested |
|  | CreateStaticRoute | 创建静态路由 | To be tested |
|  | UpdateStaticRoute | 更新静态路由 | To be tested |
|  | ShowStaticRoute | 查询静态路由详情 | To be tested |
|  | DeleteStaticRoute | 删除静态路由 | To be tested |
| RouteTable | ListRouteTables | 查询路由表列表。 | To be tested |
|  | CreateRouteTable | 路由表是企业路由器收发报文的依据,包含了连接的关联关系,传播关系以及路由信息。 | To be tested |
|  | DeleteRouteTable | 删除路由表 | To be tested |
|  | ShowRouteTable | 查询路由表详情 | To be tested |
|  | UpdateRouteTable | 更新路由表基本信息,如名称,描述等。 | To be tested |
| Tags | ShowResourceTag | 查询特定类型资源的标签信息。 | To be tested |
|  | ListProjectTags | 查询特定类型资源的标签集合。 | To be tested |
|  | BatchCreateResourceTags | - 为指定实例批量添加或删除标签 | To be tested |
|  | CreateResourceTag | 为特定类型的资源创建标签。 | To be tested |
|  | DeleteResourceTag | 删除特定类型资源的标签。 | To be tested |
| VPCAttachment | ListVpcAttachments | 查询企业路由器实例下的VPC连接列表。 | To be tested |
|  | ShowVpcAttachment | 查询VPC连接详情 | To be tested |
|  | UpdateVpcAttachment | 修改VPC连接基本信息。 | To be tested |
|  | CreateVpcAttachment | 给ER实例创建VPC连接。 | To be tested |
|  | DeleteVpcAttachment | 删除VPC连接。 | To be tested |
