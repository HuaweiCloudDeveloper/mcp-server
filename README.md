# mcp-server

[![GitHub License](https://img.shields.io/github/license/manusa/kubernetes-mcp-server)](https://github.com/manusa/kubernetes-mcp-server/blob/main/LICENSE)
[![CI](https://github.com/HuaweiCloudDeveloper/mcp-server/actions/workflows/lint.yaml/badge.svg)](https://github.com/HuaweiCloudDeveloper/mcp-server/actions/workflows/ci.yaml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/HuaweiCloudDeveloper/mcp-server/pulls)
[![Last Commit](https://img.shields.io/github/last-commit/HuaweiCloudDeveloper/mcp-server)](https://github.com/HuaweiCloudDeveloper/mcp-server/commits/main)
[![Language](https://img.shields.io/github/languages/top/HuaweiCloudDeveloper/mcp-server)](https://github.com/HuaweiCloudDeveloper/mcp-server)

[简体中文](./README_zh.md)

Huawei MCP Server is a Model Context Protocol server built on Huawei Cloud services, providing secure and controlled cloud access capabilities for large AI models. Through standardized MCP specifications, it enables AI assistants to operate Huawei Cloud resources within conversational workflows, supporting core services including ECS, OBS, GaussDB, and other widely-used cloud products.

## Demo

[Demo](https://github.com/user-attachments/assets/f0cdc18f-e3dc-401e-9ed5-5185e710b1a7)

The video demonstrates using Cline with Huawei MCP Server to create a new ECS instance and remove it.

## Running Guide

### 1. Dependency Installation

Install the Python environment in advance. Since Python 3.4 and 2.7.9, pip has been installed with Python as a standard component.

`pip install -r assets/requirements.txt`

### 2. Environment variable settings

Prepare AK and SK and set them to environment variables

- ak environment variable name: HUAWEI_ACCESS_KEY

- sk environment variable name: HUAWEI_SECRET_KEY
- ![img.png](images/img.png)

### 3. Running method

![img_1.png](images/img_1.png)

Directly enter the directory path of the sub-project, such as the run.py file under mcp_server_ecs, cd to the directory where run.py is located, and execute the command: `python run.py`, or use the pycharm tool to right-click and directly run run.py

## MCP Maketplace Integration

* [Cline](https://cline.bot/mcp-marketplace)
* Configure the mcp service to use sse in cline. The json format is as follows
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
## Tools

| Group Name | Product Name | Product Short |
|----|-------|------------|
| Cloud Store | Products and Orders | [Product&Order](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_marketplace_server)|
| Operation | Customer Operation Capabilities | BSSINTL |
| Middleware | Distributed Cache Service | [DCS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_dcs) |
| | Distributed Message Service for Kafka | [Kafka](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_kafka) |
| | Cloud Service Engines | [CSE](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_cse) |
| | Distributed Message Service for RocketMQ | [RocketMQ](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_rocketmq) |
| | Distributed Message Service for RabbitMQ | RabbitMQ |
| | API Gateway | [APIG](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_apig) |
| | Application Performance Management | [APM](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_apm) |
| CodeArts | Cloud Performance Test Service | [CPTS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_cpts) |
| | ServiceStage | ServiceStage |
| | CodeCheck | CodeCheck |
| | CodeArts Req | [ProjectMan](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_projectman) |
| | CodeHub | [CodeHub](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_codehub) |
| | CloudBuild | CloudBuild |
| | CloudTest | [CloudTest](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_cloudtest) |
| | CodeArts Deploy | [CodeArtsDeploy](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_codeartsdeploy) |
| | CodeArts Check | [CodeArtsCheck](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_codeartscheck) |
| | CodeArts Pipeline | CodeArtsPipeline |
| | CodeArts Build | [CodeArtsBuild](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_codeartsbuild) |
| | CodeArts Artifact | CodeArtsArtifact |
| | Cloud Application Engine | [CAE](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_cae) |
| Networking | Elastic Load Balance | [ELB](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_elb) |
| | Virtual Private Cloud | [VPC](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_vpc) |
| | Elastic IP | [EIP](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_eip) |
| | NAT Gateway | [NAT](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_nat) |
| | VPC Endpoint | [VPCEP](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_vpcep) |
| | Cloud Connect | CC |
| | Enterprise Router | [ER](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_er) |
| | Global Accelerator | GA |
| | Direct Connect | DC |
| | Virtual Private Network | [VPN](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_vpn) |
| Content Delivery & Edge Computing | Content Delivery NetWork | CDN |
| Compute | Elastic Cloud Server | [ECS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_ecs) |
| | Auto Scaling | [AS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_as) |
| | FunctionGraph | [FunctionGraph](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_functiongraph) |
| | Image Management Service | [IMS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_ims) |
| | Bare Metal Server | [BMS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_bms) |
| | Dedicated Host | DeH |
| Security & Compliance | Host Security Service | [HSS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_hss) |
| | Data Encryption Workshop KPS | [KPS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_kps) |
| | Cloud Secret Management Service | [CSMS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_csms) |
| | Data Encryption Workshop KMS | [KMS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_kms) |
| | Cloud Certificate Manager Service | [CCM](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_ccm) |
| | SSL Certificate Manager | [SCM](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_scm) |
| | Anti-DDoS | Anti-DDoS |
| | Database Security Service | [DBSS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_dbss) |
| | Web Application Firewall | [WAF](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_waf) |
| | Data Security Center | [DSC](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_dsc) |
| | Cloud Firewall | [CFW](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_cfw) |
| | Cloud Bastion Host | [CBH](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_cbh) |
| | Edge Security | EdgeSec |
| | SecMaster | SecMaster |
| | Advanced Anti-DDoS | [AAD](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_aad) |
| Databases | Document Database Service | [DDS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_dds) |
| | Relational Database Service | [RDS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_rds) |
| | TaurusDB | GaussDB |
| | GaussDB | [GaussDBforopenGauss](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_gaussdbforopengauss) |
| | GeminiDB | GaussDBforNoSQL |
| | Data Replication Service | [DRS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_drs) |
| | Database and Application Migration UGO | UGO |
| | Distributed Database Middleware | [DDM](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_ddm) |
| | Data Admin Service (DAS) | [DAS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_das) |
| AI | Optical Character Recognition | [OCR](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_ocr) |
| | Face Recognition Service | [FRS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_frs) |
| | ModelArts | ModelArts |
| | Image | [Image](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_image) |
| | ImageSearch | [ImageSearch](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_imagesearch) |
| | Moderation | [Moderation](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_moderation) |
| | Speech Interaction Service | [SIS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_sis) |
| | Graph Engine Service | [GES](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_ges) |
| | Question Answering Bot | [CBS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_cbs) |
| | Autonomous Driving Cloud Service | Octopus |
| Analytics | MapReduce Service | [MRS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_mrs) |
| | Data Warehouse Service | [DWS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_dws) |
| | Data Lake Insight | [DLI](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_dli) |
| | DataArts Studio | DataArtsStudio |
| | Cloud Search Service | [CSS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_css) |
| | Date Ingestion Service | [DIS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_dis) |
| Containers | Cloud Container Engine | [CCE](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_cce) |
| | SoftWare Repository for Container | [SWR](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_swr) |
| | Application Service Mesh | [ASM](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_asm) |
| | Application Orchestration Service | AOS |
| | Cloud Container Instance | [CCI](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_cci) |
| Migration | Server Migration Service | SMS |
| | Object Storage Migration Service | [OMS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_oms) |
| | CloudDataMigration | [CDM](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_cdm) |
| Management & Governance | Identity and Access Management | [IAM](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_iam) |
| | Cloud Eye | [CES](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_ces) |
| | Log Tank Service | [LTS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_lts) |
| | Resource Management Service | [RMS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_rms) |
| | Cloud Trace Service | [CTS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_cts) |
| | Tag Management Service | [TMS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_tms) |
| | Enterprise Project Management Service | [EPS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_eps) |
| | Simple Message Notification | [SMN](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_smn) |
| | Application Operations Management | [AOM](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_aom) |
| | Organizations | Organizations |
| | Resource Access Manager | [RAM](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_ram) |
| | Config | Config |
| | Resource Formation Service | RFS |
| | IAMAccessAnalyzer | IAMAccessAnalyzer |
| | IAM Identity Center | IdentityCenter |
| | IAM Identity Center Store | IdentityCenterStore |
| | IAM Identity Center SCIM | IdentityCenterSCIM |
| | IAM Identity Center OIDC | IdentityCenterOIDC |
| | Security Token Service | [STS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_sts) |
| | Cloud Operations Center | [COC](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_coc) |
| | Resource Governance Center | [RGC](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_rgc) |
| Business Applications | ROMA | [ROMA](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_roma) |
| | Domain Name Service | [DNS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_dns) |
| | HUAWEI CLOUD Meeting | Meeting |
| | Workspace | Workspace |
| Storage | Elastic Volume Service | [EVS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_evs) |
| | Cloud Backup and Recovery | [CBR](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_cbr) |
| | SFSTurbo | [SFSTurbo](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_sfsturbo) |
| | Object Storage Service | [OBS](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_obs) |
| Developer Tools | APIExplorer | APIExplorer |
| Media Services | Media Processing Center | [MPC](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_mpc) |
| | Live | Live |
| | Video On Demand | [VOD](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_vod) |
| | Huawei Cloud Real-Time Communication | CloudRTC |
| Internet of Things | IoT Device Access | IoTDA |
| | Global SIM Link | [GSL](https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master/huaweicloud_services_server/mcp_server_gsl) |
| | IoT Device Access Management | IoTDM |
| MacroVerse aPaaS | AppStage | AppStage |



## Contribution

We welcome contributions from the open-source community! 
If you'd like to contribute to this project, please refer to the [DEVELOPEMENT](./docs/develope-mcp-EN.md) file.