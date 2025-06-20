# IEF MCP Server 

## 版本信息
v0.1.0

## 产品描述

IEF MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IEF交互的能力。可以基于自然语言对IEF资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 加密数据管理 | CreateNodeEncryptdatas | 加密数据绑定边缘节点 | To be tested |
|  | CreateEncryptdatas | 新增加密数据 | To be tested |
|  | ListEncryptdataNodes | 获取加密数据绑定的边缘节点 | To be tested |
|  | DeleteNodeEncryptdatas | 解绑边缘节点的加密数据 | To be tested |
|  | ListEncryptdatas | 获取加密数据列表 | To be tested |
|  | ListNodeEncryptdatas | 获取边缘节点绑定的加密数据 | To be tested |
|  | ShowEncryptdatas | 查询加密数据详情 | To be tested |
|  | DeleteEncryptdatas | 删除加密数据 | To be tested |
|  | UpdateEncryptdatas | 更新加密数据 | To be tested |
| 密钥管理 | DeleteSecret | 删除密钥 | To be tested |
|  | ShowSecret | 查询一个密钥详情 | To be tested |
|  | ListSecrets | 查询密钥列表 | To be tested |
|  | UpdateSecret | 更新一个密钥 | To be tested |
|  | CreateSecret | 创建密钥 | To be tested |
| 应用模板管理 | CreateApp | 该API用于创建一个应用模板。 | To be tested |
|  | ListAppVersions | 查询应用模板版本列表 | To be tested |
|  | ShowAppDetail | 查询应用模板详情。 | To be tested |
|  | DeleteAppVersion | 删除应用版本 | To be tested |
|  | DeleteApp | 删除应用模板 | To be tested |
|  | ShowAppVersionDetail | 查询应用模板版本详情 | To be tested |
|  | UpdateAppVersion | 更新一个应用模板版本 | To be tested |
|  | UpdateApp | 更新一个应用模板。 | To be tested |
|  | ListApps | 查询应用模板列表 | To be tested |
|  | CreateAppVersions | 创建一个应用模板版本 | To be tested |
| 批量作业管理 | ListBatchJob | 查询批量处理作业列表 | To be tested |
|  | RestoreBatchJob | 继续执行批量处理作业。该API只对停止的批量处理作业生效 | To be tested |
|  | ShowBatchJob | 查询批量处理作业详情 | To be tested |
|  | CreateBatchJob | 创建批量处理作业。该API用于创建批量处理作业,当前支持:批量节点升级、批量应用部署、批量应用升级 | To be tested |
|  | StopBatchJob | 停止批量处理作业。该API仅对运行中的批量处理作业生效 | To be tested |
|  | RetryBatchJob | 重试批量处理作业。该API仅对执行状态失败的批量处理作业生效 | To be tested |
|  | DeleteBatchJob | 删除批量处理作业 | To be tested |
| 批量节点管理 | ShowProductDetail | 查询批量节点注册作业详情。该接口无法查询产品证书文件 | To be tested |
|  | DeleteProduct | 删除批量节点注册作业。接口调用成功后,与该批量注册任务关联的批量注册凭证将会失效 | To be tested |
|  | CreateProduct | 创建批量节点注册作业。接口调用成功后,您可以将响应消息体中product.package字段使用base64解码成tar.gz产品证书文件,并在控制台下载边缘注册软件edge-register和edge-installer,使用该产品证书批量纳管边缘节点。 | To be tested |
|  | ListProducts | 查询批量节点注册作业列表 | To be tested |
| 服务管理 | UpdateService | 更新一个服务 | To be tested |
|  | CreateService | 创建一个服务 | To be tested |
|  | ListServices | 获取所有的服务详情 | To be tested |
|  | DeleteService | 删除一个服务 | To be tested |
|  | ShowServiceDetail | 查询一个服务的详情 | To be tested |
| 标签管理 | DeleteResourceTag | 删除资源标签。删除时不对标签字符集做校验,调用前必须要做encodeURI,服务端需要对接口uri做decodeURI。删除的key不存在报404,Key不能为空或者空字符串。 | To be tested |
|  | ListTags | 查询指定实例的标签信息 | To be tested |
|  | BatchAddDeleteTags | 为指定实例批量添加或删除标签。 | To be tested |
|  | ListResourceByTags | 使用标签过滤实例 | To be tested |
|  | ListTagsByResourceType | 查询指定项目中实例类型的所有资源标签集合 | To be tested |
|  | CreateTag | 为资源添加标签。 | To be tested |
| 端点管理 | CreateEndpoint | 创建一个端点 | To be tested |
|  | DeleteEndPoint | 删除一个端点 | To be tested |
|  | ListEndpoints | 获取所有的端点详情。 | To be tested |
|  | ShowEndPointDetail | 查询一个端点的详情 | To be tested |
| 系统订阅管理 | CreateSystemEvent | 创建系统订阅 | To be tested |
|  | ShowSystemEventDetail | 查询系统订阅列表 | To be tested |
|  | DeleteSystemEvent | 删除系统订阅列表 | To be tested |
|  | ListSystemEvents | 查询系统订阅列表 | To be tested |
|  | StopSystemEvent | 停用系统订阅 | To be tested |
|  | StartSystemEvent | 启用系统订阅 | To be tested |
| 终端设备模板管理 | ShowDeviceTemplate | 查询一个终端设备模板 | To be tested |
|  | UpdateDeviceTemplateById | 更新一个终端设备模板。 | To be tested |
|  | CreateDeviceTemplate | 创建一个终端设备模板 | To be tested |
|  | ListDeviceTemplates | 查询终端设备模板列表 | To be tested |
|  | DeleteDeviceTemplate | 删除终端设备模板 | To be tested |
| 终端设备管理 | ShowDeviceTwin | 该API用于查询终端设备孪生。 | To be tested |
|  | CreateDevice | 注册终端设备。 | To be tested |
|  | UpdateNodeByDeviceId | 该API用于更新终端设备的边缘节点。功能与更新边缘节点的终端设备相同,推荐使用更新边缘节点的终端设备。 | To be tested |
|  | UpdateDeviceTwin | 该API用于更新终端设备孪生。 | To be tested |
|  | UpdateDevice | 更新一个终端设备。 | To be tested |
|  | ListDevices | 该API用于查询终端设备列表。 | To be tested |
|  | ShowDevice | 该API用于查询终端设备详情。 | To be tested |
|  | DeleteDevice | 该API用于删除终端设备。 | To be tested |
| 规则管理 | StartRule | 启用一条规则 | To be tested |
|  | StopRule | 停用一条规则 | To be tested |
|  | CreateRule | 创建一条规则 | To be tested |
|  | ListRuleErrors | 查询特定规则下的所有错误列表 | To be tested |
|  | ShowRuleDetail | 获取一条规则的详情 | To be tested |
|  | DeleteRule | 删除一条规则 | To be tested |
|  | ListRules | 查询到所有的规则 | To be tested |
| 边缘节点管理 | EnableDisableEdgeNodes | 启用停用边缘节点。被停用的边缘节点将无法连接到云端服务,可用该URI启用边缘节点恢复连接。 | To be tested |
|  | UpdateEdgeNodeDevice | 添加或删除边缘节点的终端设备 | To be tested |
|  | CreateEdgeNode | 该API用于注册一个边缘节点。接口调用成功后,您可以将响应消息体中node.package字段使用base64解码成tar.gz文件,并在控制台下载边缘核心软件,然后纳管边缘节点。 | To be tested |
|  | ListEdgeNodeCerts | 查询边缘节点上的应用证书和设备证书。 | To be tested |
|  | ShowEdgeNodeDetail | 查询边缘节点详情。 | To be tested |
|  | DeleteEdgeNodeCerts | 删除边缘节点上的证书(目前只支持删除应用证书和设备证书) | To be tested |
|  | ListEdgeNodes | 该API用于查询边缘节点。 | To be tested |
|  | UpgradeEdgeNode | 该API用于升级边缘节点。边缘节点将自动升级到最新的可用版本 | To be tested |
|  | DeleteEdgeNode | 删除边缘节点 | To be tested |
|  | CreateEdgeNodeCerts | 创建边缘节点上的应用证书和设备证书。 | To be tested |
|  | UpdateEdgeNode | 该API用于更新边缘节点。 | To be tested |
| 边缘节点组管理 | DeleteEdgeGroupCert | 删除边缘节点组证书 | To be tested |
|  | ShowEdgeGroupDetail | 查询边缘节点组详情。该API只能在铂金版实例中使用 | To be tested |
|  | CreateEdgeGroupCert | 创建边缘节点组证书。边缘节点组证书.tar.gz文件仅在调用该API时提供压缩包下载,请及时下载证书文件 | To be tested |
|  | CreateEdgeGroup | 创建边缘节点组。该API只能在铂金版实例中使用 | To be tested |
|  | ShowEdgeGroupCertDetail | 查询边缘节点组证书详情 | To be tested |
|  | DeleteEdgeGroup | 删除边缘节点组。该API只能在铂金版实例中使用 | To be tested |
|  | UpdateEdgeGroupNodeBinding | 边缘节点组绑定或解绑边缘节点。该API只能在铂金版实例中使用 | To be tested |
|  | ListEdgeGroupCerts | 查询边缘节点组证书列表 | To be tested |
|  | UpdateEdgeGroup | 更新边缘节点组描述。该API只能在铂金版实例中使用 | To be tested |
|  | ListEdgeGroups | 查询边缘节点组列表。该API只能在铂金版实例中使用 | To be tested |
| 部署管理 | UpdateDeployment | 修改应用部署 | To be tested |
|  | RestartDeploymentsPod | 重启部署下的应用实例 | To be tested |
|  | ListDeployments | 查询部署列表 | To be tested |
|  | ListPods | 查询应用实例列表 | To be tested |
|  | CreateDeployments | 创建部署 | To be tested |
|  | DeleteDeployment | 删除应用部署 | To be tested |
|  | ShowDeployment | 查询应用部署 | To be tested |
| 配置项管理 | DeleteConfigMap | 删除配置项 | To be tested |
|  | CreateConfigMap | 创建配置项 | To be tested |
|  | UpdateConfigMap | 更新一个配置项 | To be tested |
|  | ListConfigMaps | 查询配置项列表 | To be tested |
|  | ShowConfigMap | 查询一个配置项详情 | To be tested |
| 配额管理 | ShowQuota | 查询IEF服务下的资源配额 | To be tested |
