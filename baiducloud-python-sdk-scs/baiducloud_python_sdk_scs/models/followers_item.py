"""
FollowersItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FollowersItem(AbstractModel):
    """
    FollowersItem
    """

    def __init__(self, follower_id=None, follower_region=None):
        """
        Initialize FollowersItem instance.

        :param follower_id: 从角色实例ID
        :type follower_id: str (optional)

        :param follower_region: 从角色实例所在地域
        :type follower_region: str (optional)
        """
        super().__init__()
        self.follower_id = follower_id
        self.follower_region = follower_region

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
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
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FollowersItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('followerId') is not None:
            self.follower_id = m.get('followerId')
        if m.get('followerRegion') is not None:
            self.follower_region = m.get('followerRegion')
        return self
