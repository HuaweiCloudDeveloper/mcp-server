from dataclasses import dataclass
from typing import Optional, Literal

from pydantic import BaseModel, ConfigDict

TransportType = Literal["sse", "stdio"]


@dataclass
class MCPConfig:
    sse_port: int
    service_code: str
    transport: TransportType
    ak: Optional[str] = None
    sk: Optional[str] = None

    def check(self):
        if not self.service_code:
            raise ValueError("service_code必须已经初始化")

        if self.transport == "sse" and self.sse_port == 0:
            raise ValueError("sse服务端口不能设为0")


class TopResponseModel(BaseModel):
    model_config = ConfigDict(
        extra="allow", from_attributes=True, arbitrary_types_allowed=True
    )

    def __init__(self, **data):
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = TopResponseModel(**value)
            elif isinstance(value, list) and value and isinstance(value[0], dict):
                data[key] = [TopResponseModel(**item) for item in value]
        super().__init__(**data)
