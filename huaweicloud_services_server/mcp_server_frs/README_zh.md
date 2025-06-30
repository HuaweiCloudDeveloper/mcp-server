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
                    <td rowspan="4">人脸库资源管理</td>
                    <td>ShowAllFaceSets</td>
                    <td>查询当前用户所有人脸库的状态信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFaceSet</td>
                    <td>查询人脸库当前的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFaceSet</td>
                    <td>删除人脸库以及其中所有的人脸。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFaceSet</td>
                    <td>创建用于存储人脸特征的人脸库。您最多可以创建10个人脸库,每个人脸库最大容量为10万个人脸特征。如有更大规格的需求请联系客服。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">人脸搜索</td>
                    <td>SearchFaceByFaceId</td>
                    <td>人脸搜索是指在已有的人脸库中,查询与目标人脸相似的一张或者多张人脸,并返回相应的置信度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchFaceByBase64</td>
                    <td>人脸搜索是指在已有的人脸库中,查询与目标人脸相似的一张或者多张人脸,并返回相应的置信度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchFaceByUrl</td>
                    <td>人脸搜索是指在已有的人脸库中,查询与目标人脸相似的一张或者多张人脸,并返回相应的置信度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchFaceByFile</td>
                    <td>人脸搜索是指在已有的人脸库中,查询与目标人脸相似的一张或者多张人脸,并返回相应的置信度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">人脸检测</td>
                    <td>DetectFaceByFile</td>
                    <td>人脸检测是对输入图片进行人脸检测和分析,输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectFaceByUrl</td>
                    <td>人脸检测是对输入图片进行人脸检测和分析,输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectFaceByBase64</td>
                    <td>人脸检测是对输入图片进行人脸检测和分析,输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">人脸比对</td>
                    <td>CompareFaceByFile</td>
                    <td>人脸比对是将两个人脸进行比对,来判断是否为同一个人,返回比对置信度。如果传入的图片中包含多个人脸,选取最大的人脸进行比对。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CompareFaceByUrl</td>
                    <td>人脸比对是将两个人脸进行比对,来判断是否为同一个人,返回比对置信度。如果传入的图片中包含多个人脸,选取最大的人脸进行比对。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CompareFaceByBase64</td>
                    <td>人脸比对是将两个人脸进行比对,来判断是否为同一个人,返回比对置信度。如果传入的图片中包含多个人脸,选取最大的人脸进行比对。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">人脸资源管理</td>
                    <td>UpdateFace</td>
                    <td>根据人脸ID(face_id)更新单张人脸信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddFacesByBase64</td>
                    <td>添加人脸到人脸库中。将单张图片中的人脸添加至人脸库中,支持添加最大人脸或所有人脸。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddFacesByFile</td>
                    <td>添加人脸到人脸库中。将单张图片中的人脸添加至人脸库中,支持添加最大人脸或所有人脸。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFacesByLimit</td>
                    <td>查询指定人脸库中人脸信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFaceByFaceId</td>
                    <td>根据face_id删除人脸。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFaceByExternalImageId</td>
                    <td>根据external_image_id删除人脸。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFacesByFaceId</td>
                    <td>查询指定人脸库中人脸信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddFacesByUrl</td>
                    <td>添加人脸到人脸库中。将单张图片中的人脸添加至人脸库中,支持添加最大人脸或所有人脸。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteFaces</td>
                    <td>自定义筛选条件,批量删除人脸库中的符合指定条件的多张人脸。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">动作活体检测</td>
                    <td>DetectLiveByFile</td>
                    <td>动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现,则选取最大的人脸进行判定。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectLiveByUrl</td>
                    <td>动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现,则选取最大的人脸进行判定。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectLiveByBase64</td>
                    <td>动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现,则选取最大的人脸进行判定。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">静默活体检测</td>
                    <td>DetectLiveFaceByFile</td>
                    <td>静默活体检测是基于人脸图片中可能存在的畸变、摩尔纹、反光、倒影、边框等信息,判断图片中的人脸是否来自于真人活体,有效抵御纸质翻拍照、电子翻拍照以及视频翻拍等各种攻击方式。静默活体检测支持单张图片,不支持多人脸图片。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectLiveFaceByUrl</td>
                    <td>静默活体检测是基于人脸图片中可能存在的畸变、摩尔纹、反光、倒影、边框等信息,判断图片中的人脸是否来自于真人活体,有效抵御纸质翻拍照、电子翻拍照以及视频翻拍等各种攻击方式。静默活体检测支持单张图片,不支持多人脸图片。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectLiveFaceByBase64</td>
                    <td>静默活体检测是基于人脸图片中可能存在的畸变、摩尔纹、反光、倒影、边框等信息,判断图片中的人脸是否来自于真人活体,有效抵御纸质翻拍照、电子翻拍照以及视频翻拍等各种攻击方式。静默活体检测支持单张图片,不支持多人脸图片。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
