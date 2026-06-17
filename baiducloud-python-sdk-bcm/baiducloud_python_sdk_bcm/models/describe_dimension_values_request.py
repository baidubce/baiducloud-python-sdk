"""
Request entity for DescribeDimensionValuesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcm.models.filter import Filter


class DescribeDimensionValuesRequest(AbstractModel):
    """
    Request entity for DescribeDimensionValuesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        action,
        scope,
        begin_datetime,
        end_datetime,
        metric_name,
        dimension_key,
        filters,
        resource_type=None,
        region=None,
    ):
        """
        Initialize DescribeDimensionValuesRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param scope: 云产品类型，如BCE_BCC
        :type scope: str (required)

        :param resource_type: 云产品资源类型，如Instance
        :type resource_type: str (optional)

        :param region: 地域
        :type region: str (optional)

        :param begin_datetime: 开始时间，UTC时间，如 2024-10-11T10:10:10Z
        :type begin_datetime: str (required)

        :param end_datetime: 结束时间，UTC时间，如 2024-10-11T10:10:10Z
        :type end_datetime: str (required)

        :param metric_name: 指标名
        :type metric_name: str (required)

        :param dimension_key: 维度名，要查询的维度key
        :type dimension_key: str (required)

        :param filters: 过滤项列表，填入已选的指标维度值，用于级联查询
        :type filters: List[Filter] (required)
        """
        super().__init__()
        self.action = action
        self.scope = scope
        self.resource_type = resource_type
        self.region = region
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime
        self.metric_name = metric_name
        self.dimension_key = dimension_key
        self.filters = filters

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
        if self.begin_datetime is not None:
            result['beginDatetime'] = self.begin_datetime
        if self.end_datetime is not None:
            result['endDatetime'] = self.end_datetime
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.dimension_key is not None:
            result['dimensionKey'] = self.dimension_key
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeDimensionValuesRequest

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
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('dimensionKey') is not None:
            self.dimension_key = m.get('dimensionKey')
        if m.get('filters') is not None:
            self.filters = [Filter().from_dict(i) for i in m.get('filters')]
        return self
