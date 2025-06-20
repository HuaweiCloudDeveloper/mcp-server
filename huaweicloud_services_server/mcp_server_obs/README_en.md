# OBS MCP Server 


## Version
v0.1.0

## Overview

OBS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service OBS. Full-chain management of OBS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Advanced Bucket Configuration | DeleteDirectcoldaccess | Deletes the direct read configuration information about archive objects in a specified bucket. | To be tested |
|  | SetBucketEncryption | OBS uses the PUT operation to create or update the default server-side encryption configuration for a bucket. | To be tested |
|  | GetBucketPolicy | The implementation of this API uses the policy subresource to return the policy of a specified bucket to the client. | To be tested |
|  | SetBucketObsCompressPolicy | This API is used to configure a ZIP file decompression policy for a specified bucket. The interface is idempotent. If the same policy content already exists in the bucket, a success message is returned, and the return value of status code is 200. Otherwise, the return value of status code is 201. | To be tested |
|  | SetDirectcoldaccess | Direct Read of Archived Objects means that users can perform operations on archived objects without restoring them. | To be tested |
|  | GetBucketQuota | The bucket owner can obtain the bucket quota information. You cannot query the bucket quota information because the bucket owner is in the inactive state. The unit of the bucket space quota is byte. The value 0 indicates that no upper limit is set. | To be tested |
|  | DeleteBucketObsCompressPolicy | This API is used to delete the ZIP file decompression policy configured in a specified bucket. If the deletion is successful, the return value of status code is 204. | To be tested |
|  | DeleteBucketLifecycle | This API is used to delete the lifecycle configuration information of a bucket. After the object is deleted, the object in the bucket will not expire, and OBS will not automatically delete the object in the bucket. | To be tested |
|  | SetBucketLifecycle | The OBS system allows you to specify rules to periodically delete or migrate objects in buckets. This is called life cycle configuration. Typical application scenarios are as follows: | To be tested |
|  | SetBucketMirrorBackToSource | This API is used to configure an image retrieval policy for a specified bucket. The interface is idempotent. If the same policy content already exists in the bucket, a success message is returned, and the return value of status code is 200. Otherwise, the return value of status code is 201. | To be tested |
|  | GetBucketLifecycle | Obtain the lifecycle configuration information of the bucket. | To be tested |
|  | DeleteBucketEncryption | OBS uses the DELETE operation to delete the encryption configuration of a specified bucket. | To be tested |
|  | SetBucketPolicy | This API uses the policy subresource to create or modify a bucket policy. If a policy already exists in the bucket, the policy in the current request will overwrite the existing policy in the bucket. There is no limit on the number of bucket policies (statements) in a bucket. However, the total size of the JSON description of all bucket policies in a bucket cannot exceed 20 KB. | To be tested |
|  | SetBucketReplication | Cross-region replication automatically and asynchronously replicates objects across buckets in different regions. By activating cross-region replication, OBS can copy newly created and modified objects from a source bucket to a destination bucket in different regions. | To be tested |
|  | GetBucketStorageInfo |  | To be tested |
|  | ListBucketInventory | OBS uses the GET operation without the inventory ID to obtain all inventory configurations of a specified bucket. The obtained inventory configurations are returned at a time without pagination. | To be tested |
|  | GetBucketReplication | This API is used to obtain the replication configuration information of a specified bucket. Before performing this operation, ensure that you have the GetReplicationConfiguration permission. | To be tested |
|  | GetBucketMirrorBackToSource | This API is used to query the image retrieval policy of a specified bucket. If the policy exists, a success message is returned and the value of status code is 200. | To be tested |
|  | DeleteBucketReplication | This API is used to delete the replication configuration of a bucket. Before performing this operation, ensure that you have the DeleteReplicationConfiguration permission. | To be tested |
|  | GetBucketInventory | OBS uses the GET operation to obtain the inventory configuration of a specified bucket. | To be tested |
|  | SetBucketInventory | OBS uses the PUT operation to configure inventory rules for a bucket. A maximum of 10 inventory rules can be configured for each bucket.  | To be tested |
|  | GetBucketCustomdomain | OBS uses the GET operation to obtain the user-defined domain name of a bucket. | To be tested |
|  | DeleteBucketInventory | OBS uses the DELETE operation to delete the inventory configuration of a specified bucket. The inventory configuration is specified by the inventory ID. | To be tested |
|  | SetBucketTagging | OBS uses the PUT operation to add a tag to an existing bucket. | To be tested |
|  | GetBucketVersioning | The bucket owner can obtain the versioning status of a specified bucket. | To be tested |
|  | DeleteBucketCustomdomain | OBS uses the DELETE operation to delete the tag of a specified bucket. | To be tested |
|  | SetBucketVersioning | Versioning provides a means of restoring objects in the event that users overwrite or delete objects accidentally. Users can save, retrieve, and restore versions of an object using the versioning feature, allowing users to easily recover data from unexpected actions or application failures. Versioning is also available for data retention and archiving. | To be tested |
|  | SetBucketQuota | The bucket space quota must be a non-negative integer, in bytes. The maximum value is 2 ^ 63 – 1. The default bucket quota is 0, indicating that the bucket quota is not limited. | To be tested |
|  | GetBucketAcl | A user performs the operation of obtaining the bucket ACL. The returned information contains the permission control list of the specified bucket. To obtain the ACL of a bucket, you must have the READ_ACP or FULL_CONTROL permission on the bucket. | To be tested |
|  | SetBucketStoragePolicy | This API is used to create or update the default storage class configuration for a bucket. | To be tested |
|  | SetBucketCustomedomain | OBS uses the PUT operation to set a user-defined domain name for a bucket. After the setting is successful, users can access the bucket using the user-defined domain name. | To be tested |
|  | SetBucketNotification | The OBS notification function helps notify you of important operations on buckets in a timely manner, ensuring that you know key events on buckets in a secure and timely manner. | To be tested |
|  | GetBucketNotification | Obtains the notification configuration information of a specified bucket. | To be tested |
|  | GetBucketEncryption | OBS uses the GET operation to obtain the encryption configuration of a specified bucket. | To be tested |
|  | DeleteBucketMirrorBackToSource | This API is used to delete an image retrieval policy from a specified bucket. If the deletion is successful, the return value of status code is 204. | To be tested |
|  | GetBucketObsCompressPolicy | This API is used to query the ZIP file decompression policy of a specified bucket. If the policy exists, a success message is returned, and the value of status code is 200. | To be tested |
|  | SetBucketLogging | When a bucket is created, bucket logs are not generated by default. To generate bucket logs, enable log configuration management for the bucket. After the bucket logging function is enabled, a log is generated for each operation on the bucket and multiple logs are packed into a log file. You can specify the location for storing log files when enabling the logging function for the bucket. You can save the log files to the bucket where the logging function is enabled or to another bucket where you have permission to save the log files. The log files must be in the same region as the bucket where the logging function is enabled. | To be tested |
|  | GetBucketStoragePolicy | Obtain the default storage class of the bucket. | To be tested |
|  | GetDirectcoldaccess | The bucket owner can obtain the direct read status of archived objects in a specified bucket. | To be tested |
|  | GetBucketLogging | This API is used to query the log management configuration of the current bucket. This method is implemented by using the get method of HTTP and adding logging sub-resources to return the logging configuration of the current bucket. | To be tested |
|  | GetBucketTagging | OBS uses the GET operation to obtain the tag of a specified bucket. | To be tested |
|  | DeleteBucketTagging |  | To be tested |
|  | SetBucketAcl | OBS supports permission control on bucket operations. By default, only the bucket creator has the read and write permissions on the bucket. You can also set other access policies. For example, you can set a public access policy for a bucket to allow all users to read the bucket. | To be tested |
|  | DeleteBucketPolicy | This API is used to delete a policy from a specified bucket by using the policy subresource. | To be tested |
| Basic operation on bucket | GetBucketLocation | Users with the read permission on a bucket can obtain the bucket location information. | To be tested |
|  | DeleteBucket | This operation is used to delete a specified bucket. Only the bucket owner or the user with the policy permission can delete a bucket. The bucket to be deleted must be an empty bucket. If the bucket contains objects or multipart upload tasks, the bucket is not empty. You can use the APIs for listing objects and multipart upload tasks to check whether the bucket is empty. | To be tested |
|  | ListBuckets | OBS users can query the bucket list created by themselves. | To be tested |
|  | CreateBucket | Creating a bucket is to create a bucket with the specified name. | To be tested |
|  | ListObjects | Users with the read permission on a bucket can obtain the object list in the bucket. | To be tested |
|  | GetBucketMetadata | Users with the read permission on a bucket can query whether the bucket metadata exists. | To be tested |
| Multipart operation | ListParts | Listing uploaded parts | To be tested |
|  | CopyPart | Copy part | To be tested |
|  | CompleteMultipartUpload | If a user uploads all parts, the user can invoke the part combination interface. The system merges the specified parts into a complete object on the server. Before performing the merge part operation, you cannot download the uploaded data. During part combination, the additional message header information recorded during the initialization of the multipart upload task needs to be copied to the object metadata. The processing is the same as the processing for common object uploading with these message headers. In the case of concurrent merge of segments, the Last Write Win policy is still followed, but the time of 'Last Write' is defined as the initialization time of the segment task. | To be tested |
|  | AbortMultipartUpload | Cancel a multipart upload task | To be tested |
|  | ListMultipartUploads | List initialized multipart tasks in a bucket. | To be tested |
|  | UploadPart | Upload part | To be tested |
|  | InitiateMultipartUpload | Initializing a part upload task | To be tested |
| Object operation | DeleteObjects | The batch object deletion feature is used to delete some objects in a bucket at a time. The deleted objects cannot be restored. When deleting objects in batches, the returned result must contain the deletion result of each object. OBS deletes objects in batches by synchronously deleting objects. The deletion result of each object is returned to the requesting user. | To be tested |
|  | UploadModifyObject | Modifying a write object is to modify an object in a specified file bucket from the specified location to other content. | To be tested |
|  | PutObject | After creating a bucket in OBS, you can perform the PUT operation to upload objects to the bucket. To upload an object, you need to add an object to a specified bucket. To upload an object, you must have the write permission on the bucket. | To be tested |
|  | SetObjectMetadata | You can use this API to add, modify, or delete metadata of an object that has been uploaded to a bucket. | To be tested |
|  | SetObjectAcl | OBS supports permission control on object operations. By default, only the creator of an object has read and write permissions on the object. You can also set other access policies. For example, you can set a public access policy for an object to allow all users to read the object. An object encrypted in SSE-KMS mode does not take effect across tenants even if an ACL is set. | To be tested |
|  | DeleteObject | Operation for deleting an object. If the object to be deleted does not exist, a success message is returned. | To be tested |
|  | GetObjectMetadata | Users with the read permission can run the HEAD operation command to obtain object metadata. The returned information contains object metadata. | To be tested |
|  | TruncateObject | Truncating an object in a specified file bucket is to truncate an object to the specified size. | To be tested |
|  | RestoreObject | To obtain the content of an Archive object, restore the object and then download the data. After an object is restored, a copy of the object in Standard storage class is generated. That is, both the copy of the object in Standard storage class and the copy of the object in Archive storage class exist. After the storage period of the restored object expires, the copy of the object in Standard storage class is automatically deleted. | To be tested |
|  | UploadObject | Uploading an object refers to adding an object to a specified bucket. To perform this operation, you must have the write permission on the bucket. | To be tested |
|  | GetObjectAcl | A user performs the operation of obtaining the ACL of an object. The returned information contains the permission control list of the specified object. To obtain the ACL of an object, you must have the permission to read the access control policy (ACP) of the object. | To be tested |
|  | GetObject | The GET operation downloads an object from the object storage. Before using the GET interface, ensure that you have the READ permission on the object. If the object owner grants the READ access permission to an anonymous user, the object can be accessed without using the authentication header field. | To be tested |
|  | RenameObject | Rename an object in a specified bucket to another object. | To be tested |
|  | AppendObject | Appending an object in a specified bucket is to add data to the tail of an object. If no object with the same object key value exists, a new object is created. | To be tested |
|  | CopyObject | The Copy Object feature is used to create a copy of an existing object on OBS. | To be tested |
| Query version operation | ListVersions | Query the version number supported by SMN open APIs. | To be tested |
| Static Website Hosting | SetBucketCors | CORS(Cross Origin Resource Sharing) is a standard mechanism proposed by W3C, which allows the configuration of cross-domain requests from clients. In common web page requests, the script and content of one website cannot interact with the script and content of another website due to the existence of the Same Origin Policy (SOP). | To be tested |
|  | DeleteBucketWebsite | Deletes the website configuration information of a specified bucket. | To be tested |
|  | DeleteBucketCors | This API is used to delete the CORS configuration information of a specified bucket. After the bucket and objects in the bucket are deleted, the bucket and objects in the bucket cannot be accessed by other URLs. | To be tested |
|  | GetBucketWebsite | Obtain the website configuration information about the bucket. | To be tested |
|  | SetBucketWebsite | OBS allows static web page resources, such as .html web page files, flash files, and audio and video files, to be stored in buckets. When a client accesses these object resources through the website access point of the bucket, the browser can directly parse the supported web page resources. Present to the end user. Typical application scenarios are as follows: | To be tested |
|  | CheckBucketOptions | OPTIONS, called pre-request, is a type of request sent by the client to the server. It is usually used to check whether the client has the permission to perform operations on the server. The client starts to perform subsequent requests only after the pre-request is successfully returned. | To be tested |
|  | CheckObjectOptions | OPTIONS, called pre-request, is a type of request sent by the client to the server. It is usually used to check whether the client has the permission to perform operations on the server. The client starts to perform subsequent requests only after the pre-request is successfully returned. | To be tested |
|  | GetBucketCors | Obtains the CORS configuration information of a specified bucket. | To be tested |

