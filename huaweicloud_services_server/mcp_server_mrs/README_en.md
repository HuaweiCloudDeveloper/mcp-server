# MRS MCP Server 


## Version
v0.1.0

## Overview

MRS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service MRS. Full-chain management of MRS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Allied management | ListNodes | Function description: Users can use this API to query the list of trusted nodes (including aggregation nodes and compute nodes) in an alliance. | To be tested |
| Autoscaling interface | DeleteAutoScalingPolicy | Delete an AS policy. | To be tested |
|  | CreateScalingPolicy | Edit the AS rule. | To be tested |
|  | UpdateAutoScalingPolicy | Update the AS policy. | To be tested |
|  | ShowAutoScalingPolicy | Displays the information about all AS policies of a specified cluster. | To be tested |
|  | CreateAutoScalingPolicy | Create an AS policy. | To be tested |
| Certificate Label Management | ListAllTags | Query the list of all tags. | To be tested |
| Cluster HDFS File Interface | ShowHdfsFileList | Obtain the file list in the specified directory in the MRS cluster. | To be tested |
| Cluster management interface | UpdateClusterScaling | After a cluster is created, expand or reduce the capacity of the core or task nodes in the cluster. After an MRS cluster is created, the number of master nodes cannot be adjusted. That is, the master nodes cannot be scaled in or out. This interface is not compatible with Sahara. | To be tested |
|  | RunJobFlow | Create an MRS cluster, submit a job, and delete the cluster after the job is complete. MRS 1.8.9 or later is supported. Before using the API, you need to obtain the resource information listed in. | To be tested |
|  | DeleteCluster | You can delete the cluster service after data processing and analysis are complete or the cluster is running abnormally and cannot provide services. This interface is compatible with Sahara. | To be tested |
|  | ListClusters | View the cluster list created by the user. This interface is not compatible with Sahara. | To be tested |
|  | ListHosts | This API is used to query details about the host list in the input cluster. | To be tested |
|  | CreateCluster | Create an MRS cluster and submit a job in the cluster. This interface is not compatible with Sahara. | To be tested |
|  | ShowClusterDetails | View details about a specified cluster. This interface is not compatible with Sahara. | To be tested |
|  | UpdateClusterName | Change the cluster name | To be tested |
| ClusterManagement | ExpandCluster | Expand the capacity of the MRS cluster. | To be tested |
|  | AddComponent | Adding a component to a cluster | To be tested |
|  | ShrinkCluster | The MRS cluster is scaled in. | To be tested |
| DataConnectorManagement | UpdateDataConnector | Update data connection | To be tested |
|  | ListDataConnector | Query the data connection list | To be tested |
|  | CreateDataConnector | Create a data connection | To be tested |
|  | DeleteDataConnector | Delete a data connection | To be tested |
| Entrusted management | UpdateAgencyMapping | Updates the mapping between the user or user group and the IAM agency. | To be tested |
|  | ShowAgencyMapping | Obtains details about the mapping between users (user groups) and IAM agencies. | To be tested |
| IAMSyncManagement | UpdateSyncIamUser | Synchronize IAM users and user groups to Manager. If a user is specified, the IAM user group associated with the user will also be synchronized to Manager. | To be tested |
|  | CancelSyncIamUser | Cancel synchronization of a specified user or user group | To be tested |
|  | ShowSyncIamUser | Obtain synchronized IAM users and user groups. | To be tested |
| Job management interface | ShowJobExeListNew | Query the job list in a specified MRS cluster. | To be tested |
|  | ShowSingleJobExe | Query details about a specified job in the MRS cluster. | To be tested |
|  | ShowSqlResultWithJob | Query the query results returned after the SQL statements of SparkSQL and SparkScript jobs in the MRS cluster are executed. | To be tested |
|  | BatchDeleteJobs | Delete jobs in batches from the MRS cluster. | To be tested |
|  | StopJob | This API is used to terminate a specified job in the MRS cluster. | To be tested |
|  | CreateExecuteJob | Add and submit a job in the MRS cluster. | To be tested |
| Other interfaces | ListAvailableZones | When creating an instance, you need to configure the ID of the AZ where the instance is located. You can use this API to query the ID of the AZ. | To be tested |
| Quota | ShowTagQuota | Query the quota information about a tag. | To be tested |
| SQL interface | CancelSql | Cancel the execution of an SQL statement in the MRS cluster. | To be tested |
|  | ShowSqlResult | Query the execution result of an SQL statement in the MRS cluster. | To be tested |
|  | ExecuteSql | Submit and run an SQL statement in the MRS cluster. | To be tested |
| Tag management interface | CreateClusterTag | Add a tag to a specific cluster. | To be tested |
|  | ListClustersByTags | Filter clusters by label. | To be tested |
|  | ListClusterTags | Query the label information of a specified cluster. | To be tested |
|  | BatchDeleteClusterTags | This API is used to delete tags from a specified cluster in batches. | To be tested |
|  | DeleteClusterTag | Delete the tag of a specific cluster. | To be tested |
|  | BatchCreateClusterTags | Add tags to a specified cluster in batches. | To be tested |
| TagManagement | SwitchClusterTags | Enable or disable the default cluster label for an existing cluster. After this function is enabled, nodes in the cluster are labeled with the default cluster labels. | To be tested |
|  | ShowTagStatus | Query the default label status of a cluster | To be tested |
| VersionMetaQuery | ShowMrsVersionList | Displays the MRS version list. | To be tested |
|  | ShowMrsFlavors | Query the available specifications of the MRS cluster version | To be tested |
|  | ShowMrsVersionMetadata | Query the metadata of the corresponding version. If the cluster ID is specified in the parameter, the latest metadata of the cluster after the patch is updated can be queried. | To be tested |

