"""
Request entity for SlowLogDownloadDetailsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class SlowLogDownloadDetailsResponse(BceResponse):
    """
    SlowLogDownloadDetailsResponse
    """

    def __init__(self, url=None, download_expires=None, data_backup_type=None):
        """
        Initialize SlowLogDownloadDetailsResponse response.

        :param url: 下载URL
        :type url: str (optional)

        :param download_expires: 下载链接有效时间
        :type download_expires: str (optional)

        :param data_backup_type: 备份类型，支持physical/snapshot
        :type data_backup_type: str (optional)
        """
        super().__init__()
        self.url = url
        self.download_expires = download_expires
        self.data_backup_type = data_backup_type

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
        if self.url is not None:
            result['URL'] = self.url
        if self.download_expires is not None:
            result['downloadExpires'] = self.download_expires
        if self.data_backup_type is not None:
            result['dataBackupType'] = self.data_backup_type
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SlowLogDownloadDetailsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('downloadExpires') is not None:
            self.download_expires = m.get('downloadExpires')
        if m.get('dataBackupType') is not None:
            self.data_backup_type = m.get('dataBackupType')
        return self
