"""
Auth information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Auth(AbstractModel):
    """
    Auth
    """

    def __init__(self, uid=None, auth=None):
        """
        Initialize Auth instance.

        :param uid: 用户id，所有人使用\"*\"
        :type uid: str (optional)

        :param auth: 鉴权方式，取值：allow/deny，分别表示允许/拒绝
        :type auth: str (optional)
        """
        super().__init__()
        self.uid = uid
        self.auth = auth

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
        if self.uid is not None:
            result['uid'] = self.uid
        if self.auth is not None:
            result['auth'] = self.auth
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Auth

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('auth') is not None:
            self.auth = m.get('auth')
        return self
