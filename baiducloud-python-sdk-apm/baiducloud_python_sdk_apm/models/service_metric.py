"""
ServiceMetric information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_apm.models.tag import Tag

from baiducloud_python_sdk_apm.models.metric_value import MetricValue

from baiducloud_python_sdk_apm.models.metric_value import MetricValue

from baiducloud_python_sdk_apm.models.metric_value import MetricValue

from baiducloud_python_sdk_apm.models.metric_value import MetricValue

from baiducloud_python_sdk_apm.models.metric_value import MetricValue


class ServiceMetric(AbstractModel):
    """
    ServiceMetric
    """

    def __init__(
        self,
        service_name=None,
        service_id=None,
        tags=None,
        requests=None,
        requests_per_second=None,
        errors=None,
        error_rate=None,
        duration_seconds=None,
    ):
        """
        Initialize ServiceMetric instance.

        :param service_name: 服务名称
        :type service_name: str (optional)

        :param service_id: 服务ID
        :type service_id: str (optional)

        :param tags: 标签列表
        :type tags: List[Tag] (optional)

        :param requests: requests attribute
        :type requests: MetricValue (optional)

        :param requests_per_second: requests_per_second attribute
        :type requests_per_second: MetricValue (optional)

        :param errors: errors attribute
        :type errors: MetricValue (optional)

        :param error_rate: error_rate attribute
        :type error_rate: MetricValue (optional)

        :param duration_seconds: duration_seconds attribute
        :type duration_seconds: MetricValue (optional)
        """
        super().__init__()
        self.service_name = service_name
        self.service_id = service_id
        self.tags = tags
        self.requests = requests
        self.requests_per_second = requests_per_second
        self.errors = errors
        self.error_rate = error_rate
        self.duration_seconds = duration_seconds

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
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.requests is not None:
            result['requests'] = self.requests.to_dict()
        if self.requests_per_second is not None:
            result['requestsPerSecond'] = self.requests_per_second.to_dict()
        if self.errors is not None:
            result['errors'] = self.errors.to_dict()
        if self.error_rate is not None:
            result['errorRate'] = self.error_rate.to_dict()
        if self.duration_seconds is not None:
            result['durationSeconds'] = self.duration_seconds.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ServiceMetric

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('requests') is not None:
            self.requests = MetricValue().from_dict(m.get('requests'))
        if m.get('requestsPerSecond') is not None:
            self.requests_per_second = MetricValue().from_dict(m.get('requestsPerSecond'))
        if m.get('errors') is not None:
            self.errors = MetricValue().from_dict(m.get('errors'))
        if m.get('errorRate') is not None:
            self.error_rate = MetricValue().from_dict(m.get('errorRate'))
        if m.get('durationSeconds') is not None:
            self.duration_seconds = MetricValue().from_dict(m.get('durationSeconds'))
        return self
