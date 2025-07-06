import json
import os
from pathlib import Path
from typing import Union, get_args

import yaml
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions.exceptions import HostUnreachableException
from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.sdk_response import FutureSdkResponse
from huaweicloudsdkcore.utils import http_utils

from .model import MCPConfig, TransportType
from .variable import (
    HUAWEI_ACCESS_KEY,
    HUAWEI_SECRET_KEY,
    MCP_SERVER_MODE,
    MCP_SERVER_PORT,
)


class CustomClient(Client):
    def build_future_request(
        self,
        method,
        resource_path,
        path_params,
        query_params,
        header_params,
        request_body,
        post_params,
        cname,
        response_type,
        collection_formats,
        progress_callback,
    ):
        url_parse_result = self._url_parse(cname)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc

        header_params = self._parse_header_params(collection_formats, header_params)
        resource_path = self._parse_path_params(
            collection_formats,
            path_params,
            resource_path,
            self._credentials.get_update_path_params(),
        )
        query_params = self._parse_query_params(collection_formats, query_params)
        post_params = self._parse_post_params(collection_formats, post_params)

        if (
            self._config.ignore_content_type_for_get_request
            and method == "GET"
            and not request_body
        ):
            content_type = header_params.pop(self._CONTENT_TYPE, None)
        else:
            content_type = header_params.setdefault(
                self._CONTENT_TYPE, self._APPLICATION_JSON
            )

        if content_type == self._MULTIPART_FORM_DATA:
            body = self._parse_form_data_body(request_body)
            header_params[self._CONTENT_TYPE] = body.content_type
        elif content_type == self._APPLICATION_X_WWW_FORM_URLENCODED:
            body = self._parse_form_urlencoded_body(request_body)
        elif content_type == self._APPLICATION_XML:
            body = self._parse_xml_body(request_body)
        elif content_type == self._APPLICATION_BSON:
            body = self._parse_bson_body(request_body)
        elif content_type == self._APPLICATION_OCTET_STREAM:
            content_length = header_params.get("content-length")
            body = self._parse_stream_body(
                request_body, progress_callback, content_length
            )
        else:
            body = self._parse_body(request_body, post_params)

        sdk_request = SdkRequest(
            method=method,
            schema=schema,
            host=host,
            resource_path=resource_path,
            query_params=query_params,
            header_params=header_params,
            body=body,
            stream=False,
            signing_algorithm=self._config.signing_algorithm,
        )
        return self._credentials.process_auth_request(sdk_request, self._http_client)

    def do_http_request(
        self,
        method,
        resource_path,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        cname=None,
        response_type=None,
        response_headers=None,
        collection_formats=None,
        request_type=None,
        async_request=False,
        progress_callback=None,
    ):
        if async_request:
            future_request = self.build_future_request(
                method,
                resource_path,
                path_params,
                query_params,
                header_params,
                body,
                post_params,
                cname,
                response_type,
                collection_formats,
                progress_callback,
            )
            future_response = self._http_client.executor.submit(
                self._do_http_request_async,
                future_request,
                response_type,
                response_headers,
                progress_callback,
            )
            return FutureSdkResponse(future_response, self._logger)

        while True:
            try:
                request = self.build_future_request(
                    method,
                    resource_path,
                    path_params,
                    query_params,
                    header_params,
                    body,
                    post_params,
                    cname,
                    response_type,
                    collection_formats,
                    progress_callback,
                ).result()
                response = self._do_http_request_sync(request)
                break
            except HostUnreachableException as e:
                with self._mutex:
                    if self._endpoint_index < len(self._endpoints) - 1:
                        self._endpoint_index += 1
                    else:
                        self._endpoint_index = 0
                        raise e

        return response


def create_api_client(ak, sk, product_short, region="cn-north-4"):
    endpoint = f"https://{product_short}.{region}.myhuaweicloud.com"
    credentials = BasicCredentials(ak, sk)

    return (
        ClientBuilder(CustomClient)
        .with_credentials(credentials)
        .with_region(Region(id=region, endpoint=endpoint))
        .build()
    )


