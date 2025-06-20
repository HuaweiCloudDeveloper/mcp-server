# SFSTurbo MCP Server 


## Version
v0.1.0

## Overview

SFSTurbo MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SFSTurbo. Full-chain management of SFSTurbo resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Connection management | ChangeSecurityGroup | Modify the security group bound to the SFS Turbo file system. If the security group modification task is an asynchronous task, you can determine whether to modify the security group status based on the sub_status field returned by Querying a Single File System. If the sub_status field is 232, the security group is successfully modified. | To be tested |
| Directory management | UpdateFsDirQuota | Update target folder quota | To be tested |
|  | CreateFsDir | Create a directory | To be tested |
|  | ShowFsDirUsage | Query the usage of catalog resources. The backend has a cache period of 5 minutes, and the queried data may be delayed. | To be tested |
|  | CreateFsDirQuota | Create a target folder quota. | To be tested |
|  | DeleteFsDir | Delete a file system directory | To be tested |
|  | ShowFsDir | Check whether the directory exists. | To be tested |
|  | ShowFsDirQuota | Query the quota of the target folder. Querying used_capacity and used_inode data may be delayed. | To be tested |
|  | DeleteFsDirQuota | Delete the target folder quota. | To be tested |
| File System Management | ShowFsTask | Obtains details about a file system asynchronous task. Only the task for querying directory resource usage is supported. The value of feature in the API request path is dir-usage, which is referred to as DU task. | To be tested |
|  | CreateFsTask | This API is used to create an asynchronous file system task, which supports only asynchronous query of directory resource usage. The value of feature in the API request path is dir-usage, which is referred to as DU task. | To be tested |
|  | SetHpcCacheBackend | Configure the HPC cache backend information | To be tested |
|  | ListFsTasks | Obtains the asynchronous task list of the file system. Only the task for querying directory resource usage is supported. The value of feature in the API request path is dir-usage, which is referred to as DU task. | To be tested |
|  | DeleteFsTask | If the asynchronous task is being executed, cancel and delete the task. Otherwise, delete the task. Only the task for deleting directory resource usage information can be deleted. The value of feature in the API request path is dir-usage, which is referred to as DU task for short. | To be tested |
| Lifecycle Management | ExpandShare | Expand the file system. | To be tested |
|  | DeleteShare | Delete the file system. | To be tested |
|  | CreateShare | Create a file system. | To be tested |
|  | ShowShare | Query the details about an SFS Turbo file system. | To be tested |
|  | ListShares | Obtain the file system list | To be tested |
| Name Management | ChangeShareName | Change the file system name | To be tested |
| Right management | CreateLdapConfig | Create and bind LDAP configuration. Lightweight Directory Access Protocol (LDAP) is a standard protocol for accessing and controlling directory servers. The LDAP server centrally manages the user and group ownership relationships. After the LDAP server is bound, when a user accesses a file in your file system, SFS Turbo accesses your LDAP server for user authentication and obtains the user and group ownership relationships. In this way, the Linux standard file UGO permission check is performed. To use this function, you need to set up an LDAP server. Currently, SFS Turbo supports only LDAP v3.. Common directory servers that provide LDAP access include OpenLdap (Linux) and Active Directory (Windows). The implementation details vary with directory servers. Therefore, the corresponding Schema must be specified during binding. (If the Schema configuration is incorrect, SFS Turbo cannot obtain the correct user and group information. As a result, SFS Turbo cannot access files in the file system. | To be tested |
|  | ShowLdapConfig | Query the LDAP configuration. Lightweight Directory Access Protocol (LDAP) is a standard protocol used to access and control a directory server. The LDAP server manages the user and group homing relationships in a centralized manner. When a user accesses files in your file system, SFS Turbo accesses your LDAP server for user authentication and obtains the homing relationships between users and groups. In this way, the Linux standard file UGO permission check is performed. To use this function, you need to set up an LDAP server. Currently, SFS Turbo supports only LDAP v3. Common directory servers that provide LDAP access include OpenLdap (Linux) and Active Directory (Windows). The implementation details vary according to directory servers. Therefore, the corresponding Schema must be specified during binding. (If the schema is incorrectly configured, SFS Turbo cannot obtain the correct user and group information, and files in the file system may not be accessed. | To be tested |
|  | UpdatePermRule | Modifying a permission rule | To be tested |
|  | CreatePermRule | Create a permission rule | To be tested |
|  | DeletePermRule | Delete a permission rule | To be tested |
|  | ShowPermRule | Query a permission rule of a file system | To be tested |
|  | UpdateLdapConfig | Modify LDAP configuration. Lightweight Directory Access Protocol (LDAP) is a standard protocol for accessing and controlling directory servers. The LDAP server centrally manages the user and group ownership relationships. After the LDAP server is bound, when a user accesses a file in your file system, SFS Turbo accesses your LDAP server for user authentication and obtains the user and group ownership relationships. In this way, the Linux standard file UGO permission check is performed. To use this function, you need to set up an LDAP server. Currently, SFS Turbo supports only LDAP v3. Common directory servers that provide LDAP access include OpenLdap (Linux) and Active Directory (Windows). The implementation details vary according to directory servers. Therefore, the corresponding Schema must be specified during binding. (If the Schema configuration is incorrect, SFS Turbo cannot obtain the correct user and group information, which may cause users to have no permission to access files in the file system. | To be tested |
|  | ListPermRules | Query the file system permission rule list | To be tested |
|  | DeleteLdapConfig | Delete the LDAP configuration. Lightweight Directory Access Protocol (LDAP) is a standard protocol for accessing and controlling directory servers. The LDAP server manages the user and group homing relationships in a centralized manner. When a user accesses files in your file system, SFS Turbo accesses your LDAP server for user authentication and obtains the homing relationships between users and groups. In this way, the Linux standard file UGO permission check is performed. To use this function, you need to set up an LDAP server. Currently, SFS Turbo supports only LDAP v3.. Common directory servers that provide LDAP access include OpenLdap (Linux) and Active Directory (Windows). The implementation details vary with directory servers. Therefore, the corresponding Schema must be specified during binding. (If the schema is incorrectly configured, SFS Turbo cannot obtain the correct user and group information, and files in the file system may not be accessed. | To be tested |
| Shared Label | ListSharedTags | Query the set of all shared tags of a tenant. | To be tested |
|  | ShowSharedTags | Query all tags of a specified share. | To be tested |
|  | CreateSharedTag | Add a label to a specified share. | To be tested |
|  | BatchAddSharedTags | Add tags to a specified share in batches. | To be tested |
|  | DeleteSharedTag | This API is used to delete a tag from a specified share. If the key to be deleted does not exist in the share, error 404 is returned when the interface is invoked. | To be tested |
|  | ListSharesByTag | Query the file system list by label | To be tested |
| Storage association management | ListHpcCacheTasks | Query the data import and export task list | To be tested |
|  | UpdateObsTargetAttributes | Update backend storage attributes | To be tested |
|  | DeleteHpcCacheTask | Delete a data import and export task | To be tested |
|  | DeleteBackendTarget | Delete backend storage | To be tested |
|  | CreateHpcCacheTask | Create a data import and export task | To be tested |
|  | ShowBackendTargetInfo | Obtain details about backend storage | To be tested |
|  | UpdateHpcShare | Updates the time for eliminating cold data in the file system. | To be tested |
|  | UpdateObsTargetPolicy | Update the automatic synchronization policy of the backend storage. | To be tested |
|  | ListBackendTargets | Query the backend storage list | To be tested |
|  | ShowHpcCacheTask | Query details about a data import and export task | To be tested |
|  | CreateBackendTarget | Associating backend storage to the SFS Turbo file system | To be tested |
| Task Management | ShowJobDetail | Query the execution status of a job. This API is used to query the execution status of an SFS Turbo asynchronous API. For example, you can use the jobId returned by calling the interface for creating and binding LDAP configuration to query the execution status of a job. | To be tested |

