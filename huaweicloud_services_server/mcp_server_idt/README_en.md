# IDT MCP Server 


## Version
v0.1.0

## Overview

IDT MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IDT. Full-chain management of IDT resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Associated Model Graph Record | PatchUpdateXdmSearchServRelationLog |  | To be tested |
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
| Attribute Library Management | ShowExaDefinition |  | To be tested |
|  | CountExaDefinition |  | To be tested |
|  | PatchDeleteExaDefinition | Delete instance data in batches by object ID | To be tested |
|  | ShowUsageByModelTypeusage | Query the model reference status of an object based on the input parameter. | To be tested |
|  | PatchCreateExaDefinition |  | To be tested |
|  | EnableExaDefinition |  | To be tested |
|  | ListExaDefinition |  | To be tested |
|  | UpdateByConditionExaDefinition |  | To be tested |
|  | CreateExaDefinition | Creates instance data based on object input parameters. | To be tested |
|  | CompareVersionExaDefinition |  | To be tested |
|  | ExecuteStatisticsHistoryDataExaDefinition |  | To be tested |
|  | ListExtendedAttributeReferedExaDefinition | Query the reference details of the classified node of an object based on the input parameter. | To be tested |
|  | DeleteExaDefinition |  | To be tested |
|  | DeleteByConditionExaDefinition |  | To be tested |
|  | AddTagExaDefinition |  | To be tested |
|  | CheckUniqueExaDefinition | Verifies the uniqueness of an object based on the unique key of the object. | To be tested |
|  | ExecuteSelectExaDefinition |  | To be tested |
|  | RemoveTagExaDefinition |  | To be tested |
|  | SaveAllExaDefinition |  | To be tested |
|  | SaveExaDefinition |  | To be tested |
|  | ExecuteGenerateBusinessCodeExaDefinition |  | To be tested |
|  | ListExadefinitionReferedExaDefinition | Query the reference set of an object based on the input parameter. | To be tested |
|  | ListTagExaDefinition |  | To be tested |
|  | SearchExaDefinition | Query instance data based on the input parameters of the data entity instance and support pagination | To be tested |
|  | ListHistoryDataExaDefinition |  | To be tested |
| Classification management | ExecuteGenerateBusinessCodeClassificationNode |  | To be tested |
|  | SearchClassificationNode |  | To be tested |
|  | ListClassificationNodeQuery |  | To be tested |
|  | SearchAttributeattribute | Query category attributes by page | To be tested |
|  | UpdateClassificationNode | Updates only the field information transferred in the input parameter. If the ID does not exist, the transferred instance information is not processed. | To be tested |
|  | ShowCategoryNodeInfoClassificationNode | Obtain the attribute list of the category node. | To be tested |
|  | ShowRootClassificationNode |  | To be tested |
|  | DeleteClassificationNode | Delete instance data based on object input parameters. | To be tested |
|  | ExecuteLogicalDeleteByConditionClassificationNode |  | To be tested |
|  | ExecuteStatisticsHistoryDataClassificationNode |  | To be tested |
|  | ShowAllParentListClassificationNode |  | To be tested |
|  | ExecuteLogicalDeleteClassificationNode |  | To be tested |
|  | RefreshClassificationNode |  | To be tested |
|  | ShowChildrenClassificationNode | Obtain the subnode set under a specified category node. | To be tested |
|  | PatchUpdateClassificationNode |  | To be tested |
|  | CompareVersionClassificationNode |  | To be tested |
|  | ShowAttributesInfosClassificationNode | The data instance obtains node attributes and parent attribute nodes. | To be tested |
|  | PatchGetClassificationNode |  | To be tested |
|  | PatchCreateClassificationNode |  | To be tested |
|  | EnableClassificationNode | The instance data takes effect based on the object ID and the success entry data is returned. | To be tested |
|  | DisableClassificationNode | Deleting instance data based on object IDs and returning success data | To be tested |
|  | CountClassificationNode |  | To be tested |
|  | UpdateByConditionClassificationNode |  | To be tested |
|  | ShowParentClassificationNode |  | To be tested |
|  | ExecuteSelectClassificationNode |  | To be tested |
|  | CreateClassificationNode | Creates instance data based on object input parameters. | To be tested |
|  | ShowByBusinessCodeClassificationNode |  | To be tested |
|  | PatchRemoveChildNodeClassificationNode |  | To be tested |
|  | PatchDeleteClassificationNode |  | To be tested |
|  | ShowCategoryTreeByNameClassificationNode |  | To be tested |
|  | SearchParentAttributeparentAttribute | Query parent node attributes by page | To be tested |
| Classification node group | PatchUpdateClassificationNodeGroup |  | To be tested |
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
| Data Entity Authorization | DeleteauthorizationEntity | Delete data entity authorization records in batches based on object input parameters | To be tested |
|  | ShowauthorizationEntity | Obtain details based on the authorization record ID | To be tested |
|  | Createauthorization | Creates a data entity authorization record based on the object input parameters. | To be tested |
|  | ListByPrincipalprincipal | Query data entity authorization records based on the party and other input parameter conditions. | To be tested |
|  | Listauthorization | Query data entity authorization records based on object input parameters. | To be tested |
| Data Instance Authorization | ListauthorizationInstance | Obtains all authorization records of a data instance based on the data entity ID and data instance ID. | To be tested |
|  | Deleteauthorization | Delete data instance authorization records in batches based on object input parameters. | To be tested |
|  | Showauthorization | Obtains all authorization records of a data instance based on the data entity ID and data instance ID. | To be tested |
|  | Updateauthorization | Updates data instance authorization records based on object input parameters. | To be tested |
| Data instance authentication | CheckHasAccessAccessService | Check whether the user has the permission on an instance data record and return the authentication result of the instance data record. | To be tested |
|  | PatchHasAccessAccessService | Check whether the user has the permission to batch instance data and return the authentication result for each instance. | To be tested |
| Dimension attribute mapping model | SaveAllDimensionBaseAttr |  | To be tested |
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
| Entity information management | ShowAllDmEntityDataModelManagement | Obtain the information about all data entities. | To be tested |
|  | ShowAllDmDataAndRelationshipEntityDataModelManagement | Get information about all data model and relationship entity | To be tested |
|  | SearchByNameEnDataModelManagement | Query entity information based on the entity name | To be tested |
| Feature Point | UpdateByConditionXdmAspect |  | To be tested |
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
| File management | UploadLargeFileupload | Uploading a large file | To be tested |
|  | UploadFileupload | Upload small files | To be tested |
|  | RunScheduledJobsscheduledJobs | runScheduledJobs | To be tested |
|  | ExportInstanceDataByIdsfile | Export instance data based on object input parameters. | To be tested |
|  | ExecuteImagesfile | Obtain the specified image information based on the object input parameter. | To be tested |
| Folder | ShowParentFolder |  | To be tested |
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
| Folder Content | SaveFolderedLink |  | To be tested |
|  | CountFolderedLink |  | To be tested |
|  | SaveAllFolderedLink |  | To be tested |
|  | DeleteByConditionFolderedLink |  | To be tested |
|  | PatchGetFolderedLink |  | To be tested |
|  | SearchFolderedLink | Query instance data based on the input parameters of the data entity instance data. Pagination is supported. | To be tested |
|  | PatchLogicalDeleteFolderedLink |  | To be tested |
|  | UpdateByConditionFolderedLink |  | To be tested |
|  | CreateFolderedLink |  | To be tested |
|  | ExecuteLogicalDeleteByConditionFolderedLink |  | To be tested |
|  | ExecuteSelectFolderedLink |  | To be tested |
|  | PatchCreateFolderedLink |  | To be tested |
| Folder, folderedmgmt_folder | PatchDeleteFolder | Delete instance data in batches by object ID | To be tested |
|  | UpdateFolder | Updates only the field information transferred in the input parameter. If the ID does not exist, the transferred instance information is not processed. | To be tested |
|  | CheckUniqueFolder | Verify the uniqueness of an object based on the unique key of the object. | To be tested |
|  | ShowFolderTreeByName | Query a folder by name and return the tree structure | To be tested |
|  | DeleteFolder | Delete instance data based on object input parameters. | To be tested |
|  | PatchCreateFolder | Creates instance data in batches based on object input parameters. | To be tested |
| Global API | RunGlobalSystemManagement | This API is used to manage system management APIs. | To be tested |
|  | RunGlobalApiPageInfo | This API is used to query information about data entities and relationship entities by page. | To be tested |
|  | RunGlobalApi | This API is used to manage all data and relationship entities. | To be tested |
| Index Field Wide Table | PatchCreateXdmSearchColumnEntity |  | To be tested |
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
| Label | ShowByNameCnTag |  | To be tested |
|  | CompareVersionTag |  | To be tested |
|  | DetachTagFromExaAttrtag | Remove an extended attribute tag. | To be tested |
|  | ExecuteStaticsTag |  | To be tested |
|  | ListTag |  | To be tested |
|  | ListHistorytag | Query system version details that meet the search criteria based on the object input parameter in pagination mode | To be tested |
|  | ListtagQuery | Query objects based on the object list attribute. Pagination query is supported. | To be tested |
|  | PatchUpdateTag |  | To be tested |
|  | ExecuteStatisticsHistoryDataTag |  | To be tested |
|  | PatchDeleteTag |  | To be tested |
|  | SaveTag |  | To be tested |
|  | Createtag | Creates instance data based on object input parameters. | To be tested |
|  | PatchGetTag |  | To be tested |
|  | SaveAllTag |  | To be tested |
|  | CheckUniquetag | Verify the uniqueness of an object based on the unique key of the object. | To be tested |
|  | ShowByNameEnTag |  | To be tested |
|  | AttachTagToExaAttrtag | Adding an extended attribute tag | To be tested |
|  | Deletetag | Delete instance data based on object input parameters. | To be tested |
| Label Group | Createtaggroup | Creates instance data based on object input parameters. | To be tested |
|  | SearchParentTreeByChildtaggroup | Query subnodes in the label group tree based on the label group name | To be tested |
|  | SearchTagAndParentGroupTreetaggroup | Query subnodes in the label group tree based on the label name | To be tested |
|  | Listlist | Query instance data based on the input parameters of the data entity instance data. Pagination is supported. | To be tested |
|  | ListHistoryDataTagGroup |  | To be tested |
|  | CountTagGroup |  | To be tested |
|  | ShowParentTagGroup |  | To be tested |
|  | ShowRootTagGroup |  | To be tested |
|  | PatchAddChildNodeTagGroup |  | To be tested |
|  | ListTagGroupChildrentaggroup | Query the subnodes in the label group tree. Only one layer (with the tags under the node) is queried. | To be tested |
|  | SaveTagGroup |  | To be tested |
|  | CompareVersionTagGroup |  | To be tested |
|  | ShowByNameCnTagGroup |  | To be tested |
|  | PatchDeleteTagGroup |  | To be tested |
|  | ExecuteStatisticsHistoryDataTagGroup |  | To be tested |
|  | Showtaggroup | Obtains object details based on the object ID. | To be tested |
|  | ShowChildListTagGroup |  | To be tested |
|  | ExecuteLogicalDeleteTagGroup |  | To be tested |
|  | ExecuteStaticsTagGroup |  | To be tested |
|  | PatchRemoveChildNodeTagGroup |  | To be tested |
|  | PatchCreateTagGroup |  | To be tested |
|  | ListtaggroupQuery | Query objects based on the object list attribute. Pagination query is supported. | To be tested |
|  | ListTagGroup |  | To be tested |
|  | PatchLogicalDeleteTagGroup |  | To be tested |
|  | ExecuteSelectTagGroup |  | To be tested |
|  | ListFullTreetaggroup | Query the tag tree of a tenant based on the tenant ID. | To be tested |
|  | CheckUniquetaggroup | Verifies the uniqueness of an object based on the unique key of the object. | To be tested |
| Life cycle status | ShowLifecycleState |  | To be tested |
|  | ShowAllLifecycleState | Obtains all life cycle states. | To be tested |
|  | ExecuteLogicalDeleteLifecycleState |  | To be tested |
|  | UpdateByConditionLifecycleState |  | To be tested |
|  | DeleteByConditionLifecycleState |  | To be tested |
|  | SaveAllLifecycleState |  | To be tested |
|  | DeleteLifecycleState |  | To be tested |
|  | DisableLifecycleState | Deleting instance data based on object IDs and returning success data | To be tested |
|  | CreateLifecycleState | Creates instance data based on object input parameters. | To be tested |
|  | ListLifecycleStateQuery |  | To be tested |
|  | DeleteLifecycleStateDelete | Delete instance data based on the object input parameter. | To be tested |
|  | ListLifecycleStateRefered | Query the life cycle status reference based on the object input parameter in pagination mode | To be tested |
|  | PatchCreateLifecycleState |  | To be tested |
|  | CompareVersionLifecycleState |  | To be tested |
|  | ExecuteStaticsLifecycleState |  | To be tested |
|  | PatchUpdateLifecycleState |  | To be tested |
|  | ExecuteStatisticsHistoryDataLifecycleState |  | To be tested |
|  | PatchLogicalDeleteLifecycleState |  | To be tested |
|  | ListLifecycleState |  | To be tested |
|  | PatchGetLifecycleState |  | To be tested |
|  | ExecuteLogicalDeleteByConditionLifecycleState |  | To be tested |
| Lifecycle Business Operation | CreateLifecycleBusinessOperation | Creates instance data based on object input parameters. | To be tested |
|  | DeleteByConditionLifecycleBusinessOperation |  | To be tested |
|  | ExecuteLogicalDeleteByConditionLifecycleBusinessOperation |  | To be tested |
|  | CountLifecycleBusinessOperation |  | To be tested |
|  | SaveAllLifecycleBusinessOperation |  | To be tested |
|  | ListLifecycleBusinessOperationByTemplateId | Query the business operations referenced by the life cycle based on the object input parameter in pagination mode | To be tested |
|  | DisableLifecycleBusinessOperation | The instance data corresponding to the object ID is invalidated and the success entry data is returned. | To be tested |
|  | PatchUpdateLifecycleBusinessOperation |  | To be tested |
|  | CompareVersionLifecycleBusinessOperation |  | To be tested |
|  | PatchDeleteLifecycleBusinessOperation |  | To be tested |
|  | ShowByBusinessCodeLifecycleBusinessOperation |  | To be tested |
|  | DeleteLifecycleBusinessOperation | Delete instance data based on the object input parameter. | To be tested |
|  | ExecuteGenerateBusinessCodeLifecycleBusinessOperation |  | To be tested |
|  | ExecuteStaticsLifecycleBusinessOperation |  | To be tested |
|  | SearchLifecycleBusinessOperation |  | To be tested |
| Lifecycle Phase | ExecuteSelectLifecyclePhase |  | To be tested |
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
| Lifecycle Template | ListLifecycleTemplate |  | To be tested |
|  | SaveAllLifecycleTemplate |  | To be tested |
|  | PatchReviseLifecycleTemplate |  | To be tested |
|  | ExecuteReviseAndUpdateLifecycleTemplate |  | To be tested |
|  | UpdateByAdminLifecycleTemplate | Update the input parameter of the main object and version object. | To be tested |
|  | PatchCheckoutLifecycleTemplate |  | To be tested |
|  | PatchCheckoutAndUpdateLifecycleTemplate |  | To be tested |
|  | CheckUniqueLifecycleTemplate | Verify the uniqueness of an object based on the unique key of the object. | To be tested |
|  | PatchUndoCheckoutByAdminLifecycleTemplate |  | To be tested |
|  | PatchUndoCheckoutLifecycleTemplate |  | To be tested |
|  | ExecuteLogicalDeleteByConditionLifecycleTemplate |  | To be tested |
|  | ExecuteLogicalDeleteLatestVersionLifecycleTemplate |  | To be tested |
|  | UpdateLifecycleInfoLifecycleTemplate | Updates the life cycle template bound to the running model | To be tested |
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
|  | EnableLifecycleTemplate | The instance data takes effect based on the object ID and the success entry data is returned. | To be tested |
|  | DeleteByConditionLifecycleTemplate |  | To be tested |
|  | CompareBusinessVersionLifecycleTemplate |  | To be tested |
|  | ShowVersionByMasterLifecycleTemplate |  | To be tested |
|  | UpdateAndCheckinLifecycleTemplate |  | To be tested |
|  | ShowTargetPhaseAllLifecycleTemplate | Obtain the target phase information list based on the object input parameters. | To be tested |
|  | ListLifecycleInfoLifecycleTemplate | Query the life cycle template bound to the running model | To be tested |
|  | ExecuteStatisticsHistoryDataLifecycleTemplate |  | To be tested |
| Lifecycle operation type | UpdateByConditionLifecycleOperation |  | To be tested |
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
| Linkx synchronization task | PatchUpdateLinkxSyncTask |  | To be tested |
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
| Operation Relationship | DeleteTargetXdmOperationRelation |  | To be tested |
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
| Party relationship operation history | CompareVersionXDmPrincipalRelationOperationHistory |  | To be tested |
|  | PatchLogicalDeleteXDmPrincipalRelationOperationHistory |  | To be tested |
|  | ExecuteStaticsXdmPrincipalRelationOperationHistory |  | To be tested |
|  | SaveXdmPrincipalRelationOperationHistory |  | To be tested |
|  | ListHistoryDataXdmPrincipalRelationOperationHistory |  | To be tested |
|  | UpdateXdmPrincipalRelationOperationHistory |  | To be tested |
|  | PatchCreateXdmPrincipalRelationOperationHistory |  | To be tested |
|  | SearchXdmPrincipalRelationOperationHistory |  | To be tested |
| Permission | PatchLogicalDeleteXDmPermissionXdmPermission |  | To be tested |
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
| Permission operation | SaveXdmPermissionOperation |  | To be tested |
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
| Policy | CreateXDmPolicyXdmPolicy |  | To be tested |
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
| Policy Set | ShowParentXdmPolicySet |  | To be tested |
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
| Relationship between labels and objects | PatchCreateTagLink |  | To be tested |
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
| Relationship between life cycle templates and entity models | ListTargetLifecycleTemplateLink |  | To be tested |
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
| Relationship between teams and team roles | PatchDeleteXdmTeamAndTeamRoleRelation |  | To be tested |
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
| Relationship between the baseline object and the baseline object | SaveAllBaseLineLink |  | To be tested |
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
| Relationship between the permission management function and policy set | DeleteTargetXdmFolderAndPolicySetRelation |  | To be tested |
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
| Relationship between the permission management function and the team | PatchUpdateXdmTeamAndFolderRelation |  | To be tested |
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
| Relationship table between attribute values and attribute libraries | CountExaDefinitionLink |  | To be tested |
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
| Relationships between roles and members in the team | DeleteTargetXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | PatchDeleteXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | ExecuteLogicalDeleteXDmTeamAndTeamRoleRelationMember |  | To be tested |
|  | PatchQueryRelatedObjectsXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | SearchXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | PatchUpdateXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | ListRelationshipXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | ListTargetXdmTeamAndTeamRoleRelationMember |  | To be tested |
|  | PatchLogicalDeleteXDmTeamAndTeamRoleRelationMember |  | To be tested |
|  | PatchGetXdmTeamAndTeamRoleRelationMember |  | To be tested |
| Right Assignment | ShowXDmPermissionAssignmentXdmPermissionAssignment |  | To be tested |
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
| Role | SaveXdmRole |  | To be tested |
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
| Role Member | CreateXDmRoleMemberXdmRoleMember |  | To be tested |
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
| Rule | PatchGetXdmPolicyRule |  | To be tested |
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
| Search Service Definition | DeleteBranchXdmSearchServDefine |  | To be tested |
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
| Search service API | ExecuteSelectXDmSearchServDefineApiXdmSearchServDefineApi |  | To be tested |
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
| Search service definition owner | RemoveTagXdmSearchServDefineMaster |  | To be tested |
|  | ListTagXdmSearchServDefineMaster |  | To be tested |
|  | AddTagXdmSearchServDefineMaster |  | To be tested |
| Service Orchestration | SaveAscustomservice | Save the user-defined service as | To be tested |
|  | CheckUniqueunique | Check whether the parameter is unique | To be tested |
|  | UpdateApiCenterInfoapicenterinfo | Updating the API CENTER content | To be tested |
|  | DownloadSdksdk | Download SDK | To be tested |
|  | Createcustomservice | Create a custom service | To be tested |
|  | ListCustomservicelist | Query the user-defined service list | To be tested |
|  | ShowCustomSyncConfigcustomservice | Configuration information about service orchestration synchronization | To be tested |
|  | ListApiCenterNumberListapinumberQuery | Query the code list after all service orchestrations are registered with the API Center. | To be tested |
|  | Executeapi | Executing a Customized Service | To be tested |
|  | Offlineapinumber | Service Orchestration Service Offline Notification in API Center | To be tested |
|  | ListHistorycustomservice | Obtain the list of all version objects based on the main object ID. | To be tested |
|  | ExecuteRevisecustomservice | Service Object Revision | To be tested |
|  | PublishSinglecustomservice | Release a single service object | To be tested |
|  | DownloadSdkPlugincustomservice | Download the SDK plug-in | To be tested |
|  | Publishcustomservice | Release the service object | To be tested |
|  | ExecuteCompileJavaCodecustomservice | Compiling Java code | To be tested |
|  | ListApiSimpleInfoListapicenterinfoQuery | Query the simple information list of all API Center | To be tested |
|  | PatchPublishcustomservice | Service Orchestration and Batch Release | To be tested |
| Team | ExecuteSelectXDmTeamXdmTeam |  | To be tested |
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
| Team Role | DisableXDmTeamRoleXdmTeamRole |  | To be tested |
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
| Tenant | PatchGetTenant |  | To be tested |
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
| Type definition | DeleteByConditionTypeDefinition |  | To be tested |
|  | PatchRemoveChildNodeTypeDefinition |  | To be tested |
|  | ListTypeDefinitionQuery |  | To be tested |
|  | CountTypeDefinition |  | To be tested |
|  | SaveAllTypeDefinition |  | To be tested |
|  | SearchTypeDefinition | Query instance data based on the input parameters of the data entity instance. Pagination is supported. | To be tested |
|  | PatchGetTypeDefinition |  | To be tested |
|  | ShowByEntityNumberTypeDefinition |  | To be tested |
|  | ExecuteGenerateBusinessCodeTypeDefinition |  | To be tested |
|  | PatchUpdateTypeDefinition |  | To be tested |
|  | PatchDeleteTypeDefinition |  | To be tested |
|  | ExecuteStatisticsHistoryDataTypeDefinition |  | To be tested |
|  | ListHistoryDataTypeDefinition |  | To be tested |
|  | UpdateTypeDefinition |  | To be tested |
|  | AddAttributeattribute | Add an attribute based on the object input parameter. | To be tested |
|  | ShowAllParentListTypeDefinition |  | To be tested |
|  | ExecuteSelectTypeDefinition |  | To be tested |
|  | ShowRootTypeDefinition |  | To be tested |
|  | SearchAllExaAttributeTypeDefinition | Query all extended attribute sets based on input parameters. | To be tested |
|  | RefreshTypeDefinition |  | To be tested |
|  | CompareVersionTypeDefinition |  | To be tested |
|  | ExecuteLogicalDeleteTypeDefinition |  | To be tested |
| Type definition model inheritance relationship | DeleteTypeDefinitionInheritLink |  | To be tested |
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
| UOM | DisableMeasuringUnit |  | To be tested |
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
| Unit Type | PatchLogicalDeleteUnitType |  | To be tested |
|  | UpdateByConditionUnitType |  | To be tested |
|  | EnableUnitType | The instance data takes effect based on the object ID and the success entry data is returned. | To be tested |
|  | ExecuteLogicalDeleteUnitType |  | To be tested |
|  | ListAllUnitTypeNameList | Query the unit type list based on the object input parameter. | To be tested |
|  | SaveUnitType |  | To be tested |
|  | CompareVersionUnitType |  | To be tested |
|  | ListHistoryDataUnitType |  | To be tested |
|  | SaveAllUnitType |  | To be tested |
|  | ExecuteSelectUnitType |  | To be tested |
|  | ListUnitTypeQuery | Query the object list attribute based on the object input parameters and pagination is supported. | To be tested |
|  | CountUnitType |  | To be tested |
|  | DeleteUnitType | Delete instance data based on object input parameters. | To be tested |
|  | CreateUnitType | Create instance data in batches based on the input parameters of the object. | To be tested |
|  | PatchGetUnitType |  | To be tested |
|  | ListUnitType |  | To be tested |
|  | ShowByBusinessCodeUnitType |  | To be tested |
|  | UpdateUnitType | Only the field information transferred in the input parameter is updated. If the ID does not exist, the transferred instance information is not processed. | To be tested |
|  | ExecuteGenerateBusinessCodeUnitType |  | To be tested |
|  | DeleteByConditionUnitType |  | To be tested |
| User group | ListHistoryDataXdmUserGroup |  | To be tested |
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
| User group member | ListRelationshipXdmUserGroupMember |  | To be tested |
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
| User management | SaveXdmUser |  | To be tested |
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
| Valid value | PatchGetLegalValue |  | To be tested |
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
| Valid value type | ShowLegalValueType |  | To be tested |
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
| XDM Baseline Object | ListHistoryDataBaseLine |  | To be tested |
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
| XDM permission attribute | PatchGetXdmPermissionAttribute |  | To be tested |
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

