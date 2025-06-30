# MRS MCP Server 


## Version
v0.1.0

## Overview

MRS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service MRS. Full-chain management of MRS resources can be carried out based on natural language.

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
                    <td rowspan="5">Autoscaling interface</td>
                    <td>DeleteAutoScalingPolicy</td>
                    <td>Delete an AS policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScalingPolicy</td>
                    <td>Edit the AS rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutoScalingPolicy</td>
                    <td>Update the AS policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoScalingPolicy</td>
                    <td>Displays the information about all AS policies of a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutoScalingPolicy</td>
                    <td>Create an AS policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Certificate Label Management</td>
                    <td>ListAllTags</td>
                    <td>Query the list of all tags.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Cluster HDFS File Interface</td>
                    <td>ShowHdfsFileList</td>
                    <td>Obtain the file list in the specified directory in the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Cluster management interface</td>
                    <td>UpdateClusterScaling</td>
                    <td>After a cluster is created, expand or reduce the capacity of the core or task nodes in the cluster. After an MRS cluster is created, the number of master nodes cannot be adjusted. That is, the master nodes cannot be scaled in or out. This interface is not compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunJobFlow</td>
                    <td>Create an MRS cluster, submit a job, and delete the cluster after the job is complete. MRS 1.8.9 or later is supported. Before using the API, you need to obtain the resource information listed in.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCluster</td>
                    <td>You can delete the cluster service after data processing and analysis are complete or the cluster is running abnormally and cannot provide services. This interface is compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusters</td>
                    <td>View the cluster list created by the user. This interface is not compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHosts</td>
                    <td>This API is used to query details about the host list in the input cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCluster</td>
                    <td>Create an MRS cluster and submit a job in the cluster. This interface is not compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterDetails</td>
                    <td>View details about a specified cluster. This interface is not compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClusterName</td>
                    <td>Change the cluster name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ClusterManagement</td>
                    <td>ExpandCluster</td>
                    <td>Expand the capacity of the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddComponent</td>
                    <td>Adding a component to a cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShrinkCluster</td>
                    <td>The MRS cluster is scaled in.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">DataConnectorManagement</td>
                    <td>UpdateDataConnector</td>
                    <td>Update data connection</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataConnector</td>
                    <td>Query the data connection list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataConnector</td>
                    <td>Create a data connection</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDataConnector</td>
                    <td>Delete a data connection</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Entrusted management</td>
                    <td>UpdateAgencyMapping</td>
                    <td>Updates the mapping between the user or user group and the IAM agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgencyMapping</td>
                    <td>Obtains details about the mapping between users (user groups) and IAM agencies.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">IAMSyncManagement</td>
                    <td>UpdateSyncIamUser</td>
                    <td>Synchronize IAM users and user groups to Manager. If a user is specified, the IAM user group associated with the user will also be synchronized to Manager.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelSyncIamUser</td>
                    <td>Cancel synchronization of a specified user or user group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSyncIamUser</td>
                    <td>Obtain synchronized IAM users and user groups.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Job management interface</td>
                    <td>ShowJobExeListNew</td>
                    <td>Query the job list in a specified MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSingleJobExe</td>
                    <td>Query details about a specified job in the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlResultWithJob</td>
                    <td>Query the query results returned after the SQL statements of SparkSQL and SparkScript jobs in the MRS cluster are executed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteJobs</td>
                    <td>Delete jobs in batches from the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopJob</td>
                    <td>This API is used to terminate a specified job in the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateExecuteJob</td>
                    <td>Add and submit a job in the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Other interfaces</td>
                    <td>ListAvailableZones</td>
                    <td>When creating an instance, you need to configure the ID of the AZ where the instance is located. You can use this API to query the ID of the AZ.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowTagQuota</td>
                    <td>Query the quota information about a tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">SQL interface</td>
                    <td>CancelSql</td>
                    <td>Cancel the execution of an SQL statement in the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlResult</td>
                    <td>Query the execution result of an SQL statement in the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteSql</td>
                    <td>Submit and run an SQL statement in the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Tag management interface</td>
                    <td>CreateClusterTag</td>
                    <td>Add a tag to a specific cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClustersByTags</td>
                    <td>Filter clusters by label.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterTags</td>
                    <td>Query the label information of a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteClusterTags</td>
                    <td>This API is used to delete tags from a specified cluster in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClusterTag</td>
                    <td>Delete the tag of a specific cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateClusterTags</td>
                    <td>Add tags to a specified cluster in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">TagManagement</td>
                    <td>SwitchClusterTags</td>
                    <td>Enable or disable the default cluster label for an existing cluster. After this function is enabled, nodes in the cluster are labeled with the default cluster labels.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTagStatus</td>
                    <td>Query the default label status of a cluster</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">VersionMetaQuery</td>
                    <td>ShowMrsVersionList</td>
                    <td>Displays the MRS version list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMrsFlavors</td>
                    <td>Query the available specifications of the MRS cluster version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMrsVersionMetadata</td>
                    <td>Query the metadata of the corresponding version. If the cluster ID is specified in the parameter, the latest metadata of the cluster after the patch is updated can be queried.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
