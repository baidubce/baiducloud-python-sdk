# Copyright 2024 Baidu, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file
# except in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the
# License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
"""
Request body utility functions for encoding and filling HTTP request payloads.
"""

import io
import json
import os

try:
    from urllib import urlencode  # Python 2
except ImportError:
    from urllib.parse import urlencode  # Python 3

from baiducloud_python_sdk_core.http.body_type import BodyType

# Content-Type constants
CONTENT_TYPE_JSON = b'application/json; charset=utf-8'
CONTENT_TYPE_FORM = b'application/x-www-form-urlencoded; charset=utf-8'
CONTENT_TYPE_OCTET_STREAM = b'application/octet-stream'
CONTENT_TYPE_MULTIPART = b'multipart/form-data'

# Default encoding
DEFAULT_ENCODING = 'utf-8'


def fill_payload(request, body_type, custom_content_type=None):
    """
    Fill request payload with body type.

    :param request: The request object to encode
    :param body_type: The BodyType enum specifying encoding format
    :param custom_content_type: Optional custom Content-Type header value
    :return: Tuple of (body_bytes, content_type, length)
    """
    if not body_type.has_content_type():
        return None, None, 0
    
    # 确定最终的 content_type
    if custom_content_type:
        final_content_type = (
            custom_content_type
            if isinstance(custom_content_type, bytes)
            else custom_content_type.encode(DEFAULT_ENCODING)
        )
    else:
        final_content_type = body_type.get_content_type().encode(DEFAULT_ENCODING)

    if body_type == BodyType.JSON:
        try:
            body_bytes = _encode_as_json(request)
            return body_bytes, final_content_type, len(body_bytes)
        except Exception as e:
            raise ValueError("Failed to encode request as JSON: {}".format(str(e)))
    
    elif body_type == BodyType.FORM:
        try:
            body_bytes = _encode_as_form(request)
            return body_bytes, final_content_type, len(body_bytes)
        except Exception as e:
            raise ValueError("Failed to encode request as form: {}".format(str(e)))
    
    elif body_type == BodyType.XML:
        raise ValueError("XML body type is not yet implemented")
    
    else:
        raise ValueError("Unsupported BodyType: {}".format(body_type))


def fill_payload_as_stream_with_body_type(
        stream, body_type, content_length=None, custom_content_type=None
):
    """
    Fill payload from a stream with specified body type.

    :param stream: The stream data source
    :param body_type: The BodyType enum specifying encoding format
    :param content_length: Optional content length (auto-calculated if None)
    :param custom_content_type: Optional custom Content-Type header value
    :return: Tuple of (stream, content_type, content_length)
    """
    if stream is None:
        raise ValueError("stream cannot be None")
    
    # 如果用户没有指定 content_length,自动计算
    if content_length is None:
        content_length = _calculate_content_length(stream)
    
    # 确定最终的 content_type
    if custom_content_type:
        final_content_type = (
            custom_content_type
            if isinstance(custom_content_type, bytes)
            else custom_content_type.encode(DEFAULT_ENCODING)
        )
    else:
        final_content_type = body_type.get_content_type().encode(DEFAULT_ENCODING)
    
    return stream, final_content_type, content_length


def fill_payload_as_byte_array_with_body_type(data, body_type):
    """
    Fill payload from byte array with specified body type.

    :param data: The byte data to send
    :param body_type: The BodyType enum specifying encoding format
    :return: Tuple of (data, content_type, length)
    """
    if data is None:
        raise ValueError("data cannot be None")

    content_type = body_type.get_content_type().encode(DEFAULT_ENCODING)
    return data, content_type, len(data)


def fill_payload_as_json(request, content_type=None):
    """
    Fill payload as JSON format.

    :param request: The request object to encode
    :param content_type: Optional custom Content-Type header value
    :return: Tuple of (body_bytes, content_type, length)
    """
    return fill_payload(request, BodyType.JSON, content_type)


def fill_payload_as_form(request, content_type=None):
    """
    Fill payload as form-urlencoded format.

    :param request: The request object to encode
    :param content_type: Optional custom Content-Type header value
    :return: Tuple of (body_bytes, content_type, length)
    """
    return fill_payload(request, BodyType.FORM, content_type)


