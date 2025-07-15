# Time MCP Server

## 版本信息

v0.1.0

## 产品描述

Time MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)
提供时间和时区转换功能。

## 可用工具

更多工具将陆续开放，已开放列表以及状态如下：

| 类别     | 工具名称             | 功能描述                 | 状态           |
|--------|------------------|----------------------|--------------|
| Common | get_current_time | 获取指定时区（默认为系统时区）的当前时间 | To be tested |
| Common | convert_time     | 在时区之间转换时间            | To be tested |

## 安装

### 使用uv（推荐）

```shell
uv --directory <MCP-SERVER-TIME-ABSOLUTE_PATH> run mcp-server-time [-H HOST] [-p PORT]

# 例如
uv --directory /app/mcp-server/common_servers/mcp_server_time run mcp-server-time -H 0.0.0.0 -p 8999
```

### 使用 pip (Python >= 3.10)

```shell
# 进入项目路径
cd <MCP-SERVER-TIME-ABSOLUTE_PATH>

# 创建虚拟环境（推荐）
python -m venv .venv
source .venv/bin/activate

pip install .

# 启动服务
mcp-server-time -H 0.0.0.0 -p 8999
```
