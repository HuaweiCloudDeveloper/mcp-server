# -*- coding: utf-8 -*-
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkims.v2.region.ims_region import ImsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkims.v2 import ImsClient, CreateImageRequest, ListImagesRequest
from huaweicloudsdkims.v2 import CreateImageRequestBody
from tools.utils import get_aksk

tools = []


# 创建ims客户端
def get_ims_client(region="cn-south-1"):
    ak, sk = get_aksk()  # 从环境变量中获取AK和SK
    credentials = BasicCredentials(ak, sk)  # 创建凭证对象
    return (
        ImsClient.new_builder()
        .with_credentials(credentials)
        .with_region(ImsRegion.value_of(region))
        .build()
    )


# 制作系统盘镜像
@tools.append
def create_system_disk_image(region, name, instance_id):
    """
    华为云IMS-系统盘镜像
    功能说明：
        通过指定区域（region）和云主机实例ID（instance_id），
        调用华为云 IMS 服务创建一个整机镜像。

    参数：
        region (str): 区域标识符，如 'cn-north-4'
        name (str): 镜像名称，用于标识该镜像（需唯一）
        instance_id (str): 云主机实例ID，基于该实例制作镜像
    返回：
        return ：成功则打印响应信息，失败则打印错误信息
    """
    try:
        # 获取 IMS 客户端连接
        client = get_ims_client(region)

        # 构建请求体
        request = CreateImageRequest()
        request.body = CreateImageRequestBody(name=name, instance_id=instance_id)

        # 发起请求并输出结果
        response = client.create_image(request)
        print("系统盘镜像制作请求提交成功，响应如下：")
        print(response)

    except exceptions.ClientRequestException as e:
        print("系统盘镜像制作请求失败，错误信息如下：")
        print(f"状态码: {e.status_code}")
        print(f"请求ID: {e.request_id}")
        print(f"错误码: {e.error_code}")
        print(f"错误信息: {e.error_msg}")


# 查询镜像列表
@tools.append
def query_ims_images_list(
    region,
    name=None,
    imagetype="private",
    os_type="Linux",
    platform="Ubuntu",
    architecture="arm",
):
    """
    查询华为云 IMS 镜像列表

    功能说明：
        根据指定的区域和筛选条件，查询符合条件的镜像列表。
        支持按名称、类型、操作系统等条件过滤。
    参数说明：
        region (str): 区域标识符，例如 'cn-north-4'
        name (str): 镜像名称，不支持模糊匹配
        imagetype (str): 镜像类型，默认为 'private'（私有镜像）
                        可选值: gold（公共镜像）、private（私有镜像）、shared（共享镜像）、market（市场镜像）
        os_type (str): 操作系统类型，默认为 'Linux'
                       可选值: Linux、Windows、Other
        platform (str): 平台类型，默认为 'Ubuntu'
                        示例值: Ubuntu、CentOS、Windows 等
        architecture (str): 架构类型，默认为 'arm'
                            可选值: x86、arm

    返回：
       return object | None: 成功返回响应对象，失败返回 None
    """

    # 参数合法性检查
    valid_imagetypes = ["gold", "private", "shared", "market"]
    valid_os_types = ["Linux", "Windows", "Other"]
    valid_platform = [
        "Ubuntu",
        "Windows",
        "RedHat",
        "SUSE",
        "CentOS",
        "Debian",
        "OpenSUSE",
        "Fedora",
        "Oracle Linux",
        "EulerOS",
        "Huawei Cloud EulerOS",
        "CoreOS",
        "Other",
    ]
    valid_architectures = ["x86", "arm"]

    if imagetype not in valid_imagetypes:
        raise ValueError(f"imagetype 必须是 {valid_imagetypes} 中的一个值")

    if os_type not in valid_os_types:
        raise ValueError(f"os_type 必须是 {valid_os_types} 中的一个值")

    if platform not in valid_platform:
        raise ValueError(f"platform 必须是 {valid_platform} 中的一个值")

    if architecture not in valid_architectures:
        raise ValueError(f"architecture 必须是 {valid_architectures} 中的一个值")

    try:
        client = get_ims_client(region)
        request = ListImagesRequest()

        if name is not None:
            request.name = name  # 精确匹配，不支持模糊查询
        request.imagetype = imagetype
        request.os_type = os_type
        request.platform = platform
        request.architecture = architecture
        response = client.list_images(request)
        print("镜像列表查询成功：")
        print(response)
        return response
    except exceptions.ClientRequestException as e:
        print("镜像列表查询失败，错误信息如下：")
        print(f"状态码: {e.status_code}")
        print(f"请求ID: {e.request_id}")
        print(f"错误码: {e.error_code}")
        print(f"错误信息: {e.error_msg}")
        return None


if __name__ == "__main__":
    query_ims_images_list(region="cn-north-4")
#     create_system_disk_image(
#     region="cn-east-5",
#     name="ims-test2",
#     instance_id="b12ee514-4019-41ee-8f61-0139e096cd3a"
# )
