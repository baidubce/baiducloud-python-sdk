"""
Request entity for ListSharedUserResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.shared_user import SharedUser


class ListSharedUserResponse(BceResponse):
    """
    ListSharedUserResponse
    """

    def __init__(self, users=None):
        """
        Initialize ListSharedUserResponse response.

        :param users: 返回的共享用户列表
        :type users: List[SharedUser] (optional)
        """
        super().__init__()
        self.users = users

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
        if self.users is not None:
            result['users'] = [i.to_dict() for i in self.users]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListSharedUserResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('users') is not None:
            self.users = [SharedUser().from_dict(i) for i in m.get('users')]
        return self
