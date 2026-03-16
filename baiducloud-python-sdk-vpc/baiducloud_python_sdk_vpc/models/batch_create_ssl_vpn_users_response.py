"""
This module provides the BatchCreateSslVpnUsersResponse class for handling SSL VPN user creation responses.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class BatchCreateSslVpnUsersResponse(BceResponse):
    """
    Represents a response for batch creating SSL VPN users.

    Attributes:
        ssl_vpn_user_ids (list): List of created SSL VPN user IDs.
    """
    
    def __init__(self, ssl_vpn_user_ids=None):
        """
        Initializes the BatchCreateSslVpnUsersResponse instance.

        Args:
            ssl_vpn_user_ids (list, optional): List of SSL VPN user IDs. Defaults to None.
        """
        super().__init__()
        self.ssl_vpn_user_ids = ssl_vpn_user_ids

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
        if self.ssl_vpn_user_ids is not None:
            result['sslVpnUserIds'] = self.ssl_vpn_user_ids
        return result

    def from_dict(self, m):
        """
        Populates the response object from a dictionary.

        Args:
            m (dict): A dictionary containing the response data.

        Returns:
            BatchCreateSslVpnUsersResponse: The populated response object.
        """
        m = m or dict()
        if m.get('sslVpnUserIds') is not None:
            self.ssl_vpn_user_ids = m.get('sslVpnUserIds')
        return self