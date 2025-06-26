# CSE MCP Server 


## Version
v0.1.0

## Overview

CSE MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CSE. Full-chain management of CSE resources can be carried out based on natural language.

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
                    <td rowspan="1">DDM实例管理</td>
                    <td>ListEngines</td>
                    <td>查询DDM引擎信息详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">gateway</td>
                    <td>ModifyHttp2Rpc</td>
                    <td>修改http转rpc方法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlugins</td>
                    <td>查询插件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyPlugin</td>
                    <td>修改插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHttp2Rpc</td>
                    <td>创建http转rpc方法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHttp2Rpc</td>
                    <td>删除http转rpc方法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHttp2Rpcs</td>
                    <td>查询http转rpc资源列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSinglePlugin</td>
                    <td>查询单个插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">nacos</td>
                    <td>ListNacosNamespaces</td>
                    <td>查询nacos命名空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNacosNamespaces</td>
                    <td>删除nacos命名空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNacosNamespaces</td>
                    <td>更新nacos命名空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNacosNamespaces</td>
                    <td>创建nacos命名空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">引擎版本和规格</td>
                    <td>ListFlavors</td>
                    <td>查询数据库规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">引擎管理</td>
                    <td>ShowEngine</td>
                    <td>查询微服务引擎详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEngine</td>
                    <td>删除微服务引擎。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeEngine</td>
                    <td>升级微服务引擎</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryEngine</td>
                    <td>对微服务引擎进行重试,当前支持ServiceComb专享版引擎</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEngineQuotas</td>
                    <td>查询微服务引擎配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeEngine</td>
                    <td>变更微服务引擎规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeEngineConfig</td>
                    <td>更新微服务引擎配置,更新ServiceComb专享版引擎与注册配置中心引擎的配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEngine</td>
                    <td>创建微服务引擎,支持创建ServiceComb引擎专享版、注册配置中心、应用网关(公测)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEngineJob</td>
                    <td>查询微服务引擎任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">插件管理</td>
                    <td>DeletePlugin</td>
                    <td>删除插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlugin</td>
                    <td>创建插件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">治理</td>
                    <td>ListGovernancePolicyByPolicyId</td>
                    <td>查询治理策略详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGovernancePolicy</td>
                    <td>创建治理策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGovernancePolicy</td>
                    <td>修改治理策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMicroserviceRouteRule</td>
                    <td>创建灰度发布策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGovernancePolicy</td>
                    <td>删除治理策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMicroserviceRouteRule</td>
                    <td>删除灰度发布策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGovernancePolicys</td>
                    <td>查询治理策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGovernancePolicy</td>
                    <td>查询指定类型治理策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMicroserviceRouteRule</td>
                    <td>查询微服务的灰度发布规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">配置管理</td>
                    <td>UploadKie</td>
                    <td>导入kie配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadKie</td>
                    <td>导出kie配置</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
