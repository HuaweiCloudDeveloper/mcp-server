# CAE MCP Server 


## Version
v0.1.0

## Overview

CAE MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CAE. Full-chain management of CAE resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Application | ShowApplication | Obtain application details. | To be tested |
| Application operation | ListApplications | Query the application platform list. | To be tested |
|  | DeleteApplication | Delete a platform application. | To be tested |
|  | CreateApplication | Create a platform application. | To be tested |
| Certificate Management | UpdateCertificate | Modifying a Certificate | To be tested |
|  | ListCertificates | Query the certificate list | To be tested |
|  | DeleteCertificate | Delete a certificate | To be tested |
|  | CreateCertificate | Create Certificate | To be tested |
| Component | ListComponentInstances | Obtains the component instance list. | To be tested |
|  | CreateComponent | Create a component. | To be tested |
|  | DeleteComponent | Delete a component. | To be tested |
|  | ListComponents | Obtain the component list. | To be tested |
|  | CreateComponentWithConfiguration | Create, configure, and deploy the component. | To be tested |
|  | ExecuteAction | Perform specified operations on the component, such as deploying, upgrading, restarting, stopping, starting, scaling, configuring, and rolling back the component. | To be tested |
|  | ShowComponent | Obtains component details. | To be tested |
|  | UpdateComponent | Update the component. | To be tested |
|  | ListComponentSnapshots | Obtains the component snapshot list. | To be tested |
| ComponentConfiguration | CreateComponentConfiguration | Create the component configuration. | To be tested |
|  | DeleteComponentConfiguration | Delete the component configuration. | To be tested |
|  | ListComponentConfigurations | Obtain the component configuration list. | To be tested |
| Domain | DeleteDomain | Delete a domain name. | To be tested |
|  | CreateDomain | Create a domain name. | To be tested |
| EIP Management | ListEips | Querying the EIP list | To be tested |
| EVS disk | ListVolumes | Query details about all EVS disks. | To be tested |
|  | DeleteVolume | Delete an EVS disk. | To be tested |
|  | CreateVolume | Create a pay-per-use or yearly/monthly EVS disk. | To be tested |
| Eip | UpdateEip | Modify the inbound and outbound bandwidth and enable/disable status. | To be tested |
| Entrusted management | CreateAgency | This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create an agency. | To be tested |
|  | ListAgencies | This interface is used by the (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the agency list based on the specified conditions. | To be tested |
| Job | RetryJob | Retry the task. | To be tested |
| Key Management | DeleteSecret |  | To be tested |
| Key management | UpdateSecret | Update a key | To be tested |
|  | ListSecrets | Query the list of keys | To be tested |
| Mirror Task | ShowJob | This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task. | To be tested |
| MonitorSystem | CreateMonitorSystem | Create the monitoring system configuration. | To be tested |
|  | UpdateMonitorSystem | Update the monitoring system configuration. | To be tested |
|  | ShowMonitorSystem | Obtain the monitoring system configuration. | To be tested |
| NoticeRule | UpdateNoticeRule | Modifies an event notification rule. | To be tested |
|  | DeleteNoticeRule | Delete an event notification rule. | To be tested |
|  | CreateNoticeRule | Create an event notification rule. | To be tested |
|  | ShowNoticeRule | Query the event notification rule. | To be tested |
|  | ListNoticeRules | Query the event notification rule list. | To be tested |
| Secret | ListEffectiveComponents | Obtain the list of credential components that are being used. | To be tested |
| Temporary login command | CreateSecret | Invoke this interface to obtain the value of X-Swr-Dockerlogin in the response message header and the value of host in the response message body to generate a temporary login command. | To be tested |
| VpcEgress | CreateVpcEgress | Creating the VPC access configuration for the CAE environment. | To be tested |
|  | DeleteVpcEgress | Delete the configuration for accessing the VPC in the CAE environment. | To be tested |
|  | ListVpcEgress | Obtain the VPC configuration for accessing the CAE environment. | To be tested |
| environment-controller-v2 | ListEnvironments | Query the environment list of an application. | To be tested |
|  | CreateEnvironment | Create an environment under the application. | To be tested |
|  | DeleteEnvironment | Delete the environment of the application. | To be tested |
| timer-rules | CreateTimerRule | Create a scheduled start and stop rule. | To be tested |
|  | ListTimerRules | Obtain the list of scheduled start and stop rules. | To be tested |
|  | DeleteTimerRule | Delete the scheduled start and stop rule. | To be tested |
|  | UpdateTimerRule | Modify the scheduled start and stop rule. | To be tested |
|  | ShowExecutionResult | Obtain the execution status of the last scheduled start/stop rule. | To be tested |
| websites | ListDomains | Obtain all website assets of a tenant | To be tested |

