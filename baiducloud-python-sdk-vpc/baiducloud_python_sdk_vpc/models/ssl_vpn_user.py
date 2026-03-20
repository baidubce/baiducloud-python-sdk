"""
SslVpnUser information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SslVpnUser(AbstractModel):
    """
    SslVpnUser
    """

    def __init__(self, user_name=None, password=None, description=None):
        """
        Initialize SslVpnUser instance.

        :param user_name: 用户名，大小写字母、数字以及-_/.特殊字符，必须以字母开头，长度1-65
        :type user_name: str (optional)

        :param password: 密码，8～17位字符，英文、数字和符号必须同时存在，符号仅限!@#$%^*(_
        :type password: str (optional)

        :param description: 描述
        :type description: str (optional)
        """
        super().__init__()
        self.user_name = user_name
        self.password = password
        self.description = description

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
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.password is not None:
            result['password'] = self.password
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SslVpnUser

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
