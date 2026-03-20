"""
SslVpnUserVo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SslVpnUserVo(AbstractModel):
    """
    SslVpnUserVo
    """

    def __init__(self, client_name=None, user_name=None, user_id=None, description=None):
        """
        Initialize SslVpnUserVo instance.

        :param client_name: 客户端名称
        :type client_name: str (optional)

        :param user_name: 用户名
        :type user_name: str (optional)

        :param user_id: 用户ID
        :type user_id: str (optional)

        :param description: 描述
        :type description: str (optional)
        """
        super().__init__()
        self.client_name = client_name
        self.user_name = user_name
        self.user_id = user_id
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
        if self.client_name is not None:
            result['clientName'] = self.client_name
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.user_id is not None:
            result['userId'] = self.user_id
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
        :rtype: SslVpnUserVo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientName') is not None:
            self.client_name = m.get('clientName')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
