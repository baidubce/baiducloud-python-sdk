"""
Request entity for DeleteVpnTunnelRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteVpnTunnelRequest(AbstractModel):
    """
    Request entity for DeleteVpnTunnelRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpn_conn_id, client_token=None):
        """
        Initialize DeleteVpnTunnelRequest request entity.

        :param vpn_conn_id: vpn_conn_id parameter
        :type vpn_conn_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)
        """
        super().__init__()
        self.vpn_conn_id = vpn_conn_id
        self.client_token = client_token

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteVpnTunnelRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnConnId') is not None:
            self.vpn_conn_id = m.get('vpnConnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self
