# DSC MCP Server 


## Version
v0.1.0

## Overview

DSC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DSC. Full-chain management of DSC resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| API Invoking Record | ShowOpenApiCalledRecords | Query OpenApi invoking records | To be tested |
| Alarm notification | UpdateDefaultTopic | Modifies the associated project ID, notification topic, and notification status (0 indicates that notification is disabled and 1 indicates that notification is enabled) of the alarm notification. | To be tested |
|  | ShowTopics | Query alarm notification topics. The default topics, number of confirmed topics, and list are returned. | To be tested |
| Asset Management | AddBuckets | Add data asset scanning authorization | To be tested |
|  | UpdateAssetName | Editing the data asset name | To be tested |
| Basic operation on bucket | ListBuckets | OBS users can query the bucket list created by themselves. | To be tested |
|  | DeleteBucket | This operation is used to delete a specified bucket. Only the bucket owner or the user with the policy permission can delete a bucket. The bucket to be deleted must be an empty bucket. If the bucket contains objects or multipart upload tasks, the bucket is not empty. You can use the APIs for listing objects and multipart upload tasks to check whether the bucket is empty. | To be tested |
| Data static anonymization | ChangeDbTemplateOperation | Start or stop an anonymization task | To be tested |
|  | ListDbMaskTask | Query the list of anonymization tasks. | To be tested |
| Data watermark | CreateDatabaseWaterMark | Dynamic watermarking for data in the JSON body | To be tested |
|  | ShowDatabaseWaterMark | Extract the watermark content from the request data | To be tested |
| Document Watermark | CreateDocWatermark | Enembeds a dark text watermark, clear text watermark, or clear image watermark for a WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf) file. The user transfers the file to be watermarked and watermark information in formData format. After the DSC service adds the watermark to the file, the DSC service returns the binary stream of the watermarked file to the user. | To be tested |
|  | ShowDocWatermark | Extract the dark watermarks from the WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf) document that has the dark watermark embedded. The user transfers the file to be extracted in formData format. The DSC service returns the text watermark content extracted from the document in JSON format. | To be tested |
|  | ShowDocWatermarkByAddress | Watermark extraction is supported for WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf) documents with dark watermark embedded. Users can enter the address of the document from which the watermark is to be extracted (OBS is supported currently). The DSC service returns the text watermark content extracted from the document in JSON format. | To be tested |
|  | CreateDocWatermarkByAddress | Encrypts a dark watermark, clear watermark, or clear image watermark for WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf)* documents. Users can enter the address of the document to be watermarked (OBS is supported currently) and watermark information. After the DSC service adds a watermark to the document, the DSC service returns the address for storing the watermarked document to the user. | To be tested |
| Dynamic data anonymization | BatchAddDataMask | Data anonymization | To be tested |
| Picture watermark | CreateImageWatermark | To embed a dark text watermark or image watermark into an image, the user transfers the image to be watermarked and the watermark related information in formData format. The DSC service adds the watermark to the image and returns the watermarked binary stream to the user. Currently, the supported image format is *.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif. | To be tested |
|  | ShowImageWatermarkWithImage | Extracts the watermark from an image that has an image watermark embedded. The user transfers the image in formData format. The DSC service returns the extracted image watermark in binary image format. Currently, the supported image format is *.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif. | To be tested |
|  | ShowImageWatermarkByAddress | Extracts dark watermarks from images that have embedded dark watermarks in the specified storage address (HWS currently supported). The supported image format is *.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif. | To be tested |
|  | ShowImageWatermarkWithImageByAddress | Extracts a dark watermark from an image that has been embedded with a dark watermark in the specified storage address (HWS currently supported). The extracted watermark is stored in the specified location (HWS currently supported). The supported image format is *.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif. | To be tested |
|  | CreateImageWatermarkByAddress | Encrypts a dark watermark or image watermark into the image at the specified storage address (HWS OBS is supported currently). The embedded watermarked image will be stored in the specified location (HWS OBS is supported currently). The supported image format is *.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif. | To be tested |
|  | ShowImageWatermark | Extracts the watermark from an image that has embedded a text dark watermark. The DSC service transfers the image whose watermark is to be extracted in formData format. The DSC service returns the text dark watermark extracted from the image in JSON format. Currently, the supported image format is *.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif. | To be tested |
| Resource management | ShowSpecification | Query resource provisioning information and order details based on the project ID. | To be tested |
|  | CreateProductOrder | Order instances based on the charging mode and charging period. | To be tested |
| Rule engine | DeleteRule | Delete a rule | To be tested |
| Sensitive data discovery | AddRuleGroup | Create a sensitive data scanning rule group based on the specified rule group name and scanning rule list. | To be tested |
|  | DeleteScanJob | Delete a scanning task | To be tested |
|  | DeleteRuleGroup | Deletes a specified scanning rule group based on the scanning rule group ID. | To be tested |
|  | ChangeRule | Modifying a user-defined sensitive data identification rule | To be tested |
|  | ShowRules | Query the scanning rule list. The total number of scanning rules and the scanning rule list are returned. | To be tested |
|  | ShowScanJobResults | Query the scanning result of a specified task | To be tested |
|  | ShowScanJobs | Query the scanning task list | To be tested |
|  | ListRuleGroups | Query the scanning rule group list based on the specified project ID | To be tested |
|  | AddScanJob | Create a scanning task based on the specified task name, scanning mode, scanning period, scanning rule group, and scanning time. | To be tested |
|  | AddRule | Create a user-defined sensitive data identification rule based on the specified parameters, such as the rule name, rule type, risk level, and minimum number of matching times. | To be tested |

