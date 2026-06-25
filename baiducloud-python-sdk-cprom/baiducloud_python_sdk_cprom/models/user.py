"""
User information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class User(AbstractModel):
    """
    User
    """

    def __init__(self, user_id=None, user_name=None, user_type=None, phone_number=None, email=None):
        """
        Initialize User instance.

        :param user_id: 用户ID
        :type user_id: str (optional)

        :param user_name: 用户名称
        :type user_name: str (optional)

        :param user_type: 用户类型, 默认identity
        :type user_type: str (optional)

        :param phone_number: 用户手机号码
        :type phone_number: str (optional)

        :param email: 用户邮箱
        :type email: str (optional)
        """
        super().__init__()
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type
        self.phone_number = phone_number
        self.email = email

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
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.user_type is not None:
            result['userType'] = self.user_type
        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number
        if self.email is not None:
            result['email'] = self.email
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: User

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('userType') is not None:
            self.user_type = m.get('userType')
        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')
        if m.get('email') is not None:
            self.email = m.get('email')
        return self
