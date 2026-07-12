"""
Log information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Log(AbstractModel):
    """
    Log
    """

    def __init__(self, timestamp=None, level=None, msg=None, tags=None):
        """
        Initialize Log instance.

        :param timestamp: 时间戳，精确到毫秒，如：2022-01-18 13:30:00.000
        :type timestamp: str (optional)

        :param level: 日志等级
        :type level: str (optional)

        :param msg: 日志内容
        :type msg: str (optional)

        :param tags: 日志标签键值对
        :type tags: object (optional)
        """
        super().__init__()
        self.timestamp = timestamp
        self.level = level
        self.msg = msg
        self.tags = tags

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
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.level is not None:
            result['level'] = self.level
        if self.msg is not None:
            result['msg'] = self.msg
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Log

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self
