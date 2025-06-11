# coding: utf-8

import logging

from huaweicloudsdkeip.v2.region.eip_region import EipRegion
from typing import List
from tools.utils import get_aksk
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkeip.v2 import EipClient
from huaweicloudsdkeip.v2 import CreatePublicipBandwidthOption
from huaweicloudsdkeip.v2 import CreatePublicipRequestBody
from huaweicloudsdkeip.v2 import CreatePublicipRequest
from huaweicloudsdkeip.v2 import CreatePublicipOption
from huaweicloudsdkeip.v2 import ListPublicipsRequest
from huaweicloudsdkeip.v2 import ShowPublicipRequest
from huaweicloudsdkeip.v2 import DeletePublicipRequest
from huaweicloudsdkcore.exceptions import exceptions
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
tools = []


def get_region(region_name: str) -> str:
    region_list = {
        "中东-阿布扎比-OP5": "ae-ad-1",
        "非洲-开罗": "af-north-1",
        "非洲-约翰内斯堡": "af-south-1",
        "中国-香港": "ap-southeast-1",
        "亚太-曼谷": "ap-southeast-2",
        "亚太-新加坡": "ap-southeast-3",
        "亚太-雅加达": "ap-southeast-4",
        "华东-上海二": "cn-east-2",
        "华东-上海一": "cn-east-3",
        "华东二": "cn-east-4",
        "华东-青岛": "cn-east-5",
        "华北-北京一": "cn-north-1",
        "华北-乌兰察布-汽车一": "cn-north-11",
        "华北-北京二": "cn-north-2",
        "华北-北京四": "cn-north-4",
        "华北-乌兰察布一": "cn-north-9",
        "华南-广州": "cn-south-1",
        "华南-深圳": "cn-south-2",
        "华南-广州-友好用户环境": "cn-south-4",
        "西南-贵阳一": "cn-southwest-2",
        "欧洲-巴黎": "eu-west-0",
        "拉美-墨西哥城二": "la-north-2",
        "拉美-圣地亚哥": "la-south-2",
        "中东-利雅得": "me-east-1",
        "亚太-吉隆坡-OP6": "my-kualalumpur-1",
        "拉美-墨西哥城一": "na-mexico-1",
        "俄罗斯-莫斯科-OP4": "ru-moscow-1",
        "俄罗斯-莫斯科二": "ru-northwest-2",
        "拉美-圣保罗一": "sa-brazil-1",
        "土耳其-伊斯坦布尔": "tr-west-1",
    }

    # if region_name in region_list:
    #     return region_list[region_name]

    # return None
    return next(
        (value for key, value in region_list.items() if region_name in key), None
    )


class EipConfig(BaseModel):
    region: str = Field(
        default="cn-south-1",
        description="购买的ecs所属区地域ID，默认是华南-广州;区域有-代表广州-cn-south-1 、华东-上海一cn-east-3",
    )
    charge_mode: str = Field(
        default="bandwidth",
        description="功能说明：按带宽计费还是按流量计费。取值范围：bandwidth（按带宽计费），traffic（按流量计费），不填或者为空时默认是bandwidth。",
    )

    name: str = Field(
        default=None,
        description="功能说明：带宽名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点） 约束：如果share_type是PER，该参数必须带，如果share_type是WHOLE并且id有值，该参数会忽略。 最小长度：1最大长度：64",
    )

    share_type: str = Field(
        default="PRE",
        description="取值范围：PER，WHOLE（P   ER为独占带宽，WHOLE是共享带宽）。约束：该字段为WHOLE时，必须指定带宽ID。",
    )

    size: int = Field(
        default=None,
        description="功能说明：带宽大小  带宽大小当未输入带宽id，创建独占带宽时，该字段为必输 取值范围：默认1Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。约束：share_type是PER，该参数必须带，如果share_type是WHOLE并且id有值，该参数会忽略",
    )

    type: str = Field(
        default="5_bgp",
        description="弹性公网IP的类型 5_bgp（全动态BGP），5_sbgp（静态BGP）",
    )

    id: str = Field(
        default=None,
        description="功能说明：带宽ID，创建WHOLE类型带宽的弹性公网IP时可以指定之前的共享带宽创建 取值范围：WHOLE类型的带宽ID 最大长度：36",
    )

    ip_version: int = Field(
        default=4,
        description="功能说明：弹性公网IP的版本取值范围：4、6，ipv6表示开启NAT64能力 约束：必须是系统具体支持的类型  不填或空字符串时，默认创建ipv4",
    )

    alias: str = Field(
        default=None,
        description="弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  最大长度：64",
    )


