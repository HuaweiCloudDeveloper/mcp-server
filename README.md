# mcp-server

[![GitHub License](https://img.shields.io/github/license/manusa/kubernetes-mcp-server)](https://github.com/manusa/kubernetes-mcp-server/blob/main/LICENSE)
[![CI](https://github.com/HuaweiCloudDeveloper/mcp-server/actions/workflows/ci.yaml/badge.svg)](https://github.com/HuaweiCloudDeveloper/mcp-server/actions/workflows/ci.yaml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/HuaweiCloudDeveloper/mcp-server/pulls)
[![Last Commit](https://img.shields.io/github/last-commit/HuaweiCloudDeveloper/mcp-server)](https://github.com/HuaweiCloudDeveloper/mcp-server/commits/main)
[![Language](https://img.shields.io/github/languages/top/HuaweiCloudDeveloper/mcp-server)](https://github.com/HuaweiCloudDeveloper/mcp-server)

[简体中文](./README_zh.md)

Huawei MCP Server is a Model Context Protocol server built on Huawei Cloud services, providing secure and controlled cloud access capabilities for large AI models. Through standardized MCP specifications, it enables AI assistants to operate Huawei Cloud resources within conversational workflows, supporting core services including ECS, OBS, GaussDB, and other widely-used cloud products.
## Mcp-server catalog
- [Practical documents](#Practical-documents)
- [Demo](#Demo)
- [Running Guide](#Running-Guide)
- [Tools list](#Tools)
- [Contributing](#Contributing)


## Practical documents
- [Using DAS MCP to implement database conversational operation and maintenance](https://support.huaweicloud.com/bestpractice-das/das_best_practice_01_0017.html) 


## Demo

[Demo1](https://github.com/user-attachments/assets/df2c2993-42ec-4f7e-8631-29c44c58fcbd)

Cline uses Huawei Cloud EIP MCP Server to create and delete EIP instances.

## Running Guide

### 1. Dependency Installation

Install the Python environment in advance. Since Python 3.4 and 2.7.9, pip has been installed with Python as a standard component.

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (Recommended)
- Install [python](https://www.python.org/downloads/) version `3.10` or above

### 2. Environment variable settings

Prepare AK and SK and set them to environment variables

- ak environment variable name: HUAWEI_ACCESS_KEY
- sk environment variable name: HUAWEI_SECRET_KEY

![img.png](images/img.png)

### 3. Running method

Take running the `mcp-server-ecs` service as an example

#### Run with 'uv' (recommended)

```shell
# Enter the root path of the project
cd /path/to/you/mcp-server

# Start the service
uv run mcp-server-ecs
```

Execute `uv run mcp-server-ecs -h` to view the usage instructions, the configuration values of the `config.yaml` file in the sub-project can be overwritten by using the optional parameters in the command line

```text
usage: mcp-server-ecs [-h] [-p PORT] [-t {http,sse,stdio}]

MCP Server

options:
  -h, --help            show this help message and exit
  -p, --port PORT       Port number
  -t, --transport {http,sse,stdio}
                        Transport of MCP Server
```

#### Run with `python`

![img_1.png](images/img_1.png)

```shell
# Enter the root path of the project
cd /path/to/you/mcp-server

# Install dependencies
pip install -e .

# Enter the specified service (mcp-server-ecs) path
cd huaweicloud_services_server/mcp_server_ecs/src/mcp_server_ecs

# Start the service
python run.py
```

## MCP Marketplace Integration

* [Cline](https://cline.bot/mcp-marketplace)
* Configure the mcp service to use http in cline. The json format is as follows
```json
{
  "mcpServers": {
    "mcp_server_ecs": {
      "url": "http://localhost:8888/mcp",
      "disabled": false,
      "type": "streamableHttp",
      "autoApprove": []
    }
  }
}
```

## Tools

<!DOCTYPE html>
<html>
<body>
<table border="1" cellspacing="0" cellpadding="5">
  <tr>
    <th>Group Name</th>
    <th>Product Name</th>
    <th>Product Short</th>
  </tr>
  <tr>
    <td rowspan="1">KooGallery</td>
    <td>Products and Orders</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_marketplace_server">Product&Order</a></td>
  </tr>
  <tr>
    <td rowspan="10">Networking</td>
    <td>Elastic Load Balance</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_elb">ELB</a></td>
  </tr>
  <tr>
    <td>Virtual Private Cloud</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_vpc">VPC</a></td>
  </tr>
  <tr>
    <td>Elastic IP</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_eip">EIP</a></td>
  </tr>
  <tr>
    <td>NAT Gateway</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_nat">NAT</a></td>
  </tr>
  <tr>
    <td>VPC Endpoint</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_vpcep">VPCEP</a></td>
  </tr>
  <tr>
    <td>Cloud Connect</td>
    <td>CC</td>
  </tr>
  <tr>
    <td>Enterprise Router</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_er">ER</a></td>
  </tr>
  <tr>
    <td>Global Accelerator</td>
    <td>GA</td>
  </tr>
  <tr>
    <td>Direct Connect</td>
    <td>DC</td>
  </tr>
  <tr>
    <td>Virtual Private Network</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_vpn">VPN</a></td>
  </tr>
  <tr>
    <td rowspan="3">Migration</td>
    <td>Server Migration Service</td>
    <td>SMS</td>
  </tr>
  <tr>
    <td>Object Storage Migration Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_oms">OMS</a></td>
  </tr>
  <tr>
    <td>CloudDataMigration</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_cdm">CDM</a></td>
  </tr>
  <tr>
    <td rowspan="5">Containers</td>
    <td>Cloud Container Engine</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_cce">CCE</a></td>
  </tr>
  <tr>
    <td>SoftWare Repository for Container</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_swr">SWR</a></td>
  </tr>
  <tr>
    <td>Application Service Mesh</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_asm">ASM</a></td>
  </tr>
  <tr>
    <td>Application Orchestration Service</td>
    <td>AOS</td>
  </tr>
  <tr>
    <td>Cloud Container Instance</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_cci">CCI</a></td>
  </tr>
  <tr>
    <td rowspan="10">AI</td>
    <td>Optical Character Recognition</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_ocr">OCR</a></td>
  </tr>
  <tr>
    <td>Face Recognition Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_frs">FRS</a></td>
  </tr>
  <tr>
    <td>ModelArts</td>
    <td>ModelArts</td>
  </tr>
  <tr>
    <td>Image</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_image">Image</a></td>
  </tr>
  <tr>
    <td>ImageSearch</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_imagesearch">ImageSearch</a></td>
  </tr>
  <tr>
    <td>Moderation</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_moderation">Moderation</a></td>
  </tr>
  <tr>
    <td>Speech Interaction Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_sis">SIS</a></td>
  </tr>
  <tr>
    <td>Graph Engine Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_ges">GES</a></td>
  </tr>
  <tr>
    <td>Question Answering Bot</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_cbs">CBS</a></td>
  </tr>
  <tr>
    <td>Autonomous Driving Cloud Service</td>
    <td>Octopus</td>
  </tr>
  <tr>
    <td rowspan="13">CodeArts</td>
    <td>Cloud Performance Test Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_cpts">CPTS</a></td>
  </tr>
  <tr>
    <td>ServiceStage</td>
    <td>ServiceStage</td>
  </tr>
  <tr>
    <td>CodeCheck</td>
    <td>CodeCheck</td>
  </tr>
  <tr>
    <td>CodeArts Req</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_projectman">ProjectMan</a></td>
  </tr>
  <tr>
    <td>CodeHub</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_codehub">CodeHub</a></td>
  </tr>
  <tr>
    <td>CloudBuild</td>
    <td>CloudBuild</td>
  </tr>
  <tr>
    <td>CloudTest</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_cloudtest">CloudTest</a></td>
  </tr>
  <tr>
    <td>CodeArts Deploy</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_codeartsdeploy">CodeArtsDeploy</a></td>
  </tr>
  <tr>
    <td>CodeArts Check</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_codeartscheck">CodeArtsCheck</a></td>
  </tr>
  <tr>
    <td>CodeArts Pipeline</td>
    <td>CodeArtsPipeline</td>
  </tr>
  <tr>
    <td>CodeArts Build</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_codeartsbuild">CodeArtsBuild</a></td>
  </tr>
  <tr>
    <td>CodeArts Artifact</td>
    <td>CodeArtsArtifact</td>
  </tr>
  <tr>
    <td>Cloud Application Engine</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_cae">CAE</a></td>
  </tr>
  <tr>
    <td rowspan="4">Business Applications</td>
    <td>ROMA</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_roma">ROMA</a></td>
  </tr>
  <tr>
    <td>Domain Name Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_dns">DNS</a></td>
  </tr>
  <tr>
    <td>HUAWEI CLOUD Meeting</td>
    <td>Meeting</td>
  </tr>
  <tr>
    <td>Workspace</td>
    <td>Workspace</td>
  </tr>
  <tr>
    <td rowspan="1">Operation</td>
    <td>Customer Operation Capabilities</td>
    <td>BSSINTL</td>
  </tr>
  <tr>
    <td rowspan="3">Internet of Things</td>
    <td>IoT Device Access</td>
    <td>IoTDA</td>
  </tr>
  <tr>
    <td>Global SIM Link</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_gsl">GSL</a></td>
  </tr>
  <tr>
    <td>IoT Device Access Management</td>
    <td>IoTDM</td>
  </tr>
  <tr>
    <td rowspan="7">Middleware</td>
    <td>Distributed Cache Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_dcs">DCS</a></td>
  </tr>
  <tr>
    <td>Distributed Message Service for Kafka</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_kafka">Kafka</a></td>
  </tr>
  <tr>
    <td>Cloud Service Engines</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_cse">CSE</a></td>
  </tr>
  <tr>
    <td>Distributed Message Service for RocketMQ</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_rocketmq">RocketMQ</a></td>
  </tr>
  <tr>
    <td>Distributed Message Service for RabbitMQ</td>
    <td>RabbitMQ</td>
  </tr>
  <tr>
    <td>API Gateway</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_apig">APIG</a></td>
  </tr>
  <tr>
    <td>Application Performance Management</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_apm">APM</a></td>
  </tr>
  <tr>
    <td rowspan="1">MacroVerse aPaaS</td>
    <td>AppStage</td>
    <td>AppStage</td>
  </tr>
  <tr>
    <td rowspan="6">Analytics</td>
    <td>MapReduce Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_mrs">MRS</a></td>
  </tr>
  <tr>
    <td>Data Warehouse Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_dws">DWS</a></td>
  </tr>
  <tr>
    <td>Data Lake Insight</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_dli">DLI</a></td>
  </tr>
  <tr>
    <td>DataArts Studio</td>
    <td>DataArtsStudio</td>
  </tr>
  <tr>
    <td>Cloud Search Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_css">CSS</a></td>
  </tr>
  <tr>
    <td>Date Ingestion Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_dis">DIS</a></td>
  </tr>
  <tr>
    <td rowspan="4">Media Services</td>
    <td>Media Processing Center</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_mpc">MPC</a></td>
  </tr>
  <tr>
    <td>Live</td>
    <td>Live</td>
  </tr>
  <tr>
    <td>Video On Demand</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_vod">VOD</a></td>
  </tr>
  <tr>
    <td>Huawei Cloud Real-Time Communication</td>
    <td>CloudRTC</td>
  </tr>
  <tr>
    <td rowspan="21">Management &amp; Governance</td>
    <td>Identity and Access Management</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_iam">IAM</a></td>
  </tr>
  <tr>
    <td>Cloud Eye</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_ces">CES</a></td>
  </tr>
  <tr>
    <td>Log Tank Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_lts">LTS</a></td>
  </tr>
  <tr>
    <td>Resource Management Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_rms">RMS</a></td>
  </tr>
  <tr>
    <td>Cloud Trace Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_cts">CTS</a></td>
  </tr>
  <tr>
    <td>Tag Management Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_tms">TMS</a></td>
  </tr>
  <tr>
    <td>Enterprise Project Management Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_eps">EPS</a></td>
  </tr>
  <tr>
    <td>Simple Message Notification</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_smn">SMN</a></td>
  </tr>
  <tr>
    <td>Application Operations Management</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_aom">AOM</a></td>
  </tr>
  <tr>
    <td>Organizations</td>
    <td>Organizations</td>
  </tr>
  <tr>
    <td>Resource Access Manager</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_ram">RAM</a></td>
  </tr>
  <tr>
    <td>Config</td>
    <td>Config</td>
  </tr>
  <tr>
    <td>Resource Formation Service</td>
    <td>RFS</td>
  </tr>
  <tr>
    <td>IAMAccessAnalyzer</td>
    <td>IAMAccessAnalyzer</td>
  </tr>
  <tr>
    <td>IAM Identity Center</td>
    <td>IdentityCenter</td>
  </tr>
  <tr>
    <td>IAM Identity Center Store</td>
    <td>IdentityCenterStore</td>
  </tr>
  <tr>
    <td>IAM Identity Center SCIM</td>
    <td>IdentityCenterSCIM</td>
  </tr>
  <tr>
    <td>IAM Identity Center OIDC</td>
    <td>IdentityCenterOIDC</td>
  </tr>
  <tr>
    <td>Security Token Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_sts">STS</a></td>
  </tr>
  <tr>
    <td>Cloud Operations Center</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_coc">COC</a></td>
  </tr>
  <tr>
    <td>Resource Governance Center</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_rgc">RGC</a></td>
  </tr>
  <tr>
    <td rowspan="1">Developer Tools</td>
    <td>APIExplorer</td>
    <td>APIExplorer</td>
  </tr>
  <tr>
    <td rowspan="4">Storage</td>
    <td>Elastic Volume Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_evs">EVS</a></td>
  </tr>
  <tr>
    <td>Cloud Backup and Recovery</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_cbr">CBR</a></td>
  </tr>
  <tr>
    <td>SFSTurbo</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_sfsturbo">SFSTurbo</a></td>
  </tr>
  <tr>
    <td>Object Storage Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_obs">OBS</a></td>
  </tr>
  <tr>
    <td rowspan="9">Databases</td>
    <td>Document Database Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_dds">DDS</a></td>
  </tr>
  <tr>
    <td>Relational Database Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_rds">RDS</a></td>
  </tr>
  <tr>
    <td>TaurusDB</td>
    <td>TaurusDB</td>
  </tr>
  <tr>
    <td>GaussDB</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_gaussdbforopengauss">GaussDBforopenGauss</a></td>
  </tr>
  <tr>
    <td>GeminiDB</td>
    <td>GeminiDB</td>
  </tr>
  <tr>
    <td>Data Replication Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_drs">DRS</a></td>
  </tr>
  <tr>
    <td>Database and Application Migration UGO</td>
    <td>UGO</td>
  </tr>
  <tr>
    <td>Distributed Database Middleware</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_ddm">DDM</a></td>
  </tr>
  <tr>
    <td>Data Admin Service (DAS)</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_das">DAS</a></td>
  </tr>
  <tr>
    <td rowspan="6">Compute</td>
    <td>Elastic Cloud Server</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_ecs">ECS</a></td>
  </tr>
  <tr>
    <td>Auto Scaling</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_as">AS</a></td>
  </tr>
  <tr>
    <td>FunctionGraph</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_functiongraph">FunctionGraph</a></td>
  </tr>
  <tr>
    <td>Image Management Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_ims">IMS</a></td>
  </tr>
  <tr>
    <td>Bare Metal Server</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_bms">BMS</a></td>
  </tr>
  <tr>
    <td>Dedicated Host</td>
    <td>DeH</td>
  </tr>
  <tr>
    <td rowspan="1">Content Delivery &amp; Edge Computing</td>
    <td>Content Delivery NetWork</td>
    <td>CDN</td>
  </tr>
  <tr>
    <td rowspan="15">Security &amp; Compliance</td>
    <td>Host Security Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_hss">HSS</a></td>
  </tr>
  <tr>
    <td>Data Encryption Workshop KPS</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_kps">KPS</a></td>
  </tr>
  <tr>
    <td>Cloud Secret Management Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_csms">CSMS</a></td>
  </tr>
  <tr>
    <td>Data Encryption Workshop KMS</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_kms">KMS</a></td>
  </tr>
  <tr>
    <td>Cloud Certificate Manager Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_ccm">CCM</a></td>
  </tr>
  <tr>
    <td>SSL Certificate Manager</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_scm">SCM</a></td>
  </tr>
  <tr>
    <td>Anti-DDoS</td>
    <td>Anti-DDoS</td>
  </tr>
  <tr>
    <td>Database Security Service</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_dbss">DBSS</a></td>
  </tr>
  <tr>
    <td>Web Application Firewall</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_waf">WAF</a></td>
  </tr>
  <tr>
    <td>Data Security Center</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_dsc">DSC</a></td>
  </tr>
  <tr>
    <td>Cloud Firewall</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_cfw">CFW</a></td>
  </tr>
  <tr>
    <td>Cloud Bastion Host</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_cbh">CBH</a></td>
  </tr>
  <tr>
    <td>Edge Security</td>
    <td>EdgeSec</td>
  </tr>
  <tr>
    <td>SecMaster</td>
    <td>SecMaster</td>
  </tr>
  <tr>
    <td>Advanced Anti-DDoS</td>
    <td><a href="https://github.com/HuaweiCloudDeveloper/mcp-server/tree/master-dev/huaweicloud_services_server/mcp_server_aad">AAD</a></td>
  </tr>
</table>
</body>
</html>


## Contributing

We welcome contributions from the open-source community! 
If you'd like to contribute to this project, please refer to the [contributing guide](CONTRIBUTING.md).