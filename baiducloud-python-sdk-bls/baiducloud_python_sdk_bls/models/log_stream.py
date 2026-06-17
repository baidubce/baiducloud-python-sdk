"""
LogStream information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LogStream(AbstractModel):
    """
    LogStream
    """

    def __init__(self, creation_date_time=None, log_stream_name=None):
        """
        Initialize LogStream instance.

        :param creation_date_time: 日志流创建的时间
        :type creation_date_time: datetime (optional)

        :param log_stream_name: 日志流名称
        :type log_stream_name: str (optional)
        """
        super().__init__()
        self.creation_date_time = creation_date_time
        self.log_stream_name = log_stream_name

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
        if self.creation_date_time is not None:
            result['creationDateTime'] = self.creation_date_time
        if self.log_stream_name is not None:
            result['logStreamName'] = self.log_stream_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogStream

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('creationDateTime') is not None:
            self.creation_date_time = m.get('creationDateTime')
        if m.get('logStreamName') is not None:
            self.log_stream_name = m.get('logStreamName')
        return self
