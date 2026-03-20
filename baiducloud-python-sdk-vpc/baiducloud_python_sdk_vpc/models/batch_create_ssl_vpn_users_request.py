"""
Request entity for BatchCreateSslVpnUsersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.ssl_vpn_user import SslVpnUser


class BatchCreateSslVpnUsersRequest(AbstractModel):
    """
    Request entity for BatchCreateSslVpnUsersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpn_id, ssl_vpn_users, client_token=None):
        """
        Initialize BatchCreateSslVpnUsersRequest request entity.

        :param vpn_id: vpn_id parameter
        :type vpn_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ssl_vpn_users: SSL-VPN用户列表
        :type ssl_vpn_users: List[SslVpnUser] (required)
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.client_token = client_token
        self.ssl_vpn_users = ssl_vpn_users

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
        if self.ssl_vpn_users is not None:
            result['sslVpnUsers'] = [i.to_dict() for i in self.ssl_vpn_users]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchCreateSslVpnUsersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('sslVpnUsers') is not None:
            self.ssl_vpn_users = [SslVpnUser().from_dict(i) for i in m.get('sslVpnUsers')]
        return self
