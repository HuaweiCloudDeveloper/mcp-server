# FRS MCP Server 

## 版本信息
v0.1.0

## 产品描述

FRS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务FRS交互的能力。可以基于自然语言对FRS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 人脸库资源管理 | ShowAllFaceSets | 查询当前用户所有人脸库的状态信息。 | To be tested |
|  | ShowFaceSet | 查询人脸库当前的状态。 | To be tested |
|  | DeleteFaceSet | 删除人脸库以及其中所有的人脸。 | To be tested |
|  | CreateFaceSet | 创建用于存储人脸特征的人脸库。您最多可以创建10个人脸库,每个人脸库最大容量为10万个人脸特征。如有更大规格的需求请联系客服。 | To be tested |
| 人脸搜索 | SearchFaceByFaceId | 人脸搜索是指在已有的人脸库中,查询与目标人脸相似的一张或者多张人脸,并返回相应的置信度。 | To be tested |
|  | SearchFaceByBase64 | 人脸搜索是指在已有的人脸库中,查询与目标人脸相似的一张或者多张人脸,并返回相应的置信度。 | To be tested |
|  | SearchFaceByUrl | 人脸搜索是指在已有的人脸库中,查询与目标人脸相似的一张或者多张人脸,并返回相应的置信度。 | To be tested |
|  | SearchFaceByFile | 人脸搜索是指在已有的人脸库中,查询与目标人脸相似的一张或者多张人脸,并返回相应的置信度。 | To be tested |
| 人脸检测 | DetectFaceByFile | 人脸检测是对输入图片进行人脸检测和分析,输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。 | To be tested |
|  | DetectFaceByUrl | 人脸检测是对输入图片进行人脸检测和分析,输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。 | To be tested |
|  | DetectFaceByBase64 | 人脸检测是对输入图片进行人脸检测和分析,输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。 | To be tested |
| 人脸比对 | CompareFaceByFile | 人脸比对是将两个人脸进行比对,来判断是否为同一个人,返回比对置信度。如果传入的图片中包含多个人脸,选取最大的人脸进行比对。 | To be tested |
|  | CompareFaceByUrl | 人脸比对是将两个人脸进行比对,来判断是否为同一个人,返回比对置信度。如果传入的图片中包含多个人脸,选取最大的人脸进行比对。 | To be tested |
|  | CompareFaceByBase64 | 人脸比对是将两个人脸进行比对,来判断是否为同一个人,返回比对置信度。如果传入的图片中包含多个人脸,选取最大的人脸进行比对。 | To be tested |
| 人脸资源管理 | UpdateFace | 根据人脸ID(face_id)更新单张人脸信息。 | To be tested |
|  | AddFacesByBase64 | 添加人脸到人脸库中。将单张图片中的人脸添加至人脸库中,支持添加最大人脸或所有人脸。 | To be tested |
|  | AddFacesByFile | 添加人脸到人脸库中。将单张图片中的人脸添加至人脸库中,支持添加最大人脸或所有人脸。 | To be tested |
|  | ShowFacesByLimit | 查询指定人脸库中人脸信息。 | To be tested |
|  | DeleteFaceByFaceId | 根据face_id删除人脸。 | To be tested |
|  | DeleteFaceByExternalImageId | 根据external_image_id删除人脸。 | To be tested |
|  | ShowFacesByFaceId | 查询指定人脸库中人脸信息。 | To be tested |
|  | AddFacesByUrl | 添加人脸到人脸库中。将单张图片中的人脸添加至人脸库中,支持添加最大人脸或所有人脸。 | To be tested |
|  | BatchDeleteFaces | 自定义筛选条件,批量删除人脸库中的符合指定条件的多张人脸。 | To be tested |
| 动作活体检测 | DetectLiveByFile | 动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现,则选取最大的人脸进行判定。 | To be tested |
|  | DetectLiveByUrl | 动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现,则选取最大的人脸进行判定。 | To be tested |
|  | DetectLiveByBase64 | 动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现,则选取最大的人脸进行判定。 | To be tested |
| 静默活体检测 | DetectLiveFaceByFile | 静默活体检测是基于人脸图片中可能存在的畸变、摩尔纹、反光、倒影、边框等信息,判断图片中的人脸是否来自于真人活体,有效抵御纸质翻拍照、电子翻拍照以及视频翻拍等各种攻击方式。静默活体检测支持单张图片,不支持多人脸图片。 | To be tested |
|  | DetectLiveFaceByUrl | 静默活体检测是基于人脸图片中可能存在的畸变、摩尔纹、反光、倒影、边框等信息,判断图片中的人脸是否来自于真人活体,有效抵御纸质翻拍照、电子翻拍照以及视频翻拍等各种攻击方式。静默活体检测支持单张图片,不支持多人脸图片。 | To be tested |
|  | DetectLiveFaceByBase64 | 静默活体检测是基于人脸图片中可能存在的畸变、摩尔纹、反光、倒影、边框等信息,判断图片中的人脸是否来自于真人活体,有效抵御纸质翻拍照、电子翻拍照以及视频翻拍等各种攻击方式。静默活体检测支持单张图片,不支持多人脸图片。 | To be tested |
