# CAE MCP Server 


## Version
v0.1.0

## Overview

CAE MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CAE. Full-chain management of CAE resources can be carried out based on natural language.

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
                    <td rowspan="1">Application</td>
                    <td>ShowApplication</td>
                    <td>Obtain application details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Application operation</td>
                    <td>ListApplications</td>
                    <td>Query the application platform list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApplication</td>
                    <td>Delete a platform application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApplication</td>
                    <td>Create a platform application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Certificate Management</td>
                    <td>UpdateCertificate</td>
                    <td>Modifying a Certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificates</td>
                    <td>Query the certificate list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCertificate</td>
                    <td>Delete a certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificate</td>
                    <td>Create Certificate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Component</td>
                    <td>ListComponentInstances</td>
                    <td>Obtains the component instance list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateComponent</td>
                    <td>Create a component.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteComponent</td>
                    <td>Delete a component.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComponents</td>
                    <td>Obtain the component list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateComponentWithConfiguration</td>
                    <td>Create, configure, and deploy the component.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteAction</td>
                    <td>Perform specified operations on the component, such as deploying, upgrading, restarting, stopping, starting, scaling, configuring, and rolling back the component.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowComponent</td>
                    <td>Obtains component details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateComponent</td>
                    <td>Update the component.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComponentSnapshots</td>
                    <td>Obtains the component snapshot list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ComponentConfiguration</td>
                    <td>CreateComponentConfiguration</td>
                    <td>Create the component configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteComponentConfiguration</td>
                    <td>Delete the component configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComponentConfigurations</td>
                    <td>Obtain the component configuration list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Domain</td>
                    <td>DeleteDomain</td>
                    <td>Delete a domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDomain</td>
                    <td>Create a domain name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">EIP Management</td>
                    <td>ListEips</td>
                    <td>Querying the EIP list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">EVS disk</td>
                    <td>ListVolumes</td>
                    <td>Query details about all EVS disks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVolume</td>
                    <td>Delete an EVS disk.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVolume</td>
                    <td>Create a pay-per-use or yearly/monthly EVS disk.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Eip</td>
                    <td>UpdateEip</td>
                    <td>Modify the inbound and outbound bandwidth and enable/disable status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Entrusted management</td>
                    <td>CreateAgency</td>
                    <td>This API is used by the [administrator] (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to create an agency.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgencies</td>
                    <td>This interface is used by the (https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) to query the agency list based on the specified conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job</td>
                    <td>RetryJob</td>
                    <td>Retry the task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Key Management</td>
                    <td>DeleteSecret</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Key management</td>
                    <td>UpdateSecret</td>
                    <td>Update a key</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecrets</td>
                    <td>Query the list of keys</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Mirror Task</td>
                    <td>ShowJob</td>
                    <td>This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">MonitorSystem</td>
                    <td>CreateMonitorSystem</td>
                    <td>Create the monitoring system configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMonitorSystem</td>
                    <td>Update the monitoring system configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonitorSystem</td>
                    <td>Obtain the monitoring system configuration.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">NoticeRule</td>
                    <td>UpdateNoticeRule</td>
                    <td>Modifies an event notification rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNoticeRule</td>
                    <td>Delete an event notification rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNoticeRule</td>
                    <td>Create an event notification rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNoticeRule</td>
                    <td>Query the event notification rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNoticeRules</td>
                    <td>Query the event notification rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Secret</td>
                    <td>ListEffectiveComponents</td>
                    <td>Obtain the list of credential components that are being used.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Temporary login command</td>
                    <td>CreateSecret</td>
                    <td>Invoke this interface to obtain the value of X-Swr-Dockerlogin in the response message header and the value of host in the response message body to generate a temporary login command.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">VpcEgress</td>
                    <td>CreateVpcEgress</td>
                    <td>Creating the VPC access configuration for the CAE environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpcEgress</td>
                    <td>Delete the configuration for accessing the VPC in the CAE environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcEgress</td>
                    <td>Obtain the VPC configuration for accessing the CAE environment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">environment-controller-v2</td>
                    <td>ListEnvironments</td>
                    <td>Query the environment list of an application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnvironment</td>
                    <td>Create an environment under the application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnvironment</td>
                    <td>Delete the environment of the application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">timer-rules</td>
                    <td>CreateTimerRule</td>
                    <td>Create a scheduled start and stop rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTimerRules</td>
                    <td>Obtain the list of scheduled start and stop rules.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTimerRule</td>
                    <td>Delete the scheduled start and stop rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTimerRule</td>
                    <td>Modify the scheduled start and stop rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowExecutionResult</td>
                    <td>Obtain the execution status of the last scheduled start/stop rule.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">websites</td>
                    <td>ListDomains</td>
                    <td>Obtain all website assets of a tenant</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
