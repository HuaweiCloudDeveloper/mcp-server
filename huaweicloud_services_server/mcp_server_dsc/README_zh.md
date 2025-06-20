# DSC MCP Server 

## 版本信息
v0.1.0

## 产品描述

DSC MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DSC交互的能力。可以基于自然语言对DSC资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| API调用记录 | ShowOpenApiCalledRecords | 查询OpenApi调用记录 | To be tested |
| 告警通知 | UpdateDefaultTopic | 修改告警通知的关联项目ID、通知主题、通知状态(0为关闭通知,1为开启通知)等通用配置 | To be tested |
|  | ShowTopics | 查询告警通知主题,返回默认主题、已确认主题数量及列表 | To be tested |
| 图片水印 | CreateImageWatermark | 对图片嵌入文字暗水印或者图片暗水印,用户以formData的格式传入待加水印图片和水印相关信息,DSC服务对图片加完水印后返回给用户已嵌入水印的图片二进制流,目前支持的图片格式为:*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。 | To be tested |
|  | ShowImageWatermarkWithImage | 对已嵌入图片暗水印的图片进行水印提取,用户以formData的格式传入待提取水印的图片,DSC服务以图片二进制流的格式返回从图片里提取的出的图片暗水印。目前支持的图片格式为:*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。 | To be tested |
|  | ShowImageWatermarkByAddress | 对指定存储地址信息(目前支持华为云OBS)的已嵌入文字暗水印的图片提取文字暗水印,支持的图片格式为:*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。 | To be tested |
|  | ShowImageWatermarkWithImageByAddress | 对指定存储地址信息(目前支持华为云OBS)的已嵌入图片暗水印的图片提取图片暗水印,提取出的水印图片将存放在用户指定的位置(目前支持华为云OBS),支持的图片格式为:*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。 | To be tested |
|  | CreateImageWatermarkByAddress | 对指定存储地址信息(目前支持华为云OBS)的图片嵌入文字暗水印或者图片暗水印,已嵌入的水印的图片将存放在用户指定的位置(目前支持华为云OBS),支持的图片格式为:*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。 | To be tested |
|  | ShowImageWatermark | 对已嵌入文字暗水印的图片进行水印提取,用户以formData的格式传入待提取水印的图片,DSC服务以JSON的格式返回从图片里提取的出的文字暗水印。目前支持的图片格式为:*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。 | To be tested |
| 敏感数据发现 | AddRuleGroup | 根据指定的规则组名称和扫描规则列表创建敏感数据扫描规则组 | To be tested |
|  | DeleteScanJob | 删除扫描任务 | To be tested |
|  | DeleteRuleGroup | 根据扫描规则组ID删除指定的扫描规则组 | To be tested |
|  | ChangeRule | 修改自定义的敏感数据识别规则 | To be tested |
|  | ShowRules | 查询扫描规则列表,返回扫描规则总数和扫描规则列表 | To be tested |
|  | ShowScanJobResults | 查询指定任务扫描结果 | To be tested |
|  | ShowScanJobs | 查询扫描任务列表 | To be tested |
|  | DeleteRule | 删除指定的敏感数据识别规则 | To be tested |
|  | ListRuleGroups | 根据指定的项目ID查询扫描规则组列表 | To be tested |
|  | AddScanJob | 根据指定的任务名称、扫描方式、扫描周期、扫描规则组、扫描时间创建扫描任务 | To be tested |
|  | AddRule | 根据指定的规则名称、规则类型、风险等级、最小匹配次数等参数创建自定义的敏感数据识别规则 | To be tested |
| 数据动态脱敏 | BatchAddDataMask | 对数据进行脱敏 | To be tested |
| 数据水印 | CreateDatabaseWaterMark | 对json体中数据动态添加水印 | To be tested |
|  | ShowDatabaseWaterMark | 提取请求数据中水印内容 | To be tested |
| 数据静态脱敏 | ChangeDbTemplateOperation | 开启/停止脱敏任务 | To be tested |
|  | ListDbMaskTask | 查询脱敏任务执行列表 | To be tested |
| 文档水印 | CreateDocWatermark | 对WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf) 类型的文件嵌入文字暗水印、文字明水印或者图片明水印,用户以formData的格式传入待加水印的文件和水印相关信息,DSC服务给文件加完水印后返回给用户已嵌入水印的文件的二进制流。 | To be tested |
|  | ShowDocWatermark | 对已嵌入文字暗水印的WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf)类型的文档进行文字暗水印提取,用户以formData的格式传入待提取水印的文件,DSC服务以JSON的格式返回从文档里提取的出的文字暗水印内容。 | To be tested |
|  | ShowDocWatermarkByAddress | 支持对已嵌入文字暗水印的WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf)类型的文档进行水印提取,用户传入待提取水印的文档地址(目前支持OBS),DSC服务以JSON的格式返回从文档里提取的出的文字暗水印内容。 | To be tested |
|  | CreateDocWatermarkByAddress | 对WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf)*类型的文档嵌入文字暗水印、文字明水印或者图片明水印,用户传入待加水印的文档地址(目前支持OBS)和水印相关信息,DSC服务对文档加完水印后返回给用户已嵌入水印的文档的存放地址。 | To be tested |
| 资产管理 | AddBuckets | 添加数据资产扫描授权 | To be tested |
|  | ListBuckets | 查询数据资产扫描授权列表 | To be tested |
|  | DeleteBucket | 删除数据资产扫描授权 | To be tested |
|  | UpdateAssetName | 编辑数据资产名称 | To be tested |
| 资源管理 | ShowSpecification | 查询资源开通信息,根据项目ID查询订单详情 | To be tested |
|  | CreateProductOrder | 根据计费方式、计费周期等信息进行实例下单 | To be tested |
