# CDM MCP Server 


## Version
v0.1.0

## Overview

CDM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CDM. Full-chain management of CDM resources can be carried out based on natural language.

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
                    <td rowspan="10">Cluster management</td>
                    <td>StartCluster</td>
                    <td>Start the cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatastores</td>
                    <td>Query the versions supported by the CDM cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlavorDetail</td>
                    <td>Query the specifications with a specified specification ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyCluster</td>
                    <td>Modify the CDM cluster configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterEnterpriseProjects</td>
                    <td>Query the enterprise project ID of a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnterpriseProjects</td>
                    <td>Query the enterprise project IDs of all clusters in the current project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartCluster</td>
                    <td>This API is used to restart a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAvailabilityZones</td>
                    <td>Query all AZs of a CDM cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlavors</td>
                    <td>Query all compatible specifications by version ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceDetail</td>
                    <td>Query cluster instance information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Cluster management interface</td>
                    <td>DeleteCluster</td>
                    <td>You can delete the cluster service after data processing and analysis are complete or the cluster is running abnormally and cannot provide services. This interface is compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCluster</td>
                    <td>Create an MRS cluster and submit a job in the cluster. This interface is not compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterDetail</td>
                    <td>This API is used to query and display the details of a single cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusters</td>
                    <td>View the cluster list created by the user. This interface is not compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Connection management</td>
                    <td>UpdateLink</td>
                    <td>Modify the connection interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLink</td>
                    <td>Delete a connection interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLink</td>
                    <td>Create a connection interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLink</td>
                    <td>Query the connection interface.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Instance Management</td>
                    <td>UpdateJob</td>
                    <td>This API is used to update details about a task with a specified ID of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateJob</td>
                    <td>You can create a single task, such as live migration, real-time synchronization, and real-time DR based on the request parameters.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Job management</td>
                    <td>ShowJobStatus</td>
                    <td>Query the execution status of a job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubmissions</td>
                    <td>This API is used to query job execution history.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAndStartRandomClusterJob</td>
                    <td>This API is used to create and execute a job in a random cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job management interface</td>
                    <td>StopJob</td>
                    <td>This API is used to terminate a specified job in the MRS cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job-related API</td>
                    <td>StartJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job-related interfaces</td>
                    <td>ShowJobs</td>
                    <td>Query job details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Task Management</td>
                    <td>DeleteJob</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
