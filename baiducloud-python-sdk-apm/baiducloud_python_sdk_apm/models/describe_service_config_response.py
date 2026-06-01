"""
Request entity for DescribeServiceConfigResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_apm.models.sample_config import SampleConfig
from baiducloud_python_sdk_apm.models.logging_config import LoggingConfig
from baiducloud_python_sdk_apm.models.service_request_config import ServiceRequestConfig
from baiducloud_python_sdk_apm.models.service_topo_config import ServiceTopoConfig
from baiducloud_python_sdk_apm.models.mllm_resource_dump_config import MllmResourceDumpConfig


class DescribeServiceConfigResponse(BceResponse):
    """
    DescribeServiceConfigResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        language=None,
        include_llm=None,
        service_display_name=None,
        sample_config=None,
        logging_config=None,
        request_config=None,
        topo_config=None,
        mllm_resource_dump_config=None,
    ):
        """
        Initialize DescribeServiceConfigResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 状态码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param language: 语言
        :type language: str (optional)

        :param include_llm: 是否是LLM应用
        :type include_llm: bool (optional)

        :param service_display_name: 服务显示名，当该字段被设置时，Console应用名称显示该字段
        :type service_display_name: str (optional)

        :param sample_config: sample_config field
        :type sample_config: SampleConfig (optional)

        :param logging_config: logging_config field
        :type logging_config: LoggingConfig (optional)

        :param request_config: request_config field
        :type request_config: ServiceRequestConfig (optional)

        :param topo_config: topo_config field
        :type topo_config: ServiceTopoConfig (optional)

        :param mllm_resource_dump_config: mllm_resource_dump_config field
        :type mllm_resource_dump_config: MllmResourceDumpConfig (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.language = language
        self.include_llm = include_llm
        self.service_display_name = service_display_name
        self.sample_config = sample_config
        self.logging_config = logging_config
        self.request_config = request_config
        self.topo_config = topo_config
        self.mllm_resource_dump_config = mllm_resource_dump_config

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.language is not None:
            result['language'] = self.language
        if self.include_llm is not None:
            result['includeLLM'] = self.include_llm
        if self.service_display_name is not None:
            result['serviceDisplayName'] = self.service_display_name
        if self.sample_config is not None:
            result['sampleConfig'] = self.sample_config.to_dict()
        if self.logging_config is not None:
            result['loggingConfig'] = self.logging_config.to_dict()
        if self.request_config is not None:
            result['requestConfig'] = self.request_config.to_dict()
        if self.topo_config is not None:
            result['topoConfig'] = self.topo_config.to_dict()
        if self.mllm_resource_dump_config is not None:
            result['mllmResourceDumpConfig'] = self.mllm_resource_dump_config.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeServiceConfigResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('includeLLM') is not None:
            self.include_llm = m.get('includeLLM')
        if m.get('serviceDisplayName') is not None:
            self.service_display_name = m.get('serviceDisplayName')
        if m.get('sampleConfig') is not None:
            self.sample_config = SampleConfig().from_dict(m.get('sampleConfig'))
        if m.get('loggingConfig') is not None:
            self.logging_config = LoggingConfig().from_dict(m.get('loggingConfig'))
        if m.get('requestConfig') is not None:
            self.request_config = ServiceRequestConfig().from_dict(m.get('requestConfig'))
        if m.get('topoConfig') is not None:
            self.topo_config = ServiceTopoConfig().from_dict(m.get('topoConfig'))
        if m.get('mllmResourceDumpConfig') is not None:
            self.mllm_resource_dump_config = MllmResourceDumpConfig().from_dict(m.get('mllmResourceDumpConfig'))
        return self