def create_client(region: str) -> EipClient:
    ak, sk = get_aksk()
    credentials = BasicCredentials(ak, sk)

    client = (
        EipClient.new_builder()
        .with_credentials(credentials)
        .with_region(EipRegion.value_of(region))
        .build()
    )

    return client


@tools.append
def create_publicip(eipConfig: EipConfig) -> str:
    """申请弹性公网IP

        Args:
            region_name: 地域，例如：北京四, 上海二, 香港

            share_type: 功能说明：带宽类型 取值范围：PER，WHOLE（PER为独占带宽，WHOLE是共享带宽）。约束：该字段为WHOLE时，必须指定带宽ID。

            id: 功能说明：带宽ID，创建WHOLE类型带宽的弹性公网IP时可以指定之前的共享带宽创建  取值范围：WHOLE类型的带宽ID 最大长度：36。

            size: 功能说明：带宽大小，当未输入带宽id，创建独占带宽时，该字段为必输 取值范围：默认1Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。
                        约束：share_type是PER，该参数必须带，如果share_type是WHOLE并且id有值，该参数会忽略。
                            注意：调整带宽时的最小单位会根据带宽范围不同存在差异。
                            小于等于300Mbit/s：默认最小单位为1Mbit/s。300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。大于1000Mbit/s：默认最小单位为500Mbit/s。

            ip_address 功能说明：希望申请到的弹性公网IP的地址，不指定时由系统自动分配
                        约束：必须为IPv4地址格式，且必须在可用地址池范围内 最大长度：15
            type 功能说明：弹性公网IP的类型 取值范围：5_bgp（全动态BGP），5_sbgp（静态BGP），5_youxuanbgp（优选BGP）华南-广州：5_bgp、5_sbgp 华东-上海一：5_bgp、5_sbgp 华东-上海二：5_bgp、5_sbgp 华北-北京一：5_bgp、5_sbgp 中国-香港：5_bgp、5_youxuanbgp 亚太-曼谷：5_bgp 亚太-新加坡：5_bgp 非洲-约翰内斯堡：5_bgp 西南-贵阳一：5_sbgp 华北-北京四：5_bgp、5_sbgp 拉美-圣地亚哥：5_bgp 拉美-圣保罗一：5_bgp 拉美-墨西哥城一：5_bgp 拉美-布宜诺斯艾利一：5_bgp 拉美-利马一：5_bgp 拉美-圣地亚哥二： 5_bgp 约束：必须是系统具体支持的类型。 publicip_id为IPv4端口，所以"publicip_type"字段未给定时，默认为5_bgp。
            ip_version 功能说明：弹性公网IP的版本 取值范围：4、6，ipv6表示开启NAT64能力 约束：必须是系统具体支持的类型 不填或空字符串时，默认创建ipv4 缺省值：4
            alias 功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点） 最大长度：64

    Return:
        正常（状态码200）返回列表包含任务id和云硬盘id列表，格式： {
          "publicip" : {
            "tenant_id" : "8b7e35ad379141fc9df3e178bd64f55c",
            "bandwidth_size" : 0,
            "public_ip_address" : "161.xx.xx.7",
            "ip_version" : 4,
            "create_time" : "2015-07-16 04:10:52",
            "id" : "f588ccfa-8750-4d7c-bf5d-2ede24414706",
            "type" : "5_bgp",
            "status" : "PENDING_CREATE"
          }
        }
    """

    client = create_client(eipConfig.region)

    try:
        if eipConfig.share_type == "WHOLE" and eipConfig.id == "":
            return "共享带宽下请输入port_id"
        else:
            if eipConfig.size is None:
                return "独占带宽下请输入size"
            eipConfig.id = None

        request = CreatePublicipRequest()
        bandwidth = CreatePublicipBandwidthOption(
            charge_mode=eipConfig.charge_mode,
            id=eipConfig.id,
            name=eipConfig.name,
            share_type=eipConfig.share_type,
            size=eipConfig.size,
        )

        publicip = CreatePublicipOption(
            type=eipConfig.type, ip_version=eipConfig.ip_version, alias=eipConfig.alias
        )

        body = CreatePublicipRequestBody(
            bandwidth=bandwidth,
            enterprise_project_id="0",
            publicip=publicip,
        )
        request.body = body

        response = client.create_publicip(request)

        return response

    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
              {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def delete_publicip(
    region: str = Field(
        default="cn-south-1",
        description="购买的ecs所属区地域ID，默认是华南-广州;区域有-代表广州-cn-south-1 、华东-上海一cn-east-3",
    ),
    publicip_id: str = Field(default="cn-south-1", description="弹性公网IP唯一标识"),
) -> str:
    """删除弹性公网IP

    Args:
     region: 地域，例如：北京四, 上海二, 香港
     publicip_id: 弹性公网IP唯一标识。

    """

    client = create_client(region)

    try:
        request = DeletePublicipRequest(publicip_id=publicip_id)
        response = client.delete_publicip(request)
        return response

    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
            {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def list_public_ips(
    region: str = Field(
        default="cn-south-1",
        description="购买的ecs所属区地域ID，默认是华南-广州;区域有-代表广州-cn-south-1 、华东-上海一cn-east-3",
    ),
    marker: str = Field(
        default=None,
        description="取值为上一页数据的最后一条记录的id，为空时为查询第一 最大长度：36",
    ),
    limit: int = Field(
        default=None,
        description="每页返回的个数, 取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定最小值：0",
    ),
    ip_version: int = Field(
        default=None, description="IP地址版本信息，4：IPv4，6：开启NAT64能力"
    ),
    public_ip_address: List[str] = Field(
        default=None,
        description="IPv4时是申请到的弹性公网IP地址，IPv6时是IPv6地址对应的IPv4地址",
    ),
    private_ip_address: List[str] = Field(
        default=None, description="关联端口的私有IP地址"
    ),
    id: List[str] = Field(default=None, description="弹性公网IP唯一标识"),
) -> str:
    """查询弹性公网IP列表

    Args:
         region: 地域，例如：北京四, 上海二, 香港
         marker: 取值为上一页数据的最后一条记录的id，为空时为查询第一页。
         limit: 每页返回的个数
         ip_version: IP地址版本信息，4：IPv4，6：开启NAT64能力
         public_ip_address: IPv4时是申请到的弹性公网IP地址，IPv6时是IPv6地址对应的IPv4地址
         private_ip_address: 关联端口的私有IP地址
         id: 弹性公网IP唯一标识
    Return:
         alias: 弹性公网IP名称
         type: 弹性公网IP的类型
         status: 弹性公网IP的状态
         public_ip_address: Pv4时是申请到的弹性公网IP地址，IPv6时是IPv6地址对应的IPv4地址
         private_ip_address 绑定弹性公网IP的私有IP地址
         id: 弹性公网IP唯一标识
         bandwidth_size: 带宽大小，单位为Mbit/s
         bandwidth_share_type: 表示共享带宽或者独享带宽
         bandwidth_name : 带宽名称
         bandwidth_id : 弹性公网IP对应带宽ID

    """

    client = create_client(region)

    try:
        request = ListPublicipsRequest(
            marker=marker,
            limit=limit,
            ip_version=ip_version,
            id=id,
            private_ip_address=private_ip_address,
            public_ip_address=public_ip_address,
        )
        response = client.list_publicips(request)
        return response

    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
            {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def show_publicip(region_name: str, publicip_id: str) -> str:
    """查询弹性公网IP。

      Args:
       region_name: 地域，例如：北京四, 上海二, 香港
       publicip_id: 弹性公网IP唯一标识 最大长度：36。

    Return:

    """
    region = get_region(region_name)
    if region is None:
        return "无效地域，请确认地域。"
    ak, sk = get_aksk()
    credentials = BasicCredentials(ak, sk)

    client = (
        EipClient.new_builder()
        .with_credentials(credentials)
        .with_region(EipClient.value_of(region))
        .build()
    )

    try:
        request = ShowPublicipRequest(publicip_id=publicip_id)
        response = client.delete_publicip(request)
        return response

    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
               {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg
