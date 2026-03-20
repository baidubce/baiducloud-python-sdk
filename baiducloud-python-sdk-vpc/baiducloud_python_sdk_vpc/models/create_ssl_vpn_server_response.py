"""
Request entity for CreateSslVpnServerResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateSslVpnServerResponse(BceResponse):
    """
    CreateSslVpnServerResponse
    """

    def __init__(self, ssl_vpn_server_id=None):
        """
        Initialize CreateSslVpnServerResponse response.

        :param ssl_vpn_server_id: SSL-VPN服务端唯一ID
        :type ssl_vpn_server_id: str (optional)
        """
        super().__init__()
        self.ssl_vpn_server_id = ssl_vpn_server_id

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.ssl_vpn_server_id is not None:
            result['sslVpnServerId'] = self.ssl_vpn_server_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSslVpnServerResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sslVpnServerId') is not None:
            self.ssl_vpn_server_id = m.get('sslVpnServerId')
        return self
