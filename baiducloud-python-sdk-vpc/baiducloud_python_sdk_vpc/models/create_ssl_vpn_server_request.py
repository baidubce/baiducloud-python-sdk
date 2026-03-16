from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateSslVpnServerRequest(AbstractModel):
    """
    创建SSL VPN服务器请求类
    """

    def __init__(self, vpn_id, ssl_vpn_server_name, local_subnets, remote_subnet, client_token=None, interface_type=None, client_dns=None):
        """
        初始化创建SSL VPN服务器请求

        :param vpn_id: VPN实例ID
        :param ssl_vpn_server_name: SSL VPN服务器名称
        :param local_subnets: 本地子网列表
        :param remote_subnet: 客户端子网
        :param client_token: 客户端token，用于保证请求的幂等性
        :param interface_type: 接口类型
        :param client_dns: 客户端DNS服务器地址
        """
        super().__init__()
        self.vpn_id = vpn_id
        self.client_token = client_token
        self.ssl_vpn_server_name = ssl_vpn_server_name
        self.interface_type = interface_type
        self.local_subnets = local_subnets
        self.remote_subnet = remote_subnet
        self.client_dns = client_dns

    def to_dict(self):
        """
        将对象转换为字典

        :return: 包含对象属性的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.ssl_vpn_server_name is not None:
            result['sslVpnServerName'] = self.ssl_vpn_server_name
        if self.interface_type is not None:
            result['interfaceType'] = self.interface_type
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

        :param m: 包含对象属性的字典
        :return: 初始化后的对象
        """
        m = m or dict()
        if m.get('vpnId') is not None:
            self.vpn_id = m.get('vpnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('sslVpnServerName') is not None:
            self.ssl_vpn_server_name = m.get('sslVpnServerName')
        if m.get('interfaceType') is not None:
            self.interface_type = m.get('interfaceType')
        if m.get('localSubnets') is not None:
            self.local_subnets = m.get('localSubnets')
        if m.get('remoteSubnet') is not None:
            self.remote_subnet = m.get('remoteSubnet')
        if m.get('clientDns') is not None:
            self.client_dns = m.get('clientDns')
        return self