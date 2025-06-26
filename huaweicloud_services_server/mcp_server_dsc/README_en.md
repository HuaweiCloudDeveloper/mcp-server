# DSC MCP Server 


## Version
v0.1.0

## Overview

DSC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DSC. Full-chain management of DSC resources can be carried out based on natural language.

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
                    <td rowspan="1">API Invoking Record</td>
                    <td>ShowOpenApiCalledRecords</td>
                    <td>Query OpenApi invoking records</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Alarm notification</td>
                    <td>UpdateDefaultTopic</td>
                    <td>Modifies the associated project ID, notification topic, and notification status (0 indicates that notification is disabled and 1 indicates that notification is enabled) of the alarm notification.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTopics</td>
                    <td>Query alarm notification topics. The default topics, number of confirmed topics, and list are returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Asset Management</td>
                    <td>AddBuckets</td>
                    <td>Add data asset scanning authorization</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAssetName</td>
                    <td>Editing the data asset name</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Basic operation on bucket</td>
                    <td>ListBuckets</td>
                    <td>OBS users can query the bucket list created by themselves.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBucket</td>
                    <td>This operation is used to delete a specified bucket. Only the bucket owner or the user with the policy permission can delete a bucket. The bucket to be deleted must be an empty bucket. If the bucket contains objects or multipart upload tasks, the bucket is not empty. You can use the APIs for listing objects and multipart upload tasks to check whether the bucket is empty.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Data static anonymization</td>
                    <td>ChangeDbTemplateOperation</td>
                    <td>Start or stop an anonymization task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbMaskTask</td>
                    <td>Query the list of anonymization tasks.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Data watermark</td>
                    <td>CreateDatabaseWaterMark</td>
                    <td>Dynamic watermarking for data in the JSON body</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatabaseWaterMark</td>
                    <td>Extract the watermark content from the request data</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Document Watermark</td>
                    <td>CreateDocWatermark</td>
                    <td>Enembeds a dark text watermark, clear text watermark, or clear image watermark for a WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf) file. The user transfers the file to be watermarked and watermark information in formData format. After the DSC service adds the watermark to the file, the DSC service returns the binary stream of the watermarked file to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDocWatermark</td>
                    <td>Extract the dark watermarks from the WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf) document that has the dark watermark embedded. The user transfers the file to be extracted in formData format. The DSC service returns the text watermark content extracted from the document in JSON format.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDocWatermarkByAddress</td>
                    <td>Watermark extraction is supported for WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf) documents with dark watermark embedded. Users can enter the address of the document from which the watermark is to be extracted (OBS is supported currently). The DSC service returns the text watermark content extracted from the document in JSON format.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDocWatermarkByAddress</td>
                    <td>Encrypts a dark watermark, clear watermark, or clear image watermark for WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf)* documents. Users can enter the address of the document to be watermarked (OBS is supported currently) and watermark information. After the DSC service adds a watermark to the document, the DSC service returns the address for storing the watermarked document to the user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Dynamic data anonymization</td>
                    <td>BatchAddDataMask</td>
                    <td>Data anonymization</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Picture watermark</td>
                    <td>CreateImageWatermark</td>
                    <td>To embed a dark text watermark or image watermark into an image, the user transfers the image to be watermarked and the watermark related information in formData format. The DSC service adds the watermark to the image and returns the watermarked binary stream to the user. Currently, the supported image format is *.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageWatermarkWithImage</td>
                    <td>Extracts the watermark from an image that has an image watermark embedded. The user transfers the image in formData format. The DSC service returns the extracted image watermark in binary image format. Currently, the supported image format is *.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageWatermarkByAddress</td>
                    <td>Extracts dark watermarks from images that have embedded dark watermarks in the specified storage address (HWS currently supported). The supported image format is *.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageWatermarkWithImageByAddress</td>
                    <td>Extracts a dark watermark from an image that has been embedded with a dark watermark in the specified storage address (HWS currently supported). The extracted watermark is stored in the specified location (HWS currently supported). The supported image format is *.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateImageWatermarkByAddress</td>
                    <td>Encrypts a dark watermark or image watermark into the image at the specified storage address (HWS OBS is supported currently). The embedded watermarked image will be stored in the specified location (HWS OBS is supported currently). The supported image format is *.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageWatermark</td>
                    <td>Extracts the watermark from an image that has embedded a text dark watermark. The DSC service transfers the image whose watermark is to be extracted in formData format. The DSC service returns the text dark watermark extracted from the image in JSON format. Currently, the supported image format is *.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Resource management</td>
                    <td>ShowSpecification</td>
                    <td>Query resource provisioning information and order details based on the project ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProductOrder</td>
                    <td>Order instances based on the charging mode and charging period.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Rule engine</td>
                    <td>DeleteRule</td>
                    <td>Delete a rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Sensitive data discovery</td>
                    <td>AddRuleGroup</td>
                    <td>Create a sensitive data scanning rule group based on the specified rule group name and scanning rule list.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScanJob</td>
                    <td>Delete a scanning task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRuleGroup</td>
                    <td>Deletes a specified scanning rule group based on the scanning rule group ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeRule</td>
                    <td>Modifying a user-defined sensitive data identification rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRules</td>
                    <td>Query the scanning rule list. The total number of scanning rules and the scanning rule list are returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScanJobResults</td>
                    <td>Query the scanning result of a specified task</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScanJobs</td>
                    <td>Query the scanning task list</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRuleGroups</td>
                    <td>Query the scanning rule group list based on the specified project ID</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddScanJob</td>
                    <td>Create a scanning task based on the specified task name, scanning mode, scanning period, scanning rule group, and scanning time.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddRule</td>
                    <td>Create a user-defined sensitive data identification rule based on the specified parameters, such as the rule name, rule type, risk level, and minimum number of matching times.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
