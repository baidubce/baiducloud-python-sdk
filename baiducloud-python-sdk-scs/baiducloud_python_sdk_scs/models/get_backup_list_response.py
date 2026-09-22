"""
Request entity for GetBackupListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.batch_backup_record import BatchBackupRecord


class GetBackupListResponse(BceResponse):
    """
    GetBackupListResponse
    """

    def __init__(self, total_count=None, backups=None):
        """
        Initialize GetBackupListResponse response.

        :param total_count: 总数量。
        :type total_count: int (optional)

        :param backups: 结果列表。
        :type backups: List[BatchBackupRecord] (optional)
        """
        super().__init__()
        self.total_count = total_count
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
        if self.total_count is not None:
            result['totalCount'] = self.total_count
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
        :rtype: GetBackupListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('backups') is not None:
            self.backups = [BatchBackupRecord().from_dict(i) for i in m.get('backups')]
        return self
