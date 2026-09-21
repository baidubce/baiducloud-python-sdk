"""
SlowLogTrend information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SlowLogTrend(AbstractModel):
    """
    SlowLogTrend
    """

    def __init__(self, value=None, timestamp=None):
        """
        Initialize SlowLogTrend instance.

        :param value: 慢日志数量
        :type value: int (optional)

        :param timestamp: 时间点
        :type timestamp: datetime (optional)
        """
        super().__init__()
        self.value = value
        self.timestamp = timestamp

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
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SlowLogTrend

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self
