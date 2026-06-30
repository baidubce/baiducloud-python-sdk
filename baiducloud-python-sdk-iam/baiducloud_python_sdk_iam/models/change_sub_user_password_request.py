"""
Request entity for ChangeSubUserPasswordRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ChangeSubUserPasswordRequest(AbstractModel):
    """
    Request entity for ChangeSubUserPasswordRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_name, password=None):
        """
        Initialize ChangeSubUserPasswordRequest request entity.

        :param user_name: user_name parameter
        :type user_name: str (required)

        :param password: 更新后的密码
        :type password: str (optional)
        """
        super().__init__()
        self.user_name = user_name
        self.password = password

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
        if self.password is not None:
            result['password'] = self.password
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ChangeSubUserPasswordRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('password') is not None:
            self.password = m.get('password')
        return self
