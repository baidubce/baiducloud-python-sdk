from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateSslVpnServerRequest(AbstractModel):
    """
    更新SSL VPN服务器请求类
    """
    
    def __init__(self, vpn_id, ssl_vpn_server_id, ssl_vpn_server_name, local_subnets, remote_subnet, client_token=None, client_dns=None):
        """
        初始化更新SSL VPN服务器请求
        
        Args:
            vpn_id (str): VPN实例ID
            ssl_vpn_server_id (str): SSL VPN服务器ID
            ssl_vpn_server_name (str): SSL VPN服务器名称
            local_subnets (list): 本地子网列表
            remote_subnet (str): 客户端远程访问子网
            client_token (str, optional): 客户端token，用于保证幂等性
            client_dns (list, optional): 客户端DNS服务器地址列表
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.ssl_vpn_server_id = ssl_vpn_server_id
        self.client_token = client_token
        self.ssl_vpn_server_name = ssl_vpn_server_name
        self.local_subnets = local_subnets
        self.remote_subnet = remote_subnet
        self.client_dns = client_dns

    def to_dict(self):
        """
        将对象转换为字典格式
        
        Returns:
            dict: 包含对象属性的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ssl_vpn_server_name is not None:
            result['sslVpnServerName'] = self.ssl_vpn_server_name
        if self.local_subnets is not None:
            result['localSubnets'] = self.local_subnets
        if self.remote_subnet is not None:
            result['remoteSubnet'] = self.remote_subnet
        if self.client_dns is not None:
            result['clientDns'] = self.client_dns
        return result


    def from_dict(self, m):
        """
        从字典初始化对象
        
        Args:
            m (dict): 包含对象属性的字典
            
        Returns:
            UpdateSslVpnServerRequest: 初始化后的对象
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('sslVpnServerId') is not None:
            self.ssl_vpn_server_id = m.get('sslVpnServerId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('sslVpnServerName') is not None:
            self.ssl_vpn_server_name = m.get('sslVpnServerName')
        if m.get('localSubnets') is not None:
            self.local_subnets = m.get('localSubnets')
        if m.get('remoteSubnet') is not None:
            self.remote_subnet = m.get('remoteSubnet')
        if m.get('clientDns') is not None:
            self.client_dns = m.get('clientDns')
        return self