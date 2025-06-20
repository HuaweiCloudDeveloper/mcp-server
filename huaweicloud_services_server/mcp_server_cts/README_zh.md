# CTS MCP Server 

## 版本信息
v0.1.0

## 产品描述

CTS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CTS交互的能力。可以基于自然语言对CTS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 事件管理 | ListTraces | 通过事件列表查询接口,可以查出系统记录的7天内资源操作记录。 | To be tested |
| 关键操作通知管理 | DeleteNotification | 云审计服务支持删除已创建的关键操作通知。 | To be tested |
|  | ListNotifications | 查询创建的关键操作通知规则。 | To be tested |
|  | UpdateNotification | 云审计服务支持修改已创建关键操作通知配置项,通过notification_id的字段匹配修改对象,notification_id必须已经存在。 | To be tested |
|  | CreateNotification | 配置关键操作通知,可在发生特定操作时,使用预先创建好的SMN主题,向用户手机、邮箱发送消息,也可直接发送http/https消息。常用于实时感知高危操作、触发特定操作或对接用户自有审计分析系统。 | To be tested |
| 其它接口 | ListUserResources | 查询30天事件的操作用户列表。 | To be tested |
|  | ListOperations | 查询云服务的全量操作列表。 | To be tested |
|  | ListQuotas | 查询租户追踪器配额信息。 | To be tested |
|  | CheckObsBuckets | 检查已经配置OBS桶是否可以成功转储。 | To be tested |
|  | ListTraceResources | 查询事件的资源类型列表。 | To be tested |
| 标签管理 | BatchCreateResourceTags | 批量添加CTS资源标签。 | To be tested |
|  | BatchDeleteResourceTags | 批量删除CTS资源标签。 | To be tested |
| 追踪器管理 | CreateTracker | 云审计服务开通后系统会自动创建一个追踪器,用来关联系统记录的所有操作。目前,一个云账户在一个Region下支持创建一个管理类追踪器和多个数据类追踪器。 | To be tested |
|  | DeleteTracker | 云审计服务目前仅支持删除已创建的数据类追踪器。删除追踪器对已有的操作记录没有影响,当您重新开通云审计服务后,依旧可以查看已有的操作记录。 | To be tested |
|  | UpdateTracker | 云审计服务支持修改已创建追踪器的配置项,包括OBS桶转储、关键事件通知、事件转储加密、通过LTS对管理类事件进行检索、事件文件完整性校验以及追踪器启停状态等相关参数,修改追踪器对已有的操作记录没有影响。修改追踪器完成后,系统立即以新的规则开始记录操作。 | To be tested |
|  | ListTrackers | 开通云审计服务成功后,您可以在追踪器信息页面查看追踪器的详细信息。详细信息主要包括追踪器名称,用于存储操作事件的OBS桶名称和OBS桶中的事件文件前缀。 | To be tested |
