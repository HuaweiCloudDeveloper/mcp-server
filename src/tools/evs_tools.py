# coding: utf-8

import logging
from tools.utils import get_aksk
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkevs.v2.region.evs_region import EvsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkevs.v2 import EvsClient, CinderListAvailabilityZonesRequest, CreateVolumeRequest, CreateVolumeOption,\
    CreateVolumeRequestBody, ListVolumesRequest, DeleteVolumeRequest, ShowVolumeRequest


logger = logging.getLogger(__name__)


tools = []


def get_region(region_name: str) -> str:
    region_list = {
    "中东-阿布扎比-OP5":"ae-ad-1",
    "非洲-开罗":"af-north-1",
    "非洲-约翰内斯堡":"af-south-1",
    "中国-香港":"ap-southeast-1",
    "亚太-曼谷":"ap-southeast-2",
    "亚太-新加坡":"ap-southeast-3",
    "亚太-雅加达":"ap-southeast-4",
    "华东-上海二":"cn-east-2",
    "华东-上海一":"cn-east-3",
    "华东二":"cn-east-4",
    "华东-青岛":"cn-east-5",
    "华北-北京一":"cn-north-1",
    "华北-乌兰察布-汽车一":"cn-north-11",
    "华北-北京二":"cn-north-2",
    "华北-北京四":"cn-north-4",
    "华北-乌兰察布一":"cn-north-9",
    "华南-广州":"cn-south-1",
    "华南-深圳":"cn-south-2",
    "华南-广州-友好用户环境":"cn-south-4",
    "西南-贵阳一":"cn-southwest-2",
    "欧洲-巴黎":"eu-west-0",
    "拉美-墨西哥城二":"la-north-2",
    "拉美-圣地亚哥":"la-south-2",
    "中东-利雅得":"me-east-1",
    "亚太-吉隆坡-OP6":"my-kualalumpur-1",
    "拉美-墨西哥城一":"na-mexico-1",
    "俄罗斯-莫斯科-OP4":"ru-moscow-1",
    "俄罗斯-莫斯科二":"ru-northwest-2",
    "拉美-圣保罗一":"sa-brazil-1",
    "土耳其-伊斯坦布尔":"tr-west-1"}

    # if region_name in region_list:
    #     return region_list[region_name]

    # return None
    return next((value for key, value in region_list.items() if region_name in key), None)


