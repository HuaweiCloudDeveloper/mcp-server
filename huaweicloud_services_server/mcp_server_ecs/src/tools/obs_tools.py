# coding: utf-8
import traceback
import logging
from pydantic import Field
from tools.utils import get_aksk
from obs import CreateBucketHeader, HeadPermission, ObsClient

logger = logging.getLogger(__name__)


tools = []


def get_endpoint(region_name: str) -> str:
    endpoint_list = {
        "约翰内斯堡": "obs.af-south-1.myhuaweicloud.com",
        "香港": "obs.ap-southeast-1.myhuaweicloud.com",
        "曼谷": "obs.ap-southeast-2.myhuaweicloud.com",
        "新加坡": "obs.ap-southeast-3.myhuaweicloud.com",
        "雅加达": "obs.ap-southeast-4.myhuaweicloud.com",
        "上海二": "obs.cn-east-2.myhuaweicloud.com",
        "上海一": "obs.cn-east-3.myhuaweicloud.com",
        "北京一": "obs.cn-north-1.myhuaweicloud.com",
        "北京四": "obs.cn-north-4.myhuaweicloud.com",
        "乌兰察布一": "obs.cn-north-9.myhuaweicloud.com",
        "广州": "obs.cn-south-1.myhuaweicloud.com",
        "深圳": "obs.cn-south-2.myhuaweicloud.com",
        "广州-友好用户环境": "obs.cn-south-4.myhuaweicloud.com",
        "贵阳一": "obs.cn-southwest-2.myhuaweicloud.com",
        "墨西哥城二": "obs.la-north-2.myhuaweicloud.com",
        "圣地亚哥": "obs.la-south-2.myhuaweicloud.com",
        "墨西哥城一": "obs.na-mexico-1.myhuaweicloud.com",
        "圣保罗一": "obs.sa-brazil-1.myhuaweicloud.com",
        "伊斯坦布尔": "obs.tr-west-1.myhuaweicloud.com",
    }

    if region_name in endpoint_list:
        return "https://" + endpoint_list[region_name]

    raise ValueError("无效地域，请确认地域。")


def get_obsclient(server: str) -> ObsClient:
    ak, sk = get_aksk()
    return ObsClient(access_key_id=ak, secret_access_key=sk, server=server)


def get_location_from_server(server: str) -> str:
    return server.split(".")[1]


def get_resp_msg(resp) -> str:
    if resp.status < 300:
        return "操作成功"

    error_msg = getattr(resp, "errorMessage", None)
    status_code = getattr(resp, "status", "未知")
    msg = f"操作失败，{f'错误信息：{error_msg}' if error_msg else f'错误码：{status_code}'}"
    logger.warning(msg)
    return msg


@tools.append
def bucket_exist(
    bucket_name: str = Field("桶名称", description="桶名称"),
    region_name: str = Field("地域", description="地域，例如：北京四, 上海二, 香港"),
) -> str:
    """根据桶名称、地域判断桶是否存在.

    Args:
        bucket_name: 桶名称
        region_name: 地域，例如：北京四, 上海二, 香港
    """

    try:
        server = get_endpoint(region_name)
        obsClient = get_obsclient(server)
        # 判断桶是否存在
        resp = obsClient.headBucket(bucket_name)
        # 返回码为2xx时，接口调用成功，否则接口调用失败
        if resp.status < 300:
            return "存在"
        elif resp.status == 404:
            return "不存在"
        else:
            return get_resp_msg(resp)
    except Exception as ex:
        logger.error("发生异常：\n%s", traceback.format_exc())
        return f"操作失败，错误信息: {str(ex)}"


@tools.append
def get_buckets(
    region_name: str = Field("地域", description="地域，例如：北京四, 上海二, 香港"),
) -> str:
    """根据地域信息获取用户桶列表.

    Args:
        region: 地域，例如：北京四, 上海二, 香港
    """

    try:
        server = get_endpoint(region_name)
        obsClient = get_obsclient(server)
        # 列举桶，并设置isQueryLocation参数为True，同时查询桶区域
        resp = obsClient.listBuckets(True)
        # 返回码为2xx时，接口调用成功，否则接口调用失败
        buckets_info = []
        if resp.status < 300:
            for bucket in resp.body.buckets:
                bucket_info = f"""
                    name: {bucket.name}
                    location: {bucket.location}
                    type: {bucket.bucket_type}
                """
                buckets_info.append(bucket_info.strip())
            return "\n".join(buckets_info)
        else:
            return get_resp_msg(resp)
    except Exception as ex:
        logger.error("发生异常：\n%s", traceback.format_exc())
        return f"操作失败，错误信息: {str(ex)}"


@tools.append
def delete_bucket(
    bucket_name: str = Field("桶名称", description="桶名称"),
    region_name: str = Field("地域", description="地域，例如：北京四, 上海二, 香港"),
) -> str:
    """根据桶名称、地域信息删除桶.

    Args:
        bucket_name: 桶名称
        region_name: 地域，例如：北京四, 上海二, 香港
    """

    try:
        server = get_endpoint(region_name)
        obsClient = get_obsclient(server)
        resp = obsClient.deleteBucket(bucket_name)
        return get_resp_msg(resp)
    except Exception as ex:
        logger.error("发生异常：\n%s", traceback.format_exc())
        return f"操作失败，错误信息: {str(ex)}"


