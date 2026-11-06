"""
OpenapiSlowlog information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class OpenapiSlowlog(AbstractModel):
    """
    OpenapiSlowlog
    """

    def __init__(self, slowlog_id=None, slowlog_size_in_bytes=None, slowlog_start_time=None, slowlog_end_time=None):
        """
        Initialize OpenapiSlowlog instance.

        :param slowlog_id: 慢日志ID
        :type slowlog_id: str (optional)

        :param slowlog_size_in_bytes: 慢日志大小
        :type slowlog_size_in_bytes: int (optional)

        :param slowlog_start_time: 慢日志开始时间
        :type slowlog_start_time: str (optional)

        :param slowlog_end_time: 慢日志结束时间
        :type slowlog_end_time: str (optional)
        """
        super().__init__()
        self.slowlog_id = slowlog_id
        self.slowlog_size_in_bytes = slowlog_size_in_bytes
        self.slowlog_start_time = slowlog_start_time
        self.slowlog_end_time = slowlog_end_time

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
        if self.slowlog_id is not None:
            result['slowlogId'] = self.slowlog_id
        if self.slowlog_size_in_bytes is not None:
            result['slowlogSizeInBytes'] = self.slowlog_size_in_bytes
        if self.slowlog_start_time is not None:
            result['slowlogStartTime'] = self.slowlog_start_time
        if self.slowlog_end_time is not None:
            result['slowlogEndTime'] = self.slowlog_end_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OpenapiSlowlog

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('slowlogId') is not None:
            self.slowlog_id = m.get('slowlogId')
        if m.get('slowlogSizeInBytes') is not None:
            self.slowlog_size_in_bytes = m.get('slowlogSizeInBytes')
        if m.get('slowlogStartTime') is not None:
            self.slowlog_start_time = m.get('slowlogStartTime')
        if m.get('slowlogEndTime') is not None:
            self.slowlog_end_time = m.get('slowlogEndTime')
        return self
