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
                    <td rowspan="14">标签管理</td>
                    <td>ListDomainCertTags</td>
                    <td>查询所有证书标签列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateCaTags</td>
                    <td>批量创建CA标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteCaTags</td>
                    <td>批量删除CA标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateCertTags</td>
                    <td>批量创建证书标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertTag</td>
                    <td>创建证书标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountCertResourceInstances</td>
                    <td>根据标签查询证书数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCaResourceInstances</td>
                    <td>根据标签查询CA列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCaTags</td>
                    <td>根据CA证书ID查询此CA的标签列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCaTag</td>
                    <td>创建CA标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertTags</td>
                    <td>根据证书ID查询此证书的标签列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountCaResourceInstances</td>
                    <td>根据标签查询CA数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertResourceInstances</td>
                    <td>根据标签查询证书列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainCaTags</td>
                    <td>查询所有CA标签列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteCertTags</td>
                    <td>批量删除证书标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">私有CA管理</td>
                    <td>CreateCertificateAuthority</td>
                    <td>创建CA,分以下三种情况:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>IssueCertificateAuthorityCertificate</td>
                    <td>激活CA。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificateAuthority</td>
                    <td>查询CA列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeCertificateAuthority</td>
                    <td>吊销子CA。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportCertificateAuthorityCsr</td>
                    <td>导出CA的证书签名请求。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableCertificateAuthority</td>
                    <td>启用CA。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableCertificateAuthority</td>
                    <td>禁用CA。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreCertificateAuthority</td>
                    <td>恢复CA,将处于“计划删除”状态的CA证书,重新恢复为“已禁用”状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificateAuthority</td>
                    <td>查询CA详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportCertificateAuthorityCertificate</td>
                    <td>导入CA证书,使用本接口需要满足以下条件:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificateAuthorityQuota</td>
                    <td>查询CA证书配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportCertificateAuthorityCertificate</td>
                    <td>导出CA证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCertificateAuthority</td>
                    <td>计划删除CA。计划多少天后删除CA证书,可设置7天~30天内删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">私有证书管理</td>
                    <td>ListCertificate</td>
                    <td>查询私有证书列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificateByCsr</td>
                    <td>通过CSR签发证书。功能约束如下:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ParseCertificateSigningRequest</td>
                    <td>解析CSR。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificateQuota</td>
                    <td>查询私有证书配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeCertificate</td>
                    <td>吊销证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">订单管理</td>
                    <td>CreateCertificateAuthorityOrder</td>
                    <td>购买CA。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">证书吊销处理</td>
                    <td>CreateCertificateAuthorityObsAgency</td>
                    <td>用户给PCA创建OBS委托授权,用于访问OBS桶,更新吊销列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificateAuthorityObsAgency</td>
                    <td>查看是否具有委托权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableCertificateAuthorityCrl</td>
                    <td>禁用当前CA的CRL。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificateAuthorityObsBucket</td>
                    <td>查询OBS桶列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableCertificateAuthorityCrl</td>
                    <td>启用当前CA的CRL。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">证书生命周期管理</td>
                    <td>ExportCertificate</td>
                    <td>导出证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">证书管理</td>
                    <td>DeleteCertificate</td>
                    <td>删除证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCertificate</td>
                    <td>查询证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificate</td>
                    <td>创建证书</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
