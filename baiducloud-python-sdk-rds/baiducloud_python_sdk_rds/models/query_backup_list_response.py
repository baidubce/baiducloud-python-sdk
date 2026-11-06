"""
Request entity for QueryBackupListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.open_api_backup import OpenApiBackup


class QueryBackupListResponse(BceResponse):
    """
    QueryBackupListResponse
    """

    def __init__(self, marker=None, is_truncated=None, next_marker=None, backups=None):
        """
        Initialize QueryBackupListResponse response.

        :param marker: 查找的分页的backupId，默认为-1
        :type marker: str (optional)

        :param is_truncated: 是否还有下一页，如果有此选项为true，如果没有则为false
        :type is_truncated: bool (optional)

        :param next_marker: 下一页backupId值，如果有此选项不为空，没有则为空
        :type next_marker: str (optional)

        :param backups: 备份对象
        :type backups: List[OpenApiBackup] (optional)
        """
        super().__init__()
        self.marker = marker
        self.is_truncated = is_truncated
        self.next_marker = next_marker
        self.backups = backups

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
        if self.marker is not None:
            result['marker'] = self.marker
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        if self.backups is not None:
            result['backups'] = [i.to_dict() for i in self.backups]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryBackupListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        if m.get('backups') is not None:
            self.backups = [OpenApiBackup().from_dict(i) for i in m.get('backups')]
        return self
