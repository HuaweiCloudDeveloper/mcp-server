# FRS MCP Server 


## Version
v0.1.0

## Overview

FRS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service FRS. Full-chain management of FRS resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Action liveness detection | DetectLiveByFile | Action liveness detection determines whether a person in a video is alive by checking whether the person's actions in the video are consistent with the transferred action list. If multiple faces appear, the largest face is selected for judgment. | To be tested |
|  | DetectLiveByUrl | Action liveness detection determines whether a person in a video is alive by checking whether the person's actions in the video are consistent with the transferred action list. If multiple faces appear, the largest face is selected for judgment. | To be tested |
|  | DetectLiveByBase64 | Action liveness detection determines whether a person in a video is alive by checking whether the person's actions in the video are consistent with the transferred action list. If multiple faces appear, the largest face is selected for judgment. | To be tested |
| Face Match | CompareFaceByFile | Face comparison is to compare two faces to determine whether they are the same person and return the comparison confidence. If the transferred image contains multiple faces, the largest face image is selected for comparison. | To be tested |
|  | CompareFaceByUrl | Face comparison is to compare two faces to determine whether they are the same person and return the comparison confidence. If the transferred image contains multiple faces, the largest face image is selected for comparison. | To be tested |
|  | CompareFaceByBase64 | Face comparison is to compare two faces to determine whether they are the same person and return the comparison confidence. If the transferred image contains multiple faces, the largest face image is selected for comparison. | To be tested |
| Face detection | DetectFaceByFile | Face detection is to detect and analyze the face in the input image, and output the position of the face in the image, the position of the face key points, and the key attributes of the face. | To be tested |
|  | DetectFaceByUrl | Face detection is to detect and analyze the face in the input image, and output the position of the face in the image, the position of the face key points, and the key attributes of the face. | To be tested |
|  | DetectFaceByBase64 | Face detection is to detect and analyze the face in the input image, and output the position of the face in the image, the position of the face key points, and the key attributes of the face. | To be tested |
| Face library resource management | ShowAllFaceSets | Query the status of all face libraries of the current user. | To be tested |
|  | ShowFaceSet | Query the current status of the face library. | To be tested |
|  | DeleteFaceSet | Delete the face library and all faces in the library. | To be tested |
|  | CreateFaceSet | Create a face library for storing facial features. You can create a maximum of 10 face libraries. Each face library supports a maximum of 100,000 face features. If you need a larger specification, please contact customer service. | To be tested |
| Face resource management | UpdateFace | Updates the information about a single face based on the face ID (face_id). | To be tested |
|  | AddFacesByBase64 | Add a face image to the face library. Add the face image in a single image to the face image library. The maximum number of faces or all faces can be added. | To be tested |
|  | AddFacesByFile | Add a face image to the face library. Add the face image in a single image to the face image library. The maximum number of faces or all faces can be added. | To be tested |
|  | ShowFacesByLimit | Query face information in a specified face library. | To be tested |
|  | DeleteFaceByFaceId | This API is used to delete a face based on the face ID. | To be tested |
|  | DeleteFaceByExternalImageId | Delete a face based on the external_image_id value. | To be tested |
|  | ShowFacesByFaceId | Query face information in a specified face library. | To be tested |
|  | AddFacesByUrl | Add a face image to the face library. Adds the face image in a single image to the face image library. The maximum number of faces or all faces can be added. | To be tested |
|  | BatchDeleteFaces | User-defined filter criteria to delete multiple faces that meet the specified conditions from the face library in batches. | To be tested |
| Face search | SearchFaceByFaceId | Face search is to query one or more faces similar to the target face in the existing face library and return the corresponding confidence level. | To be tested |
|  | SearchFaceByBase64 | Face search is to query one or more faces similar to the target face in the existing face library and return the corresponding confidence level. | To be tested |
|  | SearchFaceByUrl | Face search is to query one or more faces similar to the target face in the existing face library and return the corresponding confidence level. | To be tested |
|  | SearchFaceByFile | Face search is to query one or more faces similar to the target face in the existing face library and return the corresponding confidence level. | To be tested |
| Silent liveness test | DetectLiveFaceByFile | Silent Liveness Detection determines whether a face in a face image is from a real person based on possible information such as distortion, moire, reflection, reflection, and frame in the face image. Effectively defend against various attacks such as paper flipping, electronic flipping, and video reshooting. Silent liveness detection supports a single image, but does not support multiple face images. | To be tested |
|  | DetectLiveFaceByUrl | Silent Liveness Detection determines whether a face in a face image is from a real person based on possible information such as distortion, moire, reflection, reflection, and frame in the face image. Effectively defend against various attacks such as paper flipping, electronic flipping, and video reshooting. Silent liveness detection supports a single image, but does not support multiple face images. | To be tested |
|  | DetectLiveFaceByBase64 | Silent Liveness Detection determines whether a face in the face image is a real person based on the possible distortion, moir grain, reflection, reflection, and frame information in the face image. Effectively defend against various attacks such as paper flipping, electronic flipping, and video reshooting. Silent liveness detection supports a single image, but does not support multiple face images. | To be tested |

