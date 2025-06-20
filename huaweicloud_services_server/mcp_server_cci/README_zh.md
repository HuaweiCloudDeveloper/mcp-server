# CCI MCP Server 

## 版本信息
v0.1.0

## 产品描述

CCI MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CCI交互的能力。可以基于自然语言对CCI资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| API groups | getCrdYangtseCniAPIGroup | 查询APIGroup /apis/crd.yangtse.cni | To be tested |
|  | getBatchVolcanoShV1alpha1APIResources | 查询所有batch.volcano.sh/v1alpha1的API | To be tested |
|  | getBatchAPIGroup | 查询APIGroup /apis/batch | To be tested |
|  | getRbacAuthorizationAPIGroup | get information of a group | To be tested |
|  | getBatchV1beta1APIResources | get available resources | To be tested |
|  | getBatchVolcanoShAPIGroup | 查询APIGroup /apis/batch.volcano.sh | To be tested |
|  | getCoreAPIVersions | get available API versions | To be tested |
|  | getExtensionsAPIGroup | 查询APIGroup /apis/extensions | To be tested |
|  | getAPIVersions | get available API versions | To be tested |
|  | getMetricsAPIGroup | 查询APIGroup /apis/metrics.k8s.io | To be tested |
|  | getRbacAuthorizationV1APIResources | get available resources | To be tested |
|  | getMetricsV1beta1APIResources | get available resources | To be tested |
|  | getCoreV1APIResources | get available resources | To be tested |
|  | getNetworkingCciIoAPIGroup | 查询APIGroup /apis/networking.cci.io | To be tested |
|  | getCrdYangtseCniV1APIResources | 查询所有crd.yangtse.cni/v1的API | To be tested |
|  | getExtensionsV1beta1APIResources | get available resources | To be tested |
|  | getNetworkingCciIoV1beta1APIResources | get available resources | To be tested |
|  | getBatchV1APIResources | get available resources | To be tested |
|  | getAppsV1APIResources | get available resources | To be tested |
|  | getAppsAPIGroup | 查询APIGroup /apis/apps | To be tested |
| ClusterRole | listRbacAuthorizationV1ClusterRole | This API is used to list or watch objects of kind ClusterRole | To be tested |
|  | readRbacAuthorizationV1ClusterRole | This API is used to read the specified ClusterRole | To be tested |
| ConfigMap | listCoreV1NamespacedConfigMap | 查询Namespace下所有ConfigMap的详细信息。 | To be tested |
|  | readCoreV1NamespacedConfigMap | 查询ConfigMap详细信息。 | To be tested |
|  | deleteCoreV1NamespacedConfigMap | 删除ConfigMap。 | To be tested |
|  | patchCoreV1NamespacedConfigMap | 更新ConfigMap。 | To be tested |
|  | replaceCoreV1NamespacedConfigMap | 替换ConfigMap。 | To be tested |
|  | deleteCoreV1CollectionNamespacedConfigMap | 删除Namespace下所有ConfigMap。 | To be tested |
|  | createCoreV1NamespacedConfigMap | 创建ConfigMap。 | To be tested |
| CronJob | listBatchV1beta1CronJobForAllNamespaces | 查询所有namespace下所有CronJob的详细信息。 | To be tested |
| Deployment | readAppsV1NamespacedDeployment | 查询Deployment的详细信息。 | To be tested |
|  | createAppsV1NamespacedDeployment | 创建一个Deployment。 | To be tested |
|  | listAppsV1DeploymentForAllNamespaces | 查询用户所有Deployment。 | To be tested |
|  | readAppsV1NamespacedDeploymentStatus | 查询Deployment的状态。 | To be tested |
|  | patchAppsV1NamespacedDeployment | 更新Deployment。 | To be tested |
|  | readAppsV1NamespacedDeploymentScale | 查询Deployment的伸缩操作 | To be tested |
|  | listAppsV1NamespacedDeployment | 查询Namespace下所有Deployment的详细信息。 | To be tested |
|  | deleteAppsV1NamespacedDeployment | 删除Deployment。 | To be tested |
|  | patchAppsV1NamespacedDeploymentScale | This API is used to partially update scale of the specified Scale. | To be tested |
|  | replaceAppsV1NamespacedDeployment | 替换Deployment。 | To be tested |
|  | deleteAppsV1CollectionNamespacedDeployment | 删除Namespace下所有Deployment。 | To be tested |
|  | replaceAppsV1NamespacedDeploymentScale | This API is used to replace scale of the specified Scale. | To be tested |
| EIPPool | deleteCrdYangtseCniV1NamespacedEIPPool | 删除指定的EIPPool。 | To be tested |
|  | readCrdYangtseCniV1NamespacedEIPPoolStatus | 查询指定的EIPPool的详细信息。 | To be tested |
|  | readCrdYangtseCniV1NamespacedEIPPool | 查询指定的EIPPool的详细信息。 | To be tested |
|  | patchCrdYangtseCniV1NamespacedEIPPool | 更新EIPPool。 | To be tested |
|  | listCrdYangtseCniV1NamespacedEIPPool | 查询指定namespace下所有EIPPool的详细信息。 | To be tested |
|  | createCrdYangtseCniV1NamespacedEIPPool | 创建EIPPool。 | To be tested |
|  | replaceCrdYangtseCniV1NamespacedEIPPool | 替换EIPPool。 | To be tested |
| Endpoint | createCoreV1NamespacedEndpoints | 创建Endpoint。 | To be tested |
|  | listCoreV1NamespacedEndpoints | 查询Namespace下所有Endpoints。 | To be tested |
|  | replaceCoreV1NamespacedEndpoints | 替换Endpoint。 | To be tested |
|  | readCoreV1NamespacedEndpoints | 查询Endpoint。 | To be tested |
|  | patchCoreV1NamespacedEndpoints | 更新Endpoint。 | To be tested |
|  | deleteCoreV1NamespacedEndpoints | 删除Endpoint。 | To be tested |
| Event | deleteCoreV1NamespacedEvent | 删除Event。 | To be tested |
|  | readCoreV1NamespacedEvent | 查询Event详细信息。 | To be tested |
|  | listCoreV1NamespacedEvent | 查询Namespace下所有Event的详细信息。 | To be tested |
| Ingress | readExtensionsV1beta1NamespacedIngressStatus | 查询Ingress状态。 | To be tested |
|  | readExtensionsV1beta1NamespacedIngress | 查询Ingress的详细信息。 | To be tested |
|  | deleteExtensionsV1beta1NamespacedIngress | 删除Ingress。 | To be tested |
|  | deleteExtensionsV1beta1CollectionNamespacedIngress | 删除Namespace下所有Ingress。 | To be tested |
|  | listExtensionsV1beta1NamespacedIngress | 查询Namespace下所有Ingress的详细信息。 | To be tested |
|  | patchExtensionsV1beta1NamespacedIngress | 更新Ingress。 | To be tested |
|  | createExtensionsV1beta1NamespacedIngress | 创建Ingress,使用http协议,关联的后端Service为“redis:8080”,使用ELB作为Ingress控制器,ELB的ip为192.168.137.182,端口号为6071。 | To be tested |
|  | replaceExtensionsV1beta1NamespacedIngress | 替换Ingress。 | To be tested |
| Job | readBatchV1NamespacedJobStatus | 查询Job状态。 | To be tested |
|  | deleteBatchV1CollectionNamespacedJob | 删除Namespace下所有Job。 | To be tested |
|  | createBatchV1NamespacedJob | 创建Job。 | To be tested |
|  | listBatchV1NamespacedJob | 查询Namespace下所有Job的详细信息。 | To be tested |
|  | replaceBatchV1NamespacedJob | 替换Job。 | To be tested |
|  | deleteBatchV1NamespacedJob | 删除Job。 | To be tested |
|  | listBatchV1JobForAllNamespaces | This API is used to obtain a Job list. | To be tested |
|  | readBatchV1NamespacedJob | 查询Job的详细信息。 | To be tested |
|  | patchBatchV1NamespacedJob | 更新Job。 | To be tested |
| Metrics | listMetricsV1beta1NamespacedPodMetrics | 获取指定namespace下所有pods的metrics信息 | To be tested |
|  | readMetricsV1beta1NamespacedPodMetrics | 获取指定namespace下指定pod的metrics信息 | To be tested |
| Namespace | listCoreV1Namespace | 该API用于获取集群中该用户当前项目下所有Namespace的详细信息。 | To be tested |
|  | createCoreV1Namespace | 创建一个Namespace。 | To be tested |
|  | deleteCoreV1Namespace | 删除一个Namespace。 | To be tested |
|  | readCoreV1Namespace | 查询Namespace的详细信息。 | To be tested |
| Network | deleteNetworkingCciIoV1beta1NamespacedNetwork | 删除一个指定Network对象。 | To be tested |
|  | createNetworkingCciIoV1beta1NamespacedNetwork | 创建一个Network对象。 | To be tested |
|  | listNetworkingCciIoV1beta1NamespacedNetwork | 查询指定namespace下的所有Network对象。 | To be tested |
|  | deleteNetworkingCciIoV1beta1CollectionNamespacedNetwork | 删除指定namespace下的所有Network对象。 | To be tested |
|  | readNetworkingCciIoV1beta1NamespacedNetworkStatus | 查询一个指定Network对象的状态。 | To be tested |
|  | readNetworkingCciIoV1beta1NamespacedNetwork | 查询指定Network对象。 | To be tested |
| OpenAPIv2 | GetOpenAPIv2 | 查询open api swagger信息。 | To be tested |
| PersistentVolumeClaim | replaceCoreV1NamespacedPersistentVolumeClaim | 替换指定PersistentVolumeClaims。 | To be tested |
|  | readCoreV1NamespacedPersistentVolumeClaim | 查询PersistentVolumeClaim。 | To be tested |
|  | createCoreV1NamespacedPersistentVolumeClaim | 创建PersistentVolumeClaim,主要适用于动态创建存储的场景,即存储资源未创建时,创建PVC会根据请求内容创建一个存储资源。 | To be tested |
|  | listCoreV1NamespacedPersistentVolumeClaim | 查询Namespace下的所有PersistentVolumeClaim。 | To be tested |
|  | deleteCoreV1NamespacedPersistentVolumeClaim | 删除PersistentVolumeClaim。 | To be tested |
| Pod | listCoreV1NamespacedPod | 查询指定namespace下的Pods的详细信息。 | To be tested |
|  | readCoreV1NamespacedPodStatus | 查询Pod对象的状态。 | To be tested |
|  | connectCoreV1PostNamespacedPodExec | 进入容器执行命令。 | To be tested |
|  | patchCoreV1NamespacedPod | 更新Pod。 | To be tested |
|  | readCoreV1NamespacedPodLog | 查询Pod的日志。 | To be tested |
|  | connectCoreV1GetNamespacedPodExec | 进入容器执行命令。 | To be tested |
|  | deleteCoreV1CollectionNamespacedPod | 删除Namespace下所有Pod。 | To be tested |
|  | createCoreV1NamespacedPod | 创建一个Pod。 | To be tested |
|  | replaceCoreV1NamespacedPod | 替换指定Pod。 | To be tested |
|  | deleteCoreV1NamespacedPod | 删除Pod,删除前持续10s。 | To be tested |
|  | readCoreV1NamespacedPod | 查询Pod的详细信息。 | To be tested |
|  | listCoreV1PodForAllNamespaces | 该API用于获取一个Pod列表。 | To be tested |
| ReplicaSet | listAppsV1NamespacedReplicaSet | 查询命名空间下所有的ReplicaSets。 | To be tested |
|  | readAppsV1NamespacedReplicaSet | 查询ReplicaSet的详细信息。 | To be tested |
| ResourceQuota | readCoreV1NamespacedResourceQuota | 查询指定的resourcequota(资源用量)。 | To be tested |
|  | listCoreV1NamespacedResourceQuota | 查询指定namespace下的resourcequotas(资源用量)。 | To be tested |
| RoleBinding | listRbacAuthorizationV1NamespacedRoleBinding | This API is used to list or watch objects of kind RoleBinding | To be tested |
|  | listRbacAuthorizationV1RoleBindingForAllNamespaces | This API is used to list or watch objects of kind RoleBinding | To be tested |
|  | readRbacAuthorizationV1NamespacedRoleBinding | This API is used to read the specified RoleBinding | To be tested |
|  | replaceRbacAuthorizationV1NamespacedRoleBinding | This API is used to replace the specified RoleBinding | To be tested |
|  | patchRbacAuthorizationV1NamespacedRoleBinding | This API is used to partially update the specified RoleBinding | To be tested |
|  | createRbacAuthorizationV1NamespacedRoleBinding | This API is used to create a RoleBinding | To be tested |
|  | deleteRbacAuthorizationV1NamespacedRoleBinding | This API is used to delete a RoleBinding | To be tested |
| Secret | deleteCoreV1NamespacedSecret | 删除Secret。 | To be tested |
|  | deleteCoreV1CollectionNamespacedSecret | 删除Namespace下所有Secret。 | To be tested |
|  | listCoreV1NamespacedSecret | 查询指定namespace下的所有Secret对象。 | To be tested |
|  | patchCoreV1NamespacedSecret | 更新Secret中部分信息。 | To be tested |
|  | readCoreV1NamespacedSecret | 查询Secret的详细信息。 | To be tested |
|  | replaceCoreV1NamespacedSecret | 替换Secret。 | To be tested |
|  | createCoreV1NamespacedSecret | 创建Secret,Kubernetes提供了Secret来处理敏感信息。 | To be tested |
| Service | patchCoreV1NamespacedService | 更新Service。 | To be tested |
|  | replaceCoreV1NamespacedService | 替换Service。 | To be tested |
|  | createCoreV1NamespacedService | 创建一个Service。 | To be tested |
|  | readCoreV1NamespacedServiceStatus | 查询指定的Service的状态。 | To be tested |
|  | readCoreV1NamespacedService | 查询Service的详细信息。 | To be tested |
|  | deleteCoreV1NamespacedService | 删除Service。 | To be tested |
|  | listCoreV1NamespacedService | 查询Namespace下所有Service的详细信息。 | To be tested |
| StatefulSet | deleteAppsV1NamespacedStatefulSet | 删除StatefulSet。 | To be tested |
|  | replaceAppsV1NamespacedStatefulSet | 替换StatefulSet。 | To be tested |
|  | readAppsV1NamespacedStatefulSet | 查询StatefulSet的详细信息。 | To be tested |
|  | patchAppsV1NamespacedStatefulSet | 更新StatefulSet。 | To be tested |
|  | readAppsV1NamespacedStatefulSetStatus | 查询StatefulSet状态。 | To be tested |
|  | createAppsV1NamespacedStatefulSet | 创建StatefulSet。 | To be tested |
|  | listAppsV1NamespacedStatefulSet | 查询Namespace下所有StatefulSet的详细信息。 | To be tested |
|  | deleteAppsV1CollectionNamespacedStatefulSet | 删除Namespace下所有StatefulSet。 | To be tested |
|  | listAppsV1StatefulSetForAllNamespaces | This API is used to list all StatefulSet resource objects. | To be tested |
| StorageClass | readStorageV1StorageClass | read the specified StorageClass | To be tested |
|  | listStorageV1StorageClass | list or watch objects of kind StorageClass | To be tested |
| VolcanoJob | replaceBatchVolcanoShV1alpha1NamespacedJob | 替换Volcano Job。 | To be tested |
|  | listBatchVolcanoShV1alpha1NamespacedJob | 查询命名空间下所有的Volcano Job。 | To be tested |
|  | createBatchVolcanoShV1alpha1NamespacedJob | 创建Volcano Job。 | To be tested |
|  | patchBatchVolcanoShV1alpha1NamespacedJob | 更新Volcano Job。 | To be tested |
|  | deleteBatchVolcanoShV1alpha1NamespacedJob | 删除Volcano Job。 | To be tested |
|  | readBatchVolcanoShV1alpha1NamespacedJob | 查询Volcano Job的详细信息。 | To be tested |
|  | deleteBatchVolcanoShV1alpha1CollectionNamespacedJob | 删除命名空间下的所有Volcano Job。 | To be tested |
