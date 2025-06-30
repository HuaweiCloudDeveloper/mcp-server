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
                    <td>Query the APIGroup /apis/crd.yangtse.cni</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getBatchVolcanoShV1alpha1APIResources</td>
                    <td>Query all APIs for batch.volcano.sh/v1alpha1</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getBatchAPIGroup</td>
                    <td>Query APIGroup /apis/batch</td>
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
                    <td>Query APIGroup /apis/batch.volcano.sh</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getCoreAPIVersions</td>
                    <td>get available API versions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getExtensionsAPIGroup</td>
                    <td>Query APIGroup /apis/extensions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getAPIVersions</td>
                    <td>get available API versions</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getMetricsAPIGroup</td>
                    <td>Query APIGroup /apis/metrics.k8s.io</td>
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
                    <td>Query APIGroup /apis/networking.cci.io</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getCrdYangtseCniV1APIResources</td>
                    <td>Query all crd.yangtse.cni/v1 APIs</td>
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
                    <td>Query APIGroup /apis/apps</td>
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
                    <td>Query details about all ConfigMaps in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedConfigMap</td>
                    <td>Query the details about the ConfigMap.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1NamespacedConfigMap</td>
                    <td>Delete the ConfigMap.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchCoreV1NamespacedConfigMap</td>
                    <td>Update the ConfigMap.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceCoreV1NamespacedConfigMap</td>
                    <td>Replace the ConfigMap.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1CollectionNamespacedConfigMap</td>
                    <td>Delete all ConfigMaps in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCoreV1NamespacedConfigMap</td>
                    <td>Create the ConfigMap.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">CronJob</td>
                    <td>listBatchV1beta1CronJobForAllNamespaces</td>
                    <td>Query details about all CronJobs in all namespaces.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Deployment</td>
                    <td>readAppsV1NamespacedDeployment</td>
                    <td>Query the details about a Deployment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createAppsV1NamespacedDeployment</td>
                    <td>Create a Deployment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listAppsV1DeploymentForAllNamespaces</td>
                    <td>Query all Deployments of a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readAppsV1NamespacedDeploymentStatus</td>
                    <td>Query the status of a Deployment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchAppsV1NamespacedDeployment</td>
                    <td>Update the Deployment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readAppsV1NamespacedDeploymentScale</td>
                    <td>Query the scaling operation of a Deployment</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listAppsV1NamespacedDeployment</td>
                    <td>Query details about all Deployments in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteAppsV1NamespacedDeployment</td>
                    <td>Delete a Deployment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchAppsV1NamespacedDeploymentScale</td>
                    <td>This API is used to partially update scale of the specified Scale.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceAppsV1NamespacedDeployment</td>
                    <td>Replace a Deployment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteAppsV1CollectionNamespacedDeployment</td>
                    <td>Delete all Deployments in the namespace.</td>
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
                    <td>Deletes a specified EIP pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCrdYangtseCniV1NamespacedEIPPoolStatus</td>
                    <td>Query the details about a specified EIP pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCrdYangtseCniV1NamespacedEIPPool</td>
                    <td>Query the details about a specified EIP pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchCrdYangtseCniV1NamespacedEIPPool</td>
                    <td>Updates the EIP pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCrdYangtseCniV1NamespacedEIPPool</td>
                    <td>Query details about all EIP pools in a specified namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCrdYangtseCniV1NamespacedEIPPool</td>
                    <td>Create an EIP pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceCrdYangtseCniV1NamespacedEIPPool</td>
                    <td>Replace the EIP pool.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Endpoint</td>
                    <td>createCoreV1NamespacedEndpoints</td>
                    <td>Create an endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1NamespacedEndpoints</td>
                    <td>Query all endpoints in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceCoreV1NamespacedEndpoints</td>
                    <td>Replace the endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedEndpoints</td>
                    <td>Query the endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchCoreV1NamespacedEndpoints</td>
                    <td>Update the endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1NamespacedEndpoints</td>
                    <td>Delete the endpoint.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Event</td>
                    <td>deleteCoreV1NamespacedEvent</td>
                    <td>Delete the event.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedEvent</td>
                    <td>Query event details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1NamespacedEvent</td>
                    <td>Query details about all events in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Ingress</td>
                    <td>readExtensionsV1beta1NamespacedIngressStatus</td>
                    <td>Query the ingress status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readExtensionsV1beta1NamespacedIngress</td>
                    <td>Query detailed information about the ingress.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteExtensionsV1beta1NamespacedIngress</td>
                    <td>Delete the ingress.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteExtensionsV1beta1CollectionNamespacedIngress</td>
                    <td>Delete all ingresses in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listExtensionsV1beta1NamespacedIngress</td>
                    <td>Query details about all ingresses in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchExtensionsV1beta1NamespacedIngress</td>
                    <td>Update the Ingress.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createExtensionsV1beta1NamespacedIngress</td>
                    <td>Create an ingress, use HTTP, associate backend service redis:8080, use ELB as the ingress controller, set the ELB IP address to 192.168.137.182, and port number to 6071.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceExtensionsV1beta1NamespacedIngress</td>
                    <td>Replace the Ingress.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Job</td>
                    <td>readBatchV1NamespacedJobStatus</td>
                    <td>Query the job status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteBatchV1CollectionNamespacedJob</td>
                    <td>Delete all jobs in the namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createBatchV1NamespacedJob</td>
                    <td>Create a job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listBatchV1NamespacedJob</td>
                    <td>Query details about all jobs in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceBatchV1NamespacedJob</td>
                    <td>Replace the job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteBatchV1NamespacedJob</td>
                    <td>Delete a job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listBatchV1JobForAllNamespaces</td>
                    <td>This API is used to obtain a Job list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readBatchV1NamespacedJob</td>
                    <td>Query job details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchBatchV1NamespacedJob</td>
                    <td>Update the job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Metrics</td>
                    <td>listMetricsV1beta1NamespacedPodMetrics</td>
                    <td>Obtain the metrics of all pods in a specified namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readMetricsV1beta1NamespacedPodMetrics</td>
                    <td>Obtain the metrics information about a specified pod in a specified namespace</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Namespace</td>
                    <td>listCoreV1Namespace</td>
                    <td>This API is used to obtain details about all namespaces in the current project of a user in a cluster.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCoreV1Namespace</td>
                    <td>Create a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1Namespace</td>
                    <td>Delete a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1Namespace</td>
                    <td>Query details about a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Network</td>
                    <td>deleteNetworkingCciIoV1beta1NamespacedNetwork</td>
                    <td>Deletes a specified network object.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createNetworkingCciIoV1beta1NamespacedNetwork</td>
                    <td>Create a Network object.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listNetworkingCciIoV1beta1NamespacedNetwork</td>
                    <td>Query all network objects in a specified namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteNetworkingCciIoV1beta1CollectionNamespacedNetwork</td>
                    <td>Delete all Network objects in a specified namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readNetworkingCciIoV1beta1NamespacedNetworkStatus</td>
                    <td>Query the status of a specified network object.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readNetworkingCciIoV1beta1NamespacedNetwork</td>
                    <td>Query the specified network object.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">OpenAPIv2</td>
                    <td>GetOpenAPIv2</td>
                    <td>Query the open API swagger information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">PersistentVolumeClaim</td>
                    <td>replaceCoreV1NamespacedPersistentVolumeClaim</td>
                    <td>Replaces the specified PersistentVolumeClaims.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedPersistentVolumeClaim</td>
                    <td>Query PersistentVolumeClaim.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCoreV1NamespacedPersistentVolumeClaim</td>
                    <td>Creating a PersistentVolumeClaim is applicable to the scenario where storage resources are dynamically created. That is, when storage resources are not created, a storage resource will be created based on the requested content when a PVC is created.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1NamespacedPersistentVolumeClaim</td>
                    <td>Query all PersistentVolumeClaims in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1NamespacedPersistentVolumeClaim</td>
                    <td>Delete PersistentVolumeClaim.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Pod</td>
                    <td>listCoreV1NamespacedPod</td>
                    <td>Query detailed information about pods in a specified namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedPodStatus</td>
                    <td>Query the status of a pod object.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>connectCoreV1PostNamespacedPodExec</td>
                    <td>Go to the container and run the command.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchCoreV1NamespacedPod</td>
                    <td>Updates a pod.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedPodLog</td>
                    <td>Query pod logs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>connectCoreV1GetNamespacedPodExec</td>
                    <td>Go to the container and run the command.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1CollectionNamespacedPod</td>
                    <td>Delete all pods in the namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCoreV1NamespacedPod</td>
                    <td>Create a pod.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceCoreV1NamespacedPod</td>
                    <td>Replace the specified pod.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1NamespacedPod</td>
                    <td>Delete a pod. The pod must be deleted for 10 seconds.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedPod</td>
                    <td>Query pod details.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1PodForAllNamespaces</td>
                    <td>This API is used to obtain a pod list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ReplicaSet</td>
                    <td>listAppsV1NamespacedReplicaSet</td>
                    <td>Query all ReplicaSets in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readAppsV1NamespacedReplicaSet</td>
                    <td>Query details about a ReplicaSet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ResourceQuota</td>
                    <td>readCoreV1NamespacedResourceQuota</td>
                    <td>Query the specified resourcequota.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1NamespacedResourceQuota</td>
                    <td>Query the resourcequotas (resource usage) in a specified namespace.</td>
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
                    <td>Delete a secret.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1CollectionNamespacedSecret</td>
                    <td>Delete all secrets in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1NamespacedSecret</td>
                    <td>Query all Secret objects in a specified namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchCoreV1NamespacedSecret</td>
                    <td>Updates some information in the secret.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedSecret</td>
                    <td>Query details about a secret.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceCoreV1NamespacedSecret</td>
                    <td>Replace the secret.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCoreV1NamespacedSecret</td>
                    <td>Create a secret. Kubernetes provides the secret to process sensitive information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Service</td>
                    <td>patchCoreV1NamespacedService</td>
                    <td>Update the service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceCoreV1NamespacedService</td>
                    <td>Replace a service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createCoreV1NamespacedService</td>
                    <td>Create a service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedServiceStatus</td>
                    <td>Query the status of a specified service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readCoreV1NamespacedService</td>
                    <td>Query the details about a service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteCoreV1NamespacedService</td>
                    <td>Delete a service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listCoreV1NamespacedService</td>
                    <td>Query details about all services in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">StatefulSet</td>
                    <td>deleteAppsV1NamespacedStatefulSet</td>
                    <td>Delete a StatefulSet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>replaceAppsV1NamespacedStatefulSet</td>
                    <td>Replace a StatefulSet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readAppsV1NamespacedStatefulSet</td>
                    <td>Query the details about a StatefulSet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchAppsV1NamespacedStatefulSet</td>
                    <td>Update the StatefulSet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readAppsV1NamespacedStatefulSetStatus</td>
                    <td>Query the StatefulSet status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createAppsV1NamespacedStatefulSet</td>
                    <td>Create a StatefulSet.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listAppsV1NamespacedStatefulSet</td>
                    <td>Query details about all StatefulSets in a namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteAppsV1CollectionNamespacedStatefulSet</td>
                    <td>Delete all StatefulSets in a namespace.</td>
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
                    <td>Replace the Volcano Job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>listBatchVolcanoShV1alpha1NamespacedJob</td>
                    <td>Query all Volcano jobs in the namespace.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>createBatchVolcanoShV1alpha1NamespacedJob</td>
                    <td>Create a Volcano Job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>patchBatchVolcanoShV1alpha1NamespacedJob</td>
                    <td>Update the Volcano Job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteBatchVolcanoShV1alpha1NamespacedJob</td>
                    <td>Delete a Volcano Job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>readBatchVolcanoShV1alpha1NamespacedJob</td>
                    <td>Query the details about a Volcano Job.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>deleteBatchVolcanoShV1alpha1CollectionNamespacedJob</td>
                    <td>Delete all Volcano jobs in the namespace.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
