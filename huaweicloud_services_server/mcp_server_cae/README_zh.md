# CAE MCP Server 

## 版本信息
v0.1.0

## 产品描述

CAE MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CAE交互的能力。可以基于自然语言对CAE资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Agency | CreateAgency | 创建委托。 | To be tested |
|  | ListAgencies | 获取委托列表。 | To be tested |
| Application | ListApplications | 获取应用列表。 | To be tested |
|  | DeleteApplication | 删除应用。 | To be tested |
|  | ShowApplication | 获取应用详情。 | To be tested |
|  | CreateApplication | 创建应用。 | To be tested |
| Certificate | UpdateCertificate | 修改证书。 | To be tested |
|  | ListCertificates | 获取证书列表。 | To be tested |
|  | DeleteCertificate | 删除证书。 | To be tested |
|  | CreateCertificate | 创建证书。 | To be tested |
| Component | ListComponentInstances | 获取组件实例列表。 | To be tested |
|  | CreateComponent | 创建组件。 | To be tested |
|  | DeleteComponent | 删除组件。 | To be tested |
|  | ListComponents | 获取组件列表。 | To be tested |
|  | CreateComponentWithConfiguration | 创建、生效配置并部署组件。 | To be tested |
|  | ExecuteAction | 对组件执行指定操作,如部署、升级、重启、停止、启动、伸缩、配置、回滚。 | To be tested |
|  | ShowComponent | 获取组件详情。 | To be tested |
|  | UpdateComponent | 更新组件。 | To be tested |
|  | ListComponentSnapshots | 获取组件快照列表。 | To be tested |
| ComponentConfiguration | CreateComponentConfiguration | 创建组件配置。 | To be tested |
|  | DeleteComponentConfiguration | 删除组件配置。 | To be tested |
|  | ListComponentConfigurations | 获取组件配置列表。 | To be tested |
| Domain | ListDomains | 获取域名列表。 | To be tested |
|  | DeleteDomain | 删除域名。 | To be tested |
|  | CreateDomain | 创建域名。 | To be tested |
| Eip | UpdateEip | 修改出入网带宽以及开闭状态。 | To be tested |
|  | ListEips | 获取集群节点弹性公网IP列表。 | To be tested |
| Environment | ListEnvironments | 获取环境列表。 | To be tested |
|  | CreateEnvironment | 创建环境。 | To be tested |
|  | DeleteEnvironment | 删除环境。 | To be tested |
| Job | RetryJob | 重试任务。 | To be tested |
|  | ShowJob | 获取任务详情。 | To be tested |
| MonitorSystem | CreateMonitorSystem | 创建监控系统配置。 | To be tested |
|  | UpdateMonitorSystem | 更新监控系统配置。 | To be tested |
|  | ShowMonitorSystem | 获取监控系统配置。 | To be tested |
| NoticeRule | UpdateNoticeRule | 修改事件通知规则。 | To be tested |
|  | DeleteNoticeRule | 删除事件通知规则。 | To be tested |
|  | CreateNoticeRule | 创建事件通知规则。 | To be tested |
|  | ShowNoticeRule | 查询事件通知规则。 | To be tested |
|  | ListNoticeRules | 查询事件通知规则列表。 | To be tested |
| Secret | CreateSecret | 关联租户已注册的凭据。 | To be tested |
|  | UpdateSecret | 修改用户已在DEW服务上注册的凭据版本。 | To be tested |
|  | DeleteSecret | 删除用户已在DEW服务上注册的凭据。 | To be tested |
|  | ListEffectiveComponents | 获取当前正在使用的对应凭据组件列表。 | To be tested |
|  | ListSecrets | 获取用户现有的凭据。 | To be tested |
| Volume | ListVolumes | 获取云存储列表。 | To be tested |
|  | DeleteVolume | 解绑云存储。 | To be tested |
|  | CreateVolume | 授权云存储。 | To be tested |
| VpcEgress | CreateVpcEgress | 创建CAE环境访问VPC配置。 | To be tested |
|  | DeleteVpcEgress | 删除CAE环境访问VPC配置。 | To be tested |
|  | ListVpcEgress | 获取CAE环境访问VPC配置。 | To be tested |
| timer-rules | CreateTimerRule | 创建定时启停规则。 | To be tested |
|  | ListTimerRules | 获取定时启停规则列表。 | To be tested |
|  | DeleteTimerRule | 删除定时启停规则。 | To be tested |
|  | UpdateTimerRule | 修改定时启停规则。 | To be tested |
|  | ShowExecutionResult | 获取上次定时启停规则的执行情况。 | To be tested |
