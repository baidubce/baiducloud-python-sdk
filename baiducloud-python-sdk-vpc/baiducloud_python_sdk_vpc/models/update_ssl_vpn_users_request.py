"""
Request entity for UpdateSslVpnUsersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateSslVpnUsersRequest(AbstractModel):
    """
    Request entity for UpdateSslVpnUsersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpn_id, user_id, client_token=None, client_name=None, password=None, description=None):
        """
        Initialize UpdateSslVpnUsersRequest request entity.

        :param vpn_id: vpn_id parameter
        :type vpn_id: str (required)

        :param user_id: user_id parameter
        :type user_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param client_name: 客户端名称
        :type client_name: str (optional)

        :param password: 密码，8～17位字符，英文、数字和符号必须同时存在，符号仅限!@#$%^*(_
        :type password: str (optional)

        :param description: 描述
        :type description: str (optional)
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.user_id = user_id
        self.client_token = client_token
        self.client_name = client_name
        self.password = password
        self.description = description

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
        if self.client_name is not None:
            result['clientName'] = self.client_name
        if self.password is not None:
            result['password'] = self.password
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateSslVpnUsersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('clientName') is not None:
            self.client_name = m.get('clientName')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
