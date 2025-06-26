# CCI MCP Server 


## Version
v0.1.0

## Overview

CCI MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CCI. Full-chain management of CCI resources can be carried out based on natural language.

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
                    <td rowspan="20">API groups</td>
                    <td>getCrdYangtseCniAPIGroup</td>
                    <td>查询APIGroup /apis/crd.yangtse.cni</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getBatchVolcanoShV1alpha1APIResources</td>
                    <td>查询所有batch.volcano.sh/v1alpha1的API</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getBatchAPIGroup</td>
                    <td>查询APIGroup /apis/batch</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getRbacAuthorizationAPIGroup</td>
                    <td>get information of a group</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getBatchV1beta1APIResources</td>
                    <td>get available resources</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getBatchVolcanoShAPIGroup</td>
                    <td>查询APIGroup /apis/batch.volcano.sh</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getCoreAPIVersions</td>
                    <td>get available API versions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getExtensionsAPIGroup</td>
                    <td>查询APIGroup /apis/extensions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getAPIVersions</td>
                    <td>get available API versions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getMetricsAPIGroup</td>
                    <td>查询APIGroup /apis/metrics.k8s.io</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getRbacAuthorizationV1APIResources</td>
                    <td>get available resources</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getMetricsV1beta1APIResources</td>
                    <td>get available resources</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getCoreV1APIResources</td>
                    <td>get available resources</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getNetworkingCciIoAPIGroup</td>
                    <td>查询APIGroup /apis/networking.cci.io</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getCrdYangtseCniV1APIResources</td>
                    <td>查询所有crd.yangtse.cni/v1的API</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getExtensionsV1beta1APIResources</td>
                    <td>get available resources</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getNetworkingCciIoV1beta1APIResources</td>
                    <td>get available resources</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getBatchV1APIResources</td>
                    <td>get available resources</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getAppsV1APIResources</td>
                    <td>get available resources</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getAppsAPIGroup</td>
                    <td>查询APIGroup /apis/apps</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ClusterRole</td>
                    <td>listRbacAuthorizationV1ClusterRole</td>
                    <td>This API is used to list or watch objects of kind ClusterRole</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readRbacAuthorizationV1ClusterRole</td>
                    <td>This API is used to read the specified ClusterRole</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">ConfigMap</td>
                    <td>listCoreV1NamespacedConfigMap</td>
                    <td>查询Namespace下所有ConfigMap的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedConfigMap</td>
                    <td>查询ConfigMap详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1NamespacedConfigMap</td>
                    <td>删除ConfigMap。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchCoreV1NamespacedConfigMap</td>
                    <td>更新ConfigMap。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceCoreV1NamespacedConfigMap</td>
                    <td>替换ConfigMap。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1CollectionNamespacedConfigMap</td>
                    <td>删除Namespace下所有ConfigMap。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCoreV1NamespacedConfigMap</td>
                    <td>创建ConfigMap。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">CronJob</td>
                    <td>listBatchV1beta1CronJobForAllNamespaces</td>
                    <td>查询所有namespace下所有CronJob的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Deployment</td>
                    <td>readAppsV1NamespacedDeployment</td>
                    <td>查询Deployment的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createAppsV1NamespacedDeployment</td>
                    <td>创建一个Deployment。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listAppsV1DeploymentForAllNamespaces</td>
                    <td>查询用户所有Deployment。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readAppsV1NamespacedDeploymentStatus</td>
                    <td>查询Deployment的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchAppsV1NamespacedDeployment</td>
                    <td>更新Deployment。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readAppsV1NamespacedDeploymentScale</td>
                    <td>查询Deployment的伸缩操作</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listAppsV1NamespacedDeployment</td>
                    <td>查询Namespace下所有Deployment的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteAppsV1NamespacedDeployment</td>
                    <td>删除Deployment。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchAppsV1NamespacedDeploymentScale</td>
                    <td>This API is used to partially update scale of the specified Scale.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceAppsV1NamespacedDeployment</td>
                    <td>替换Deployment。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteAppsV1CollectionNamespacedDeployment</td>
                    <td>删除Namespace下所有Deployment。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceAppsV1NamespacedDeploymentScale</td>
                    <td>This API is used to replace scale of the specified Scale.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">EIPPool</td>
                    <td>deleteCrdYangtseCniV1NamespacedEIPPool</td>
                    <td>删除指定的EIPPool。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCrdYangtseCniV1NamespacedEIPPoolStatus</td>
                    <td>查询指定的EIPPool的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCrdYangtseCniV1NamespacedEIPPool</td>
                    <td>查询指定的EIPPool的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchCrdYangtseCniV1NamespacedEIPPool</td>
                    <td>更新EIPPool。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCrdYangtseCniV1NamespacedEIPPool</td>
                    <td>查询指定namespace下所有EIPPool的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCrdYangtseCniV1NamespacedEIPPool</td>
                    <td>创建EIPPool。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceCrdYangtseCniV1NamespacedEIPPool</td>
                    <td>替换EIPPool。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Endpoint</td>
                    <td>createCoreV1NamespacedEndpoints</td>
                    <td>创建Endpoint。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1NamespacedEndpoints</td>
                    <td>查询Namespace下所有Endpoints。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceCoreV1NamespacedEndpoints</td>
                    <td>替换Endpoint。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedEndpoints</td>
                    <td>查询Endpoint。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchCoreV1NamespacedEndpoints</td>
                    <td>更新Endpoint。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1NamespacedEndpoints</td>
                    <td>删除Endpoint。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Event</td>
                    <td>deleteCoreV1NamespacedEvent</td>
                    <td>删除Event。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedEvent</td>
                    <td>查询Event详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1NamespacedEvent</td>
                    <td>查询Namespace下所有Event的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Ingress</td>
                    <td>readExtensionsV1beta1NamespacedIngressStatus</td>
                    <td>查询Ingress状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readExtensionsV1beta1NamespacedIngress</td>
                    <td>查询Ingress的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteExtensionsV1beta1NamespacedIngress</td>
                    <td>删除Ingress。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteExtensionsV1beta1CollectionNamespacedIngress</td>
                    <td>删除Namespace下所有Ingress。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listExtensionsV1beta1NamespacedIngress</td>
                    <td>查询Namespace下所有Ingress的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchExtensionsV1beta1NamespacedIngress</td>
                    <td>更新Ingress。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createExtensionsV1beta1NamespacedIngress</td>
                    <td>创建Ingress,使用http协议,关联的后端Service为“redis:8080”,使用ELB作为Ingress控制器,ELB的ip为192.168.137.182,端口号为6071。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceExtensionsV1beta1NamespacedIngress</td>
                    <td>替换Ingress。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Job</td>
                    <td>readBatchV1NamespacedJobStatus</td>
                    <td>查询Job状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteBatchV1CollectionNamespacedJob</td>
                    <td>删除Namespace下所有Job。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createBatchV1NamespacedJob</td>
                    <td>创建Job。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listBatchV1NamespacedJob</td>
                    <td>查询Namespace下所有Job的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceBatchV1NamespacedJob</td>
                    <td>替换Job。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteBatchV1NamespacedJob</td>
                    <td>删除Job。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listBatchV1JobForAllNamespaces</td>
                    <td>This API is used to obtain a Job list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readBatchV1NamespacedJob</td>
                    <td>查询Job的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchBatchV1NamespacedJob</td>
                    <td>更新Job。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Metrics</td>
                    <td>listMetricsV1beta1NamespacedPodMetrics</td>
                    <td>获取指定namespace下所有pods的metrics信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readMetricsV1beta1NamespacedPodMetrics</td>
                    <td>获取指定namespace下指定pod的metrics信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Namespace</td>
                    <td>listCoreV1Namespace</td>
                    <td>该API用于获取集群中该用户当前项目下所有Namespace的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCoreV1Namespace</td>
                    <td>创建一个Namespace。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1Namespace</td>
                    <td>删除一个Namespace。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1Namespace</td>
                    <td>查询Namespace的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Network</td>
                    <td>deleteNetworkingCciIoV1beta1NamespacedNetwork</td>
                    <td>删除一个指定Network对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createNetworkingCciIoV1beta1NamespacedNetwork</td>
                    <td>创建一个Network对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listNetworkingCciIoV1beta1NamespacedNetwork</td>
                    <td>查询指定namespace下的所有Network对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteNetworkingCciIoV1beta1CollectionNamespacedNetwork</td>
                    <td>删除指定namespace下的所有Network对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readNetworkingCciIoV1beta1NamespacedNetworkStatus</td>
                    <td>查询一个指定Network对象的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readNetworkingCciIoV1beta1NamespacedNetwork</td>
                    <td>查询指定Network对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">OpenAPIv2</td>
                    <td>GetOpenAPIv2</td>
                    <td>查询open api swagger信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">PersistentVolumeClaim</td>
                    <td>replaceCoreV1NamespacedPersistentVolumeClaim</td>
                    <td>替换指定PersistentVolumeClaims。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedPersistentVolumeClaim</td>
                    <td>查询PersistentVolumeClaim。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCoreV1NamespacedPersistentVolumeClaim</td>
                    <td>创建PersistentVolumeClaim,主要适用于动态创建存储的场景,即存储资源未创建时,创建PVC会根据请求内容创建一个存储资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1NamespacedPersistentVolumeClaim</td>
                    <td>查询Namespace下的所有PersistentVolumeClaim。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1NamespacedPersistentVolumeClaim</td>
                    <td>删除PersistentVolumeClaim。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Pod</td>
                    <td>listCoreV1NamespacedPod</td>
                    <td>查询指定namespace下的Pods的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedPodStatus</td>
                    <td>查询Pod对象的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>connectCoreV1PostNamespacedPodExec</td>
                    <td>进入容器执行命令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchCoreV1NamespacedPod</td>
                    <td>更新Pod。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedPodLog</td>
                    <td>查询Pod的日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>connectCoreV1GetNamespacedPodExec</td>
                    <td>进入容器执行命令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1CollectionNamespacedPod</td>
                    <td>删除Namespace下所有Pod。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCoreV1NamespacedPod</td>
                    <td>创建一个Pod。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceCoreV1NamespacedPod</td>
                    <td>替换指定Pod。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1NamespacedPod</td>
                    <td>删除Pod,删除前持续10s。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedPod</td>
                    <td>查询Pod的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1PodForAllNamespaces</td>
                    <td>该API用于获取一个Pod列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ReplicaSet</td>
                    <td>listAppsV1NamespacedReplicaSet</td>
                    <td>查询命名空间下所有的ReplicaSets。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readAppsV1NamespacedReplicaSet</td>
                    <td>查询ReplicaSet的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ResourceQuota</td>
                    <td>readCoreV1NamespacedResourceQuota</td>
                    <td>查询指定的resourcequota(资源用量)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1NamespacedResourceQuota</td>
                    <td>查询指定namespace下的resourcequotas(资源用量)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">RoleBinding</td>
                    <td>listRbacAuthorizationV1NamespacedRoleBinding</td>
                    <td>This API is used to list or watch objects of kind RoleBinding</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listRbacAuthorizationV1RoleBindingForAllNamespaces</td>
                    <td>This API is used to list or watch objects of kind RoleBinding</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readRbacAuthorizationV1NamespacedRoleBinding</td>
                    <td>This API is used to read the specified RoleBinding</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceRbacAuthorizationV1NamespacedRoleBinding</td>
                    <td>This API is used to replace the specified RoleBinding</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchRbacAuthorizationV1NamespacedRoleBinding</td>
                    <td>This API is used to partially update the specified RoleBinding</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createRbacAuthorizationV1NamespacedRoleBinding</td>
                    <td>This API is used to create a RoleBinding</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteRbacAuthorizationV1NamespacedRoleBinding</td>
                    <td>This API is used to delete a RoleBinding</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Secret</td>
                    <td>deleteCoreV1NamespacedSecret</td>
                    <td>删除Secret。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1CollectionNamespacedSecret</td>
                    <td>删除Namespace下所有Secret。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1NamespacedSecret</td>
                    <td>查询指定namespace下的所有Secret对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchCoreV1NamespacedSecret</td>
                    <td>更新Secret中部分信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedSecret</td>
                    <td>查询Secret的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceCoreV1NamespacedSecret</td>
                    <td>替换Secret。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCoreV1NamespacedSecret</td>
                    <td>创建Secret,Kubernetes提供了Secret来处理敏感信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Service</td>
                    <td>patchCoreV1NamespacedService</td>
                    <td>更新Service。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceCoreV1NamespacedService</td>
                    <td>替换Service。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCoreV1NamespacedService</td>
                    <td>创建一个Service。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedServiceStatus</td>
                    <td>查询指定的Service的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedService</td>
                    <td>查询Service的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1NamespacedService</td>
                    <td>删除Service。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1NamespacedService</td>
                    <td>查询Namespace下所有Service的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">StatefulSet</td>
                    <td>deleteAppsV1NamespacedStatefulSet</td>
                    <td>删除StatefulSet。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceAppsV1NamespacedStatefulSet</td>
                    <td>替换StatefulSet。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readAppsV1NamespacedStatefulSet</td>
                    <td>查询StatefulSet的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchAppsV1NamespacedStatefulSet</td>
                    <td>更新StatefulSet。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readAppsV1NamespacedStatefulSetStatus</td>
                    <td>查询StatefulSet状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createAppsV1NamespacedStatefulSet</td>
                    <td>创建StatefulSet。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listAppsV1NamespacedStatefulSet</td>
                    <td>查询Namespace下所有StatefulSet的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteAppsV1CollectionNamespacedStatefulSet</td>
                    <td>删除Namespace下所有StatefulSet。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listAppsV1StatefulSetForAllNamespaces</td>
                    <td>This API is used to list all StatefulSet resource objects.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">StorageClass</td>
                    <td>readStorageV1StorageClass</td>
                    <td>read the specified StorageClass</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listStorageV1StorageClass</td>
                    <td>list or watch objects of kind StorageClass</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">VolcanoJob</td>
                    <td>replaceBatchVolcanoShV1alpha1NamespacedJob</td>
                    <td>替换Volcano Job。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listBatchVolcanoShV1alpha1NamespacedJob</td>
                    <td>查询命名空间下所有的Volcano Job。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createBatchVolcanoShV1alpha1NamespacedJob</td>
                    <td>创建Volcano Job。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchBatchVolcanoShV1alpha1NamespacedJob</td>
                    <td>更新Volcano Job。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteBatchVolcanoShV1alpha1NamespacedJob</td>
                    <td>删除Volcano Job。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readBatchVolcanoShV1alpha1NamespacedJob</td>
                    <td>查询Volcano Job的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteBatchVolcanoShV1alpha1CollectionNamespacedJob</td>
                    <td>删除命名空间下的所有Volcano Job。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
