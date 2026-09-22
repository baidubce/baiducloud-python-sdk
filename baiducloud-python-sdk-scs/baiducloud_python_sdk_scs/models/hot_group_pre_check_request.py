"""
Request entity for HotGroupPreCheckRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.leader import Leader
from baiducloud_python_sdk_scs.models.followers_item import FollowersItem


class HotGroupPreCheckRequest(AbstractModel):
    """
    Request entity for HotGroupPreCheckRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, leader, followers=None):
        """
        Initialize HotGroupPreCheckRequest request entity.

        :param leader: leader parameter
        :type leader: Leader (required)

        :param followers: 从角色信息
        :type followers: List[FollowersItem] (optional)
        """
        super().__init__()
        self.leader = leader
        self.followers = followers

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
        if self.leader is not None:
            result['leader'] = self.leader.to_dict()
        if self.followers is not None:
            result['followers'] = [i.to_dict() for i in self.followers]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HotGroupPreCheckRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('leader') is not None:
            self.leader = Leader().from_dict(m.get('leader'))
        if m.get('followers') is not None:
            self.followers = [FollowersItem().from_dict(i) for i in m.get('followers')]
        return self
