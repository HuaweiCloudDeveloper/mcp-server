# CCM MCP Server 


## Version
v0.1.0

## Overview

CCM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CCM. Full-chain management of CCM resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

<html>
    <head></head>
    <body>
        <table border="1" cellspacing="0" cellpadding="5">
            <tbody>
                <tr>
                    <th>类别</th>
                    <th>工具名称</th>
                    <th>功能描述</th>
                    <th>状态</th>
                </tr>
                <tr>
                    <td rowspan="1">Certificate Lifecycle Management</td>
                    <td>ExportCertificate</td>
                    <td>Export the certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Certificate Management</td>
                    <td>DeleteCertificate</td>
                    <td>Delete a certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificate</td>
                    <td>Querying a certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificate</td>
                    <td>Create Certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Certificate revocation processing</td>
                    <td>CreateCertificateAuthorityObsAgency</td>
                    <td>The user creates an OBS agency authorization for PCA to access OBS buckets and update the revocation list (CRL).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificateAuthorityObsAgency</td>
                    <td>Check whether the user has the agency permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableCertificateAuthorityCrl</td>
                    <td>Disable the CRL of the current CA.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificateAuthorityObsBucket</td>
                    <td>Query the OBS bucket list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableCertificateAuthorityCrl</td>
                    <td>Enable the CRL of the current CA.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Order management</td>
                    <td>CreateCertificateAuthorityOrder</td>
                    <td>Subscribe to the CA.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">Private CA management</td>
                    <td>CreateCertificateAuthority</td>
                    <td>Create a CA in the following three scenarios:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>IssueCertificateAuthorityCertificate</td>
                    <td>Activates the CA.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificateAuthority</td>
                    <td>Query the CA list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeCertificateAuthority</td>
                    <td>Revocation of the child CA.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportCertificateAuthorityCsr</td>
                    <td>Export the certificate signing request of the CA.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableCertificateAuthority</td>
                    <td>Enable the CA.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableCertificateAuthority</td>
                    <td>Disable the CA.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreCertificateAuthority</td>
                    <td>Recover the CA certificate that is in the Scheduled Delete state and then the status of the CA certificate is changed to Disabled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificateAuthority</td>
                    <td>Query CA details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportCertificateAuthorityCertificate</td>
                    <td>To import the CA certificate, the following conditions must be met:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificateAuthorityQuota</td>
                    <td>Query the CA certificate quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportCertificateAuthorityCertificate</td>
                    <td>Export the CA certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCertificateAuthority</td>
                    <td>Plan to delete the CA. Specifies the number of days after which the CA certificate is to be deleted. The value can be set to 7 to 30 days after the CA certificate is deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Private Certificate Management</td>
                    <td>ListCertificate</td>
                    <td>Query the private certificate list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificateByCsr</td>
                    <td>Use the CSR to issue the certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ParseCertificateSigningRequest</td>
                    <td>Resolve the CSR.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificateQuota</td>
                    <td>Query the private certificate quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeCertificate</td>
                    <td>Revoke the certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Tag Management</td>
                    <td>ListDomainCertTags</td>
                    <td>Query the list of all certificate tags.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateCaTags</td>
                    <td>Create CA tags in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteCaTags</td>
                    <td>Delete CA tags in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateCertTags</td>
                    <td>Create certificate labels in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertTag</td>
                    <td>Create a certificate label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountCertResourceInstances</td>
                    <td>Query the number of certificates by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCaResourceInstances</td>
                    <td>Query the CA list by tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCaTags</td>
                    <td>Query the label list of the CA based on the CA certificate ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCaTag</td>
                    <td>Create a CA tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertTags</td>
                    <td>Query the label list of the certificate based on the certificate ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountCaResourceInstances</td>
                    <td>Query the number of CAs by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertResourceInstances</td>
                    <td>Query the certificate list by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainCaTags</td>
                    <td>Query the list of all CA tags.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteCertTags</td>
                    <td>Deleting certificate labels in batches.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
