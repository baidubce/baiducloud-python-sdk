"""
OpenapiErrorlog information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class OpenapiErrorlog(AbstractModel):
    """
    OpenapiErrorlog
    """

    def __init__(
        self, errorlog_id=None, errorlog_size_in_bytes=None, errorlog_start_time=None, errorlog_end_time=None
    ):
        """
        Initialize OpenapiErrorlog instance.

        :param errorlog_id: 错误日志id
        :type errorlog_id: str (optional)

        :param errorlog_size_in_bytes: 错误日志大小
        :type errorlog_size_in_bytes: int (optional)

        :param errorlog_start_time: 错误日志开始时间
        :type errorlog_start_time: str (optional)

        :param errorlog_end_time: 错误日志结束时间
        :type errorlog_end_time: str (optional)
        """
        super().__init__()
        self.errorlog_id = errorlog_id
        self.errorlog_size_in_bytes = errorlog_size_in_bytes
        self.errorlog_start_time = errorlog_start_time
        self.errorlog_end_time = errorlog_end_time

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
        if self.errorlog_id is not None:
            result['errorlogId'] = self.errorlog_id
        if self.errorlog_size_in_bytes is not None:
            result['errorlogSizeInBytes'] = self.errorlog_size_in_bytes
        if self.errorlog_start_time is not None:
            result['errorlogStartTime'] = self.errorlog_start_time
        if self.errorlog_end_time is not None:
            result['errorlogEndTime'] = self.errorlog_end_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OpenapiErrorlog

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('errorlogId') is not None:
            self.errorlog_id = m.get('errorlogId')
        if m.get('errorlogSizeInBytes') is not None:
            self.errorlog_size_in_bytes = m.get('errorlogSizeInBytes')
        if m.get('errorlogStartTime') is not None:
            self.errorlog_start_time = m.get('errorlogStartTime')
        if m.get('errorlogEndTime') is not None:
            self.errorlog_end_time = m.get('errorlogEndTime')
        return self
