"""
Request entity for ListRolesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_iam.models.role_model import RoleModel


class ListRolesResponse(BceResponse):
    """
    ListRolesResponse
    """

    def __init__(self, roles=None):
        """
        Initialize ListRolesResponse response.

        :param roles: 角色对象的列表
        :type roles: List[RoleModel] (optional)
        """
        super().__init__()
        self.roles = roles

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
        if self.roles is not None:
            result['roles'] = [i.to_dict() for i in self.roles]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListRolesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('roles') is not None:
            self.roles = [RoleModel().from_dict(i) for i in m.get('roles')]
        return self
