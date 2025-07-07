import re
from copy import deepcopy
from typing import Any, Dict, List, Optional, Set

from fastmcp.utilities.logging import configure_logging, get_logger
from mcp.types import Tool
from pydantic import ValidationError

# 配置日志
logger = get_logger(__name__)
configure_logging("INFO")


class SwaggerRefResolver:
    """处理 Swagger/OpenAPI 文档中的 $ref 引用解析"""

    def __init__(self, spec_dict: Dict[str, Any]):
        """初始化引用解析器"""
        self.openapi_dict = spec_dict
        self.cache = {}
        self.processing_stack = set()

    def parse(self) -> Dict[str, Any]:
        """执行引用解析，返回解析后的文档副本"""
        return self._parse_node(deepcopy(self.openapi_dict))

    def _parse_node(self, node: Any) -> Any:
        """递归解析节点中的引用"""
        if isinstance(node, list):
            return [self._parse_node(item) for item in node]

        if not isinstance(node, dict):
            return node

        if "$ref" in node:
            return self._handle_ref(node)

        return {k: self._parse_node(v) for k, v in node.items()}

    def _handle_ref(self, ref_node: Dict[str, Any]) -> Any:
        """处理 $ref 引用节点"""
        ref_uri = ref_node["$ref"]

        if not isinstance(ref_uri, str):
            logger.error(f"无效的 $ref 路径: {ref_uri}")
            return self._process_invalid_ref(ref_node)

        if ref_uri.startswith("#/"):
            return self._parse_internal_ref(ref_uri, ref_node)

        logger.error(f"不支持的外部引用: {ref_uri}")
        return self._process_invalid_ref(ref_node)

    def _process_invalid_ref(self, node: Dict[str, Any]) -> Dict[str, Any]:
        """处理无效引用，返回不含 $ref 的节点"""
        return {k: self._parse_node(v) for k, v in node.items() if k != "$ref"}

    def _parse_internal_ref(self, ref_uri: str, ref_node: Dict[str, Any]) -> Any:
        """解析内部引用（#/ 开头的路径）"""
        if ref_uri in self.cache:
            return deepcopy(self.cache[ref_uri])

        if ref_uri in self.processing_stack:
            logger.error(f"检测到循环引用: {ref_uri}")
            return {"$ref_cycle_detected": ref_uri}

        self.processing_stack.add(ref_uri)

        try:
            ref_object = self._find_ref_object(ref_uri)
            resolved_ref = self._parse_node(deepcopy(ref_object))

            # 合并原始节点中的其他属性（除 $ref 外）
            if isinstance(resolved_ref, dict):
                resolved_ref.update(
                    {k: self._parse_node(v) for k, v in ref_node.items() if k != "$ref"}
                )

            self.cache[ref_uri] = resolved_ref
            return deepcopy(resolved_ref)

        except (KeyError, IndexError, ValueError) as e:
            logger.error(f"引用路径解析失败: {ref_uri}, 错误: {e}")
            return {"$ref_resolve_error": str(e)}

        finally:
            self.processing_stack.remove(ref_uri)

    def _find_ref_object(self, ref_uri: str) -> Any:
        """查找引用路径指向的目标对象"""
        parts = ref_uri[2:].split("/")
        ref_object = self.openapi_dict

        for part in parts:
            part = part.replace("~1", "/").replace("~0", "~")

            if isinstance(ref_object, list):
                if not part.isdigit():
                    raise KeyError(f"列表索引不是数字: {part}")
                ref_object = ref_object[int(part)]
            elif isinstance(ref_object, dict):
                if part not in ref_object:
                    raise KeyError(f"字典键不存在: {part}")
                ref_object = ref_object[part]
            else:
                raise TypeError(f"无法索引类型: {type(ref_object).__name__}")

        return ref_object


