# SCM MCP Server 


## Version
v0.1.0

## Overview

SCM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SCM. Full-chain management of SCM resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| CSR Management | ShowCsrPrivateKey | Query the private key. | To be tested |
|  | ListCsr | Query the CSR list. | To be tested |
|  | UploadCsr | Upload the CSR. | To be tested |
|  | ShowCsr | Query the CSR. | To be tested |
|  | DeleteCsr | Delete the CSR. | To be tested |
|  | UpdateCsr | Update the CSR. | To be tested |
|  | CreateCsr | Create a CSR. | To be tested |
| Certificate Application Management | CancelCertificateRequest | Withdraw the certificate application. | To be tested |
|  | ApplyCertificate | Apply for a certificate. | To be tested |
| Certificate Deployment Management | ListDeployedResources | Query the resource where the certificate has been deployed. For issued and uploaded non-national secret certificates. | To be tested |
|  | DeployCertificate | Deploy the SSL certificate to other HUAWEI CLOUD products, such as Elastic Load Balance (Elastic Load Balance), Web Application Firewall (WAF), and Content Delivery Network (CDN). | To be tested |
|  | BatchPushCertificate | Push SSL certificates to other HUAWEI CLOUD products, such as Elastic Load Balance (Elastic Load Balance), Web Application Firewall (WAF), and Content Delivery Network (CDN) in batches. | To be tested |
|  | PushCertificate | Push the SSL certificate to other HUAWEI CLOUD products, such as Elastic Load Balance (Elastic Load Balance), Web Application Firewall (WAF), and Content Delivery Network (CDN). | To be tested |
| Certificate Label Management | BatchCreateOrDeleteTags | Create or delete tags in batches. | To be tested |
|  | ListTagsByCertificate | Query the tag list based on the certificate ID. | To be tested |
|  | CreateCertificateTag | Create a tag. | To be tested |
|  | ListAllTags | Query the list of all tags. | To be tested |
|  | ListCertificatesByTag | Query the certificate list by label. | To be tested |
| Certificate Lifecycle Management | ImportCertificate | Import the certificate to CCM. | To be tested |
|  | ExportCertificate | Export the certificate. | To be tested |
| Certificate Management | ListCertificates | Query the certificate list | To be tested |
|  | DeleteCertificate | Delete a certificate | To be tested |
|  | ShowCertificate | Querying a certificate | To be tested |
| Certificate Order Management | SubscribeCertificate | Purchasing an SSL certificate. | To be tested |
|  | UnsubscribeCertificate | Unsubscribe from the certificate. | To be tested |

