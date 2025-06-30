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
                    <td rowspan="2">AppManagement</td>
                    <td>CreateApp</td>
                    <td>该接口用于用户创建应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApp</td>
                    <td>该接口用于用户修改应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">IAlgorithmController</td>
                    <td>ShowServiceDetail</td>
                    <td>获取服务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">临时登录指令</td>
                    <td>CreateSecret</td>
                    <td>调用该接口,通过获取响应消息头的X-Swr-Dockerlogin的值及响应消息体的host值,可生成临时登录指令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">产品管理</td>
                    <td>DeleteProduct</td>
                    <td>删除产品</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProduct</td>
                    <td>创建产品</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProducts</td>
                    <td>查询产品</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">加密数据管理</td>
                    <td>CreateNodeEncryptdatas</td>
                    <td>加密数据绑定边缘节点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEncryptdatas</td>
                    <td>新增加密数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEncryptdataNodes</td>
                    <td>获取加密数据绑定的边缘节点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNodeEncryptdatas</td>
                    <td>解绑边缘节点的加密数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEncryptdatas</td>
                    <td>获取加密数据列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodeEncryptdatas</td>
                    <td>获取边缘节点绑定的加密数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEncryptdatas</td>
                    <td>查询加密数据详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEncryptdatas</td>
                    <td>删除加密数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEncryptdatas</td>
                    <td>更新加密数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">密钥管理</td>
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
                    <td>ListSecrets</td>
                    <td>查询密钥列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecret</td>
                    <td>更新一个密钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">应用模板管理</td>
                    <td>ListAppVersions</td>
                    <td>查询应用模板版本列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppDetail</td>
                    <td>查询应用模板详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppVersion</td>
                    <td>删除应用版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApp</td>
                    <td>删除应用模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppVersionDetail</td>
                    <td>查询应用模板版本详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppVersion</td>
                    <td>更新一个应用模板版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApps</td>
                    <td>查询应用模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppVersions</td>
                    <td>创建一个应用模板版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">批量作业管理</td>
                    <td>ListBatchJob</td>
                    <td>查询批量处理作业列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreBatchJob</td>
                    <td>继续执行批量处理作业。该API只对停止的批量处理作业生效</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBatchJob</td>
                    <td>查询批量处理作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBatchJob</td>
                    <td>创建批量处理作业。该API用于创建批量处理作业,当前支持:批量节点升级、批量应用部署、批量应用升级</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopBatchJob</td>
                    <td>停止批量处理作业。该API仅对运行中的批量处理作业生效</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryBatchJob</td>
                    <td>重试批量处理作业。该API仅对执行状态失败的批量处理作业生效</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBatchJob</td>
                    <td>删除批量处理作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">批量节点管理</td>
                    <td>ShowProductDetail</td>
                    <td>查询批量节点注册作业详情。该接口无法查询产品证书文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">服务管理</td>
                    <td>UpdateService</td>
                    <td>修改服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateService</td>
                    <td>创建服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServices</td>
                    <td>查询服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteService</td>
                    <td>删除服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">标签管理</td>
                    <td>BatchAddDeleteTags</td>
                    <td>为指定实例批量添加或删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceByTags</td>
                    <td>使用标签过滤实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagsByResourceType</td>
                    <td>查询指定项目中实例类型的所有资源标签集合</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTag</td>
                    <td>为资源添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">端点管理</td>
                    <td>DeleteEndPoint</td>
                    <td>删除一个端点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEndPointDetail</td>
                    <td>查询一个端点的详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">系统订阅管理</td>
                    <td>CreateSystemEvent</td>
                    <td>创建系统订阅</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSystemEventDetail</td>
                    <td>查询系统订阅列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSystemEvent</td>
                    <td>删除系统订阅列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSystemEvents</td>
                    <td>查询系统订阅列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopSystemEvent</td>
                    <td>停用系统订阅</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartSystemEvent</td>
                    <td>启用系统订阅</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">终端节点功能</td>
                    <td>CreateEndpoint</td>
                    <td>创建终端节点,以便访问终端节点服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpoints</td>
                    <td>查询当前用户下的终端节点的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">终端设备模板管理</td>
                    <td>ShowDeviceTemplate</td>
                    <td>查询一个终端设备模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceTemplateById</td>
                    <td>更新一个终端设备模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeviceTemplate</td>
                    <td>创建一个终端设备模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDeviceTemplates</td>
                    <td>查询终端设备模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceTemplate</td>
                    <td>删除终端设备模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">终端设备管理</td>
                    <td>ShowDeviceTwin</td>
                    <td>该API用于查询终端设备孪生。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNodeByDeviceId</td>
                    <td>该API用于更新终端设备的边缘节点。功能与更新边缘节点的终端设备相同,推荐使用更新边缘节点的终端设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceTwin</td>
                    <td>该API用于更新终端设备孪生。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">规则引擎</td>
                    <td>CreateRule</td>
                    <td>创建规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRule</td>
                    <td>删除规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRules</td>
                    <td>查询规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">规则管理</td>
                    <td>StartRule</td>
                    <td>启用一条规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopRule</td>
                    <td>停用一条规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRuleErrors</td>
                    <td>查询特定规则下的所有错误列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRuleDetail</td>
                    <td>获取一条规则的详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">设备管理</td>
                    <td>CreateDevice</td>
                    <td>创建设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDevice</td>
                    <td>修改设备信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevices</td>
                    <td>此接口用于获取已经注册成功的GB/T28181设备列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDevice</td>
                    <td>查询设备详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDevice</td>
                    <td>此接口用于删除指定设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资源标签</td>
                    <td>DeleteResourceTag</td>
                    <td>用于批量移除云服务多个资源的标签,每个资源最多支持移除10个标签,每次最多支持批量操作20个资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">边缘节点管理</td>
                    <td>EnableDisableEdgeNodes</td>
                    <td>启用停用边缘节点。被停用的边缘节点将无法连接到云端服务,可用该URI启用边缘节点恢复连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeNodeDevice</td>
                    <td>添加或删除边缘节点的终端设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeNode</td>
                    <td>该API用于注册一个边缘节点。接口调用成功后,您可以将响应消息体中node.package字段使用base64解码成tar.gz文件,并在控制台下载边缘核心软件,然后纳管边缘节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeNodeCerts</td>
                    <td>查询边缘节点上的应用证书和设备证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeNodeDetail</td>
                    <td>查询边缘节点详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeNodeCerts</td>
                    <td>删除边缘节点上的证书(目前只支持删除应用证书和设备证书)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeNodes</td>
                    <td>该API用于查询边缘节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeEdgeNode</td>
                    <td>该API用于升级边缘节点。边缘节点将自动升级到最新的可用版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeNode</td>
                    <td>删除边缘节点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeNodeCerts</td>
                    <td>创建边缘节点上的应用证书和设备证书。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeNode</td>
                    <td>该API用于更新边缘节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">边缘节点组管理</td>
                    <td>DeleteEdgeGroupCert</td>
                    <td>删除边缘节点组证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeGroupDetail</td>
                    <td>查询边缘节点组详情。该API只能在铂金版实例中使用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeGroupCert</td>
                    <td>创建边缘节点组证书。边缘节点组证书.tar.gz文件仅在调用该API时提供压缩包下载,请及时下载证书文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeGroup</td>
                    <td>创建边缘节点组。该API只能在铂金版实例中使用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeGroupCertDetail</td>
                    <td>查询边缘节点组证书详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeGroup</td>
                    <td>删除边缘节点组。该API只能在铂金版实例中使用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeGroupNodeBinding</td>
                    <td>边缘节点组绑定或解绑边缘节点。该API只能在铂金版实例中使用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeGroupCerts</td>
                    <td>查询边缘节点组证书列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeGroup</td>
                    <td>更新边缘节点组描述。该API只能在铂金版实例中使用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeGroups</td>
                    <td>查询边缘节点组列表。该API只能在铂金版实例中使用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">部署管理</td>
                    <td>UpdateDeployment</td>
                    <td>修改应用部署</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartDeploymentsPod</td>
                    <td>重启部署下的应用实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDeployments</td>
                    <td>查询部署列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPods</td>
                    <td>查询应用实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeployments</td>
                    <td>创建部署</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeployment</td>
                    <td>删除应用部署</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeployment</td>
                    <td>查询应用部署</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">配置项管理</td>
                    <td>DeleteConfigMap</td>
                    <td>删除配置项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConfigMap</td>
                    <td>创建配置项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfigMap</td>
                    <td>更新一个配置项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigMaps</td>
                    <td>查询配置项列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigMap</td>
                    <td>查询一个配置项详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ShowQuota</td>
                    <td>查询单租户在VPC服务下的网络资源配额,包括vpc配额、子网配额、安全组配额、安全组规则配额、弹性公网IP配额,vpn配额等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像标签</td>
                    <td>ListTags</td>
                    <td>根据不同条件查询镜像标签列表信息。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
