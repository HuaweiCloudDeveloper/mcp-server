# KPS MCP Server 


## Version
v0.1.0

## Overview

KPS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service KPS. Full-chain management of KPS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Key Pair Management | CreateKeypair | Create and import an SSH key pair | To be tested |
|  | ClearPrivateKey | Clear the private key of the SSH key pair. | To be tested |
|  | ExportPrivateKey | Exports the private key of a specified key pair. | To be tested |
|  | UpdateKeypairDescription | Updates the description of the SSH key pair. | To be tested |
|  | ImportPrivateKey | Import the private key to the specified key pair. | To be tested |
|  | BatchImportKeypair | Import SSH key pairs in batches. A maximum of 10 records can be imported at a time. | To be tested |
|  | DeleteKeypair | Delete the SSH key pair. | To be tested |
|  | ListKeypairs | Query the SSH key pair list | To be tested |
|  | BatchExportPrivateKey | Export private keys in batches. A maximum of 10 records can be exported at a time. | To be tested |
|  | ListKeypairDetail | Query the details about an SSH key pair | To be tested |
| Key Pair Task Management | ListFailedTask | Query information about the tasks that fail to be bound or unbound. | To be tested |
|  | DeleteFailedTask | Delete a failed task. | To be tested |
|  | AssociateKeypair | Associate to a specified VM. (Replacement or reset. The SSH key pair private key configured on the VM must be provided for the replacement. The SSH key pair private key of the VM does not need to be provided for the reset.) New SSH key pair. | To be tested |
|  | BatchAssociateKeypair | This command is used to bind new SSH key pairs to specified VMs in batches. | To be tested |
|  | ListKeypairTask | Query the execution status of the current SSH key pair task based on the task_id returned by the SSH key pair interface. | To be tested |
|  | DisassociateKeypair | Unbind the SSH key pair from the specified VM and restore the SSH password for login. | To be tested |
|  | DeleteAllFailedTask | Deleting the information about the failed task. | To be tested |
|  | ListRunningTask | Query the information about the tasks being processed. | To be tested |

