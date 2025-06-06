import logging
import time
from pydantic import Field
from tools.utils import get_aksk
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkdas.v3 import DasClient
from huaweicloudsdkdas.v3 import ListCloudDbaInstancesRequest
from huaweicloudsdkdas.v3 import ListHealthReportTaskRequest
from huaweicloudsdkdas.v3 import ExportTopRiskInstancesRequest
from huaweicloudsdkdas.v3.region.das_region import DasRegion
from huaweicloudsdkcore.exceptions import exceptions

logger = logging.getLogger(__name__)
tools = []


def create_client(region: str) -> DasClient:
    ak, sk = get_aksk()
    credentials = BasicCredentials(ak, sk)

    client = (
        DasClient.new_builder()
        .with_credentials(credentials)
        .with_region(DasRegion.value_of(region))
        .build()
    )

    return client


@tools.append
def list_health_report_task(
    region: str = Field(
        default="cn-south-1",
        description="购买的ecs所属区地域ID，默认是华南-广州;区域有-代表广州-cn-south-1 、华东-上海一cn-east-3",
    ),
    instance_id: str = Field(
        default="cn-south-1",
        description="实例ID。标识实例的唯一标识。取值范围：只能由英文字母、数字组成，且长度为32个字符。",
    ),
    start_at: int = Field(
        description="开始时间（Unix timestamp），单位：毫秒。取值范围：[0, 2^31-1]，实际取决于查询。"
    ),
    end_at: int = Field(
        default=int(time.time() * 1000),
        description="结束时间Unix timestamp），单位：毫秒。取值范围：[0, 2^31-1]，实际取决于查询。",
    ),
    offset: int = Field(
        default=0,
        description="索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为1，limit指定为10，则只展示第2~11条数据。取值范围：[0, 5000] 默认取值：默认为0（偏移0条数据，表示从第一条数据开始查询）。",
    ),
) -> str:
    """查询实例健康诊断报告列表

    Args:
         region: 地域，例如：北京四, 上海二, 香港
         instance_id (str): 云主机实例ID，基于该实例制作镜像
         start_at: 开始时间（Unix timestamp），单位：毫秒。取值范围：[0, 2^31-1]，实际取决于查询。
         end_at: 结束时间Unix timestamp），单位：毫秒。取值范围：[0, 2^31-1]，实际取决于查询。
         offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为1，limit指定为10，则只展示第2~11条数据。取值范围：[0, 5000] 默认取值：默认为0（偏移0条数据，表示从第一条数据开始查询）。
     Return:
    """
    client = create_client(region)
    try:
        request = ListHealthReportTaskRequest(
            instance_id=instance_id, start_at=start_at, end_at=end_at, offset=offset
        )
        response = client.list_health_report_task(request)
        return response

    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
                   {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def list_cloud_dba_instances(
    region: str = Field(
        default="cn-south-1",
        description="购买的ecs所属区地域ID，默认是华南-广州;区域有-代表广州-cn-south-1 、华东-上海一cn-east-3",
    ),
    datastore_type: str = Field(
        default="mysql", description="数据库类型。mysql, oracle"
    ),
    offset: int = Field(
        default=0,
        description="索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为1，limit指定为10，则只展示第2~11条数据。取值范围：[0, 5000] 默认取值：默认为0（偏移0条数据，表示从第一条数据开始查询）。",
    ),
) -> str:
    """获取DAS云DBA实例列表

    Args:
         region: 地域，例如：北京四, 上海二, 香港
         datastore_type: 数据库类型。mysql, oracle
         offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为1，limit指定为10，则只展示第2~11条数据。取值范围：[0, 5000] 默认取值：默认为0（偏移0条数据，表示从第一条数据开始查询）。
     Return:
    """
    client = create_client(region)
    try:
        request = ListCloudDbaInstancesRequest(datastore_type, offset, None, None)
        response = client.list_cloud_dba_instances(request)
        return response

    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
                   {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


@tools.append
def export_top_risk_instances(
    region: str = Field(
        default="cn-south-1",
        description="购买的ecs所属区地域ID，默认是华南-广州;区域有-代表广州-cn-south-1 、华东-上海一cn-east-3",
    ),
    start_at: int = Field(
        description="开始时间(Unix timestamp),单位:毫秒。1749089575000，时间控制在24小时内, start_at与end_at时间范围需要大于10分钟 非空"
    ),
    end_at: int = Field(
        default=int(time.time() * 1000),
        description="结束时间(Unix timestamp),单位:毫秒。1749089575000，时间控制在24小时内, start_at与end_at时间范围需要大于10分钟，非空",
    ),
    datastore_type: str = Field(
        default="mysql", description="数据库类型。mysql, oracle"
    ),
) -> str:
    """导出TOP风险实例列表

    Args:
         region: 地域，例如：北京四, 上海二, 香港
         start_at: 开始时间(Unix timestamp),单位:毫秒
         end_at: 结束时间(Unix timestamp),单位:毫秒。
         datastore_type: 数据库类型。mysql, oracle
     Return:
          top_risk_info
              instance_id string	实例id。
              instance_name string 实例名称。
              node_id string	节点ID。
              metric_names Array of strings	指标名称。
              metric_values Array of double	指标值,单位%。
          total_count
    """
    if not is_within_24h(start_at, end_at):
        return "导出时间请控制在24小时内"

    client = create_client(region)
    try:
        request = ExportTopRiskInstancesRequest(
            start_at=start_at, end_at=end_at, datastore_type=datastore_type
        )
        response = client.export_top_risk_instances(request)
        return response

    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
                   {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg


def is_within_24h(start_at, end_at, unit="milliseconds"):
    """
    判断两个时间戳是否在24小时内

    参数:
        start_at: 开始时间戳
        end_at: 结束时间戳
        unit: 时间戳单位，'seconds'（默认）或'milliseconds'
    """
    # 转换为秒
    if unit == "milliseconds":
        start_at = start_at / 1000
        end_at = end_at / 1000

    # 计算时间差（秒）
    diff_seconds = end_at - start_at
    return 0 <= diff_seconds <= 86400  # 86400秒 = 24小时
