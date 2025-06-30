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
                    <td rowspan="1">API调用记录</td>
                    <td>ShowOpenApiCalledRecords</td>
                    <td>查询OpenApi调用记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">告警通知</td>
                    <td>UpdateDefaultTopic</td>
                    <td>修改告警通知的关联项目ID、通知主题、通知状态(0为关闭通知,1为开启通知)等通用配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTopics</td>
                    <td>查询告警通知主题,返回默认主题、已确认主题数量及列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">图片水印</td>
                    <td>CreateImageWatermark</td>
                    <td>对图片嵌入文字暗水印或者图片暗水印,用户以formData的格式传入待加水印图片和水印相关信息,DSC服务对图片加完水印后返回给用户已嵌入水印的图片二进制流,目前支持的图片格式为:*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageWatermarkWithImage</td>
                    <td>对已嵌入图片暗水印的图片进行水印提取,用户以formData的格式传入待提取水印的图片,DSC服务以图片二进制流的格式返回从图片里提取的出的图片暗水印。目前支持的图片格式为:*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageWatermarkByAddress</td>
                    <td>对指定存储地址信息(目前支持华为云OBS)的已嵌入文字暗水印的图片提取文字暗水印,支持的图片格式为:*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageWatermarkWithImageByAddress</td>
                    <td>对指定存储地址信息(目前支持华为云OBS)的已嵌入图片暗水印的图片提取图片暗水印,提取出的水印图片将存放在用户指定的位置(目前支持华为云OBS),支持的图片格式为:*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateImageWatermarkByAddress</td>
                    <td>对指定存储地址信息(目前支持华为云OBS)的图片嵌入文字暗水印或者图片暗水印,已嵌入的水印的图片将存放在用户指定的位置(目前支持华为云OBS),支持的图片格式为:*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageWatermark</td>
                    <td>对已嵌入文字暗水印的图片进行水印提取,用户以formData的格式传入待提取水印的图片,DSC服务以JSON的格式返回从图片里提取的出的文字暗水印。目前支持的图片格式为:*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">敏感数据发现</td>
                    <td>AddRuleGroup</td>
                    <td>根据指定的规则组名称和扫描规则列表创建敏感数据扫描规则组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScanJob</td>
                    <td>删除扫描任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRuleGroup</td>
                    <td>根据扫描规则组ID删除指定的扫描规则组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeRule</td>
                    <td>修改自定义的敏感数据识别规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRules</td>
                    <td>查询扫描规则列表,返回扫描规则总数和扫描规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScanJobResults</td>
                    <td>查询指定任务扫描结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScanJobs</td>
                    <td>查询扫描任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRuleGroups</td>
                    <td>根据指定的项目ID查询扫描规则组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddScanJob</td>
                    <td>根据指定的任务名称、扫描方式、扫描周期、扫描规则组、扫描时间创建扫描任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddRule</td>
                    <td>根据指定的规则名称、规则类型、风险等级、最小匹配次数等参数创建自定义的敏感数据识别规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">数据动态脱敏</td>
                    <td>BatchAddDataMask</td>
                    <td>对数据进行脱敏</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">数据水印</td>
                    <td>CreateDatabaseWaterMark</td>
                    <td>对json体中数据动态添加水印</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatabaseWaterMark</td>
                    <td>提取请求数据中水印内容</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">数据静态脱敏</td>
                    <td>ChangeDbTemplateOperation</td>
                    <td>开启/停止脱敏任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbMaskTask</td>
                    <td>查询脱敏任务执行列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">文档水印</td>
                    <td>CreateDocWatermark</td>
                    <td>对WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf) 类型的文件嵌入文字暗水印、文字明水印或者图片明水印,用户以formData的格式传入待加水印的文件和水印相关信息,DSC服务给文件加完水印后返回给用户已嵌入水印的文件的二进制流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDocWatermark</td>
                    <td>对已嵌入文字暗水印的WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf)类型的文档进行文字暗水印提取,用户以formData的格式传入待提取水印的文件,DSC服务以JSON的格式返回从文档里提取的出的文字暗水印内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDocWatermarkByAddress</td>
                    <td>支持对已嵌入文字暗水印的WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf)类型的文档进行水印提取,用户传入待提取水印的文档地址(目前支持OBS),DSC服务以JSON的格式返回从文档里提取的出的文字暗水印内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDocWatermarkByAddress</td>
                    <td>对WORD(.docx),PPT(.pptx),EXCEL(.xlsx),PDF(.pdf)*类型的文档嵌入文字暗水印、文字明水印或者图片明水印,用户传入待加水印的文档地址(目前支持OBS)和水印相关信息,DSC服务对文档加完水印后返回给用户已嵌入水印的文档的存放地址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">桶的基础操作</td>
                    <td>ListBuckets</td>
                    <td>OBS用户可以通过请求查询自己创建的桶列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBucket</td>
                    <td>删除桶操作用于删除用户指定的桶。只有桶的所有者或者拥有桶的删桶policy权限的用户可以执行删除桶的操作,要删除的桶必须是空桶。如果桶中有对象或者有多段任务则认为桶不为空,可以使用列举桶内对象和列举出多段上传任务接口来确认桶是否为空。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">规则引擎</td>
                    <td>DeleteRule</td>
                    <td>删除规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">资产管理</td>
                    <td>AddBuckets</td>
                    <td>添加数据资产扫描授权</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAssetName</td>
                    <td>编辑数据资产名称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">资源管理</td>
                    <td>ShowSpecification</td>
                    <td>查询资源开通信息,根据项目ID查询订单详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProductOrder</td>
                    <td>根据计费方式、计费周期等信息进行实例下单</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
