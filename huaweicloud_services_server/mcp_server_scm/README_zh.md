# SCM MCP Server 

## 版本信息
v0.1.0

## 产品描述

SCM MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务SCM交互的能力。可以基于自然语言对SCM资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| CSR管理 | ShowCsrPrivateKey | 查询私钥。 | To be tested |
|  | ListCsr | 查询CSR列表。 | To be tested |
|  | UploadCsr | 上传CSR。 | To be tested |
|  | ShowCsr | 查询CSR。 | To be tested |
|  | DeleteCsr | 删除CSR。 | To be tested |
|  | UpdateCsr | 更新CSR。 | To be tested |
|  | CreateCsr | 创建CSR。 | To be tested |
| 证书标签管理 | BatchCreateOrDeleteTags | 批量创建或删除标签。 | To be tested |
|  | ListTagsByCertificate | 根据证书ID查询标签列表。 | To be tested |
|  | CreateCertificateTag | 创建标签。 | To be tested |
|  | ListAllTags | 查询所有标签列表。 | To be tested |
|  | ListCertificatesByTag | 根据标签查询证书列表。 | To be tested |
| 证书生命周期管理 | ImportCertificate | 导入证书到CCM服务管理。 | To be tested |
|  | ListCertificates | 根据证书名称或绑定域名查询证书列表。 | To be tested |
|  | DeleteCertificate | 删除证书实例,即将证书资源从系统中删除。 | To be tested |
|  | ExportCertificate | 导出证书。 | To be tested |
|  | ShowCertificate | 查询某张证书的详细信息。 | To be tested |
| 证书申请管理 | CancelCertificateRequest | 撤回证书申请。 | To be tested |
|  | ApplyCertificate | 申请证书。 | To be tested |
| 证书订单管理 | SubscribeCertificate | 购买SSL证书。 | To be tested |
|  | UnsubscribeCertificate | 退订证书。 | To be tested |
| 证书部署管理 | ListDeployedResources | 查询证书已部署的具体资源。针对已签发和上传的非国密证书。 | To be tested |
|  | DeployCertificate | 部署SSL证书到弹性负载均衡(Elastic Load Balance,简称ELB)、Web应用防火墙(Web Application Firewall,WAF)、CDN(Content Delivery Network,内容分发网络)等其它华为云产品中。 | To be tested |
|  | BatchPushCertificate | 批量推送SSL证书到弹性负载均衡(Elastic Load Balance,简称ELB)、Web应用防火墙(Web Application Firewall,WAF)、CDN(Content Delivery Network,内容分发网络)等其它华为云产品中。 | To be tested |
|  | PushCertificate | 推送SSL证书到弹性负载均衡(Elastic Load Balance,简称ELB)、Web应用防火墙(Web Application Firewall,WAF)、CDN(Content Delivery Network,内容分发网络)等其它华为云产品中。 | To be tested |
