# Copyright 2014 Baidu, Inc.
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
This module provide base class for BCE service clients.
"""
from __future__ import absolute_import
import copy
from builtins import str, bytes

import baiducloud_python_sdk_core
from baiducloud_python_sdk_core import bce_client_configuration
from baiducloud_python_sdk_core.exception import BceClientError
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import bce_http_client

class BceBaseClient(object):
    """
    TODO: add docstring
    """
    def __init__(self, config, region_supported=True):
        """
        :param config: the client configuration. The constructor makes a copy of this parameter so
                        that it is safe to change the configuration after then.
        :type config: BceClientConfiguration

        :param region_supported: true if this client supports region.
        :type region_supported: bool
        """
        self.service_id = self._compute_service_id()
        self.region_supported = region_supported
        # just for debug
        self.config = copy.deepcopy(bce_client_configuration.DEFAULT_CONFIG)
        if config is not None:
            self.config.merge_non_none_values(config)
        if self.config.endpoint is None:
            self.config.endpoint = self._compute_endpoint()


    def _compute_service_id(self):
        return self.__module__.split('.')[2]

    def _compute_endpoint(self):
        if self.config.endpoint:
            return self.config.endpoint
        if self.region_supported:
            return b'%s://%s.%s.%s' % (
                self.config.protocol,
                self.service_id,
                self.config.region,
                baiducloud_python_sdk_core.DEFAULT_SERVICE_DOMAIN)
        else:
            return b'%s://%s.%s' % (
                self.config.protocol,
                self.service_id,
                baiducloud_python_sdk_core.DEFAULT_SERVICE_DOMAIN)

    def _send_request(self, http_method, path, headers=None, params=None, body=None, model=None):
        return bce_http_client.send_request(
            self.config, bce_v1_signer.sign, [handler.parse_error, handler.parse_json],
            http_method, path, body, headers, params, model=model)

    def _get_config(self, apiDict, apiName):
        return copy.deepcopy(apiDict[apiName])

    def _add_header(self, apiConfig, key, value):
        self._set_if_nonnull(apiConfig["headers"], key, value)

    def _add_query(self, apiConfig, key, value):
        # key-only query parameter's value is "" and can satisfy non-null
        self._set_if_nonnull(apiConfig["queries"], key, value)

    def _add_path_param(self, apiConfig, key, value):
        if value is None:
            raise BceClientError(b"Path param can't be none.")
        apiConfig["path"] = apiConfig["path"].replace("[" + key + "]", value)

    def _set_if_nonnull(self, params, param_name=None, value=None):
        if value is not None:
            params[param_name] = value

    def _extract_host_annotation_value(self, bce_request):
        if bce_request is None:
            return None
        try:
            from baiducloud_python_sdk_core.annotation import is_host_field
            # 获取类的所有属性（包括property）
            for attr_name in dir(bce_request):
                # 跳过私有属性和内置属性
                if attr_name.startswith('_'):
                    continue
                try:
                    # 获取类属性（property 对象）
                    class_attr = getattr(type(bce_request), attr_name, None)
                    # 检查是否被 @host 装饰
                    if class_attr is not None and is_host_field(class_attr):
                        # 获取实例属性的值
                        value = getattr(bce_request, attr_name, None)
                        if value is not None and isinstance(value, str):
                            return value
                    # 也检查 property 的 fget
                    if isinstance(class_attr, property) and class_attr.fget is not None:
                        if is_host_field(class_attr.fget):
                            value = getattr(bce_request, attr_name, None)
                            if value is not None and isinstance(value, str):
                                return value
                except (AttributeError, TypeError):
                    # 如果访问某个属性失败，跳过
                    continue
        except ImportError:
            # 如果 annotation 模块不存在，返回 None
            pass
        except Exception:
            # 其他异常也返回 None，不影响正常流程
            pass

        return None

    def _build_host_endpoint(self, original_endpoint, host_prefix):
        if not original_endpoint or not host_prefix:
            return original_endpoint
        try:
            # 转换为字符串进行处理
            if isinstance(original_endpoint, bytes):
                endpoint_str = original_endpoint.decode('utf-8')
            else:
                endpoint_str = original_endpoint
            # 检查是否包含协议
            if '://' in endpoint_str:
                protocol, host = endpoint_str.split('://', 1)
                result = protocol + '://' + host_prefix + '.' + host
            else:
                result = host_prefix + '.' + endpoint_str
            # 返回与输入相同的类型
            if isinstance(original_endpoint, bytes):
                return result.encode('utf-8')
            return result
        except Exception:
            # 如果构建失败，返回原始 endpoint
            return original_endpoint
    
    def _create_request_with_host(self, bce_request, config=None):
        # 1. 合并配置
        merged_config = copy.deepcopy(self.config)
        if config is not None:
            merged_config.merge_non_none_values(config)
        
        # 2. 提取 @host 注解值
        host_prefix = self._extract_host_annotation_value(bce_request)
        
        # 3. 如果存在 @host 注解，修改 endpoint
        if host_prefix:
            merged_config.endpoint = self._build_host_endpoint(
                merged_config.endpoint, host_prefix)
        
        return merged_config
