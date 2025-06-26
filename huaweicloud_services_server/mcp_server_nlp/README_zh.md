# NLP MCP Server 


## Version
v0.1.0

## Overview

NLP MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service NLP. Full-chain management of NLP resources can be carried out based on natural language.

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
                    <td rowspan="4">机器翻译服务</td>
                    <td>RunFileTranslation</td>
                    <td>文档翻译接口,用于翻译文档格式文件。由于文档翻译会需要较长的时间,因此识别是异步的,也即接口分为创建翻译任务和查询任务状态两个接口。创建翻译任务接口创建任务完成后返回,然后用户通过调用查询任务状态接口来获得翻译状态和临时URL。 用户可以使用临时URL下载翻译好的文件,每个临时URL有效期为10分种。翻译结果会保存24小时(从翻译完成的时间算起)。24小时后如果再访问,将会返回 \"task id is not found\"错误。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunGetFileTranslationResult</td>
                    <td>该接口用于获取文档翻译识别状态以及临时url,临时url可以用与获取翻译后的文档,每个临时url有效期为十分钟。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTextTranslation</td>
                    <td>对于用户输入原始语种的文本,转换为目标语种的文本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunLanguageDetection</td>
                    <td>对于用户输入的文本,返回识别出的所属语种。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">自然语言处理基础服务</td>
                    <td>RunKeywordExtract</td>
                    <td>给定一段文本,抽取其中最能够反映文本主题或者意思的词汇。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTextSimilarity</td>
                    <td>文本相似度服务,对文本对进行相似度计算。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTextSimilarityAdvance</td>
                    <td>文本相似度服务高级版,对文本对进行相似度计算。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunNer</td>
                    <td>基础版命名实体识别,对文本进行命名实体识别分析,目前支持人名、地名、时间、组织机构类实体的识别。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunNerDomain</td>
                    <td>领域版本命名实体识别,对文本进行命名实体识别分析,目前支持人名、地名、组织机构、时间点、日期、百分比、货币额度、序数词、计量规格词、民族、职业、邮箱12类实体的识别。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunSegment</td>
                    <td>对文本进行分词和词性标注处理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunEntityLinking</td>
                    <td>针对通用领域的文本进行实体链接分析,识别出其中的实体,并返回实体相关信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunDependencyParser</td>
                    <td>识别句子中词汇与词汇之间的相互依存关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunEventExtraction</td>
                    <td>事件抽取是指从自然语言文本中抽取指定类型的事件以及相关实体信息,并形成结构化数据输出的文本处理技术。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunConstituencyParser</td>
                    <td>识别句子中的成分以及成分之间的层次包含关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunMultiGrainedSegment</td>
                    <td>多粒度分词:给定一个句子输入,输出不同粒度的所有单词的层次结构。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunSentenceEmbedding</td>
                    <td>输入句子,返回对应的句向量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">语言理解服务</td>
                    <td>RunAspectSentiment</td>
                    <td>属性级情感分析,针对手机领域的用户评论进行属性级情感分析。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunSentiment</td>
                    <td>通用情感分析,针对通用领域的用户评论进行情感分析。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunEntitySentiment</td>
                    <td>实体级情感分析,本产品适用于金融方面公司实体正负面新闻的分析。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunDocClassification</td>
                    <td>文档分类接口,输入文档内容,输出文档的标签和置信度,支持多个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunSemanticParser</td>
                    <td>针对天气、报时、新闻、笑话、翻译、提醒、闹钟、音乐8个领域进行意图理解,对用户的问题进行领域识别并提取领域内的参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunDomainSentiment</td>
                    <td>领域情感分析,针对未知领域,电商,汽车领域的用户评论进行情感分析。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunAspectSentimentAdvance</td>
                    <td>属性级情感分析(高级版),针对手机、汽车领域的用户评论进行属性级情感分析。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunClassification</td>
                    <td>针对广告领域的自动分类,判断是否是广告。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">语言生成服务</td>
                    <td>RunSummary</td>
                    <td>对文本生成摘要。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunPoem</td>
                    <td>根据用户的输入生成诗歌。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunSummaryDomain</td>
                    <td>对文本生成摘要。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