def fill_payload_as_stream(stream, content_length=None, content_type=None):
    """
    Fill payload from a stream with octet-stream content type.

    :param stream: The stream data source
    :param content_length: Optional content length (auto-calculated if None)
    :param content_type: Optional Content-Type header value
    :return: Tuple of (stream, content_type, content_length)
    """
    if stream is None:
        raise ValueError("stream cannot be None")
    
    if content_type is None:
        content_type = CONTENT_TYPE_OCTET_STREAM
    elif isinstance(content_type, str):
        content_type = content_type.encode(DEFAULT_ENCODING)
    
    # 如果用户没有指定 content_length,自动计算
    if content_length is None:
        content_length = _calculate_content_length(stream)
    
    return stream, content_type, content_length


def fill_payload_as_byte_array(data, content_type=None):
    """
    Fill payload from a byte array with octet-stream content type.

    :param data: The byte data to send
    :param content_type: Optional Content-Type header value
    :return: Tuple of (data, content_type, length)
    """
    if data is None:
        raise ValueError("data cannot be None")
    
    if content_type is None:
        content_type = CONTENT_TYPE_OCTET_STREAM
    elif isinstance(content_type, str):
        content_type = content_type.encode(DEFAULT_ENCODING)
    
    if isinstance(data, bytearray):
        data = bytes(data)
    
    return data, content_type, len(data)


def _encode_as_json(request):
    if request is None:
        return b'{}'
    
    # 如果对象有 to_json_string 方法,使用它
    if hasattr(request, 'to_json_string'):
        json_str = request.to_json_string()
    # 如果对象有 to_dict 方法,转换为字典后序列化
    elif hasattr(request, 'to_dict'):
        json_str = json.dumps(request.to_dict(), ensure_ascii=False)
    # 否则直接序列化
    else:
        json_str = json.dumps(request, ensure_ascii=False)
    
    if isinstance(json_str, bytes):
        return json_str
    return json_str.encode(DEFAULT_ENCODING)


def _encode_as_form(request):
    if request is None:
        return b''
    
    # 1. 将对象转换为字典
    if hasattr(request, 'to_dict'):
        field_dict = request.to_dict()
    elif isinstance(request, dict):
        field_dict = request
    else:
        # 尝试将对象转换为 JSON,然后解析为字典
        json_str = json.dumps(request, ensure_ascii=False)
        field_dict = json.loads(json_str)
    
    # 2. 过滤 None 值和空字符串
    form_data = {}
    for key, value in field_dict.items():
        if value is not None and value != '':
            form_data[key] = _format_form_value(value)
    
    # 3. 编码为 URL-encoded 格式
    encoded_str = urlencode(form_data)
    
    if isinstance(encoded_str, bytes):
        return encoded_str
    return encoded_str.encode(DEFAULT_ENCODING)


def _format_form_value(value):
    if value is None:
        return ''
    
    if isinstance(value, bool):
        return 'true' if value else 'false'
    
    if isinstance(value, (int, float)):
        return str(value)
    
    if isinstance(value, str):
        return value
    
    if isinstance(value, bytes):
        return value.decode(DEFAULT_ENCODING)
    
    # 复杂类型转换为 JSON 字符串
    try:
        return json.dumps(value, ensure_ascii=False)
    except Exception:
        return str(value)


def _calculate_content_length(stream):
    # 1. bytes/bytearray - 直接获取 len() (最高效)
    if isinstance(stream, (bytes, bytearray)):
        return len(stream)
    
    # 2. io.BytesIO - 使用 seek() 获取长度 (高效)
    if isinstance(stream, io.BytesIO):
        current_pos = stream.tell()
        stream.seek(0, io.SEEK_END)
        length = stream.tell()
        stream.seek(current_pos, io.SEEK_SET)
        return length
    
    # 3. 文件对象 - 从文件 fstat() 获取大小 (高效,不读取文件内容)
    if hasattr(stream, 'fileno'):
        try:
            return os.fstat(stream.fileno()).st_size
        except (OSError, AttributeError):
            pass
    
    # 4. 文件对象 (通过 name 属性获取路径) - 使用 os.path.getsize()
    if hasattr(stream, 'name') and isinstance(stream.name, str):
        try:
            return os.path.getsize(stream.name)
        except (OSError, TypeError):
            pass
    
    # 5. io.IOBase with seek - 使用 seek() 获取长度 (高效)
    if isinstance(stream, io.IOBase) and hasattr(stream, 'seek') and hasattr(stream, 'tell'):
        try:
            current_pos = stream.tell()
            stream.seek(0, io.SEEK_END)
            length = stream.tell()
            stream.seek(current_pos, io.SEEK_SET)
            return length
        except (OSError, IOError):
            pass
    
    # 6. 其他类型的流 - 使用 Chunked Transfer Encoding (无需读入内存,无 OOM 风险)
    # 返回 None 表示使用 chunked encoding
    # 优点:
    # - 完全避免 OOM,不需要读入内存
    # - 流式传输,边读边发
    # - BCE 服务端支持 chunked encoding
    return None


