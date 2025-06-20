# Image MCP Server 


## Version
v0.1.0

## Overview

Image MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service Image. Full-chain management of Image resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Celebrity Recognition | RunCelebrityRecognition | Analyzes and identifies politicians, stars, and celebrities in the image, and returns the person information and face coordinates. | To be tested |
| Image Label | RunImageTagging | Natural images have rich semantic content. An image contains multiple tags. The image tag service accurately identifies hundreds of scenarios, thousands of common objects, and their attributes. Make intelligent album management, photo retrieval and classification, and advertising recommendations based on scene content or objects more intuitive. When the user sends a picture to be processed, the image label content and the corresponding confidence level are returned. | To be tested |
| Media asset image label (category) | RunImageMediaTagging | Natural images have rich semantic content. An image contains multiple tags. The image tag service accurately identifies hundreds of scenarios, thousands of common objects, and their attributes. Make intelligent album management, photo retrieval and classification, and advertising recommendations based on scene content or objects more intuitive. When the user sends a picture to be processed, the image label content and the corresponding confidence level are returned. | To be tested |
| Media asset image label (detection) | RunImageMediaTaggingDet | Natural images have rich semantic content. An image contains multiple tags. The image tag service accurately identifies hundreds of scenarios, thousands of common objects, and their attributes. Make intelligent album management, photo retrieval and classification, and ad recommendation based on scene content or object more intuitive. When the user sends the image to be processed, the image label content and the corresponding position coordinates are returned. | To be tested |
| Remake Identification | RunRecaptureDetect | In the retail industry, sales rewards are usually provided based on the sales volume of retail stores. It is a common statistical method to shoot the barcodes of sold goods and upload them to the background. The deep neural network algorithm is used to determine whether a barcode image is an original image or a second image that has been rephotographed or printed. By using the remake recognition, we can detect the non-standard pictures after secondary processing, so that the statistics data is more accurate and effective. | To be tested |
| Subject Identification | RunImageMainObjectDetection | Detects the main content in the image and returns the coordinate information of the main content. The main content includes bounding_box and main_object_box. | To be tested |

