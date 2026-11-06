"""
PgLogResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class PgLogResponse(BceResponse):
    """
    PgLogResponse
    """

    def __init__(self, pglog_id=None, pglog_size_in_bytes=None, pglog_start_time=None, pglog_end_time=None):
        """
        Initialize PgLogResponse instance.

        :param pglog_id: 日志id。
        :type pglog_id: str (optional)

        :param pglog_size_in_bytes: 日志大小。
        :type pglog_size_in_bytes: int (optional)

        :param pglog_start_time: 日志开始时间。
        :type pglog_start_time: str (optional)

        :param pglog_end_time: 日志结束时间。
        :type pglog_end_time: str (optional)
        """
        super().__init__()
        self.pglog_id = pglog_id
        self.pglog_size_in_bytes = pglog_size_in_bytes
        self.pglog_start_time = pglog_start_time
        self.pglog_end_time = pglog_end_time

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.pglog_id is not None:
            result['pglogId'] = self.pglog_id
        if self.pglog_size_in_bytes is not None:
            result['pglogSizeInBytes'] = self.pglog_size_in_bytes
        if self.pglog_start_time is not None:
            result['pglogStartTime'] = self.pglog_start_time
        if self.pglog_end_time is not None:
            result['pglogEndTime'] = self.pglog_end_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PgLogResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pglogId') is not None:
            self.pglog_id = m.get('pglogId')
        if m.get('pglogSizeInBytes') is not None:
            self.pglog_size_in_bytes = m.get('pglogSizeInBytes')
        if m.get('pglogStartTime') is not None:
            self.pglog_start_time = m.get('pglogStartTime')
        if m.get('pglogEndTime') is not None:
            self.pglog_end_time = m.get('pglogEndTime')
        return self
