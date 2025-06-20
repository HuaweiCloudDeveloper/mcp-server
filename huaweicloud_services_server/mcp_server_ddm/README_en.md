# DDM MCP Server 


## Version
v0.1.0

## Overview

DDM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DDM. Full-chain management of DDM resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Allied management | ListNodes | Function description: Users can use this API to query the list of trusted nodes (including aggregation nodes and compute nodes) in an alliance. | To be tested |
| Asset Management | ListUsers | Query the server list of the account | To be tested |
| DDM Account Management | ResetAdministrator | Create a DDM administrator account and set a password when the DDM administrator is invoked for the first time. Only the administrator password will be updated on subsequent invocations. | To be tested |
|  | ResetUserPassword | Reset the password of an existing DDM account. | To be tested |
|  | CreateUsers | The DDM account is used to connect to and manage schemas. A maximum of 100 DDM accounts can be created for a DDM instance. A DDM account can be associated with multiple schemas. | To be tested |
| DDM Instance Management | UpdateReadAndWriteStrategy | Modify the read policy of the database instance associated with DDM. | To be tested |
|  | ExpandDdmInstanceNodes | Performs scale-up of the nodes of a specified DDM instance. On-demand and yearly/monthly DB instances are supported. | To be tested |
|  | ShowInstanceParam | Query the parameter details of a specified DDM instance. | To be tested |
|  | ListDdmEngines | Query the DDM engine information | To be tested |
|  | UpdateDatabaseInfo | Synchronize the configuration information of all DNs associated with the current DDM instance. | To be tested |
|  | ShowNode | Query the DDM instance node details. | To be tested |
|  | CreateGroup | Create a group | To be tested |
|  | UpdateInstanceParam | Modifies DDM instance parameters. | To be tested |
|  | UpdateInstanceSecurityGroup | Modify the security group of a DDM instance. | To be tested |
|  | ShowDdmJobResult | Obtain the task information with a specified ID | To be tested |
|  | ListGroup | Obtains the instance group list. | To be tested |
|  | ResizeFlavor | Change the DDM instance specifications. | To be tested |
|  | ListDdmFlavors | Query DDM AZ specifications | To be tested |
|  | ListEngines | Query the DDM engine details. | To be tested |
|  | DeleteDdmInstance | This API is used to delete a specified DDM instance and release all resources of the instance. | To be tested |
|  | RebuildConfig | In the cross-region DR scenario, table data is reloaded for the target DDM instance to synchronize data. | To be tested |
|  | ExpandInstanceNodes | Performs the scale-up of the nodes of a specified DDM instance. Both pay-per-use and yearly/monthly DB instances are supported. | To be tested |
| DDM Monitoring Management | ListSlowLog | Query information about slow SQL statements executed on a DDM instance within a specified period. | To be tested |
|  | ListReadWriteRatio | Query the number of read and write times of a DDM instance within a specified period. | To be tested |
| DDM Schema Management | ShowDatabase | Query details about a specified schema. | To be tested |
|  | CreateDdmDatabase | Create a DDM schema. | To be tested |
|  | ListAvailableRdsList | Query the list of database instances available for creating a schema. | To be tested |
|  | DeleteDdmDatabase | Delete a specified schema. | To be tested |
| DDM Session Management | ExecuteKillPhysicalProcesses | Kill a physical session | To be tested |
|  | ShowProcessesAuditLog | Query the audit logs of the kill session | To be tested |
|  | ShowLogicalProcesses | Query the logical session list | To be tested |
|  | ShowPhysicalProcesses | Query the physical session list | To be tested |
|  | ExecuteKillLogicalProcesses | kill logical session | To be tested |
| Database security | SwitchSsl | Set SSL data encryption. | To be tested |
| Engine version and specification | ListFlavors | Query database specifications. | To be tested |
| Exclusive Instance Management | CreateInstance | Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore | To be tested |
|  | ShowInstance | Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
|  | DeleteInstance | Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore. | To be tested |
| Instance Management | ShrinkInstanceNodes | Delete the instance node. | To be tested |
|  | RestartInstance | Restarts a specified instance. | To be tested |
|  | ValidateWeakPassword | Verify the password security of the database user root. | To be tested |
| Instance management | UpdateInstanceName | Change the instance name. | To be tested |
| Lifecycle Management | ListInstances | Query the instance list of a tenant. Query by condition is supported. | To be tested |
| Managing Databases and Users (MySQL) | DeleteDatabase | Delete the database. | To be tested |
|  | ListDatabases | Query the database list. | To be tested |
|  | CreateDatabase | Create a database. | To be tested |
| Obtain log information | ListSlowLogs | Query slow database logs. | To be tested |
| OpenStack - API version information | ListApiVersion | All available API versions (only for native OpenStack APIs) are returned. | To be tested |
| Parameter Configuration | ListDdmConfigurations | Obtains the parameter template list, including all default DDM parameter templates and user-created parameter templates. | To be tested |
|  | ShowConfiguration | Obtains the parameters of a specified parameter template. | To be tested |
| User management | UpdateUser | Modify user parameters. | To be tested |
|  | DeleteUser | Delete a user. | To be tested |
| Version Management | ChangeDatabaseVersion | Change the kernel version | To be tested |
|  | ShowRiskInfo | Kernel version risk warning | To be tested |
|  | ListDatabaseAvailableVersions | Querying the kernel version that can be changed | To be tested |
|  | RollBackDatabaseVersion | Roll back the kernel version | To be tested |