@tools.append
def evs_list_availability_zones(region_name: str) -> str:
    """查询云硬盘(EVS)所有的可用分区信息。     

    Args:
        region_name: 地域，例如：北京四, 上海二, 香港

    Return:
        正常返回列表包含可用区名称和状态，格式： [  { "zoneState": { "available": true }, "zoneName": "cn-south-4a" }]
        异常返回错误信息。
    """

    region = get_region(region_name)
    if region is None:
        return "无效地域，请确认地域。"
    
    ak, sk = get_aksk()
    credentials = BasicCredentials(ak, sk)

    client = EvsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(EvsRegion.value_of(region)) \
        .build()

    try:
        request = CinderListAvailabilityZonesRequest()
        response = client.cinder_list_availability_zones(request)
        return response 
    except exceptions.ClientRequestException as e:    
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
            {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def create_volume(region_name: str, az: str, evs_name: str, evs_size: int, evs_type: str = "SSD",
                  shared: bool = False) -> str:
    """查询云硬盘(EVS)所有的可用分区信息。     

    Args:
        region_name: 地域，例如：北京四, 上海二, 香港
        az: 指定要创建云硬盘的可用区，每个地域下面有多个可用区域
        evs_name: 云硬盘的名称
        evs_size: 云硬盘大小，单位为GB
        evs_type: 云硬盘类型。目前支持\&quot;SATA\&quot;，\&quot;SAS\&quot;，\&quot;GPSSD\&quot;，\&quot;SSD\&quot;，\&quot;ESSD\&quot;，\&quot;GPSSD2\&quot;和\&quot;ESSD2\&quot;七种。  - \&quot;SATA\&quot;为普通IO云硬盘(已售罄) - \&quot;SAS\&quot;为高IO云硬盘 - \&quot;GPSSD\&quot;为通用型SSD云硬盘 - \&quot;SSD\&quot;为超高IO云硬盘 - \&quot;ESSD\&quot;为极速IO云硬盘 - \&quot;GPSSD2\&quot;为通用型SSD V2云硬盘 - \&quot;ESSD2\&quot;为极速型SSD V2云硬盘 当指定的云硬盘类型在avaliability_zone内不存在时，则创建云硬盘失败。
        shared: 是否为共享云硬盘。true为共享盘，false为普通云硬盘。
    Return:
        正常（状态码202）返回列表包含任务id和云硬盘id列表，格式： {  "job_id" : "70a599e0-31e7-49b7-b260-868f441e862b",
                                                            "volume_ids" : [ "e1fa3e72-8c92-4871-9152-bf66fef0afe9" ]
                                                            }
        异常返回错误信息。
    """
    
    region = get_region(region_name)
    if region is None:
        return "无效地域，请确认地域。"
    
    # Todo 待实现对所有输入参数进行有效性校验

    ak, sk = get_aksk()    
    credentials = BasicCredentials(ak, sk)

    client = EvsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(EvsRegion.value_of(region)) \
        .build()

    try:
        request = CreateVolumeRequest()
        volumebody = CreateVolumeOption(
            availability_zone=az,
            multiattach=shared,
            name=evs_name,
            size=evs_size,
            volume_type=evs_type
        )
        request.body = CreateVolumeRequestBody(
            volume=volumebody
        )
        response = client.create_volume(request)
        return (response)
    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
            {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def list_all_volumes(region_name: str) -> str:
    """查询所有云硬盘详情。     

    Args:
        region_name: 地域，例如：北京四, 上海二, 香港

    Return:
        正常返回云硬盘数量以及硬盘信息列表，格式： {"count":43,"volumes":[
                {"id":"","name":"ecs-be83-volume-0000","status":"in-use","size":50,"user_id":"5d8d9c47ae8c4e40aaa9e8e136498310","service_type":"EVS",
                "volume_type":"GPSSD","shareable":"false","multiattach":false}]}
        异常返回错误信息。
    """

    region = get_region(region_name)
    if region is None:
        return "无效地域，请确认地域。"
    
    ak, sk = get_aksk()
    credentials = BasicCredentials(ak, sk)

    client = EvsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(EvsRegion.value_of(region)) \
        .build()

    try:
        request = ListVolumesRequest()
        response = client.list_volumes(request)
        return response
    except exceptions.ClientRequestException as e:    
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
            {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def delete_volume(region_name: str, vol_id:str) -> str:
    """删除云硬盘。     

    Args:
        region_name: 地域，例如：北京四, 上海二, 香港
        vol_id: 云硬盘的id, 可以通过查询所有云硬盘详情工具来获取。

    Return:
        正常返回删除任务的JobID
        异常返回错误信息。
    """

    region = get_region(region_name)
    if region is None:
        return "无效地域，请确认地域。"
    
    ak, sk = get_aksk()
    credentials = BasicCredentials(ak, sk)

    client = EvsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(EvsRegion.value_of(region)) \
        .build()

    try:
        request = DeleteVolumeRequest()
        request.volume_id = vol_id
        response = client.delete_volume(request)
        return response
    except exceptions.ClientRequestException as e:    
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
            {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def list_volume_info(region_name: str, vol_id:str) -> str:
    """查询单个云硬盘的详情。     

    Args:
        region_name: 地域，例如：北京四, 上海二, 香港
        vol_id: 云硬盘的id, 可以通过查询所有云硬盘详情工具来获取。

    Return:
        正常返回云硬盘详情： {"id":"","name":"ecs-be83-volume-0000","status":"in-use","size":50,"user_id":"5d8d9c47ae8c4e40aaa9e8e136498310","service_type":"EVS",
                "volume_type":"GPSSD","shareable":"false","multiattach":false}
        异常返回错误信息。
    """

    region = get_region(region_name)
    if region is None:
        return "无效地域，请确认地域。"
    
    ak, sk = get_aksk()
    credentials = BasicCredentials(ak, sk)

    client = EvsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(EvsRegion.value_of(region)) \
        .build()

    try:
        request = ShowVolumeRequest()
        request.volume_id = vol_id
        response = client.show_volume(request)
        return response
    except exceptions.ClientRequestException as e:    
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
            {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg

