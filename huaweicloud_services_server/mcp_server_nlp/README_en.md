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
                    <td rowspan="3">Language Generation Service</td>
                    <td>RunSummary</td>
                    <td>Generates a summary of the text.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunPoem</td>
                    <td>Generate a poem based on the user's input.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunSummaryDomain</td>
                    <td>Generates a summary of the text.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Language Understanding Service</td>
                    <td>RunAspectSentiment</td>
                    <td>Attribute-level sentiment analysis, which is performed on user comments in the mobile phone domain.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunSentiment</td>
                    <td>General sentiment analysis, which is used to analyze user comments in the general domain.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunEntitySentiment</td>
                    <td>Entity-level sentiment analysis, which is applicable to the analysis of positive and negative news about financial entities.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunDocClassification</td>
                    <td>The document classification interface is used to enter the document content and output the document label and confidence. Multiple labels are supported.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunSemanticParser</td>
                    <td>Intention understanding is performed in eight fields: weather, time, news, joke, translation, reminder, alarm clock, and music. Identifies user questions and extracts parameters in the fields.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunDomainSentiment</td>
                    <td>Domain sentiment analysis, which is used to analyze user comments in unknown domains, e-commerce, and automobile fields.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunAspectSentimentAdvance</td>
                    <td>Attribute-level sentiment analysis (advanced edition), which is used to perform attribute-level sentiment analysis on user comments in the mobile phone and automobile fields.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunClassification</td>
                    <td>Automatic classification of the ad domain, which determines whether the ad is an ad.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Machine Translation Service</td>
                    <td>RunFileTranslation</td>
                    <td>Document translation interface, which is used to translate document format files. Document translation takes a long time. Therefore, the identification is asynchronous. That is, the interfaces are divided into two interfaces: creating a translation task and querying the task status. Interface for creating a translation task. After the task is created, the system returns. Then, the user invokes the interface for querying the task status to obtain the translation status and temporary URL. Users can download translated files by using temporary URLs. Each temporary URL is valid for 10 minutes. The translation results will be stored for 24 hours (counted from the time the translation is completed). If you access it again after 24 hours, the \"task id is not found\" error will be returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunGetFileTranslationResult</td>
                    <td>This interface is used to obtain the document translation identification status and temporary URLs. Temporary URLs can be used to obtain translated documents. Each temporary URL is valid for 10 minutes.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTextTranslation</td>
                    <td>Convert the text in the original language to the text in the target language.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunLanguageDetection</td>
                    <td>For the text entered by the user, the recognized language is returned.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">Natural Language Processing Basic Service</td>
                    <td>RunKeywordExtract</td>
                    <td>Extract the words that best reflect the theme or meaning of a given text.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTextSimilarity</td>
                    <td>Text similarity service, which calculates the similarity of text pairs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTextSimilarityAdvance</td>
                    <td>Text Similarity Service Advanced Edition, which calculates the similarity between text pairs.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunNer</td>
                    <td>In the basic version, named entities can be identified and analyzed based on the text. Currently, the system supports the identification of entities such as person names, place names, time, and organizations.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunNerDomain</td>
                    <td>Domain version named entity recognition, which identifies and analyzes named entities of the text. Currently, the following types of entities can be identified: person name, place name, organization, time point, date, percentage, currency limit, ordinal number, measurement specification, nationality, occupation, and email address.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunSegment</td>
                    <td>Performs word segmentation and part-of-speech annotations on text.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunEntityLinking</td>
                    <td>Analyzes the entity links of the text in the common domain, identifies the entities in the text, and returns the entity information.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunDependencyParser</td>
                    <td>Identifies the interdependence between words in a sentence.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunEventExtraction</td>
                    <td>Event extraction is a text processing technology that extracts specified types of events and related entity information from natural language texts and generates structured data for output.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunConstituencyParser</td>
                    <td>Identifies the components in a sentence and the hierarchical inclusion relationship between the components.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunMultiGrainedSegment</td>
                    <td>Multi-granularity word segmentation: The hierarchy of all words at different granularity is outputted given a sentence input.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunSentenceEmbedding</td>
                    <td>Enter a sentence and return the corresponding sentence vector.</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
