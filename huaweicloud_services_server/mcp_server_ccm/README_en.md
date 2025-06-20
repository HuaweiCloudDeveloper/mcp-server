# CCM MCP Server 


## Version
v0.1.0

## Overview

CCM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CCM. Full-chain management of CCM resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Certificate Lifecycle Management | ExportCertificate | Export the certificate. | To be tested |
| Certificate Management | DeleteCertificate | Delete a certificate | To be tested |
|  | ShowCertificate | Querying a certificate | To be tested |
|  | CreateCertificate | Create Certificate | To be tested |
| Certificate revocation processing | CreateCertificateAuthorityObsAgency | The user creates an OBS agency authorization for PCA to access OBS buckets and update the revocation list (CRL). | To be tested |
|  | ShowCertificateAuthorityObsAgency | Check whether the user has the agency permission. | To be tested |
|  | DisableCertificateAuthorityCrl | Disable the CRL of the current CA. | To be tested |
|  | ListCertificateAuthorityObsBucket | Query the OBS bucket list. | To be tested |
|  | EnableCertificateAuthorityCrl | Enable the CRL of the current CA. | To be tested |
| Order management | CreateCertificateAuthorityOrder | Subscribe to the CA. | To be tested |
| Private CA management | CreateCertificateAuthority | Create a CA in the following three scenarios: | To be tested |
|  | IssueCertificateAuthorityCertificate | Activates the CA. | To be tested |
|  | ListCertificateAuthority | Query the CA list. | To be tested |
|  | RevokeCertificateAuthority | Revocation of the child CA. | To be tested |
|  | ExportCertificateAuthorityCsr | Export the certificate signing request of the CA. | To be tested |
|  | EnableCertificateAuthority | Enable the CA. | To be tested |
|  | DisableCertificateAuthority | Disable the CA. | To be tested |
|  | RestoreCertificateAuthority | Recover the CA certificate that is in the Scheduled Delete state and then the status of the CA certificate is changed to Disabled. | To be tested |
|  | ShowCertificateAuthority | Query CA details. | To be tested |
|  | ImportCertificateAuthorityCertificate | To import the CA certificate, the following conditions must be met: | To be tested |
|  | ShowCertificateAuthorityQuota | Query the CA certificate quota. | To be tested |
|  | ExportCertificateAuthorityCertificate | Export the CA certificate. | To be tested |
|  | DeleteCertificateAuthority | Plan to delete the CA. Specifies the number of days after which the CA certificate is to be deleted. The value can be set to 7 to 30 days after the CA certificate is deleted. | To be tested |
| Private Certificate Management | ListCertificate | Query the private certificate list. | To be tested |
|  | CreateCertificateByCsr | Use the CSR to issue the certificate.  | To be tested |
|  | ParseCertificateSigningRequest | Resolve the CSR. | To be tested |
|  | ShowCertificateQuota | Query the private certificate quota. | To be tested |
|  | RevokeCertificate | Revoke the certificate. | To be tested |
| Tag Management | ListDomainCertTags | Query the list of all certificate tags. | To be tested |
|  | BatchCreateCaTags | Create CA tags in batches. | To be tested |
|  | BatchDeleteCaTags | Delete CA tags in batches. | To be tested |
|  | BatchCreateCertTags | Create certificate labels in batches. | To be tested |
|  | CreateCertTag | Create a certificate label. | To be tested |
|  | CountCertResourceInstances | Query the number of certificates by label. | To be tested |
|  | ListCaResourceInstances | Query the CA list by tag. | To be tested |
|  | ListCaTags | Query the label list of the CA based on the CA certificate ID. | To be tested |
|  | CreateCaTag | Create a CA tag. | To be tested |
|  | ListCertTags | Query the label list of the certificate based on the certificate ID. | To be tested |
|  | CountCaResourceInstances | Query the number of CAs by label. | To be tested |
|  | ListCertResourceInstances | Query the certificate list by label. | To be tested |
|  | ListDomainCaTags | Query the list of all CA tags. | To be tested |
|  | BatchDeleteCertTags | Deleting certificate labels in batches. | To be tested |

