# EDS MCP Server 


## Version
v0.1.0

## Overview

EDS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EDS. Full-chain management of EDS resources can be carried out based on natural language.

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
                    <td rowspan="2">offer</td>
                    <td>ListOffers</td>
                    <td>查询指定连接器下的offer列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOffer</td>
                    <td>查询指定offer详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">user</td>
                    <td>AddConnectorUser</td>
                    <td>分配子账号</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnectorUser</td>
                    <td>账号回收</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">合约</td>
                    <td>CommitContract</td>
                    <td>提交合约</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelContract</td>
                    <td>终止合约</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowContract</td>
                    <td>查询合约</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">审计日志</td>
                    <td>ShowAuditLog</td>
                    <td>查询数据资产的审计日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">连接器</td>
                    <td>ShowConnector</td>
                    <td>查询指定租户的连接器详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConnectorsByInstanceUser</td>
                    <td>按空间用户查询连接器列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConnectorsByInstanceManger</td>
                    <td>按空间管理员查询连接器列表</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
