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
                    <td>获取应用详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Application操作</td>
                    <td>ListApplications</td>
                    <td>查询应用平台列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApplication</td>
                    <td>删除平台应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApplication</td>
                    <td>创建平台应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Component</td>
                    <td>ListComponentInstances</td>
                    <td>获取组件实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateComponent</td>
                    <td>创建组件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteComponent</td>
                    <td>删除组件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComponents</td>
                    <td>获取组件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateComponentWithConfiguration</td>
                    <td>创建、生效配置并部署组件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteAction</td>
                    <td>对组件执行指定操作,如部署、升级、重启、停止、启动、伸缩、配置、回滚。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowComponent</td>
                    <td>获取组件详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateComponent</td>
                    <td>更新组件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComponentSnapshots</td>
                    <td>获取组件快照列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ComponentConfiguration</td>
                    <td>CreateComponentConfiguration</td>
                    <td>创建组件配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteComponentConfiguration</td>
                    <td>删除组件配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComponentConfigurations</td>
                    <td>获取组件配置列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Domain</td>
                    <td>DeleteDomain</td>
                    <td>删除域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDomain</td>
                    <td>创建域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">EIP管理</td>
                    <td>ListEips</td>
                    <td>弹性IP列表查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Eip</td>
                    <td>UpdateEip</td>
                    <td>修改出入网带宽以及开闭状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job</td>
                    <td>RetryJob</td>
                    <td>重试任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">MonitorSystem</td>
                    <td>CreateMonitorSystem</td>
                    <td>创建监控系统配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMonitorSystem</td>
                    <td>更新监控系统配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMonitorSystem</td>
                    <td>获取监控系统配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">NoticeRule</td>
                    <td>UpdateNoticeRule</td>
                    <td>修改事件通知规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNoticeRule</td>
                    <td>删除事件通知规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNoticeRule</td>
                    <td>创建事件通知规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNoticeRule</td>
                    <td>查询事件通知规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNoticeRules</td>
                    <td>查询事件通知规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Secret</td>
                    <td>ListEffectiveComponents</td>
                    <td>获取当前正在使用的对应凭据组件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">VpcEgress</td>
                    <td>CreateVpcEgress</td>
                    <td>创建CAE环境访问VPC配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVpcEgress</td>
                    <td>删除CAE环境访问VPC配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVpcEgress</td>
                    <td>获取CAE环境访问VPC配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">environment-controller-v2</td>
                    <td>ListEnvironments</td>
                    <td>查询应用下环境列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnvironment</td>
                    <td>应用下创建环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnvironment</td>
                    <td>删除应用下的环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">timer-rules</td>
                    <td>CreateTimerRule</td>
                    <td>创建定时启停规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTimerRules</td>
                    <td>获取定时启停规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTimerRule</td>
                    <td>删除定时启停规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTimerRule</td>
                    <td>修改定时启停规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowExecutionResult</td>
                    <td>获取上次定时启停规则的执行情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">websites</td>
                    <td>ListDomains</td>
                    <td>获取租户的所有网站资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">临时登录指令</td>
                    <td>CreateSecret</td>
                    <td>调用该接口,通过获取响应消息头的X-Swr-Dockerlogin的值及响应消息体的host值,可生成临时登录指令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">云硬盘</td>
                    <td>ListVolumes</td>
                    <td>查询所有云硬盘的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVolume</td>
                    <td>删除一个云硬盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVolume</td>
                    <td>创建按需或包周期云硬盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">委托管理</td>
                    <td>CreateAgency</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgencies</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定条件下的委托列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">密钥管理</td>
                    <td>UpdateSecret</td>
                    <td>更新一个密钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecret</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecrets</td>
                    <td>查询密钥列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">证书管理</td>
                    <td>UpdateCertificate</td>
                    <td>修改证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCertificates</td>
                    <td>查询证书列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCertificate</td>
                    <td>删除证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCertificate</td>
                    <td>创建证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像任务</td>
                    <td>ShowJob</td>
                    <td>该接口为扩展接口,主要用于查询异步接口执行情况,比如查询导出镜像任务的执行状态。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
