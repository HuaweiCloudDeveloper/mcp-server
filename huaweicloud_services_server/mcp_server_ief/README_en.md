# IEF MCP Server 


## Version
v0.1.0

## Overview

IEF MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IEF. Full-chain management of IEF resources can be carried out based on natural language.

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
                    <td rowspan="8">App Template Management</td>
                    <td>ListAppVersions</td>
                    <td>Query the application template version list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppDetail</td>
                    <td>Query details about an application template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppVersion</td>
                    <td>Delete an application version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApp</td>
                    <td>Delete an application template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppVersionDetail</td>
                    <td>Query the details about the application template version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppVersion</td>
                    <td>Update an application template version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApps</td>
                    <td>Query the application template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppVersions</td>
                    <td>Create an application template version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">AppManagement</td>
                    <td>CreateApp</td>
                    <td>This interface is used by users to create application information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApp</td>
                    <td>This interface is used by users to modify application information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Configuration Item Management</td>
                    <td>DeleteConfigMap</td>
                    <td>Delete a configuration item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConfigMap</td>
                    <td>Create a configuration item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfigMap</td>
                    <td>Update a configuration item</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigMaps</td>
                    <td>Query the configuration item list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigMap</td>
                    <td>Query the details of a configuration item.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Deployment Management</td>
                    <td>UpdateDeployment</td>
                    <td>Modifying Application Deployment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartDeploymentsPod</td>
                    <td>Restarting the deployed application instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDeployments</td>
                    <td>Query the deployment list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPods</td>
                    <td>Query the application instance list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeployments</td>
                    <td>Create a deployment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeployment</td>
                    <td>Delete an application deployment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeployment</td>
                    <td>Query the application deployment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Device Template Management</td>
                    <td>ShowDeviceTemplate</td>
                    <td>Query a terminal device template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceTemplateById</td>
                    <td>Updates a device template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeviceTemplate</td>
                    <td>Create a terminal device template.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDeviceTemplates</td>
                    <td>Query the terminal device template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceTemplate</td>
                    <td>Delete a device template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Device management</td>
                    <td>ShowDeviceTwin</td>
                    <td>This API is used to query device twins.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDevice</td>
                    <td>Create Device</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNodeByDeviceId</td>
                    <td>This API is used to update the edge node of a terminal. The function is the same as that of updating the terminal device on the edge node. You are advised to use the terminal device on the edge node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceTwin</td>
                    <td>This API is used to update device twins.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDevice</td>
                    <td>Modifying device information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevices</td>
                    <td>This interface is used to obtain the list of registered GB/T 28181 devices.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDevice</td>
                    <td>Query device details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDevice</td>
                    <td>This API is used to delete a specified device.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Edge node group management</td>
                    <td>DeleteEdgeGroupCert</td>
                    <td>Delete the certificate of the edge node group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeGroupDetail</td>
                    <td>Query details about an edge node group. This API can only be used in Platinum Edition instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeGroupCert</td>
                    <td>Create an edge node group certificate. The .tar.gz file of the edge node group certificate can be downloaded only when the API is invoked. Download the certificate file in time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeGroup</td>
                    <td>Create an edge node group. This API can only be used in Platinum Edition instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeGroupCertDetail</td>
                    <td>Query the certificate details of an edge node group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeGroup</td>
                    <td>Delete an edge node group. This API can only be used in Platinum Edition instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeGroupNodeBinding</td>
                    <td>Bind or unbind the edge node group to or from the edge node. This API can only be used in Platinum Edition instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeGroupCerts</td>
                    <td>Query the certificate list of the edge node group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeGroup</td>
                    <td>Updates the description of the edge node group. This API can only be used in Platinum Edition instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeGroups</td>
                    <td>Query the edge node group list. This API can only be used in Platinum Edition instances.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Edge node management</td>
                    <td>EnableDisableEdgeNodes</td>
                    <td>Enable or disable an edge node. A disabled edge node cannot connect to the cloud service. You can use the URI to enable the edge node to restore the connection.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeNodeDevice</td>
                    <td>Adding or deleting an edge POP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeNode</td>
                    <td>This API is used to register an edge node. After the API is invoked successfully, you can use Base64 to decode the node.package field in the response body to a tar.gz file, download the core software on the console, and manage the edge node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeNodeCerts</td>
                    <td>Query the application certificate and device certificate on the edge node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeNodeDetail</td>
                    <td>Query details about an edge node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeNodeCerts</td>
                    <td>Delete the certificate on the edge node. Currently, only the application certificate and device certificate can be deleted.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeNodes</td>
                    <td>This API is used to query edge nodes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeEdgeNode</td>
                    <td>This API is used to upgrade edge nodes. Edge nodes will be automatically upgraded to the latest available version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeNode</td>
                    <td>Delete an edge node</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeNodeCerts</td>
                    <td>Create the application certificate and device certificate on the edge node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeNode</td>
                    <td>This API is used to update edge nodes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Encrypted Data Management</td>
                    <td>CreateNodeEncryptdatas</td>
                    <td>Encrypted data is bound to an edge node.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEncryptdatas</td>
                    <td>Adding encrypted data</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEncryptdataNodes</td>
                    <td>Obtain the edge node bound to the encrypted data.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNodeEncryptdatas</td>
                    <td>Unbinding the encrypted data from the edge node</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEncryptdatas</td>
                    <td>Obtain the encrypted data list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodeEncryptdatas</td>
                    <td>Obtain the encrypted data bound to the edge node</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEncryptdatas</td>
                    <td>Query encrypted data details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEncryptdatas</td>
                    <td>Delete encrypted data</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEncryptdatas</td>
                    <td>Update encrypted data</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Endpoint management</td>
                    <td>DeleteEndPoint</td>
                    <td>Delete an endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEndPointDetail</td>
                    <td>Query the details about an endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">IAlgorithmController</td>
                    <td>ShowServiceDetail</td>
                    <td>Obtain service details</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Image Tag</td>
                    <td>ListTags</td>
                    <td>Query the image tag list based on different conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Key Management</td>
                    <td>DeleteSecret</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecret</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Key management</td>
                    <td>ListSecrets</td>
                    <td>Query the list of keys</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecret</td>
                    <td>Update a key</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Manage batch jobs</td>
                    <td>ListBatchJob</td>
                    <td>Query the batch processing job list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreBatchJob</td>
                    <td>Continue the batch processing job. This API takes effect only for stopped batch processing jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBatchJob</td>
                    <td>Query the details of a batch processing job</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBatchJob</td>
                    <td>Create a batch processing job. This API is used to create batch processing jobs. Currently, the following operations are supported: batch node upgrade, batch application deployment, and batch application upgrade.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopBatchJob</td>
                    <td>Stop batch processing jobs. This API takes effect only for running batch processing jobs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryBatchJob</td>
                    <td>Retry the batch processing job. This API takes effect only for batch processing jobs that fail to be executed.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBatchJob</td>
                    <td>Delete a batch processing job</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Manage nodes in batches</td>
                    <td>ShowProductDetail</td>
                    <td>Query the details about a batch node registration job. This interface cannot query the product certificate file.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Product Management</td>
                    <td>DeleteProduct</td>
                    <td>Delete a product</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProduct</td>
                    <td>Create a product</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProducts</td>
                    <td>Query products</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowQuota</td>
                    <td>Query the network resource quotas of a single tenant in the VPC service, including the VPC quota, subnet quota, security group quota, security group rule quota, EIP quota, and VPN quota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Resource Tag</td>
                    <td>DeleteResourceTag</td>
                    <td>This API is used to remove tags of multiple cloud service resources in batches. A maximum of 10 tags can be removed for each resource. A maximum of 20 tags can be removed at a time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Rule Management</td>
                    <td>StartRule</td>
                    <td>Enable a rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopRule</td>
                    <td>Disable a rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRuleErrors</td>
                    <td>Query the list of all errors in a specified rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRuleDetail</td>
                    <td>Obtains the details about a rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Rule engine</td>
                    <td>CreateRule</td>
                    <td>Create Rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRule</td>
                    <td>Delete a rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRules</td>
                    <td>Query Rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Service Management</td>
                    <td>UpdateService</td>
                    <td>Modifying a service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateService</td>
                    <td>Create a service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServices</td>
                    <td>Query service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteService</td>
                    <td>Delete a service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">System Subscription Management</td>
                    <td>CreateSystemEvent</td>
                    <td>Create a system subscription</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSystemEventDetail</td>
                    <td>Query the system subscription list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSystemEvent</td>
                    <td>Delete the system subscription list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSystemEvents</td>
                    <td>Query the system subscription list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopSystemEvent</td>
                    <td>Disable system subscription</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartSystemEvent</td>
                    <td>Enable system subscription</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Tag Management</td>
                    <td>BatchAddDeleteTags</td>
                    <td>This API is used to add or delete tags for specified instances in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceByTags</td>
                    <td>Filter instances by label</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagsByResourceType</td>
                    <td>Query all resource tags of an instance type in a specified project.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTag</td>
                    <td>Add a tag to a resource.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Temporary login command</td>
                    <td>CreateSecret</td>
                    <td>Invoke this interface to obtain the value of X-Swr-Dockerlogin in the response message header and the value of host in the response message body to generate a temporary login command.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">VPC Endpoint Function</td>
                    <td>CreateEndpoint</td>
                    <td>Create a VPC endpoint so that it can access the VPC endpoint service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpoints</td>
                    <td>Query the list of VPC endpoints of the current user.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
