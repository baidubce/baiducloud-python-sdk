from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.vpn_conn import VpnConn

class SearchVpnTunnelResponse(BceResponse):
    """
    SearchVpnTunnelResponse
    """
    def __init__(self, vpn_conns=None):
        super().__init__()
        self.vpn_conns = vpn_conns

    def to_dict(self):
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
        m = m or dict()
        if m.get('vpnConns') is not None:
            self.vpn_conns = [
            VpnConn().from_dict(i)
            for i in m.get('vpnConns')
            ]
        return self