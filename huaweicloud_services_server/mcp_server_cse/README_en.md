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
                    <td rowspan="2">Configuration Management</td>
                    <td>UploadKie</td>
                    <td>Importing the kie configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadKie</td>
                    <td>Exporting the kie configuration</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">DDM Instance Management</td>
                    <td>ListEngines</td>
                    <td>Query the DDM engine details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Engine Management</td>
                    <td>ShowEngine</td>
                    <td>Query the details of a microservice engine</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEngine</td>
                    <td>Delete a microservice engine.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeEngine</td>
                    <td>Upgrading the Microservice Engine</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryEngine</td>
                    <td>Retry the microservice engine. Currently, only ServiceComb is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEngineQuotas</td>
                    <td>Query the CSE quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeEngine</td>
                    <td>Change the CSE specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeEngineConfig</td>
                    <td>Update the configuration of the CSE, including the configuration of the ServiceComb exclusive engine and the registration configuration center engine.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEngine</td>
                    <td>Create a microservice engine. You can create the ServiceComb exclusive edition, register with the configuration center, and AGW (open beta test).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEngineJob</td>
                    <td>Query the details of a CSE task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Engine version and specification</td>
                    <td>ListFlavors</td>
                    <td>Query database specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Governance</td>
                    <td>ListGovernancePolicyByPolicyId</td>
                    <td>Query governance policy details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGovernancePolicy</td>
                    <td>Create a governance policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGovernancePolicy</td>
                    <td>Modify a governance policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMicroserviceRouteRule</td>
                    <td>Create a gray release policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGovernancePolicy</td>
                    <td>Delete a governance policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMicroserviceRouteRule</td>
                    <td>Delete the dark launch policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGovernancePolicys</td>
                    <td>Query the governance policy list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGovernancePolicy</td>
                    <td>Query the governance policy list of a specified type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMicroserviceRouteRule</td>
                    <td>Query the dark launch rules of a microservice.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Plug-in management</td>
                    <td>DeletePlugin</td>
                    <td>Delete the plug-in.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlugin</td>
                    <td>Create plug-in information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">gateway</td>
                    <td>ModifyHttp2Rpc</td>
                    <td>Modify the HTTP-to-RPC conversion method.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlugins</td>
                    <td>Query the plug-in list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyPlugin</td>
                    <td>Modify the plug-in.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHttp2Rpc</td>
                    <td>Create an HTTP-to-RPC method.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHttp2Rpc</td>
                    <td>The HTTP-to-RPC method is deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHttp2Rpcs</td>
                    <td>Query the list of resources converted from HTTP to RPC.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSinglePlugin</td>
                    <td>Query a single plug-in.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">nacos</td>
                    <td>ListNacosNamespaces</td>
                    <td>Query the nacos namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNacosNamespaces</td>
                    <td>Delete the nacos namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNacosNamespaces</td>
                    <td>Update the nacos namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNacosNamespaces</td>
                    <td>Create the nacos namespace.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
