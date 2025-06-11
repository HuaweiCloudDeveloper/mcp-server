# coding: utf-8
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkecs.v2 import EcsClient
from huaweicloudsdkecs.v2 import (
    CreatePostPaidServersRequest,
    CreatePostPaidServersRequestBody,
)
from huaweicloudsdkecs.v2 import PostPaidServerRootVolume

# from huaweicloudsdkecs.v2 import PostPaidServerDataVolume
from huaweicloudsdkecs.v2 import (
    PostPaidServerNic,
    PostPaidServerPublicip,
    PostPaidServerEip,
    PostPaidServerEipBandwidth,
)
from huaweicloudsdkecs.v2 import PostPaidServerSecurityGroup, PostPaidServer
from huaweicloudsdkecs.v2 import ListCloudServersRequest
from huaweicloudsdkecs.v2 import (
    DeleteServersRequest,
    DeleteServersRequestBody,
    ServerId,
)
from typing import Optional
from pydantic import BaseModel, Field
from tools.utils import get_aksk
import logging

# 导入本地 的环境变量
from dotenv import load_dotenv

load_dotenv()  # 这将默认从当前目录下的 .env 文件加载变量
# 配置日志
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
tools = []


# 配置模型
class ECSInstanceConfig(BaseModel):
    region: str = Field(
        "cn-south-1",
        description="购买的ecs所属区地域ID，默认是华南-广州;区域有-代表广州-cn-south-1 、华东-上海一cn-east-3",
    )
    flavor_ref: str = Field(
        "kc1.large.2", description="云服务器规格ID,默认的cpu架构 鲲鹏计算"
    )
    image_ref: str = Field(
        "1d9bdfd3-1ea4-4c21-a930-5638966f7de3",
        description="镜像ID，默认id是 Ubuntu22.04",
    )
    root_volume_type: str = Field(
        "SAS", description="系统盘类型，如 SSD、SAS、SATA、co-p1"
    )
    root_volume_size: int = Field(40, description="系统盘大小，单位GB")
    data_volume_type: Optional[str] = Field("SSD", description="数据盘类型")
    data_volume_size: Optional[int] = Field(100, description="数据盘大小，单位GB")
    adminPass: str = Field(
        "Huawei123!@",
        description="登录密码，密码复杂度要求:长度为8-26位。密码至少必须包含大写字母、小写字母、数字和特殊字符(!@$%^-_=+[{}]:,./?)中的三种。密码不能包含用户名或用户名的逆序。",
    )
    vpc_id: str = Field(
        "a4d2ac4d-7944-407d-9309-890f4f6d099c",
        description="VPC ID，默认值是华南-广州的",
    )
    subnet_id: str = Field(
        "f70800df-5329-41c4-90ff-2a45cfb1f101",
        description="子网ID，默认值是华南-广州的",
    )
    eip_iptype: str = Field("5_bgp", description="弹性IP类型")
    bandwidth_size: int = Field(5, description="弹性IP带宽大小，单位Mbit/s")
    bandwidth_iptype: str = Field("PER", description="带宽共享类型 PER=独享 WHOLE=共享")
    delete_on_termination: bool = Field(True, description="实例删除时是否自动释放EIP")
    SecurityGroup_id: str = Field(
        "4c78e26d-11cc-424e-ae5b-91c3c0a83121", description="安全组ID"
    )
    instance_name: str = Field("ai_mcp_build", description="ECS实例名称")
    count: int = Field(1, description="创建ECS实例的数量")


# 创建ecs客户端
def get_ecs_client(region="cn-south-1"):
    ak, sk = get_aksk()  # 从环境变量中获取AK和SK
    print(f"AK: {ak}, SK: {sk}")
    credentials = BasicCredentials(ak, sk)  # 创建凭证对象
    return (
        EcsClient.new_builder()
        .with_credentials(credentials)
        .with_region(EcsRegion.value_of(region))
        .build()
    )


