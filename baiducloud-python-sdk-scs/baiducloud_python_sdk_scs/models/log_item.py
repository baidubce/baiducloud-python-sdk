"""
LogItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LogItem(AbstractModel):
    """
    LogItem
    """

    def __init__(
        self,
        log_id=None,
        log_size_in_bytes=None,
        log_start_time=None,
        log_end_time=None,
        download_url=None,
        download_expires=None,
    ):
        """
        Initialize LogItem instance.

        :param log_id: 日志记录ID
        :type log_id: str (optional)

        :param log_size_in_bytes: 日志文件大小(单位为字节)
        :type log_size_in_bytes: int (optional)

        :param log_start_time: 日志起始时间点
        :type log_start_time: str (optional)

        :param log_end_time: 日志结束时间点
        :type log_end_time: str (optional)

        :param download_url: 日志下载链接
        :type download_url: str (optional)

        :param download_expires: 下载链接到期时间
        :type download_expires: str (optional)
        """
        super().__init__()
        self.log_id = log_id
        self.log_size_in_bytes = log_size_in_bytes
        self.log_start_time = log_start_time
        self.log_end_time = log_end_time
        self.download_url = download_url
        self.download_expires = download_expires

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
        if self.log_id is not None:
            result['logId'] = self.log_id
        if self.log_size_in_bytes is not None:
            result['logSizeInBytes'] = self.log_size_in_bytes
        if self.log_start_time is not None:
            result['logStartTime'] = self.log_start_time
        if self.log_end_time is not None:
            result['logEndTime'] = self.log_end_time
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.download_expires is not None:
            result['downloadExpires'] = self.download_expires
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logId') is not None:
            self.log_id = m.get('logId')
        if m.get('logSizeInBytes') is not None:
            self.log_size_in_bytes = m.get('logSizeInBytes')
        if m.get('logStartTime') is not None:
            self.log_start_time = m.get('logStartTime')
        if m.get('logEndTime') is not None:
            self.log_end_time = m.get('logEndTime')
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('downloadExpires') is not None:
            self.download_expires = m.get('downloadExpires')
        return self
