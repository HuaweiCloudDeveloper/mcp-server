# NLP MCP Server 


## Version
v0.1.0

## Overview

NLP MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service NLP. Full-chain management of NLP resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| Language Generation Service | RunSummary | Generates a summary of the text. | To be tested |
|  | RunPoem | Generate a poem based on the user's input. | To be tested |
|  | RunSummaryDomain | Generates a summary of the text. | To be tested |
| Language Understanding Service | RunAspectSentiment | Attribute-level sentiment analysis, which is performed on user comments in the mobile phone domain. | To be tested |
|  | RunSentiment | General sentiment analysis, which is used to analyze user comments in the general domain. | To be tested |
|  | RunEntitySentiment | Entity-level sentiment analysis, which is applicable to the analysis of positive and negative news about financial entities. | To be tested |
|  | RunDocClassification | The document classification interface is used to enter the document content and output the document label and confidence. Multiple labels are supported. | To be tested |
|  | RunSemanticParser | Intention understanding is performed in eight fields: weather, time, news, joke, translation, reminder, alarm clock, and music. Identifies user questions and extracts parameters in the fields. | To be tested |
|  | RunDomainSentiment | Domain sentiment analysis, which is used to analyze user comments in unknown domains, e-commerce, and automobile fields. | To be tested |
|  | RunAspectSentimentAdvance | Attribute-level sentiment analysis (advanced edition), which is used to perform attribute-level sentiment analysis on user comments in the mobile phone and automobile fields. | To be tested |
|  | RunClassification | Automatic classification of the ad domain, which determines whether the ad is an ad. | To be tested |
| Machine Translation Service | RunFileTranslation | Document translation interface, which is used to translate document format files. Document translation takes a long time. Therefore, the identification is asynchronous. That is, the interfaces are divided into two interfaces: creating a translation task and querying the task status. Interface for creating a translation task. After the task is created, the system returns. Then, the user invokes the interface for querying the task status to obtain the translation status and temporary URL. Users can download translated files by using temporary URLs. Each temporary URL is valid for 10 minutes. The translation results will be stored for 24 hours (counted from the time the translation is completed). If you access it again after 24 hours, the \"task id is not found\" error will be returned. | To be tested |
|  | RunGetFileTranslationResult | This interface is used to obtain the document translation identification status and temporary URLs. Temporary URLs can be used to obtain translated documents. Each temporary URL is valid for 10 minutes. | To be tested |
|  | RunTextTranslation | Convert the text in the original language to the text in the target language. | To be tested |
|  | RunLanguageDetection | For the text entered by the user, the recognized language is returned. | To be tested |
| Natural Language Processing Basic Service | RunKeywordExtract | Extract the words that best reflect the theme or meaning of a given text. | To be tested |
|  | RunTextSimilarity | Text similarity service, which calculates the similarity of text pairs. | To be tested |
|  | RunTextSimilarityAdvance | Text Similarity Service Advanced Edition, which calculates the similarity between text pairs. | To be tested |
|  | RunNer | In the basic version, named entities can be identified and analyzed based on the text. Currently, the system supports the identification of entities such as person names, place names, time, and organizations. | To be tested |
|  | RunNerDomain | Domain version named entity recognition, which identifies and analyzes named entities of the text. Currently, the following types of entities can be identified: person name, place name, organization, time point, date, percentage, currency limit, ordinal number, measurement specification, nationality, occupation, and email address. | To be tested |
|  | RunSegment | Performs word segmentation and part-of-speech annotations on text. | To be tested |
|  | RunEntityLinking | Analyzes the entity links of the text in the common domain, identifies the entities in the text, and returns the entity information. | To be tested |
|  | RunDependencyParser | Identifies the interdependence between words in a sentence. | To be tested |
|  | RunEventExtraction | Event extraction is a text processing technology that extracts specified types of events and related entity information from natural language texts and generates structured data for output. | To be tested |
|  | RunConstituencyParser | Identifies the components in a sentence and the hierarchical inclusion relationship between the components. | To be tested |
|  | RunMultiGrainedSegment | Multi-granularity word segmentation: The hierarchy of all words at different granularity is outputted given a sentence input. | To be tested |
|  | RunSentenceEmbedding | Enter a sentence and return the corresponding sentence vector. | To be tested |

