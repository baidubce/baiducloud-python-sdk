"""
Metric information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Metric(AbstractModel):
    """
    Metric
    """

    def __init__(self, time=None, value=None):
        """
        Initialize Metric instance.

        :param time: 时间戳（Unix Timestamp），单位为毫秒
        :type time: str (optional)

        :param value: 监控数据的值。
        :type value: int (optional)
        """
        super().__init__()
        self.time = time
        self.value = value

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
        if self.time is not None:
            result['time'] = self.time
        if self.value is not None:
            result['value'] = self.value
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
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self
