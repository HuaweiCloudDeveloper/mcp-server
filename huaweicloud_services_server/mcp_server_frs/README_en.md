# FRS MCP Server 


## Version
v0.1.0

## Overview

FRS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service FRS. Full-chain management of FRS resources can be carried out based on natural language.

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
                    <td rowspan="3">Action liveness detection</td>
                    <td>DetectLiveByFile</td>
                    <td>Action liveness detection determines whether a person in a video is alive by checking whether the person's actions in the video are consistent with the transferred action list. If multiple faces appear, the largest face is selected for judgment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectLiveByUrl</td>
                    <td>Action liveness detection determines whether a person in a video is alive by checking whether the person's actions in the video are consistent with the transferred action list. If multiple faces appear, the largest face is selected for judgment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectLiveByBase64</td>
                    <td>Action liveness detection determines whether a person in a video is alive by checking whether the person's actions in the video are consistent with the transferred action list. If multiple faces appear, the largest face is selected for judgment.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Face Match</td>
                    <td>CompareFaceByFile</td>
                    <td>Face comparison is to compare two faces to determine whether they are the same person and return the comparison confidence. If the transferred image contains multiple faces, the largest face image is selected for comparison.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CompareFaceByUrl</td>
                    <td>Face comparison is to compare two faces to determine whether they are the same person and return the comparison confidence. If the transferred image contains multiple faces, the largest face image is selected for comparison.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CompareFaceByBase64</td>
                    <td>Face comparison is to compare two faces to determine whether they are the same person and return the comparison confidence. If the transferred image contains multiple faces, the largest face image is selected for comparison.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Face detection</td>
                    <td>DetectFaceByFile</td>
                    <td>Face detection is to detect and analyze the face in the input image, and output the position of the face in the image, the position of the face key points, and the key attributes of the face.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectFaceByUrl</td>
                    <td>Face detection is to detect and analyze the face in the input image, and output the position of the face in the image, the position of the face key points, and the key attributes of the face.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectFaceByBase64</td>
                    <td>Face detection is to detect and analyze the face in the input image, and output the position of the face in the image, the position of the face key points, and the key attributes of the face.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Face library resource management</td>
                    <td>ShowAllFaceSets</td>
                    <td>Query the status of all face libraries of the current user.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFaceSet</td>
                    <td>Query the current status of the face library.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFaceSet</td>
                    <td>Delete the face library and all faces in the library.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFaceSet</td>
                    <td>Create a face library for storing facial features. You can create a maximum of 10 face libraries. Each face library supports a maximum of 100,000 face features. If you need a larger specification, please contact customer service.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Face resource management</td>
                    <td>UpdateFace</td>
                    <td>Updates the information about a single face based on the face ID (face_id).</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddFacesByBase64</td>
                    <td>Add a face image to the face library. Add the face image in a single image to the face image library. The maximum number of faces or all faces can be added.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddFacesByFile</td>
                    <td>Add a face image to the face library. Add the face image in a single image to the face image library. The maximum number of faces or all faces can be added.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFacesByLimit</td>
                    <td>Query face information in a specified face library.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFaceByFaceId</td>
                    <td>This API is used to delete a face based on the face ID.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFaceByExternalImageId</td>
                    <td>Delete a face based on the external_image_id value.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFacesByFaceId</td>
                    <td>Query face information in a specified face library.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddFacesByUrl</td>
                    <td>Add a face image to the face library. Adds the face image in a single image to the face image library. The maximum number of faces or all faces can be added.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteFaces</td>
                    <td>User-defined filter criteria to delete multiple faces that meet the specified conditions from the face library in batches.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Face search</td>
                    <td>SearchFaceByFaceId</td>
                    <td>Face search is to query one or more faces similar to the target face in the existing face library and return the corresponding confidence level.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchFaceByBase64</td>
                    <td>Face search is to query one or more faces similar to the target face in the existing face library and return the corresponding confidence level.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchFaceByUrl</td>
                    <td>Face search is to query one or more faces similar to the target face in the existing face library and return the corresponding confidence level.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchFaceByFile</td>
                    <td>Face search is to query one or more faces similar to the target face in the existing face library and return the corresponding confidence level.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Silent liveness test</td>
                    <td>DetectLiveFaceByFile</td>
                    <td>Silent Liveness Detection determines whether a face in a face image is from a real person based on possible information such as distortion, moire, reflection, reflection, and frame in the face image. Effectively defend against various attacks such as paper flipping, electronic flipping, and video reshooting. Silent liveness detection supports a single image, but does not support multiple face images.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectLiveFaceByUrl</td>
                    <td>Silent Liveness Detection determines whether a face in a face image is from a real person based on possible information such as distortion, moire, reflection, reflection, and frame in the face image. Effectively defend against various attacks such as paper flipping, electronic flipping, and video reshooting. Silent liveness detection supports a single image, but does not support multiple face images.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectLiveFaceByBase64</td>
                    <td>Silent Liveness Detection determines whether a face in the face image is a real person based on the possible distortion, moir grain, reflection, reflection, and frame information in the face image. Effectively defend against various attacks such as paper flipping, electronic flipping, and video reshooting. Silent liveness detection supports a single image, but does not support multiple face images.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
