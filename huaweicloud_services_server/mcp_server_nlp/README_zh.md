# NLP MCP Server 

## 版本信息
v0.1.0

## 产品描述

NLP MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务NLP交互的能力。可以基于自然语言对NLP资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 机器翻译服务 | RunFileTranslation | 文档翻译接口,用于翻译文档格式文件。由于文档翻译会需要较长的时间,因此识别是异步的,也即接口分为创建翻译任务和查询任务状态两个接口。创建翻译任务接口创建任务完成后返回,然后用户通过调用查询任务状态接口来获得翻译状态和临时URL。 用户可以使用临时URL下载翻译好的文件,每个临时URL有效期为10分种。翻译结果会保存24小时(从翻译完成的时间算起)。24小时后如果再访问,将会返回 \"task id is not found\"错误。 | To be tested |
|  | RunGetFileTranslationResult | 该接口用于获取文档翻译识别状态以及临时url,临时url可以用与获取翻译后的文档,每个临时url有效期为十分钟。 | To be tested |
|  | RunTextTranslation | 对于用户输入原始语种的文本,转换为目标语种的文本。 | To be tested |
|  | RunLanguageDetection | 对于用户输入的文本,返回识别出的所属语种。 | To be tested |
| 自然语言处理基础服务 | RunKeywordExtract | 给定一段文本,抽取其中最能够反映文本主题或者意思的词汇。 | To be tested |
|  | RunTextSimilarity | 文本相似度服务,对文本对进行相似度计算。 | To be tested |
|  | RunTextSimilarityAdvance | 文本相似度服务高级版,对文本对进行相似度计算。 | To be tested |
|  | RunNer | 基础版命名实体识别,对文本进行命名实体识别分析,目前支持人名、地名、时间、组织机构类实体的识别。 | To be tested |
|  | RunNerDomain | 领域版本命名实体识别,对文本进行命名实体识别分析,目前支持人名、地名、组织机构、时间点、日期、百分比、货币额度、序数词、计量规格词、民族、职业、邮箱12类实体的识别。 | To be tested |
|  | RunSegment | 对文本进行分词和词性标注处理。 | To be tested |
|  | RunEntityLinking | 针对通用领域的文本进行实体链接分析,识别出其中的实体,并返回实体相关信息。 | To be tested |
|  | RunDependencyParser | 识别句子中词汇与词汇之间的相互依存关系。 | To be tested |
|  | RunEventExtraction | 事件抽取是指从自然语言文本中抽取指定类型的事件以及相关实体信息,并形成结构化数据输出的文本处理技术。 | To be tested |
|  | RunConstituencyParser | 识别句子中的成分以及成分之间的层次包含关系。 | To be tested |
|  | RunMultiGrainedSegment | 多粒度分词:给定一个句子输入,输出不同粒度的所有单词的层次结构。 | To be tested |
|  | RunSentenceEmbedding | 输入句子,返回对应的句向量。 | To be tested |
| 语言理解服务 | RunAspectSentiment | 属性级情感分析,针对手机领域的用户评论进行属性级情感分析。 | To be tested |
|  | RunSentiment | 通用情感分析,针对通用领域的用户评论进行情感分析。 | To be tested |
|  | RunEntitySentiment | 实体级情感分析,本产品适用于金融方面公司实体正负面新闻的分析。 | To be tested |
|  | RunDocClassification | 文档分类接口,输入文档内容,输出文档的标签和置信度,支持多个标签。 | To be tested |
|  | RunSemanticParser | 针对天气、报时、新闻、笑话、翻译、提醒、闹钟、音乐8个领域进行意图理解,对用户的问题进行领域识别并提取领域内的参数。 | To be tested |
|  | RunDomainSentiment | 领域情感分析,针对未知领域,电商,汽车领域的用户评论进行情感分析。 | To be tested |
|  | RunAspectSentimentAdvance | 属性级情感分析(高级版),针对手机、汽车领域的用户评论进行属性级情感分析。 | To be tested |
|  | RunClassification | 针对广告领域的自动分类,判断是否是广告。 | To be tested |
| 语言生成服务 | RunSummary | 对文本生成摘要。 | To be tested |
|  | RunPoem | 根据用户的输入生成诗歌。 | To be tested |
|  | RunSummaryDomain | 对文本生成摘要。 | To be tested |
