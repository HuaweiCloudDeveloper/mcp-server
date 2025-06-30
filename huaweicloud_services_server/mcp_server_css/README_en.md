# CSS MCP Server 


## Version
v0.1.0

## Overview

CSS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CSS. Full-chain management of CSS resources can be carried out based on natural language.

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
                    <td rowspan="1">Cluster management</td>
                    <td>RestartCluster</td>
                    <td>This API is used to restart a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="25">Cluster management interface</td>
                    <td>UpdateShrinkNodes</td>
                    <td>This API is used to scale in a specified node in a cluster. A yearly/monthly cluster does not support scaling in a specified node using APIs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClusterName</td>
                    <td>Change the cluster name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlavor</td>
                    <td>This API is used to modify cluster specifications. Only the ESS node type can be changed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOndemandClusterToPeriod</td>
                    <td>This interface is used to change a pay-per-use cluster to a yearly/monthly cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddIndependentNode</td>
                    <td>Because of the growth or uncertainty of services on the cluster data plane, it is difficult to understand the cluster scale at the beginning. This interface can be used to independently play the master and client roles in a cluster that does not have independent master and client roles.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateExtendInstanceStorage</td>
                    <td>This API is used to scale up the number and storage capacity of instances of different types in a cluster. This API is used to expand the capacity of a cluster that already has independent master, client, and cold data nodes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClustersDetails</td>
                    <td>This API is used to query and display the cluster list and cluster status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterTag</td>
                    <td>This API is used to query the label information of a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadCert</td>
                    <td>This interface is used to download the security certificate.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterDetail</td>
                    <td>This API is used to query and display the details of a single cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFlavorByType</td>
                    <td>Modify the cluster specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClustersTags</td>
                    <td>This API is used to delete a cluster tag.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryUpgradeTask</td>
                    <td>The upgrade process takes a long time and may fail due to network problems. You can use this interface to retry the task or terminate the task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateShrinkCluster</td>
                    <td>This API is used to scale in the number and storage capacity of different types of instances in a cluster. In a yearly/monthly cluster, the capacity of a specified node type cannot be reduced using APIs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollingRestart</td>
                    <td>This interface restarts nodes one by one, which takes a long time when there are a large number of indexes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeDetail</td>
                    <td>This API is used to display the phase information about the node to be upgraded (switched AZ) because the upgrade process takes a long time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBatchClustersTags</td>
                    <td>This API is used to add or delete tags in a cluster in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClustersTags</td>
                    <td>This API is used to query all tag sets in a specified region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAzByInstanceType</td>
                    <td>This API is invoked to switch the AZ by specifying the node type.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeCore</td>
                    <td>This interface is used to upgrade the ES of an earlier version to a later version or the same version.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCluster</td>
                    <td>Create an MRS cluster and submit a job in the cluster. This interface is not compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeMode</td>
                    <td>This interface is used to switch the security mode of a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateExtendCluster</td>
                    <td>This API is used to scale up instances in a cluster (only elasticsearch instances can be scaled up). Only common nodes can be added, and the cluster instance to be expanded does not contain special nodes (Master, Client, or cold data nodes).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCluster</td>
                    <td>You can delete the cluster service after data processing and analysis are complete or the cluster is running abnormally and cannot provide services. This interface is compatible with Sahara.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClustersTags</td>
                    <td>This API is used to add tags to a specified cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Connection management</td>
                    <td>ChangeSecurityGroup</td>
                    <td>Modify the security group bound to the SFS Turbo file system. If the security group modification task is an asynchronous task, you can determine whether to modify the security group status based on the sub_status field returned by Querying a Single File System. If the sub_status field is 232, the security group is successfully modified.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListElbs</td>
                    <td>Query the list of ELBs that can be associated with a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">EVS Snapshot</td>
                    <td>CreateSnapshot</td>
                    <td>Create an EVS snapshot.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSnapshot</td>
                    <td>Delete an EVS snapshot.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshots</td>
                    <td>Query the details about EVS snapshots.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Engine version and specification</td>
                    <td>ListFlavors</td>
                    <td>Query database specifications.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Instance Management</td>
                    <td>ResetPassword</td>
                    <td>Reset the password (only for instances with SSL enabled).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Intelligent O&amp;M</td>
                    <td>DeleteAiOps</td>
                    <td>This interface is used to delete a detection task record.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSmnTopics</td>
                    <td>This API is used to obtain the available SMN topics of intelligent O&amp;M alarms.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAiOps</td>
                    <td>This API is used to create a cluster detection task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAiOps</td>
                    <td>This interface is used to obtain the list and details of intelligent O&amp;M tasks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Internet access interface</td>
                    <td>StopPublicWhitelist</td>
                    <td>This interface is used to disable the public network access control trustlist.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBindPublic</td>
                    <td>This interface is used to enable public network access.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUnbindPublic</td>
                    <td>This interface is used to disable public network access. Do not disable public network access for yearly/monthly clusters through APIs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublicBandWidth</td>
                    <td>This interface is used to modify the bandwidth for accessing the public network.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartPublicWhitelist</td>
                    <td>This interface is used to enable the public network access control trustlist.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Kibana public network access interface</td>
                    <td>StartKibanaPublic</td>
                    <td>This API is used to enable Kibana public network access.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopPublicKibanaWhitelist</td>
                    <td>This interface is used to disable Kibana public network access control.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCloseKibana</td>
                    <td>This interface is used to disable Kibana public network access. You cannot disable Kibana public network access for yearly/monthly clusters using APIs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlterKibana</td>
                    <td>This API is used to modify the public network bandwidth of Kibana.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublicKibanaWhitelist</td>
                    <td>This interface modifies the Kibana trustlist to modify the Kibana access permission.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Lifecycle Management</td>
                    <td>UpdateInstance</td>
                    <td>Modifies the name and description of an instance.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Load balancing</td>
                    <td>ListElbCerts</td>
                    <td>This interface is used to query the certificate list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateElbListener</td>
                    <td>This interface is used to configure the ES listener.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableOrDisableElb</td>
                    <td>This interface enables or disables the ES load balancer.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEsListener</td>
                    <td>This interface is used to update the ES listener.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowElbDetail</td>
                    <td>This interface is used to obtain the information about the eELB and the health check status to be displayed on the page.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Log management interface</td>
                    <td>StopLogAutoBackupPolicy</td>
                    <td>This interface is used to disable the automatic log backup policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopLogs</td>
                    <td>This interface is used to disable the log function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartLogAutoBackupPolicy</td>
                    <td>This interface is used to enable the automatic log backup policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartTargetClusterConnectivityTest</td>
                    <td>This interface is used for connectivity tests.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogsJob</td>
                    <td>This API is used to query the log task list of a specific cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogSetting</td>
                    <td>This interface is used to modify basic log configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLogBackup</td>
                    <td>This interface is used to query logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogBackup</td>
                    <td>This interface is used to back up logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartLogs</td>
                    <td>This interface is used to enable the log function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGetLogSetting</td>
                    <td>This interface is used to query basic log configurations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="20">Logstash interface</td>
                    <td>ShowCertsDetail</td>
                    <td>This interface is used to query certificate file information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfs</td>
                    <td>This interface is used to query the configuration file list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartHotPipeline</td>
                    <td>This API is used to migrate data from the hot start pipeline.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListActions</td>
                    <td>This interface is used to query operation records.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadCerts</td>
                    <td>This interface is used to upload certificate files.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGetConfDetail</td>
                    <td>This interface is used to query the content of a configuration file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartConnectivityTest</td>
                    <td>This interface is used for connectivity tests.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCnf</td>
                    <td>This interface is used to create a configuration file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartPipeline</td>
                    <td>This interface is used to start the pipeline data migration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopPipeline</td>
                    <td>This interface is used to stop pipeline data migration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConf</td>
                    <td>Delete the configuration file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebootCluster</td>
                    <td>The cluster is unavailable during the restart. Exercise caution when performing this operation. If a cluster is in the working state, the Logstash process will be stopped during the restart. If the value of Remaining in the pipeline list is No, the status of all running pipelines will be set to Stopped. If the value of Retain Resident is Yes, the Logstash process recovery mechanism is triggered and the status of the working pipe is set to Recovering. If the Logstash process is restarted within 10 minutes, the status of the pipe is restored to Running. Otherwise, the status of the pipe is set to Failed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopHotPipeline</td>
                    <td>This API is used to hot stop pipeline data migration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRoute</td>
                    <td>This interface is used to update cluster routes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCerts</td>
                    <td>This interface is used to query the certificate list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetRoutes</td>
                    <td>This interface is used to obtain cluster routes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddFavorite</td>
                    <td>This interface is used to add a template to a user-defined template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPipelines</td>
                    <td>This API is used to query the pipeline list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCerts</td>
                    <td>This interface is used to delete a certificate file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCnf</td>
                    <td>This interface is used to update the configuration file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Mirror</td>
                    <td>ListImages</td>
                    <td>Query the image list based on different conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Parameter Configuration Interface</td>
                    <td>ListYmlsJob</td>
                    <td>This interface is used to obtain the task operation list of parameter settings.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListYmls</td>
                    <td>This interface is used to obtain the parameter configuration list of the current cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateYmls</td>
                    <td>This interface is used to modify parameter settings.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Project Information</td>
                    <td>ListTemplates</td>
                    <td>Query project template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Snapshot management interface</td>
                    <td>CreateAutoCreatePolicy</td>
                    <td>This API is used to set the automatic snapshot creation. By default, a snapshot is created every day.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoCreatePolicy</td>
                    <td>This API is used to query the automatic snapshot creation policy.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreSnapshot</td>
                    <td>This API is used to manually restore a snapshot.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartAutoCreateSnapshots</td>
                    <td>This interface is used to enable the automatic backup function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSnapshotSetting</td>
                    <td>This API is used to modify the basic configuration of a cluster snapshot, including an OBS bucket and an IAM agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartAutoSetting</td>
                    <td>This API is used to automatically configure basic cluster snapshot configurations, including OBS buckets and IAM agencies.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopAutoCreateSnapshots</td>
                    <td>This interface is used to disable the automatic backup function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopSnapshot</td>
                    <td>This API is used to disable the snapshot function.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TemplateManagement</td>
                    <td>DeleteTemplate</td>
                    <td>This API is used to delete a created template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Thesaurus management interface</td>
                    <td>ShowIkThesaurus</td>
                    <td>This interface is used to query the loading status of a customized word dictionary.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLoadIkThesaurus</td>
                    <td>This API is used to load the user-defined word dictionary stored on OBS.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIkThesaurus</td>
                    <td>This interface is used to delete a user-defined word dictionary.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">VPC Endpoint Interface</td>
                    <td>ShowVpcepConnection</td>
                    <td>This interface is used to obtain VPC endpoint connections.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopVpecp</td>
                    <td>This API is used to stop the VPC endpoint service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpcepConnection</td>
                    <td>This interface is used to update a VPC endpoint connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartVpecp</td>
                    <td>This API is used to enable the VPC endpoint service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVpcepWhitelist</td>
                    <td>This API is used to modify the VPC endpoint service trustlist.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
