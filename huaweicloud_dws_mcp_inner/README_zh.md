[English](README.md) | 中文

# DWS MCP Server

## 目录
  - [1. 简介](#1-前言)
  - [2. 功能介绍](#2-功能介绍)
    - [2.1 工具](#21-工具)
    - [2.2 资源](#22-资源)
  - [3. 配置](#3-Agent搭建及server配置)
    - [3.1 环境准备](#31-环境准备)
    - [3.2 下载源码](#32-下载Server源码)
    - [3.3 集群配置](#33-dws集群配置)
    - [3.4 客户端配置](#34-客户端配置)
  - [4. 开始体验](#4-开始体验)

## 1. 前言
MCP（Model Context Protocol）是由Anthropic于2024年11月提出的开放协议标准，旨在解决大型语言模型与外部系统（如数据库、API）交互的碎片化问题。通过标准化接口，让LLM动态理解工具功能并执行操作，降低集成成本。
通过搭建 DWS MCP Server，用户可以借助大模型的能力，以自然语言直接操作数据库，实现自然语言到 SQL 的自动转换，从而完成一键式后端查询，并在客户端直接查看结果。

## 2. 功能介绍
DWS MCP Server目前支持包括元数据查询、语句执行、监控信息查询等基本功能。支持功能以MCP协议中的工具（Tools）以及资源（Resource）形式向支持MCP协议的客户端暴露。

### 2.1 工具
DWS MCP Server 提供以下数据库管理工具：
1. **list_databases**  
   列出所有数据库

2. **get_activity**  
   从 `pgxc_stat_activity`视图获取最近的查询活动

3. **execute_query**  
   执行 SQL 查询

4. **list_schemas**  
   列出当前数据库中的所有模式  

5. **list_tables**  
   列出指定模式下的所有表

6. **list_views**  
   列出指定模式下的所有视图

7. **get_table_info**  
   获取表/视图的定义

8. **get_comment**  
   获取模式/表的注释

### 2.2 资源
DWS MCP Server 通过 MCP 暴露以下资源：

1. **gaussdb:////{schema}/tables**  
  列出指定模式下的所有表

2. **gaussdb:///{schema}/views**  
  列出指定模式下的所有视图

3. **gaussdb:///{schema}/{table}/attributes**  
  列出指定表/视图所有的列

4. **system:///{system_path}**  
  系统信息（例如 /version）

## 3. Agent搭建及server配置
以下使用Cline作为客户端演示如何配置使用DWS MCP Server。可根据需求选择其他支持MCP的客户端，如Claude Desktop等

### 3.1 环境准备
+ 确保dws集群版本支持psycopg2库
+ 确保使用环境python版本为3.10及以上
+ 确保安装uv版本0.6.7及以上
+ 安装VS Code客户端并安装Cline插件

### 3.2 下载Server源码
+ 从github下载 DWS MCP Server 源码
```
git clone https://github.com/HuaweiCloudDeveloper/mcp-server.git
```
> 说明：以上github链接包含众多华为云提供的MCP server，DWS MCP Server位于目录huaweicloud_dws_mcp_inner下

### 3.3 dws集群配置
+ 编辑集群安装目录下CN节点的```pg_hba.conf```配置文件，添加以下配置信息将客户端所在环境添加为host
```
host    <允许访问的库>        <允许的用户名>        <客户端ip/掩码>        <加密算法>
```
> 说明：PostgreSQL 默认使用 MD5 加密，而 DWS 默认使用 SHA256。由于加密协议的不同，可能会导致连接失败问题。
> 
> 解决方法：修改GUC参数password_encryption_type的值为1，在```pg_hba.conf```中将上述新增的host加密算法更改为md5，修改后需重启数据库并重新设置用户密码，以使新密码采用 MD5 算法存储。

+ 编辑postgresql.conf文件，将客户端所在环境的ip地址增加至```listen_addresses```
```
listen_addresses = 'localhost,<client_ip>'
```

### 3.4 客户端配置
+ 进入Cline设置界面，根据自身使用情况在API Configuration页面下填入API Provider、API Key等信息

![cline API 配置界面](images/cline_api.png)

+ 点击Cline页面右上角MCP图标进入MCP配置界面并点击Installed页签，在下方点击Configure MCP Servers,并填入以下DWS MCP Server配置
```
{
  "mcpServers": {
    "dws": {
      "disabled": false,
      "timeout": 60,
      "type": "stdio",
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/huaweicloud_dws_mcp_inner",
        "run",
        "server.py"
      ],
      "env": {
        "DB_HOST": "host_ip",
        "DB_PORT": "port_no",
        "DB_NAME": "database",
        "DB_USER": "username",
        "DB_PWD": "password"
      }
    }
  }
}
```
> 参数说明：将env中对应字段值替换为集群需要连接的节点对应的信息 
> 
> /path/to/huaweicloud_dws_mcp_inner"   替换为huaweicloud_dws_mcp_inner目录
> 
> host_ip   替换为集群实际ip地址
> 
> port_no   替换为实际端口号
> 
> database  替换为需要连接的数据库名
> 
> username  替换为需要连接的用户名
> 
> password  替换为上述用户的密码

如果因网络问题无法使用uv，可以通过python启动server，步骤如下：
+ 在源码目录下通过pip安装dws-mcp-server

  ```pip install .```
+ 将cline的mcp server配置更换为：
```
{
  "mcpServers": {
    "dws": {
      "disabled": false,
      "timeout": 60,
      "type": "stdio",
      "command": "python",
      "args": [

        "/path/to/huaweicloud_dws_mcp_inner/src/server.py",
      ],
      "env": {
        "DB_HOST": "host_ip",
        "DB_PORT": "port_no",
        "DB_NAME": "database",
        "DB_USER": "username",
        "DB_PWD": "password"
      }
    }
  }
}
```
> /path/to/huaweicloud_dws_mcp_inner/src/server.py 替换为 DWS MCP Server 源码中 server.py 的完整路径。

保存配置信息后，观察cline mcp页面是否成功加载dws mcp server，若如下图能够加载dws server及显示对应工具及资源说明配置成功

![cline mcpserver 配置成功界面](images/mcpconfig.png)

## 4 开始体验
完成上述配置后，即可在 Cline 客户端中，通过 Agent 或大模型连接 DWS 集群执行数据分析任务。
+ 在cline的对话框中输入需要完成的数据分析任务

![cline 对话框界面](images/cline_task.PNG)

+ 发送任务后，cline会调用模型并依据推理结果发起一系列tools或resource的调用请求。观察请求主体并选择同意（可以按需开启自动同意执行）

![cline 发起请求图示](images/cline_approve.PNG)

+ 大模型会通过一系列与dws的交互以及获取的查询结果进行分析，最终呈现结果

![cline 结果输出图示](images/cline_result.PNG)
