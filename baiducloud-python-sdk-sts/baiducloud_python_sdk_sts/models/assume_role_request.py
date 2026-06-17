"""
Request entity for AssumeRoleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AssumeRoleRequest(AbstractModel):
    """
    Request entity for AssumeRoleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, account_id, role_name, duration_seconds=None, user_id=None, access_control_list=None):
        """
        Initialize AssumeRoleRequest request entity.

        :param duration_seconds: duration_seconds parameter
        :type duration_seconds: str (optional)

        :param account_id: account_id parameter
        :type account_id: str (required)

        :param user_id: user_id parameter
        :type user_id: str (optional)

        :param role_name: role_name parameter
        :type role_name: str (required)

        :param access_control_list: 为临时身份凭证绑定的权限
        :type access_control_list: str (optional)
        """
        super().__init__()
        self.duration_seconds = duration_seconds
        self.account_id = account_id
        self.user_id = user_id
        self.role_name = role_name
        self.access_control_list = access_control_list

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
        if self.access_control_list is not None:
            result['accessControlList'] = self.access_control_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AssumeRoleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('durationSeconds') is not None:
            self.duration_seconds = m.get('durationSeconds')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('accessControlList') is not None:
            self.access_control_list = m.get('accessControlList')
        return self
