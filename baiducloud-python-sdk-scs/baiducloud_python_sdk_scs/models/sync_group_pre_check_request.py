"""
Request entity for SyncGroupPreCheckRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.check_sync_group_request_member import CheckSyncGroupRequestMember


class SyncGroupPreCheckRequest(AbstractModel):
    """
    Request entity for SyncGroupPreCheckRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, sync_group_show_id=None, members=None):
        """
        Initialize SyncGroupPreCheckRequest request entity.

        :param sync_group_show_id: 多活实例组展示ID（新建校验时可不传）
        :type sync_group_show_id: str (optional)

        :param members: 成员实例列表
        :type members: List[CheckSyncGroupRequestMember] (optional)
        """
        super().__init__()
        self.sync_group_show_id = sync_group_show_id
        self.members = members

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.sync_group_show_id is not None:
            result['syncGroupShowId'] = self.sync_group_show_id
        if self.members is not None:
            result['members'] = [i.to_dict() for i in self.members]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SyncGroupPreCheckRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('syncGroupShowId') is not None:
            self.sync_group_show_id = m.get('syncGroupShowId')
        if m.get('members') is not None:
            self.members = [CheckSyncGroupRequestMember().from_dict(i) for i in m.get('members')]
        return self
