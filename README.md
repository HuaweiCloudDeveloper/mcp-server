# mcp-server
[![GitHub License](https://img.shields.io/github/license/manusa/kubernetes-mcp-server)](https://github.com/manusa/kubernetes-mcp-server/blob/main/LICENSE)
[![CI](https://github.com/HuaweiCloudDeveloper/mcp-server/actions/workflows/lint.yaml/badge.svg)](https://github.com/HuaweiCloudDeveloper/mcp-server/actions/workflows/lint.yaml) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/HuaweiCloudDeveloper/mcp-server/pulls)
[![Last Commit](https://img.shields.io/github/last-commit/HuaweiCloudDeveloper/mcp-server)](https://github.com/HuaweiCloudDeveloper/mcp-server/commits/main) 
[![Language](https://img.shields.io/github/languages/top/HuaweiCloudDeveloper/mcp-server)](https://github.com/HuaweiCloudDeveloper/mcp-server)

Huawei MCP Server is a Model Context Protocol server built on Huawei Cloud services, providing secure and controlled cloud access capabilities for large AI models. Through standardized MCP specifications, it enables AI assistants to operate Huawei Cloud resources within conversational workflows, supporting core services including ECS, OBS, GaussDB, and other widely-used cloud products.

## Demo

[Demo](https://github.com/user-attachments/assets/f0cdc18f-e3dc-401e-9ed5-5185e710b1a7)

The video demonstrates using Cline with Huawei MCP Server to create a new ECS instance and remove it.

## Prepare
Install [uv](https://github.com/astral-sh/uv)

```sh
# On macOS and Linux.
 curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Configuration
Use [VS Code](https://code.visualstudio.com/) + [Cline](https://cline.bot/) to config MCP Server.

To use huaweicloud-mcp-server MCP Server with any other MCP Client, you can manually add this configuration and restart for changes to take effect:

```json
{
  "mcpServers": {
    "huaweicloud-mcp-server": {
      "timeout": 600,
      "command": "uv",
      "args": [
            "--directory",
            "/path/to/yours/mcp-server/src",
            "run",
            "server.py"
      ],
      "env": {
        "HUAWEI_CLOUD_MCP_TRANSPORT": "stdio",
        "HUAWEI_CLOUD_AK": "Your Access Key AK",
        "HUAWEI_CLOUD_SK": "Your Access Key SK"
      }
    }
  }
}
```
## MCP Maketplace Integration

* [Cline](https://cline.bot/mcp-marketplace)

## Tools

| **Product** | **Tool** | **Function**                  | **Implematation** | **Status** |
| --- | --- |-------------------------------|-------------------| --- |
| ECS | create_post_paid_ecs_instance | Create post paid ecs instance | ECS               | Done |
| | delete_ecs_instance | Delete ecs instance         | ECS               | Done |
| | select_ecs_instance | Retrieve ecs instance | ECS               | Done |
| VPC | get_vpc_id | Get vpc id     | VPC               | Done |
| | list_all_subnets | list all subnets              | VPC               | Done |
| | get_subnet_id | Get subnet id              | VPC               | Done |
| OBS | bucket_exist | Checks if a specified bucket exists | OBS               | Done |
|  | get_buckets | Get buckets                | OBS               | Done |
|  | delete_bucket | Delete bucket                 | OBS               | Done |
|  | create_bucket | Create bucket                 | OBS               | Done |
|  | get_objects | Get objects in the bucket     | OBS               | Done |
|  | download_object | Download object               | OBS               | Done |
|  | delete_object | Delete object                 | OBS               | Done |
| OCR | recognize_general_text | Recognize general text in images                 | OCR               | Done |

## Roadmap

Please refer to the [roadmap](docs/roadmap.md).
