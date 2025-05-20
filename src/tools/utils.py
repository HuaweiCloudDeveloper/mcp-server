# coding: utf-8

import os
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler


load_dotenv()  # 这将默认从当前目录下的 .env 文件加载变量


# Transport protocol to use ("stdio", "sse", or "streamable-http")
def get_transport():
    ak = os.getenv("HUAWEI_CLOUD_MCP_TRANSPORT", "stdio")


def get_aksk():
    ak = os.getenv("HUAWEI_CLOUD_AK", None)
    sk = os.getenv("HUAWEI_CLOUD_SK", None)
    return ak, sk


def setup_logging():
    # 创建日志目录（如果不存在）
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "app.log")

    # 全局日志格式
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 配置 RotatingFileHandler（按大小轮转日志）
    file_handler = RotatingFileHandler(
        filename = log_file,
        maxBytes = 5 * 1024 * 1024,  # 5MB
        backupCount = 3,             # 保留3个备份
        encoding = "utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # 全局根 logger 配置
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)

    # 可选：同时输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    root_logger.addHandler(console_handler)