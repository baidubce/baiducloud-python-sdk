"""
AlarmCondition information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcm.models.metric_dimension import MetricDimension


class AlarmCondition(AbstractModel):
    """
    AlarmCondition
    """

    def __init__(
        self,
        metric_name=None,
        metric_dimensions=None,
        operator=None,
        threshold=None,
        aggregate_type=None,
        window_seconds=None,
        display_unit=None,
        display_threshold=None,
    ):
        """
        Initialize AlarmCondition instance.

        :param metric_name: 指标名称
        :type metric_name: str (optional)

        :param metric_dimensions: 指标维度筛选条件
        :type metric_dimensions: List[MetricDimension] (optional)

        :param operator: operator attribute
        :type operator: str (optional)

        :param threshold: 报警阈值
        :type threshold: float (optional)

        :param aggregate_type: 聚合方式，可选值：MAX / MIN / SUM / AVG
        :type aggregate_type: str (optional)

        :param window_seconds: 聚合窗口时间，单位：秒，取值范围：大于0
        :type window_seconds: int (optional)

        :param display_unit: 回显单位
        :type display_unit: str (optional)

        :param display_threshold: 回显阈值
        :type display_threshold: str (optional)
        """
        super().__init__()
        self.metric_name = metric_name
        self.metric_dimensions = metric_dimensions
        self.operator = operator
        self.threshold = threshold
        self.aggregate_type = aggregate_type
        self.window_seconds = window_seconds
        self.display_unit = display_unit
        self.display_threshold = display_threshold

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
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.metric_dimensions is not None:
            result['metricDimensions'] = [i.to_dict() for i in self.metric_dimensions]
        if self.operator is not None:
            result['operator'] = self.operator
        if self.threshold is not None:
            result['threshold'] = self.threshold
        if self.aggregate_type is not None:
            result['aggregateType'] = self.aggregate_type
        if self.window_seconds is not None:
            result['windowSeconds'] = self.window_seconds
        if self.display_unit is not None:
            result['displayUnit'] = self.display_unit
        if self.display_threshold is not None:
            result['displayThreshold'] = self.display_threshold
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlarmCondition

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('metricDimensions') is not None:
            self.metric_dimensions = [MetricDimension().from_dict(i) for i in m.get('metricDimensions')]
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        if m.get('aggregateType') is not None:
            self.aggregate_type = m.get('aggregateType')
        if m.get('windowSeconds') is not None:
            self.window_seconds = m.get('windowSeconds')
        if m.get('displayUnit') is not None:
            self.display_unit = m.get('displayUnit')
        if m.get('displayThreshold') is not None:
            self.display_threshold = m.get('displayThreshold')
        return self
