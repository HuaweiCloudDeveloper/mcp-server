# CDM MCP Server 


## Version
v0.1.0

## Overview

CDM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CDM. Full-chain management of CDM resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Cluster management | StartCluster | Start the cluster. | To be tested |
|  | ShowDatastores | Query the versions supported by the CDM cluster. | To be tested |
|  | ShowFlavorDetail | Query the specifications with a specified specification ID. | To be tested |
|  | ModifyCluster | Modify the CDM cluster configuration. | To be tested |
|  | ShowClusterEnterpriseProjects | Query the enterprise project ID of a specified cluster. | To be tested |
|  | ShowEnterpriseProjects | Query the enterprise project IDs of all clusters in the current project. | To be tested |
|  | RestartCluster | This API is used to restart a cluster. | To be tested |
|  | ShowAvailabilityZones | Query all AZs of a CDM cluster. | To be tested |
|  | ShowFlavors | Query all compatible specifications by version ID. | To be tested |
|  | ShowInstanceDetail | Query cluster instance information. | To be tested |
| Cluster management interface | DeleteCluster | You can delete the cluster service after data processing and analysis are complete or the cluster is running abnormally and cannot provide services. This interface is compatible with Sahara. | To be tested |
|  | CreateCluster | Create an MRS cluster and submit a job in the cluster. This interface is not compatible with Sahara. | To be tested |
|  | ShowClusterDetail | This API is used to query and display the details of a single cluster. | To be tested |
|  | ListClusters | View the cluster list created by the user. This interface is not compatible with Sahara. | To be tested |
| Connection management | UpdateLink | Modify the connection interface. | To be tested |
|  | DeleteLink | Delete a connection interface. | To be tested |
|  | CreateLink | Create a connection interface. | To be tested |
|  | ShowLink | Query the connection interface. | To be tested |
| Instance Management | UpdateJob | This API is used to update details about a task with a specified ID of a tenant. | To be tested |
|  | CreateJob | You can create a single task, such as live migration, real-time synchronization, and real-time DR based on the request parameters. | To be tested |
| Job management | ShowJobStatus | Query the execution status of a job. | To be tested |
|  | ShowSubmissions | This API is used to query job execution history. | To be tested |
|  | CreateAndStartRandomClusterJob | This API is used to create and execute a job in a random cluster. | To be tested |
| Job management interface | StopJob | This API is used to terminate a specified job in the MRS cluster. | To be tested |
| Job-related API | StartJob |  | To be tested |
| Job-related interfaces | ShowJobs | Query job details | To be tested |
| Task Management | DeleteJob |  | To be tested |

