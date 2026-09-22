"""
Request entity for HotGroupPreCheckResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.connection_results import ConnectionResults
from baiducloud_python_sdk_scs.models.leader_result import LeaderResult
from baiducloud_python_sdk_scs.models.follower_result import FollowerResult


class HotGroupPreCheckResponse(BceResponse):
    """
    HotGroupPreCheckResponse
    """

    def __init__(self, connection_results=None, leader_result=None, follower_result=None):
        """
        Initialize HotGroupPreCheckResponse response.

        :param connection_results: 如果存在多个实例，检查主从、从从之间的网络联通性
        :type connection_results: List[ConnectionResults] (optional)

        :param leader_result: leader_result field
        :type leader_result: LeaderResult (optional)

        :param follower_result: 从角色实例数据配置检查结果
        :type follower_result: List[FollowerResult] (optional)
        """
        super().__init__()
        self.connection_results = connection_results
        self.leader_result = leader_result
        self.follower_result = follower_result

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
        if self.connection_results is not None:
            result['connectionResults'] = [i.to_dict() for i in self.connection_results]
        if self.leader_result is not None:
            result['leaderResult'] = self.leader_result.to_dict()
        if self.follower_result is not None:
            result['followerResult'] = [i.to_dict() for i in self.follower_result]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HotGroupPreCheckResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('connectionResults') is not None:
            self.connection_results = [ConnectionResults().from_dict(i) for i in m.get('connectionResults')]
        if m.get('leaderResult') is not None:
            self.leader_result = LeaderResult().from_dict(m.get('leaderResult'))
        if m.get('followerResult') is not None:
            self.follower_result = [FollowerResult().from_dict(i) for i in m.get('followerResult')]
        return self
