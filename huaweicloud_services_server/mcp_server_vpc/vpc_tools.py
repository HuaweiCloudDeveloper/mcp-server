# coding: utf-8
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkvpc.v2.region.vpc_region import VpcRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkvpc.v2 import ListVpcsRequest, ListSubnetsRequest, VpcClient
from typing import Optional
from tools.utils import get_aksk
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
tools = []


# 创建vpc客户端
def get_vpc_client(region):
    ak, sk = get_aksk()  # 从环境变量中获取AK和SK
    credentials = BasicCredentials(ak, sk)  # 创建凭证对象
    return (
        VpcClient.new_builder()
        .with_credentials(credentials)
        .with_region(VpcRegion.value_of(region))
        .build()
    )


# 获取vpcid
@tools.append
def get_vpc_id(region, target_vpc_name=None):
    """
    获取VPC ID，如果target_vpc_name为None，则打印所有VPC及其ID。
    :param region: 查寻指定的区域
    :param target_vpc_name: 目标VPC名称（可选）
    return: 找到的目标VPC的ID或None
    """
    try:
        client = get_vpc_client(region)
        # 创建ListVpcsRequest请求
        request = ListVpcsRequest()
        # 发送请求，获取响应
        response = client.list_vpcs(request)

        # 解析响应，查找目标VPC ID
        for vpc in response.vpcs:
            if target_vpc_name is None:
                print(f"VPC Name: {vpc.name}, VPC ID: {vpc.id}")
            elif vpc.name == target_vpc_name:
                return vpc.id

        # 如果没有找到目标VPC且提供了target_vpc_name，则返回None
        if target_vpc_name is not None:
            print(f"未找到名为{target_vpc_name}的VPC")
            return f"未找到名为{target_vpc_name}的VPC"
    except exceptions.ClientRequestException as e:
        return {"error": str(e)}


# # 获取所有子网id 列表
@tools.append
def list_all_subnets(region):
    """
    获取所有子网信息列表。
    :param region: 查询指定的区域
    :return: 返回指定区域内的所有子网信息
    """
    try:
        client = get_vpc_client(region=region)
        request = ListSubnetsRequest()
        response = client.list_subnets(request)

        # 使用列表推导式优化子网信息提取
        subnets = [
            {
                "id": subnet.id,
                "name": subnet.name,
                "cidr": subnet.cidr,
                "vpc_id": subnet.vpc_id,
                "status": subnet.status,
            }
            for subnet in response.subnets or []
        ]

        logger.info(f"获取到的子网列表: {subnets}")
        return subnets

    except exceptions.ClientRequestException as e:
        logger.error(f"获取子网列表失败: {e.error_msg}")
        return f"获取子网列表失败: {e.error_msg}"
    except Exception as e:
        logger.error(f"未知错误: {str(e)}")
        return f"未知错误: {str(e)}"


# # 获取子网id
@tools.append
def get_subnet_id(
    region, subnet_name: Optional[str] = None, vpc_id: Optional[str] = None
) -> Optional[str]:
    """
    获取指定区域的子网ID
        :param 子网region: 查询的指定区域
        :param subnet_name: 子网名称(可选)
        :param vpc_id: VPC ID(可选)
        :return: 子网ID或None
    """
    try:
        subnets = list_all_subnets(region)
        # 如果没有过滤条件，返回第一个子网ID
        if not subnet_name and not vpc_id:
            if subnets:
                logger.info(f"返回第一个子网ID: {subnets[0]['id']}")
                return subnets[0]["id"]
            return None

        # 根据条件过滤子网
        for subnet in subnets:
            match = True
            if subnet_name and subnet["name"] != subnet_name:
                match = False
            if vpc_id and subnet["vpc_id"] != vpc_id:
                match = False
            if match:
                logger.info(f"找到匹配子网: {subnet}")
                return subnet["id"]
        logger.warning("未找到匹配的子网")
        return None

    except Exception as e:
        logger.error(f"获取子网ID出错: {str(e)}")
        return f"获取子网ID出错: {str(e)}"


if __name__ == "__main__":
    region = "cn-east-5"
    get_vpc_id(region)
#     list_all_subnets(region)
#     get_subnet_id(region)