def build_http_info(name, arguments, openapi_spec, mcp_tools):
    # 基于Path name找到调用的Tool
    invoked_tool = next((tool for tool in mcp_tools if tool.name == name), None)
    if not invoked_tool:
        raise Exception(f"MCP工具({name})未找到")
    method = openapi_spec.get("paths").get(f"/{name}").get("x-method")
    resource_path = (
        openapi_spec.get("paths").get(f"/{name}").get("x-url").replace("{endpoint}", "")
    )

    cname = None
    collection_formats = {}
    path_params = {}
    query_params = {}
    header_params = {}
    form_params = {}
    request_body = {}
    response_headers = None

    properties = invoked_tool.inputSchema.get("properties", {})
    for property_name, property_body in properties.items():
        if property_name in ["X-Auth-Token"]:
            pass
        elif (
            property_name in invoked_tool.inputSchema.get("required", [])
            and arguments.get(property_name) is None
        ):
            raise Exception(f"{property_name}为必填参数.")

        property_in = property_body.get("in")
        if property_in == "query":
            query_params[property_name] = arguments.get(property_name)
        elif property_in == "path":
            path_params[property_name] = arguments.get(property_name)
        elif property_in == "header":
            header_params[property_name] = arguments.get(property_name)
        elif property_in is None:
            request_body[property_name] = arguments.get(property_name)
    header_params["Content-Type"] = http_utils.select_header_content_type(
        ["application/json;charset=UTF-8"]
    )
    http_info = {
        "method": method,
        "resource_path": resource_path,
        "cname": cname,
        "collection_formats": collection_formats,
        "path_params": path_params,
        "query_params": query_params,
        "header_params": header_params,
        "post_params": form_params,
        "body": request_body,
        "response_headers": response_headers,
    }

    return http_info


def load_openapi(config_path):
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            result = json.load(file)
            return result
    except FileNotFoundError:
        raise FileNotFoundError(f"OpenAPI文件未找到: {config_path}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"无效的JSON格式: {str(e)}", e.doc, e.pos)
    except IOError as e:
        raise IOError(f"加载OpenAPI文件失败: {str(e)}")


def load_config(config_path: Union[str, Path]) -> MCPConfig:
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config_dict = yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"YAML 文件未找到: {config_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"无效的 YAML 格式: {e}")

    # 创建主配置对象
    try:
        cfg = MCPConfig(
            service_code=config_dict.get("service_code", ""),
            transport=config_dict.get("transport", ""),
            sse_port=config_dict.get("sse_port", 8888),
            ak=config_dict.get("ak", ""),
            sk=config_dict.get("sk", ""),
        )

        env_mapping = [
            (HUAWEI_ACCESS_KEY, "ak", None, None),
            (HUAWEI_SECRET_KEY, "sk", None, None),
            (MCP_SERVER_MODE, "transport", None, get_args(TransportType)),
            (MCP_SERVER_PORT, "sse_port", int, None),
        ]

        for env_var, attr_name, converter, allowed_values in env_mapping:
            env_value_str = os.environ.get(env_var)
            if env_value_str is not None and env_value_str != "":
                # 转换类型
                value_to_set = converter(env_value_str) if converter else env_value_str
                # 验证 Literal 类型的值
                if allowed_values is not None and value_to_set not in allowed_values:
                    raise ValueError(
                        f"无效值 '{value_to_set}'. 有效值清单: {allowed_values}"
                    )
                setattr(cfg, attr_name, value_to_set)
        # 参数校验
        cfg.check()
        return cfg
    except (ValueError, TypeError) as e:
        raise ValueError(f"读取配置文件时发生错误 {e}")


def filter_parameters(params_dict):
    filtered_dict = {}
    for key, value in params_dict.items():
        # 检查值是否不是 None 并且不是空列表
        if value is not None and not (isinstance(value, list) and not value):
            filtered_dict[key] = value
    return filtered_dict
