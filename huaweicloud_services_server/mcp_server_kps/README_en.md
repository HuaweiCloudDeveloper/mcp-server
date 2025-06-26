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
                    <td rowspan="10">Key Pair Management</td>
                    <td>CreateKeypair</td>
                    <td>Create and import an SSH key pair</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ClearPrivateKey</td>
                    <td>Clear the private key of the SSH key pair.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportPrivateKey</td>
                    <td>Exports the private key of a specified key pair.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKeypairDescription</td>
                    <td>Updates the description of the SSH key pair.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportPrivateKey</td>
                    <td>Import the private key to the specified key pair.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchImportKeypair</td>
                    <td>Import SSH key pairs in batches. A maximum of 10 records can be imported at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKeypair</td>
                    <td>Delete the SSH key pair.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeypairs</td>
                    <td>Query the SSH key pair list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchExportPrivateKey</td>
                    <td>Export private keys in batches. A maximum of 10 records can be exported at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeypairDetail</td>
                    <td>Query the details about an SSH key pair</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Key Pair Task Management</td>
                    <td>ListFailedTask</td>
                    <td>Query information about the tasks that fail to be bound or unbound.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFailedTask</td>
                    <td>Delete a failed task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateKeypair</td>
                    <td>Associate to a specified VM. (Replacement or reset. The SSH key pair private key configured on the VM must be provided for the replacement. The SSH key pair private key of the VM does not need to be provided for the reset.) New SSH key pair.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAssociateKeypair</td>
                    <td>This command is used to bind new SSH key pairs to specified VMs in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeypairTask</td>
                    <td>Query the execution status of the current SSH key pair task based on the task_id returned by the SSH key pair interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateKeypair</td>
                    <td>Unbind the SSH key pair from the specified VM and restore the SSH password for login.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAllFailedTask</td>
                    <td>Deleting the information about the failed task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRunningTask</td>
                    <td>Query the information about the tasks being processed.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
