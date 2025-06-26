# APM MCP Server 


## Version
v0.1.0

## Overview

APM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service APM. Full-chain management of APM resources can be carried out based on natural language.

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
                    <td rowspan="3">AKSK</td>
                    <td>ShowAkSks</td>
                    <td>Query the AK/SK of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAkSk</td>
                    <td>Create an AK/SK.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAkSk</td>
                    <td>Delete the AK/SK.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ALARM</td>
                    <td>ListAlarmNotify</td>
                    <td>Query the triggering details and history of a single alarm.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarmData</td>
                    <td>Query alarms in the system.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">APM</td>
                    <td>ChangeAgentStatus</td>
                    <td>Changes the collection status of a specified instance, that is, enabled or disabled.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMasterAddress</td>
                    <td>Obtain the POLB address of the master service in the region based on the region name.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAgent</td>
                    <td>Delete an agent</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveMonitorItemConfig</td>
                    <td>Save the monitoring item.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvMonitorItem</td>
                    <td>Query the monitoring item list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAkSk</td>
                    <td>Obtain the AK/SK list created by the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBusiness</td>
                    <td>This interface is used to query applications of a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchAgent</td>
                    <td>This interface is used to search for all probes in an application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchApplication</td>
                    <td>Search for components, environments, and probes in a specified region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">App Template Management</td>
                    <td>ListApps</td>
                    <td>Query the application template list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApp</td>
                    <td>Delete an application template</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">CMDB</td>
                    <td>ShowSubBusinessDetail</td>
                    <td>Query details about a single subapplication.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppEnvs</td>
                    <td>Obtain the environment list of the component.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvTags</td>
                    <td>API for querying environment labels.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBusinessDetail</td>
                    <td>Query details about a single application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTopologyTree</td>
                    <td>Obtain the application tree.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Profiling</td>
                    <td>ShowFlameLineTree</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">REGION</td>
                    <td>ListOpenRegion</td>
                    <td>This interface is used to query the information about the region enabled by a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSupportedRegion</td>
                    <td>Query information about all supported regions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">TOPOLOGY</td>
                    <td>SearchEnvTopology</td>
                    <td>Query the environment-level global topology information of a component.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchBusinessTopology</td>
                    <td>Query application-level global topology information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">TRACING</td>
                    <td>ShowToken</td>
                    <td>Obtain the token of the link trace application.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBusiness</td>
                    <td>Create a link trace application</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAccessPoint</td>
                    <td>Obtain the access address of the link trace application</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">TRANSACTION</td>
                    <td>SearchTransactionConfig</td>
                    <td>Query the configured URL tracing configuration list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBusinessEnv</td>
                    <td>Query the list of environments where URL tracing is enabled in the selected region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchTransaction</td>
                    <td>Query the list of invoked URL tracing views.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTransactionDetail</td>
                    <td>Query the details of a URL tracing view.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">VIEW</td>
                    <td>ShowEnvMonitorItems</td>
                    <td>Obtain monitoring item information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRawTable</td>
                    <td>Obtain the original data table.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonitorItemDetail</td>
                    <td>Obtains details about a monitoring item.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonitorItemViewConfig</td>
                    <td>Query the configuration information about a monitoring item.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSpanSearch</td>
                    <td>Interface for querying span data.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTopology</td>
                    <td>Call chain topology.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClobDetail</td>
                    <td>Obtain raw data details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvInstances</td>
                    <td>Obtains the instance list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrend</td>
                    <td>Obtain the trend chart.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSumTable</td>
                    <td>Obtains summary table data.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTraceEvents</td>
                    <td>Obtains all call chain data of a trace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEventDetail</td>
                    <td>Obtains details about an event.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
