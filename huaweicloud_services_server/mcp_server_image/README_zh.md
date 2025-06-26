# Image MCP Server 


## Version
v0.1.0

## Overview

Image MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service Image. Full-chain management of Image resources can be carried out based on natural language.

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
                    <td rowspan="1">主体识别</td>
                    <td>RunImageMainObjectDetection</td>
                    <td>检测图像中的主要内容,返回主要内容的坐标信息,这里的主要内容包括两方面:bounding_box和main_object_box</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">名人识别</td>
                    <td>RunCelebrityRecognition</td>
                    <td>分析并识别图片中包含的政治人物、明星及网红人物,返回人物信息及人脸坐标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">图像标签</td>
                    <td>RunImageTagging</td>
                    <td>自然图像的语义内容非常丰富,一个图像包含多个标签内容,图像标签服务准确识别自然图片中数百种场景、上千种通用物体及其属性,让智能相册管理、照片检索和分类、基于场景内容或者物体的广告推荐等功能更加直观。使用时用户发送待处理图片,返回图片标签内容及相应置信度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">媒资图像标签(分类)</td>
                    <td>RunImageMediaTagging</td>
                    <td>自然图像的语义内容非常丰富,一个图像包含多个标签内容,图像标签服务准确识别自然图片中数百种场景、上千种通用物体及其属性,让智能相册管理、照片检索和分类、基于场景内容或者物体的广告推荐等功能更加直观。使用时用户发送待处理图片,返回图片标签内容及相应置信度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">媒资图像标签(检测)</td>
                    <td>RunImageMediaTaggingDet</td>
                    <td>自然图像的语义内容非常丰富,一个图像包含多个标签内容,图像标签服务准确识别自然图片中数百种场景、上千种通用物体及其属性,让智能相册管理、照片检索和分类、基于场景内容或者物体的广告推荐等功能更加直观。使用时用户发送待处理图片,返回图片标签内容及相应的位置坐标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">翻拍识别</td>
                    <td>RunRecaptureDetect</td>
                    <td>零售行业通常根据零售店的销售量进行销售奖励,拍摄售出商品的条形码上传后台是常用的统计方式。翻拍识别利用深度神经网络算法判断条形码图片为原始拍摄,还是经过二次翻拍、打印翻拍等手法二次处理的图片。利用翻拍识别,可以检测出经过二次处理的不合规范图片,使得统计数据更准确、有效。。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
