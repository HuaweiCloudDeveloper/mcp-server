# SFSTurbo MCP Server 


## Version
v0.1.0

## Overview

SFSTurbo MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SFSTurbo. Full-chain management of SFSTurbo resources can be carried out based on natural language.

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
                    <td rowspan="1">Connection management</td>
                    <td>ChangeSecurityGroup</td>
                    <td>Modify the security group bound to the SFS Turbo file system. If the security group modification task is an asynchronous task, you can determine whether to modify the security group status based on the sub_status field returned by Querying a Single File System. If the sub_status field is 232, the security group is successfully modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Directory management</td>
                    <td>UpdateFsDirQuota</td>
                    <td>Update target folder quota</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFsDir</td>
                    <td>Create a directory</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFsDirUsage</td>
                    <td>Query the usage of catalog resources. The backend has a cache period of 5 minutes, and the queried data may be delayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFsDirQuota</td>
                    <td>Create a target folder quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFsDir</td>
                    <td>Delete a file system directory</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFsDir</td>
                    <td>Check whether the directory exists.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFsDirQuota</td>
                    <td>Query the quota of the target folder. Querying used_capacity and used_inode data may be delayed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFsDirQuota</td>
                    <td>Delete the target folder quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">File System Management</td>
                    <td>ShowFsTask</td>
                    <td>Obtains details about a file system asynchronous task. Only the task for querying directory resource usage is supported. The value of feature in the API request path is dir-usage, which is referred to as DU task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFsTask</td>
                    <td>This API is used to create an asynchronous file system task, which supports only asynchronous query of directory resource usage. The value of feature in the API request path is dir-usage, which is referred to as DU task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetHpcCacheBackend</td>
                    <td>Configure the HPC cache backend information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFsTasks</td>
                    <td>Obtains the asynchronous task list of the file system. Only the task for querying directory resource usage is supported. The value of feature in the API request path is dir-usage, which is referred to as DU task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFsTask</td>
                    <td>If the asynchronous task is being executed, cancel and delete the task. Otherwise, delete the task. Only the task for deleting directory resource usage information can be deleted. The value of feature in the API request path is dir-usage, which is referred to as DU task for short.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Lifecycle Management</td>
                    <td>ExpandShare</td>
                    <td>Expand the file system.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteShare</td>
                    <td>Delete the file system.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateShare</td>
                    <td>Create a file system.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowShare</td>
                    <td>Query the details about an SFS Turbo file system.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListShares</td>
                    <td>Obtain the file system list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Name Management</td>
                    <td>ChangeShareName</td>
                    <td>Change the file system name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Right management</td>
                    <td>CreateLdapConfig</td>
                    <td>Create and bind LDAP configuration. Lightweight Directory Access Protocol (LDAP) is a standard protocol for accessing and controlling directory servers. The LDAP server centrally manages the user and group ownership relationships. After the LDAP server is bound, when a user accesses a file in your file system, SFS Turbo accesses your LDAP server for user authentication and obtains the user and group ownership relationships. In this way, the Linux standard file UGO permission check is performed. To use this function, you need to set up an LDAP server. Currently, SFS Turbo supports only LDAP v3.. Common directory servers that provide LDAP access include OpenLdap (Linux) and Active Directory (Windows). The implementation details vary with directory servers. Therefore, the corresponding Schema must be specified during binding. (If the Schema configuration is incorrect, SFS Turbo cannot obtain the correct user and group information. As a result, SFS Turbo cannot access files in the file system.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLdapConfig</td>
                    <td>Query the LDAP configuration. Lightweight Directory Access Protocol (LDAP) is a standard protocol used to access and control a directory server. The LDAP server manages the user and group homing relationships in a centralized manner. When a user accesses files in your file system, SFS Turbo accesses your LDAP server for user authentication and obtains the homing relationships between users and groups. In this way, the Linux standard file UGO permission check is performed. To use this function, you need to set up an LDAP server. Currently, SFS Turbo supports only LDAP v3. Common directory servers that provide LDAP access include OpenLdap (Linux) and Active Directory (Windows). The implementation details vary according to directory servers. Therefore, the corresponding Schema must be specified during binding. (If the schema is incorrectly configured, SFS Turbo cannot obtain the correct user and group information, and files in the file system may not be accessed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePermRule</td>
                    <td>Modifying a permission rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePermRule</td>
                    <td>Create a permission rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePermRule</td>
                    <td>Delete a permission rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPermRule</td>
                    <td>Query a permission rule of a file system</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLdapConfig</td>
                    <td>Modify LDAP configuration. Lightweight Directory Access Protocol (LDAP) is a standard protocol for accessing and controlling directory servers. The LDAP server centrally manages the user and group ownership relationships. After the LDAP server is bound, when a user accesses a file in your file system, SFS Turbo accesses your LDAP server for user authentication and obtains the user and group ownership relationships. In this way, the Linux standard file UGO permission check is performed. To use this function, you need to set up an LDAP server. Currently, SFS Turbo supports only LDAP v3. Common directory servers that provide LDAP access include OpenLdap (Linux) and Active Directory (Windows). The implementation details vary according to directory servers. Therefore, the corresponding Schema must be specified during binding. (If the Schema configuration is incorrect, SFS Turbo cannot obtain the correct user and group information, which may cause users to have no permission to access files in the file system.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPermRules</td>
                    <td>Query the file system permission rule list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLdapConfig</td>
                    <td>Delete the LDAP configuration. Lightweight Directory Access Protocol (LDAP) is a standard protocol for accessing and controlling directory servers. The LDAP server manages the user and group homing relationships in a centralized manner. When a user accesses files in your file system, SFS Turbo accesses your LDAP server for user authentication and obtains the homing relationships between users and groups. In this way, the Linux standard file UGO permission check is performed. To use this function, you need to set up an LDAP server. Currently, SFS Turbo supports only LDAP v3.. Common directory servers that provide LDAP access include OpenLdap (Linux) and Active Directory (Windows). The implementation details vary with directory servers. Therefore, the corresponding Schema must be specified during binding. (If the schema is incorrectly configured, SFS Turbo cannot obtain the correct user and group information, and files in the file system may not be accessed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Shared Label</td>
                    <td>ListSharedTags</td>
                    <td>Query the set of all shared tags of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSharedTags</td>
                    <td>Query all tags of a specified share.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSharedTag</td>
                    <td>Add a label to a specified share.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddSharedTags</td>
                    <td>Add tags to a specified share in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSharedTag</td>
                    <td>This API is used to delete a tag from a specified share. If the key to be deleted does not exist in the share, error 404 is returned when the interface is invoked.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSharesByTag</td>
                    <td>Query the file system list by label</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Storage association management</td>
                    <td>ListHpcCacheTasks</td>
                    <td>Query the data import and export task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateObsTargetAttributes</td>
                    <td>Update backend storage attributes</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHpcCacheTask</td>
                    <td>Delete a data import and export task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackendTarget</td>
                    <td>Delete backend storage</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHpcCacheTask</td>
                    <td>Create a data import and export task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackendTargetInfo</td>
                    <td>Obtain details about backend storage</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHpcShare</td>
                    <td>Updates the time for eliminating cold data in the file system.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateObsTargetPolicy</td>
                    <td>Update the automatic synchronization policy of the backend storage.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackendTargets</td>
                    <td>Query the backend storage list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHpcCacheTask</td>
                    <td>Query details about a data import and export task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBackendTarget</td>
                    <td>Associating backend storage to the SFS Turbo file system</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Task Management</td>
                    <td>ShowJobDetail</td>
                    <td>Query the execution status of a job. This API is used to query the execution status of an SFS Turbo asynchronous API. For example, you can use the jobId returned by calling the interface for creating and binding LDAP configuration to query the execution status of a job.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