# 创建按需计费的ECS实例
@tools.append
def create_post_paid_ecs_instance(config: ECSInstanceConfig):
    """
    创建按需计费的ECS实例
     :param config: ECSInstanceConfig对象，包含实例配置参数
     :return: 创建实例的响应信息
    """
    try:
        # 获取客户端连接
        client = get_ecs_client(region=config.region)
        # 创建请求
        request = CreatePostPaidServersRequest()
        # 云服务器系统盘相关配置。
        rootVolumeServer = PostPaidServerRootVolume(
            volumetype=config.root_volume_type, size=config.root_volume_size
        )
        # 云服务器数据盘
        #     listDataVolumesServer = [
        #     PostPaidServerDataVolume(
        #         volumetype=config.data_volume_type,
        #         size=config.data_volume_size
        #     )
        # ]

        # 待创建云服务器的网卡信息,网卡对应的子网(subnet)必须属于vpcid对应的VPC。当前单个云服务器支持最多挂载12张网卡
        listNicsServer = [PostPaidServerNic(subnet_id=config.subnet_id)]
        # 配置云服务器的弹性IP信息,弹性IP有三种配置方式。不使用(无该字段)自动分配,需要指定新创建弹性IP的信息,使用已有,需要指定已创建弹性IP的信息
        publicipServer = PostPaidServerPublicip(
            # 自动分配IP的配置参数
            eip=PostPaidServerEip(
                iptype=config.eip_iptype,
                bandwidth=PostPaidServerEipBandwidth(
                    size=config.bandwidth_size,  # 默认带宽5M
                    sharetype=config.bandwidth_iptype,  # 共享类型枚举:PER,表示独享。WHOLE,表示共享。
                ),
            ),
            delete_on_termination=config.delete_on_termination,
        )
        # 安全组
        listSecurityGroupsServer = [
            PostPaidServerSecurityGroup(id=config.SecurityGroup_id)
        ]
        # 配置服务器参数
        server_body = PostPaidServer(
            # 1、云服务器系统规格
            flavor_ref=config.flavor_ref,
            # 2、系统镜像id
            image_ref=config.image_ref,
            # 3、云服务系统盘配置
            root_volume=rootVolumeServer,
            # data_volumes=listDataVolumesServer, # 4、数据盘盘
            # 5、云服务网卡信息子网 和vpc
            vpcid=config.vpc_id,  # vpcid
            nics=listNicsServer,  # 云服务网卡信息
            # 6、安全组
            security_groups=listSecurityGroupsServer,
            # 7、公网带宽
            publicip=publicipServer,  # 配置公网
            # 8、云服务器管理
            is_auto_rename=True,  # 当批量创建弹性云服务器时,云服务器名称是否允许重名,当count大于1的时候该参数生效。默认为True。
            name=config.instance_name,  # ecs 云服务名称
            # 9、密码复杂度要求:长度为8-26位。密码至少必须包含大写字母、小写字母、数字和特殊字符(!@$%^-_=+[{}]:,./?)中的三种。密码不能包含用户名或用户名的逆序。
            admin_pass=config.adminPass,  # 设置管理员密码
            # 10、创建云服务器的数量
            count=config.count,  # 购买
        )

        request.body = CreatePostPaidServersRequestBody(server=server_body)

        response = client.create_post_paid_servers(request)
        logger.info("Instance creation request sent successfully")
        return response

    except exceptions.ClientRequestException as e:
        logger.error(f"Failed to create instance: {e.error_msg}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise


# 删除ECS实例
@tools.append
def delete_ecs_instance(instance_id, region="cn-south-1"):
    """
    删除ECS实例
    :param instance_id: 删除ecs实例的id
    :return: 返回删除成功或失败
    """
    try:
        # 获取客户端连接
        client = get_ecs_client(region=region)

        request = DeleteServersRequest()
        listServersbody = [ServerId(id=instance_id)]

        request.body = DeleteServersRequestBody(
            servers=listServersbody,
            delete_volume=True,  # 删除对应的数据盘
            delete_publicip=True,  # 删除绑定的弹性ip
        )
        response = client.delete_servers(request)
        logger.info("Instance delete request sent successfully")
        return response

    except exceptions.ClientRequestException as e:
        logger.error(f"Failed to delete instance: {e.error_msg}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise


# 查询云服务器列表
@tools.append
def select_ecs_instance(region="cn-south-1", ecs_id=None, ecs_name=None):
    """
    Query ECS instances based on filters (ID, name, or both)

    Args:
        region (str): Region to query (default: cn-south-1)
        ecs_id (str, optional): Specific ECS instance ID to filter
        ecs_name (str, optional): ECS instance name to filter (supports fuzzy matching)

    Returns:
        List of matching ECS instances

    Raises:
        ClientRequestException: For Huawei Cloud API errors
        Exception: For other unexpected errors
    """
    try:
        client = get_ecs_client(
            region=region
        )  # Fixed typo in parameter name (regin -> region)
        request = ListCloudServersRequest()

        # Only set filters if parameters are provided
        if ecs_id is not None:
            request.id = ecs_id
        if ecs_name is not None:
            request.name = ecs_name
        response = client.list_cloud_servers(request)
        logger.info(f"Instance query successfully--{response}")
        return response

    except exceptions.ClientRequestException as e:
        logger.error(
            f"Failed to query instances. Error: {e.error_code} - {e.error_msg}"
        )
        raise
    except Exception as e:
        logger.error(f"Unexpected error during instance query: {str(e)}")
        raise


if __name__ == "__main__":
    # 实例配置
    instance_config = ECSInstanceConfig(
        region="cn-north-4",
        flavor_ref="kc1.large.2",
        image_ref="a5fc7477-70a1-4c67-a972-c0fbbe5f310e",
        # root_volume_type="SSD",
        # root_volume_size=40,
        # data_volume_type="SSD",
        # data_volume_size=50,
        # adminPass="luke@158",
        instance_name="mcp-test",
        SecurityGroup_id="b2e3d775-a48f-408f-9d0f-d0a4f751112b",
        vpc_id="cd18f070-7184-49c7-a48b-a257a66aa339",
        subnet_id="6f1d3bd8-a6b4-4acc-9685-cbc56e65bf1c",
    )

    # create_post_paid_ecs_instance(instance_config)

    # select_ecs_instance(region="cn-south-1")
    # delete_ecs_instance(instance_id="3be6f85b-4a38-44ee-add7-037da88ca73a",region="cn-north-4")
