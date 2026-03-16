from baiducloud_python_sdk_core.bce_response import BceResponse


class QuerySslVpnServerResponse(BceResponse):
    """
    QuerySslVpnServerResponse class is used to encapsulate the response data of SSL VPN server query.
    
    Attributes:
        vpn_id (str): The ID of the VPN.
        ssl_vpn_server_id (str): The ID of the SSL VPN server.
        ssl_vpn_server_name (str): The name of the SSL VPN server.
        interface_type (str): The type of the interface.
        status (str): The status of the SSL VPN server.
        local_subnets (list): The list of local subnets.
        remote_subnet (str): The remote subnet.
        client_dns (list): The list of client DNS servers.
        max_connection (int): The maximum number of connections.
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
        """Convert the response object to a dictionary.
        
        Returns:
            dict: A dictionary containing all the attributes of the response object.
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
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
        """Populate the response object from a dictionary.
        
        Args:
            m (dict): A dictionary containing the response data.
            
        Returns:
            QuerySslVpnServerResponse: The populated response object.
        """
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