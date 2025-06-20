# IMS MCP Server 


## Version
v0.1.0

## Overview

IMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IMS. Full-chain management of IMS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Image (Native OpenStack API) | GlanceShowImage | Query details about a single image. You can use this API to query details about a single private or public image. | To be tested |
|  | GlanceUpdateImage | Modifying image information | To be tested |
|  | GlanceCreateImageMetadata | Creates image metadata. After the API for creating image metadata is invoked successfully, only the image metadata is created, but the image file corresponding to the image does not exist. | To be tested |
|  | GlanceDeleteImage | This API is used to delete an image. You can use this API to delete your own private image. | To be tested |
|  | GlanceListImages | Obtain the image list. | To be tested |
| Image Quota | ShowImageQuota | This API is an extended API and is used to query the quota of private images of a tenant in the current region. | To be tested |
| Image Sharing (Native OpenStack API) | GlanceShowImageMember | This API is used to query details about an image member in image sharing. | To be tested |
|  | GlanceAddImageMember | When a user shares an image with another user, this API is used to add the project ID of the user who accepts the image to the image members. | To be tested |
|  | GlanceDeleteImageMember | This API is used to cancel the image sharing of a user. | To be tested |
|  | GlanceListImageMembers | This API is used to obtain the list of members who accept the image during image sharing. | To be tested |
|  | GlanceUpdateImageMember | When a user accepts or rejects an image sharing, this API is used to update the image member status. | To be tested |
| Image Tag | ListTags | Query the image tag list based on different conditions. | To be tested |
|  | BatchAddOrDeleteTags | This API is used to add or update tags or delete tags for specified images in batches. | To be tested |
|  | AddImageTag | This API is used to add or update a specified tag to a specified image. | To be tested |
|  | ListImagesTags | This API is used to query tags on all images of a tenant. | To be tested |
|  | ListImageTags | This API is used to query all tags on a specified image. | To be tested |
|  | ListImageByTags | This API is used to filter or count images by label or other conditions. | To be tested |
|  | CreateOrUpdateTags | This API is used to add or modify a custom tag for an image. You can use custom tags to classify images. | To be tested |
|  | DeleteImageTag | This API is used to delete a specified tag from an image. | To be tested |
| Image Tag (Native OpenStack API) | GlanceDeleteTag | This API is used to delete the custom tags of an image. You can use this API to delete unnecessary tags from a private image. | To be tested |
|  | GlanceCreateTag | This API is used to add a custom tag to an image. Users can use custom tags to classify images. | To be tested |
| Image sharing | BatchUpdateMembers | This API is an extended API. It is used to update the status of multiple image members in batches when a user accepts or rejects multiple shared images. | To be tested |
|  | BatchAddMembers | This API is an extended API and is used to share multiple images with multiple users during image sharing. | To be tested |
|  | ListImageMembers | This API is used to obtain the list of members who accept the image during image sharing. | To be tested |
|  | ShowImageMember | This API is used to query details about an image member in image sharing. | To be tested |
|  | BatchDeleteMembers | This API is an extended API and is used to cancel image sharing. | To be tested |
| Image view (Native OpenStack API) | GlanceListImageSchemas | This API is used to query the image list view. By using this API, you can learn the details and data structure of the image list. | To be tested |
|  | GlanceListImageMemberSchemas | This API is used to query the image member list view. With the view, you can learn the attributes of an image member and the data type of each attribute. | To be tested |
|  | GlanceShowImageMemberSchemas | This API is used to query the image member view. Through the view, you can learn the attributes of an image member and the data type of each attribute. | To be tested |
|  | GlanceShowImageSchemas | This API is used to query the image view. Through the view, you can learn the attributes of an image and the data type of each attribute. | To be tested |
| Mirror | UpdateImage | This API is used to update image information. This API is used to modify image attributes. Currently, only images in the active state can be updated. | To be tested |
|  | ListOsVersions | Query the OS compatibility list of ECSs in the current region. | To be tested |
|  | CreateDataImage | Use the external data volume image file uploaded to the OBS bucket to create a data image. As an asynchronous interface, if the interface is invoked successfully, the background receives the creation request. To check whether the image is created successfully, you need to query the execution status of the task through the asynchronous task query interface. For details, see Asynchronous Task Query. | To be tested |
|  | RegisterImage | This API is used to register an image file as an uninitialized private image on the cloud platform. | To be tested |
|  | CreateWholeImage | Use an ECS or a CSS backup to create a full-ECS image. If the API is invoked successfully, the background has received the request for creating a full-ECS image. To check whether the image is successfully created, you need to query the execution status of the task through the API for querying asynchronous tasks. For details, see Querying Asynchronous Tasks. | To be tested |
|  | ExportImage | This API is an extended API. It is used to export private images to a specified OBS bucket. | To be tested |
|  | ListImages | Query the image list based on different conditions. | To be tested |
|  | CreateImage | This API is used to create private images. The following functions are supported: | To be tested |
|  | ImportImageQuick | Create a private image using a large external image file uploaded to an OBS bucket. Currently, only RAW or ZVHD2 image files are supported. The size of the image file cannot exceed 1 TB. | To be tested |
| Mirror Replication | CopyImageCrossRegion | This API is an extended API. You can copy a private image created in a region to another region and provision ECSs of the same type in the region, helping you migrate services between regions. | To be tested |
|  | CopyImageInRegion | This API is an extended API. It is used to copy an existing image to another image. When copying an image, you can change the image attributes such as encryption to meet the requirements of different scenarios. | To be tested |
| Mirror Task | ShowJob | This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task. | To be tested |
|  | ShowJobProgress | This interface is an extended interface and is used to query the progress of an asynchronous task. | To be tested |
| Query the API version information about the CMK | ShowVersion | -Function description: This API is used to query the version information of a specified API. | To be tested |
| Query version operation | ListVersions | Query the version number supported by SMN open APIs. | To be tested |
| Tag Management | BatchDeleteTags | This API is used to delete tags for a specified protected instance in batches. A maximum of 10 labels can be placed on a resource. | To be tested |

