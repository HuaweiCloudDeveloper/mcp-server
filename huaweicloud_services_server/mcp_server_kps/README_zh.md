# KPS MCP Server 


## Version
v0.1.0

## Overview

KPS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service KPS. Full-chain management of KPS resources can be carried out based on natural language.

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
                    <td rowspan="8">密钥对任务管理</td>
                    <td>ListFailedTask</td>
                    <td>查询绑定、解绑等操作失败的任务信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFailedTask</td>
                    <td>删除失败的任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateKeypair</td>
                    <td>给指定的虚拟机绑定(替换或重置,替换需提供虚拟机已配置的SSH密钥对私钥;重置不需要提供虚拟机的SSH密钥对私钥)新的SSH密钥对。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAssociateKeypair</td>
                    <td>给指定的虚拟机批量绑定新的SSH密钥对。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeypairTask</td>
                    <td>根据SSH密钥对接口返回的task_id,查询SSH密钥对当前任务的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateKeypair</td>
                    <td>给指定的虚拟机解除绑定SSH密钥对并恢复SSH密码登录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAllFailedTask</td>
                    <td>删除操作失败的任务信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRunningTask</td>
                    <td>查询正在处理的任务信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">密钥对管理</td>
                    <td>CreateKeypair</td>
                    <td>创建和导入SSH密钥对</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ClearPrivateKey</td>
                    <td>清除SSH密钥对私钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportPrivateKey</td>
                    <td>导出指定密钥对的私钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKeypairDescription</td>
                    <td>更新SSH密钥对描述。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportPrivateKey</td>
                    <td>导入私钥到指定密钥对。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchImportKeypair</td>
                    <td>批量导入SSH密钥对,单次批量导入不得超过10条记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKeypair</td>
                    <td>删除SSH密钥对。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeypairs</td>
                    <td>查询SSH密钥对列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchExportPrivateKey</td>
                    <td>批量导出密钥对私钥,单次最多导出10条数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeypairDetail</td>
                    <td>查询SSH密钥对详细信息</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
