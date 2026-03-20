"""
Request entity for SearchVpnTunnelResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.vpn_conn import VpnConn


class SearchVpnTunnelResponse(BceResponse):
    """
    SearchVpnTunnelResponse
    """

    def __init__(self, vpn_conns=None):
        """
        Initialize SearchVpnTunnelResponse response.

        :param vpn_conns: VPN隧道列表
        :type vpn_conns: List[VpnConn] (optional)
        """
        super().__init__()
        self.vpn_conns = vpn_conns

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
        if self.vpn_conns is not None:
            result['vpnConns'] = [i.to_dict() for i in self.vpn_conns]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SearchVpnTunnelResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpnConns') is not None:
            self.vpn_conns = [VpnConn().from_dict(i) for i in m.get('vpnConns')]
        return self
