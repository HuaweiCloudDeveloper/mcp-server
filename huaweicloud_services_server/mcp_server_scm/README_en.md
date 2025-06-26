# SCM MCP Server 


## Version
v0.1.0

## Overview

SCM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SCM. Full-chain management of SCM resources can be carried out based on natural language.

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
                    <td rowspan="7">CSR Management</td>
                    <td>ShowCsrPrivateKey</td>
                    <td>Query the private key.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCsr</td>
                    <td>Query the CSR list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadCsr</td>
                    <td>Upload the CSR.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCsr</td>
                    <td>Query the CSR.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCsr</td>
                    <td>Delete the CSR.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCsr</td>
                    <td>Update the CSR.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCsr</td>
                    <td>Create a CSR.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Certificate Application Management</td>
                    <td>CancelCertificateRequest</td>
                    <td>Withdraw the certificate application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplyCertificate</td>
                    <td>Apply for a certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Certificate Deployment Management</td>
                    <td>ListDeployedResources</td>
                    <td>Query the resource where the certificate has been deployed. For issued and uploaded non-national secret certificates.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeployCertificate</td>
                    <td>Deploy the SSL certificate to other HUAWEI CLOUD products, such as Elastic Load Balance (Elastic Load Balance), Web Application Firewall (WAF), and Content Delivery Network (CDN).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchPushCertificate</td>
                    <td>Push SSL certificates to other HUAWEI CLOUD products, such as Elastic Load Balance (Elastic Load Balance), Web Application Firewall (WAF), and Content Delivery Network (CDN) in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PushCertificate</td>
                    <td>Push the SSL certificate to other HUAWEI CLOUD products, such as Elastic Load Balance (Elastic Load Balance), Web Application Firewall (WAF), and Content Delivery Network (CDN).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Certificate Label Management</td>
                    <td>BatchCreateOrDeleteTags</td>
                    <td>Create or delete tags in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagsByCertificate</td>
                    <td>Query the tag list based on the certificate ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificateTag</td>
                    <td>Create a tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllTags</td>
                    <td>Query the list of all tags.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificatesByTag</td>
                    <td>Query the certificate list by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Certificate Lifecycle Management</td>
                    <td>ImportCertificate</td>
                    <td>Import the certificate to CCM.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportCertificate</td>
                    <td>Export the certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Certificate Management</td>
                    <td>ListCertificates</td>
                    <td>Query the certificate list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
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
                    <td rowspan="2">Certificate Order Management</td>
                    <td>SubscribeCertificate</td>
                    <td>Purchasing an SSL certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnsubscribeCertificate</td>
                    <td>Unsubscribe from the certificate.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
