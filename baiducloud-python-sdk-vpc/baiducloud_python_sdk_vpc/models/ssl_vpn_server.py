
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SslVpnServer(AbstractModel):
    """
    SslVpnServer
    """
    def __init__(self, vpn_id=None, ssl_vpn_server_id=None, ssl_vpn_server_name=None, interface_type=None, status=None, local_subnets=None, remote_subnet=None, client_dns=None, max_connection=None):
        super().__init__()
        self.vpn_id = vpn_id
        self.ssl_vpn_server_id = ssl_vpn_server_id
        self.ssl_vpn_server_name = ssl_vpn_server_name
        self.interface_type = interface_type
        self.status = status
        self.local_subnets = local_subnets
        self.remote_subnet = remote_subnet
        self.client_dns = client_dns
        self.max_connection = max_connection

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.vpn_id is not None:
            result['vpnId'] = self.vpn_id
        if self.ssl_vpn_server_id is not None:
            result['sslVpnServerId'] = self.ssl_vpn_server_id
        if self.ssl_vpn_server_name is not None:
            result['sslVpnServerName'] = self.ssl_vpn_server_name
        if self.interface_type is not None:
            result['interfaceType'] = self.interface_type
        if self.status is not None:
            result['status'] = self.status
        if self.local_subnets is not None:
            result['localSubnets'] = self.local_subnets
        if self.remote_subnet is not None:
            result['remoteSubnet'] = self.remote_subnet
        if self.client_dns is not None:
            result['clientDns'] = self.client_dns
        if self.max_connection is not None:
            result['maxConnection'] = self.max_connection
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('sslVpnServerId') is not None:
            self.ssl_vpn_server_id = m.get('sslVpnServerId')
        if m.get('sslVpnServerName') is not None:
            self.ssl_vpn_server_name = m.get('sslVpnServerName')
        if m.get('interfaceType') is not None:
            self.interface_type = m.get('interfaceType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('localSubnets') is not None:
            self.local_subnets = m.get('localSubnets')
        if m.get('remoteSubnet') is not None:
            self.remote_subnet = m.get('remoteSubnet')
        if m.get('clientDns') is not None:
            self.client_dns = m.get('clientDns')
        if m.get('maxConnection') is not None:
            self.max_connection = m.get('maxConnection')
        return self
