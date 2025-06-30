# DDM MCP Server 


## Version
v0.1.0

## Overview

DDM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DDM. Full-chain management of DDM resources can be carried out based on natural language.

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
                    <td rowspan="1">Allied management</td>
                    <td>ListNodes</td>
                    <td>Function description: Users can use this API to query the list of trusted nodes (including aggregation nodes and compute nodes) in an alliance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Asset Management</td>
                    <td>ListUsers</td>
                    <td>Query the server list of the account</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">DDM Account Management</td>
                    <td>ResetAdministrator</td>
                    <td>Create a DDM administrator account and set a password when the DDM administrator is invoked for the first time. Only the administrator password will be updated on subsequent invocations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetUserPassword</td>
                    <td>Reset the password of an existing DDM account.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUsers</td>
                    <td>The DDM account is used to connect to and manage schemas. A maximum of 100 DDM accounts can be created for a DDM instance. A DDM account can be associated with multiple schemas.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">DDM Instance Management</td>
                    <td>UpdateReadAndWriteStrategy</td>
                    <td>Modify the read policy of the database instance associated with DDM.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandDdmInstanceNodes</td>
                    <td>Performs scale-up of the nodes of a specified DDM instance. On-demand and yearly/monthly DB instances are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceParam</td>
                    <td>Query the parameter details of a specified DDM instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDdmEngines</td>
                    <td>Query the DDM engine information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDatabaseInfo</td>
                    <td>Synchronize the configuration information of all DNs associated with the current DDM instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNode</td>
                    <td>Query the DDM instance node details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGroup</td>
                    <td>Create a group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceParam</td>
                    <td>Modifies DDM instance parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceSecurityGroup</td>
                    <td>Modify the security group of a DDM instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDdmJobResult</td>
                    <td>Obtain the task information with a specified ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGroup</td>
                    <td>Obtains the instance group list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeFlavor</td>
                    <td>Change the DDM instance specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDdmFlavors</td>
                    <td>Query DDM AZ specifications</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEngines</td>
                    <td>Query the DDM engine details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDdmInstance</td>
                    <td>This API is used to delete a specified DDM instance and release all resources of the instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebuildConfig</td>
                    <td>In the cross-region DR scenario, table data is reloaded for the target DDM instance to synchronize data.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandInstanceNodes</td>
                    <td>Performs the scale-up of the nodes of a specified DDM instance. Both pay-per-use and yearly/monthly DB instances are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">DDM Monitoring Management</td>
                    <td>ListSlowLog</td>
                    <td>Query information about slow SQL statements executed on a DDM instance within a specified period.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReadWriteRatio</td>
                    <td>Query the number of read and write times of a DDM instance within a specified period.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">DDM Schema Management</td>
                    <td>ShowDatabase</td>
                    <td>Query details about a specified schema.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDdmDatabase</td>
                    <td>Create a DDM schema.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableRdsList</td>
                    <td>Query the list of database instances available for creating a schema.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDdmDatabase</td>
                    <td>Delete a specified schema.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">DDM Session Management</td>
                    <td>ExecuteKillPhysicalProcesses</td>
                    <td>Kill a physical session</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProcessesAuditLog</td>
                    <td>Query the audit logs of the kill session</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLogicalProcesses</td>
                    <td>Query the logical session list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPhysicalProcesses</td>
                    <td>Query the physical session list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteKillLogicalProcesses</td>
                    <td>kill logical session</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Database security</td>
                    <td>SwitchSsl</td>
                    <td>Set SSL data encryption.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Engine version and specification</td>
                    <td>ListFlavors</td>
                    <td>Query database specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Exclusive Instance Management</td>
                    <td>CreateInstance</td>
                    <td>Create an exclusive WAF engine instance. The exclusive mode supports the following sites: CN East-Qingdao, Middle East-Riyadh, CN North-Beijing 1, CN North-Beijing4, CN North-Ulanqab 1, CN East-Shanghai1, CN East-Shanghai2, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Southwest-Guiyang1, and Asia Pacific. - Bangkok, Asia Pacific - Singapore, Johannesburg, Africa, Türkiye - Istanbul; Sites that are exclusively supported by common tenants: CN North-Beijing4, CN East-Shanghai1, CN South-Guangzhou, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>Query the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>Deletes the information about the exclusive WAF engine. The exclusive mode is supported only at some sites, including CN North-Beijing 4, CN East-Shanghai 1, CN South-Guangzhou, CN South-Shenzhen, China-Hong Kong, Asia Pacific-Bangkok, and Asia Pacific-Singapore.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Instance Management</td>
                    <td>ShrinkInstanceNodes</td>
                    <td>Delete the instance node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartInstance</td>
                    <td>Restarts a specified instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateWeakPassword</td>
                    <td>Verify the password security of the database user root.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Instance management</td>
                    <td>UpdateInstanceName</td>
                    <td>Change the instance name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Lifecycle Management</td>
                    <td>ListInstances</td>
                    <td>Query the instance list of a tenant. Query by condition is supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Managing Databases and Users (MySQL)</td>
                    <td>DeleteDatabase</td>
                    <td>Delete the database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabases</td>
                    <td>Query the database list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabase</td>
                    <td>Create a database.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Obtain log information</td>
                    <td>ListSlowLogs</td>
                    <td>Query slow database logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">OpenStack - API version information</td>
                    <td>ListApiVersion</td>
                    <td>All available API versions (only for native OpenStack APIs) are returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Parameter Configuration</td>
                    <td>ListDdmConfigurations</td>
                    <td>Obtains the parameter template list, including all default DDM parameter templates and user-created parameter templates.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfiguration</td>
                    <td>Obtains the parameters of a specified parameter template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">User management</td>
                    <td>UpdateUser</td>
                    <td>Modify user parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUser</td>
                    <td>Delete a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Version Management</td>
                    <td>ChangeDatabaseVersion</td>
                    <td>Change the kernel version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRiskInfo</td>
                    <td>Kernel version risk warning</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseAvailableVersions</td>
                    <td>Querying the kernel version that can be changed</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollBackDatabaseVersion</td>
                    <td>Roll back the kernel version</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
