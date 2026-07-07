"""
Request entity for CreateUserRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateUserRequest(AbstractModel):
    """
    Request entity for CreateUserRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, user_pool_id, username, display_name=None, description=None, password=None, force_reset_password=None
    ):
        """
        Initialize CreateUserRequest request entity.

        :param user_pool_id: 用户池 ID
        :type user_pool_id: str (required)

        :param username: 用户名（1-64字符，仅允许字母、数字、`_.@-`）
        :type username: str (required)

        :param display_name: 显示名称（最多64字符）
        :type display_name: str (optional)

        :param description: 用户描述（最多128字符）
        :type description: str (optional)

        :param password: 用户密码（8-32字符）；不传则用户无密码，仅能通过 IdP 登录
        :type password: str (optional)

        :param force_reset_password: 是否强制用户首次登录时重置密码，默认 false
        :type force_reset_password: bool (optional)
        """
        super().__init__()
        self.user_pool_id = user_pool_id
        self.username = username
        self.display_name = display_name
        self.description = description
        self.password = password
        self.force_reset_password = force_reset_password

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
        if self.user_pool_id is not None:
            result['userPoolId'] = self.user_pool_id
        if self.username is not None:
            result['username'] = self.username
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.description is not None:
            result['description'] = self.description
        if self.password is not None:
            result['password'] = self.password
        if self.force_reset_password is not None:
            result['forceResetPassword'] = self.force_reset_password
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateUserRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userPoolId') is not None:
            self.user_pool_id = m.get('userPoolId')
        if m.get('username') is not None:
            self.username = m.get('username')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('forceResetPassword') is not None:
            self.force_reset_password = m.get('forceResetPassword')
        return self
