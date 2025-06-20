# EVS MCP Server 

## 版本信息
v0.1.0

## 产品描述

EVS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务EVS交互的能力。可以基于自然语言对EVS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| API版本信息查询 | ShowVersion | 查询接口的指定版本信息。 | To be tested |
|  | ListVersions | 查询接口版本信息列表。 | To be tested |
| 云硬盘 | RetypeVolume | 对按需或者包周期云硬盘进行磁盘类型变更。 | To be tested |
|  | ListVolumes | 查询所有云硬盘的详细信息。 | To be tested |
|  | CinderListAvailabilityZones | 查询所有的可用分区信息。 | To be tested |
|  | ResizeVolume | 对按需或者包周期云硬盘进行扩容。 | To be tested |
|  | DeleteVolume | 删除一个云硬盘。 | To be tested |
|  | UpdateVolume | 更新一个云硬盘的名称和描述。 | To be tested |
|  | UnsubscribePostpaidVolume | 退订包周期计费模式的云硬盘,有如下约束: | To be tested |
|  | ModifyVolumeQoS | 调整云硬盘的iops或者吞吐量。 | To be tested |
|  | CreateVolume | 创建按需或包周期云硬盘。 | To be tested |
|  | CinderListQuotas | 查询租户的详细配额。 | To be tested |
|  | CinderListVolumeTypes | 查询云硬盘类型列表。 | To be tested |
|  | ShowVolume | 查询单个云硬盘的详细信息。支持企业项目授权功能。 | To be tested |
| 云硬盘快照 | RollbackSnapshot | 将快照数据回滚到云硬盘。支持企业项目授权功能。 | To be tested |
|  | ListSnapshots | 查询云硬盘快照详细列表信息。 | To be tested |
|  | DeleteSnapshot | 删除云硬盘快照。 | To be tested |
|  | CreateSnapshot | 创建云硬盘快照。 | To be tested |
|  | ShowSnapshot | 查询单个云硬盘快照信息。支持企业项目授权功能。 | To be tested |
|  | UpdateSnapshot | 更新云硬盘快照。支持企业项目授权功能。 | To be tested |
| 云硬盘标签 | ShowVolumeTags | 查询指定云硬盘的标签信息。 | To be tested |
|  | ListVolumeTags | 获取某个租户的所有云硬盘资源的标签信息。 | To be tested |
|  | ListVolumesByTags | 通过标签查询云硬盘资源实例详情。 | To be tested |
|  | BatchCreateVolumeTags | 为指定云硬盘批量添加标签。 | To be tested |
|  | BatchDeleteVolumeTags | 为指定云硬盘批量删除标签。 | To be tested |
| 云硬盘过户 | CinderDeleteVolumeTransfer | 当云硬盘过户未被接受时,您可以删除云硬盘过户记录,接受后则无法执行删除操作。 | To be tested |
|  | CinderListVolumeTransfers | 查询当前租户下所有云硬盘的过户记录列表 | To be tested |
|  | CinderCreateVolumeTransfer | 指定云硬盘来创建云硬盘过户记录,创建成功后,会返回过户记录ID以及身份认证密钥。 | To be tested |
|  | CinderShowVolumeTransfer | 查询单个云硬盘的过户记录详情,比如过户记录创建时间、ID以及名称等信息。 | To be tested |
|  | CinderAcceptVolumeTransfer | 通过云硬盘过户记录ID以及身份认证密钥来接受云硬盘过户。 | To be tested |
| 其他 | ShowJob | 查询Job的执行状态。 | To be tested |
