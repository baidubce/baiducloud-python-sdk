"""
Event information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Event(AbstractModel):
    """
    Event
    """

    def __init__(self, reason=None, message=None, first_timestamp=None, last_timestamp=None, count=None, type=None):
        """
        Initialize Event instance.

        :param reason: 原因
        :type reason: str (optional)

        :param message: 详细信息
        :type message: str (optional)

        :param first_timestamp: 首次出现时间
        :type first_timestamp: str (optional)

        :param last_timestamp: 最后出现时间
        :type last_timestamp: str (optional)

        :param count: 出现次数
        :type count: int (optional)

        :param type: 事件类型
        :type type: int (optional)
        """
        super().__init__()
        self.reason = reason
        self.message = message
        self.first_timestamp = first_timestamp
        self.last_timestamp = last_timestamp
        self.count = count
        self.type = type

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
        if self.reason is not None:
            result['reason'] = self.reason
        if self.message is not None:
            result['message'] = self.message
        if self.first_timestamp is not None:
            result['firstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['lastTimestamp'] = self.last_timestamp
        if self.count is not None:
            result['count'] = self.count
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Event

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('firstTimestamp') is not None:
            self.first_timestamp = m.get('firstTimestamp')
        if m.get('lastTimestamp') is not None:
            self.last_timestamp = m.get('lastTimestamp')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
