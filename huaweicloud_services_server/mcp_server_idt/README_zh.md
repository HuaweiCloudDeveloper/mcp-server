# IDT MCP Server 

## 版本信息
v0.1.0

## 产品描述

IDT MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IDT交互的能力。可以基于自然语言对IDT资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Linkx同步任务 | PatchUpdateLinkxSyncTask |  | To be tested |
|  | PatchGetLinkxSyncTask |  | To be tested |
|  | PatchLogicalDeleteLinkxSyncTask |  | To be tested |
|  | ListHistoryDataLinkxSyncTask |  | To be tested |
|  | ShowLinkxSyncTask |  | To be tested |
|  | DeleteLinkxSyncTask |  | To be tested |
|  | SaveLinkxSyncTask |  | To be tested |
|  | UpdateByConditionLinkxSyncTask |  | To be tested |
|  | UpdateLinkxSyncTask |  | To be tested |
|  | ExecuteStaticsLinkxSyncTask |  | To be tested |
|  | ExecuteLogicalDeleteByConditionLinkxSyncTask |  | To be tested |
|  | ExecuteStatisticsHistoryDataLinkxSyncTask |  | To be tested |
|  | CompareVersionLinkxSyncTask |  | To be tested |
|  | CountLinkxSyncTask |  | To be tested |
| XDM基线对象 | ListHistoryDataBaseLine |  | To be tested |
|  | DeleteBaseLine |  | To be tested |
|  | SaveAllBaseLine |  | To be tested |
|  | DeleteByConditionBaseLine |  | To be tested |
|  | UpdateBaseLine |  | To be tested |
|  | CountBaseLine |  | To be tested |
|  | ShowBaseLine |  | To be tested |
|  | PatchCreateBaseLine |  | To be tested |
|  | ExecuteStatisticsHistoryDataBaseLine |  | To be tested |
|  | CompareVersionBaseLine |  | To be tested |
|  | PatchDeleteBaseLine |  | To be tested |
|  | UpdateByConditionBaseLine |  | To be tested |
|  | SearchBaseLine |  | To be tested |
| XDM权限属性 | PatchGetXdmPermissionAttribute |  | To be tested |
|  | ShowXDmPermissionAttributeXdmPermissionAttribute |  | To be tested |
|  | PatchDeleteXdmPermissionAttribute |  | To be tested |
|  | PatchCreateXdmPermissionAttribute |  | To be tested |
|  | UpdateByConditionXdmPermissionAttribute |  | To be tested |
|  | SaveAllXDmPermissionAttributeXdmPermissionAttribute |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmPermissionAttribute |  | To be tested |
|  | ListXdmPermissionAttributeQuery |  | To be tested |
|  | DeleteXDmPermissionAttributeXdmPermissionAttribute |  | To be tested |
|  | ListXDmPermissionAttributeXdmPermissionAttribute |  | To be tested |
|  | PatchUpdateXdmPermissionAttribute |  | To be tested |
|  | SearchXdmPermissionAttribute |  | To be tested |
|  | SaveXdmPermissionAttribute |  | To be tested |
|  | ListHistoryDataXdmPermissionAttribute |  | To be tested |
| 全局API | RunGlobalSystemManagement | 该API用于管理系统管理API。 | To be tested |
|  | RunGlobalApiPageInfo | 该API用于分页查询数据实体/关系实体的相关信息。 | To be tested |
|  | RunGlobalApi | 该API用于管理数据实体/关系实体的全量API。 | To be tested |
| 关联模型图记录 | PatchUpdateXdmSearchServRelationLog |  | To be tested |
|  | DeleteXDmSearchServRelationLogXdmSearchServRelationLog |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmSearchServRelationLog |  | To be tested |
|  | SearchXdmSearchServRelationLog |  | To be tested |
|  | UpdateXdmSearchServRelationLog |  | To be tested |
|  | PatchCreateXdmSearchServRelationLog |  | To be tested |
|  | PatchDeleteXdmSearchServRelationLog |  | To be tested |
|  | PatchGetXdmSearchServRelationLog |  | To be tested |
|  | DeleteByConditionXdmSearchServRelationLog |  | To be tested |
|  | CountXDmSearchServRelationLogXdmSearchServRelationLog |  | To be tested |
|  | ExecuteStaticsXdmSearchServRelationLog |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmSearchServRelationLog |  | To be tested |
|  | ShowXDmSearchServRelationLogXdmSearchServRelationLog |  | To be tested |
|  | UpdateByConditionXdmSearchServRelationLog |  | To be tested |
| 分类管理 | ExecuteGenerateBusinessCodeClassificationNode |  | To be tested |
|  | SearchClassificationNode |  | To be tested |
|  | ListClassificationNodeQuery |  | To be tested |
|  | SearchAttributeattribute | 分类节点属性分页查询 | To be tested |
|  | UpdateClassificationNode | 仅更新入参传入的字段信息,当ID不存在时,不处理传入的实例信息 | To be tested |
|  | ShowCategoryNodeInfoClassificationNode | 获取分类节点属性列表 | To be tested |
|  | ShowRootClassificationNode |  | To be tested |
|  | DeleteClassificationNode | 根据对象入参删除实例数据 | To be tested |
|  | ExecuteLogicalDeleteByConditionClassificationNode |  | To be tested |
|  | ExecuteStatisticsHistoryDataClassificationNode |  | To be tested |
|  | ShowAllParentListClassificationNode |  | To be tested |
|  | ExecuteLogicalDeleteClassificationNode |  | To be tested |
|  | RefreshClassificationNode |  | To be tested |
|  | ShowChildrenClassificationNode | 获取指定分类节点下子节点集合 | To be tested |
|  | PatchUpdateClassificationNode |  | To be tested |
|  | CompareVersionClassificationNode |  | To be tested |
|  | ShowAttributesInfosClassificationNode | 数据实例获取节点属性以及父属性节点 | To be tested |
|  | PatchGetClassificationNode |  | To be tested |
|  | PatchCreateClassificationNode |  | To be tested |
|  | EnableClassificationNode | 根据对象ID生效对应实例数据,返回成功条目数据 | To be tested |
|  | DisableClassificationNode | 根据对象ID失效对应实例数据,返回成功条目数据 | To be tested |
|  | CountClassificationNode |  | To be tested |
|  | UpdateByConditionClassificationNode |  | To be tested |
|  | ShowParentClassificationNode |  | To be tested |
|  | ExecuteSelectClassificationNode |  | To be tested |
|  | CreateClassificationNode | 根据对象入参创建实例数据 | To be tested |
|  | ShowByBusinessCodeClassificationNode |  | To be tested |
|  | PatchRemoveChildNodeClassificationNode |  | To be tested |
|  | PatchDeleteClassificationNode |  | To be tested |
|  | ShowCategoryTreeByNameClassificationNode |  | To be tested |
|  | SearchParentAttributeparentAttribute | 父节点属性分页查询 | To be tested |
| 分类节点的分组 | PatchUpdateClassificationNodeGroup |  | To be tested |
|  | PatchCreateClassificationNodeGroup |  | To be tested |
|  | PatchLogicalDeleteClassificationNodeGroup |  | To be tested |
|  | CountClassificationNodeGroup |  | To be tested |
|  | ExecuteSelectClassificationNodeGroup |  | To be tested |
|  | UpdateClassificationNodeGroup |  | To be tested |
|  | DeleteByConditionClassificationNodeGroup |  | To be tested |
|  | SaveAllClassificationNodeGroup |  | To be tested |
|  | ExecuteLogicalDeleteByConditionClassificationNodeGroup |  | To be tested |
|  | ListClassificationNodeGroupQuery |  | To be tested |
|  | PatchDeleteClassificationNodeGroup |  | To be tested |
|  | ExecuteStaticsClassificationNodeGroup |  | To be tested |
|  | ExecuteLogicalDeleteClassificationNodeGroup |  | To be tested |
|  | SearchClassificationNodeGroup |  | To be tested |
|  | CompareVersionClassificationNodeGroup |  | To be tested |
| 单位类型 | PatchLogicalDeleteUnitType |  | To be tested |
|  | UpdateByConditionUnitType |  | To be tested |
|  | EnableUnitType | 根据对象ID生效对应实例数据,返回成功条目数据 | To be tested |
|  | ExecuteLogicalDeleteUnitType |  | To be tested |
|  | ListAllUnitTypeNameList | 根据对象入参查询单位类型列表 | To be tested |
|  | SaveUnitType |  | To be tested |
|  | CompareVersionUnitType |  | To be tested |
|  | ListHistoryDataUnitType |  | To be tested |
|  | SaveAllUnitType |  | To be tested |
|  | ExecuteSelectUnitType |  | To be tested |
|  | ListUnitTypeQuery | 根据对象入参查询对象列表属性且支持分页 | To be tested |
|  | CountUnitType |  | To be tested |
|  | DeleteUnitType | 根据对象入参删除实例数据 | To be tested |
|  | CreateUnitType | 根据对象入参批量创建实例数据 | To be tested |
|  | PatchGetUnitType |  | To be tested |
|  | ListUnitType |  | To be tested |
|  | ShowByBusinessCodeUnitType |  | To be tested |
|  | UpdateUnitType | 仅更新入参传入的字段信息,当ID不存在时,不处理传入的实例信息 | To be tested |
|  | ExecuteGenerateBusinessCodeUnitType |  | To be tested |
|  | DeleteByConditionUnitType |  | To be tested |
| 参与者关系的操作历史记录 | CompareVersionXDmPrincipalRelationOperationHistory |  | To be tested |
|  | PatchLogicalDeleteXDmPrincipalRelationOperationHistory |  | To be tested |
|  | ExecuteStaticsXdmPrincipalRelationOperationHistory |  | To be tested |
|  | SaveXdmPrincipalRelationOperationHistory |  | To be tested |
|  | ListHistoryDataXdmPrincipalRelationOperationHistory |  | To be tested |
|  | UpdateXdmPrincipalRelationOperationHistory |  | To be tested |
|  | PatchCreateXdmPrincipalRelationOperationHistory |  | To be tested |
|  | SearchXdmPrincipalRelationOperationHistory |  | To be tested |
| 合法值 | PatchGetLegalValue |  | To be tested |
|  | EnableLegalValue |  | To be tested |
|  | ExecuteStaticsLegalValue |  | To be tested |
|  | PatchCreateLegalValue |  | To be tested |
|  | ExecuteSelectLegalValue |  | To be tested |
|  | SaveAllLegalValue |  | To be tested |
|  | DeleteByConditionLegalValue |  | To be tested |
|  | ShowLegalValue |  | To be tested |
|  | DeleteLegalValue |  | To be tested |
|  | CountLegalValue |  | To be tested |
|  | UpdateByConditionLegalValue |  | To be tested |
|  | PatchLogicalDeleteLegalValue |  | To be tested |
|  | SearchLegalValue |  | To be tested |
|  | ExecuteLogicalDeleteLegalValue |  | To be tested |
| 合法值类型 | ShowLegalValueType |  | To be tested |
|  | UpdateByConditionLegalValueType |  | To be tested |
|  | CountLegalValueType |  | To be tested |
|  | DeleteByConditionLegalValueType |  | To be tested |
|  | PatchGetLegalValueType |  | To be tested |
|  | PatchLogicalDeleteLegalValueType |  | To be tested |
|  | ExecuteLogicalDeleteByConditionLegalValueType |  | To be tested |
|  | ExecuteSelectLegalValueType |  | To be tested |
|  | SaveAllLegalValueType |  | To be tested |
|  | SearchLegalValueType |  | To be tested |
|  | PatchCreateLegalValueType |  | To be tested |
|  | ExecuteStatisticsHistoryDataLegalValueType |  | To be tested |
|  | ListHistoryDataLegalValueType |  | To be tested |
|  | ExecuteStaticsLegalValueType |  | To be tested |
|  | CreateLegalValueType |  | To be tested |
| 团队 | ExecuteSelectXDmTeamXdmTeam |  | To be tested |
|  | SaveXdmTeam |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmTeam |  | To be tested |
|  | EnableXDmTeamXdmTeam |  | To be tested |
|  | ListXDmTeamXdmTeam |  | To be tested |
|  | UpdateByConditionXdmTeam |  | To be tested |
|  | ListHistoryDataXdmTeam |  | To be tested |
|  | ExecuteStaticsXdmTeam |  | To be tested |
|  | UpdateXdmTeam |  | To be tested |
|  | SaveAllXDmTeamXdmTeam |  | To be tested |
|  | CountXDmTeamXdmTeam |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmTeamXdmTeam |  | To be tested |
|  | DeleteXDmTeamXdmTeam |  | To be tested |
|  | DeleteByConditionXdmTeam |  | To be tested |
|  | ShowXDmTeamXdmTeam |  | To be tested |
| 团队与团队角色关系 | PatchDeleteXdmTeamAndTeamRoleRelation |  | To be tested |
|  | SaveAllXDmTeamAndTeamRoleRelationXdmTeamAndTeamRoleRelation |  | To be tested |
|  | SaveXdmTeamAndTeamRoleRelation |  | To be tested |
|  | ListXDmTeamAndTeamRoleRelationXdmTeamAndTeamRoleRelation |  | To be tested |
|  | PatchUpdateXdmTeamAndTeamRoleRelation |  | To be tested |
|  | PatchGetXdmTeamAndTeamRoleRelation |  | To be tested |
|  | ListHistoryDataXdmTeamAndTeamRoleRelation |  | To be tested |
|  | PatchCreateXdmTeamAndTeamRoleRelation |  | To be tested |
|  | ListXDmTeamAndTeamRoleRelationXdmTeamAndTeamRoleRelationQuery |  | To be tested |
|  | DeleteByConditionXdmTeamAndTeamRoleRelation |  | To be tested |
|  | EnableXDmTeamAndTeamRoleRelationXdmTeamAndTeamRoleRelation |  | To be tested |
|  | CreateXDmTeamAndTeamRoleRelationXdmTeamAndTeamRoleRelation |  | To be tested |
|  | ShowXDmTeamAndTeamRoleRelationXdmTeamAndTeamRoleRelation |  | To be tested |
|  | DeleteXDmTeamAndTeamRoleRelationXdmTeamAndTeamRoleRelation |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmTeamAndTeamRoleRelation |  | To be tested |
| 团队角色 | DisableXDmTeamRoleXdmTeamRole |  | To be tested |
|  | ListHistoryDataXdmTeamRole |  | To be tested |
|  | CountXDmTeamRoleXdmTeamRole |  | To be tested |
|  | UpdateXdmTeamRole |  | To be tested |
|  | PatchDeleteXdmTeamRole |  | To be tested |
|  | SaveAllXDmTeamRoleXdmTeamRole |  | To be tested |
|  | ShowXDmTeamRoleXdmTeamRole |  | To be tested |
|  | ExecuteStaticsXdmTeamRole |  | To be tested |
|  | PatchCreateXdmTeamRole |  | To be tested |
|  | CreateXDmTeamRoleXdmTeamRole |  | To be tested |
|  | EnableXDmTeamRoleXdmTeamRole |  | To be tested |
|  | SearchXdmTeamRole |  | To be tested |
|  | ExecuteSelectXDmTeamRoleXdmTeamRole |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmTeamRole |  | To be tested |
|  | PatchLogicalDeleteXDmTeamRoleXdmTeamRole |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmTeamRoleXdmTeamRole |  | To be tested |
|  | ExecuteLogicalDeleteXDmTeamRoleXdmTeamRole |  | To be tested |
|  | ListXDmTeamRoleXdmTeamRoleQuery |  | To be tested |
| 团队里的团队角色成员关系 | DeleteTargetXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | PatchDeleteXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | ExecuteLogicalDeleteXDmTeamAndTeamRoleRelationMember |  | To be tested |
|  | PatchQueryRelatedObjectsXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | SearchXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | PatchUpdateXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | ListRelationshipXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | ListTargetXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | PatchLogicalDeleteXDmTeamAndTeamRoleRelationMember |  | To be tested |
|  | PatchGetXdmTeamAndTeamRoleRelationMember |  | To be tested |
| 基线对象与被基线对象的关系 | SaveAllBaseLineLink |  | To be tested |
|  | ExecuteLogicalDeleteBaseLineLink |  | To be tested |
|  | DeleteBaseLineLink |  | To be tested |
|  | CompareVersionBaseLineLink |  | To be tested |
|  | ExecuteStatisticsHistoryDataBaseLineLink |  | To be tested |
|  | PatchCreateBaseLineLink |  | To be tested |
|  | UpdateByConditionBaseLineLink |  | To be tested |
|  | UpdateBaseLineLink |  | To be tested |
|  | ExecuteLogicalDeleteByConditionBaseLineLink |  | To be tested |
|  | DeleteTargetBaseLineLink |  | To be tested |
|  | PatchQueryRelatedObjectsBaseLineLink |  | To be tested |
| 实体信息管理 | ShowAllDmEntityDataModelManagement | 获取所有数据实体的信息 | To be tested |
|  | ShowAllDmDataAndRelationshipEntityDataModelManagement | Get information about all data model and relationship entity | To be tested |
|  | SearchByNameEnDataModelManagement | 根据实体名称查询实体信息 | To be tested |
| 属性值与属性库关系表 | CountExaDefinitionLink |  | To be tested |
|  | DeleteExaDefinitionLink |  | To be tested |
|  | CompareVersionExaDefinitionLink |  | To be tested |
|  | UpdateByConditionExaDefinitionLink |  | To be tested |
|  | ExecuteLogicalDeleteExaDefinitionLink |  | To be tested |
|  | SaveAllExaDefinitionLink |  | To be tested |
|  | PatchGetExaDefinitionLink |  | To be tested |
|  | PatchQueryRelatedObjectsExaDefinitionLink |  | To be tested |
|  | PatchLogicalDeleteExaDefinitionLink |  | To be tested |
|  | DeleteTargetExaDefinitionLink |  | To be tested |
|  | ListTargetExaDefinitionLink |  | To be tested |
|  | PatchUpdateExaDefinitionLink |  | To be tested |
|  | ListHistoryDataExaDefinitionLink |  | To be tested |
|  | CreateExaDefinitionLink |  | To be tested |
| 属性库管理 | ShowExaDefinition |  | To be tested |
|  | CountExaDefinition |  | To be tested |
|  | PatchDeleteExaDefinition | 根据对象ID批量删除实例数据 | To be tested |
|  | ShowUsageByModelTypeusage | 根据入参查询对象的被模型引用情况 | To be tested |
|  | PatchCreateExaDefinition |  | To be tested |
|  | EnableExaDefinition |  | To be tested |
|  | ListExaDefinition |  | To be tested |
|  | UpdateByConditionExaDefinition |  | To be tested |
|  | CreateExaDefinition | 根据对象入参创建实例数据 | To be tested |
|  | CompareVersionExaDefinition |  | To be tested |
|  | ExecuteStatisticsHistoryDataExaDefinition |  | To be tested |
|  | ListExtendedAttributeReferedExaDefinition | 根据入参查询对象的被分类节点引用详情 | To be tested |
|  | DeleteExaDefinition |  | To be tested |
|  | DeleteByConditionExaDefinition |  | To be tested |
|  | AddTagExaDefinition |  | To be tested |
|  | CheckUniqueExaDefinition | 根据对象的唯一键校验唯一性 | To be tested |
|  | ExecuteSelectExaDefinition |  | To be tested |
|  | RemoveTagExaDefinition |  | To be tested |
|  | SaveAllExaDefinition |  | To be tested |
|  | SaveExaDefinition |  | To be tested |
|  | ExecuteGenerateBusinessCodeExaDefinition |  | To be tested |
|  | ListExadefinitionReferedExaDefinition | 根据入参查询对象的引用集合 | To be tested |
|  | ListTagExaDefinition |  | To be tested |
|  | SearchExaDefinition | 根据数据实体实例数据入参精确查询实例数据且支持分页 | To be tested |
|  | ListHistoryDataExaDefinition |  | To be tested |
| 搜索服务API | ExecuteSelectXDmSearchServDefineApiXdmSearchServDefineApi |  | To be tested |
|  | ListHistoryDataXdmSearchServDefineApi |  | To be tested |
|  | PatchGetXdmSearchServDefineApi |  | To be tested |
|  | ShowXDmSearchServDefineApiXdmSearchServDefineApi |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmSearchServDefineApi |  | To be tested |
|  | SearchXdmSearchServDefineApi |  | To be tested |
|  | SaveXdmSearchServDefineApi |  | To be tested |
|  | ListXDmSearchServDefineApiXdmSearchServDefineApi |  | To be tested |
|  | SaveAllXDmSearchServDefineApiXdmSearchServDefineApi |  | To be tested |
|  | UpdateByConditionXdmSearchServDefineApi |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmSearchServDefineApi |  | To be tested |
|  | PatchCreateXdmSearchServDefineApi |  | To be tested |
|  | PatchDeleteXdmSearchServDefineApi |  | To be tested |
|  | CountXDmSearchServDefineApiXdmSearchServDefineApi |  | To be tested |
| 搜索服务定义 | DeleteBranchXdmSearchServDefine |  | To be tested |
|  | UpdateStateXdmSearchServDefine |  | To be tested |
|  | ExecuteLogicalDeleteXDmSearchServDefineXdmSearchServDefine |  | To be tested |
|  | PatchCheckoutXdmSearchServDefine |  | To be tested |
|  | CheckoutAndUpdateXdmSearchServDefine |  | To be tested |
|  | PatchCheckinXdmSearchServDefine |  | To be tested |
|  | UpdateByConditionXdmSearchServDefine |  | To be tested |
|  | ShowAllVersionsXdmSearchServDefine |  | To be tested |
|  | CreateXDmSearchServDefineXdmSearchServDefine |  | To be tested |
|  | SaveAsXdmSearchServDefine |  | To be tested |
|  | PatchReviseXdmSearchServDefine |  | To be tested |
|  | PatchLogicalDeleteBranchXdmSearchServDefine |  | To be tested |
|  | UpdateAndCheckinXdmSearchServDefine |  | To be tested |
|  | CompareBusinessVersionXdmSearchServDefine |  | To be tested |
|  | ListXDmSearchServDefineXdmSearchServDefine |  | To be tested |
|  | ExecuteUndoCheckoutByAdminXdmSearchServDefine |  | To be tested |
|  | DisableXDmSearchServDefineXdmSearchServDefine |  | To be tested |
|  | PatchUpdateByAdminXdmSearchServDefine |  | To be tested |
|  | SwitchLifecycleTemplateXdmSearchServDefine |  | To be tested |
|  | SaveXdmSearchServDefine |  | To be tested |
|  | PatchReviseAndUpdateXdmSearchServDefine |  | To be tested |
|  | DeleteXDmSearchServDefineXdmSearchServDefine |  | To be tested |
|  | CountXDmSearchServDefineXdmSearchServDefine |  | To be tested |
|  | PatchUpdateAndCheckinXdmSearchServDefine |  | To be tested |
|  | ExecuteReviseXdmSearchServDefine |  | To be tested |
|  | ExecuteLogicalDeleteLatestVersionXdmSearchServDefine |  | To be tested |
|  | EnableXDmSearchServDefineXdmSearchServDefine |  | To be tested |
|  | PatchGetXdmSearchServDefine |  | To be tested |
|  | PatchCreateXdmSearchServDefine |  | To be tested |
|  | CheckoutXdmSearchServDefine |  | To be tested |
|  | CheckinXdmSearchServDefine |  | To be tested |
|  | PatchUpdateVersionXdmSearchServDefine |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmSearchServDefine |  | To be tested |
|  | ShowXDmSearchServDefineXdmSearchServDefine |  | To be tested |
|  | PatchDeleteBranchXdmSearchServDefine |  | To be tested |
| 搜索服务定义主人 | RemoveTagXdmSearchServDefineMaster |  | To be tested |
|  | ListTagXdmSearchServDefineMaster |  | To be tested |
|  | AddTagXdmSearchServDefineMaster |  | To be tested |
| 操作关系 | DeleteTargetXdmOperationRelation |  | To be tested |
|  | PatchQueryRelatedObjectsXdmOperationRelation |  | To be tested |
|  | PatchLogicalDeleteXDmOperationRelationXdmOperationRelation |  | To be tested |
|  | ExecuteSelectXDmOperationRelationXdmOperationRelation |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmOperationRelation |  | To be tested |
|  | DeleteXDmOperationRelationXdmOperationRelation |  | To be tested |
|  | UpdateByConditionXdmOperationRelation |  | To be tested |
|  | ListHistoryDataXdmOperationRelation |  | To be tested |
|  | ShowXDmOperationRelationXdmOperationRelation |  | To be tested |
|  | UpdateXdmOperationRelation |  | To be tested |
|  | CreateXDmOperationRelationXdmOperationRelation |  | To be tested |
|  | CountXDmOperationRelationXdmOperationRelation |  | To be tested |
|  | ListTargetXdmOperationRelation |  | To be tested |
|  | ExecuteStaticsXdmOperationRelation |  | To be tested |
|  | ListRelationshipXdmOperationRelation |  | To be tested |
|  | PatchUpdateXdmOperationRelation |  | To be tested |
|  | PatchCreateXdmOperationRelation |  | To be tested |
| 数据实体授权 | DeleteauthorizationEntity | 根据对象入参批量删除数据实体授权记录 | To be tested |
|  | ShowauthorizationEntity | 根据授权记录ID获取详细信息 | To be tested |
|  | Createauthorization | 根据对象入参创建数据实体授权记录 | To be tested |
|  | ListByPrincipalprincipal | 根据参与者及其他入参条件查询数据实体授权记录 | To be tested |
|  | Listauthorization | 根据对象入参查询数据实体授权记录 | To be tested |
| 数据实例授权 | ListauthorizationInstance | 根据数据实体ID和数据实例ID获取数据实例所有授权记录 | To be tested |
|  | Deleteauthorization | 根据对象入参批量删除数据实例授权记录 | To be tested |
|  | Showauthorization | 根据数据实体ID和数据实例ID获取数据实例所有授权记录 | To be tested |
|  | Updateauthorization | 根据对象入参更新数据实例授权记录 | To be tested |
| 数据实例鉴权 | CheckHasAccessAccessService | 判断用户对某条实例数据是否有权限,返回用户对该实例数据的鉴权结果 | To be tested |
|  | PatchHasAccessAccessService | 判断用户对批量实例数据是否有权限,返回用户对每条实例鉴权结果 | To be tested |
| 文件夹 | ShowParentFolder |  | To be tested |
|  | CompareVersionFolder |  | To be tested |
|  | DisableFolder |  | To be tested |
|  | RefreshFolder |  | To be tested |
|  | ShowByBusinessCodeFolder |  | To be tested |
|  | SearchFolder |  | To be tested |
|  | CountFolder |  | To be tested |
|  | ShowRootFolder |  | To be tested |
|  | ListFolder |  | To be tested |
|  | EnableFolder |  | To be tested |
|  | SaveFolder |  | To be tested |
|  | PatchRemoveChildNodeFolder |  | To be tested |
|  | ListFolderQuery |  | To be tested |
|  | PatchLogicalDeleteFolder |  | To be tested |
|  | PatchGetFolder |  | To be tested |
|  | ListHistoryDataFolder |  | To be tested |
|  | ShowAllParentListFolder |  | To be tested |
|  | PatchAddChildNodeFolder |  | To be tested |
|  | ExecuteStatisticsHistoryDataFolder |  | To be tested |
|  | ShowChildListFolder |  | To be tested |
|  | ExecuteGenerateBusinessCodeFolder |  | To be tested |
| 文件夹, folderedmgmt_folder | PatchDeleteFolder | 根据对象ID批量删除实例数据 | To be tested |
|  | UpdateFolder | 仅更新入参传入的字段信息,当ID不存在时,不处理传入的实例信息 | To be tested |
|  | CheckUniqueFolder | 根据对象的唯一键校验唯一性 | To be tested |
|  | ShowFolderTreeByName | 根据名称模糊查询文件夹,返回树形结构 | To be tested |
|  | DeleteFolder | 根据对象入参删除实例数据 | To be tested |
|  | PatchCreateFolder | 根据对象入参批量创建实例数据 | To be tested |
| 文件夹内容 | SaveFolderedLink |  | To be tested |
|  | CountFolderedLink |  | To be tested |
|  | SaveAllFolderedLink |  | To be tested |
|  | DeleteByConditionFolderedLink |  | To be tested |
|  | PatchGetFolderedLink |  | To be tested |
|  | SearchFolderedLink | 根据数据实体实例数据入参精确查询实例数据且支持分页 | To be tested |
|  | PatchLogicalDeleteFolderedLink |  | To be tested |
|  | UpdateByConditionFolderedLink |  | To be tested |
|  | CreateFolderedLink |  | To be tested |
|  | ExecuteLogicalDeleteByConditionFolderedLink |  | To be tested |
|  | ExecuteSelectFolderedLink |  | To be tested |
|  | PatchCreateFolderedLink |  | To be tested |
| 文件管理 | UploadLargeFileupload | 上传大文件 | To be tested |
|  | UploadFileupload | 上传小文件 | To be tested |
|  | RunScheduledJobsscheduledJobs | runScheduledJobs | To be tested |
|  | ExportInstanceDataByIdsfile | 根据对象入参导出实例数据 | To be tested |
|  | ExecuteImagesfile | 根据对象入参获取指定图片信息 | To be tested |
| 服务编排 | SaveAscustomservice | 自定义服务另存 | To be tested |
|  | CheckUniqueunique | 检验参数是否唯一 | To be tested |
|  | UpdateApiCenterInfoapicenterinfo | 更新API CENTER内容 | To be tested |
|  | DownloadSdksdk | 下载SDK | To be tested |
|  | Createcustomservice | 创建自定义服务 | To be tested |
|  | ListCustomservicelist | 查询自定义服务列表 | To be tested |
|  | ShowCustomSyncConfigcustomservice | 服务编排同步的配置信息 | To be tested |
|  | ListApiCenterNumberListapinumberQuery | 查询所有服务编排注册到API中心后的编码列表 | To be tested |
|  | Executeapi | 执行自定义服务 | To be tested |
|  | Offlineapinumber | 服务编排在API中心下线通知 | To be tested |
|  | ListHistorycustomservice | 通过主对象ID获取所有版本对象列表 | To be tested |
|  | ExecuteRevisecustomservice | 服务对象修订 | To be tested |
|  | PublishSinglecustomservice | 单个服务对象发布 | To be tested |
|  | DownloadSdkPlugincustomservice | 下载SDK插件 | To be tested |
|  | Publishcustomservice | 服务对象发布 | To be tested |
|  | ExecuteCompileJavaCodecustomservice | 编译Java代码 | To be tested |
|  | ListApiSimpleInfoListapicenterinfoQuery | 查询所有API中心简单信息列表 | To be tested |
|  | PatchPublishcustomservice | 服务编排批量发布 | To be tested |
| 权限 | PatchLogicalDeleteXDmPermissionXdmPermission |  | To be tested |
|  | CountXDmPermissionXdmPermission |  | To be tested |
|  | ListXDmPermissionXdmPermissionQuery |  | To be tested |
|  | CreateXDmPermissionXdmPermission |  | To be tested |
|  | ListHistoryDataXdmPermission |  | To be tested |
|  | DeleteXDmPermissionXdmPermission |  | To be tested |
|  | PatchDeleteXdmPermission |  | To be tested |
|  | SaveAllXDmPermissionXdmPermission |  | To be tested |
|  | CompareVersionXDmPermissionXdmPermission |  | To be tested |
|  | ExecuteLogicalDeleteXDmPermissionXdmPermission |  | To be tested |
|  | ExecuteStaticsXdmPermission |  | To be tested |
|  | SearchXdmPermission |  | To be tested |
|  | ShowXDmPermissionXdmPermission |  | To be tested |
|  | PatchCreateXdmPermission |  | To be tested |
| 权限分配 | ShowXDmPermissionAssignmentXdmPermissionAssignment |  | To be tested |
|  | CompareVersionXDmPermissionAssignmentXdmPermissionAssignment |  | To be tested |
|  | CreateXDmPermissionAssignmentXdmPermissionAssignment |  | To be tested |
|  | ListXDmPermissionAssignmentXdmPermissionAssignmentQuery |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmPermissionAssignment |  | To be tested |
|  | CountXDmPermissionAssignmentXdmPermissionAssignment |  | To be tested |
|  | ExecuteSelectXDmPermissionAssignmentXdmPermissionAssignment |  | To be tested |
|  | ListHistoryDataXdmPermissionAssignment |  | To be tested |
|  | PatchDeleteXdmPermissionAssignment |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmPermissionAssignment |  | To be tested |
|  | ExecuteStaticsXdmPermissionAssignment |  | To be tested |
|  | SearchXdmPermissionAssignment |  | To be tested |
|  | SaveXdmPermissionAssignment |  | To be tested |
|  | SaveAllXDmPermissionAssignmentXdmPermissionAssignment |  | To be tested |
|  | PatchUpdateXdmPermissionAssignment |  | To be tested |
| 权限操作 | SaveXdmPermissionOperation |  | To be tested |
|  | ListHistoryDataXdmPermissionOperation |  | To be tested |
|  | PatchUpdateXdmPermissionOperation |  | To be tested |
|  | PatchLogicalDeleteXDmPermissionOperationXdmPermissionOperation |  | To be tested |
|  | PatchDeleteXdmPermissionOperation |  | To be tested |
|  | PatchCreateXdmPermissionOperation |  | To be tested |
|  | CountXDmPermissionOperationXdmPermissionOperation |  | To be tested |
|  | DeleteXDmPermissionOperationXdmPermissionOperation |  | To be tested |
|  | UpdateByConditionXdmPermissionOperation |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmPermissionOperation |  | To be tested |
|  | ListXDmPermissionOperationXdmPermissionOperation |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmPermissionOperation |  | To be tested |
|  | ExecuteStaticsXdmPermissionOperation |  | To be tested |
|  | CreateXDmPermissionOperationXdmPermissionOperation |  | To be tested |
|  | ExecuteGenerateBusinessCodeXdmPermissionOperation |  | To be tested |
|  | ShowXDmPermissionOperationXdmPermissionOperation |  | To be tested |
| 权限管理功能与团队关系 | PatchUpdateXdmTeamAndFolderRelation |  | To be tested |
|  | ExecuteSelectXDmTeamAndFolderRelationXdmTeamAndFolderRelation |  | To be tested |
|  | PatchQueryRelatedObjectsXdmTeamAndFolderRelation |  | To be tested |
|  | ExecuteStaticsXdmTeamAndFolderRelation |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmTeamAndFolderRelation |  | To be tested |
|  | PatchCreateXdmTeamAndFolderRelation |  | To be tested |
|  | PatchDeleteXdmTeamAndFolderRelation |  | To be tested |
|  | PatchGetXdmTeamAndFolderRelation |  | To be tested |
|  | CountXDmTeamAndFolderRelationXdmTeamAndFolderRelation |  | To be tested |
|  | ListRelatedObjectsXdmTeamAndFolderRelation |  | To be tested |
|  | ShowXDmTeamAndFolderRelationXdmTeamAndFolderRelation |  | To be tested |
|  | CreateXDmTeamAndFolderRelationXdmTeamAndFolderRelation |  | To be tested |
|  | UpdateXdmTeamAndFolderRelation |  | To be tested |
|  | DeleteXDmTeamAndFolderRelationXdmTeamAndFolderRelation |  | To be tested |
|  | ListRelationshipXdmTeamAndFolderRelation |  | To be tested |
|  | SaveAllXDmTeamAndFolderRelationXdmTeamAndFolderRelation |  | To be tested |
| 权限管理功能与策略集关系 | DeleteTargetXdmFolderAndPolicySetRelation |  | To be tested |
|  | CountXDmFolderAndPolicySetRelationXdmFolderAndPolicySetRelation |  | To be tested |
|  | SearchXdmFolderAndPolicySetRelation |  | To be tested |
|  | PatchQueryRelatedObjectsXdmFolderAndPolicySetRelation |  | To be tested |
|  | ListRelationshipXdmFolderAndPolicySetRelation |  | To be tested |
|  | PatchGetXdmFolderAndPolicySetRelation |  | To be tested |
|  | PatchCreateXdmFolderAndPolicySetRelation |  | To be tested |
|  | ExecuteStaticsXdmFolderAndPolicySetRelation |  | To be tested |
|  | PatchDeleteXdmFolderAndPolicySetRelation |  | To be tested |
|  | DeleteByConditionXdmFolderAndPolicySetRelation |  | To be tested |
|  | ListRelatedObjectsXdmFolderAndPolicySetRelation |  | To be tested |
|  | ListXDmFolderAndPolicySetRelationXdmFolderAndPolicySetRelation |  | To be tested |
|  | SaveXdmFolderAndPolicySetRelation |  | To be tested |
| 标签 | ShowByNameCnTag |  | To be tested |
|  | CompareVersionTag |  | To be tested |
|  | DetachTagFromExaAttrtag | 移除扩展属性标签 | To be tested |
|  | ExecuteStaticsTag |  | To be tested |
|  | ListTag |  | To be tested |
|  | ListHistorytag | 根据对象入参分页查询满足条件的系统版本详细信息 | To be tested |
|  | ListtagQuery | 根据对象list属性查询对象且支持分页查询 | To be tested |
|  | PatchUpdateTag |  | To be tested |
|  | ExecuteStatisticsHistoryDataTag |  | To be tested |
|  | PatchDeleteTag |  | To be tested |
|  | SaveTag |  | To be tested |
|  | Createtag | 根据对象入参创建实例数据 | To be tested |
|  | PatchGetTag |  | To be tested |
|  | SaveAllTag |  | To be tested |
|  | CheckUniquetag | 根据对象的唯一键校验唯一性 | To be tested |
|  | ShowByNameEnTag |  | To be tested |
|  | AttachTagToExaAttrtag | 添加扩展属性标签 | To be tested |
|  | Deletetag | 根据对象入参删除实例数据 | To be tested |
| 标签与对象关系 | PatchCreateTagLink |  | To be tested |
|  | SaveAllTagLink |  | To be tested |
|  | SaveTagLink |  | To be tested |
|  | CountTagLink |  | To be tested |
|  | ExecuteStatisticsHistoryDataTagLink |  | To be tested |
|  | UpdateByConditionTagLink |  | To be tested |
|  | ListRelatedObjectsTagLink |  | To be tested |
|  | PatchLogicalDeleteTagLink |  | To be tested |
|  | ListTagLink |  | To be tested |
|  | CompareVersionTagLink |  | To be tested |
|  | UpdateTagLink |  | To be tested |
|  | DeleteTagLink |  | To be tested |
|  | DeleteByConditionTagLink |  | To be tested |
|  | SearchTagLink |  | To be tested |
|  | PatchGetTagLink |  | To be tested |
|  | ShowTagLink |  | To be tested |
|  | ExecuteLogicalDeleteByConditionTagLink |  | To be tested |
|  | DeleteTargetTagLink |  | To be tested |
| 标签分组 | Createtaggroup | 根据对象入参创建实例数据 | To be tested |
|  | SearchParentTreeByChildtaggroup | 根据标签分组名称模糊查询标签分组树子节点 | To be tested |
|  | SearchTagAndParentGroupTreetaggroup | 根据标签名称模糊查询标签分组树子节点 | To be tested |
|  | Listlist | 根据数据实体实例数据入参精确查询实例数据且支持分页 | To be tested |
|  | ListHistoryDataTagGroup |  | To be tested |
|  | CountTagGroup |  | To be tested |
|  | ShowParentTagGroup |  | To be tested |
|  | ShowRootTagGroup |  | To be tested |
|  | PatchAddChildNodeTagGroup |  | To be tested |
|  | ListTagGroupChildrentaggroup | 查询标签分组树子节点,只查询一层(带出其下的标签) | To be tested |
|  | SaveTagGroup |  | To be tested |
|  | CompareVersionTagGroup |  | To be tested |
|  | ShowByNameCnTagGroup |  | To be tested |
|  | PatchDeleteTagGroup |  | To be tested |
|  | ExecuteStatisticsHistoryDataTagGroup |  | To be tested |
|  | Showtaggroup | 根据对象ID获取对象详细信息 | To be tested |
|  | ShowChildListTagGroup |  | To be tested |
|  | ExecuteLogicalDeleteTagGroup |  | To be tested |
|  | ExecuteStaticsTagGroup |  | To be tested |
|  | PatchRemoveChildNodeTagGroup |  | To be tested |
|  | PatchCreateTagGroup |  | To be tested |
|  | ListtaggroupQuery | 根据对象list属性查询对象且支持分页查询 | To be tested |
|  | ListTagGroup |  | To be tested |
|  | PatchLogicalDeleteTagGroup |  | To be tested |
|  | ExecuteSelectTagGroup |  | To be tested |
|  | ListFullTreetaggroup | 根据租户id查询租户下的标签树 | To be tested |
|  | CheckUniquetaggroup | 根据对象的唯一键校验唯一性 | To be tested |
| 特征点 | UpdateByConditionXdmAspect |  | To be tested |
|  | UpdateXdmAspect |  | To be tested |
|  | PatchGetXdmAspect |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmAspect |  | To be tested |
|  | SearchXdmAspect |  | To be tested |
|  | SaveAllXDmAspectXdmAspect |  | To be tested |
|  | PatchUpdateXdmAspect |  | To be tested |
|  | CountXDmAspectXdmAspect |  | To be tested |
|  | DeleteByConditionXdmAspect |  | To be tested |
|  | PatchLogicalDeleteXDmAspectXdmAspect |  | To be tested |
|  | ListHistoryDataXdmAspect |  | To be tested |
|  | ShowXDmAspectXdmAspect |  | To be tested |
|  | PatchDeleteXdmAspect |  | To be tested |
|  | ExecuteStaticsXdmAspect |  | To be tested |
|  | PatchCreateXdmAspect |  | To be tested |
|  | DeleteXDmAspectXdmAspect |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmAspectXdmAspect |  | To be tested |
| 生命周期业务操作 | CreateLifecycleBusinessOperation | 根据对象入参创建实例数据 | To be tested |
|  | DeleteByConditionLifecycleBusinessOperation |  | To be tested |
|  | ExecuteLogicalDeleteByConditionLifecycleBusinessOperation |  | To be tested |
|  | CountLifecycleBusinessOperation |  | To be tested |
|  | SaveAllLifecycleBusinessOperation |  | To be tested |
|  | ListLifecycleBusinessOperationByTemplateId | 根据对象入参分页查询生命周期引用的业务操作 | To be tested |
|  | DisableLifecycleBusinessOperation | 根据对象ID失效对应实例数据,返回成功条目数据 | To be tested |
|  | PatchUpdateLifecycleBusinessOperation |  | To be tested |
|  | CompareVersionLifecycleBusinessOperation |  | To be tested |
|  | PatchDeleteLifecycleBusinessOperation |  | To be tested |
|  | ShowByBusinessCodeLifecycleBusinessOperation |  | To be tested |
|  | DeleteLifecycleBusinessOperation | 根据对象入参删除实例数据 | To be tested |
|  | ExecuteGenerateBusinessCodeLifecycleBusinessOperation |  | To be tested |
|  | ExecuteStaticsLifecycleBusinessOperation |  | To be tested |
|  | SearchLifecycleBusinessOperation |  | To be tested |
| 生命周期操作类型 | UpdateByConditionLifecycleOperation |  | To be tested |
|  | ExecuteSelectLifecycleOperation |  | To be tested |
|  | ExecuteStatisticsHistoryDataLifecycleOperation |  | To be tested |
|  | CountLifecycleOperation |  | To be tested |
|  | PatchGetLifecycleOperation |  | To be tested |
|  | SearchLifecycleOperation |  | To be tested |
|  | CompareVersionLifecycleOperation |  | To be tested |
|  | ListLifecycleOperationQuery |  | To be tested |
|  | ListHistoryDataLifecycleOperation |  | To be tested |
|  | ExecuteLogicalDeleteLifecycleOperation |  | To be tested |
|  | ExecuteLogicalDeleteByConditionLifecycleOperation |  | To be tested |
|  | SaveLifecycleOperation |  | To be tested |
|  | CreateLifecycleOperation |  | To be tested |
|  | ListLifecycleOperation |  | To be tested |
|  | ExecuteGenerateBusinessCodeLifecycleOperation |  | To be tested |
|  | ShowByBusinessCodeLifecycleOperation |  | To be tested |
|  | ExecuteStaticsLifecycleOperation |  | To be tested |
|  | ShowLifecycleOperation |  | To be tested |
|  | DeleteByConditionLifecycleOperation |  | To be tested |
| 生命周期模板 | ListLifecycleTemplate |  | To be tested |
|  | SaveAllLifecycleTemplate |  | To be tested |
|  | PatchReviseLifecycleTemplate |  | To be tested |
|  | ExecuteReviseAndUpdateLifecycleTemplate |  | To be tested |
|  | UpdateByAdminLifecycleTemplate | 更新主对象+版本对象入参传入的字段信 | To be tested |
|  | PatchCheckoutLifecycleTemplate |  | To be tested |
|  | PatchCheckoutAndUpdateLifecycleTemplate |  | To be tested |
|  | CheckUniqueLifecycleTemplate | 根据对象的唯一键校验唯一性 | To be tested |
|  | PatchUndoCheckoutByAdminLifecycleTemplate |  | To be tested |
|  | PatchUndoCheckoutLifecycleTemplate |  | To be tested |
|  | ExecuteLogicalDeleteByConditionLifecycleTemplate |  | To be tested |
|  | ExecuteLogicalDeleteLatestVersionLifecycleTemplate |  | To be tested |
|  | UpdateLifecycleInfoLifecycleTemplate | 更新运行态模型绑定的生命周期模板 | To be tested |
|  | UpdateLifecyclePhaseAndTemplateLifecycleTemplate |  | To be tested |
|  | ShowCreateAndUpdateTargetStateLifecycleTemplate |  | To be tested |
|  | PatchUpdateLifecycleTemplate |  | To be tested |
|  | UpdateLifecycleTemplate |  | To be tested |
|  | PatchDeleteBranchLifecycleTemplate |  | To be tested |
|  | PatchUpdateByAdminLifecycleTemplate |  | To be tested |
|  | SaveAsLifecycleTemplate |  | To be tested |
|  | ExecuteLogicalDeleteLifecycleTemplate |  | To be tested |
|  | PatchLogicalDeleteBranchLifecycleTemplate |  | To be tested |
|  | PatchReviseAndUpdateLifecycleTemplate |  | To be tested |
|  | UpdateByConditionLifecycleTemplate |  | To be tested |
|  | CompareVersionLifecycleTemplate |  | To be tested |
|  | CheckoutLifecycleTemplate |  | To be tested |
|  | DeleteLifecycleTemplate |  | To be tested |
|  | CountLifecycleTemplate |  | To be tested |
|  | PatchUpdateAndCheckinLifecycleTemplate |  | To be tested |
|  | PatchDeleteLifecycleTemplate |  | To be tested |
|  | ExecuteUndoCheckoutLifecycleTemplate |  | To be tested |
|  | EnableLifecycleTemplate | 根据对象ID生效对应实例数据,返回成功条目数据 | To be tested |
|  | DeleteByConditionLifecycleTemplate |  | To be tested |
|  | CompareBusinessVersionLifecycleTemplate |  | To be tested |
|  | ShowVersionByMasterLifecycleTemplate |  | To be tested |
|  | UpdateAndCheckinLifecycleTemplate |  | To be tested |
|  | ShowTargetPhaseAllLifecycleTemplate | 根据对象入参获取目标阶段信息列表 | To be tested |
|  | ListLifecycleInfoLifecycleTemplate | 查询运行态模型绑定的生命周期模板 | To be tested |
|  | ExecuteStatisticsHistoryDataLifecycleTemplate |  | To be tested |
| 生命周期模板与实体模型的关系 | ListTargetLifecycleTemplateLink |  | To be tested |
|  | ListLifecycleTemplateLink |  | To be tested |
|  | ListRelatedObjectsLifecycleTemplateLink |  | To be tested |
|  | ShowLifecycleTemplateLink |  | To be tested |
|  | ListHistoryDataLifecycleTemplateLink |  | To be tested |
|  | CreateLifecycleTemplateLink |  | To be tested |
|  | ExecuteSelectLifecycleTemplateLink |  | To be tested |
|  | PatchGetLifecycleTemplateLink |  | To be tested |
|  | PatchUpdateLifecycleTemplateLink |  | To be tested |
|  | UpdateByConditionLifecycleTemplateLink |  | To be tested |
|  | ExecuteLogicalDeleteLifecycleTemplateLink |  | To be tested |
|  | ExecuteStatisticsHistoryDataLifecycleTemplateLink |  | To be tested |
|  | PatchLogicalDeleteLifecycleTemplateLink |  | To be tested |
|  | SaveLifecycleTemplateLink |  | To be tested |
|  | SaveAllLifecycleTemplateLink |  | To be tested |
|  | SearchLifecycleTemplateLink |  | To be tested |
|  | PatchDeleteLifecycleTemplateLink |  | To be tested |
|  | PatchQueryRelatedObjectsLifecycleTemplateLink |  | To be tested |
|  | PatchCreateLifecycleTemplateLink |  | To be tested |
|  | ExecuteLogicalDeleteByConditionLifecycleTemplateLink |  | To be tested |
|  | DeleteByConditionLifecycleTemplateLink |  | To be tested |
| 生命周期状态 | ShowLifecycleState |  | To be tested |
|  | ShowAllLifecycleState | 获取所有生命周期状态 | To be tested |
|  | ExecuteLogicalDeleteLifecycleState |  | To be tested |
|  | UpdateByConditionLifecycleState |  | To be tested |
|  | DeleteByConditionLifecycleState |  | To be tested |
|  | SaveAllLifecycleState |  | To be tested |
|  | DeleteLifecycleState |  | To be tested |
|  | DisableLifecycleState | 根据对象ID失效对应实例数据,返回成功条目数据 | To be tested |
|  | CreateLifecycleState | 根据对象入参创建实例数据 | To be tested |
|  | ListLifecycleStateQuery |  | To be tested |
|  | DeleteLifecycleStateDelete | 根据对象入参删除实例数据 | To be tested |
|  | ListLifecycleStateRefered | 根据对象入参分页查询生命周期状态引用 | To be tested |
|  | PatchCreateLifecycleState |  | To be tested |
|  | CompareVersionLifecycleState |  | To be tested |
|  | ExecuteStaticsLifecycleState |  | To be tested |
|  | PatchUpdateLifecycleState |  | To be tested |
|  | ExecuteStatisticsHistoryDataLifecycleState |  | To be tested |
|  | PatchLogicalDeleteLifecycleState |  | To be tested |
|  | ListLifecycleState |  | To be tested |
|  | PatchGetLifecycleState |  | To be tested |
|  | ExecuteLogicalDeleteByConditionLifecycleState |  | To be tested |
| 生命周期阶段 | ExecuteSelectLifecyclePhase |  | To be tested |
|  | ExecuteStaticsLifecyclePhase |  | To be tested |
|  | PatchDeleteLifecyclePhase |  | To be tested |
|  | PatchLogicalDeleteLifecyclePhase |  | To be tested |
|  | ListLifecyclePhaseQuery |  | To be tested |
|  | SaveLifecyclePhase |  | To be tested |
|  | ExecuteStatisticsHistoryDataLifecyclePhase |  | To be tested |
|  | SaveAllLifecyclePhase |  | To be tested |
|  | UpdateLifecyclePhase |  | To be tested |
|  | PatchCreateLifecyclePhase |  | To be tested |
|  | ShowLifecyclePhase |  | To be tested |
|  | SearchLifecyclePhase |  | To be tested |
|  | CompareVersionLifecyclePhase |  | To be tested |
| 用户管理 | SaveXdmUser |  | To be tested |
|  | SaveAllXDmUserXdmUser |  | To be tested |
|  | ExecuteStaticsXdmUser |  | To be tested |
|  | PatchCreateXdmUser |  | To be tested |
|  | DeleteXDmUserXdmUser |  | To be tested |
|  | DeleteByConditionXdmUser |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmUserXdmUser |  | To be tested |
|  | ShowXDmUserXdmUser |  | To be tested |
|  | ExecuteSelectXDmUserXdmUser |  | To be tested |
|  | CreateXDmUserXdmUser |  | To be tested |
|  | ListHistoryDataXdmUser |  | To be tested |
|  | PatchLogicalDeleteXDmUserXdmUser |  | To be tested |
|  | UpdateByConditionXdmUser |  | To be tested |
|  | ListXDmUserXdmUser |  | To be tested |
|  | ListXDmUserXdmUserQuery |  | To be tested |
|  | PatchGetXdmUser |  | To be tested |
|  | CompareVersionXDmUserXdmUser |  | To be tested |
|  | ExecuteLogicalDeleteXDmUserXdmUser |  | To be tested |
| 用户组成员 | ListRelationshipXdmUserGroupMember |  | To be tested |
|  | SaveXdmUserGroupMember |  | To be tested |
|  | ExecuteLogicalDeleteXDmUserGroupMemberXdmUserGroupMember |  | To be tested |
|  | ShowXDmUserGroupMemberXdmUserGroupMember |  | To be tested |
|  | SearchXdmUserGroupMember |  | To be tested |
|  | ListXDmUserGroupMemberXdmUserGroupMember |  | To be tested |
|  | PatchCreateXdmUserGroupMember |  | To be tested |
|  | PatchGetXdmUserGroupMember |  | To be tested |
|  | DeleteByConditionXdmUserGroupMember |  | To be tested |
|  | ListRelatedObjectsXdmUserGroupMember |  | To be tested |
|  | ExecuteSelectXDmUserGroupMemberXdmUserGroupMember |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmUserGroupMember |  | To be tested |
|  | ExecuteStaticsXdmUserGroupMember |  | To be tested |
|  | CreateXDmUserGroupMemberXdmUserGroupMember |  | To be tested |
| 用户群组 | ListHistoryDataXdmUserGroup |  | To be tested |
|  | SaveAllXDmUserGroupXdmUserGroup |  | To be tested |
|  | UpdateByConditionXdmUserGroup |  | To be tested |
|  | ListXDmUserGroupXdmUserGroup |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmUserGroup |  | To be tested |
|  | SaveXdmUserGroup |  | To be tested |
|  | CompareVersionXDmUserGroupXdmUserGroup |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmUserGroupXdmUserGroup |  | To be tested |
|  | SearchXdmUserGroup |  | To be tested |
|  | PatchCreateXdmUserGroup |  | To be tested |
|  | ExecuteStaticsXdmUserGroup |  | To be tested |
|  | DeleteXDmUserGroupXdmUserGroup |  | To be tested |
|  | PatchGetXdmUserGroup |  | To be tested |
|  | PatchLogicalDeleteXDmUserGroupXdmUserGroup |  | To be tested |
|  | EnableXDmUserGroupXdmUserGroup |  | To be tested |
|  | ListXDmUserGroupXdmUserGroupQuery |  | To be tested |
| 租户 | PatchGetTenant |  | To be tested |
|  | SaveTenant |  | To be tested |
|  | ExecuteSelectTenant |  | To be tested |
|  | CreateTenant |  | To be tested |
|  | SearchTenant |  | To be tested |
|  | ShowTenant |  | To be tested |
|  | ExecuteStaticsTenant |  | To be tested |
|  | ListTenantQuery |  | To be tested |
|  | PatchUpdateTenant |  | To be tested |
|  | ShowByCodeTenant |  | To be tested |
|  | SaveAllTenant |  | To be tested |
|  | EnableTenant |  | To be tested |
|  | ExecuteStatisticsHistoryDataTenant |  | To be tested |
|  | ListHistoryDataTenant |  | To be tested |
|  | CompareVersionTenant |  | To be tested |
| 策略 | CreateXDmPolicyXdmPolicy |  | To be tested |
|  | SearchXdmPolicy |  | To be tested |
|  | PatchCreateXdmPolicy |  | To be tested |
|  | PatchGetXdmPolicy |  | To be tested |
|  | UpdateXdmPolicy |  | To be tested |
|  | SaveAllXDmPolicyXdmPolicy |  | To be tested |
|  | ShowXDmPolicyXdmPolicy |  | To be tested |
|  | DeleteXDmPolicyXdmPolicy |  | To be tested |
|  | ExecuteSelectXDmPolicyXdmPolicy |  | To be tested |
|  | PatchLogicalDeleteXDmPolicyXdmPolicy |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmPolicy |  | To be tested |
|  | ListHistoryDataXdmPolicy |  | To be tested |
| 策略集 | ShowParentXdmPolicySet |  | To be tested |
|  | DeleteXDmPolicySetXdmPolicySet |  | To be tested |
|  | ExecuteLogicalDeleteXDmPolicySetXdmPolicySet |  | To be tested |
|  | ListXDmPolicySetXdmPolicySetQuery |  | To be tested |
|  | ShowRootXdmPolicySet |  | To be tested |
|  | ShowByCodeXdmPolicySet |  | To be tested |
|  | PatchLogicalDeleteXDmPolicySetXdmPolicySet |  | To be tested |
|  | ShowAllParentListXdmPolicySet |  | To be tested |
|  | ShowXDmPolicySetXdmPolicySet |  | To be tested |
|  | PatchCreateXdmPolicySet |  | To be tested |
|  | CountXDmPolicySetXdmPolicySet |  | To be tested |
|  | PatchGetXdmPolicySet |  | To be tested |
|  | ShowChildListXdmPolicySet |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmPolicySetXdmPolicySet |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmPolicySet |  | To be tested |
|  | ExecuteGenerateBusinessCodeXdmPolicySet |  | To be tested |
|  | PatchRemoveChildNodeXdmPolicySet |  | To be tested |
|  | PatchAddChildNodeXdmPolicySet |  | To be tested |
| 类型定义 | DeleteByConditionTypeDefinition |  | To be tested |
|  | PatchRemoveChildNodeTypeDefinition |  | To be tested |
|  | ListTypeDefinitionQuery |  | To be tested |
|  | CountTypeDefinition |  | To be tested |
|  | SaveAllTypeDefinition |  | To be tested |
|  | SearchTypeDefinition | 根据数据实体实例数据入参精确查询实例数据且支持分页 | To be tested |
|  | PatchGetTypeDefinition |  | To be tested |
|  | ShowByEntityNumberTypeDefinition |  | To be tested |
|  | ExecuteGenerateBusinessCodeTypeDefinition |  | To be tested |
|  | PatchUpdateTypeDefinition |  | To be tested |
|  | PatchDeleteTypeDefinition |  | To be tested |
|  | ExecuteStatisticsHistoryDataTypeDefinition |  | To be tested |
|  | ListHistoryDataTypeDefinition |  | To be tested |
|  | UpdateTypeDefinition |  | To be tested |
|  | AddAttributeattribute | 根据对象入参添加属性 | To be tested |
|  | ShowAllParentListTypeDefinition |  | To be tested |
|  | ExecuteSelectTypeDefinition |  | To be tested |
|  | ShowRootTypeDefinition |  | To be tested |
|  | SearchAllExaAttributeTypeDefinition | 根据入参查询所有扩展属性集合 | To be tested |
|  | RefreshTypeDefinition |  | To be tested |
|  | CompareVersionTypeDefinition |  | To be tested |
|  | ExecuteLogicalDeleteTypeDefinition |  | To be tested |
| 类型定义模型继承关系 | DeleteTypeDefinitionInheritLink |  | To be tested |
|  | PatchDeleteTypeDefinitionInheritLink |  | To be tested |
|  | PatchUpdateTypeDefinitionInheritLink |  | To be tested |
|  | ListTypeDefinitionInheritLink |  | To be tested |
|  | UpdateTypeDefinitionInheritLink |  | To be tested |
|  | SearchTypeDefinitionInheritLink |  | To be tested |
|  | ListRelatedObjectsTypeDefinitionInheritLink |  | To be tested |
|  | ShowTypeDefinitionInheritLink |  | To be tested |
|  | ListTargetTypeDefinitionInheritLink |  | To be tested |
|  | CountTypeDefinitionInheritLink |  | To be tested |
|  | CompareVersionTypeDefinitionInheritLink |  | To be tested |
|  | PatchQueryRelatedObjectsTypeDefinitionInheritLink |  | To be tested |
|  | SaveTypeDefinitionInheritLink |  | To be tested |
|  | SaveAllTypeDefinitionInheritLink |  | To be tested |
|  | DeleteTargetTypeDefinitionInheritLink |  | To be tested |
|  | ListHistoryDataTypeDefinitionInheritLink |  | To be tested |
|  | ExecuteStaticsTypeDefinitionInheritLink |  | To be tested |
|  | PatchGetTypeDefinitionInheritLink |  | To be tested |
|  | PatchLogicalDeleteTypeDefinitionInheritLink |  | To be tested |
|  | ListRelationshipTypeDefinitionInheritLink |  | To be tested |
| 索引字段宽表 | PatchCreateXdmSearchColumnEntity |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmSearchColumnEntity |  | To be tested |
|  | DeleteXDmSearchColumnEntityXdmSearchColumnEntity |  | To be tested |
|  | DeleteByConditionXdmSearchColumnEntity |  | To be tested |
|  | PatchGetXdmSearchColumnEntity |  | To be tested |
|  | PatchDeleteXdmSearchColumnEntity |  | To be tested |
|  | ListXDmSearchColumnEntityXdmSearchColumnEntity |  | To be tested |
|  | CreateXDmSearchColumnEntityXdmSearchColumnEntity |  | To be tested |
|  | UpdateByConditionXdmSearchColumnEntity |  | To be tested |
|  | SaveXdmSearchColumnEntity |  | To be tested |
|  | PatchUpdateXdmSearchColumnEntity |  | To be tested |
|  | ExecuteSelectXDmSearchColumnEntityXdmSearchColumnEntity |  | To be tested |
|  | ShowXDmSearchColumnEntityXdmSearchColumnEntity |  | To be tested |
|  | ListHistoryDataXdmSearchColumnEntity |  | To be tested |
|  | CompareVersionXDmSearchColumnEntityXdmSearchColumnEntity |  | To be tested |
|  | ExecuteStaticsXdmSearchColumnEntity |  | To be tested |
| 维度属性映射模型 | SaveAllDimensionBaseAttr |  | To be tested |
|  | ExecuteLogicalDeleteByConditionDimensionBaseAttr |  | To be tested |
|  | ListHistoryDataDimensionBaseAttr |  | To be tested |
|  | UpdateDimensionBaseAttr |  | To be tested |
|  | ShowByDataModelNameDimensionBaseAttr |  | To be tested |
|  | PatchLogicalDeleteDimensionBaseAttr |  | To be tested |
|  | SearchDimensionBaseAttr |  | To be tested |
|  | ListDimensionBaseAttrQuery |  | To be tested |
|  | PatchCreateDimensionBaseAttr |  | To be tested |
|  | PatchUpdateDimensionBaseAttr |  | To be tested |
|  | UpdateByConditionDimensionBaseAttr |  | To be tested |
|  | ShowByInnerCodeDimensionBaseAttr |  | To be tested |
|  | CountDimensionBaseAttr |  | To be tested |
|  | DeleteDimensionBaseAttr |  | To be tested |
|  | ShowByDimensionModelNameDimensionBaseAttr |  | To be tested |
|  | SaveDimensionBaseAttr |  | To be tested |
|  | ShowDimensionBaseAttr |  | To be tested |
|  | PatchGetDimensionBaseAttr |  | To be tested |
|  | ExecuteStaticsDimensionBaseAttr |  | To be tested |
|  | ListDimensionBaseAttr |  | To be tested |
|  | ExecuteSelectDimensionBaseAttr |  | To be tested |
| 规则 | PatchGetXdmPolicyRule |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmPolicyRule |  | To be tested |
|  | ExecuteLogicalDeleteXDmPolicyRuleXdmPolicyRule |  | To be tested |
|  | PatchDeleteXdmPolicyRule |  | To be tested |
|  | ListXDmPolicyRuleXdmPolicyRuleQuery |  | To be tested |
|  | CompareVersionXDmPolicyRuleXdmPolicyRule |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmPolicyRuleXdmPolicyRule |  | To be tested |
|  | PatchLogicalDeleteXDmPolicyRuleXdmPolicyRule |  | To be tested |
|  | DeleteXDmPolicyRuleXdmPolicyRule |  | To be tested |
|  | CreateXDmPolicyRuleXdmPolicyRule |  | To be tested |
|  | SearchXdmPolicyRule |  | To be tested |
|  | ExecuteSelectXDmPolicyRuleXdmPolicyRule |  | To be tested |
|  | UpdateByConditionXdmPolicyRule |  | To be tested |
|  | DeleteByConditionXdmPolicyRule |  | To be tested |
|  | ShowXDmPolicyRuleXdmPolicyRule |  | To be tested |
| 角色 | SaveXdmRole |  | To be tested |
|  | DeleteXDmRoleXdmRole |  | To be tested |
|  | CreateXDmRoleXdmRole |  | To be tested |
|  | UpdateXdmRole |  | To be tested |
|  | ExecuteStatisticsHistoryDataXDmRoleXdmRole |  | To be tested |
|  | ListXdmRole |  | To be tested |
|  | UpdateByConditionXdmRole |  | To be tested |
|  | ExecuteStaticsXdmRole |  | To be tested |
|  | DeleteByConditionXdmRole |  | To be tested |
|  | SearchXdmRole |  | To be tested |
|  | EnableXDmRoleXdmRole |  | To be tested |
|  | ListXDmRoleXdmRoleQuery |  | To be tested |
|  | DisableXDmRoleXdmRole |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmRole |  | To be tested |
|  | CompareVersionXDmRoleXdmRole |  | To be tested |
|  | ExecuteLogicalDeleteXDmRoleXdmRole |  | To be tested |
| 角色成员 | CreateXDmRoleMemberXdmRoleMember |  | To be tested |
|  | UpdateByConditionXdmRoleMember |  | To be tested |
|  | PatchQueryRelatedObjectsXdmRoleMember |  | To be tested |
|  | ExecuteSelectXDmRoleMemberXdmRoleMember |  | To be tested |
|  | PatchDeleteXdmRoleMember |  | To be tested |
|  | PatchGetXdmRoleMember |  | To be tested |
|  | ShowXDmRoleMemberXdmRoleMember |  | To be tested |
|  | UpdateXdmRoleMember |  | To be tested |
|  | ExecuteLogicalDeleteByConditionXdmRoleMember |  | To be tested |
|  | DeleteByConditionXdmRoleMember |  | To be tested |
|  | DeleteXDmRoleMemberXdmRoleMember |  | To be tested |
|  | SearchXdmRoleMember |  | To be tested |
|  | PatchLogicalDeleteXDmRoleMemberXdmRoleMember |  | To be tested |
|  | PatchCreateXdmRoleMember |  | To be tested |
|  | DeleteTargetXdmRoleMember |  | To be tested |
| 计量单位 | DisableMeasuringUnit |  | To be tested |
|  | PatchUpdateMeasuringUnit |  | To be tested |
|  | CompareVersionMeasuringUnit |  | To be tested |
|  | ListHistoryDataMeasuringUnit |  | To be tested |
|  | PatchDeleteMeasuringUnit |  | To be tested |
|  | PatchLogicalDeleteMeasuringUnit |  | To be tested |
|  | DeleteMeasuringUnit |  | To be tested |
|  | ShowMeasuringUnit |  | To be tested |
|  | UpdateMeasuringUnit |  | To be tested |
|  | ExecuteLogicalDeleteMeasuringUnit |  | To be tested |
|  | EnableMeasuringUnit |  | To be tested |
|  | SaveMeasuringUnit |  | To be tested |
|  | ShowByBusinessCodeMeasuringUnit |  | To be tested |
|  | SaveAllMeasuringUnit |  | To be tested |
|  | ListMeasuringUnit |  | To be tested |
|  | ListMeasuringUnitQuery |  | To be tested |
