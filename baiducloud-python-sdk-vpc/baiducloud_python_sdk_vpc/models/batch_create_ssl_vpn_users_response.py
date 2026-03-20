"""
Request entity for BatchCreateSslVpnUsersResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class BatchCreateSslVpnUsersResponse(BceResponse):
    """
    BatchCreateSslVpnUsersResponse
    """

    def __init__(self, ssl_vpn_user_ids=None):
        """
        Initialize BatchCreateSslVpnUsersResponse response.

        :param ssl_vpn_user_ids: SSL-VPN用户ID列表
        :type ssl_vpn_user_ids: List[str] (optional)
        """
        super().__init__()
        self.ssl_vpn_user_ids = ssl_vpn_user_ids

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
        if self.ssl_vpn_user_ids is not None:
            result['sslVpnUserIds'] = self.ssl_vpn_user_ids
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchCreateSslVpnUsersResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sslVpnUserIds') is not None:
            self.ssl_vpn_user_ids = m.get('sslVpnUserIds')
        return self
