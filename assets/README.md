# mcp-server-huaweicloud


## 运行指南

### 1. 依赖安装

`pip install -r requirements.txt`

### 2. 环境变量设置

准备AK、SK并设置到环境变量

- ak 环境变量名:  HUAWEI_ACCESS_KEY
- sk 环境变量名:  HUAWEI_SECRET_KEY


### 3. 运行方法

- 使用默认配置，直接调用`run.py`

```python
from mcp_server_huaweicloud import main


if __name__ == "__main__":
    main()
```

- 更改配置文件，创建如下py文件
```python
from pathlib import Path

from mcp_server_huaweicloud import server
from mcp_server_huaweicloud.utils import load_config


def main():
    """Huawei Cloud MCP Server"""
    import asyncio
    
    # 指定配置文件(yaml和swagger文件)目录的绝对路径
    server.config_folder = Path(__file__).parent / 'config'
    server.config_file = 'config.yaml'
    server.server_config = load_config(Path(server.config_folder) / server.config_file)
    asyncio.run(server.serve())


if __name__ == "__main__":
    main()
```

执行命令：`python run.py`
