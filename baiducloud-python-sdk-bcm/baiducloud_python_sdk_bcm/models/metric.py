"""
Metric information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Metric(AbstractModel):
    """
    Metric
    """

    def __init__(
        self,
        name=None,
        label=None,
        resource_identifiers=None,
        metric_dimensions=None,
        period=None,
        period_unit=None,
        unit=None,
    ):
        """
        Initialize Metric instance.

        :param name: 指标名称，可作为指标数据查询接口的metricNames参数
        :type name: str (optional)

        :param label: 指标显示名称，根据locale返回中文或英文名称
        :type label: str (optional)

        :param resource_identifiers: 资源标识维度列表。查询指标数据时，过滤条件需要包含当前资源类型要求的全部资源标识维度
        :type resource_identifiers: List[str] (optional)

        :param metric_dimensions: 除资源标识维度以外的指标维度列表，可用于进一步筛选时序数据
        :type metric_dimensions: List[str] (optional)

        :param period: 指标采集周期数值
        :type period: float (optional)

        :param period_unit: 指标采集周期单位，例如s表示秒
        :type period_unit: str (optional)

        :param unit: 指标值单位，根据locale返回中文或英文单位
        :type unit: str (optional)
        """
        super().__init__()
        self.name = name
        self.label = label
        self.resource_identifiers = resource_identifiers
        self.metric_dimensions = metric_dimensions
        self.period = period
        self.period_unit = period_unit
        self.unit = unit

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
        if self.name is not None:
            result['name'] = self.name
        if self.label is not None:
            result['label'] = self.label
        if self.resource_identifiers is not None:
            result['resourceIdentifiers'] = self.resource_identifiers
        if self.metric_dimensions is not None:
            result['metricDimensions'] = self.metric_dimensions
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['periodUnit'] = self.period_unit
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Metric

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('resourceIdentifiers') is not None:
            self.resource_identifiers = m.get('resourceIdentifiers')
        if m.get('metricDimensions') is not None:
            self.metric_dimensions = m.get('metricDimensions')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('periodUnit') is not None:
            self.period_unit = m.get('periodUnit')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self
