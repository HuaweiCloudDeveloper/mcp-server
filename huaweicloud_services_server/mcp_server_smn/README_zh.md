# SMN MCP Server 

## 版本信息
v0.1.0

## 产品描述

SMN MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务SMN交互的能力。可以基于自然语言对SMN资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Application endpoint操作 | CreateApplicationEndpoint | 创建应用平台的endpoint终端。 | To be tested |
|  | ListApplicationEndpoints | 查询平台的endpoint列表。 | To be tested |
|  | DeleteApplicationEndpoint | 删除设备。 | To be tested |
|  | UpdateApplicationEndpoint | 更新设备属性。 | To be tested |
|  | ListApplicationEndpointAttributes | 获取endpoint的属性。 | To be tested |
| Application操作 | CreateApplication | 创建平台应用。 | To be tested |
|  | UpdateApplication | 更新应用平台。 | To be tested |
|  | ListApplications | 查询应用平台列表。 | To be tested |
|  | ListApplicationAttributes | 获取应用平台属性。 | To be tested |
|  | DeleteApplication | 删除平台应用。 | To be tested |
| Application直发消息操作 | PublishAppMessage | 将消息直发给endpoint设备。 | To be tested |
| 主题操作 | DeleteTopic | 删除主题。 | To be tested |
|  | ListTopicDetails | 查询Topic的详细信息。 | To be tested |
|  | UpdateTopicAttribute | 更新主题的策略信息。 | To be tested |
|  | ListTopics | 分页查询Topic列表,Topic列表按照Topic创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在Topic,则返回空列表。 | To be tested |
|  | DeleteTopicAttributeByName | 删除指定名称的主题策略。 | To be tested |
|  | DeleteTopicAttributes | 删除所有主题策略。 | To be tested |
|  | UpdateTopic | 更新显示名。 | To be tested |
|  | ListTopicAttributes | 查询主题的策略信息。 | To be tested |
|  | CreateTopic | 创建Topic,单用户默认配额为3000。高并发场景下,可能会出现Topic数量超过3000仍创建成功的情况,此为正常现象。 | To be tested |
| 云日志操作 | CreateLogtank | 为指定Topic绑定一个云日志,用于记录主题消息发送状态等信息。 | To be tested |
|  | UpdateLogtank | 更新指定Topic绑定的云日志。 | To be tested |
|  | DeleteLogtank | 解绑指定Topic绑定的云日志。 | To be tested |
|  | ListLogtank | 查询指定Topic绑定的云日志。 | To be tested |
| 使用标签管理服务 | CreateResourceTag | 一个资源上最多有10个标签。此接口为幂等接口:创建时,如果创建的标签已经存在(key相同),则覆盖。 | To be tested |
|  | ListResourceInstances | 使用标签过滤实例。 | To be tested |
|  | ListProjectTags | 查询租户在指定Region和实例类型的所有标签集合。 | To be tested |
|  | DeleteResourceTag | 幂等接口:删除时,不对标签做校验。删除的key不存在报404,key不能为空或者空字符串。 | To be tested |
|  | BatchCreateOrDeleteResourceTags | 为指定实例批量添加或删除标签。一个资源上最多有10个标签。 | To be tested |
|  | ListResourceTags | 查询指定实例的标签信息。 | To be tested |
| 发布消息操作 | ShowHttpDetectResult | 根据http探测发送返回的task_id查询探测结果。 | To be tested |
|  | PublishMessage | 将消息发送给Topic的所有订阅端点。当返回消息ID时,该消息已被保存并开始尝试将其推送给Topic的订阅者。为确保您的消息能够成功推送到各个订阅者,请确保您的消息内容符合当地法律法规要求。 | To be tested |
|  | PublishHttpDetect | 基于主题发送http/https探测消息,探测当前http/https 终端是否可用,SMN出口是否能够正常访问该终端。 | To be tested |
| 查询版本操作 | ListVersion | 查询SMN API V2版本信息。 | To be tested |
|  | ListVersions | 查询SMN开放API支持的版本号。 | To be tested |
| 模板操作 | ListMessageTemplateDetails | 查询模板详情,包括模板内容。 | To be tested |
|  | CreateMessageTemplate | 创建一个模板,用户可以按照模板去发送消息,这样可以减少请求的数据量。 | To be tested |
|  | UpdateMessageTemplate | 修改消息模板的内容。 | To be tested |
|  | ListMessageTemplates | 分页查询模板列表,模板列表按照创建时间进行升序排列。分页查询可以指定offset以及limit。如果不存在模板,则返回空列表。额外的查询参数分别有message_template_name和protocol。 | To be tested |
|  | DeleteMessageTemplate | 删除消息模板。删除模板之前的消息请求都可以使用该模板发送,删除之后无法再使用该模板发送消息。 | To be tested |
| 订阅操作 | AddSubscriptionFromSubscriptionUser | 为指定的Topic添加订阅者,订阅者信息来源为订阅用户列表。 | To be tested |
|  | ListSubscriptions | 分页返回请求者的所有的订阅列表,订阅列表按照订阅创建时间进行升序排列。分页查询可以指定offset以及limit。如果订阅者不存在,返回空列表。 | To be tested |
|  | ListSubscriptionsByTopic | 分页获取特定Topic的订阅列表,订阅列表按照订阅创建时间进行升序排列。分页查询可以指定offset以及limit。如果指定Topic不存在订阅者,返回空列表。 | To be tested |
|  | CancelSubscription | 删除指定的订阅者。 | To be tested |
|  | AddSubscription | 为指定Topic添加一个订阅者,如果订阅者的状态为未确认,则向订阅者发送一个确认的消息。待订阅者进行ConfirmSubscription确认后,该订阅者才能收到Topic发布的消息。单Topic默认可添加10000个订阅者,高并发场景下,可能会出现订阅者数量超过10000仍添加成功的情况,此为正常现象。接口是幂等的,如果添加已存在的订阅者,则返回成功,且status code为200,否则status code为201。 | To be tested |
|  | UpdateSubscription | 更新订阅者备注。 | To be tested |
| 订阅过滤策略操作 | BatchCreateSubscriptionsFilterPolices | 创建订阅者的消息过滤策略。 | To be tested |
|  | BatchUpdateSubscriptionsFilterPolices | 更新订阅者的消息过滤策略。 | To be tested |
|  | BatchDeleteSubscriptionsFilterPolices | 删除订阅者的消息过滤策略。 | To be tested |
| 通知策略 | ShowNotifyPolicy | 查询通知策略 | To be tested |
|  | CreateNotifyPolicy | 创建通知策略 | To be tested |
|  | UpdateNotifyPolicy | 修改通知策略,该接口仅支持全量修改,不支持部分修改。 | To be tested |
|  | DeleteNotifyPolicy | 删除通知策略 | To be tested |
