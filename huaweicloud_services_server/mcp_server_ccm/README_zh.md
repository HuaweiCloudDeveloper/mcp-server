# CCM MCP Server 

## 版本信息
v0.1.0

## 产品描述

CCM MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CCM交互的能力。可以基于自然语言对CCM资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 标签管理 | ListDomainCertTags | 查询所有证书标签列表。 | To be tested |
|  | BatchCreateCaTags | 批量创建CA标签。 | To be tested |
|  | BatchDeleteCaTags | 批量删除CA标签。 | To be tested |
|  | BatchCreateCertTags | 批量创建证书标签。 | To be tested |
|  | CreateCertTag | 创建证书标签。 | To be tested |
|  | CountCertResourceInstances | 根据标签查询证书数量。 | To be tested |
|  | ListCaResourceInstances | 根据标签查询CA列表。 | To be tested |
|  | ListCaTags | 根据CA证书ID查询此CA的标签列表。 | To be tested |
|  | CreateCaTag | 创建CA标签。 | To be tested |
|  | ListCertTags | 根据证书ID查询此证书的标签列表。 | To be tested |
|  | CountCaResourceInstances | 根据标签查询CA数量。 | To be tested |
|  | ListCertResourceInstances | 根据标签查询证书列表。 | To be tested |
|  | ListDomainCaTags | 查询所有CA标签列表。 | To be tested |
|  | BatchDeleteCertTags | 批量删除证书标签。 | To be tested |
| 私有CA管理 | CreateCertificateAuthority | 创建CA,分以下三种情况: | To be tested |
|  | IssueCertificateAuthorityCertificate | 激活CA。 | To be tested |
|  | ListCertificateAuthority | 查询CA列表。 | To be tested |
|  | RevokeCertificateAuthority | 吊销子CA。 | To be tested |
|  | ExportCertificateAuthorityCsr | 导出CA的证书签名请求。 | To be tested |
|  | EnableCertificateAuthority | 启用CA。 | To be tested |
|  | DisableCertificateAuthority | 禁用CA。 | To be tested |
|  | RestoreCertificateAuthority | 恢复CA,将处于“计划删除”状态的CA证书,重新恢复为“已禁用”状态。 | To be tested |
|  | ShowCertificateAuthority | 查询CA详情。 | To be tested |
|  | ImportCertificateAuthorityCertificate | 导入CA证书,使用本接口需要满足以下条件: | To be tested |
|  | ShowCertificateAuthorityQuota | 查询CA证书配额。 | To be tested |
|  | ExportCertificateAuthorityCertificate | 导出CA证书。 | To be tested |
|  | DeleteCertificateAuthority | 计划删除CA。计划多少天后删除CA证书,可设置7天~30天内删除。 | To be tested |
| 私有证书管理 | ListCertificate | 查询私有证书列表。 | To be tested |
|  | DeleteCertificate | 删除证书。 | To be tested |
|  | ShowCertificate | 查询证书详情。 | To be tested |
|  | CreateCertificateByCsr | 通过CSR签发证书。功能约束如下: | To be tested |
|  | ParseCertificateSigningRequest | 解析CSR。 | To be tested |
|  | ShowCertificateQuota | 查询私有证书配额。 | To be tested |
|  | RevokeCertificate | 吊销证书。 | To be tested |
|  | ExportCertificate | 导出证书。 | To be tested |
|  | CreateCertificate | 申请证书。 | To be tested |
| 订单管理 | CreateCertificateAuthorityOrder | 购买CA。 | To be tested |
| 证书吊销处理 | CreateCertificateAuthorityObsAgency | 用户给PCA创建OBS委托授权,用于访问OBS桶,更新吊销列表。 | To be tested |
|  | ShowCertificateAuthorityObsAgency | 查看是否具有委托权限。 | To be tested |
|  | DisableCertificateAuthorityCrl | 禁用当前CA的CRL。 | To be tested |
|  | ListCertificateAuthorityObsBucket | 查询OBS桶列表。 | To be tested |
|  | EnableCertificateAuthorityCrl | 启用当前CA的CRL。 | To be tested |
