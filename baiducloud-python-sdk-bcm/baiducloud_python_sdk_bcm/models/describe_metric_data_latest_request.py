"""
Request entity for DescribeMetricDataLatestRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcm.models.filter import Filter


class DescribeMetricDataLatestRequest(AbstractModel):
    """
    Request entity for DescribeMetricDataLatestRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        action,
        scope,
        region,
        end_datetime,
        metric_name,
        filters,
        resource_type=None,
        limit=None,
        offset=None,
        period_seconds=None,
        aggregation_over_time=None,
    ):
        """
        Initialize DescribeMetricDataLatestRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param scope: 云产品类型，如BCE_BCC
        :type scope: str (required)

        :param resource_type: resource_type parameter
        :type resource_type: str (optional)

        :param region: 地域
        :type region: str (required)

        :param end_datetime: 结束时间，UTC时间，如 2024-10-11T10:25:10Z
        :type end_datetime: str (required)

        :param metric_name: 指标名
        :type metric_name: str (required)

        :param filters: 维度过滤项列表，必须包含该资源类型下所有的Resource.Identifiers维度
        :type filters: List[Filter] (required)

        :param limit: 若查询命中多条曲线，则最多返回limit条曲线，默认值：10，最大值：100
        :type limit: int (optional)

        :param offset: 偏移量，用于翻页查询，默认值：0
        :type offset: int (optional)

        :param period_seconds: 周期，单位：秒，默认值：60
        :type period_seconds: int (optional)

        :param aggregation_over_time: aggregation_over_time parameter
        :type aggregation_over_time: List[str] (optional)
        """
        super().__init__()
        self.action = action
        self.scope = scope
        self.resource_type = resource_type
        self.region = region
        self.end_datetime = end_datetime
        self.metric_name = metric_name
        self.filters = filters
        self.limit = limit
        self.offset = offset
        self.period_seconds = period_seconds
        self.aggregation_over_time = aggregation_over_time

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
        if self.scope is not None:
            result['scope'] = self.scope
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.region is not None:
            result['region'] = self.region
        if self.end_datetime is not None:
            result['endDatetime'] = self.end_datetime
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.limit is not None:
            result['limit'] = self.limit
        if self.offset is not None:
            result['offset'] = self.offset
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        if self.aggregation_over_time is not None:
            result['aggregationOverTime'] = self.aggregation_over_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeMetricDataLatestRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('filters') is not None:
            self.filters = [Filter().from_dict(i) for i in m.get('filters')]
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        if m.get('aggregationOverTime') is not None:
            self.aggregation_over_time = m.get('aggregationOverTime')
        return self
