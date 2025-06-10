# mcp-server

[![GitHub License](https://img.shields.io/github/license/manusa/kubernetes-mcp-server)](https://github.com/manusa/kubernetes-mcp-server/blob/main/LICENSE)
[![CI](https://github.com/HuaweiCloudDeveloper/mcp-server/actions/workflows/lint.yaml/badge.svg)](https://github.com/HuaweiCloudDeveloper/mcp-server/actions/workflows/lint.yaml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/HuaweiCloudDeveloper/mcp-server/pulls)
[![Last Commit](https://img.shields.io/github/last-commit/HuaweiCloudDeveloper/mcp-server)](https://github.com/HuaweiCloudDeveloper/mcp-server/commits/main)
[![Language](https://img.shields.io/github/languages/top/HuaweiCloudDeveloper/mcp-server)](https://github.com/HuaweiCloudDeveloper/mcp-server)

[English](./README.md)

华为MCP Server是基于华为云服务构建的模型上下文协议服务器，为大型AI模型提供安全可控的云服务访问能力。通过标准化的MCP协议规范，使AI助手能在对话流中操作华为云资源，支持ECS、OBS、GaussDB等核心服务及广泛使用的云产品。

## Demo

[Demo](https://github.com/user-attachments/assets/f0cdc18f-e3dc-401e-9ed5-5185e710b1a7)

该Demo展示了使用Cline与华为MCP Server创建并删除ECS实例的全过程。

## 环境说明

安装[uv](https://github.com/astral-sh/uv)

```sh
# On macOS and Linux.
 curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 配置

使用[VS Code](https://code.visualstudio.com/) + [Cline](https://cline.bot/)配置MCP Server。

如需将huaweicloud-mcp-server与其他MCP客户端配合使用，可手动添加以下配置并重启生效：

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

## MCP市场集成

* [Cline](https://cline.bot/mcp-marketplace)

## 功能点(Tools)

| **产品** | **工具**                      | **功能**             | **实现方式** | **状态** |
| -------- | ----------------------------- | -------------------- | ------------ | -------- |
| ECS      | create_post_paid_ecs_instance | 创建按需ECS实例      | ECS          | 已完成   |
|          | delete_ecs_instance           | 删除ECS实例          | ECS          | 已完成   |
|          | select_ecs_instance           | 查询ECS实例详情      | ECS          | 已完成   |
| VPC      | get_vpc_id                    | 获取VPC ID           | VPC          | 已完成   |
|          | list_all_subnets              | 列出所有子网         | VPC          | 已完成   |
|          | get_subnet_id                 | 获取子网ID           | VPC          | 已完成   |
| OBS      | bucket_exist                  | 验证存储桶是否存在   | OBS          | 已完成   |
|          | get_buckets                   | 获取存储桶列表       | OBS          | 已完成   |
|          | delete_bucket                 | 删除存储桶           | OBS          | 已完成   |
|          | create_bucket                 | 创建存储桶           | OBS          | 已完成   |
|          | get_objects                   | 获取存储桶内对象列表 | OBS          | 已完成   |
|          | download_object               | 下载对象文件         | OBS          | 已完成   |
|          | delete_object                 | 删除指定对象         | OBS          | 已完成   |
| OCR      | recognize_general_text        | 通用文字识别         | OCR          | 已完成   |

## Roadmap

详细路线图请参见[roadmap](docs/roadmap.md)。

## 贡献指南

我们热忱欢迎开源社区的贡献
如果您想参与本项目开发，请查阅[开发文档](./docs/develope-mcp.md)。
