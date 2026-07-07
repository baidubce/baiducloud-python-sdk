"""
Request entity for ResetPasswordRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResetPasswordRequest(AbstractModel):
    """
    Request entity for ResetPasswordRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_pool_id, user_id, new_password, password=None, force_reset_password=None):
        """
        Initialize ResetPasswordRequest request entity.

        :param user_pool_id: 用户池 ID
        :type user_pool_id: str (required)

        :param user_id: 用户 ID
        :type user_id: str (required)

        :param new_password: 新密码（8-32字符，须含大写、小写、数字）
        :type new_password: str (required)

        :param password: 当前密码；传入时校验当前密码，适用于用户自行修改场景；不传则为管理员重置，跳过校验
        :type password: str (optional)

        :param force_reset_password: 是否强制用户下次登录时重置密码，默认 true
        :type force_reset_password: bool (optional)
        """
        super().__init__()
        self.user_pool_id = user_pool_id
        self.user_id = user_id
        self.new_password = new_password
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
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.new_password is not None:
            result['newPassword'] = self.new_password
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
        :rtype: ResetPasswordRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userPoolId') is not None:
            self.user_pool_id = m.get('userPoolId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('newPassword') is not None:
            self.new_password = m.get('newPassword')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('forceResetPassword') is not None:
            self.force_reset_password = m.get('forceResetPassword')
        return self
