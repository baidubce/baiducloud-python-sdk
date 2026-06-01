"""
MetricValue information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MetricValue(AbstractModel):
    """
    MetricValue
    """

    def __init__(self, value=None, compare_to_yesterday=None):
        """
        Initialize MetricValue instance.

        :param value: 指标当前值
        :type value: float (optional)

        :param compare_to_yesterday: 日环比，1表示100%
        :type compare_to_yesterday: float (optional)
        """
        super().__init__()
        self.value = value
        self.compare_to_yesterday = compare_to_yesterday

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
        if self.value is not None:
            result['value'] = self.value
        if self.compare_to_yesterday is not None:
            result['compareToYesterday'] = self.compare_to_yesterday
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MetricValue

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('compareToYesterday') is not None:
            self.compare_to_yesterday = m.get('compareToYesterday')
        return self
