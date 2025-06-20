# mcp-server

[![GitHub License](https://img.shields.io/github/license/manusa/kubernetes-mcp-server)](https://github.com/manusa/kubernetes-mcp-server/blob/main/LICENSE)
[![CI](https://github.com/HuaweiCloudDeveloper/mcp-server/actions/workflows/lint.yaml/badge.svg)](https://github.com/HuaweiCloudDeveloper/mcp-server/actions/workflows/ci.yaml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/HuaweiCloudDeveloper/mcp-server/pulls)
[![Last Commit](https://img.shields.io/github/last-commit/HuaweiCloudDeveloper/mcp-server)](https://github.com/HuaweiCloudDeveloper/mcp-server/commits/main)
[![Language](https://img.shields.io/github/languages/top/HuaweiCloudDeveloper/mcp-server)](https://github.com/HuaweiCloudDeveloper/mcp-server)

[English](./README.md)

华为MCP Server是基于华为云服务构建的模型上下文协议服务器，为大型AI模型提供安全可控的云服务访问能力。通过标准化的MCP协议规范，使AI助手能在对话流中操作华为云资源，支持ECS、OBS、GaussDB等核心服务及广泛使用的云产品。

## Demo

[Demo](https://github.com/user-attachments/assets/f0cdc18f-e3dc-401e-9ed5-5185e710b1a7)

该Demo展示了使用Cline与华为MCP Server创建并删除ECS实例的全过程。

## 运行指南

### 1. 依赖安装

提前安装python环境，自Python 3.4和2.7.9版本起，pip已经作为标准组件与Python一同安装。

`pip install -r assets/requirements.txt`

### 2. 环境变量设置

准备AK、SK并设置到环境变量

- ak 环境变量名:  HUAWEI_ACCESS_KEY
- sk 环境变量名:  HUAWEI_SECRET_KEY
- ![img.png](images/img.png)

### 3. 运行方法


![img_1.png](images/img_1.png)

直接进入子项目的目录路径，比如 mcp_server_ecs 下的run.py文件，cd进入run.py在所在目录，执行命令：`python run.py`，或者使用pycharm工具右键直接Run run.py

## MCP市场集成

* [Cline](https://cline.bot/mcp-marketplace)
* 在cline 中配置 mcp 服务使用sse的方式，json格式如下
```json
{
  "mcpServers": {
    "mcp_server_ecs": {
      "url": "http://localhost:8888/sse",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```



## 功能点(Tools)

| Group Name | Product Name | Product Short |
|------------|------------|------------|
| 计算 | 弹性云服务器 | [ECS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_ecs) |
| | GPU加速云服务器 | GACS |
| | FPGA加速云服务器 | FACS |
| | 裸金属服务器 | [BMS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_bms) |
| | 专属主机 | DeH |
| | 弹性伸缩 | [AS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_as) |
| | 镜像服务 | [IMS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_ims) |
| | 函数工作流 | [FunctionGraph](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_functiongraph) |
| | VR云渲游平台 | CVR |
| | 云手机 | [CPH](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cph) |
| | 容量管理服务 | [CMS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cms) |
| 存储 | 对象存储服务 | [OBS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_obs) |
| | 云硬盘 | [EVS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_evs) |
| | 云硬盘备份 | VBS |
| | 云服务器备份 | CSBS |
| | 存储容灾服务 | [SDRS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_sdrs) |
| | 弹性文件服务(SFS Turbo) | [SFSTurbo](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_sfsturbo) |
| | 数据快递服务 | DES |
| | 直播加速 | LSA |
| | 云备份 | [CBR](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cbr) |
| | 专属分布式存储服务 | [DSS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_dss) |
| | 专属企业存储服务 | DESS |
| | 数据工坊 | DWR |
| | 地图数据服务 | MapDS |
| | 键值存储服务 | [KVS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_kvs) |
| | 知识湖存储 | LMS |
| 网络 | 虚拟私有云 | [VPC](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_vpc) |
| | 弹性负载均衡 | [ELB](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_elb) |
| | NAT网关 | [NAT](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_nat) |
| | 弹性公网IP | [EIP](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_eip) |
| | 云专线 | DC |
| | 虚拟专用网络 | [VPN](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_vpn) |
| | VPC终端节点  | [VPCEP](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_vpcep) |
| | 云连接 | CC |
| | 企业路由器 | [ER](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_er) |
| | 全球加速 | GA |
| | 企业连接 | EC |
| | 全域弹性公网IP | [GEIP](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_geip) |
| 数据库 | 云数据库 | [RDS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_rds) |
| | 文档数据库服务 | [DDS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_dds) |
| | 分布式数据库中间件 | [DDM](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_ddm) |
| | 数据复制服务 | [DRS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_drs) |
| | 数据管理服务 | [DAS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_das) |
| | 多模NoSQL服务 | NoSQL |
| | 云数据库产品总览 | DBS |
| | 云数据库 TaurusDB | TaurusDB |
| | 云数据库TaurusDB | GaussDB |
| | 云数据库 GeminiDB | GaussDBforNoSQL |
| | GeminiDB Cassandra 接口 | GaussDBforCassandra |
| | GeminiDB Mongo 接口 | GaussDBforMongo |
| | GeminiDB Redis接口 | GaussDBforRedis |
| | GeminiDB Influx 接口 | GaussDBforInflux |
| | 云数据库 GaussDB | [GaussDBforopenGauss](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_gaussdbforopengauss) |
| | 数据库和应用迁移 UGO | UGO |
| 人工智能 | 机器学习服务 | MLS |
| | 自然语言处理 | [NLP](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_nlp) |
| | 语言理解 | nlplu |
| | 语言生成 | nlplg |
| | 定制自然语言处理 | nlpc |
| | 机器翻译 | nlpmt |
| | 知识图谱 | nlpkg |
| | 对话机器人服务 | [CBS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cbs) |
| | 智能问答机器人 | QABot |
| | 智能话务机器人 | PhoneBot |
| | 智能对话质检 | cbssa |
| | 智能语音助手 | cbsc |
| | 人脸识别服务 | [FRS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_frs) |
| | 内容审核 | [Moderation](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_moderation) |
| | 内容审核-文本 | textmoderation |
| | 内容审核-图像 | imagemoderation |
| | 商超视频分析 | Smart Retail |
| | 园区视频分析 | Smart Campus |
| | 交通视频分析 | Smart Traffic |
| | 文字识别 | [OCR](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_ocr) |
| | 文字识别-通用类 | generalocr |
| | 文字识别-证件类 | cardocr |
| | 文字识别-票据类 | receiptocr |
| | 文字识别-行业类 | domainocr |
| | 文字识别-定制模板 | customocr |
| | 图像识别 | [Image](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_image) |
| | 名人识别 | ROC |
| | 图像标签 | imagetagging |
| | 深度学习服务 | DLS |
| | 图引擎服务 | [GES](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_ges) |
| | 图像搜索 | [ImageSearch](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_imagesearch) |
| | 推荐系统 | [RES](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_res) |
| | 智能水务 | iWater |
| | 智能制造 | iManufacturing |
| | 智能交通 | iTransport |
| | 智能电力 | iPower |
| | 智能金融 | iFinance |
| | 智能零售 | iRetail |
| | 机器翻译服务 | MTS |
| | AI开发平台 | ModelArts |
| | Huawei HiLens | HiLens |
| | 视频指纹 | VFP |
| | 视频编辑 | VCP |
| | 视频标签 | VCT |
| | 机器翻译 | MT |
| | 定制语音识别 | ASRC |
| | 知识图谱 | KG |
| | 视频分析服务 | [VAS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_vas) |
| | 语音交互服务 | [SIS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_sis) |
| | 录音文件识别 | LASR |
| | 语音合成 | TTS |
| | 实时语音识别 | RASR |
| | 一句话识别 | ASR |
| | 网络智能体 | NAIE |
| | 人证核身服务 | [IVS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_ivs) |
| | 园区智能体 | CampusGo |
| | 视频内容审核 | [VCM](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_vcm) |
| | 医疗智能体 | eiHealth |
| | 运筹优化算法服务 | [OROAS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_oroas) |
| | 盘古大模型 | PanguLargeModels |
| | 天筹求解器服务 | OptVerse |
| | 盘古大模型-应用开发 | AppKit |
| | 八爪鱼自动驾驶云服务 | Octopus |
| | 视频智能分析服务 | [VIAS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_vias) |
| | 大模型开发平台 | MaStudio |
| | 数智融合计算服务 | DataArtsFabric |
| 大数据 | 数据接入服务 | [DIS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_dis) |
| | 数据仓库服务 | [DWS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_dws) |
| | 云搜索服务 | [CSS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_css) |
| | 数据湖工厂 | [DLF](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_dlf) |
| | 实时流计算服务 | CS |
| | MapReduce服务 | [MRS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_mrs) |
| | 数据湖探索 | [DLI](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_dli) |
| | 批处理服务 | Batch |
| | 数据湖治理中心 | [DGC](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_dgc) |
| | 表格存储服务 | CloudTable |
| | 数据治理中心 | DataArtsStudio |
| | 湖仓构建 | LakeFormation |
| | 可信智能计算服务 | [TICS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_tics) |
| | 智能数据洞察 | DataArtsInsight |
| 容器 | 云容器引擎 | [CCE](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cce) |
| | 云容器实例 | [CCI](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cci) |
| | 容器镜像服务 | [SWR](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_swr) |
| | 应用编排服务 | AOS |
| | 应用服务网格 | [ASM](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_asm) |
| 安全与合规 | Web应用防火墙 | [WAF](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_waf) |
| | DDoS高防 | [AAD](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_aad) |
| | Anti-DDoS流量清洗 | Anti-DDoS |
| | 企业主机安全 | [HSS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_hss) |
| | 数据加密服务-密钥管理 | [KMS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_kms) |
| | 数据加密服务-凭据管理 | [CSMS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_csms) |
| | 数据加密服务-密钥对管理 | [KPS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_kps) |
| | 数据库安全服务 | [DBSS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_dbss) |
| | 安全专家服务 | SES |
| | 态势感知 | [SA](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_sa) |
| | SSL证书管理 | [SCM](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_scm) |
| | 云堡垒机 | [CBH](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cbh) |
| | 容器安全服务 | CGS |
| | 数据安全中心 | [DSC](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_dsc) |
| | 云证书管理服务 | [CCM](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_ccm) |
| | 云防火墙 | [CFW](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cfw) |
| | 安全云脑 | SecMaster |
| 运营 | 运营能力开放 | BSS |
| 应用中间件 | 微服务引擎 | [CSE](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cse) |
| | API网关 | [APIG](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_apig) |
| | 分布式消息服务 Kafka | [Kafka](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_kafka) |
| | 分布式消息服务 RocketMQ | [RocketMQ](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_rocketmq) |
| | 分布式消息服务 RabbitMQ | RabbitMQ |
| | 分布式缓存服务 | [DCS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_dcs) |
| | 分布式缓存服务Redis | DCSforRedis |
| | 分布式缓存服务Memcached | DCSforMemcached |
| | 事件网格 | [EG](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_eg) |
| | 多活高可用服务 | [MAS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_mas) |
| 管理与监管 | 云监控服务 | [CES](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_ces) |
| | 云日志服务 | [LTS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_lts) |
| | 统一身份认证服务 | [IAM](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_iam) |
| | 云审计服务 | [CTS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cts) |
| | 标签管理服务 | [TMS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_tms) |
| | 资源模板服务 | RTS |
| | 企业项目管理服务 | [EPS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_eps) |
| | 资源管理服务 | [RMS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_rms) |
| | 消息通知服务 | [SMN](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_smn) |
| | 应用性能管理 | [APM](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_apm) |
| | 应用运维管理 | [AOM](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_aom) |
| | 组织 | Organizations |
| | 资源访问管理 | [RAM](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_ram) |
| | 配置审计 | Config |
| | IAM 身份中心 | IdentityCenter |
| | 优化顾问 | OA |
| | 资源治理中心 | [RGC](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_rgc) |
| | 访问分析 | IAMAccessAnalyzer |
| | IAM 身份中心身份源 | IdentityCenterStore |
| | IAM 身份中心 SCIM | IdentityCenterSCIM |
| | IAM 身份中心 OIDC | IdentityCenterOIDC |
| | 安全令牌服务 | [STS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_sts) |
| | 云运维中心 | [COC](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_coc) |
| | 消息通知服务Global | [SMNGLOBAL](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_smnglobal) |
| | IAM 身份中心 PortalAPI | IdentityCenterPortalAPI |
| CDN与智能边缘 | 内容分发网络 | CDN |
| | 智能边缘平台 | [IEF](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_ief) |
| | 智能边缘小站 | CloudPond |
| | 智能边缘云 | [IEC](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_iec) |
| | 智能边缘小站 | [IES](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_ies) |
| 软件开发生产线 | 需求管理 | [ProjectMan](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_projectman) |
| | 代码托管 | [CodeHub](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_codehub) |
| | 流水线 | [CloudPipeline](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cloudpipeline) |
| | 代码检查 | CodeCheck |
| | 移动应用测试 | MobileAppTest |
| | 测试计划 | [CloudTest](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cloudtest) |
| | 意见反馈 | VOC |
| | CloudIDE | CloudIDE |
| | 大赛服务 | CodeCraft |
| | 研发安全服务 | DevSecurity |
| | 应用管理与运维平台 | ServiceStage |
| | 云性能测试服务 | [CPTS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cpts) |
| | 云应用引擎 | [CAE](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cae) |
| | 制品仓库 | CodeArtsArtifact |
| | 编译构建 | [CodeArtsBuild](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_codeartsbuild) |
| | 代码检查 | [CodeArtsCheck](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_codeartscheck) |
| | 部署 | [CodeArtsDeploy](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_codeartsdeploy) |
| | 漏洞管理服务 | [CodeArtsInspector](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_codeartsinspector) |
| | 流水线 | CodeArtsPipeline |
| 企业应用 | 云解析服务 | [DNS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_dns) |
| | 华为云WeLink | WeLink |
| | 华为云会议 | Meeting |
| | 语音通话 | VoiceCall |
| | 消息&短信 | [MSGSMS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_msgsms) |
| | 隐私保护通话 | PrivateNumber |
| | 联络中心 | ContactCenter |
| | 全栈专属服务 | FCS |
| | 云管理网络 | CMN |
| | 应用与数据集成平台 | [ROMA](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_roma) |
| | 云桌面 | Workspace |
| | 云应用 | WorkspaceApp |
| | 消息&短信(业务API) | SMSApi |
| 迁移 | 云迁移中心 | CMC |
| | 对象存储迁移服务 | [OMS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_oms) |
| | 云数据迁移 | [CDM](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_cdm) |
| | 数据复制服务 | [DRS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_drs) |
| | 主机迁移服务 | SMS |
| 区块链 | 区块链服务 | [BCS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_bcs) |
| 视频 | 媒体转码 | [MPC](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_mpc) |
| | 视频点播 | [VOD](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_vod) |
| | 视频直播 | Live |
| | 融合视频云服务 | CVCS |
| | 云VR | CloudVR |
| | 媒体智能 | Media AI |
| | 华为好望云服务 | IVM |
| | 华为云实时音视频 | CloudRTC |
| | 视频接入服务 | [VIS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_vis) |
| | 数字内容生产线 | MetaStudio |
| IoT物联网 | 智能边缘平台 | [IEF](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_ief) |
| | OceanBooster | OceanBooster |
| | 设备发放 | IoTDP |
| | 车路协同平台 | ocv2x |
| | OceanConnect 车联网 | OCIOV |
| | 设备接入 | IoTDA |
| | 物联网应用构建器 | OCStudio |
| | 物联网数据分析 | IoTAnalytics |
| |  路网数字化服务 | [DRIS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_dris) |
| | IoT边缘 | IoTEdge |
| | 全球SIM联接 | [GSL](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_gsl) |
| | 设备接入管理 | IoTDM |
| 专属云 | 专属计算集群服务 | DCC |
| | 裸金属服务器 | [BMS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_bms) |
| 企业网络 | 视频加速服务 | VGVAS |
| 开天aPaaS | 云消息服务 | KooMessage |
| | 云地图服务 | KooMap |
| | 交换数据空间 | [EDS](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_eds) |
| | 开天集成工作台 | [MSSI](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_mssi) |
| | 云手机服务 | KooPhone |
| | 组织成员账号 | OrgID |
| | 应用平台 | AppStage |
| 工业软件 | 工业数字主线云服务 | [IDT](https://gitee.com/HuaweiCloudDeveloper/hwc-mcp-server/tree/master/huaweicloud_services_server/mcp_server_idt) |
| | 工业数字模型驱动引擎 | iDME |
| | 工业数字模型驱动引擎(典型API体验) | iDMEClassicAPI |
| | 硬件开发工具链平台云服务 | CraftArtsIPDCenter |
| 开发者工具 | DevStar | DevStar |
| | 开源平台 | OpenSource |
| | 华为云CLI | HCloud CLI |
| | APIExplorer | APIExplorer |
| | FlowCube | FlowCube |
| 支持与服务 | 工单管理 | OSM |




## 贡献指南

我们热忱欢迎开源社区的贡献
如果您想参与本项目开发，请查阅[开发文档](./docs/develope-mcp.md)。
