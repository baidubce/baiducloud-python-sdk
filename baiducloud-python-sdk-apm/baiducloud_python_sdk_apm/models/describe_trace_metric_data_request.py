"""
Request entity for DescribeTraceMetricDataRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.trace_metric_query import TraceMetricQuery
from baiducloud_python_sdk_apm.models.filter import Filter


class DescribeTraceMetricDataRequest(AbstractModel):
    """
    Request entity for DescribeTraceMetricDataRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        action,
        begin_datetime,
        end_datetime,
        metrics,
        metrics_name,
        filters=None,
        group_by=None,
        period_seconds=None,
        aggregate=None,
    ):
        """
        Initialize DescribeTraceMetricDataRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param begin_datetime: 开始时间，UTC时间
        :type begin_datetime: str (required)

        :param end_datetime: 结束时间，UTC时间
        :type end_datetime: str (required)

        :param metrics: metrics parameter
        :type metrics: List[TraceMetricQuery] (required)

        :param metrics_name: 指标名
        :type metrics_name: str (required)

        :param filters: 过滤项列表
        :type filters: List[Filter] (optional)

        :param group_by: group_by parameter
        :type group_by: List[str] (optional)

        :param period_seconds: period_seconds parameter
        :type period_seconds: int (optional)

        :param aggregate: 返回聚合值。可选项：sum（求和）、sumPerSecond（求和后计算每秒平均值）
        :type aggregate: List[str] (optional)
        """
        super().__init__()
        self.action = action
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime
        self.metrics = metrics
        self.metrics_name = metrics_name
        self.filters = filters
        self.group_by = group_by
        self.period_seconds = period_seconds
        self.aggregate = aggregate

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
        if self.metrics is not None:
            result['metrics'] = [i.to_dict() for i in self.metrics]
        if self.metrics_name is not None:
            result['metrics.name'] = self.metrics_name
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        if self.aggregate is not None:
            result['aggregate'] = self.aggregate
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeTraceMetricDataRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        if m.get('metrics') is not None:
            self.metrics = [TraceMetricQuery().from_dict(i) for i in m.get('metrics')]
        if m.get('metrics.name') is not None:
            self.metrics_name = m.get('metrics.name')
        if m.get('filters') is not None:
            self.filters = [Filter().from_dict(i) for i in m.get('filters')]
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        if m.get('aggregate') is not None:
            self.aggregate = m.get('aggregate')
        return self
