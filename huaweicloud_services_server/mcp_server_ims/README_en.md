# IMS MCP Server 


## Version
v0.1.0

## Overview

IMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IMS. Full-chain management of IMS resources can be carried out based on natural language.

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
                    <td rowspan="5">Image (Native OpenStack API)</td>
                    <td>GlanceShowImage</td>
                    <td>Query details about a single image. You can use this API to query details about a single private or public image.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceUpdateImage</td>
                    <td>Modifying image information</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceCreateImageMetadata</td>
                    <td>Creates image metadata. After the API for creating image metadata is invoked successfully, only the image metadata is created, but the image file corresponding to the image does not exist.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceDeleteImage</td>
                    <td>This API is used to delete an image. You can use this API to delete your own private image.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceListImages</td>
                    <td>Obtain the image list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Image Quota</td>
                    <td>ShowImageQuota</td>
                    <td>This API is an extended API and is used to query the quota of private images of a tenant in the current region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Image Sharing (Native OpenStack API)</td>
                    <td>GlanceShowImageMember</td>
                    <td>This API is used to query details about an image member in image sharing.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceAddImageMember</td>
                    <td>When a user shares an image with another user, this API is used to add the project ID of the user who accepts the image to the image members.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceDeleteImageMember</td>
                    <td>This API is used to cancel the image sharing of a user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceListImageMembers</td>
                    <td>This API is used to obtain the list of members who accept the image during image sharing.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceUpdateImageMember</td>
                    <td>When a user accepts or rejects an image sharing, this API is used to update the image member status.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Image Tag</td>
                    <td>ListTags</td>
                    <td>Query the image tag list based on different conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddOrDeleteTags</td>
                    <td>This API is used to add or update tags or delete tags for specified images in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddImageTag</td>
                    <td>This API is used to add or update a specified tag to a specified image.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImagesTags</td>
                    <td>This API is used to query tags on all images of a tenant.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageTags</td>
                    <td>This API is used to query all tags on a specified image.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageByTags</td>
                    <td>This API is used to filter or count images by label or other conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrUpdateTags</td>
                    <td>This API is used to add or modify a custom tag for an image. You can use custom tags to classify images.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteImageTag</td>
                    <td>This API is used to delete a specified tag from an image.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Image Tag (Native OpenStack API)</td>
                    <td>GlanceDeleteTag</td>
                    <td>This API is used to delete the custom tags of an image. You can use this API to delete unnecessary tags from a private image.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceCreateTag</td>
                    <td>This API is used to add a custom tag to an image. Users can use custom tags to classify images.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Image sharing</td>
                    <td>BatchUpdateMembers</td>
                    <td>This API is an extended API. It is used to update the status of multiple image members in batches when a user accepts or rejects multiple shared images.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddMembers</td>
                    <td>This API is an extended API and is used to share multiple images with multiple users during image sharing.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageMembers</td>
                    <td>This API is used to obtain the list of members who accept the image during image sharing.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageMember</td>
                    <td>This API is used to query details about an image member in image sharing.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteMembers</td>
                    <td>This API is an extended API and is used to cancel image sharing.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Image view (Native OpenStack API)</td>
                    <td>GlanceListImageSchemas</td>
                    <td>This API is used to query the image list view. By using this API, you can learn the details and data structure of the image list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceListImageMemberSchemas</td>
                    <td>This API is used to query the image member list view. With the view, you can learn the attributes of an image member and the data type of each attribute.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceShowImageMemberSchemas</td>
                    <td>This API is used to query the image member view. Through the view, you can learn the attributes of an image member and the data type of each attribute.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceShowImageSchemas</td>
                    <td>This API is used to query the image view. Through the view, you can learn the attributes of an image and the data type of each attribute.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Mirror</td>
                    <td>UpdateImage</td>
                    <td>This API is used to update image information. This API is used to modify image attributes. Currently, only images in the active state can be updated.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOsVersions</td>
                    <td>Query the OS compatibility list of ECSs in the current region.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataImage</td>
                    <td>Use the external data volume image file uploaded to the OBS bucket to create a data image. As an asynchronous interface, if the interface is invoked successfully, the background receives the creation request. To check whether the image is created successfully, you need to query the execution status of the task through the asynchronous task query interface. For details, see Asynchronous Task Query.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterImage</td>
                    <td>This API is used to register an image file as an uninitialized private image on the cloud platform.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWholeImage</td>
                    <td>Use an ECS or a CSS backup to create a full-ECS image. If the API is invoked successfully, the background has received the request for creating a full-ECS image. To check whether the image is successfully created, you need to query the execution status of the task through the API for querying asynchronous tasks. For details, see Querying Asynchronous Tasks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportImage</td>
                    <td>This API is an extended API. It is used to export private images to a specified OBS bucket.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImages</td>
                    <td>Query the image list based on different conditions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateImage</td>
                    <td>This API is used to create private images. The following functions are supported:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportImageQuick</td>
                    <td>Create a private image using a large external image file uploaded to an OBS bucket. Currently, only RAW or ZVHD2 image files are supported. The size of the image file cannot exceed 1 TB.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Mirror Replication</td>
                    <td>CopyImageCrossRegion</td>
                    <td>This API is an extended API. You can copy a private image created in a region to another region and provision ECSs of the same type in the region, helping you migrate services between regions.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyImageInRegion</td>
                    <td>This API is an extended API. It is used to copy an existing image to another image. When copying an image, you can change the image attributes such as encryption to meet the requirements of different scenarios.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Mirror Task</td>
                    <td>ShowJob</td>
                    <td>This API is an extended API and is used to query the execution status of an asynchronous API, for example, the execution status of an image export task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobProgress</td>
                    <td>This interface is an extended interface and is used to query the progress of an asynchronous task.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query the API version information about the CMK</td>
                    <td>ShowVersion</td>
                    <td>-Function description: This API is used to query the version information of a specified API.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Query version operation</td>
                    <td>ListVersions</td>
                    <td>Query the version number supported by SMN open APIs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tag Management</td>
                    <td>BatchDeleteTags</td>
                    <td>This API is used to delete tags for a specified protected instance in batches. A maximum of 10 labels can be placed on a resource.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
