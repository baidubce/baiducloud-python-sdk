"""
UserGetResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_face.models.user_get_user_info import UserGetUserInfo


class UserGetResult(AbstractModel):
    """
    UserGetResult
    """

    def __init__(self, user_list=None):
        """
        Initialize UserGetResult instance.

        :param user_list: 用户信息列表
        :type user_list: List[UserGetUserInfo] (optional)
        """
        super().__init__()
        self.user_list = user_list

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
        if self.user_list is not None:
            result['user_list'] = [i.to_dict() for i in self.user_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UserGetResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('user_list') is not None:
            self.user_list = [UserGetUserInfo().from_dict(i) for i in m.get('user_list')]
        return self