class OpenAPIToToolsConverter:
    """将 OpenAPI 规范转换为 MCP Tools 的转换器"""

    OPENAPI_METHODS = {
        "get",
        "put",
        "post",
        "delete",
        "options",
        "head",
        "patch",
        "trace",
    }

    def __init__(self, openapi_dict: Dict[str, Any]):
        """初始化转换器"""
        self.openapi_dict = openapi_dict
        self.resolved_openapi = None
        self.tools: List[Tool] = []

    def convert(self) -> List[Tool]:
        """执行转换流程"""
        self._resolve_references()
        self._extract_tools()
        return self.tools

    def _resolve_references(self) -> None:
        """解析 OpenAPI 规范中的所有 $ref 引用"""
        resolver = SwaggerRefResolver(self.openapi_dict)
        self.resolved_openapi = resolver.parse()

    def _extract_tools(self) -> None:
        """从解析后的规范中提取工具"""
        paths = self.resolved_openapi.get("paths", {})
        if not isinstance(paths, dict):
            logger.error("缺少有效的 'paths' 字段")
            return

        for path, path_values in paths.items():
            logger.debug(f"开始解析{path}...................。")
            if not isinstance(path_values, dict):
                continue

            path_parameters = self._extract_path_parameters(path_values)

            for method, operation in path_values.items():
                if method not in self.OPENAPI_METHODS or not isinstance(
                    operation, dict
                ):
                    continue

                tool = self._create_tool(method, path, operation, path_parameters)
                if tool:
                    self.tools.append(tool)

    @staticmethod
    def _extract_path_parameters(path_values: Dict[str, Any]) -> List[Dict[str, Any]]:
        """提取路径级别的参数"""
        parameters = path_values.get("parameters", [])
        if not isinstance(parameters, list):
            logger.error(f"路径 '{path_values}' 的 parameters 不是列表，忽略")
            return []
        return [p for p in parameters if isinstance(p, dict)]

    def _create_tool(
        self,
        method: str,
        path: str,
        operation: Dict[str, Any],
        path_parameters: List[Dict[str, Any]],
    ) -> Optional[Tool]:
        """创建单个 MCP Tool 对象"""
        try:
            tool_name = self._determine_tool_name(method, path, operation)
            tool_description = self._determine_tool_description(method, path, operation)
            tool_parameters = self._build_tool_parameters(path_parameters, operation)

            return Tool(
                name=tool_name,
                description=tool_description,
                inputSchema=tool_parameters,
            )
        except ValidationError as e:
            logger.error(f"参数验证失败: {method.upper()} {path}: {e}")
            return None
        except Exception as e:
            logger.error(f"创建工具失败: {method.upper()} {path}: {e}")
            return None

    def _determine_tool_name(
        self, method: str, path: str, operation: Dict[str, Any]
    ) -> str:
        """确定工具名称"""
        raw_name = operation.get("operationId", "")
        if not raw_name:
            cleaned_path = path.replace("/", "_").replace("{", "_").replace("}", "")
            if cleaned_path.startswith("_"):
                cleaned_path = cleaned_path[1:]
            raw_name = f"{method}_{cleaned_path}"
        return self.cleanup_name(raw_name)

    @staticmethod
    def cleanup_name(name: str) -> str:
        """清理名称以符合 MCP Tool 命名要求"""
        name = re.sub(r"^[^a-zA-Z0-9_]+|[^a-zA-Z0-9_]+$", "", name)
        name = re.sub(r"[^a-zA-Z0-9_]+", "_", name)
        if not name:
            return "unnamed_tool"

        if len(name) > 64:
            name = name[:64].rstrip("_")
            if not name:
                name = "unnamed_tool"
        if not re.match(r"^[a-zA-Z0-9_]+$", name):
            name = "unnamed_tool"
        return name

    @staticmethod
    def _determine_tool_description(
        method: str, path: str, operation: Dict[str, Any]
    ) -> str:
        """确定工具描述"""
        description = operation.get("description", "") or operation.get("summary", "")
        if not isinstance(description, str):
            description = f"API 调用: {method.upper()} {path}"
        return description

    def _build_tool_parameters(
        self, path_parameters: List[Dict[str, Any]], operation: Dict[str, Any]
    ) -> Dict[str, Any]:
        """构建工具参数模式"""
        required_parameters = set()
        parameter_properties = {}
        processed_parameters = set()

        # 处理路径和操作参数
        operation_parameters = operation.get("parameters", [])
        if not isinstance(operation_parameters, list):
            operation_parameters = []

        total_parameters = [
            p for p in (path_parameters + operation_parameters) if isinstance(p, dict)
        ]

        for param_def in reversed(total_parameters):
            param_name = param_def.get("name")
            param_in = param_def.get("in")

            if (
                not isinstance(param_name, str)
                or not isinstance(param_in, str)
                or param_name in processed_parameters
                or param_in not in ["path", "query"]
            ):
                continue

            param_schema = param_def.get("schema")
            if (
                not isinstance(param_schema, dict)
                or "$ref_cycle_detected" in param_schema
            ):
                continue

            if "description" not in param_schema and param_def.get("description"):
                param_schema["description"] = param_def.get("description")

            param_schema["in"] = param_in
            parameter_properties[param_name] = param_schema
            if param_def.get("required", False) or param_in == "path":
                required_parameters.add(param_name)

            processed_parameters.add(param_name)

        # 处理请求体
        self._process_request_body(operation, parameter_properties, required_parameters)

        return self._finalize_parameters(parameter_properties, required_parameters)

    def _process_request_body(
        self,
        operation: Dict[str, Any],
        parameter_properties: Dict[str, Any],
        required_parameters: Set[str],
    ) -> None:
        """处理请求体参数"""
        request_body = operation.get("requestBody")
        if not isinstance(request_body, dict) or "$ref_cycle_detected" in request_body:
            return

        content = request_body.get("content")
        if not isinstance(content, dict):
            return

        media_type_obj = content.get("application/json") or content.get(
            "application/x-www-form-urlencoded"
        )

        if not isinstance(media_type_obj, dict):
            return

        body_schema = media_type_obj.get("schema")
        if self._is_valid_body_schema(body_schema):
            self._process_body_properties(
                body_schema, parameter_properties, required_parameters
            )

    @staticmethod
    def _is_valid_body_schema(body_schema: Any) -> bool:
        """验证请求体 schema 是否有效"""
        return (
            isinstance(body_schema, dict)
            and body_schema.get("type") == "object"
            and isinstance(body_schema.get("properties"), dict)
            and "$ref_cycle_detected" not in body_schema
        )

    @staticmethod
    def _process_body_properties(
        body_schema: Dict[str, Any],
        parameter_properties: Dict[str, Any],
        required_parameters: Set[str],
    ) -> None:
        """处理请求体中的属性"""
        for prop_name, prop_schema in body_schema["properties"].items():
            if (
                not isinstance(prop_name, str)
                or not isinstance(prop_schema, dict)
                or "$ref_cycle_detected" in prop_schema
            ):
                continue

            if prop_name in parameter_properties:
                logger.warning(f"属性名称冲突 '{prop_name}'，请求体属性将覆盖")

            parameter_properties[prop_name] = prop_schema

        # 合并必需字段
        body_required = body_schema.get("required", [])
        if isinstance(body_required, list):
            required_parameters.update(
                req for req in body_required if isinstance(req, str)
            )

    @staticmethod
    def _finalize_parameters(
        parameter_properties: Dict[str, Any], required_parameters: Set[str]
    ) -> Dict[str, Any]:
        """完成参数模式的最终处理，返回新的参数对象"""
        tool_parameters = {"type": "object", "properties": {}}

        if parameter_properties:
            tool_parameters["properties"] = parameter_properties.copy()  # 创建副本

        valid_required = [
            req for req in sorted(required_parameters) if req in parameter_properties
        ]
        if valid_required:
            tool_parameters["required"] = valid_required

        return tool_parameters
