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
                    <td rowspan="7">CSR管理</td>
                    <td>ShowCsrPrivateKey</td>
                    <td>查询私钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCsr</td>
                    <td>查询CSR列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadCsr</td>
                    <td>上传CSR。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCsr</td>
                    <td>查询CSR。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCsr</td>
                    <td>删除CSR。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCsr</td>
                    <td>更新CSR。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCsr</td>
                    <td>创建CSR。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">证书标签管理</td>
                    <td>BatchCreateOrDeleteTags</td>
                    <td>批量创建或删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagsByCertificate</td>
                    <td>根据证书ID查询标签列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificateTag</td>
                    <td>创建标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllTags</td>
                    <td>查询所有标签列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificatesByTag</td>
                    <td>根据标签查询证书列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">证书生命周期管理</td>
                    <td>ImportCertificate</td>
                    <td>导入证书到CCM服务管理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportCertificate</td>
                    <td>导出证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">证书申请管理</td>
                    <td>CancelCertificateRequest</td>
                    <td>撤回证书申请。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplyCertificate</td>
                    <td>申请证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">证书管理</td>
                    <td>ListCertificates</td>
                    <td>查询证书列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
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
                    <td rowspan="2">证书订单管理</td>
                    <td>SubscribeCertificate</td>
                    <td>购买SSL证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnsubscribeCertificate</td>
                    <td>退订证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">证书部署管理</td>
                    <td>ListDeployedResources</td>
                    <td>查询证书已部署的具体资源。针对已签发和上传的非国密证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeployCertificate</td>
                    <td>部署SSL证书到弹性负载均衡(Elastic Load Balance,简称ELB)、Web应用防火墙(Web Application Firewall,WAF)、CDN(Content Delivery Network,内容分发网络)等其它华为云产品中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchPushCertificate</td>
                    <td>批量推送SSL证书到弹性负载均衡(Elastic Load Balance,简称ELB)、Web应用防火墙(Web Application Firewall,WAF)、CDN(Content Delivery Network,内容分发网络)等其它华为云产品中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PushCertificate</td>
                    <td>推送SSL证书到弹性负载均衡(Elastic Load Balance,简称ELB)、Web应用防火墙(Web Application Firewall,WAF)、CDN(Content Delivery Network,内容分发网络)等其它华为云产品中。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
