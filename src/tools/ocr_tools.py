# coding: utf-8

import logging
from tools.utils import get_aksk
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkocr.v1.region.ocr_region import OcrRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkocr.v1 import OcrClient, RecognizeGeneralTextRequest, GeneralTextRequestBody
import base64
from pathlib import Path


logger = logging.getLogger(__name__)


tools = []


def get_region(region_name: str) -> str:
    region_list = {
    "北京一":"cn-north-1",
    "北京四":"cn-north-4",
    "广州":"cn-south-1",
    "上海一":"cn-east-3",
    "曼谷":"ap-southeast-2",
    "圣地亚哥":"la-south-2",
    "墨西哥城二":"la-north-2",
    "贵阳一":"cn-southwest-2",
    "香港":"ap-southeast-1",
    "新加坡":"ap-southeast-3",
    "约翰内斯堡":"af-south-1"}

    if region_name in region_list:
        return region_list[region_name]

    return None


def image_to_base64(file_path):
    with open(file_path, 'rb') as image_file:
        encoded_bytes = base64.b64encode(image_file.read())
    return encoded_bytes.decode('utf-8')


@tools.append
def recognize_general_text(region_name: str, image_name: str) -> str:
    """通用文字识别, 识别图片上的文字信息，以JSON格式返回识别的文字和坐标。
        支持扫描文件、电子文档、书籍、票据和表单等多种场景的文字识别。      

    Args:
        region_name: 地域，例如：北京四, 上海二, 香港
        image_name: 识别图片名称，支持本地图片和网络图片。网络图片名称以"http"或"ftp"开始，其他为本地图片
    """

    ak, sk = get_aksk()
    credentials = BasicCredentials(ak, sk)

    region = get_region(region_name)
    if region is None:
        return "无效地域，请确认地域。"

    client = OcrClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(OcrRegion.value_of(region)) \
        .build()

    try:
        request = RecognizeGeneralTextRequest()
        if image_name.lower().startswith("http:") or image_name.lower().startswith("ftp:"):
            request.body = GeneralTextRequestBody(
                quick_mode=False,
                detect_direction=False,
                url=image_name
            )
        else:
            if not Path.exists(image_name):
                return "图像文件不存在，请重新输入文件。"
            
            request.body = GeneralTextRequestBody(
                quick_mode=False,
                detect_direction=False,
                image=image_to_base64(image_name)
            )
        response = client.recognize_general_text(request)
        return getattr(response, 'result')   
    except exceptions.ClientRequestException as e:
        msg = f"操作失败，{f'状态码：{e.status_code}', f'请求信息：{e.request_id}'}, \
            {f'错误码：{e.error_code}', f'错误信息：{e.error_msg}'}"
        logger.error(msg)
        return msg
