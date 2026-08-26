"""
Request entity for DescribeMetricCatalogsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcm.models.metric_filter import MetricFilter


class DescribeMetricCatalogsRequest(AbstractModel):
    """
    Request entity for DescribeMetricCatalogsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        locale,
        scope,
        resource_type,
        filters_key,
        filters_op,
        catalog=None,
        filters=None,
        filters_value=None,
        filters_values=None,
        including_dimensions=None,
        excluding_dimensions=None,
    ):
        """
        Initialize DescribeMetricCatalogsRequest request entity.

        :param locale: locale parameter
        :type locale: str (required)

        :param scope: 云产品标识，可通过DescribeResourceCatalogs接口获取，例如BCE_BCC
        :type scope: str (required)

        :param resource_type: 资源类型标识，可通过DescribeResourceCatalogs接口获取，例如Instance
        :type resource_type: str (required)

        :param catalog: 一级指标目录名称。按名称过滤目录时使用，名称匹配不区分大小写
        :type catalog: str (optional)

        :param filters: 指标属性过滤条件列表。多个条件之间为AND关系，可根据指标标签或指标维度过滤
        :type filters: List[MetricFilter] (optional)

        :param filters_key: 过滤字段名称。配置filters时必填，可填写指标标签名称或指标维度名称
        :type filters_key: str (required)

        :param filters_op: 过滤操作符，可选值：= / != / contains / in
        :type filters_op: str (required)

        :param filters_value: 单值过滤条件，用于=、!=或contains操作符。对指标维度使用空字符串时，可用于判断该维度是否存在
        :type filters_value: str (optional)

        :param filters_values: 多值过滤条件，op为in时必填，匹配任意一个值即满足当前条件
        :type filters_values: List[str] (optional)

        :param including_dimensions: 指标必须同时包含的指标维度列表
        :type including_dimensions: List[str] (optional)

        :param excluding_dimensions: 指标不能包含其中任意维度的指标维度列表
        :type excluding_dimensions: List[str] (optional)
        """
        super().__init__()
        self.locale = locale
        self.scope = scope
        self.resource_type = resource_type
        self.catalog = catalog
        self.filters = filters
        self.filters_key = filters_key
        self.filters_op = filters_op
        self.filters_value = filters_value
        self.filters_values = filters_values
        self.including_dimensions = including_dimensions
        self.excluding_dimensions = excluding_dimensions

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
        if self.catalog is not None:
            result['catalog'] = self.catalog
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.filters_key is not None:
            result['filters[].key'] = self.filters_key
        if self.filters_op is not None:
            result['filters[].op'] = self.filters_op
        if self.filters_value is not None:
            result['filters[].value'] = self.filters_value
        if self.filters_values is not None:
            result['filters[].values'] = self.filters_values
        if self.including_dimensions is not None:
            result['includingDimensions'] = self.including_dimensions
        if self.excluding_dimensions is not None:
            result['excludingDimensions'] = self.excluding_dimensions
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeMetricCatalogsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('catalog') is not None:
            self.catalog = m.get('catalog')
        if m.get('filters') is not None:
            self.filters = [MetricFilter().from_dict(i) for i in m.get('filters')]
        if m.get('filters[].key') is not None:
            self.filters_key = m.get('filters[].key')
        if m.get('filters[].op') is not None:
            self.filters_op = m.get('filters[].op')
        if m.get('filters[].value') is not None:
            self.filters_value = m.get('filters[].value')
        if m.get('filters[].values') is not None:
            self.filters_values = m.get('filters[].values')
        if m.get('includingDimensions') is not None:
            self.including_dimensions = m.get('includingDimensions')
        if m.get('excludingDimensions') is not None:
            self.excluding_dimensions = m.get('excludingDimensions')
        return self
