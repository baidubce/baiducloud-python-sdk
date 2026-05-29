"""
LogRecord information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LogRecord(AbstractModel):
    """
    LogRecord
    """

    def __init__(self, message=None, timestamp=None):
        """
        Initialize LogRecord instance.

        :param message: 日志内容
        :type message: str (optional)

        :param timestamp: 日志时间戳
        :type timestamp: int (optional)
        """
        super().__init__()
        self.message = message
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
        if self.message is not None:
            result['message'] = self.message
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
        :rtype: LogRecord

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self
