"""
UserGetUserInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UserGetUserInfo(AbstractModel):
    """
    UserGetUserInfo
    """

    def __init__(self, user_info=None, group_id=None):
        """
        Initialize UserGetUserInfo instance.

        :param user_info: 用户资料，被查询用户的资料
        :type user_info: str (optional)

        :param group_id: 用户所属的group_id，被查询用户的所在组
        :type group_id: str (optional)
        """
        super().__init__()
        self.user_info = user_info
        self.group_id = group_id

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
        if self.user_info is not None:
            result['user_info'] = self.user_info
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UserGetUserInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('user_info') is not None:
            self.user_info = m.get('user_info')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self
