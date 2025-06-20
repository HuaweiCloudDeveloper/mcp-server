# KPS MCP Server 

## 版本信息
v0.1.0

## 产品描述

KPS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务KPS交互的能力。可以基于自然语言对KPS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 密钥对任务管理 | ListFailedTask | 查询绑定、解绑等操作失败的任务信息。 | To be tested |
|  | DeleteFailedTask | 删除失败的任务。 | To be tested |
|  | AssociateKeypair | 给指定的虚拟机绑定(替换或重置,替换需提供虚拟机已配置的SSH密钥对私钥;重置不需要提供虚拟机的SSH密钥对私钥)新的SSH密钥对。 | To be tested |
|  | BatchAssociateKeypair | 给指定的虚拟机批量绑定新的SSH密钥对。 | To be tested |
|  | ListKeypairTask | 根据SSH密钥对接口返回的task_id,查询SSH密钥对当前任务的执行状态。 | To be tested |
|  | DisassociateKeypair | 给指定的虚拟机解除绑定SSH密钥对并恢复SSH密码登录。 | To be tested |
|  | DeleteAllFailedTask | 删除操作失败的任务信息。 | To be tested |
|  | ListRunningTask | 查询正在处理的任务信息。 | To be tested |
| 密钥对管理 | CreateKeypair | 创建和导入SSH密钥对 | To be tested |
|  | ClearPrivateKey | 清除SSH密钥对私钥。 | To be tested |
|  | ExportPrivateKey | 导出指定密钥对的私钥。 | To be tested |
|  | UpdateKeypairDescription | 更新SSH密钥对描述。 | To be tested |
|  | ImportPrivateKey | 导入私钥到指定密钥对。 | To be tested |
|  | BatchImportKeypair | 批量导入SSH密钥对,单次批量导入不得超过10条记录。 | To be tested |
|  | DeleteKeypair | 删除SSH密钥对。 | To be tested |
|  | ListKeypairs | 查询SSH密钥对列表 | To be tested |
|  | BatchExportPrivateKey | 批量导出密钥对私钥,单次最多导出10条数据 | To be tested |
|  | ListKeypairDetail | 查询SSH密钥对详细信息 | To be tested |
