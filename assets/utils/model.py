from dataclasses import dataclass
from typing import Optional, Literal

TransportType = Literal["sse", "stdio", "http"]


@dataclass
class MCPConfig:
    port: int
    service_code: str
    transport: TransportType
    ak: Optional[str] = None
    sk: Optional[str] = None
    endpoint_domain: Optional[str] = None
    endpoint_prefix: Optional[str] = None
    project_id: Optional[str] = None
    iam_endpoint: Optional[str] = None

    def check(self):
        if not self.service_code:
            raise ValueError("service_code必须已经初始化")

        if self.transport in ("sse", "http") and self.port == 0:
            raise ValueError("sse和http服务端口不能设为0")
