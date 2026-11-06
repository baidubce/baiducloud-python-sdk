"""
Request entity for GetPgLogDetailsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetPgLogDetailsResponse(BceResponse):
    """
    GetPgLogDetailsResponse
    """

    def __init__(
        self,
        pglog_id=None,
        pglog_size_in_bytes=None,
        pglog_start_time=None,
        pglog_end_time=None,
        download_url=None,
        download_expires=None,
    ):
        """
        Initialize GetPgLogDetailsResponse response.

        :param pglog_id: 日志ID。
        :type pglog_id: str (optional)

        :param pglog_size_in_bytes: 日志大小。
        :type pglog_size_in_bytes: int (optional)

        :param pglog_start_time: 日志开始时间。
        :type pglog_start_time: str (optional)

        :param pglog_end_time: 日志结束时间。
        :type pglog_end_time: str (optional)

        :param download_url: 日志下载链接。
        :type download_url: str (optional)

        :param download_expires: 日志下载链接有效期。
        :type download_expires: str (optional)
        """
        super().__init__()
        self.pglog_id = pglog_id
        self.pglog_size_in_bytes = pglog_size_in_bytes
        self.pglog_start_time = pglog_start_time
        self.pglog_end_time = pglog_end_time
        self.download_url = download_url
        self.download_expires = download_expires

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
        if self.pglog_id is not None:
            result['pglogId'] = self.pglog_id
        if self.pglog_size_in_bytes is not None:
            result['pglogSizeInBytes'] = self.pglog_size_in_bytes
        if self.pglog_start_time is not None:
            result['pglogStartTime'] = self.pglog_start_time
        if self.pglog_end_time is not None:
            result['pglogEndTime'] = self.pglog_end_time
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.download_expires is not None:
            result['downloadExpires'] = self.download_expires
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetPgLogDetailsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
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
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('downloadExpires') is not None:
            self.download_expires = m.get('downloadExpires')
        return self
