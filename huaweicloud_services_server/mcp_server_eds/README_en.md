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
                    <td rowspan="1">Audit Log</td>
                    <td>ShowAuditLog</td>
                    <td>Query audit logs of data assets</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Connector</td>
                    <td>ShowConnector</td>
                    <td>Query the connector details of a specified tenant</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConnectorsByInstanceUser</td>
                    <td>Query the connector list by space user</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConnectorsByInstanceManger</td>
                    <td>Query the connector list by space administrator</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Contract</td>
                    <td>CommitContract</td>
                    <td>Submit the contract</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelContract</td>
                    <td>Terminate the contract</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowContract</td>
                    <td>Query a contract</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">offer</td>
                    <td>ListOffers</td>
                    <td>Query the offering list under a specified connector</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOffer</td>
                    <td>Query the details of a specified offering</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">user</td>
                    <td>AddConnectorUser</td>
                    <td>Assigning a subaccount</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConnectorUser</td>
                    <td>Reclaiming an account</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
