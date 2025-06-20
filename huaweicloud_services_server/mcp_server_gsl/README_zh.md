# GSL MCP Server 

## 版本信息
v0.1.0

## 产品描述

GSL MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务GSL交互的能力。可以基于自然语言对GSL资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Attribute | CreateAttribute | 用户新增自定义属性接口 | To be tested |
|  | EnableAttribute | 启用自定义属性接口 | To be tested |
|  | DisableAttribute | 停用自定义属性接口 | To be tested |
|  | ListAttributes | 查询自定义属性列表接口 | To be tested |
|  | UpdateAttribute | 修改自定义属性接口 | To be tested |
|  | BatchSetAttributes | 批量设置自定义属性接口 | To be tested |
| BackPool | ListBackPools | 查询后向流量池列表 | To be tested |
|  | ListBackPoolMembers | 查询后向流量池成员列表 | To be tested |
| NetworkSwitchPolicies | ListNetworkSwitchPolicies | 查询策略列表 | To be tested |
|  | AddNetworkSwitchPolicy | 新增网络切换策略 | To be tested |
| PricePlans | ListProPricePlans | 查询套餐列表信息 | To be tested |
| SimCards | ListSimCards | 查询SIM卡列表 | To be tested |
|  | StartStopNet | SIM卡申请断网/恢复在用,接口仅支持中国电信卡调用。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。 | To be tested |
|  | SetSpeedValue | 实体卡限速接口,接口仅支持中国电信和中国联通实体卡调用。中国联通卡需要个人实名认证后才能使用限速功能。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。 | To be tested |
|  | ShowMonthUsages | 设备月用量统计 | To be tested |
|  | DeleteRealName | 清除实名认证信息,接口仅支持中国电信卡调用。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。 | To be tested |
|  | ShowSimCard | 查询SIM卡详情 | To be tested |
|  | StopSimCard | 创建停机申请,返回业务受理单号。1~2个工作日完成停机操作。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。 | To be tested |
|  | EnableSimCard | 创建激活实体卡申请,返回业务受理单号。1~2个工作日完成激活操作。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。 | To be tested |
|  | ListSimCardFlowPerDay | 批量查询SIM卡日用量接口,支持按天或按月查询。SIM卡标识和容器ID只能选一个参数,天和月也只能选一个参数 | To be tested |
|  | ShowRealNamed | 实时查询SIM卡实名认证信息,接口仅支持查询中国大陆运营商卡片的实名认证信息。 | To be tested |
|  | RegisterImei | 支持固定机卡重绑(需要上传IMEI,将SIM卡绑定到指定IMEI的设备)和普通机卡重绑(会清除之前绑定的设备,将SIM卡绑定到正在使用的设备),接口仅支持中国电信卡,中国移动卡调用。中国电信卡单卡每月只允许重绑2次,中国移动卡仅支持普通机卡重绑。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。 | To be tested |
|  | SetExceedCutNet | SIM卡达量断网/取消达量断网,接口仅支持中国电信的卡以及中国联通、中国移动的组池卡调用。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。 | To be tested |
|  | ResetSimCard | 创建复机申请,返回业务受理单号。1~2个工作日完成复机操作。注:由于运营商侧业务限制,建议您同一张SIM卡不要同时执行多种不同业务的操作。 | To be tested |
| SimDeviceMultiply | SwitchNetwork | 切换网络 | To be tested |
|  | ListSimDeviceMultiply | 通过cid或全量查询三网卡列表 | To be tested |
|  | SetNetworkSwitchPolicy | SIM卡设置网络切换策略,接口仅支持三网卡调用。 | To be tested |
| SimPool | ListSimPools | 查询流量池列表 | To be tested |
|  | ListSimPoolMembers | 查询流量池成员列表 | To be tested |
| SimPricePlans | ListSimPricePlans | SIM卡套餐列表查询,实体卡只会有一个套餐,eSIM/vSIM可能会有多个套餐 | To be tested |
|  | ListFlowBySimCards | 批量查询实体卡流量 | To be tested |
| Sms | SendSms | 发送短信,接口仅支持开通短信套餐的中国移动与中国电信卡调用。 | To be tested |
|  | ListSmsDetails | 短信发送详情,接口仅支持开通短信套餐的中国移动与中国电信卡调用 | To be tested |
| Tag | CreateTag | 添加标签接口 | To be tested |
|  | ListTags | 查询标签列表 | To be tested |
|  | DeleteTag | 删除标签 | To be tested |
|  | BatchSetTags | 批量设置/取消设置标签接口 | To be tested |
| WorkOrder | ListWorkOrders | 分页查询业务受理单 | To be tested |
|  | ListWorkOrderDetails | 分页查询业务受理明细 | To be tested |
