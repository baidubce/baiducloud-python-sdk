"""
Request entity for LogDetailsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class LogDetailsResponse(BceResponse):
    """
    LogDetailsResponse
    """

    def __init__(self, log_id=None, download_url=None, download_expire=None):
        """
        Initialize LogDetailsResponse response.

        :param log_id: 日志ID
        :type log_id: str (optional)

        :param download_url: 日志下载链接
        :type download_url: str (optional)

        :param download_expire: 下载链接到期时间
        :type download_expire: str (optional)
        """
        super().__init__()
        self.log_id = log_id
        self.download_url = download_url
        self.download_expire = download_expire

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.log_id is not None:
            result['logId'] = self.log_id
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.download_expire is not None:
            result['downloadExpire'] = self.download_expire
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LogDetailsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logId') is not None:
            self.log_id = m.get('logId')
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('downloadExpire') is not None:
            self.download_expire = m.get('downloadExpire')
        return self
