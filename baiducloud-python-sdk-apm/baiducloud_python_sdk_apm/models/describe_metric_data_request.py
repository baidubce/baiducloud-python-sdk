"""
Request entity for DescribeMetricDataRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.metric_query import MetricQuery
from baiducloud_python_sdk_apm.models.filter import Filter
from baiducloud_python_sdk_apm.models.filter import Filter


class DescribeMetricDataRequest(AbstractModel):
    """
    Request entity for DescribeMetricDataRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        action,
        metrics,
        metrics_name,
        begin_datetime,
        end_datetime,
        metrics_compare_to=None,
        metrics_filters=None,
        filters=None,
        group_by=None,
        order_by=None,
        order=None,
        limit=None,
        period_seconds=None,
        reserve_empty_dimensions=None,
    ):
        """
        Initialize DescribeMetricDataRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param metrics: 指标名列表
        :type metrics: List[MetricQuery] (required)

        :param metrics_name: 指标名
        :type metrics_name: str (required)

        :param metrics_compare_to: metrics_compare_to parameter
        :type metrics_compare_to: List[str] (optional)

        :param metrics_filters: 该指标的特殊过滤条件，会与全局过滤项列表进行合并
        :type metrics_filters: List[Filter] (optional)

        :param begin_datetime: 开始时间，UTC时间
        :type begin_datetime: str (required)

        :param end_datetime: 结束时间，UTC时间
        :type end_datetime: str (required)

        :param filters: 过滤项列表，所有指标共享
        :type filters: List[Filter] (optional)

        :param group_by: GroupBy列表
        :type group_by: List[str] (optional)

        :param order_by: 排序字段
        :type order_by: str (optional)

        :param order: 排序方式，可选值：asc、desc
        :type order: str (optional)

        :param limit: 返回数量限制，若未设置，后端服务将返回尽可能多的数据
        :type limit: int (optional)

        :param period_seconds: period_seconds parameter
        :type period_seconds: int (optional)

        :param reserve_empty_dimensions: 当dimensions为空时，是否保留对应的时间序列。默认值：false
        :type reserve_empty_dimensions: bool (optional)
        """
        super().__init__()
        self.action = action
        self.metrics = metrics
        self.metrics_name = metrics_name
        self.metrics_compare_to = metrics_compare_to
        self.metrics_filters = metrics_filters
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime
        self.filters = filters
        self.group_by = group_by
        self.order_by = order_by
        self.order = order
        self.limit = limit
        self.period_seconds = period_seconds
        self.reserve_empty_dimensions = reserve_empty_dimensions

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
        if self.metrics is not None:
            result['metrics'] = [i.to_dict() for i in self.metrics]
        if self.metrics_name is not None:
            result['metrics.name'] = self.metrics_name
        if self.metrics_compare_to is not None:
            result['metrics.compareTo'] = self.metrics_compare_to
        if self.metrics_filters is not None:
            result['metrics.filters'] = [i.to_dict() for i in self.metrics_filters]
        if self.begin_datetime is not None:
            result['beginDatetime'] = self.begin_datetime
        if self.end_datetime is not None:
            result['endDatetime'] = self.end_datetime
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
        if self.reserve_empty_dimensions is not None:
            result['reserveEmptyDimensions'] = self.reserve_empty_dimensions
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeMetricDataRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('metrics') is not None:
            self.metrics = [MetricQuery().from_dict(i) for i in m.get('metrics')]
        if m.get('metrics.name') is not None:
            self.metrics_name = m.get('metrics.name')
        if m.get('metrics.compareTo') is not None:
            self.metrics_compare_to = m.get('metrics.compareTo')
        if m.get('metrics.filters') is not None:
            self.metrics_filters = [Filter().from_dict(i) for i in m.get('metrics.filters')]
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
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
        if m.get('reserveEmptyDimensions') is not None:
            self.reserve_empty_dimensions = m.get('reserveEmptyDimensions')
        return self
