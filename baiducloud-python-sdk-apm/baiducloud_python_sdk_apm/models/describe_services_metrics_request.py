"""
Request entity for DescribeServicesMetricsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.metric_filter import MetricFilter


class DescribeServicesMetricsRequest(AbstractModel):
    """
    Request entity for DescribeServicesMetricsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, begin_datetime, end_datetime, services, metrics=None, metric_filters=None):
        """
        Initialize DescribeServicesMetricsRequest request entity.

        :param begin_datetime: 开始时间，格式为ISO 8601
        :type begin_datetime: str (required)

        :param end_datetime: 结束时间，格式为ISO 8601
        :type end_datetime: str (required)

        :param services: 应用名列表，第一阶段查询返回的全量服务中每页需要展示的服务
        :type services: List[str] (required)

        :param metrics: metrics parameter
        :type metrics: List[str] (optional)

        :param metric_filters: 指标过滤条件
        :type metric_filters: List[MetricFilter] (optional)
        """
        super().__init__()
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime
        self.services = services
        self.metrics = metrics
        self.metric_filters = metric_filters

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.begin_datetime is not None:
            result['beginDatetime'] = self.begin_datetime
        if self.end_datetime is not None:
            result['endDatetime'] = self.end_datetime
        if self.services is not None:
            result['services'] = self.services
        if self.metrics is not None:
            result['metrics'] = self.metrics
        if self.metric_filters is not None:
            result['metricFilters'] = [i.to_dict() for i in self.metric_filters]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeServicesMetricsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        if m.get('services') is not None:
            self.services = m.get('services')
        if m.get('metrics') is not None:
            self.metrics = m.get('metrics')
        if m.get('metricFilters') is not None:
            self.metric_filters = [MetricFilter().from_dict(i) for i in m.get('metricFilters')]
        return self
