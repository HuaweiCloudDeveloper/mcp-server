# CodeArtsInspector MCP Server 

## 版本信息
v0.1.0

## 产品描述

CodeArtsInspector MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CodeArtsInspector交互的能力。可以基于自然语言对CodeArtsInspector资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| host_groups | ListGroups | 获取主机组列表 | To be tested |
|  | DeleteGroup | 删除主机组 | To be tested |
|  | AddGroup | 批量创建主机组 | To be tested |
| host_results | ListHostResults | 获取主机漏洞扫描结果 | To be tested |
| host_tasks | BatchStartHostTasks | 批量启动或取消主机漏洞扫描任务 | To be tested |
| hosts | BatchCreateHosts | 批量创建租户的主机资产 | To be tested |
|  | DeleteHost | 删除租户的主机资产 | To be tested |
|  | ListHosts | 获取租户的主机资产列表 | To be tested |
| purchase | CreatePurchaseOrder | 订购下单接口 | To be tested |
|  | ShowSubscription | 资源版本查询接口 | To be tested |
|  | UpdatePurchaseOrder | 变更下单接口 | To be tested |
| web_results | ShowReportStatus | 获取网站扫描PDF报告生成状态 | To be tested |
|  | DownloadTaskReport | 下载网站扫描任务PDF报告 | To be tested |
|  | UpdateFalsePositive | 更新网站扫描漏洞的误报状态 | To be tested |
|  | ExecuteGenerateReport | 生成网站扫描PDF报告 | To be tested |
|  | ListPortResults | 获取网站端口扫描结果 | To be tested |
|  | ListBusinessRisks | 获取网站业务风险扫描结果 | To be tested |
|  | ShowResults | 获取网站漏洞扫描结果 | To be tested |
| web_tasks | CreateTasks | 创建网站漏洞扫描任务并启动 | To be tested |
|  | CancelTasks | 取消或重启网站漏洞扫描任务 | To be tested |
|  | ShowTasks | 获取网站漏洞扫描任务详情 | To be tested |
|  | ListTaskHistories | 获取网站漏洞扫描的历史扫描任务 | To be tested |
| websites | DeleteDomains | 删除租户的网站资产 | To be tested |
|  | AuthorizeDomains | 认证租户的网站资产 | To be tested |
|  | UpdateDomainSettings | 更新网站登录配置 | To be tested |
|  | CreateDomains | 创建租户的网站资产 | To be tested |
|  | ListDomains | 获取租户的所有网站资产 | To be tested |
|  | ShowDomainSettings | 获取网站登录配置 | To be tested |
