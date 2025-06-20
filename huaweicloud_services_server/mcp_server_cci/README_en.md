# CCI MCP Server 


## Version
v0.1.0

## Overview

CCI MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CCI. Full-chain management of CCI resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| API groups | getCrdYangtseCniAPIGroup | Query the APIGroup /apis/crd.yangtse.cni | To be tested |
|  | getBatchVolcanoShV1alpha1APIResources | Query all APIs for batch.volcano.sh/v1alpha1 | To be tested |
|  | getBatchAPIGroup | Query APIGroup /apis/batch | To be tested |
|  | getRbacAuthorizationAPIGroup | get information of a group | To be tested |
|  | getBatchV1beta1APIResources | get available resources | To be tested |
|  | getBatchVolcanoShAPIGroup | Query APIGroup /apis/batch.volcano.sh | To be tested |
|  | getCoreAPIVersions | get available API versions | To be tested |
|  | getExtensionsAPIGroup | Query APIGroup /apis/extensions | To be tested |
|  | getAPIVersions | get available API versions | To be tested |
|  | getMetricsAPIGroup | Query APIGroup /apis/metrics.k8s.io | To be tested |
|  | getRbacAuthorizationV1APIResources | get available resources | To be tested |
|  | getMetricsV1beta1APIResources | get available resources | To be tested |
|  | getCoreV1APIResources | get available resources | To be tested |
|  | getNetworkingCciIoAPIGroup | Query APIGroup /apis/networking.cci.io | To be tested |
|  | getCrdYangtseCniV1APIResources | Query all crd.yangtse.cni/v1 APIs | To be tested |
|  | getExtensionsV1beta1APIResources | get available resources | To be tested |
|  | getNetworkingCciIoV1beta1APIResources | get available resources | To be tested |
|  | getBatchV1APIResources | get available resources | To be tested |
|  | getAppsV1APIResources | get available resources | To be tested |
|  | getAppsAPIGroup | Query APIGroup /apis/apps | To be tested |
| ClusterRole | listRbacAuthorizationV1ClusterRole | This API is used to list or watch objects of kind ClusterRole | To be tested |
|  | readRbacAuthorizationV1ClusterRole | This API is used to read the specified ClusterRole | To be tested |
| ConfigMap | listCoreV1NamespacedConfigMap | Query details about all ConfigMaps in a namespace. | To be tested |
|  | readCoreV1NamespacedConfigMap | Query the details about the ConfigMap. | To be tested |
|  | deleteCoreV1NamespacedConfigMap | Delete the ConfigMap. | To be tested |
|  | patchCoreV1NamespacedConfigMap | Update the ConfigMap. | To be tested |
|  | replaceCoreV1NamespacedConfigMap | Replace the ConfigMap. | To be tested |
|  | deleteCoreV1CollectionNamespacedConfigMap | Delete all ConfigMaps in a namespace. | To be tested |
|  | createCoreV1NamespacedConfigMap | Create the ConfigMap. | To be tested |
| CronJob | listBatchV1beta1CronJobForAllNamespaces | Query details about all CronJobs in all namespaces. | To be tested |
| Deployment | readAppsV1NamespacedDeployment | Query the details about a Deployment. | To be tested |
|  | createAppsV1NamespacedDeployment | Create a Deployment. | To be tested |
|  | listAppsV1DeploymentForAllNamespaces | Query all Deployments of a user. | To be tested |
|  | readAppsV1NamespacedDeploymentStatus | Query the status of a Deployment. | To be tested |
|  | patchAppsV1NamespacedDeployment | Update the Deployment. | To be tested |
|  | readAppsV1NamespacedDeploymentScale | Query the scaling operation of a Deployment | To be tested |
|  | listAppsV1NamespacedDeployment | Query details about all Deployments in a namespace. | To be tested |
|  | deleteAppsV1NamespacedDeployment | Delete a Deployment. | To be tested |
|  | patchAppsV1NamespacedDeploymentScale | This API is used to partially update scale of the specified Scale. | To be tested |
|  | replaceAppsV1NamespacedDeployment | Replace a Deployment. | To be tested |
|  | deleteAppsV1CollectionNamespacedDeployment | Delete all Deployments in the namespace. | To be tested |
|  | replaceAppsV1NamespacedDeploymentScale | This API is used to replace scale of the specified Scale. | To be tested |
| EIPPool | deleteCrdYangtseCniV1NamespacedEIPPool | Deletes a specified EIP pool. | To be tested |
|  | readCrdYangtseCniV1NamespacedEIPPoolStatus | Query the details about a specified EIP pool. | To be tested |
|  | readCrdYangtseCniV1NamespacedEIPPool | Query the details about a specified EIP pool. | To be tested |
|  | patchCrdYangtseCniV1NamespacedEIPPool | Updates the EIP pool. | To be tested |
|  | listCrdYangtseCniV1NamespacedEIPPool | Query details about all EIP pools in a specified namespace. | To be tested |
|  | createCrdYangtseCniV1NamespacedEIPPool | Create an EIP pool. | To be tested |
|  | replaceCrdYangtseCniV1NamespacedEIPPool | Replace the EIP pool. | To be tested |
| Endpoint | createCoreV1NamespacedEndpoints | Create an endpoint. | To be tested |
|  | listCoreV1NamespacedEndpoints | Query all endpoints in a namespace. | To be tested |
|  | replaceCoreV1NamespacedEndpoints | Replace the endpoint. | To be tested |
|  | readCoreV1NamespacedEndpoints | Query the endpoint. | To be tested |
|  | patchCoreV1NamespacedEndpoints | Update the endpoint. | To be tested |
|  | deleteCoreV1NamespacedEndpoints | Delete the endpoint. | To be tested |
| Event | deleteCoreV1NamespacedEvent | Delete the event. | To be tested |
|  | readCoreV1NamespacedEvent | Query event details. | To be tested |
|  | listCoreV1NamespacedEvent | Query details about all events in a namespace. | To be tested |
| Ingress | readExtensionsV1beta1NamespacedIngressStatus | Query the ingress status. | To be tested |
|  | readExtensionsV1beta1NamespacedIngress | Query detailed information about the ingress. | To be tested |
|  | deleteExtensionsV1beta1NamespacedIngress | Delete the ingress. | To be tested |
|  | deleteExtensionsV1beta1CollectionNamespacedIngress | Delete all ingresses in a namespace. | To be tested |
|  | listExtensionsV1beta1NamespacedIngress | Query details about all ingresses in a namespace. | To be tested |
|  | patchExtensionsV1beta1NamespacedIngress | Update the Ingress. | To be tested |
|  | createExtensionsV1beta1NamespacedIngress | Create an ingress, use HTTP, associate backend service redis:8080, use ELB as the ingress controller, set the ELB IP address to 192.168.137.182, and port number to 6071. | To be tested |
|  | replaceExtensionsV1beta1NamespacedIngress | Replace the Ingress. | To be tested |
| Job | readBatchV1NamespacedJobStatus | Query the job status. | To be tested |
|  | deleteBatchV1CollectionNamespacedJob | Delete all jobs in the namespace. | To be tested |
|  | createBatchV1NamespacedJob | Create a job. | To be tested |
|  | listBatchV1NamespacedJob | Query details about all jobs in a namespace. | To be tested |
|  | replaceBatchV1NamespacedJob | Replace the job. | To be tested |
|  | deleteBatchV1NamespacedJob | Delete a job. | To be tested |
|  | listBatchV1JobForAllNamespaces | This API is used to obtain a Job list. | To be tested |
|  | readBatchV1NamespacedJob | Query job details. | To be tested |
|  | patchBatchV1NamespacedJob | Update the job. | To be tested |
| Metrics | listMetricsV1beta1NamespacedPodMetrics | Obtain the metrics of all pods in a specified namespace. | To be tested |
|  | readMetricsV1beta1NamespacedPodMetrics | Obtain the metrics information about a specified pod in a specified namespace | To be tested |
| Namespace | listCoreV1Namespace | This API is used to obtain details about all namespaces in the current project of a user in a cluster. | To be tested |
|  | createCoreV1Namespace | Create a namespace. | To be tested |
|  | deleteCoreV1Namespace | Delete a namespace. | To be tested |
|  | readCoreV1Namespace | Query details about a namespace. | To be tested |
| Network | deleteNetworkingCciIoV1beta1NamespacedNetwork | Deletes a specified network object. | To be tested |
|  | createNetworkingCciIoV1beta1NamespacedNetwork | Create a Network object. | To be tested |
|  | listNetworkingCciIoV1beta1NamespacedNetwork | Query all network objects in a specified namespace. | To be tested |
|  | deleteNetworkingCciIoV1beta1CollectionNamespacedNetwork | Delete all Network objects in a specified namespace. | To be tested |
|  | readNetworkingCciIoV1beta1NamespacedNetworkStatus | Query the status of a specified network object. | To be tested |
|  | readNetworkingCciIoV1beta1NamespacedNetwork | Query the specified network object. | To be tested |
| OpenAPIv2 | GetOpenAPIv2 | Query the open API swagger information. | To be tested |
| PersistentVolumeClaim | replaceCoreV1NamespacedPersistentVolumeClaim | Replaces the specified PersistentVolumeClaims. | To be tested |
|  | readCoreV1NamespacedPersistentVolumeClaim | Query PersistentVolumeClaim. | To be tested |
|  | createCoreV1NamespacedPersistentVolumeClaim | Creating a PersistentVolumeClaim is applicable to the scenario where storage resources are dynamically created. That is, when storage resources are not created, a storage resource will be created based on the requested content when a PVC is created. | To be tested |
|  | listCoreV1NamespacedPersistentVolumeClaim | Query all PersistentVolumeClaims in a namespace. | To be tested |
|  | deleteCoreV1NamespacedPersistentVolumeClaim | Delete PersistentVolumeClaim. | To be tested |
| Pod | listCoreV1NamespacedPod | Query detailed information about pods in a specified namespace. | To be tested |
|  | readCoreV1NamespacedPodStatus | Query the status of a pod object. | To be tested |
|  | connectCoreV1PostNamespacedPodExec | Go to the container and run the command. | To be tested |
|  | patchCoreV1NamespacedPod | Updates a pod. | To be tested |
|  | readCoreV1NamespacedPodLog | Query pod logs. | To be tested |
|  | connectCoreV1GetNamespacedPodExec | Go to the container and run the command. | To be tested |
|  | deleteCoreV1CollectionNamespacedPod | Delete all pods in the namespace. | To be tested |
|  | createCoreV1NamespacedPod | Create a pod. | To be tested |
|  | replaceCoreV1NamespacedPod | Replace the specified pod. | To be tested |
|  | deleteCoreV1NamespacedPod | Delete a pod. The pod must be deleted for 10 seconds. | To be tested |
|  | readCoreV1NamespacedPod | Query pod details. | To be tested |
|  | listCoreV1PodForAllNamespaces | This API is used to obtain a pod list. | To be tested |
| ReplicaSet | listAppsV1NamespacedReplicaSet | Query all ReplicaSets in a namespace. | To be tested |
|  | readAppsV1NamespacedReplicaSet | Query details about a ReplicaSet. | To be tested |
| ResourceQuota | readCoreV1NamespacedResourceQuota | Query the specified resourcequota. | To be tested |
|  | listCoreV1NamespacedResourceQuota | Query the resourcequotas (resource usage) in a specified namespace. | To be tested |
| RoleBinding | listRbacAuthorizationV1NamespacedRoleBinding | This API is used to list or watch objects of kind RoleBinding | To be tested |
|  | listRbacAuthorizationV1RoleBindingForAllNamespaces | This API is used to list or watch objects of kind RoleBinding | To be tested |
|  | readRbacAuthorizationV1NamespacedRoleBinding | This API is used to read the specified RoleBinding | To be tested |
|  | replaceRbacAuthorizationV1NamespacedRoleBinding | This API is used to replace the specified RoleBinding | To be tested |
|  | patchRbacAuthorizationV1NamespacedRoleBinding | This API is used to partially update the specified RoleBinding | To be tested |
|  | createRbacAuthorizationV1NamespacedRoleBinding | This API is used to create a RoleBinding | To be tested |
|  | deleteRbacAuthorizationV1NamespacedRoleBinding | This API is used to delete a RoleBinding | To be tested |
| Secret | deleteCoreV1NamespacedSecret | Delete a secret. | To be tested |
|  | deleteCoreV1CollectionNamespacedSecret | Delete all secrets in a namespace. | To be tested |
|  | listCoreV1NamespacedSecret | Query all Secret objects in a specified namespace. | To be tested |
|  | patchCoreV1NamespacedSecret | Updates some information in the secret. | To be tested |
|  | readCoreV1NamespacedSecret | Query details about a secret. | To be tested |
|  | replaceCoreV1NamespacedSecret | Replace the secret. | To be tested |
|  | createCoreV1NamespacedSecret | Create a secret. Kubernetes provides the secret to process sensitive information. | To be tested |
| Service | patchCoreV1NamespacedService | Update the service. | To be tested |
|  | replaceCoreV1NamespacedService | Replace a service. | To be tested |
|  | createCoreV1NamespacedService | Create a service. | To be tested |
|  | readCoreV1NamespacedServiceStatus | Query the status of a specified service. | To be tested |
|  | readCoreV1NamespacedService | Query the details about a service. | To be tested |
|  | deleteCoreV1NamespacedService | Delete a service. | To be tested |
|  | listCoreV1NamespacedService | Query details about all services in a namespace. | To be tested |
| StatefulSet | deleteAppsV1NamespacedStatefulSet | Delete a StatefulSet. | To be tested |
|  | replaceAppsV1NamespacedStatefulSet | Replace a StatefulSet. | To be tested |
|  | readAppsV1NamespacedStatefulSet | Query the details about a StatefulSet. | To be tested |
|  | patchAppsV1NamespacedStatefulSet | Update the StatefulSet. | To be tested |
|  | readAppsV1NamespacedStatefulSetStatus | Query the StatefulSet status. | To be tested |
|  | createAppsV1NamespacedStatefulSet | Create a StatefulSet. | To be tested |
|  | listAppsV1NamespacedStatefulSet | Query details about all StatefulSets in a namespace. | To be tested |
|  | deleteAppsV1CollectionNamespacedStatefulSet | Delete all StatefulSets in a namespace. | To be tested |
|  | listAppsV1StatefulSetForAllNamespaces | This API is used to list all StatefulSet resource objects. | To be tested |
| StorageClass | readStorageV1StorageClass | read the specified StorageClass | To be tested |
|  | listStorageV1StorageClass | list or watch objects of kind StorageClass | To be tested |
| VolcanoJob | replaceBatchVolcanoShV1alpha1NamespacedJob | Replace the Volcano Job. | To be tested |
|  | listBatchVolcanoShV1alpha1NamespacedJob | Query all Volcano jobs in the namespace. | To be tested |
|  | createBatchVolcanoShV1alpha1NamespacedJob | Create a Volcano Job. | To be tested |
|  | patchBatchVolcanoShV1alpha1NamespacedJob | Update the Volcano Job. | To be tested |
|  | deleteBatchVolcanoShV1alpha1NamespacedJob | Delete a Volcano Job. | To be tested |
|  | readBatchVolcanoShV1alpha1NamespacedJob | Query the details about a Volcano Job. | To be tested |
|  | deleteBatchVolcanoShV1alpha1CollectionNamespacedJob | Delete all Volcano jobs in the namespace. | To be tested |

