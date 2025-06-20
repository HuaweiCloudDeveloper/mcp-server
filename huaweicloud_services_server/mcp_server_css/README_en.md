# CSS MCP Server 


## Version
v0.1.0

## Overview

CSS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CSS. Full-chain management of CSS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Cluster management | RestartCluster | This API is used to restart a cluster. | To be tested |
| Cluster management interface | UpdateShrinkNodes | This API is used to scale in a specified node in a cluster. A yearly/monthly cluster does not support scaling in a specified node using APIs. | To be tested |
|  | UpdateClusterName | Change the cluster name | To be tested |
|  | UpdateFlavor | This API is used to modify cluster specifications. Only the ESS node type can be changed. | To be tested |
|  | UpdateOndemandClusterToPeriod | This interface is used to change a pay-per-use cluster to a yearly/monthly cluster. | To be tested |
|  | AddIndependentNode | Because of the growth or uncertainty of services on the cluster data plane, it is difficult to understand the cluster scale at the beginning. This interface can be used to independently play the master and client roles in a cluster that does not have independent master and client roles. | To be tested |
|  | UpdateExtendInstanceStorage | This API is used to scale up the number and storage capacity of instances of different types in a cluster. This API is used to expand the capacity of a cluster that already has independent master, client, and cold data nodes. | To be tested |
|  | ListClustersDetails | This API is used to query and display the cluster list and cluster status. | To be tested |
|  | ShowClusterTag | This API is used to query the label information of a specified cluster. | To be tested |
|  | DownloadCert | This interface is used to download the security certificate. | To be tested |
|  | ShowClusterDetail | This API is used to query and display the details of a single cluster. | To be tested |
|  | UpdateFlavorByType | Modify the cluster specifications.  | To be tested |
|  | DeleteClustersTags | This API is used to delete a cluster tag. | To be tested |
|  | RetryUpgradeTask | The upgrade process takes a long time and may fail due to network problems. You can use this interface to retry the task or terminate the task. | To be tested |
|  | UpdateShrinkCluster | This API is used to scale in the number and storage capacity of different types of instances in a cluster. In a yearly/monthly cluster, the capacity of a specified node type cannot be reduced using APIs. | To be tested |
|  | RollingRestart | This interface restarts nodes one by one, which takes a long time when there are a large number of indexes. | To be tested |
|  | UpgradeDetail | This API is used to display the phase information about the node to be upgraded (switched AZ) because the upgrade process takes a long time. | To be tested |
|  | UpdateBatchClustersTags | This API is used to add or delete tags in a cluster in batches. | To be tested |
|  | ListClustersTags | This API is used to query all tag sets in a specified region. | To be tested |
|  | UpdateAzByInstanceType | This API is invoked to switch the AZ by specifying the node type. | To be tested |
|  | UpgradeCore | This interface is used to upgrade the ES of an earlier version to a later version or the same version. | To be tested |
|  | CreateCluster | Create an MRS cluster and submit a job in the cluster. This interface is not compatible with Sahara. | To be tested |
|  | ChangeMode | This interface is used to switch the security mode of a cluster. | To be tested |
|  | UpdateExtendCluster | This API is used to scale up instances in a cluster (only elasticsearch instances can be scaled up). Only common nodes can be added, and the cluster instance to be expanded does not contain special nodes (Master, Client, or cold data nodes). | To be tested |
|  | DeleteCluster | You can delete the cluster service after data processing and analysis are complete or the cluster is running abnormally and cannot provide services. This interface is compatible with Sahara. | To be tested |
|  | CreateClustersTags | This API is used to add tags to a specified cluster. | To be tested |
| Connection management | ChangeSecurityGroup | Modify the security group bound to the SFS Turbo file system. If the security group modification task is an asynchronous task, you can determine whether to modify the security group status based on the sub_status field returned by Querying a Single File System. If the sub_status field is 232, the security group is successfully modified. | To be tested |
|  | ListElbs | Query the list of ELBs that can be associated with a cluster. | To be tested |
| EVS Snapshot | CreateSnapshot | Create an EVS snapshot. | To be tested |
|  | DeleteSnapshot | Delete an EVS snapshot. | To be tested |
|  | ListSnapshots | Query the details about EVS snapshots. | To be tested |
| Engine version and specification | ListFlavors | Query database specifications. | To be tested |
| Instance Management | ResetPassword | Reset the password (only for instances with SSL enabled). | To be tested |
| Intelligent O&M | DeleteAiOps | This interface is used to delete a detection task record. | To be tested |
|  | ListSmnTopics | This API is used to obtain the available SMN topics of intelligent O&M alarms. | To be tested |
|  | CreateAiOps | This API is used to create a cluster detection task. | To be tested |
|  | ListAiOps | This interface is used to obtain the list and details of intelligent O&M tasks. | To be tested |
| Internet access interface | StopPublicWhitelist | This interface is used to disable the public network access control trustlist. | To be tested |
|  | CreateBindPublic | This interface is used to enable public network access. | To be tested |
|  | UpdateUnbindPublic | This interface is used to disable public network access. Do not disable public network access for yearly/monthly clusters through APIs. | To be tested |
|  | UpdatePublicBandWidth | This interface is used to modify the bandwidth for accessing the public network. | To be tested |
|  | StartPublicWhitelist | This interface is used to enable the public network access control trustlist. | To be tested |
| Kibana public network access interface | StartKibanaPublic | This API is used to enable Kibana public network access. | To be tested |
|  | StopPublicKibanaWhitelist | This interface is used to disable Kibana public network access control. | To be tested |
|  | UpdateCloseKibana | This interface is used to disable Kibana public network access. You cannot disable Kibana public network access for yearly/monthly clusters using APIs. | To be tested |
|  | UpdateAlterKibana | This API is used to modify the public network bandwidth of Kibana. | To be tested |
|  | UpdatePublicKibanaWhitelist | This interface modifies the Kibana trustlist to modify the Kibana access permission. | To be tested |
| Lifecycle Management | UpdateInstance | Modifies the name and description of an instance. | To be tested |
| Load balancing | ListElbCerts | This interface is used to query the certificate list. | To be tested |
|  | CreateElbListener | This interface is used to configure the ES listener. | To be tested |
|  | EnableOrDisableElb | This interface enables or disables the ES load balancer. | To be tested |
|  | UpdateEsListener | This interface is used to update the ES listener. | To be tested |
|  | ShowElbDetail | This interface is used to obtain the information about the eELB and the health check status to be displayed on the page. | To be tested |
| Log management interface | StopLogAutoBackupPolicy | This interface is used to disable the automatic log backup policy. | To be tested |
|  | StopLogs | This interface is used to disable the log function. | To be tested |
|  | StartLogAutoBackupPolicy | This interface is used to enable the automatic log backup policy. | To be tested |
|  | StartTargetClusterConnectivityTest | This interface is used for connectivity tests. | To be tested |
|  | ListLogsJob | This API is used to query the log task list of a specific cluster. | To be tested |
|  | UpdateLogSetting | This interface is used to modify basic log configuration. | To be tested |
|  | ShowLogBackup | This interface is used to query logs. | To be tested |
|  | CreateLogBackup | This interface is used to back up logs. | To be tested |
|  | StartLogs | This interface is used to enable the log function. | To be tested |
|  | ShowGetLogSetting | This interface is used to query basic log configurations. | To be tested |
| Logstash interface | ShowCertsDetail | This interface is used to query certificate file information. | To be tested |
|  | ListConfs | This interface is used to query the configuration file list. | To be tested |
|  | StartHotPipeline | This API is used to migrate data from the hot start pipeline. | To be tested |
|  | ListActions | This interface is used to query operation records. | To be tested |
|  | UploadCerts | This interface is used to upload certificate files. | To be tested |
|  | ShowGetConfDetail | This interface is used to query the content of a configuration file. | To be tested |
|  | StartConnectivityTest | This interface is used for connectivity tests. | To be tested |
|  | CreateCnf | This interface is used to create a configuration file. | To be tested |
|  | StartPipeline | This interface is used to start the pipeline data migration. | To be tested |
|  | StopPipeline | This interface is used to stop pipeline data migration. | To be tested |
|  | DeleteConf | Delete the configuration file. | To be tested |
|  | RebootCluster | The cluster is unavailable during the restart. Exercise caution when performing this operation. If a cluster is in the working state, the Logstash process will be stopped during the restart. If the value of Remaining in the pipeline list is No, the status of all running pipelines will be set to Stopped. If the value of Retain Resident is Yes, the Logstash process recovery mechanism is triggered and the status of the working pipe is set to Recovering. If the Logstash process is restarted within 10 minutes, the status of the pipe is restored to Running. Otherwise, the status of the pipe is set to Failed. | To be tested |
|  | StopHotPipeline | This API is used to hot stop pipeline data migration. | To be tested |
|  | UpdateRoute | This interface is used to update cluster routes. | To be tested |
|  | ListCerts | This interface is used to query the certificate list. | To be tested |
|  | GetRoutes | This interface is used to obtain cluster routes. | To be tested |
|  | AddFavorite | This interface is used to add a template to a user-defined template. | To be tested |
|  | ListPipelines | This API is used to query the pipeline list. | To be tested |
|  | DeleteCerts | This interface is used to delete a certificate file. | To be tested |
|  | UpdateCnf | This interface is used to update the configuration file. | To be tested |
| Mirror | ListImages | Query the image list based on different conditions. | To be tested |
| Parameter Configuration Interface | ListYmlsJob | This interface is used to obtain the task operation list of parameter settings. | To be tested |
|  | ListYmls | This interface is used to obtain the parameter configuration list of the current cluster. | To be tested |
|  | UpdateYmls | This interface is used to modify parameter settings. | To be tested |
| Project Information | ListTemplates | Query project template | To be tested |
| Snapshot management interface | CreateAutoCreatePolicy | This API is used to set the automatic snapshot creation. By default, a snapshot is created every day. | To be tested |
|  | ShowAutoCreatePolicy | This API is used to query the automatic snapshot creation policy. | To be tested |
|  | RestoreSnapshot | This API is used to manually restore a snapshot. | To be tested |
|  | StartAutoCreateSnapshots | This interface is used to enable the automatic backup function. | To be tested |
|  | UpdateSnapshotSetting | This API is used to modify the basic configuration of a cluster snapshot, including an OBS bucket and an IAM agency. | To be tested |
|  | StartAutoSetting | This API is used to automatically configure basic cluster snapshot configurations, including OBS buckets and IAM agencies. | To be tested |
|  | StopAutoCreateSnapshots | This interface is used to disable the automatic backup function. | To be tested |
|  | StopSnapshot | This API is used to disable the snapshot function. | To be tested |
| TemplateManagement | DeleteTemplate | This API is used to delete a created template. | To be tested |
| Thesaurus management interface | ShowIkThesaurus | This interface is used to query the loading status of a customized word dictionary. | To be tested |
|  | CreateLoadIkThesaurus | This API is used to load the user-defined word dictionary stored on OBS. | To be tested |
|  | DeleteIkThesaurus | This interface is used to delete a user-defined word dictionary. | To be tested |
| VPC Endpoint Interface | ShowVpcepConnection | This interface is used to obtain VPC endpoint connections. | To be tested |
|  | StopVpecp | This API is used to stop the VPC endpoint service. | To be tested |
|  | UpdateVpcepConnection | This interface is used to update a VPC endpoint connection. | To be tested |
|  | StartVpecp | This API is used to enable the VPC endpoint service. | To be tested |
|  | UpdateVpcepWhitelist | This API is used to modify the VPC endpoint service trustlist. | To be tested |

