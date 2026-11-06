"""
Binlogs information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Binlogs(AbstractModel):
    """
    Binlogs
    """

    def __init__(
        self,
        binlog_id=None,
        binlog_size_in_bytes=None,
        binlog_end_time=None,
        binlog_start_time=None,
        binlog_status=None,
        binlog_real_id=None,
    ):
        """
        Initialize Binlogs instance.

        :param binlog_id: binlogId
        :type binlog_id: str (optional)

        :param binlog_size_in_bytes: 文件大小，单位mb
        :type binlog_size_in_bytes: int (optional)

        :param binlog_end_time: binlog文件记录的开始时间
        :type binlog_end_time: str (optional)

        :param binlog_start_time: binlog文件记录的结束时间
        :type binlog_start_time: str (optional)

        :param binlog_status: binlog日志状态 available
        :type binlog_status: str (optional)

        :param binlog_real_id: 文件名
        :type binlog_real_id: str (optional)
        """
        super().__init__()
        self.binlog_id = binlog_id
        self.binlog_size_in_bytes = binlog_size_in_bytes
        self.binlog_end_time = binlog_end_time
        self.binlog_start_time = binlog_start_time
        self.binlog_status = binlog_status
        self.binlog_real_id = binlog_real_id

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
        if self.binlog_id is not None:
            result['binlogId'] = self.binlog_id
        if self.binlog_size_in_bytes is not None:
            result['binlogSizeInBytes'] = self.binlog_size_in_bytes
        if self.binlog_end_time is not None:
            result['binlogEndTime'] = self.binlog_end_time
        if self.binlog_start_time is not None:
            result['binlogStartTime'] = self.binlog_start_time
        if self.binlog_status is not None:
            result['binlogStatus'] = self.binlog_status
        if self.binlog_real_id is not None:
            result['binlogRealId'] = self.binlog_real_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Binlogs

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('binlogId') is not None:
            self.binlog_id = m.get('binlogId')
        if m.get('binlogSizeInBytes') is not None:
            self.binlog_size_in_bytes = m.get('binlogSizeInBytes')
        if m.get('binlogEndTime') is not None:
            self.binlog_end_time = m.get('binlogEndTime')
        if m.get('binlogStartTime') is not None:
            self.binlog_start_time = m.get('binlogStartTime')
        if m.get('binlogStatus') is not None:
            self.binlog_status = m.get('binlogStatus')
        if m.get('binlogRealId') is not None:
            self.binlog_real_id = m.get('binlogRealId')
        return self
