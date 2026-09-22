"""
Request entity for GetSyncGroupStatusResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.sync_status_item import SyncStatusItem


class GetSyncGroupStatusResponse(BceResponse):
    """
    GetSyncGroupStatusResponse
    """

    def __init__(self, sync_group_show_id=None, sync_status=None):
        """
        Initialize GetSyncGroupStatusResponse response.

        :param sync_group_show_id: 实例组ID。
        :type sync_group_show_id: str (optional)

        :param sync_status: 状态列表。
        :type sync_status: List[SyncStatusItem] (optional)
        """
        super().__init__()
        self.sync_group_show_id = sync_group_show_id
        self.sync_status = sync_status

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
        if self.sync_group_show_id is not None:
            result['syncGroupShowId'] = self.sync_group_show_id
        if self.sync_status is not None:
            result['syncStatus'] = [i.to_dict() for i in self.sync_status]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetSyncGroupStatusResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('syncGroupShowId') is not None:
            self.sync_group_show_id = m.get('syncGroupShowId')
        if m.get('syncStatus') is not None:
            self.sync_status = [SyncStatusItem().from_dict(i) for i in m.get('syncStatus')]
        return self
