"""
This module provides the CreateSslVpnServerResponse class for handling SSL VPN server creation responses.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateSslVpnServerResponse(BceResponse):
    """
    Represents a response for creating an SSL VPN server.

    Attributes:
        ssl_vpn_server_id (str): The ID of the created SSL VPN server.
    """
    
    def __init__(self, ssl_vpn_server_id=None):
        """
        Initializes the CreateSslVpnServerResponse instance.

        Args:
            ssl_vpn_server_id (str, optional): The ID of the created SSL VPN server. Defaults to None.
        """
        super().__init__()
        self.ssl_vpn_server_id = ssl_vpn_server_id

    def to_dict(self):
        """
        Converts the response object to a dictionary.

        Returns:
            dict: A dictionary containing the response data.
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
        Populates the response object from a dictionary.

        Args:
            m (dict): A dictionary containing the response data.

        Returns:
            CreateSslVpnServerResponse: The populated response object.
        """
        m = m or dict()
        if m.get('sslVpnServerId') is not None:
            self.ssl_vpn_server_id = m.get('sslVpnServerId')
        return self