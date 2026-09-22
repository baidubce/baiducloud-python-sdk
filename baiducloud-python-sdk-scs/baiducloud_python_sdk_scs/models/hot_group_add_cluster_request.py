"""
Request entity for HotGroupAddClusterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HotGroupAddClusterRequest(AbstractModel):
    """
    Request entity for HotGroupAddClusterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, follower_id, follower_region, sync_master):
        """
        Initialize HotGroupAddClusterRequest request entity.

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param follower_id: 从角色集群ID
        :type follower_id: str (required)

        :param follower_region: 从角色集群所在地域
        :type follower_region: str (required)

        :param sync_master: 是否同步主角色的参数（sync: 同步主角色参数， nosync：不同步主角色参数）
        :type sync_master: str (required)
        """
        super().__init__()
        self.group_id = group_id
        self.follower_id = follower_id
        self.follower_region = follower_region
        self.sync_master = sync_master

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
        if self.follower_region is not None:
            result['followerRegion'] = self.follower_region
        if self.sync_master is not None:
            result['syncMaster'] = self.sync_master
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HotGroupAddClusterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('followerId') is not None:
            self.follower_id = m.get('followerId')
        if m.get('followerRegion') is not None:
            self.follower_region = m.get('followerRegion')
        if m.get('syncMaster') is not None:
            self.sync_master = m.get('syncMaster')
        return self
