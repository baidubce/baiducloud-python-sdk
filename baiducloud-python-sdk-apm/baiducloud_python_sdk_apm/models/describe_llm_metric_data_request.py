"""
Request entity for DescribeLLMMetricDataRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.metric_query import MetricQuery
from baiducloud_python_sdk_apm.models.filter import Filter


class DescribeLLMMetricDataRequest(AbstractModel):
    """
    Request entity for DescribeLLMMetricDataRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        begin_datetime,
        end_datetime,
        metrics,
        filters=None,
        group_by=None,
        order_by=None,
        order=None,
        limit=None,
        period_seconds=None,
        aggregate=None,
    ):
        """
        Initialize DescribeLLMMetricDataRequest request entity.

        :param begin_datetime: 开始时间，UTC时间
        :type begin_datetime: str (required)

        :param end_datetime: 结束时间，UTC时间
        :type end_datetime: str (required)

        :param metrics: metrics parameter
        :type metrics: List[MetricQuery] (required)

        :param filters: 过滤项列表
        :type filters: List[Filter] (optional)

        :param group_by: GroupBy维度列表
        :type group_by: List[str] (optional)

        :param order_by: 排序字段
        :type order_by: str (optional)

        :param order: 排序方向，可选值：asc(升序)、desc(降序)
        :type order: str (optional)

        :param limit: 返回数量限制，若未设置则返回尽可能多的数据
        :type limit: int (optional)

        :param period_seconds: 按时间聚合周期（秒），默认值0。若为0或未设置，表示从起止时间只计算一个聚合点
        :type period_seconds: int (optional)

        :param aggregate: 返回聚合值，可选项：sum(求和)、sumPerSecond(求和后计算每秒平均值)
        :type aggregate: List[str] (optional)
        """
        super().__init__()
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime
        self.metrics = metrics
        self.filters = filters
        self.group_by = group_by
        self.order_by = order_by
        self.order = order
        self.limit = limit
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
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.order is not None:
            result['order'] = self.order
        if self.limit is not None:
            result['limit'] = self.limit
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
        :rtype: DescribeLLMMetricDataRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        if m.get('metrics') is not None:
            self.metrics = [MetricQuery().from_dict(i) for i in m.get('metrics')]
        if m.get('filters') is not None:
            self.filters = [Filter().from_dict(i) for i in m.get('filters')]
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        if m.get('aggregate') is not None:
            self.aggregate = m.get('aggregate')
        return self
