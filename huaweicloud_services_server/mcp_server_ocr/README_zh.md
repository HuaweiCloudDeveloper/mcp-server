# OCR MCP Server 

## 版本信息
v0.1.0

## 产品描述

OCR MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务OCR交互的能力。可以基于自然语言对OCR资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| VIN码识别 | RecognizeVin | 识别图片中的车架号信息,并将识别结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section14),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 不动产证识别 | RecognizeRealEstateCertificate | 识别不动产证中的文字信息,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section11),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 保险单识别 | RecognizeInsurancePolicy | 识别保险单图片上的文字信息,并将识别的结构化结果返回给用户。支持对多种版式保险单的扫描图片及手机照片进行结构化信息提取。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section23),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 出租车发票识别 | RecognizeTaxiInvoice | 识别出租车发票中的文字信息,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section18),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 印章识别 | RecognizeSeal | 检测和识别合同文件或常用票据中的印章,并可擦除和提取图片中的印章,通过JSON格式返回印章检测、识别、擦除和提取的结果。 | To be tested |
| 发票验真 | RecognizeInvoiceVerification | 发票验真服务支持10种增值税发票的信息核验,包括增值税专用发票、增值税普通发票、增值税普通发票(卷式)、增值税电子专用发票、增值税电子普通发票、增值税电子普通发票(通行费)、二手车销售统一发票、机动车销售统一发票、区块链电子发票、全电发票,支持返回票面的全部信息。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section16),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 名片识别 | RecognizeBusinessCard | 识别名片图片上的文字信息,并返回识别的结构化结果。支持对多种不同版式名片进行结构化信息提取。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section13),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 哥伦比亚身份证识别 | RecognizeColombiaIdCard | 识别哥伦比亚身份证中的文字信息,并将识别的结构化结果返回给用户。 | To be tested |
| 增值税发票识别 | RecognizeVatInvoice | 识别增值税发票的类别,以及图片中的文字内容,并以json格式返回识别的结构化结果,不支持真伪验证。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section15),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 定额发票识别 | RecognizeQuotaInvoice | 识别定额发票中的文字信息,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section21),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 户口本识别 | RecognizeHouseholdRegister | 识别户口本中的文字信息,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section11),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 手写文字识别 | RecognizeHandwriting | 识别文档中的手写文字信息,并将识别的结构化结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section4),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 承兑汇票识别 | RecognizeAcceptanceBill | 识别承兑汇票中的关键信息, 并以json格式返回结构化结果。 | To be tested |
| 护照识别 | RecognizePassport | 识别用户上传的护照首页图片中的文字信息,并返回识别的结构化结果。当前版本支持中国护照的全字段识别。外国护照支持护照下方两行国际标准化的机读码识别,并可从中提取6-7个关键字段信息。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section8),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 智能分类识别 | RecognizeAutoClassification | 检测定位图片上指定要识别的票证(票据、证件或其他文字载体),并对其进行结构化识别。接口以列表形式返回图片上要识别票证的位置坐标、结构化识别的内容以及对应的类别。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section3),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 智能文档解析 | RecognizeSmartDocumentRecognizer | 对证件、票据、表单等任意版式文档进行键值对提取、文字识别、以及表格识别等任务,实现进阶高效的自动化结构化返回。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section11),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 机动车销售发票识别 | RecognizeMvsInvoice | 识别机动车销售发票、二手车销售发票图片(服务能自动分辨两种类型,返回对应的字段)中的文字内容,并将识别的结果以JSON格式返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section17),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 泰国车牌识别 | RecognizeThailandLicensePlate | 识别泰国车牌图片中的车牌信息,并返回识别的结构化结果。 | To be tested |
| 泰文身份证识别 | RecognizeThailandIdcard | 识别泰国身份证中的文字信息,并返回识别的结构化结果。 | To be tested |
| 火车票识别 | RecognizeTrainTicket | 识别火车票中的文字信息,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section22),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 电子面单识别 | RecognizeWaybillElectronic | 识别用户上传的电子面单图片中的文字内容,并将识别的结果以json格式返回给用户。 | To be tested |
| 网络图片识别 | RecognizeWebImage | 识别网络图片中的文字内容,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section2),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 自定义模板OCR | RecognizeCustomTemplate | 自定义模板OCR,支持用户自定义模板,对于版式固定的各种票据和卡证,通过可视化界面操作,指定需要识别的关键字段,实现用户特定格式图片的自动识别和结构化提取。 | To be tested |
| 营业执照识别 | RecognizeBusinessLicense | 识别营业执照首页图片中的文字信息,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section10),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 行驶证识别 | RecognizeVehicleLicense | 识别用户上传的行驶证图片(或者用户提供的华为云上OBS的行驶证图片文件的URL)中主页和副页的文字内容,并将识别的结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section7),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 财务报表识别 | RecognizeFinancialStatement | 识别用户上传的表格图片中的文字内容,并将识别的结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section24),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 身份证识别 | RecognizeIdCard | 识别身份证图片中的文字内容,并将识别的结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section5),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 车牌识别 | RecognizeLicensePlate | 识别输入图片中的车牌信息,并返回其坐标和内容。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section12),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 车辆合格证识别 | RecognizeVehicleCertificate | 识别车辆合格证中的文字信息,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section11),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 车辆通行费发票识别 | RecognizeTollInvoice | 识别车辆通行费发票中的文字信息,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section19),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 通用文字识别 | RecognizeGeneralText | 识别图片上的文字信息,返回识别的文字和坐标。支持扫描文件、电子文档、书籍、票据和表单等多种场景的文字识别。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section1),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 通用表格识别 | RecognizeGeneralTable | 用于识别用户上传的通用表格图片(或者用户提供的华为云上OBS的通用表格图片文件的URL)中的文字内容,并将识别的结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section0),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 道路运输从业资格证识别 | RecognizeQualificationCertificate | 识别道路运输从业资格证上的关键文字信息,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section25),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 道路运输证识别 | RecognizeTransportationLicense | 识别道路运输证首页中的文字信息,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section11),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 银行卡识别 | RecognizeBankcard | 识别银行卡上的关键文字信息,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section9),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 银行回单识别 | RecognizeBankReceipt | 支持对银行回单版式进行文字识别及键值对提取,实现高效的自动化结构化返回。 | To be tested |
| 飞机行程单识别 | RecognizeFlightItinerary | 识别飞机行程单中的文字信息,并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section20),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
| 驾驶证识别 | RecognizeDriverLicense | 识别用户上传的驾驶证图片(或者用户提供的华为云上OBS的驾驶证图片文件的URL)中主页与副页的文字内容,并将识别的结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section6),详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。 | To be tested |
