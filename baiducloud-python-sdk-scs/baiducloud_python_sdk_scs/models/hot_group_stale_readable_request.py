"""
Request entity for HotGroupStaleReadableRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HotGroupStaleReadableRequest(AbstractModel):
    """
    Request entity for HotGroupStaleReadableRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, follower_id, stale_readable):
        """
        Initialize HotGroupStaleReadableRequest request entity.

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param follower_id: 从角色集群ID
        :type follower_id: str (required)

        :param stale_readable: 是否开启从角色脏读（true：开启，false：关闭）
        :type stale_readable: bool (required)
        """
        super().__init__()
        self.group_id = group_id
        self.follower_id = follower_id
        self.stale_readable = stale_readable

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
        if self.follower_id is not None:
            result['followerId'] = self.follower_id
        if self.stale_readable is not None:
            result['staleReadable'] = self.stale_readable
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HotGroupStaleReadableRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('followerId') is not None:
            self.follower_id = m.get('followerId')
        if m.get('staleReadable') is not None:
            self.stale_readable = m.get('staleReadable')
        return self
