# IEF MCP Server 


## Version
v0.1.0

## Overview

IEF MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IEF. Full-chain management of IEF resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| App Template Management | ListAppVersions | Query the application template version list | To be tested |
|  | ShowAppDetail | Query details about an application template. | To be tested |
|  | DeleteAppVersion | Delete an application version | To be tested |
|  | DeleteApp | Delete an application template | To be tested |
|  | ShowAppVersionDetail | Query the details about the application template version | To be tested |
|  | UpdateAppVersion | Update an application template version | To be tested |
|  | ListApps | Query the application template list | To be tested |
|  | CreateAppVersions | Create an application template version | To be tested |
| AppManagement | CreateApp | This interface is used by users to create application information. | To be tested |
|  | UpdateApp | This interface is used by users to modify application information. | To be tested |
| Configuration Item Management | DeleteConfigMap | Delete a configuration item | To be tested |
|  | CreateConfigMap | Create a configuration item | To be tested |
|  | UpdateConfigMap | Update a configuration item | To be tested |
|  | ListConfigMaps | Query the configuration item list | To be tested |
|  | ShowConfigMap | Query the details of a configuration item. | To be tested |
| Deployment Management | UpdateDeployment | Modifying Application Deployment | To be tested |
|  | RestartDeploymentsPod | Restarting the deployed application instance | To be tested |
|  | ListDeployments | Query the deployment list | To be tested |
|  | ListPods | Query the application instance list | To be tested |
|  | CreateDeployments | Create a deployment | To be tested |
|  | DeleteDeployment | Delete an application deployment | To be tested |
|  | ShowDeployment | Query the application deployment | To be tested |
| Device Template Management | ShowDeviceTemplate | Query a terminal device template | To be tested |
|  | UpdateDeviceTemplateById | Updates a device template. | To be tested |
|  | CreateDeviceTemplate | Create a terminal device template. | To be tested |
|  | ListDeviceTemplates | Query the terminal device template list | To be tested |
|  | DeleteDeviceTemplate | Delete a device template | To be tested |
| Device management | ShowDeviceTwin | This API is used to query device twins. | To be tested |
|  | CreateDevice | Create Device | To be tested |
|  | UpdateNodeByDeviceId | This API is used to update the edge node of a terminal. The function is the same as that of updating the terminal device on the edge node. You are advised to use the terminal device on the edge node. | To be tested |
|  | UpdateDeviceTwin | This API is used to update device twins. | To be tested |
|  | UpdateDevice | Modifying device information | To be tested |
|  | ListDevices | This interface is used to obtain the list of registered GB/T 28181 devices. | To be tested |
|  | ShowDevice | Query device details | To be tested |
|  | DeleteDevice | This API is used to delete a specified device. | To be tested |
| Edge node group management | DeleteEdgeGroupCert | Delete the certificate of the edge node group | To be tested |
|  | ShowEdgeGroupDetail | Query details about an edge node group. This API can only be used in Platinum Edition instances. | To be tested |
|  | CreateEdgeGroupCert | Create an edge node group certificate. The .tar.gz file of the edge node group certificate can be downloaded only when the API is invoked. Download the certificate file in time. | To be tested |
|  | CreateEdgeGroup | Create an edge node group. This API can only be used in Platinum Edition instances. | To be tested |
|  | ShowEdgeGroupCertDetail | Query the certificate details of an edge node group | To be tested |
|  | DeleteEdgeGroup | Delete an edge node group. This API can only be used in Platinum Edition instances. | To be tested |
|  | UpdateEdgeGroupNodeBinding | Bind or unbind the edge node group to or from the edge node. This API can only be used in Platinum Edition instances. | To be tested |
|  | ListEdgeGroupCerts | Query the certificate list of the edge node group | To be tested |
|  | UpdateEdgeGroup | Updates the description of the edge node group. This API can only be used in Platinum Edition instances. | To be tested |
|  | ListEdgeGroups | Query the edge node group list. This API can only be used in Platinum Edition instances. | To be tested |
| Edge node management | EnableDisableEdgeNodes | Enable or disable an edge node. A disabled edge node cannot connect to the cloud service. You can use the URI to enable the edge node to restore the connection. | To be tested |
|  | UpdateEdgeNodeDevice | Adding or deleting an edge POP | To be tested |
|  | CreateEdgeNode | This API is used to register an edge node. After the API is invoked successfully, you can use Base64 to decode the node.package field in the response body to a tar.gz file, download the core software on the console, and manage the edge node. | To be tested |
|  | ListEdgeNodeCerts | Query the application certificate and device certificate on the edge node. | To be tested |
|  | ShowEdgeNodeDetail | Query details about an edge node. | To be tested |
|  | DeleteEdgeNodeCerts | Delete the certificate on the edge node. Currently, only the application certificate and device certificate can be deleted. | To be tested |
|  | ListEdgeNodes | This API is used to query edge nodes. | To be tested |
|  | UpgradeEdgeNode | This API is used to upgrade edge nodes. Edge nodes will be automatically upgraded to the latest available version | To be tested |
|  | DeleteEdgeNode | Delete an edge node | To be tested |
|  | CreateEdgeNodeCerts | Create the application certificate and device certificate on the edge node. | To be tested |
|  | UpdateEdgeNode | This API is used to update edge nodes. | To be tested |
| Encrypted Data Management | CreateNodeEncryptdatas | Encrypted data is bound to an edge node. | To be tested |
|  | CreateEncryptdatas | Adding encrypted data | To be tested |
|  | ListEncryptdataNodes | Obtain the edge node bound to the encrypted data. | To be tested |
|  | DeleteNodeEncryptdatas | Unbinding the encrypted data from the edge node | To be tested |
|  | ListEncryptdatas | Obtain the encrypted data list. | To be tested |
|  | ListNodeEncryptdatas | Obtain the encrypted data bound to the edge node | To be tested |
|  | ShowEncryptdatas | Query encrypted data details | To be tested |
|  | DeleteEncryptdatas | Delete encrypted data | To be tested |
|  | UpdateEncryptdatas | Update encrypted data | To be tested |
| Endpoint management | DeleteEndPoint | Delete an endpoint. | To be tested |
|  | ShowEndPointDetail | Query the details about an endpoint. | To be tested |
| IAlgorithmController | ShowServiceDetail | Obtain service details | To be tested |
| Image Tag | ListTags | Query the image tag list based on different conditions. | To be tested |
| Key Management | DeleteSecret |  | To be tested |
|  | ShowSecret |  | To be tested |
| Key management | ListSecrets | Query the list of keys | To be tested |
|  | UpdateSecret | Update a key | To be tested |
| Manage batch jobs | ListBatchJob | Query the batch processing job list | To be tested |
|  | RestoreBatchJob | Continue the batch processing job. This API takes effect only for stopped batch processing jobs. | To be tested |
|  | ShowBatchJob | Query the details of a batch processing job | To be tested |
|  | CreateBatchJob | Create a batch processing job. This API is used to create batch processing jobs. Currently, the following operations are supported: batch node upgrade, batch application deployment, and batch application upgrade. | To be tested |
|  | StopBatchJob | Stop batch processing jobs. This API takes effect only for running batch processing jobs. | To be tested |
|  | RetryBatchJob | Retry the batch processing job. This API takes effect only for batch processing jobs that fail to be executed. | To be tested |
|  | DeleteBatchJob | Delete a batch processing job | To be tested |
| Manage nodes in batches | ShowProductDetail | Query the details about a batch node registration job. This interface cannot query the product certificate file. | To be tested |
| Product Management | DeleteProduct | Delete a product | To be tested |
|  | CreateProduct | Create a product | To be tested |
|  | ListProducts | Query products | To be tested |
| Quota | ShowQuota | Query the network resource quotas of a single tenant in the VPC service, including the VPC quota, subnet quota, security group quota, security group rule quota, EIP quota, and VPN quota. | To be tested |
| Resource Tag | DeleteResourceTag | This API is used to remove tags of multiple cloud service resources in batches. A maximum of 10 tags can be removed for each resource. A maximum of 20 tags can be removed at a time. | To be tested |
| Rule Management | StartRule | Enable a rule | To be tested |
|  | StopRule | Disable a rule. | To be tested |
|  | ListRuleErrors | Query the list of all errors in a specified rule | To be tested |
|  | ShowRuleDetail | Obtains the details about a rule. | To be tested |
| Rule engine | CreateRule | Create Rule | To be tested |
|  | DeleteRule | Delete a rule | To be tested |
|  | ListRules | Query Rule | To be tested |
| Service Management | UpdateService | Modifying a service | To be tested |
|  | CreateService | Create a service | To be tested |
|  | ListServices | Query service | To be tested |
|  | DeleteService | Delete a service | To be tested |
| System Subscription Management | CreateSystemEvent | Create a system subscription | To be tested |
|  | ShowSystemEventDetail | Query the system subscription list | To be tested |
|  | DeleteSystemEvent | Delete the system subscription list | To be tested |
|  | ListSystemEvents | Query the system subscription list | To be tested |
|  | StopSystemEvent | Disable system subscription | To be tested |
|  | StartSystemEvent | Enable system subscription | To be tested |
| Tag Management | BatchAddDeleteTags | This API is used to add or delete tags for specified instances in batches. | To be tested |
|  | ListResourceByTags | Filter instances by label | To be tested |
|  | ListTagsByResourceType | Query all resource tags of an instance type in a specified project. | To be tested |
|  | CreateTag | Add a tag to a resource. | To be tested |
| Temporary login command | CreateSecret | Invoke this interface to obtain the value of X-Swr-Dockerlogin in the response message header and the value of host in the response message body to generate a temporary login command. | To be tested |
| VPC Endpoint Function | CreateEndpoint | Create a VPC endpoint so that it can access the VPC endpoint service. | To be tested |
|  | ListEndpoints | Query the list of VPC endpoints of the current user. | To be tested |