@tools.append
def create_bucket(
    bucket_name: str = Field("桶名称", description="桶名称"),
    region_name: str = Field("地域", description="地域，例如：北京四, 上海二, 香港"),
    storage_class: str = Field(
        "存储类别",
        description="存储类别 ，包括, 标准存储:STANDARD;低频访问存储:WARM;归档存储:COLD",
    ),
    available_zone: str = Field(
        "AZ类别", description="AZ类别 ，包括: 多AZ:3az;单AZ:默认值"
    ),
) -> str:
    """根据桶名称、地域、存储类别、AZ类型创建用户桶.

    Args:
        bucket_name: 桶名称
        region_name: 地域，例如：北京四, 上海二, 香港
        storage_class: 存储类别 ，包括, 标准存储:STANDARD;低频访问存储:WARM;归档存储:COLD
        available_zone: AZ类别 ，包括: 多AZ:3az;单AZ:默认值
    """

    try:
        server = get_endpoint(region_name)
        location = get_location_from_server(server)
        obsClient = get_obsclient(server)
        sc = {"归档存储": "COLD", "低频访问存储": "WARM"}.get(storage_class, "STANDARD")
        az = "3az" if not available_zone.strip() else None
        if az:
            header = CreateBucketHeader(
                aclControl=HeadPermission.PRIVATE, storageClass=sc, availableZone=az
            )
        else:
            header = CreateBucketHeader(
                aclControl=HeadPermission.PRIVATE, storageClass=sc
            )

        # 创建桶
        resp = obsClient.createBucket(bucket_name, header, location)
        return get_resp_msg(resp)
    except Exception as ex:
        logger.error("发生异常：\n%s", traceback.format_exc())
        return f"操作失败，错误信息: {str(ex)}"


@tools.append
def get_objects(
    bucket_name: str = Field("桶名称", description="桶名称"),
    region_name: str = Field("地域", description="地域，例如：北京四, 上海二, 香港"),
) -> str:
    """根据桶名称、地域获取用户桶中对象列表.

    Args:
        bucket_name: 桶名称
        region: 地域，例如：北京四, 上海二, 香港
    """

    try:
        server = get_endpoint(region_name)
        obsClient = get_obsclient(server)
        # 指定单次列举对象个数为100
        max_keys = 100

        # 列举桶内对象
        resp = obsClient.listObjects(
            bucket_name, max_keys=max_keys, encoding_type="url"
        )

        # 返回码为2xx时，接口调用成功，否则接口调用失败
        if resp.status < 300:
            contents_info = []
            for content in resp.body.contents:
                if not content.key.endswith("/"):
                    content_info = f"""
                        {
                        (
                            "key:",
                            content.key,
                            "size:",
                            content.size,
                            "lastModified:",
                            content.lastModified,
                            "storageClass:",
                            content.storageClass,
                        )
                    }
                    """
                    contents_info.append(content_info)
            return "\n".join(contents_info)
        else:
            return get_resp_msg(resp)
    except Exception as ex:
        logger.error("发生异常：\n%s", traceback.format_exc())
        return f"操作失败，错误信息: {str(ex)}"


@tools.append
def download_object(
    bucket_name: str = Field("桶名称", description="桶名称"),
    region_name: str = Field("地域", description="地域，例如：北京四, 上海二, 香港"),
    object_key: str = Field("对象名称", description="桶中对象的名称"),
    local_file: str = Field("本地文件", description="本地文件，需要包含路径"),
) -> str:
    """根据桶名称、地域、对象名称下载对象的内容保存到本地文件中.

    Args:
        bucket_name: 桶名称
        region_name: 地域，例如：北京四, 上海二, 香港
        object_key: 对象名称
        local_file: 本地文件，需要包含路径
    """

    try:
        server = get_endpoint(region_name)
        obsClient = get_obsclient(server)
        resp = obsClient.getObject(bucket_name, object_key, local_file)
        return get_resp_msg(resp)
    except Exception as ex:
        logger.error("发生异常：\n%s", traceback.format_exc())
        return f"操作失败，错误信息: {str(ex)}"


@tools.append
def delete_object(
    bucket_name: str = Field("桶名称", description="桶名称"),
    region_name: str = Field("地域", description="地域，例如：北京四, 上海二, 香港"),
    object_key: str = Field("对象名称", description="桶中对象的名称"),
) -> str:
    """根据桶名称、地域、对象名称删除桶中对象.

    Args:
        bucket_name: 桶名称
        region_name: 地域，例如：北京四, 上海二, 香港
        object_key: 对象名称
    """

    try:
        server = get_endpoint(region_name)
        obsClient = get_obsclient(server)
        resp = obsClient.deleteObject(bucket_name, object_key)
        return get_resp_msg(resp)
    except Exception as ex:
        logger.error("发生异常：\n%s", traceback.format_exc())
        return f"操作失败，错误信息: {str(ex)}"