# ========== Host 处理工具方法 ==========

def build_host_endpoint(endpoint, host_param):
    """
    Build host endpoint with prefix parameter.

    :param endpoint: The original endpoint URL or hostname
    :param host_param: The prefix parameter to prepend to host
    :return: Modified endpoint with host prefix
    """
    if not host_param:
        return endpoint
    
    # 记录原始类型，最后返回相同类型
    input_is_bytes = isinstance(endpoint, bytes)
    
    # 转换为 str 进行处理
    if isinstance(endpoint, bytes):
        endpoint_str = endpoint.decode('utf-8')
    else:
        endpoint_str = endpoint
    if isinstance(host_param, bytes):
        host_param_str = host_param.decode('utf-8')
    else:
        host_param_str = host_param
    
    # 检查是否包含协议
    if '://' in endpoint_str:
        protocol, host = endpoint_str.split('://', 1)
        result = protocol + '://' + host_param_str + '.' + host
    else:
        result = host_param_str + '.' + endpoint_str
    
    # 返回与输入相同的类型
    if input_is_bytes:
        return result.encode('utf-8')
    return result


# ========== 请求体填充方法（类似 Java 的 RequestBodyUtils）==========

def fill_request_as_json(headers, request):
    """
    Fill request headers with JSON body.

    :param headers: The headers dict to populate
    :param request: The request object to encode as JSON
    :return: The JSON-encoded request body
    """
    return fill_request_as_json_with_content_type(headers, request, None)


def fill_request_as_json_with_content_type(headers, request, content_type):
    """
    Fill request headers with JSON body and custom content type.

    :param headers: The headers dict to populate
    :param request: The request object to encode as JSON
    :param content_type: Optional custom Content-Type header value
    :return: The JSON-encoded request body
    """
    body, ct, length = fill_payload_as_json(request, content_type)
    headers[b'Content-Type'] = ct
    if length is not None:
        headers[b'Content-Length'] = length
    return body


def fill_request_as_form(headers, request):
    """
    使用表单格式填充请求体
    类似 Java 的 RequestBodyUtils.fillPayloadAsForm(internalRequest, request)
    """
    return fill_request_as_form_with_content_type(headers, request, None)


def fill_request_as_form_with_content_type(headers, request, content_type):
    """
    使用表单格式填充请求体（自定义 Content-Type）
    """
    body, ct, length = fill_payload_as_form(request, content_type)
    headers[b'Content-Type'] = ct
    if length is not None:
        headers[b'Content-Length'] = length
    return body


def fill_request_as_stream(headers, stream, content_type=None, content_length=None):
    """
    Fill request headers with stream body.

    :param headers: The headers dict to populate
    :param stream: The stream data to send
    :param content_type: Optional Content-Type header value
    :param content_length: Optional content length (auto-calculated if None)
    :return: The stream body
    """
    body, ct, auto_length = fill_payload_as_stream(stream, content_length, content_type)
    headers[b'Content-Type'] = ct
    # 如果用户指定了 content_length，使用用户的值
    if content_length is not None:
        headers[b'Content-Length'] = content_length
    elif auto_length is not None:
        headers[b'Content-Length'] = auto_length
    return body


def fill_request_as_byte_array(headers, data, content_type=None):
    """
    使用字节数组填充请求体
    类似 Java 的 RequestBodyUtils.fillPayloadAsByteArray(internalRequest, data, contentType)
    """
    body, ct, length = fill_payload_as_byte_array(data, content_type)
    headers[b'Content-Type'] = ct
    if length is not None:
        headers[b'Content-Length'] = length
    return body
