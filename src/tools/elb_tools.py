# coding: utf-8

import logging

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkelb.v2 import (
    CreateLoadbalancerReq,
    CreateLoadbalancerRequest,
    CreateLoadbalancerRequestBody,
    DeleteLoadbalancerRequest,
    ListLoadbalancersRequest,
    ShowLoadbalancerRequest,
    CreatePoolRequest,
    CreatePoolRequestBody,
    CreatePoolReq,
    ElbClient,
)
from huaweicloudsdkelb.v2.region.elb_region import ElbRegion
from pydantic import Field

from tools.utils import get_aksk

logger = logging.getLogger(__name__)
tools = []


def create_client(region: str) -> ElbClient:
    ak, sk = get_aksk()
    credentials = BasicCredentials(ak, sk)

    client = (
        ElbClient.new_builder()
        .with_credentials(credentials)
        .with_region(ElbRegion.value_of(region))
        .build()
    )

    return client


@tools.append
def create_pool(
    region: str = Field(
        default="cn-south-1", description="地域，例如：北京四, 上海二, 香港"
    ),
    loadbalancer_id: str = Field(default=None, description="负载均衡器ID"),
    listener_id: str = Field(default=None, description="监听器ID"),
    name: str = Field(description="后端云服务器组名称, 不传默认给我生成一个名称"),
    protocol: str = Field(
        default="TCP",
        description="后端云服务器组的后端协议。支持TCP、UDP和HTTP。当指定listener_id创建后端云服务器组时，后端云服务器组的protocol和它关联的监听器的protocol有如下关系：监听器的protocol为UDP时，后端云服务器组的protocol必须为UDP；监听器的protocol为TCP时，后端云服务器组的protocol必须为TCP；监听器的protocol为HTTP或TERMINATED_HTTPS时，后端云服务器组的protocol必须为HTTP。",
    ),
    lb_algorithm: str = Field(
        description="后端云服务器组的负载均衡算法。取值范围：ROUND_ROBIN：加权轮询算法。LEAST_CONNECTIONS：加权最少连接算法。SOURCE_IP：源IP算法。当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。"
    ),
):
    """创建后端云服务器组

        Args:
            lb_algorithm: 后端云服务器组的负载均衡算法。取值范围：ROUND_ROBIN：加权轮询算法。LEAST_CONNECTIONS：加权最少连接算法。SOURCE_IP：源IP算法。当该字段的取值为SOURCE_IP时，后端云服务器组绑定的后端云服务器的weight字段无效。
            region: 地域，例如：北京四, 上海二, 香港
            loadbalancer_id: 负载均衡器ID
            listener_id: 监听器ID
            name: 后端云服务器组名称
            protocol: 后端云服务器组的后端协议。支持TCP、UDP和HTTP。当指定listener_id创建后端云服务器组时，后端云服务器组的protocol和它关联的监听器的protocol有如下关系：监听器的protocol为UDP时，后端云服务器组的protocol必须为UDP；监听器的protocol为TCP时，后端云服务器组的protocol必须为TCP；监听器的protocol为HTTP或TERMINATED_HTTPS时，后端云服务器组的protocol必须为HTTP。

    Return:
        创建结果
    """

    client = create_client(region)

    try:
        body = CreatePoolRequestBody(
            CreatePoolReq(
                loadbalancer_id=loadbalancer_id,
                listener_id=listener_id,
                name=name,
                protocol=protocol,
                lb_algorithm=lb_algorithm,
            )
        )

        response = client.create_pool(CreatePoolRequest(body))

        return response

    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
              {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def create_loadbalancer(
    region: str = Field(
        default="cn-south-1",
        description="购买的ecs所属区地域ID，默认是华南-广州;区域有-代表广州-cn-south-1 、华东-上海一cn-east-3",
    ),
    vip_subnet_id: str = Field(
        default=None,
        description="负载均衡器所在的子网IPv4子网ID。可通过查询子网列表获取（字段是neutron_subnet_id）。vip_address将从该子网中产生。只支持指定IPv4子网。暂不支持IPv6。",
    ),
    name: str = Field(
        default=None,
        description="负载均衡器名称。支持的最大字符长度：255, 为空随便生成一个名称",
    ),
):
    """创建负载均衡器

        Args:
            name:负载均衡器名称。支持的最大字符长度：255
            region: 地域，例如：北京四, 上海二, 香港
            vip_subnet_id: 负载均衡器所在的子网IPv4子网ID。可通过查询子网列表获取（字段是neutron_subnet_id）。vip_address将从该子网中产生。只支持指定IPv4子网。暂不支持IPv6。

    Return:
    """

    client = create_client(region)

    try:
        body = CreateLoadbalancerRequestBody(
            CreateLoadbalancerReq(vip_subnet_id=vip_subnet_id, name=name)
        )

        response = client.create_loadbalancer(CreateLoadbalancerRequest(body))

        return response

    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
              {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def delete_loadbalancer(
    region: str = Field(
        default="cn-south-1",
        description="购买的ecs所属区地域ID，默认是华南-广州;区域有-代表广州-cn-south-1 、华东-上海一cn-east-3",
    ),
    loadbalancer_id: str = Field(default="None", description="负载均衡器id。必填"),
):
    """删除负载均衡

    Args:
     region: 地域，例如：北京四, 上海二, 香港
     loadbalancer_id: 负载均衡器id。必填。

    """

    client = create_client(region)

    try:
        request = DeleteLoadbalancerRequest(loadbalancer_id=loadbalancer_id)
        response = client.delete_loadbalancer(request)
        return response

    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
            {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def list_loadbalancers(
    region: str = Field(
        default="cn-south-1",
        description="购买的ecs所属区地域ID，默认是华南-广州;区域有-代表广州-cn-south-1 、华东-上海一cn-east-3",
    ),
    operating_status: str = Field(
        default=None,
        description="负载均衡器的操作状态。取值范围：可以为ONLINE和FROZEN。",
    ),
    vpc_id: str = Field(
        default=None,
        description="负载均衡器所在的虚拟私有云ID。",
    ),
    vip_subnet_id: str = Field(
        default=None,
        description="负载均衡器所在的子网IPv4子网ID。",
    ),
):
    """查询负载均衡列表

    Args:
     region: 地域，例如：北京四, 上海二, 香港
     operating_status: 负载均衡器的操作状态。取值范围：可以为ONLINE和FROZEN。。
     vpc_id: 负载均衡器所在的虚拟私有云ID。
     vip_subnet_id: 负载均衡器所在的子网IPv4子网ID。
    """

    client = create_client(region)

    try:
        request = ListLoadbalancersRequest(
            operating_status=operating_status,
            vpc_id=vpc_id,
            vip_subnet_id=vip_subnet_id,
        )
        response = client.list_loadbalancers(request)
        return response

    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
            {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def show_loadbalancer(
    region: str = Field(
        default="cn-south-1",
        description="购买的ecs所属区地域ID，默认是华南-广州;区域有-代表广州-cn-south-1 、华东-上海一cn-east-3",
    ),
    loadbalancer_id: str = Field(default="None", description="负载均衡器id。必填"),
):
    """查询负载均衡详情

    Args:
     region: 地域，例如：北京四, 上海二, 香港
     loadbalancer_id: 负载均衡器id。必填。
    """

    client = create_client(region)

    try:
        request = ShowLoadbalancerRequest(loadbalancer_id=loadbalancer_id)
        response = client.show_loadbalancer(request)
        return response

    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
            {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg
