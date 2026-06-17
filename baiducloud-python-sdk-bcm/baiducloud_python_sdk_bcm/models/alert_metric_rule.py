"""
AlertMetricRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AlertMetricRule(AbstractModel):
    """
    AlertMetricRule
    """

    def __init__(self, metric_name=None, operator=None, threshold=None, statistics=None, window=None):
        """
        Initialize AlertMetricRule instance.

        :param metric_name: 规则指标名
        :type metric_name: str (optional)

        :param operator: 规则比较符
        :type operator: str (optional)

        :param threshold: 规则比较阈值
        :type threshold: float (optional)

        :param statistics: 规则窗口聚合方式
        :type statistics: str (optional)

        :param window: 规则窗口大小，单位：秒
        :type window: int (optional)
        """
        super().__init__()
        self.metric_name = metric_name
        self.operator = operator
        self.threshold = threshold
        self.statistics = statistics
        self.window = window

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
        if self.operator is not None:
            result['operator'] = self.operator
        if self.threshold is not None:
            result['threshold'] = self.threshold
        if self.statistics is not None:
            result['statistics'] = self.statistics
        if self.window is not None:
            result['window'] = self.window
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlertMetricRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')
        if m.get('window') is not None:
            self.window = m.get('window')
        return self
