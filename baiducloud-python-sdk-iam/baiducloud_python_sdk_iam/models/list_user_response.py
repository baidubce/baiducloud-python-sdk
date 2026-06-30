"""
ListUserResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_iam.models.user_model import UserModel


class ListUserResponse(BceResponse):
    """
    ListUserResponse
    """

    def __init__(self, users=None):
        """
        Initialize ListUserResponse instance.

        :param users: 用户对象的列表
        :type users: List[UserModel] (optional)
        """
        super().__init__()
        self.users = users

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.users is not None:
            result['users'] = [i.to_dict() for i in self.users]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListUserResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('users') is not None:
            self.users = [UserModel().from_dict(i) for i in m.get('users')]
        return self
