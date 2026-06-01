"""
LLMService information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_apm.models.tag import Tag

from baiducloud_python_sdk_apm.models.metric_value import MetricValue

from baiducloud_python_sdk_apm.models.metric_value import MetricValue

from baiducloud_python_sdk_apm.models.metric_value import MetricValue

from baiducloud_python_sdk_apm.models.metric_value import MetricValue

from baiducloud_python_sdk_apm.models.metric_value import MetricValue


class LLMService(AbstractModel):
    """
    LLMService
    """

    def __init__(
        self,
        service_name=None,
        service_display_name=None,
        service_id=None,
        tags=None,
        llm_requests=None,
        llm_requests_per_second=None,
        llm_errors=None,
        llm_duration_seconds=None,
        llm_tokens=None,
    ):
        """
        Initialize LLMService instance.

        :param service_name: 服务名称
        :type service_name: str (optional)

        :param service_display_name: 服务显示名
        :type service_display_name: str (optional)

        :param service_id: 服务ID
        :type service_id: str (optional)

        :param tags: 标签列表
        :type tags: List[Tag] (optional)

        :param llm_requests: llm_requests attribute
        :type llm_requests: MetricValue (optional)

        :param llm_requests_per_second: llm_requests_per_second attribute
        :type llm_requests_per_second: MetricValue (optional)

        :param llm_errors: llm_errors attribute
        :type llm_errors: MetricValue (optional)

        :param llm_duration_seconds: llm_duration_seconds attribute
        :type llm_duration_seconds: MetricValue (optional)

        :param llm_tokens: llm_tokens attribute
        :type llm_tokens: MetricValue (optional)
        """
        super().__init__()
        self.service_name = service_name
        self.service_display_name = service_display_name
        self.service_id = service_id
        self.tags = tags
        self.llm_requests = llm_requests
        self.llm_requests_per_second = llm_requests_per_second
        self.llm_errors = llm_errors
        self.llm_duration_seconds = llm_duration_seconds
        self.llm_tokens = llm_tokens

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_display_name is not None:
            result['serviceDisplayName'] = self.service_display_name
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.llm_requests is not None:
            result['llmRequests'] = self.llm_requests.to_dict()
        if self.llm_requests_per_second is not None:
            result['llmRequestsPerSecond'] = self.llm_requests_per_second.to_dict()
        if self.llm_errors is not None:
            result['llmErrors'] = self.llm_errors.to_dict()
        if self.llm_duration_seconds is not None:
            result['llmDurationSeconds'] = self.llm_duration_seconds.to_dict()
        if self.llm_tokens is not None:
            result['llmTokens'] = self.llm_tokens.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LLMService

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceDisplayName') is not None:
            self.service_display_name = m.get('serviceDisplayName')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('llmRequests') is not None:
            self.llm_requests = MetricValue().from_dict(m.get('llmRequests'))
        if m.get('llmRequestsPerSecond') is not None:
            self.llm_requests_per_second = MetricValue().from_dict(m.get('llmRequestsPerSecond'))
        if m.get('llmErrors') is not None:
            self.llm_errors = MetricValue().from_dict(m.get('llmErrors'))
        if m.get('llmDurationSeconds') is not None:
            self.llm_duration_seconds = MetricValue().from_dict(m.get('llmDurationSeconds'))
        if m.get('llmTokens') is not None:
            self.llm_tokens = MetricValue().from_dict(m.get('llmTokens'))
        return self
